"""v10 (24 Oct 2026, measure revised 16 Nov 2026): apply the README read bar to every document marked read.

The 22-23 Oct audit marked a document "read" when it built coherent sentences (about 0.60 clean sentences). The
project's read bar is stricter: 95% of the words read as sense. This pass measures read_share = 1 - (explicit holes + doubtful
words) / (words + holes), counted after v2_score.holes, (every [?word], supplied [word], {?}, part-word, unread sign and unvalued code is a hole)
for every entry whose state is read, records it in the entry, and moves entries under 0.95 to "read in part".

    python research/reading_audit/v10_relabel.py            dry run: tsv on stdout, summary on stderr
    python research/reading_audit/v10_relabel.py --apply    write the profiles

Entries with no local text to measure (external pointers, unspaced scripts, readings kept only in a table) are left
as they are and listed. Each changed profile gets one solution step. Only the touched entries are rewritten; the rest
keeps its layout.

What is measured (16 Nov 2026, README Conventions "The read share counts cipher words only"; R23 scan defects):
- The body: the entry's reading_section if declared, else the "## Reading" section, else the file without its
  apparatus. In every case sections headed Notes, Translation, English, Count, Sources, Key, Open, Clear ... are cut,
  and so are HTML comments and, in a file with no "## Reading" heading, its title and label paragraphs
  ("Conventions: ...", "Marks: ...", "Status: ..."). When most of the body's words stand on '>' lines in a few blocks,
  the blockquote is the reading and the lines around it are commentary; otherwise '>' lines are dropped (see quoted).
- Cipher words only, when declared: outcome.texts[].cipher_markup or clear_markup (profile.schema.json), or a
  <!-- measure: cipher_markup=X --> line in the reading file; '>' declares the blockquoted lines to be the cipher or
  the clear text. With cipher_markup only the marked words count, with the
  hole marks that touch them; with clear_markup the marked words go, holes and doubts inside them too. Undeclared, the
  whole body is measured and the tsv says "not split" in its split column, with the marks seen in the body, so that a
  missing declaration shows.
- Not holes: view and line markers ([v006r], [f. 12r], [image 3]), a read sign or code given with its value
  ([sign = Venetorum], **94,** [le marquis]), and, where bracket_expansions is declared, abbreviations expanded in a
  word (Ip[sis]). Supplied letters (actu[al]) stay holes.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))
import _texts, v2_score as v2
import _check_reading as cr

BAR = 0.95
NUM = re.compile(r'^\s*(?:[A-Z]?\d+[a-z]?|[A-Z]\d+\.\d+)[.:)]?\s+')
STEP_RE = re.compile(r'\n([ \t]*)\{')


# ---- the reading body ------------------------------------------------------------------------------------------
# Sections that are not the reading, whatever the file calls its reading (16 Nov 2026, R23 scan: a file with no
# "## Reading" heading was scored whole, notes, tables and translation included). A section runs to the next heading
# of the same or a higher level. Only "##" and lower headings stop: some files write their apparatus as "# ..." lines.
STOP_HEAD = re.compile(
    r'(?:\d+[.)]?\s*)?(?:notes?\b|editorial|commentary|comments?\b|apparatus|alignment|justification|counts?\b|measure|'
    r'state of the reading|what it says|summary|english|translation|traduction|traduzione|übersetzung|übersetzung|'
    r'open\b|open (?:points|items|questions)|remaining gaps|gaps\b|holes\b|sources?\b|keys?\b|glossary|references|'
    r'method|checks?\b|verification|conventions|marks\b|legend|cut from|codes?\b(?! *\d)|code list|nomenclator|variants|'
    r'collation|transcription|cipher ?text|cipher notes|decode notes|history|context|provenance|caveats?|'
    r'status\b|clear\b|en clair|in chiaro|in clear)', re.I)
HEAD = re.compile(r'^(#{1,6})\s+(.*)$')
# A paragraph of the file's own apparatus at the head of a reading with no "## Reading" heading.
LABEL_PARA = re.compile(r'^[*_]{0,2}(?:conventions?|marks|rests on|spelling|sources?|files?|key|notes?|counts?|'
                        r'legend|method|transcription|measured?|status|probable|restored)\b[^:\n]{0,40}:', re.I)
COMMENT = re.compile(r'<!--.*?-->', re.S)
DECL = re.compile(r'<!--\s*measure:(.*?)-->', re.S | re.I)


def drop_sections(body):
    """Body without the sections whose heading names notes, a translation, counts, sources and the like."""
    out, skip = [], None
    for line in body.split('\n'):
        h = HEAD.match(line)
        if h:
            lvl = len(h.group(1))
            if skip is not None and lvl <= skip: skip = None
            if skip is None and lvl >= 2 and len(h.group(2)) <= 80 and STOP_HEAD.match(h.group(2).strip(' *_')):
                skip = lvl
        if skip is None: out.append(line)
    return '\n'.join(out)


def section(text, name):
    """The section whose heading starts with name (any level), to the next heading of the same or a higher level."""
    lines, out, lvl = text.split('\n'), None, None
    for line in lines:
        h = HEAD.match(line)
        if h and out is not None and len(h.group(1)) <= lvl: break
        if out is not None: out.append(line)
        elif h and h.group(2).strip(' *_').lower().startswith(name.lower()):
            out, lvl = [], len(h.group(1))
    return '\n'.join(out) if out is not None else None


def reading_body(text, reading_section=None):
    """The reading as written: the declared section, else the "## Reading" section, else the file without its apparatus
    (title, label paragraphs such as "Conventions: ...", and the sections STOP_HEAD names). HTML comments dropped."""
    text = COMMENT.sub(' ', text)
    if reading_section:
        sec = section(text, reading_section)
        if sec is not None: return drop_sections(sec)
    if re.search(r'^## Reading(?![ \t]*(?:notes?|conventions|marks|review|check))', text, re.M | re.I):
        return drop_sections(v2.body_of(text))
    body = drop_sections(text)
    paras = re.split(r'\n[ \t]*\n', body)
    return '\n\n'.join(p for p in paras if not LABEL_PARA.match(p.lstrip('# \t>')))


def quote_runs(body):
    """(quote blocks, text runs between two of them, headings) of a body: blank lines do not break a block."""
    blocks = inter = heads = 0
    state, pending = None, False
    for l in body.split('\n'):
        x = l.strip()
        if not x: continue
        if x.startswith('#'):
            heads += 1; continue
        if x.startswith('>'):
            if state != 'q':
                blocks += 1
                inter += pending
            state, pending = 'q', False
        else:
            pending = pending or state == 'q'
            state = 't'
    return blocks, inter, heads


def quoted(body, mode=None):
    """(body, quote lines taken as the reading?). mode 'cipher': the '>' lines are the reading (cipher_markup '>');
    'clear': they are clear text and go (clear_markup '>'). Undeclared (16 Nov 2026, R23 scan: bethune, laigue1649,
    wesselenyi1664): when most of the body's words stand on '>' lines in a few blocks (no more than two runs of text
    between blocks, besides one per heading), the blockquote is the reading and the lines around it are commentary.
    Otherwise '>' lines are dropped as before, e.g. klingenberg1675, where they carry the clear text between the
    cipher runs."""
    lines = [l for l in body.split('\n') if l.strip() and not l.lstrip().startswith(('|', '#'))]
    q = [l for l in lines if l.lstrip().startswith('>')]
    take = mode == 'cipher'
    if mode is None and q:
        nq = sum(len(WORD.findall(l)) for l in q)
        na = sum(len(WORD.findall(l)) for l in lines)
        blocks, inter, heads = quote_runs(body)
        take = nq >= 0.5 * na and inter <= 2 + heads
    if take:
        return '\n'.join(re.sub(r'^\s*(?:>\s?)+', '', l) for l in body.split('\n') if l.lstrip().startswith('>')), True
    return '\n'.join(l for l in body.split('\n') if not l.lstrip().startswith('>')), False


def joined(body):
    """Line labels cut and words broken at a line end joined, when the body is numbered line by line."""
    lines = [l for l in body.split('\n') if l.strip()]
    if lines and sum(bool(NUM.match(l)) for l in lines) > 0.5 * len(lines):
        out = ''
        for l in lines:
            if l.lstrip().startswith(('#', '==')): continue
            l = NUM.sub('', l).strip()
            out = out[:-1] + l if out.endswith('-') else (out + ' ' + l if out else l)
        return out
    return body


def running(text, reading_section=None):
    """Reading body as running text (see reading_body, quoted, joined)."""
    return joined(quoted(reading_body(text, reading_section))[0])


WORD = re.compile(r'[^\W\d_]+')

# ---- cipher words only -------------------------------------------------------------------------------------------
# README Conventions, 16 Nov 2026: the read share counts the words written in cipher only. A reading that marks its
# cipher or its clear words says so with a declaration, in the profile entry ("cipher_markup": "⟦⟧" or
# "clear_markup": "{}", profile.schema.json) or in the reading file (<!-- measure: cipher_markup=** -->, which wins).
# Undeclared, the whole body is measured and the result says "not split".
ITAL = r'(?<![*\w])\*(?![*\s])((?:[^*\n]|\n(?!\s*\n))+?)(?<![\s*])\*(?![*\w])|(?<![\w_])_(?![_\s])((?:[^_\n]|\n(?!\s*\n))+?)(?<!\s)_(?![\w_])'
BOLDITAL = r'\*\*\*((?:[^*\n]|\n(?!\s*\n))+?)\*\*\*'
MARKUP = {
    '⟦⟧': re.compile(r'⟦([^⟧]*)⟧'),
    '⟨⟩': re.compile(r'⟨([^⟩]*)⟩'),
    '«»': re.compile(r'«([^»]*)»'),
    '‹›': re.compile(r'‹([^›]*)›'),
    '<>': re.compile(r'<([^<>\n]+)>'),
    '{}': re.compile(r'\{(?![?+\-])([^{}\n]*)\}'),
    '**': re.compile(BOLDITAL + r'|\*\*((?:[^*\n]|\n(?!\s*\n))+?)\*\*'),
    '*': re.compile(BOLDITAL + '|' + ITAL),
    'CAPS': re.compile(r'(?<![^\W\d_])((?:[A-ZÀ-ÞŒ]{2,}[\s,.;:\'’\-]+(?:\[\?\][\s,.;:]*)*)*[A-ZÀ-ÞŒ]{2,})(?![^\W\d_])'),
}
SEEN = [('⟦⟧', '⟦'), ('⟨⟩', '⟨'), ('«»', '«'), ('‹›', '‹'), ('**', '**'), ('{}', re.compile(r'\{[^\W\d_]'))]
HOLE_TOK = re.compile(r'\[\?\]|\(\?\)|[^\W\d_]+')


def declaration(text, entry=None):
    """{'cipher_markup' | 'clear_markup' | 'bracket_expansions' | 'reading_section': value} for one reading file."""
    d = {k: entry[k] for k in ('cipher_markup', 'clear_markup', 'bracket_expansions', 'reading_section')
         if entry and k in entry}
    for m in DECL.finditer(text):
        for k, v in re.findall(r'(\w+)\s*=\s*(\S+)', m.group(1)):
            if k in ('cipher_markup', 'clear_markup'):
                d.pop('cipher_markup', None); d.pop('clear_markup', None); d[k] = v
            elif k == 'bracket_expansions': d[k] = v.lower() in ('1', 'true', 'yes')
    return d


def marks_seen(body):
    """Markups present in a body that was not split, so that a missing declaration is visible."""
    out = []
    for name, rx in SEEN:
        if (rx in body) if isinstance(rx, str) else rx.search(body): out.append(name)
    if re.search(ITAL, body.replace('**', '')): out.append('*')
    return out


def groups(m):
    return ' '.join(g for g in m.groups() if g)


def cipher_only(b, mark):
    """Keep the cipher spans of a holes-converted body, and the hole marks that touch a cipher span (an unread group is
    often left out of the mark: '**Generalis** [?]'); clear words, and holes and doubtful marks among them, go."""
    rx = MARKUP[mark]
    out, pos, spans = [], 0, list(rx.finditer(b))
    for i, m in enumerate(spans + [None]):
        rest = b[pos:m.start() if m else len(b)]
        toks = HOLE_TOK.findall(rest)
        words = [k for k, x in enumerate(toks) if x not in ('[?]', '(?)')]
        first, last = (words[0], words[-1]) if words else (len(toks), -1)
        for k, x in enumerate(toks):
            if x == '[?]' and ((i > 0 and k < first) or (m is not None and k > last)):
                out.append('[?]')
        if m is None: break
        out.append(groups(m))
        pos = m.end()
    return ' '.join(out)


def clear_removed(b, mark):
    """Drop the clear spans of a holes-converted body, with any hole or doubtful mark inside them."""
    return MARKUP[mark].sub(' ', b)


EXPANSION = re.compile(r'(?<=[^\W\d_])\[([^\W\d_]+)\]|\[([^\W\d_]+)\](?=[^\W\d_])')


def measure_text(text, decl=None):
    """Count one reading file. Returns dict(words, holes, doubtful, share, split, marks, quoted):
    split is 'cipher only (cipher_markup X)', 'cipher only (clear_markup X)' or 'not split'."""
    decl = decl or {}
    qmode = 'cipher' if decl.get('cipher_markup') == '>' else 'clear' if decl.get('clear_markup') == '>' else None
    raw = reading_body(text, decl.get('reading_section'))
    body, q = quoted(raw, qmode)
    body = joined(body)
    body = '\n'.join(l for l in body.split('\n') if not l.lstrip().startswith(('|', '#')))
    if decl.get('bracket_expansions'):   # abbreviations written in the source and expanded here: Ip[sis], R[everendi]ssimam
        body = EXPANSION.sub(lambda m: m.group(1) or m.group(2), body)
    b = v2.holes(body)
    split, marks = 'not split', []
    if qmode:
        split = f"cipher only ({qmode}_markup >)"
    elif decl.get('cipher_markup') in MARKUP:
        b, split = cipher_only(b, decl['cipher_markup']), f"cipher only (cipher_markup {decl['cipher_markup']})"
    elif decl.get('clear_markup') in MARKUP:
        b, split = clear_removed(b, decl['clear_markup']), f"cipher only (clear_markup {decl['clear_markup']})"
    else:
        marks = marks_seen(body) + (['>'] if re.search(r'^\s*>', raw, re.M) else [])
    holes = b.count('[?]')
    doubtful = len(re.findall(r'\(\?\)', b))
    words = len(WORD.findall(b.replace('[?]', ' ')))
    rs = round(1 - (holes + doubtful) / (words + holes), 3) if words + holes else None   # a doubtful word is among the words
    return {'words': words, 'holes': holes, 'doubtful': doubtful, 'share': rs, 'split': split, 'marks': marks, 'quoted': q}


def share(text, decl=None):
    """(words read, holes, doubtful) on the reading body, counted by measure_text: holes are the explicit markers left
    by v2_score.holes ([?] for every [?word], supplied [word], {?}, part-word, unread sign and unvalued code) plus each
    doubtful word marked (?). Tables, headings, notes and translations are not counted; with a declaration, clear
    words are not counted either."""
    m = measure_text(text, decl)
    return m['words'], m['holes'], m['doubtful']


def measure_detail(folder, t):
    """The measure of one outcome.texts entry: dict as measure_text plus 'file', or None when nothing local can be
    measured. Of several files, the one with the highest share is kept (as before 16 Nov 2026)."""
    lang = (t.get('language') or '').split('-')[0]
    if lang in ('zh', 'ja'): return None
    files = _texts.listify(t.get('reading')) or _texts.listify(t.get('decryption'))
    best = None
    for r in files:
        f = ROOT / 'targets' / folder / str(r)
        if str(r).startswith('http') or not f.is_file() or f.suffix.lower() in ('.pdf', '.json', '.tsv'): continue
        text = f.read_text(encoding='utf8', errors='replace')
        m = measure_text(text, declaration(text, t))
        if m['words'] < 5: continue
        m['file'] = str(r)
        if best is None or m['share'] > best['share']: best = m
    return best


def measure(folder, t):
    """(file, read_share, words) for one entry, or None (see measure_detail)."""
    m = measure_detail(folder, t)
    return (m['file'], m['share'], m['words']) if m else None


def rewrite_entry(raw, idx, fn):
    """Apply fn(dict) to outcome.texts[idx], rewriting only that object in the file's own style."""
    dec = json.JSONDecoder()
    m = re.search(r'"texts":\s*\[', raw)
    pos, n = m.end(), -1
    while True:
        pos = raw.index('{', pos)
        obj, end = dec.raw_decode(raw, pos)
        n += 1
        if n == idx:
            start = pos
            break
        pos = end
    new = fn(dict(obj))
    text = raw[start:end]
    if '\n' not in text:
        out = json.dumps(new, ensure_ascii=False)
    else:
        nl = '\r\n' if '\r\n' in text else '\n'
        ind = re.search(r'\n([ \t]*)"', text).group(1)
        close = re.search(r'\n([ \t]*)\}\s*$', text).group(1)
        step = ind[len(close):] or ' '
        body = json.dumps(new, ensure_ascii=False, indent=len(step)).split('\n')
        out = body[0] + ''.join(nl + close + line for line in body[1:])
    return raw[:start] + out + raw[end:]


def add_step(raw, step):
    """Append one step to the top-level "solution" list, in the list's own style."""
    d = json.loads(raw)
    if not isinstance(d.get('solution'), list) or not d['solution']: return raw
    m = re.search(r'"solution":\s*\[', raw)
    dec = json.JSONDecoder()
    pos, last_end = m.end(), None
    while True:
        j = raw.find('{', pos)
        k = raw.find(']', pos)
        if j == -1 or (k != -1 and k < j): break
        _, e = dec.raw_decode(raw, j)
        last_end = pos = e
    if last_end is None: return raw
    ind = STEP_RE.search(raw[m.end():last_end])
    nl = '\r\n' if '\r\n' in raw else '\n'
    item = json.dumps(step, ensure_ascii=False)
    piece = (',' + nl + ind.group(1) + item) if ind else (', ' + item)
    out = raw[:last_end] + piece + raw[last_end:]
    assert len(json.loads(out)['solution']) == len(d['solution']) + 1
    return out


def main(apply):
    print('folder\tidx\tdoc\tfile\twords\tread_share\tstate_now\tsplit\tmarks_seen')
    changed, unmeasured, not_split = {}, [], 0
    for p in sorted((ROOT / 'targets').glob('*/profile.json')):
        raw = p.read_bytes().decode('utf-8')
        d = json.loads(raw)
        o = d.get('outcome') or {}
        if o.get('texts_withheld'): continue
        moves = []
        for i, t in enumerate(o.get('texts') or []):
            if _texts.entry_state(t) != 'read': continue
            md = measure_detail(p.parent.name, t)
            doc = '/'.join(map(str, _texts.listify(t.get('doc'))))
            if md is None:
                unmeasured.append((p.parent.name, i, doc))
                continue
            f, rs, words = md['file'], md['share'], md['words']
            st = 'read' if rs >= BAR else 'read in part'
            if md['split'] == 'not split': not_split += 1
            print(f'{p.parent.name}\t{i}\t{doc}\t{f}\t{words}\t{rs}\t{st}\t{md["split"]}\t{",".join(md["marks"])}')
            moves.append((i, rs, st, f))
        if not moves: continue
        changed[p.parent.name] = moves
        if not apply: continue
        for i, rs, st, f in moves:
            def fn(e, rs=rs, st=st, f=f):
                e['read_share'] = rs
                if st == 'read in part':
                    e['state'] = 'read in part'
                    note = (f'24 Oct 2026: {rs * 100:.1f}% of the words of {f} read as sense (v2_score explicit holes); '
                            'coherent sentences but under the 95% read bar, so read in part.')
                    e['note'] = (e['note'] + ' ' + note) if e.get('note') else note
                return e
            raw = rewrite_entry(raw, i, fn)
        n_part = sum(1 for m in moves if m[2] == 'read in part')
        if n_part:
            raw = add_step(raw, {'date': '2026-10-24', 'kind': 'verification',
                                 'what': f'Read bar applied per document (v10): {n_part} of {len(moves)} documents marked '
                                         'read measure under 95% of words read as sense (v2_score explicit holes) and are '
                                         'now read in part; read_share recorded for each.',
                                 'result': 'partial'})
        json.loads(raw)
        p.write_bytes(raw.encode('utf-8'))
    n = sum(len(v) for v in changed.values())
    part = sum(1 for v in changed.values() for m in v if m[2] == 'read in part')
    print(f'# measured {n} read entries in {len(changed)} targets; {part} under 0.95 -> read in part; '
          f'{not_split} not split (whole body measured: no cipher_markup / clear_markup declared); '
          f'{len(unmeasured)} not measurable: ' + ', '.join(f'{a}#{b}' for a, b, _ in unmeasured), file=sys.stderr)


if __name__ == '__main__':
    main('--apply' in sys.argv)
