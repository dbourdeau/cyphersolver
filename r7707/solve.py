import sys, random, math
sys.path.insert(0,'.')
from lang import lm
ct=open('r7707/ct.txt').read().split()
syms=sorted(set(ct)); idx=[syms.index(s) for s in ct]
AL='abcdefghijklmnopqrstuvwxyz'
def run(name,restarts=30,iters=20000):
    m=lm.load(name,order=4,spaces=False)
    best=(-1e9,None)
    for r in range(restarts):
        key=[random.randrange(26) for _ in syms]
        def f(k):
            from collections import Counter
            c=Counter(k); pen=sum(max(0,v-2) for v in c.values())*50
            return m.score(''.join(AL[k[i]] for i in idx))-pen
        cur=f(key); T=2.0
        for it in range(iters):
            j=random.randrange(len(syms)); old=key[j]; key[j]=random.randrange(26)
            s=f(key)
            if s>cur or random.random()<math.exp((s-cur)/T): cur=s
            else: key[j]=old
            T=max(0.05,T*0.9997)
        if cur>best[0]: best=(cur,key[:])
    k=best[1]; print(name,round(best[0],1),''.join(AL[k[i]] for i in idx))
    print(' '.join(f'{s}={AL[k[n]]}' for n,s in enumerate(syms)))
for n in sys.argv[1:]: run(n)
