"""castelcicala1816: independent check of key.tsv against the contemporary interlinear glosses.
Brice Dudout (Claude Opus 5.5), 14 Nov 2026. Reads only key.tsv and transcripts/R*.txt (not apply.py/corpus.py).
Usage: python3 verify_dudout_20261114.py <path to targets/castelcicala1816>
For every "P:" gloss line, each gloss word is attached to the code group under which it starts (column position:
the P: line, prefix included, is column-aligned with the group line below it). Prints, per glossed line, the groups,
their key value (and grade) and the gloss word starting over them; then a summary of key values that disagree with
the gloss word they sit under."""
import sys, os, re, glob, unicodedata
root = sys.argv[1] if len(sys.argv) > 1 else '.'
K = {}
for l in open(os.path.join(root, 'key.tsv'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a, b, g = (l.rstrip('\n').split('\t') + ['', ''])[:3]
    K[a] = (b, g)
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z]", '', s)
def spans(line):
    return [(m.start(), m.group()) for m in re.finditer(r'\S+', line)]
rows = []
for f in sorted(glob.glob(os.path.join(root, 'transcripts', 'R*.txt'))):
    doc = os.path.basename(f)[:-4]
    L = open(f, encoding='utf-8').read().split('\n')
    for i, l in enumerate(L):
        if not l.startswith('P:') or i + 1 >= len(L): continue
        g = L[i + 1]
        if g.startswith(('P:', 'C:', '#')) or not re.search(r'\d', g): continue
        G = spans(g); W = [(c, w) for c, w in spans(l) if c >= 2 and w != 'P:']
        att = {k: [] for k in range(len(G))}
        for c, w in W:
            # group whose span contains c, else the last group starting before c, else the first
            k = max([j for j, (gc, _) in enumerate(G) if gc <= c] or [0])
            att[k].append(w)
        print(f'== {doc} line {i + 2}')
        for j, (gc, t) in enumerate(G):
            tt = re.sub(r'[^0-9?]', '', t)
            v, gr = K.get(tt, ('', ''))
            gl = ' '.join(att[j])
            print(f'   {t:>7} {v:>14} {gr:1}  | {gl}')
            rows.append((doc, i + 2, tt, v, gr, gl))
print('\n== per glossed line: are the key values found, in order, in the gloss letters of that line?')
# The gloss words are not exactly column-aligned, so the check is order-based: the largest set of key values
# (letters only) that occur in the line's gloss string in order and without overlap (dynamic programming, scored
# by matched letters), so that a short value such as "e" cannot swallow a later match.
from collections import OrderedDict
from functools import lru_cache
lines = OrderedDict()
for doc, ln, t, v, gr, gl in rows: lines.setdefault((doc, ln), []).append((t, v, gr, gl))
tot = {'G': [0, 0], 'X': [0, 0], 'I': [0, 0]}; miss = []
for (doc, ln), gs in lines.items():
    gloss = norm(' '.join(x[3] for x in gs))
    vals = [norm(v) if gr in tot else '' for t, v, gr, gl in gs]
    @lru_cache(None)
    def best(i, pos):
        if i == len(vals): return (0, ())
        r = best(i + 1, pos)
        a = vals[i]
        if a:
            k = gloss.find(a, pos)
            while k >= 0:
                s2, m2 = best(i + 1, k + len(a))
                if s2 + len(a) > r[0]: r = (s2 + len(a), (i,) + m2)
                k = gloss.find(a, k + 1)
        return r
    hit = set(best(0, 0)[1])
    for i, (t, v, gr, gl) in enumerate(gs):
        if not vals[i]: continue
        tot[gr][0] += 1
        if i in hit: tot[gr][1] += 1
        else: miss.append((doc, ln, t, v, gr, gloss))
for g, (n, f) in tot.items(): print(f'grade {g}: {f}/{n} found in order')
for x in miss: print('   not found:', x)
