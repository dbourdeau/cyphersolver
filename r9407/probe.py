"""probe.py "SIGNS" [free-positions or '*sign'] — beam-decode a sign string with the key, letting chosen positions
(0-based, or every occurrence of a sign given as *x) take any letter/'ch'/null. Prints the top 8 readings.
  python r9407/probe.py "jo5yEuw6wxbz#Ey3vcHw" *b *z *#"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
from lang import lm
M = lm.load('de-1500s', spaces=False)
A, K, LP = M.A, M.order, M.lp
key = {}
for l in open(os.path.join(HERE, 'key.txt'), encoding='utf8'):
    p = l.split()
    if len(p) >= 2: key[p[0]] = p[1]
POLY = {'E': ['d', 'ch'], 'n': ['w', 'b', 't'], 'o': ['b', 'w'], '#': ['g', 'u']}
s = sys.argv[1].replace('jo', 'J').replace('mg', 'M')
free = set()
for a in sys.argv[2:]:
    if a.startswith('*'): free |= {i for i, c in enumerate(s) if c == a[1:]}
    else: free.add(int(a))
ALL = list(M.alpha) + ['ch', '']
def lpn(h, c):
    if len(h) < K-1: return -2.5
    x = 0
    for y in h[-(K-1):]: x = x * A + y
    return float(LP[x * A + c])
beams = [(0.0, [], '')]
for i, c in enumerate(s):
    opts = ALL if i in free else POLY.get(c, [key.get(c, '')])
    nb = []
    for sc, h, t in beams:
        for o in opts:
            s2, h2 = sc, list(h)
            for ch in o:
                if ch in M.index: s2 += lpn(h2, M.index[ch]); h2.append(M.index[ch])
            if o == '' and i in free: s2 -= 3.0
            nb.append((s2, h2, t + (o.upper() if i in free else o)))
    nb.sort(key=lambda b: -b[0])
    seen, beams = set(), []
    for b in nb:
        k2 = tuple(b[1][-(K-1):]) + (b[2][-6:],)
        if k2 in seen: continue
        seen.add(k2); beams.append(b)
        if len(beams) >= 300: break
for sc, h, t in beams[:8]: print(round(sc, 1), t)
