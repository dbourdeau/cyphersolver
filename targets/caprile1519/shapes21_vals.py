# LM value chosen for each QB occurrence (k-th QB in its line), R1136/R1139, union priors as in lookalike21.py
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import beam21, lookalike21, shapes21
from lang import lm
m = lm.load('it-cinquecento', spaces=False); P = beam21.priors()
for pair, labs in lookalike21.PAIRS.items():
    for l in labs: P[l] = {v: math.log(1 / len(lookalike21.UNION[pair])) for v in lookalike21.UNION[pair]}
for src, fn in [('R1136', 'r1136_pass4.txt'), ('R1139', 'r1139_pass4.txt')]:
    for li, line in enumerate([l for l in open(os.path.join(HERE, fn), encoding='utf8') if l.startswith(src + ' ')], 1):
        T = shapes21.tokens(line)
        idx = {}
        k = 0
        for j, t in enumerate(T):
            if t == 'QB': idx[j] = k; k += 1
        vals = [v for t, v in lookalike21.decode_track(beam21.tokens(line), m, P) if t == 'QB']
        for j, kk in idx.items():
            print(f'{src[-2:]}L{li}#{j}', kk, vals[kk] if kk < len(vals) else '?')
