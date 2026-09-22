import os,sys,random,math,re
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang import lm
exec(open(os.path.join(os.path.dirname(__file__),'parse.py')).read().split('for k,v in segs')[0])
runs=[v for k,v in segs if k=='N']
model=sys.argv[1]; seeds=int(sys.argv[2]) if len(sys.argv)>2 else 10
m=lm.load(model,order=4,spaces=False)
syms=sorted({x for r in runs for x in r if x not in('60','64')},key=int)
alpha=m.alpha
def dec(key): return [''.join(key[x] if x in key else '#' for x in r) for r in runs]
def score(key):
    return sum(m.score_idx(m.encode(s.replace('#',''))) for s in dec(key))
best=None
for sd in range(seeds):
    random.seed(sd)
    key={s:random.choice(alpha) for s in syms}; cur=score(key); T=5
    for it in range(40000):
        s=random.choice(syms); old=key[s]; key[s]=random.choice(alpha)
        n=score(key)
        if n>cur or random.random()<math.exp((n-cur)/T): cur=n
        else: key[s]=old
        T=max(0.05,T*0.9998)
    if best is None or cur>best[0]: best=(cur,dict(key))
    print(sd,round(cur,1),' | '.join(dec(key)),flush=True)
print('BEST',best[0]); print(' '.join(f'{s}={best[1][s]}' for s in syms)); print(' | '.join(dec(best[1])))
