"""Polish a key: low-temperature hill-climb from a given mapping, order-6 sparse LM if available."""
import sys, os, json, random, math, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')
from lang import lm
import numpy as np
from solve import load_runs
M = lm.load(os.environ.get('MODEL','fr-1530-despatches'), order=int(os.environ.get('ORDER','5')), spaces=False)
start = json.load(open(sys.argv[1]))
IT = int(sys.argv[2]) if len(sys.argv) > 2 else 300000
runs = [r for r in load_runs() if len(r) >= 4]
signs = sorted({s for r in runs for s in r}); si = {s:i for i,s in enumerate(signs)}
seq = [np.array([si[s] for s in r]) for r in runs]
occ = [[j for j,r in enumerate(seq) if i in set(r.tolist())] for i in range(len(signs))]
LET='abcdefghilmnopqrstuxy'; alpha=[M.encode(c)[0] for c in LET]
inv={M.encode(c)[0]:c for c in LET}
key=np.array([M.encode(start.get(s,'e'))[0] for s in signs])
rsc=np.array([M.score_idx(key[r]) for r in seq]); cur=rsc.sum(); best=(cur,key.copy())
for it in range(IT):
    T=1.5*(1-it/IT)+0.01
    i=random.randrange(len(signs)); old=int(key[i]); nv=random.choice(alpha)
    if nv==old: continue
    key[i]=nv; js=occ[i]; ns=np.array([M.score_idx(key[seq[j]]) for j in js])
    new=rsc.sum()-rsc[js].sum()+ns.sum()
    if new>=cur or random.random()<math.exp((new-cur)/T):
        cur=new; rsc[js]=ns
        if cur>best[0]: best=(cur,key.copy())
    else: key[i]=old
key=best[1]; mp={s:inv[int(key[i])] for i,s in enumerate(signs)}
print(json.dumps(mp,sort_keys=True))
txt=[''.join(mp[s] for s in r) for r in runs]
print('per-char', round(sum(M.score(t) for t in txt)/sum(len(t) for t in txt),3))
for t in txt: print(t)
