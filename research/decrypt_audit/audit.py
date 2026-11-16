"""Decrypt audit (16 Nov 2026): does the published reading follow from the key and the transcription?

For every target whose profile says the key was recovered here (outcome.method starts "key recovered"), and for each
entry of outcome.texts, the script

  1. parses the key file(s) named in outcome.key_file (tsv, txt, json, md tables), trying the column pairings and
     keeping the one that best reproduces the published text;
  2. tokenises the transcription (whitespace, punctuation, per character or longest match; again the scheme that
     best reproduces the published text, the choice most favourable to the reading) and applies the key with
     nothing edited: the mechanical decrypt;
  3. aligns the letters of the mechanical decrypt with the letters of the published text (the reading file, else
     the decryption file), folding case, accents, u/v, i/j/y;
  4. counts the letters of the published text that the mechanical decrypt does not give, apart for letters inside
     a mark and outside, and the words that hold one. Marks: [ ] { } ‹ › ⟨ ⟩ « » < > and word°. Asterisks are not
     taken as a mark: some targets use them for emphasis, some for clear text, one for the cipher passages.
     Line labels ("L07:", "c. 11r l. 7:") are dropped from both files, and doubt marks (? ^ *) from tokens.

The alignment is anchored on runs of 8 or more letters common to both texts; only the short gaps between two
anchors are compared, so headers, notes, clear passages and translations inside the published file are left out
(counted as extra). A text is judged only when 60% of the decrypt is found in the published text this way. A
nomenclator whose codes expand to words the key file does not hold, or a reading kept as numbers, is not checked.

It reads files only and writes results.tsv and results.json next to itself. It is a triage, not a verdict:
"not checked" means the script could not rebuild the decrypt (key format, tokens, codes kept as numbers), not that
the reading is sound, and a flag means "open the files", not "wrong". memoire1560 before its fix scored 26% of
words with an unmarked departure and is the calibration case.

Usage: python research/decrypt_audit/audit.py [folder ...]
"""
import json, os, re, sys, glob, unicodedata, collections

try:
    from rapidfuzz.distance import Levenshtein, LCSseq
    def opcodes(a, b):
        return [(o.tag, o.src_start, o.src_end, o.dest_start, o.dest_end) for o in Levenshtein.opcodes(a, b)]
    Sim = Levenshtein.normalized_similarity
except ImportError:
    sys.exit('pip install rapidfuzz (used for the letter alignment)')

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
CAP = 20000          # letters aligned per text (longer texts: the first CAP letters of each side)
ANCHOR = 8           # a run of this many letters common to both texts anchors the comparison
GAP = 40             # between two anchors, a gap up to this long on both sides is compared letter by letter
FOLD = {'v': 'u', 'j': 'i', 'y': 'i', 'ß': 'ss', 'æ': 'ae', 'œ': 'oe', 'ł': 'l', 'ø': 'o', 'đ': 'd'}
NULLS = {'', '-', '–', '—', 'null', 'nul', 'nulla', '(null)', '∅', '0null', 'none'}


def fold(s):
    out = []
    for c in unicodedata.normalize('NFD', s.lower()):
        if unicodedata.category(c) == 'Mn' or not c.isalpha():
            continue
        out.append(FOLD.get(c, c))
    return ''.join(out)


def read(path):
    try:
        return open(path, encoding='utf8', errors='replace').read()
    except OSError:
        return None


def as_list(v):
    return [v] if isinstance(v, str) else list(v or [])


# ---------------------------------------------------------------- keys
def value_of(v):
    """First alternative of a key value, folded to letters ('' for a null)."""
    v = v.strip()
    if v.lower() in NULLS:
        return ''
    v = re.split(r'\s*(?:/|\||,| or )\s*', v)[0]
    v = re.sub(r'\([^)]*\)', '', v)
    return fold(v)


def key_tables(path):
    """Candidate {sign: value} maps from one key file (several, for the column pairings)."""
    t = read(path)
    if t is None:
        return []
    cands = []
    if path.endswith('.json'):
        try:
            j = json.loads(t)
        except ValueError:
            return []
        def dicts(o, depth=0):
            if isinstance(o, dict):
                flat = {str(k): v for k, v in o.items() if isinstance(v, (str, int))}
                if len(flat) >= 5:
                    yield {k: str(v) for k, v in flat.items()}
                lists = {str(k): v for k, v in o.items() if isinstance(v, list) and all(isinstance(x, (str, int)) for x in v)}
                if len(lists) >= 5:                      # letter -> [signs]
                    yield {str(x): k for k, v in lists.items() for x in v}
                if depth < 2:
                    for v in o.values():
                        yield from dicts(v, depth + 1)
            elif isinstance(o, list) and depth < 2:
                for v in o:
                    yield from dicts(v, depth + 1)
        for d in dicts(j):
            cands.append(d)
            cands.append({v: k for k, v in d.items()})
        return cands
    rows = []
    for line in t.split('\n'):
        if not line.strip() or (line.lstrip().startswith('#') and not line.startswith('#\t')):
            continue
        if line.startswith('==') and '\t' not in line:          # a sign named '=' in a sign=value file
            rows.append(['=', line[2:].strip()]); continue
        if '\t' in line:
            rows.append([c.strip() for c in line.split('\t')])
        elif line.count('|') >= 2:
            cells = [c.strip().strip('`*') for c in line.strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?', c or '-') for c in cells):
                rows.append(cells)
        elif path.endswith('.txt') and re.match(r'^\S+\s*(=|->|→|:)\s*\S', line):
            a, b = re.split(r'\s*(?:=|->|→|:)\s*', line.strip(), maxsplit=1)
            rows.append([a, b])
    rows = [[re.sub(r'^=(?=.)', '', r[0])] + r[1:] for r in rows if len(r) >= 2]
    if len(rows) < 5:
        return []
    width = max(len(r) for r in rows)
    for a, b in [(0, 1), (1, 0), (1, 2), (0, 2), (2, 1)]:
        if a < width and b < width:
            d = {r[a]: r[b] for r in rows if len(r) > max(a, b) and r[a]}
            if len(d) >= 5:
                cands.append(d)
    return cands


# ---------------------------------------------------------------- transcription
LABEL = re.compile(r'^\s*(?:\[?(?:f|fol|p|l|line|page|c)?\.?\s*\d+[rv]?(?:[.:]\d+)?m?\]?[:.)]?\s*\t|\d+[rv]?\.\d+m?\s+)', re.I)


# a line label before the text: "L07:", "V01 ", "M16 ", "c. 11r l. 7:", "k.138r.01:" (a bare "U2 " is a token, kept)
LABEL2 = re.compile(r'^\s*(?:[A-Za-z]{1,2}\d{1,3}[a-z]?[:)]\s*(?=\S)|[A-Za-z]{1,2}\d{2,3}\s+(?=\S)|[A-Za-z]{1,2}\.?\s?\d[\w. ]{0,14}:\s*)')


def body_lines(t):
    for line in t.split('\n'):
        s = line.strip()
        if not s or s.startswith(('#', '//', '|--', '```', '---')):
            continue
        yield LABEL2.sub('', LABEL.sub('', line), count=1)


def tokenise(t, signs):
    """Token lists for a transcription under each scheme; the caller keeps the one the key covers best."""
    text = '\n'.join(body_lines(t))
    text = re.sub(r'\[[^\]\n]{0,80}\]', ' ', text)            # editorial marks, struck signs
    longest = sorted(signs, key=len, reverse=True)
    maxlen = len(longest[0]) if longest else 1
    def greedy(words):
        out = []
        for w in words:
            i = 0
            while i < len(w):
                for n in range(min(maxlen, len(w) - i), 0, -1):
                    if w[i:i + n] in signs:
                        out.append(w[i:i + n]); i += n; break
                else:
                    out.append(w[i]); i += 1
        return out
    ws = text.split()
    yield 'whitespace', ws
    yield 'punctuation', [x for x in re.split(r'[\s.,;:/|·+\-]+', text) if x]
    yield 'longest match', greedy(ws)
    yield 'characters', [c for c in text if not c.isspace()]


def mechanical(trans_text, tables, rd):
    """Apply each candidate key table under each tokenisation; keep the pair that best reproduces the published
    text rd (the choice most favourable to the reading), among those where the key covers 70% of the tokens.
    If none reaches 70%, the best-covered one is returned so that the coverage can be reported."""
    best = cover = None
    for table in tables:
        signs = set(table)
        low = {k.lower(): v for k, v in table.items()}
        vals = {k: value_of(v) for k, v in table.items()}
        lowv = {k.lower(): v for k, v in vals.items()}
        for scheme, toks in tokenise(trans_text, signs):
            if len(toks) < 20:
                continue
            toks = [x if x in table else (x.rstrip('?^*') or x) for x in toks]      # doubt marks on a token
            hit = sum(1 for x in toks if x in table or x.lower() in low)
            cov = hit / len(toks)
            letters = ''.join(vals.get(x, lowv.get(x.lower(), '')) for x in toks)
            cand = dict(coverage=cov, scheme=scheme, tokens=len(toks), letters=letters)
            if cover is None or cov > cover['coverage']:
                cover = cand
            if cov >= 0.7 and letters:
                sim = Sim(letters[:CAP], rd[:CAP])
                if best is None or sim > best[0]:
                    best = (sim, cand)
    return best[1] if best else cover


# ---------------------------------------------------------------- reading
def reading_letters(t):
    """Folded letters of a published text, a parallel list of 'inside brackets', and a word index per letter."""
    m = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
    if m:
        t = m.group(1)
    letters, marked, word = [], [], []
    w = 0
    for line in body_lines(t):
        depth = 0
        for tok in re.split(r'(\s+)', line):
            if not tok.strip():
                continue
            w += 1
            deg = '°' in tok             # word° = a repaired word
            for c in tok:
                if c in '[{‹⟨«<':
                    depth += 1
                elif c in ']}›⟩»>':
                    depth = max(0, depth - 1)
                else:
                    for f in fold(c):
                        letters.append(f); marked.append(depth > 0 or deg); word.append(w)
    return ''.join(letters), marked, word


def compare(mech, rd, marked, word):
    """Anchor on runs of ANCHOR or more letters common to both texts (in order). Between two anchors, when the
    gap is short on both sides (GAP letters), the reading's letters there are compared with the decrypt's:
    that is where a departure shows. Everything else in the published text (headers, notes, clear passages,
    passages the key does not cover) is outside the comparison and counted as extra."""
    mech, rd = mech[:CAP], rd[:CAP]
    marked, word = marked[:len(rd)], word[:len(rd)]
    blocks = [(o.src_start, o.dest_start, o.src_end - o.src_start) for o in LCSseq.opcodes(mech, rd)
              if o.tag == 'equal' and o.src_end - o.src_start >= ANCHOR]
    same = dep_un = dep_mk = cov_m = cov_r = 0
    bad_words, cov_words = set(), set()
    for k, (i, j, n) in enumerate(blocks):
        same += n; cov_m += n; cov_r += n
        cov_words.update(word[j:j + n])
        if k + 1 < len(blocks):
            i2, j2, _ = blocks[k + 1]
            ga, gb = i2 - (i + n), j2 - (j + n)
            if ga <= GAP and gb <= GAP and (ga or gb):
                cov_m += ga; cov_r += gb
                cov_words.update(word[j + n:j2])
                for tag, a1, a2, b1, b2 in opcodes(mech[i + n:i2], rd[j + n:j2]):
                    if tag == 'equal':
                        same += a2 - a1
                    elif tag != 'delete':
                        for x in range(j + n + b1, j + n + b2):
                            if marked[x]:
                                dep_mk += 1
                            else:
                                dep_un += 1; bad_words.add(word[x])
                    if tag == 'delete' and b1 < gb:          # decrypt letters dropped inside a word of the reading
                        x = j + n + b1
                        if not marked[x] and x > 0 and word[x] == word[x - 1]:
                            dep_un += 1; bad_words.add(word[x])
    unmarked_words = {w for w, m in zip(word, marked) if not m} & cov_words
    base = sum(1 for x in range(len(rd)) if not marked[x] and word[x] in cov_words)
    return dict(mech_letters=len(mech), read_letters=len(rd), same=same, unmarked=dep_un, marked=dep_mk,
                extra_reading=len(rd) - cov_r, extra_mechanical=len(mech) - cov_m,
                letter_rate=dep_un / base if base else None,
                words=len(unmarked_words), words_departing=len(bad_words & unmarked_words),
                word_rate=len(bad_words & unmarked_words) / len(unmarked_words) if unmarked_words else None,
                agreement=cov_m / max(1, len(mech)))


def verdict(r):
    if why_not(r):
        return 'not checked'
    wr = r['word_rate'] or 0
    return 'agrees' if wr <= 0.03 else 'some unmarked departures' if wr <= 0.10 else 'many unmarked departures'


def why_not(r):
    if r.get('why'):
        return r['why']
    if r['coverage'] < 0.7:
        return f"key covers {r['coverage']:.0%} of the transcription tokens"
    if r['mech_letters'] < 100:
        return 'under 100 letters decrypted'
    if r['agreement'] < 0.6:
        return (f"only {r['agreement']:.0%} of the decrypt is found in the published text (codes kept as numbers or "
                "expanded to words, nulls, another key, or a text edited beyond letter changes)")
    if r['words'] < 30:
        return 'under 30 words compared'
    return ''


def audit(folder):
    d = os.path.join(ROOT, 'targets', folder)
    try:
        p = json.load(open(os.path.join(d, 'profile.json'), encoding='utf8'))
    except (OSError, ValueError):
        return []
    o = p.get('outcome') or {}
    if not (o.get('method') or '').startswith('key recovered'):
        return []
    tables = []
    for k in as_list(o.get('key_file')):
        if not k.startswith('http'):
            tables += key_tables(os.path.join(d, k))
    rows = []
    for n, t in enumerate(o.get('texts') or []):
        base = dict(folder=folder, text=n, label=t.get('label') or str(t.get('doc')), state=t.get('state', 'read'),
                    method=o.get('method'), cls=o.get('class'))
        pub = as_list(t.get('reading')) or as_list(t.get('decryption'))
        trans = as_list(t.get('transcription'))
        if t.get('state') == 'not prose':
            rows.append(dict(base, why='not prose (key sheet, list or figures)')); continue
        if not trans or not pub:
            rows.append(dict(base, why='no transcription or no published text listed')); continue
        if not tables:
            rows.append(dict(base, why='no key file the script can parse' if as_list(o.get('key_file')) else 'no key_file in the profile')); continue
        tt = [read(os.path.join(d, x)) for x in trans if not x.startswith('http')]
        pp = [read(os.path.join(d, x)) for x in pub if not x.startswith('http')]
        if not tt or any(x is None for x in tt) or not pp or any(x is None for x in pp):
            rows.append(dict(base, why='a listed file is missing or remote')); continue
        if set(trans) & set(pub):
            rows.append(dict(base, why='transcription and published text are the same file')); continue
        rd, marked, word = reading_letters('\n'.join(pp))
        m = mechanical('\n'.join(tt), tables, rd)
        if m is None:
            rows.append(dict(base, why='transcription too short to tokenise')); continue
        r = dict(base, coverage=m['coverage'], scheme=m['scheme'], tokens=m['tokens'], published=';'.join(pub))
        r.update(compare(m['letters'], rd, marked, word))
        rows.append(r)
    return rows


def main():
    folders = sys.argv[1:] or sorted(os.path.basename(os.path.dirname(f)) for f in glob.glob(os.path.join(ROOT, 'targets', '*', 'profile.json')))
    rows = []
    for f in folders:
        rows += audit(f)
    for r in rows:
        r['why'] = why_not(r); r['verdict'] = 'not checked' if r['why'] else verdict(r)
    if sys.argv[1:]:
        for r in rows:
            print(json.dumps(r, ensure_ascii=False))
        return
    cols = ['folder', 'text', 'label', 'state', 'method', 'verdict', 'word_rate', 'words_departing', 'words', 'letter_rate',
            'unmarked', 'marked', 'agreement', 'coverage', 'scheme', 'mech_letters', 'read_letters', 'extra_reading',
            'extra_mechanical', 'why']
    fmt = lambda v: '' if v is None else f'{v:.3f}' if isinstance(v, float) else str(v).replace('\t', ' ').replace('\n', ' ')
    with open(os.path.join(HERE, 'results.tsv'), 'w', encoding='utf8', newline='\n') as f:
        f.write('\t'.join(cols) + '\n')
        for r in sorted(rows, key=lambda r: (-(r.get('word_rate') or -1) if r['verdict'] != 'not checked' else 2, r['folder'], r['text'])):
            f.write('\t'.join(fmt(r.get(c)) for c in cols) + '\n')
    by = collections.Counter(r['verdict'] for r in rows)
    targets = collections.defaultdict(set)
    for r in rows:
        targets[r['verdict']].add(r['folder'])
    why = collections.Counter(re.sub(r'\d+%', 'N%', r['why']) for r in rows if r['verdict'] == 'not checked')
    summary = dict(date='2026-11-16', targets=len({r['folder'] for r in rows}), texts=len(rows), texts_by_verdict=dict(by),
                   targets_by_verdict={k: len(v) for k, v in targets.items()}, not_checked_reasons=dict(why.most_common()))
    json.dump(summary, open(os.path.join(HERE, 'results.json'), 'w', encoding='utf8'), indent=1, ensure_ascii=False)
    print(json.dumps(summary, indent=1, ensure_ascii=False))


if __name__ == '__main__':
    main()
