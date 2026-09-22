import sys, random, math
sys.path.insert(0,'.')
from lang import lm
ct=open('r7707/ct.txt').read().split()
syms=sorted(set(ct),key=lambda s:-ct.count(s)); idx=[syms.index(s) for s in ct]
AL='abcdefghijklmnopqrstuvwxyz'
def run(name,restarts=40,iters=30000):
    m=lm.load(name,order=4,spaces=False)
    pool=list(AL)+['#']*(len(syms)-26+2)  # '#' = unused symbol slot
    best=(-1e9,None)
    for r in range(restarts):
        key=pool[:]; random.shuffle(key)
        f=lambda k: m.score(''.join(k[i] for i in idx if k[i]!='#'))-40*sum(k[i]=='#' for i in idx)
        cur=f(key); T=3.0
        for it in range(iters):
            a=random.randrange(len(syms)); b=random.randrange(len(pool))
            key[a],key[b]=key[b],key[a]; s=f(key)
            if s>cur or random.random()<math.exp((s-cur)/T): cur=s
            else: key[a],key[b]=key[b],key[a]
            T=max(0.05,T*0.9998)
        if cur>best[0]: best=(cur,key[:])
    k=best[1]; print(name,round(best[0]/len(ct),2),''.join(k[i] for i in idx),flush=True)
    print('  '+' '.join(f'{s}={k[n]}' for n,s in enumerate(syms)),flush=True)
for n in sys.argv[1:]: run(n)
