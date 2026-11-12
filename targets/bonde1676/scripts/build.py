# build.py: targets/bonde1676. Standard library only. Run from anywhere: python3 -I scripts/build.py
# Decodes every transcription with the frozen key, checks that each segmentation file rebuilds the decode exactly,
# classes each word unit S / E / N, and writes decryptions/, units.tsv, counts.txt and holes.md.
#
# The decoder and the classing rule are those of the original scripts (scripts/original/b101_decode3.py and
# b101_tally.py, unchanged in substance), so the figures below are the filed ones recomputed, not new scores.
#   Decode: a number whose key tier is A, B, F or P gives its letter value (lower case); tier C gives the value in
#           CAPITALS (a weak guess); tiers W and U (word codes) and numbers not in the key give <n>; a number cut at
#           the gutter ('~') gives [~]; clear words in quotes are shown in guillemets and are outside the count.
#   Class:  a unit is N if the reader flagged it !N (the frozen key gives a wrong letter or no reading); E if flagged
#           !E or if its decoded form holds a capital, '<' or '['; otherwise S. Strict = S / (S + E + N).
#   So a code (<314>) is never counted read, even where the 1675 gloss gives its value (314 = Danmarck).
import os, re, sys, hashlib, collections

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(HERE, *a)
KEY_MD5 = '8e1d93d1188e698ad6dd14826e8ba168'

# Pages decoded once with the frozen key v3 (held out from it), in the order of the memorial.
FRESH = [
    ('f306r_321R', 'b104', '03:42:40'), ('f306v_322L', 'b104', '03:40:25'), ('f307r_322R', 'b104', '03:40:25'),
    ('f307v_323L', 'b101', '03:03:54'), ('f308r_323R', 'b101', '03:03:54'), ('f309v_325L', 'b101', '03:03:54'),
    ('f310r_325R', 'b101', '03:03:54'), ('f310v_326L', 'b101', '03:03:54'), ('f311r_326R', 'b101', '03:03:54'),
]
B101 = [p for p, w, _ in FRESH if w == 'b101']
B104 = [p for p, w, _ in FRESH if w == 'b104']

def md5(path):
    return hashlib.md5(open(path, 'rb').read()).hexdigest()

def load_key(path):
    key = {}
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        g, s, t = l.rstrip('\n').split('\t')
        key[g] = (s, t)
    return key

def decode3(key, path, letter_tiers='ABFP'):
    """b101 decode3.py: one output line per transcription line R<n>."""
    out_lines = []
    for l in open(path, encoding='utf-8'):
        m = re.match(r'(R\d+):\s*(.*)', l)
        if not m:
            continue
        out = []
        for part in re.findall(r'"[^"]*"|\S+', m.group(2)):
            if part.startswith('"'):
                out.append(' «' + part.strip('"') + '» '); continue
            if part.endswith('~'):
                out.append('[~]'); continue
            if part not in key:
                out.append('<%s>' % part); continue
            s, t = key[part]
            out.append(s if t in letter_tiers else (s.upper() if t == 'C' else '<%s>' % part))
        out_lines.append(m.group(1) + ' ' + ''.join(out))
    return out_lines

def decode2(key, path):
    """b99 decode2.py (key v2, used only for the 1st test on image 324)."""
    out_lines = []
    for l in open(path, encoding='utf-8'):
        m = re.match(r'([RrLl]\d+):\s*(.*)', l)
        if not m:
            continue
        out = []
        for part in re.findall(r'"[^"]*"|\S+', m.group(2)):
            if part.startswith('"'):
                out.append(' «' + part.strip('"') + '» '); continue
            cut = part.endswith('~'); g = re.sub(r'[^0-9]', '', part)
            if cut or not g:
                out.append('[~]'); continue
            if g not in key:
                out.append('<%s>' % g); continue
            s, t = key[g]
            out.append(s if t in 'ABF' else ('<%s>' % g if t in 'UW' else ('' if t == 'N' else s.upper())))
        out_lines.append(m.group(1) + ' ' + ''.join(out))
    return out_lines

def tally(dec_lines, seg_path):
    """b101 tally.py: the segmentation must rebuild the decode exactly; then class each unit."""
    dec = ''.join(re.sub(r'«[^»]*»', '', l.split(' ', 1)[1]).replace(' ', '').strip() for l in dec_lines if l.strip())
    segs = []
    for u in open(seg_path, encoding='utf-8').read().split():
        flag = None
        if u.endswith('!N') or u.endswith('!E'):
            flag = u[-1]; u = u[:-2]
        s, _, r = u.partition('=')
        segs.append((s, r, flag))
    rebuilt = ''.join(s for s, _, _ in segs)
    if rebuilt != dec:
        i = next((k for k in range(min(len(rebuilt), len(dec))) if rebuilt[k] != dec[k]), min(len(rebuilt), len(dec)))
        sys.exit('MISMATCH %s at %d\n seg: %s\n dec: %s' % (seg_path, i, rebuilt[max(0, i-30):i+30], dec[max(0, i-30):i+30]))
    rows = []
    for s, r, flag in segs:
        weak = bool(re.search(r'[A-ZÅÄÖ<\[]', s))
        c = 'N' if flag == 'N' else ('E' if flag == 'E' or weak else 'S')
        rows.append((s, c, r, flag))
    return rows

def why(s, c, flag):
    if c == 'S':
        return ''
    k = []
    if flag == 'N': k.append('flagged N by the reader (key gives a wrong letter, or no reading)')
    if flag == 'E': k.append('flagged E by the reader (emended)')
    if '[~]' in s: k.append('numeral cut at the gutter or edge')
    for n in re.findall(r'<(\d+)>', s): k.append('no value for %s' % n)
    if re.search(r'[A-Z]', s): k.append('weak C-tier value')
    return '; '.join(k)

def counts_block(name, rows, by_line=None):
    S = sum(c == 'S' for _, c, _, _ in rows); E = sum(c == 'E' for _, c, _, _ in rows); N = sum(c == 'N' for _, c, _, _ in rows)
    T = S + E + N
    return S, E, N, T

def pct(a, b):
    return '%d/%d = %.2f%%' % (a, b, 100.0 * a / b)

def main():
    key_path = P('key.tsv')
    assert md5(key_path) == KEY_MD5, 'key.tsv is not the frozen key v3'
    key = load_key(key_path)
    os.makedirs(P('decryptions'), exist_ok=True)
    out = ['counts.txt: written by scripts/build.py. Strict count per word unit (rule in the header of scripts/build.py).',
           'S = every sign a frozen key-v3 letter value and the word spelt; E = holds a code, a sign with no value, a weak',
           'value or a gutter cut, or emended; N = the frozen key gives a wrong letter or no reading. Clear words outside the count.',
           'key.tsv md5 %s (= the key v3 frozen 12 Nov 2026 02:55:22 UTC, before any of these pages was transcribed).' % md5(key_path), '']
    allrows = []; table = []
    out.append('## A. The memorial, pages decoded once with key v3 frozen (held out from the key)')
    out.append('')
    for page, worker, t in FRESH:
        tx = P('transcriptions', page + '.txt'); seg = P('segmentation', 'seg_' + page + '.txt')
        dec = decode3(key, tx)
        open(P('decryptions', page + '.txt'), 'w', encoding='utf-8').write(
            '# Decryption of transcriptions/%s.txt with key.tsv (v3), written by scripts/build.py. «» = clear on the page; '
            '[~] = numeral cut at the gutter; <n> = no value in the key; CAPITALS = weak value. First decoded once on 12 Nov 2026 at %s UTC (%s).\n' % (page, t, worker)
            + '\n'.join(dec) + '\n')
        rows = tally(dec, seg)
        S, E, N, T = counts_block(page, rows)
        allrows += [(page, i + 1) + r for i, r in enumerate(rows)]
        table.append((page, S, E, N, T))
        out.append('%s  transcription md5 %s' % (page, md5(tx)))
        out.append('  S %d + E %d + N %d = %d units; strict %s; S+E %s' % (S, E, N, T, pct(S, T), pct(S + E, T)))
    def pool(pages, label):
        r = [x for x in table if x[0] in pages]
        S = sum(x[1] for x in r); E = sum(x[2] for x in r); N = sum(x[3] for x in r); T = sum(x[4] for x in r)
        out.append('')
        out.append(label)
        out.append('  S ' + ' + '.join(str(x[1]) for x in r) + ' = %d' % S)
        out.append('  E ' + ' + '.join(str(x[2]) for x in r) + ' = %d' % E)
        out.append('  N ' + ' + '.join(str(x[3]) for x in r) + ' = %d' % N)
        out.append('  units ' + ' + '.join(str(x[4]) for x in r) + ' = %d' % T)
        out.append('  strict %s; S+E %s' % (pct(S, T), pct(S + E, T)))
        return S, T
    pool(B101, 'Filed in #453 (b101: f.307v, 308r, 309v, 310r, 310v, 311r)')
    pool(B104, 'Filed in the 2nd comment on #453 (b104: f.306r, 306v, 307r)')
    pool([p for p, _, _ in FRESH], 'Whole memorial, all nine held-out pages (not filed as one figure before)')

    # A2. corrections declared in overrides.tsv (downgrades only), applied after the filed tally
    ov = {}
    for l in open(P('overrides.tsv'), encoding='utf-8'):
        if l.startswith('#') or l.startswith('page\t') or not l.strip(): continue
        pg, un, dec_, frm, to, reason = l.rstrip('\n').split('\t')
        ov[(pg, int(un))] = (dec_, frm, to, reason)
    fixed = []
    for page, i, s, cl, r, flag in allrows:
        if (page, i) in ov:
            dec_, frm, to, reason = ov[(page, i)]
            assert dec_ == s and frm == cl, 'override does not match unit %s %d' % (page, i)
            fixed.append((page, i, s, to, r, flag, cl, reason))
        else:
            fixed.append((page, i, s, cl, r, flag, cl, ''))
    assert sum(1 for x in fixed if x[7]) == len(ov), 'unused override'
    out += ['', '## A2. After the corrections in overrides.tsv (%d units downgraded S -> N; see NOTES.md, Corrections)' % len(ov), '']
    table2 = []
    for page, _, _ in FRESH:
        r = [x for x in fixed if x[0] == page]
        S = sum(x[3] == 'S' for x in r); E = sum(x[3] == 'E' for x in r); N = sum(x[3] == 'N' for x in r)
        d = sum(1 for x in r if x[7])
        table2.append((page, S, E, N, S + E + N))
        out.append('%s  S %d + E %d + N %d = %d; strict %s%s' % (page, S, E, N, S + E + N, pct(S, S + E + N), ('  (%d downgraded)' % d) if d else ''))
    table_filed = table; table = table2
    pool(B101, 'Corrected, the six pages of #453')
    pool(B104, 'Corrected, the three opening pages (no change)')
    pool([p for p, _, _ in FRESH], 'Corrected, whole memorial, nine pages: THE FIGURE')
    table = table_filed
    allrows = [(x[0], x[1], x[2], x[3], x[4], x[5]) for x in fixed]
    filed_class = {(x[0], x[1]): x[6] for x in fixed}
    ov_reason = {(x[0], x[1]): x[7] for x in fixed}

    # B. image 324, the page the key's values 100-176 were fixed on
    out += ['', '## B. Image 324 (f.308v-309r): the page the key was finished on. NOT held out from v3.', '']
    k2 = load_key(P('gloss', 'KEY_v2.tsv'))
    d2 = decode2(k2, P('transcriptions', 'f308v-309r_324_heldout_v2.txt'))
    open(P('decryptions', 'f308v-309r_324_heldout_v2.txt'), 'w', encoding='utf-8').write(
        '# Decryption of the 30 held-out lines of image 324 with gloss/KEY_v2.tsv (b99 decode2 rule), the first test (12 Nov 2026 02:50 UTC).\n' + '\n'.join(d2) + '\n')
    d3 = decode3(key, P('transcriptions', 'f308v-309r_324_heldout_v2.txt'))
    open(P('decryptions', 'f308v-309r_324_v3_insample.txt'), 'w', encoding='utf-8').write(
        '# The same lines decoded with key.tsv (v3). IN-SAMPLE: v3 values P were fixed from these lines. Shown for reading, not counted.\n' + '\n'.join(d3) + '\n')
    # the training file numbers its lines l1..l14; renumbered R1..R14 in a temporary copy, decoded for display only
    lines =[l for l in open(P('transcriptions', 'f308v_324L_lines1-14_training.txt'), encoding='utf-8') if re.match(r'l\d+:', l)]
    tmp = P('decryptions', '.tmp_training.txt')
    open(tmp, 'w', encoding='utf-8').write(''.join('R' + l[1:] for l in lines))
    dtr = decode3(key, tmp); os.remove(tmp)
    open(P('decryptions', 'f308v_324L_lines1-14_training.txt'), 'w', encoding='utf-8').write(
        '# Training lines 1-14 of image 324 left decoded with key.tsv (v3). TRAINING: values F of the key come from these lines. Not counted.\n' + '\n'.join(dtr) + '\n')
    u = [l.rstrip('\n').split('\t') for l in open(P('segmentation', 'units_f308v-309r_324_heldout_v2.tsv'), encoding='utf-8') if l.strip() and not l.startswith('#')]
    c = collections.Counter(x[1] for x in u)
    out.append('First test, key v2 frozen 02:49:24 UTC, held-out lines frozen 02:50:10, decoded once (b99): units classed by hand in')
    out.append('segmentation/units_f308v-309r_324_heldout_v2.tsv (counted here): S %d + E %d + N %d = %d; strict %s; S+E %s'
               % (c['S'], c['E'], c['N'], len(u), pct(c['S'], len(u)), pct(c['S'] + c['E'], len(u))))
    out.append('v3 on image 324 is in-sample (its tier-P values were read off these lines after that test): no count is given.')

    # C. blind second transcription (b103) of f.307v and f.309v
    out += ['', '## C. Second transcription of f.307v and f.309v (b103), frozen 03:16:08 UTC before any b101 file was opened', '']
    bS = bT = 0
    for page in ('f307v_323L', 'f309v_325L'):
        d = decode3(key, P('second_transcription', 'blindR_' + page + '.txt'))
        rows = tally(d, P('second_transcription', 'seg_blind_' + page + '.txt'))
        S, E, N, T = counts_block(page, rows); bS += S; bT += T
        out.append('blind %s: S %d + E %d + N %d = %d; strict %s' % (page, S, E, N, T, pct(S, T)))
    fS = sum(x[1] for x in table if x[0] in ('f307v_323L', 'f309v_325L')); fT = sum(x[4] for x in table if x[0] in ('f307v_323L', 'f309v_325L'))
    out.append('blind both: strict %s; first transcription on the same two pages: strict %s' % (pct(bS, bT), pct(fS, fT)))
    out.append('Numerals read in full, blind against first: see controls/compare_blind.txt (scripts/compare_blind.py).')

    # units.tsv and holes.md
    with open(P('units.tsv'), 'w', encoding='utf-8') as f:
        f.write('page\tunit\tdecoded\tclass\tclass as filed\treading\tnot read because\n')
        for page, i, s, cl, r, flag in allrows:
            f.write('%s\t%d\t%s\t%s\t%s\t%s\t%s\n' % (page, i, s, cl, filed_class[(page, i)], r, ov_reason[(page, i)] or why(s, cl, flag)))
    holes = ['# Holes: every word unit of the nine held-out pages that is not counted read', '',
             'Written by scripts/build.py from units.tsv. A unit is a hole when its class is E or N (rule in scripts/build.py), after overrides.tsv.',
             'The reason column is the script\'s reading of the decoded form, not a hand classification.', '',
             '## 1. Totals by page', '', '| page | units | S | E | N | gutter cut | no value (code or sign) | weak value | flagged by reader or overrides.tsv |', '|---|---|---|---|---|---|---|---|---|']
    tot = collections.Counter()
    for page, S, E, N, T in table2:
        h = [x for x in allrows if x[0] == page and x[3] != 'S']
        g = sum('[~]' in x[2] for x in h); v = sum('<' in x[2] for x in h); w = sum(bool(re.search(r'[A-Z]', x[2])) for x in h); fl = sum(x[5] is not None or bool(ov_reason[(x[0], x[1])]) for x in h)
        holes.append('| %s | %d | %d | %d | %d | %d | %d | %d | %d |' % (page, T, S, E, N, g, v, w, fl))
        for k, val in zip('TSENgvwf', (T, S, E, N, g, v, w, fl)): tot[k] += val
    holes.append('| all | %d | %d | %d | %d | %d | %d | %d | %d |' % tuple(tot[k] for k in 'TSENgvwf'))
    holes.append('')
    holes.append('A unit can fall in more than one of the last four columns.')
    holes += ['', '## 2. Numbers with no value in key v3, as they occur in the nine pages', '', '| number | occurrences | pages | key row | sense from context (not read) |', '|---|---|---|---|---|']
    occ = collections.defaultdict(list)
    for page, _, _ in FRESH:
        for l in open(P('transcriptions', page + '.txt'), encoding='utf-8'):
            m = re.match(r'R\d+:\s*(.*)', l)
            if not m: continue
            for part in re.findall(r'"[^"]*"|\S+', m.group(1)):
                if part.startswith('"') or part.endswith('~'): continue
                if part not in key or key[part][1] not in 'ABFPC': occ[part].append(page)
    sense = {'314': 'Danmarck (1675 gloss; counted not read by rule)', '267': 'alliance', '324': 'discours', '463': 'reputation?',
             '173': 'null?', '174': 'null?', '175': 'null?', '176': 'null?', '177': 'null?', '178': 'null?', '3': 'null?', '4': 'null?', '8': 'null?'}
    # letter values proposed after the b101 decode (its REPORT, 'corrections found after the test'); not in v3, never counted
    for n, v in (('99', 'st'), ('124', 'st'), ('157', 'st'), ('44', 'x'), ('155', 'x'), ('109', 'ff'), ('120', 'q'), ('129', 'y'),
                 ('76', 'g'), ('145', 'l'), ('162', 'o'), ('111', 'h'), ('134', 'h'), ('130', 'p'), ('115', 'll'), ('139', 'll'), ('123', 'ss')):
        sense[n] = '%s (proposed after the test; not counted)' % v
    for n in sorted(occ, key=lambda x: (len(occ[x]) * -1, int(x))):
        kr = '%s %s' % key[n] if n in key else 'not in key'
        holes.append('| %s | %d | %s | %s | %s |' % (n, len(occ[n]), ', '.join('%s x%d' % (p, occ[n].count(p)) for p in dict.fromkeys(occ[n])), kr, sense.get(n, '')))
    holes += ['', '## 3. Every hole', '', '| page | unit | decoded | class | reading | not read because |', '|---|---|---|---|---|---|']
    for page, i, s, cl, r, flag in allrows:
        if cl != 'S':
            holes.append('| %s | %d | `%s` | %s | %s | %s |' % (page, i, s, cl, r, ov_reason[(page, i)] or why(s, cl, flag)))
    open(P('holes.md'), 'w', encoding='utf-8').write('\n'.join(holes) + '\n')
    open(P('counts.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('\n'.join(out))

if __name__ == '__main__':
    main()
