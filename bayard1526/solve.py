import os,sys,random,math
sys.path.insert(0,'..')
from lang import lm
M=lm.load('fr-1530-despatches',order=5,spaces=False)
rows=[l.split()[1:] for l in open('ct.txt') if l.startswith('L')]
toks=[s for r in rows for s in r]
S=sorted(set(toks)); ix={s:i for i,s in enumerate(S)}
ct=[ix[s] for s in toks]
A='abcdefghilmnopqrstuxyz'
def dec(k): return ''.join(k[c] for c in ct)
def sc(k): return M.score_idx(M.encode(dec(k)))
best=None
for run in range(int(sys.argv[1]) if len(sys.argv)>1 else 20):
    k=[random.choice('eainrstuol') for _ in S]; s=sc(k); T=3.0
    for it in range(30000):
        k2=k[:]; k2[random.randrange(len(S))]=random.choice(A)
        s2=sc(k2)
        if s2>s or random.random()<math.exp((s2-s)/T): k,s=k2,s2
        T=max(0.05,T*0.99985)
    if best is None or s>best[0]: best=(s,k[:])
    print(run,round(s/len(ct),3),dec(k)[:120],flush=True)
s,k=best
print('BEST',s/len(ct)); print(' '.join(f'{a}={b}' for a,b in zip(S,k)))
for r in rows: print(''.join(k[ix[x]] for x in r))
