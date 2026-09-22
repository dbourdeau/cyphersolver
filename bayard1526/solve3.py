import sys,random,math
sys.path.insert(0,'..')
from lang import lm
M=lm.load('fr-1530-despatches',order=5,spaces=False)
rows=[l.split()[1:] for l in open('ct2.txt') if l.startswith('L')]
toks=[s for r in rows for s in r]
S=sorted(set(toks)); ix={s:i for i,s in enumerate(S)}
ct=[ix[s] for s in toks]
A='abcdefghilmnopqrstuxyz'
pin=dict(a.split('=') for a in sys.argv[2:])
def dec(k): return ''.join(k[c] for c in ct)
def sc(k): return M.score_idx(M.encode(dec(k)))
free=[i for i,s in enumerate(S) if s not in pin]
best=None
for run in range(int(sys.argv[1])):
    k=[pin.get(s) or random.choice('eainrstuol') for s in S]; s=sc(k); T=3.0
    for it in range(30000):
        k2=k[:]; k2[random.choice(free)]=random.choice(A)
        s2=sc(k2)
        if s2>s or random.random()<math.exp((s2-s)/T): k,s=k2,s2
        T=max(0.05,T*0.99985)
    if best is None or s>best[0]: best=(s,k[:])
    print(run,round(s/len(ct),3),' | '.join(''.join(k[ix[x]] for x in r) for r in rows),flush=True)
