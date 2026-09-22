import os,sys,random,math
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang import lm
exec(open(os.path.join(os.path.dirname(__file__),'parse.py')).read().split('for k,v in segs')[0])
runs=[v for k,v in segs if k=='N']
model=sys.argv[1]; seeds=int(sys.argv[2]); order=int(sys.argv[3]); cap=int(sys.argv[4])
m=lm.load(model,order=order,spaces=False)
syms=sorted({x for r in runs for x in r if x not in('60','64')},key=int)
letters=list(m.alpha)*cap
def dec(key): return [''.join(key.get(x,'#') for x in r) for r in runs]
def score(key): return sum(m.score_idx(m.encode(s.replace('#',''))) for s in dec(key))
res=[]
for sd in range(seeds):
    random.seed(sd); perm=letters[:]; random.shuffle(perm)
    key=lambda: {s:perm[i] for i,s in enumerate(syms)}
    cur=score(key()); T=10
    for it in range(60000):
        i=random.randrange(len(syms)); j=random.randrange(len(perm))
        perm[i],perm[j]=perm[j],perm[i]; n=score(key())
        if n>cur or random.random()<math.exp((n-cur)/T): cur=n
        else: perm[i],perm[j]=perm[j],perm[i]
        T=max(0.2,T*0.99988)
    res.append((cur,key())); print(sd,round(cur,1),' | '.join(dec(key())),flush=True)
res.sort(key=lambda r:-r[0]); b=res[0]
print('BEST',b[0]); print(' '.join(f'{s}={b[1][s]}' for s in syms))
