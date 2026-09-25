"""Homophonic solver where a sign may stand for a letter OR a frequent Italian bigram (syllabic/digraph signs).
usage: python sylsolve.py FILE [model] [restarts] [iters] [seed=1] [nbig=40] [bpen=0.5]"""
import sys, os, re, math, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
a = [x for x in sys.argv[1:] if '=' not in x]; o = dict(x.split('=', 1) for x in sys.argv[1:] if '=' in x)
path = a[0]; model = a[1] if len(a) > 1 else 'it-cinquecento'
R = int(a[2]) if len(a) > 2 else 8; IT = int(a[3]) if len(a) > 3 else 60000
K = int(o.get('order', 4)); M = lm.load(model, order=K, spaces=False); A = len(M.alpha)
BIG = ['ch','er','on','an','re','di','la','te','ra','co','to','ar','al','en','in','de','ta','ti','li','ri','no','or','le','se','es','ne','si','st','nt','ma','ll','ss','tt','qu','gn','gl','pe','mo','io','lo'][:int(o.get('nbig', 40))]
LET = [c for c in M.alpha if c.isalpha()]
units = [[M.index[c]] for c in LET] + [[M.index[b[0]], M.index[b[1]]] for b in BIG]
names = LET + BIG
NL = len(LET); BPEN = float(o.get('bpen', 0.5))
runs = []
for line in open(path, encoding='utf-8'):
    t = line.split()
    if t: runs.append(t)
signs = sorted({s for r in runs for s in r}); si = {s: i for i, s in enumerate(signs)}; S = len(signs)
cnt = np.zeros(S)
for r in runs:
    for s in r: cnt[si[s]] += 1
ORD = 'eaoinlrtscdpumghfbqvz'
WF = np.array([11.8, 11.7, 9.8, 10.1, 6.9, 6.5, 6.4, 5.6, 5.0, 4.5, 3.7, 3.0, 5.1, 2.5, 1.6, 1.1, 1.0, 0.9, 0.5, 0.9, 0.5]); WF /= WF.sum()
freq = np.full(A, 1e-3)
for c, f in zip(ORD, WF):
    if c in M.index: freq[M.index[c]] = f
freq /= freq.sum()
rs = [np.array([si[s] for s in r]) for r in runs]
def expand(key):
    out = []
    for r in rs:
        seq = []
        for i in r: seq += units[key[i]]
        out.append(np.array(seq))
    return out
def score(key):
    tot = 0.0; allv = []
    for y in expand(key):
        n = len(y) - K + 1
        if n <= 0: continue
        ctx = np.zeros(n, dtype=np.int64)
        for j in range(K): ctx = ctx * A + y[j:n + j]
        tot += M.lp[ctx].sum(); allv.append(y)
    v = np.concatenate(allv); ob = np.bincount(v, minlength=A) / len(v); m = ob > 0
    kl = float((ob[m] * np.log(ob[m] / freq[m])).sum())
    nb = sum(cnt[i] for i in range(S) if key[i] >= NL)
    return tot - 1.5 * len(v) * kl - BPEN * nb
rnd = random.Random(int(o.get('seed', 1))); res = []
for r in range(R):
    key = np.array([rnd.randrange(NL) for _ in range(S)])
    cur = score(key); T = 6.0
    for it in range(IT):
        i = rnd.randrange(S); old = key[i]
        key[i] = rnd.randrange(len(units)) if rnd.random() < 0.35 else rnd.randrange(NL)
        s = score(key)
        if s >= cur or rnd.random() < math.exp((s - cur) / T): cur = s
        else: key[i] = old
        T = max(0.15, T * (1 - 7.0 / IT))
    res.append((cur, key.copy()))
    txt = ' | '.join(''.join(M.alpha[c] for c in y) for y in expand(key))
    print('%3d %9.1f %s' % (r, cur, txt[:160]), flush=True)
res.sort(key=lambda z: -z[0]); sc, key = res[0]
print('\nscore', round(sc, 1)); print(' '.join('%s=%s' % (s, names[key[si[s]]]) for s in signs))
print(' | '.join(''.join(M.alpha[c] for c in y) for y in expand(key)))
