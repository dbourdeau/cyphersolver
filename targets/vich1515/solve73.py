"""Anneal a homophonic key for N.73 against the esp318 Spanish 5-gram model.
mode 'chars': lowercase tokens split into letters (each a cipher symbol); uppercase labels are symbols."""
import pickle, numpy as np, sys, math, random, collections, re
sys.path.insert(0, '../esp318')
from lm import ALPHA, IDX
L = len(ALPHA)
tabs = pickle.load(open('../esp318/lm_tabs.pkl', 'rb')); lp1, lp2, lp3, lp4, lp5 = tabs[1:]
mode = sys.argv[1]; seeds = int(sys.argv[2]); iters = int(sys.argv[3])
units = []; lines = []
for ln in open('n73_transcription.txt', encoding='utf-8'):
    if not re.match(r'L\d+:', ln): continue
    tag, body = ln.split(':', 1)
    for t in body.split():
        if t in ('?', 'SUPNO'): continue
        if mode == 'chars' and t.islower(): units += list(t); lines += [tag]*len(t)
        else: units.append(t); lines.append(tag)
syms = sorted(set(units)); sid = {s: i for i, s in enumerate(syms)}; seq = np.array([sid[u] for u in units]); S = len(syms)
n = len(seq); idx = np.arange(4, n)
freq = collections.Counter(units)
print('units', n, 'symbols', S)
pexp = np.exp(lp1)
def score(key):
    d = key[seq]
    s = lp5[d[idx-4], d[idx-3], d[idx-2], d[idx-1], d[idx]].sum()
    obs = np.bincount(d, minlength=L)/n; kl = (obs*np.log(np.maximum(obs, 1e-9)/pexp)).sum()
    return s - 0.5*n*kl
def anneal(seed):
    rng = random.Random(seed); key = np.array([rng.randrange(L) for _ in range(S)])
    cur = score(key); best, bk = cur, key.copy()
    for it in range(iters):
        T = 3.0*(0.03/3.0)**(it/iters); s = rng.randrange(S); old = key[s]; key[s] = rng.randrange(L)
        new = score(key)
        if new >= cur or rng.random() < math.exp((new-cur)/T): cur = new
        else: key[s] = old
        if cur > best: best, bk = cur, key.copy()
    return best, bk
res = [anneal(sd) for sd in range(seeds)]
for b, k in res: print('seed', round(b/n, 3), ''.join(ALPHA[x] for x in k[seq][:80]))
b, k = max(res, key=lambda r: r[0])
print('key', {s: ALPHA[k[sid[s]]] for s in sorted(syms, key=lambda s: -freq[s])})
out = collections.OrderedDict()
for u, t in zip(units, lines): out.setdefault(t, []).append(ALPHA[k[sid[u]]])
open(f'n73_solve_{mode}.txt', 'w').write('\n'.join(f'{t} {"".join(v)}' for t, v in out.items()))
