import os,sys,random,math
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang import lm
exec(open(os.path.join(os.path.dirname(__file__),'parse.py')).read().split('for k,v in segs')[0])
runs=[v for k,v in segs if k=='N']
model=sys.argv[1]; seeds=int(sys.argv[2]); order=int(sys.argv[3]) if len(sys.argv)>3 else 4
m=lm.load(model,order=order,spaces=False)
syms=sorted({x for r in runs for x in r if x not in('60','64')},key=int)
letters=list(m.alpha)
def dec(key): return [''.join(key.get(x,'#') for x in r) for r in runs]
def score(key): return sum(m.score_idx(m.encode(s.replace('#',''))) for s in dec(key))
res=[]
for sd in range(seeds):
    random.seed(sd); pool=letters[:]; random.shuffle(pool)
    # slots: syms + spare letters
    perm=pool+[]  # perm[i] letter for syms[i]; tail unused
    key=lambda: {s:perm[i] for i,s in enumerate(syms)}
    cur=score(key()); T=8
    for it in range(30000):
        i=random.randrange(len(syms)); j=random.randrange(len(perm))
        perm[i],perm[j]=perm[j],perm[i]; n=score(key())
        if n>cur or random.random()<math.exp((n-cur)/T): cur=n
        else: perm[i],perm[j]=perm[j],perm[i]
        T=max(0.1,T*0.99975)
    res.append((cur,key())); print(sd,round(cur,1),' | '.join(dec(key())),flush=True)
res.sort(key=lambda r:-r[0]); b=res[0]
print('BEST',b[0]); print(' '.join(f'{s}={b[1][s]}' for s in syms))
