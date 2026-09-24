# Glyph-level XML export of existing cipher transcriptions (pilot, 24 Sept 2026; George Lasry's question
# "can the LLM give a transcription XML?").
#
# Nothing here re-reads an image. The input is the transcription files the project already has; the output is
# one XML file per document, one <g> element per cipher glyph, grouped in <page> and <line>.
#
#   python tools/transcription_xml.py sormano      -> sormano/xml/no63.xml, no65.xml, no66.xml
#   python tools/transcription_xml.py mondoucet    -> gallica_sweep/mondoucet/xml/1573-09-09.xml, 1572-07-13.xml
#   python tools/transcription_xml.py survey       -> papers/lasry/graphic_sign_transcriptions.csv (profiles whose
#                                                     non-letter, non-digit signs the model transcribed from images)
#   python tools/transcription_xml.py all
#
# Two kinds of source, so two adapters:
#   sormano    Markdown (n6x_transcription.md): the cipher is recorded as the decoded letters, in *italics*, with
#              {..} doubtful glyph, (ɦ) null, (·) noise box, (?) doubtful word, ◎ the DUCA sign. There is no sign
#              label, so <g> carries a reading and a certainty, not a sign identity.
#   mondoucet  sign-label text (ct/*_split.txt, hand/ct_f6*_split.txt): one label per glyph, '/' the scribe's
#              word gap. 9 Sept 1573 adds the Court's letter for each glyph from the hard-EM alignment
#              (f1573/key1573_split2_align.txt); 13 July 1572 has no decipherment, so each glyph gets only
#              the key's alternatives and the beam decoder's letter.
#
# Element and attribute set (the same for both):
#   <g>  one glyph.   sign= transcription label (mondoucet only)   shape= a glyph drawn as a character when it
#        has no reading   r= reading (letter, or word for a word sign)   type= letter | null | code | noise |
#        unknown | extra | dot   cert=low where the transcription marks a doubt   basis= court | eye | decoder
#        key= P(letter|sign) from the key counts, 'null' included, share >= 0.05, as "s:0.90 null:0.05"
#   <w>  a word: the editor's division (sormano) or the scribe's gap (mondoucet, gap="scribe").
#   <gap/> nothing transcribed (reason=), or a letter of the decipherment with no glyph matched to it (r=).
#   <clear> clear text inside the line.   <note> editorial remark carried over from the source.
# No glyph has coordinates: the transcriptions were made from line strips by eye (with k-NN help for sormano),
# and no bounding box was ever stored.
import sys, os, re, json, datetime, collections
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()


def header(target, doc, sources, provenance):
    t = ET.Element('transcription', target=target, document=doc, generator='tools/transcription_xml.py',
                   date=TODAY)
    for s in sources:
        ET.SubElement(t, 'source', file=s)
    ET.SubElement(t, 'provenance').text = provenance
    return t


def write(tree, path):
    ET.indent(tree, space=' ')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    ET.ElementTree(tree).write(path, encoding='utf-8', xml_declaration=True)
    ET.parse(path)                                              # well-formed check
    g = tree.findall('.//g')
    c = collections.Counter(x.get('type', 'letter') for x in g)
    low = sum(1 for x in g if x.get('cert') == 'low')
    print('%-55s %6d glyphs  %s  low-certainty %d  gaps %d' % (os.path.relpath(path, ROOT), len(g),
          ' '.join('%s %d' % kv for kv in sorted(c.items())), low, len(tree.findall('.//gap'))))


# ---------------------------------------------------------------- sormano (Markdown, decoded letters)

LATIN = re.compile(r'[a-zA-ZàèéìòùÀÈÉÌÒÙ]')
SOR_PROV = ('LLM transcription from the Gallica images of BnF fr. 3096 (btv1b9060015d): automatic glyph '
            'segmentation and k-NN classification against a hand-labelled sample, every line checked by eye '
            'against its strip. The file records the decoded letter of each glyph, not a sign label; '
            'no glyph coordinates were kept.')


def sor_cipher(text, line, state):
    """Parse one italic run into <w>/<g> children of <cipher>."""
    cip = ET.SubElement(line, 'cipher')
    w = None

    def word():
        nonlocal w
        if w is None:
            w = ET.SubElement(cip, 'w')
        return w

    def g(**a):
        ET.SubElement(word(), 'g', {k: v for k, v in a.items() if v})

    i = 0
    while i < len(text):
        ch = text[i]
        if ch == ' ':
            w = None; i += 1; continue
        if ch == '=' and text[i:i + 2] in ('= ', '=n'):      # "= n65 L20-22": editorial cross-reference
            ET.SubElement(cip, 'note').text = text[i:].strip(); break
        if ch in '{([':
            close = {'{': '}', '(': ')', '[': ']'}[ch]
            j = text.find(close, i)
            if j < 0:
                j = len(text)
            body = text[i + 1:j]
            i = j + 1
            if ch == '{':                                    # doubtful glyph(s)
                for c in body:
                    if c == '·': g(type='noise', cert='low')
                    elif c == '?': g(type='unknown', cert='low')
                    elif c in '…': ET.SubElement(word(), 'gap', reason='unread')
                    elif c.islower() and LATIN.match(c): g(r=c, cert='low')
                    else: g(shape=c, cert='low')          # a shape note, no reading given
            elif ch == '(':
                if body == '?':                              # doubtful word
                    if w is not None:
                        w.set('cert', 'low')
                elif body and all(c in 'ɦﬀHh' for c in body):
                    for c in body: g(type='null', shape=c)
                elif body and all(c == '·' for c in body):
                    for c in body: g(type='noise')
                else:
                    ET.SubElement(cip, 'note').text = body
            else:                                            # [..]
                if len(body) == 1:
                    g(type='extra', shape=body, cert='low')
                else:
                    ET.SubElement(cip, 'note').text = body
            continue
        if text.startswith('...', i) or ch == '…':
            ET.SubElement(word(), 'gap', reason='unread'); i += 3 if ch == '.' else 1; continue
        if ch == '◎':
            w = None; ET.SubElement(ET.SubElement(cip, 'w'), 'g', type='code', shape='◎', r='DUCA'); i += 1; continue
        if ch == '·':
            g(type='noise'); i += 1; continue
        if LATIN.match(ch):
            g(r=ch.lower()); i += 1; continue
        if ch in "-'.,;:!–—":                                # line-end hyphens, editorial punctuation
            i += 1; continue
        g(shape=ch, cert='low'); i += 1                      # a sign written as its shape (ꝓ, ≠, ⊡ ...)


def sor_line(body, line, state):
    """Split a line into clear and cipher runs; the italic state carries over line ends."""
    parts = body.split('*')
    for k, part in enumerate(parts):
        if k:
            state['it'] = not state['it']
        if not part.strip():
            continue
        if state['it']:
            sor_cipher(part, line, state)
        else:
            clear = part
            for m in re.split(r'(◎)', clear):
                if m == '◎':
                    ET.SubElement(ET.SubElement(ET.SubElement(line, 'cipher'), 'w'), 'g', type='code', shape='◎', r='DUCA')
                elif m.strip():
                    ET.SubElement(line, 'clear').text = m.strip()


def sormano():
    folder = os.path.join(ROOT, 'sormano')
    for no in ('63', '65', '66'):
        src = 'sormano/n%s_transcription.md' % no
        lines = open(os.path.join(ROOT, src), encoding='utf-8').read().split('\n')
        t = header('sormano', 'no%s' % no, [src], SOR_PROV)
        conv = ET.SubElement(t, 'conventions')
        page = None; state = {'it': False}; pre = []
        for l in lines[1:]:
            m = re.match(r'^## (f\. \S+)\s*(?:\((.*)\))?', l)
            if m:
                if page is None:
                    conv.text = ' '.join(x.strip() for x in pre if x.strip())
                page = ET.SubElement(t, 'page', n=m.group(1), image=m.group(2) or '')
                state['it'] = False
                continue
            if page is None:
                pre.append(l); continue
            m = re.match(r'^L(\d+)\s(.*)$', l)
            if m:
                line = ET.SubElement(page, 'line', n='L' + m.group(1))
                sor_line(m.group(2), line, state)
            elif l.strip():
                ET.SubElement(page, 'note').text = l.strip()
        write(t, os.path.join(folder, 'xml', 'no%s.xml' % no))


# ---------------------------------------------------------------- mondoucet (sign labels)

MON = os.path.join(ROOT, 'gallica_sweep', 'mondoucet')
MON_PROV = ('LLM transcription from the Gallica microfilm images of BnF fr. 16127, glyph by glyph on '
            'line strips, one ASCII label per sign (legend in <conventions>); a = round closed a, α/@ = open '
            'alpha, split on 21 Sept 2026. No glyph coordinates were kept.')


def legend():
    s = open(os.path.join(MON, 'hand', 'legend.md'), encoding='utf-8').read()
    return ' '.join(x.strip() for x in s.split('\n')[1:] if x.strip())


def key_str(sign, counts, nulls):
    c = counts.get(sign, {}); n = nulls.get(sign, 0); tot = sum(c.values()) + n
    if not tot:
        return None
    items = sorted(list(c.items()) + [('null', n)], key=lambda kv: -kv[1])
    return ' '.join('%s:%.2f' % (k, v / tot) for k, v in items if v / tot >= 0.05)


def ct_lines(fn):
    """[(folio, label, tokens)] from a sign-label file; folio from '# f.NNNx' comment lines."""
    out = []; fol = None
    for l in open(fn, encoding='utf-8'):
        m = re.match(r'#\s*(?:\d+ \w+ \d+, )?f\.\s?(\d+[rv])', l)
        if m:
            fol = 'f. ' + m.group(1)
        if l.startswith('#') or ':' not in l:
            continue
        lab, rest = l.split(':', 1)
        out.append((fol, lab.strip(), re.findall(r'\[[^\]]*\]|\S+', rest)))
    return out


def align_paths(fn):
    """Moves per document from key1573_split2_align.txt: list of [(ct, pt)] per path, in order."""
    txt = open(fn, encoding='utf-8').read().split('\n')
    paths = []; cur = None; i = 0
    while i < len(txt):
        l = txt[i]
        if l == '':
            cur = []; paths.append(cur); i += 1; continue
        if cur is not None and re.match(r'^\S+ \| ', l) and i + 1 < len(txt) and txt[i + 1].startswith('   | '):
            ct = l.split(' | ', 1)[1].split()
            pt = re.sub(r'\{\?\}', ' {?} ', txt[i + 1][5:]).split()
            assert len(ct) == len(pt), l
            cur.extend(zip(ct, pt)); i += 2; continue
        i += 1
    return [p for p in paths if p]


def mon_1573():
    key = json.load(open(os.path.join(MON, 'f1573', 'key1573_split2.json'), encoding='utf-8'))
    counts, nulls = key['counts'], key['nulls']
    files = ['f1573/ct/f135r_split.txt', 'f1573/ct/blk2_split.txt']
    folios = {'': None, 'v': 'f. 136v', 'w': 'f. 137r'}
    paths = align_paths(os.path.join(MON, 'f1573', 'key1573_split2_align.txt'))
    assert len(paths) == 2
    codes = collections.Counter(m for p in paths for m in p if m[1].startswith('{'))
    t = header('mondoucet', '9 Sept 1573, Amsterdam (ff. 135r-137r)',
               ['gallica_sweep/mondoucet/' + f for f in files] +
               ['gallica_sweep/mondoucet/f1573/key1573_split2_align.txt',
                'gallica_sweep/mondoucet/f1573/key1573_split2.json'],
               MON_PROV + ' The reading of each glyph (r, basis="court") is the letter of the Court\'s '
               'contemporary decipherment (ff. 139-141) that the hard-EM aligner (f1573/align2.py) matched to it; '
               'key= gives the same sign\'s spread over the whole alignment. f. 137v was not transcribed.')
    ET.SubElement(t, 'conventions').text = legend() + ' Split: α = open alpha. "/" = scribe\'s word gap, "." = dot.'
    for f, moves in zip(files, paths):
        mi = 0; page = None
        for fol, lab, toks in ct_lines(os.path.join(MON, f)):
            pre = re.match(r'^([a-z]*)', lab).group(1)
            fol = folios.get(pre) or fol
            if page is None or page.get('n') != fol:
                page = ET.SubElement(t, 'page', n=fol)
            line = ET.SubElement(page, 'line', n=lab)
            w = ET.SubElement(line, 'w', gap='scribe')
            for tok in toks:
                if tok == '/':
                    if len(w): w = ET.SubElement(line, 'w', gap='scribe')
                    continue
                if tok in ('.', ':'):
                    ET.SubElement(w, 'g', type='dot', shape=tok); continue
                while mi < len(moves) and moves[mi][0] == '-':          # Court letter with no glyph
                    ET.SubElement(w, 'gap', r=moves[mi][1].lower(), reason='letter of the decipherment not matched to a glyph')
                    mi += 1
                ct, pt = moves[mi]; mi += 1
                if tok.startswith('['):
                    assert ct == 'CLEAR', (lab, tok, ct)
                    ET.SubElement(line, 'clear').text = tok[1:-1]
                    w = ET.SubElement(line, 'w', gap='scribe'); continue
                assert ct == tok, (f, lab, tok, ct)
                a = {'sign': tok}
                if pt == '_':
                    a.update(type='null', basis='court')
                elif pt.startswith('{'):
                    a.update(type='code', r=pt[1:-1], basis='court')
                    if codes[(tok, pt)] < 3:
                        a['cert'] = 'low'                    # a one-off sign-to-word match is aligner slack
                else:
                    a.update(r=pt, basis='court')
                k = key_str(tok, counts, nulls)
                if k: a['key'] = k
                ET.SubElement(w, 'g', a)
            for x in list(line):
                if x.tag == 'w' and not len(x): line.remove(x)
        while mi < len(moves) and moves[mi][0] == '-':
            ET.SubElement(line, 'gap', r=moves[mi][1].lower(), reason='letter of the decipherment not matched to a glyph'); mi += 1
        assert mi == len(moves), (f, mi, len(moves))
    write(t, os.path.join(MON, 'xml', '1573-09-09.xml'))


def mon_1572():
    k2 = json.load(open(os.path.join(MON, 'hand', 'key2.json'), encoding='utf-8'))
    k3 = json.load(open(os.path.join(MON, 'f1573', 'key1573_split2.json'), encoding='utf-8'))
    counts = {t: dict(v) for t, v in k2['key'].items()}; nulls = collections.Counter(k2['nulls'])
    for s in ('*', 'C', 'mq', 'j'):
        nulls[s] += 20                                   # hard nulls of the 1572 key (hand/decode_retry.py)
    counts['@'] = dict(collections.Counter(counts.get('@', {})) + collections.Counter(k3['counts']['α']))
    counts['a'].pop('r', None)                           # the 'ext' key of hand/decode_retry.py
    dec = {}; sec = None
    for l in open(os.path.join(MON, 'hand', 'decode_retry.txt'), encoding='utf-8'):
        if l.startswith('=='):
            sec = l.strip(); continue
        m = re.match(r'^\s*(\w+)\s+(\S+)$', l)
        if sec == '== ext (split)' and m:
            dec[m.group(1)] = m.group(2)
    files = ['hand/ct_f60_split.txt', 'hand/ct_f60v_split.txt', 'hand/ct_f61_split.txt']
    t = header('mondoucet', '13 July 1572, Brussels (ff. 60r-61r)',
               ['gallica_sweep/mondoucet/' + f for f in files] +
               ['gallica_sweep/mondoucet/hand/key2.json', 'gallica_sweep/mondoucet/hand/decode_retry.txt'],
               MON_PROV + ' This letter has no contemporary decipherment and is not in print; it is NOT read '
               '(about 1-8 % of glyphs fall in stretches that make sense). key= is the 1572 key with alpha = r '
               '(the "ext" key of hand/decode_retry.py); r with basis="decoder" is the beam decoder\'s output '
               'for that glyph, kept to show what the key gives, not a reading.')
    ET.SubElement(t, 'conventions').text = legend() + ' Split: @ = open alpha. Also mq = m with long descender, ' \
        'pc = p with cross below, X = b with cross below, 9 = q with cross below.'
    folio = {'ct_f60_split': 'f. 60r', 'ct_f60v_split': 'f. 60v', 'ct_f61_split': 'f. 61r'}
    for f in files:
        page = ET.SubElement(t, 'page', n=folio[os.path.basename(f)[:-4]])
        for _, lab, toks in ct_lines(os.path.join(MON, f)):
            line = ET.SubElement(page, 'line', n=lab)
            glyphs = [x for x in toks if x not in ('/', '.', ':') and not x.startswith('[')]
            d = dec.get(lab, '')
            if len(d) != len(glyphs):
                d = ''
                ET.SubElement(line, 'note').text = 'decoder output not aligned to this line'
            w = ET.SubElement(line, 'w'); gi = 0
            for tok in toks:
                if tok == '/':
                    w = ET.SubElement(line, 'w', gap='scribe'); continue
                if tok in ('.', ':') or tok.startswith('['):
                    continue
                a = {'sign': tok}
                k = key_str(tok, counts, nulls)
                if k: a['key'] = k
                else: a['cert'] = 'low'
                if d:
                    if d[gi] == '·': a.update(type='null', basis='decoder')
                    else: a.update(r=d[gi], basis='decoder')
                gi += 1
                ET.SubElement(w, 'g', a)
    write(t, os.path.join(MON, 'xml', '1572-07-13.xml'))


def mondoucet():
    mon_1573(); mon_1572()


# ---------------------------------------------------------------- survey: which targets had signs read from images

def survey(out='papers/lasry/graphic_sign_transcriptions.csv'):
    """Profiles whose cipher uses signs that are not plain letters or digits, and whose ciphertext was
    transcribed from images by the model (transcription.by 'llm from images' or 'mixed')."""
    import csv, pathlib
    rows = []
    root = pathlib.Path(ROOT)
    for p in sorted(list(root.glob('*/profile.json')) + list(root.glob('*/*/profile.json'))):
        d = json.loads(p.read_text(encoding='utf-8'))
        sk = d['system'].get('symbol_kind')
        if sk not in ('symbols', 'letters and symbols', 'digits and symbols'):
            continue
        docs = [x for x in d['documents'] if x.get('transcription', {}).get('by') in ('llm from images', 'mixed')]
        if not docs:
            continue
        toks = [x['length'].get('tokens') for x in docs]
        rows.append({
            'target': p.parent.relative_to(root).as_posix(),
            'symbol_kind': sk,
            'system': d['system'].get('summary', ''),
            'distinct_symbols': d['system'].get('distinct_symbols'),
            'documents_llm': len(docs), 'documents_all': len(d['documents']),
            'tokens_llm': sum(t for t in toks if isinstance(t, int)) if any(isinstance(t, int) for t in toks) else 'unknown',
            'measured': all(x['length'].get('measured') for x in docs),
            'glyph_file': '; '.join(sorted({x['length'].get('file', '') for x in docs} - {''})),
            'image_quality': '; '.join(sorted({str(x['transcription'].get('image_quality')) for x in docs})),
            'outcome': d['outcome'].get('class'),
            'transcription_notes': ' | '.join(x['transcription'].get('notes', '') for x in docs if x['transcription'].get('notes')),
        })
    path = os.path.join(ROOT, out)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    c = collections.Counter(r['symbol_kind'] for r in rows)
    print('%d targets -> %s  (%s)' % (len(rows), out, ', '.join('%s %d' % kv for kv in sorted(c.items()))))


if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('sormano', 'all'): sormano()
    if what in ('mondoucet', 'all'): mondoucet()
    if what in ('survey', 'all'): survey()
