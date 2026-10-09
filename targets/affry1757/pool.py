# pool.py g1 g2 ... : every occurrence of the groups across all letters (transcr/ overrides cipher_U), with context
import sys, glob, os
import measure_sense as m
from view import load
U = load('U')
for f in glob.glob('transcr/R*.txt'):
    U[os.path.basename(f)[:-4]] = [int(t.split('|')[0]) for l in open(f, encoding='utf8') if not l.startswith('#') for t in l.split()]
def v(x): r = m.val(x); return f'[{x}]' if r is None else r
for q in map(int, sys.argv[1:]):
    print('==', q)
    for r, g in U.items():
        for i, x in enumerate(g):
            if x == q: print(' ', r, i, ' '.join(v(y) for y in g[max(0,i-6):i]), '<<', q, '>>', ' '.join(v(y) for y in g[i+1:i+7]))
