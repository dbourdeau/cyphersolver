"""Homophonic anneal for R1871 (Foscarini 1680): self-delimiting tokens [1-4]*[5-90], one letter per token type."""
import os, re, sys, random, math
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
toks = [x for l in open(os.path.join(HERE, 'runs.txt')) for x in l.split(':')[1].split()]
types = sorted(set(toks), key=lambda t: -toks.count(t))
tid = {t: i for i, t in enumerate(types)}
seq = np.array([tid[t] for t in toks])

LP = np.load(os.path.join(HERE, 'q4.npy'))  # clean 4-gram, built by buildq4.py
ALPH = 'abcdefghilmnopqrstuz'
N = 20

def score(mp):
    y = mp[seq]
    return LP[((y[:-3] * N + y[1:-2]) * N + y[2:-1]) * N + y[3:]].sum()

best_all = None
for restart in range(int(os.environ.get('R', 8))):
    rng = random.Random(restart)
    mp = np.array([rng.randrange(len(ALPH)) for _ in types])
    cur = score(mp); T = 5.0
    for it in range(40000):
        i = rng.randrange(len(types)); old = mp[i]
        mp[i] = rng.randrange(len(ALPH))
        new = score(mp)
        if new >= cur or rng.random() < math.exp((new - cur) / T):
            cur = new
        else:
            mp[i] = old
        T = max(0.2, T * 0.9998)
    txt = ''.join(ALPH[k] for k in mp[seq])
    print(restart, round(cur / len(seq), 3), txt[:160], flush=True)
    if best_all is None or cur > best_all[0]:
        best_all = (cur, mp.copy())
mp = best_all[1]
print(''.join(ALPH[k] for k in mp[seq]))
print({t: ALPH[mp[tid[t]]] for t in types[:60]})
