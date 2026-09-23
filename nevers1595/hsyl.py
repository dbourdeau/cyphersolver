"""Homophonic + syllabic annealer: every unit stands for one letter or one consonant+vowel syllable.

usage: python hsyl.py MODE [restarts] [iters]   (MODE as in anneal.py); env CTFILES, ONLYNUM=1 (only figure units
may take syllables), SEED, W.  Full rescoring per move (the plaintext length changes with syllables).
"""
import os, sys, math, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
from anneal import runs

mode = sys.argv[1] if len(sys.argv) > 1 else 'pairall'
restarts = int(sys.argv[2]) if len(sys.argv) > 2 else 3
iters = int(sys.argv[3]) if len(sys.argv) > 3 else 200000
random.seed(int(os.environ.get('SEED', '1')))
K = 5
m = lm.load('fr-1600-letters', order=K, spaces=False)
A = m.A; lp = m.lp
R = runs(mode)
units = sorted({u for r in R for u in r}); ui = {u: i for i, u in enumerate(units)}; U = len(units)
Ri = [np.array([ui[u] for u in r]) for r in R]
LET = [c for c in 'abcdefghilmnopqrstuxyz']
SYL = [c + v for c in 'bcdfglmnpqrstu' for v in 'aeiou' if not (c == 'q' and v != 'u')]
VALS = LET + SYL
enc = [np.array([m.index[ch] for ch in v]) for v in VALS]
isnum = np.array([u[0].isdigit() for u in units])
onlynum = os.environ.get('ONLYNUM', '1') == '1'
FR = {'a': .08, 'b': .01, 'c': .033, 'd': .038, 'e': .16, 'f': .012, 'g': .009, 'h': .008, 'i': .07, 'l': .055,
      'm': .03, 'n': .072, 'o': .052, 'p': .028, 'q': .014, 'r': .065, 's': .082, 't': .07, 'u': .068, 'x': .004,
      'y': .004, 'z': .002}
W = float(os.environ.get('W', '1.0'))
powers = A ** np.arange(K - 1, -1, -1)

def score(key):
    tot = 0.0; n = 0; counts = {}
    for r in Ri:
        x = np.concatenate([enc[key[u]] for u in r])
        n += len(x)
        if len(x) >= K:
            ctx = np.lib.stride_tricks.sliding_window_view(x, K) @ powers
            tot += float(lp[ctx].sum())
        for c in x: counts[c] = counts.get(c, 0) + 1
    pen = 0.0
    for ch, f in FR.items():
        e = f * n; pen += (counts.get(m.index[ch], 0) - e) ** 2 / (e + 2)
    return tot - W * pen, n

best_all = None
for rs in range(restarts):
    key = [random.randrange(len(LET)) for _ in range(U)]
    cur, n = score(key); best = (cur, key[:])
    for it in range(iters):
        T = 12 * (1 - it / iters) + 0.2
        u = random.randrange(U); old = key[u]
        if isnum[u] or not onlynum:
            new = random.randrange(len(VALS)) if random.random() < 0.5 else random.randrange(len(LET))
        else:
            new = random.randrange(len(LET))
        if new == old: continue
        key[u] = new
        s, n = score(key)
        d = s - cur
        if d >= 0 or random.random() < math.exp(d / T):
            cur = s
            if cur > best[0]: best = (cur, key[:])
        else:
            key[u] = old
    _, n = score(best[1])
    print(f'restart {rs}: {best[0] / n:.3f}/char', flush=True)
    if best_all is None or best[0] > best_all[0]: best_all = best
key = best_all[1]
for r in Ri:
    print(''.join(VALS[key[u]] for u in r))
print(' '.join(f'{u}={VALS[key[ui[u]]]}' for u in units))
