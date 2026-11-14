"""Independent check of maisse1592 f. 370 (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).
1) Decodes texts/f370_figures.txt and texts/f373_figures.txt with key1.tsv only (not decode.py / align scripts) and
   compares the letters with the reading (accents, case, punctuation removed; difflib letter alignment).
2) Compares a blind re-reading of five f. 370 lines (BLIND below; lines drawn with random.seed(370) from r23-r30 and
   v00-v31) with f370_figures.txt, group by group.
usage: python3 verify_dudout_20261114.py targets/maisse1592
"""
import sys, re, difflib, unicodedata
T = sys.argv[1] if len(sys.argv) > 1 else '.'
key = {}
for l in open(f'{T}/key1.tsv', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k, v = l.rstrip('\n').split('\t')[:2]; key[k] = v
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isalpha() and ord(c) < 128)
    return s.replace('j', 'i').replace('v', 'u').replace('w', 'u')
def figures(path):
    lines = {}
    for l in open(path, encoding='utf8'):
        m = re.match(r'([rv]\d\d):\s*(.*)', l)
        if m: lines[m.group(1)] = m.group(2).split()
    return lines
def decode(groups):
    out = []
    for g in groups:
        g0 = g.rstrip('?')
        if g0 in key: out.append(key[g0] if len(key[g0]) <= 2 else '#' * len(norm(key[g0])))
        elif g0 == 'w': out.append('d')
        elif g0 == '~' or g0 == 'G' or g0.startswith('X'): continue
        else: out.append('?')
    return ''.join(out)
def reading_body(path):
    t = open(path, encoding='utf8').read()
    m = re.search(r'## Reading\s*\n(.*?)(\n## |\Z)', t, re.S)
    return norm(re.sub(r'\[[^\]]*\]|\{[^}]*\}', lambda x: x.group(0)[1:-1], m.group(1) if m else t))
for f in ('f370', 'f373'):
    figs = figures(f'{T}/texts/{f}_figures.txt')
    dec = norm(''.join(decode(g) for g in figs.values()).replace('#', 'x'))
    rd = reading_body(f'{T}/texts/{f}_reading.md')
    sm = difflib.SequenceMatcher(None, dec, rd, autojunk=False)
    same = sum(b.size for b in sm.get_matching_blocks())
    print(f'{f}: {sum(len(g) for g in figs.values())} groups, {len(dec)} decoded letters; '
          f'{same} align with the reading ({same/len(dec):.1%} of decoded, {same/len(rd):.1%} of {len(rd)} reading letters)')
BLIND = {
 'r30': '11 18 9 13 68 13 4 72 7 12 9 11 15 19 11 19 13 19 7? 7 19 11 22 10 11 17 7 66 7 4 16 11 17 10 11 10 11 5 7',
 'v09': '7 66 4 12 10 21 14 16 11 12 10 16 11 2 7 16 10 11 11 18 11 6 14 11 17 9 3 11 16 15 19 11 16 4 11 12',
 'v10': '17 9 11 7 6 13 12 14 16 11 4 19 10 4 9 11 15 19 11 14 13 19 16 11 17 9 3 7 19 1 11 16 5 11 17 14 16 13',
 'v25': '5 11 17 16 11 17 13 5 19 18 4 13 12 17 10 19 25? 11 12 9 11 15 19 4 18 13 19 9 3 11 9 11 16 13 21',
 'v29': '14? 9 13 12 18 16 7 4 12 8 18 10 11 17 19 4 19 16 11 7 73 11 12 10 7 12 18 15 19 4 5 5 19 21'}
figs = figures(f'{T}/texts/f370_figures.txt')
ta = tb = tm = 0
for ln, b in BLIND.items():
    a = [g.rstrip('?') for g in figs[ln] if g != 'G']; b = [g.rstrip('?') for g in b.split()]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False); m = sum(x.size for x in sm.get_matching_blocks())
    ta += len(a); tb += len(b); tm += m
    diffs = [(op, a[i1:i2], b[j1:j2]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']
    print(f'{ln}: figures {len(a)}, blind {len(b)}, agree {m}', diffs)
print(f'blind sample: {tm} groups agree; Dice {2*tm/(ta+tb):.1%} ({ta} vs {tb} groups)')
