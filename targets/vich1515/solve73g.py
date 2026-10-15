"""N.73: anneal uppercase symbols as a homophonic alphabet; lowercase code words break context."""
import pickle, numpy as np, sys, math, random, collections, re
sys.path.insert(0, '../esp318')
from lm import ALPHA
L = len(ALPHA)
lp = pickle.load(open('../esp318/lm_tabs.pkl', 'rb'))
seeds, iters = int(sys.argv[1]), int(sys.argv[2])
fixed = dict(a.split('=') for a in sys.argv[3:])
runs = []; cur = []
for ln in open('n73_transcription.txt', encoding='utf-8'):
    if not re.match(r'L\d+:', ln): continue
    for t in ln.split(':', 1)[1].split():
        if t.isupper() and t != 'SUPNO': cur.append(t)
        else:
            if cur: runs.append(cur); cur = []
if cur: runs.append(cur)
syms = sorted({t for r in runs for t in r}); sid = {s: i for i, s in enumerate(syms)}; S = len(syms)
flat = np.array([sid[t] for r in runs for t in r]); pos = np.array([k for r in runs for k in range(len(r))])
n = len(flat); I = [np.where(np.minimum(pos, 4) == o)[0] for o in range(5)]
pexp = np.exp(lp[1]); freq = collections.Counter(t for r in runs for t in r)
def score(key):
    d = key[flat]; s = 0
    for o in range(5):
        ix = I[o]; s += lp[o+1][tuple(d[ix-o+j] for j in range(o+1))].sum()
    obs = np.bincount(d, minlength=L)/n
    return s - 0.5*n*(obs*np.log(np.maximum(obs, 1e-9)/pexp)).sum()
free = [s for s in range(S) if syms[s] not in fixed]
def anneal(seed):
    rng = random.Random(seed); key = np.array([ALPHA.index(fixed[s]) if s in fixed else rng.randrange(L) for s in syms])
    cur = score(key); best, bk = cur, key.copy()
    for it in range(iters):
        T = 3.0*(0.03/3.0)**(it/iters); s = rng.choice(free); old = key[s]; key[s] = rng.randrange(L)
        new = score(key)
        if new >= cur or rng.random() < math.exp((new-cur)/T): cur = new
        else: key[s] = old
        if cur > best: best, bk = cur, key.copy()
    return best, bk
res = [anneal(sd) for sd in range(seeds)]
for b, k in sorted(res, key=lambda r: -r[0]):
    print(round(b/n, 3), ' '.join(f'{s}={ALPHA[k[sid[s]]]}' for s in sorted(syms, key=lambda s: -freq[s])[:20]))
b, k = max(res, key=lambda r: r[0])
print('\n'.join(''.join(ALPHA[k[sid[t]]] for t in r) for r in runs if len(r) >= 6)[:1500])
