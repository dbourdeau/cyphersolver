"""Scan unassigned digit pairs of R91 for a missing syllable code: add one value to one pair, report the score gain."""
import importlib, copy, sys
import vdot
base = {k: list(v) for k, v in importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else 'k2d').KEY.items()}
for c in vdot.DOTTED:
    if c in base: base[c] = [v for v in base[c] if v not in vdot.DOTTED[c]]
D = vdot.Dec(B=16)
s0 = D.run(base)[0]
from collections import Counter
dg = ''.join(str(x) for x in D.dig if x >= 0)
pc = Counter(dg[i:i + 2] for i in range(len(dg) - 1))
pairs = [p for p, n in pc.most_common() if p not in base and n >= 15]
vals = [c + v for c in 'bcdfglmnprstuz' for v in 'aeiou'] + ['per', 'con', 'che', 'non', 'et', 'qu', 'gli', 'gn', 'ch', 'st', 'pr', 'tr', 'nt']
res = []
for p in pairs:
    best = (-1e9, None)
    for v in vals:
        k = dict(base); k[p] = [v]
        g = D.run(k)[0] - s0
        if g > best[0]: best = (g, v)
    res.append((best[0], p, best[1], pc[p]))
    print(f'{p} (x{pc[p]}): best {best[1]} {best[0]:+.1f}', flush=True)
print(sorted(res, reverse=True)[:12])
