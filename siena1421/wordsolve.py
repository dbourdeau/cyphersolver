"""Homophonic anneal for word-divided ciphertext (no. 14 and the like).

Input: a .tok file, one word per whitespace-separated group, signs joined by '_' inside a word
(built by prep14.py). Each sign maps to one letter; word boundaries are spaces in the plaintext and are
scored by a spaced n-gram model.

usage: python wordsolve.py file.tok [model] [iters] [restarts] [order=5] [klw=2] [fix=SIGN:x,...] [seed=1]
"""
import sys, os, math, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm

args = [a for a in sys.argv[1:] if '=' not in a]
opts = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a)
path = args[0]
model = args[1] if len(args) > 1 else 'it-cinquecento'
ITERS = int(args[2]) if len(args) > 2 else 100000
RESTARTS = int(args[3]) if len(args) > 3 else 10
ORDER = int(opts.get('order', 5)); KLW = float(opts.get('klw', 2.0))
M = lm.load(model, order=ORDER, spaces=True)
A = len(M.alpha); SP = M.index[' ']
LET = [c for c in M.alpha if c.isalpha()]
ORD = {'la': 'eiatusnrmocldpqbgfvh'}.get(model, 'eaoinlrtscdpumghfbqvz')
W = np.array([11.8, 11.7, 9.8, 10.1, 6.9, 6.5, 6.4, 5.6, 5.0, 4.5, 3.7, 3.0, 5.1, 2.5, 1.6, 1.1, 1.0, 0.9, 0.5, 0.9, 0.5])
freq = np.full(A, 0.002)
for c, f in zip(ORD, W / W.sum()):
    if c in M.index: freq[M.index[c]] = f
freq[SP] = 0; freq /= freq.sum()

words = [w.split('_') for w in open(path, encoding='utf-8').read().split()]
signs = sorted({s for w in words for s in w}); si = {s: i for i, s in enumerate(signs)}
SPACE = len(signs)
seq = [SPACE]
for w in words: seq += [si[s] for s in w] + [SPACE]
x = np.array(seq)
cnt = np.bincount(x, minlength=SPACE + 1).astype(float)[:SPACE]; N = cnt.sum()
letters = [M.index[c] for c in LET]
fixed = {}
for kv in opts.get('fix', '').split(','):
    if ':' in kv:
        g, c = kv.rsplit(':', 1)
        if g in si: fixed[si[g]] = M.index[c]


def score(key):
    k2 = np.append(key, SP); y = k2[x]
    ctx = np.zeros(len(y) - ORDER + 1, dtype=np.int64)
    for j in range(ORDER): ctx = ctx * A + y[j:len(y) - ORDER + 1 + j]
    s = M.lp[ctx].sum()
    obs = np.bincount(key, weights=cnt, minlength=A) / N; m = obs > 0
    return s - KLW * N * float((obs[m] * np.log(obs[m] / freq[m])).sum())


def show(key):
    return ' '.join(''.join(M.alpha[key[si[s]]] for s in w) for w in words)


rnd = random.Random(int(opts.get('seed', 1)))
free = [i for i in range(SPACE) if i not in fixed]
res = []
for r in range(RESTARTS):
    key = np.array([rnd.choice(letters) for _ in signs])
    for i, c in fixed.items(): key[i] = c
    cur = score(key); T = 10.0; best = (cur, key.copy())
    for it in range(ITERS):
        i = rnd.choice(free); old = key[i]; key[i] = rnd.choice(letters)
        s = score(key)
        if s >= cur or rnd.random() < math.exp((s - cur) / T): cur = s
        else: key[i] = old
        if cur > best[0]: best = (cur, key.copy())
        T = max(0.3, T * (1 - 6.0 / ITERS))
    res.append(best)
    print('%3d %9.1f  %s' % (r, best[0], show(best[1])[:180]), flush=True)
res.sort(key=lambda z: -z[0]); sc, key = res[0]
print('\nbest', round(sc, 1), 'per-char', round(sc / len(x), 3))
print(' '.join('%s=%s' % (s, M.alpha[key[si[s]]]) for s in signs))
print(show(key))
