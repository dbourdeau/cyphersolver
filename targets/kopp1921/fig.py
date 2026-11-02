"""Figure small table: each whole group as one letter (homophones allowed) under the corrected model; shuffled control. Also neighbours of the recurring pair 9030 7010."""
import sys,collections
from joint import *
G=[g for f in ('kopp0876_ct.txt','kopp0877_ct.txt','lutowinoff417_ct.txt') for g in open(f).read().split() if '?' not in g]
n=collections.Counter(zip(G,G[1:]));print(len(G),len(set(G)),n.most_common(12))
a=collections.Counter(G[i-1] for i in range(1,len(G)-1) if G[i]=='9030' and G[i+1]=='7010');b=collections.Counter(G[i+2] for i in range(len(G)-2) if G[i]=='9030' and G[i+1]=='7010')
print('before',a.most_common(6),'after',b.most_common(6))
sy=[k for k,_ in collections.Counter(G).most_common()];ix={k:i for i,k in enumerate(sy)};x0=np.array([ix[g] for g in G])
fr=[IDX[c] for c,_ in collections.Counter(T).most_common() if c in IDX]
def run(x,seed,its):
    rnd=random.Random(seed);p=np.array([fr[int(len(fr)*rnd.random()**2)] for _ in sy]);cur=score(p[x])[0]/len(x);best=cur;bp=p.copy()
    for i in range(its):
        t=.05*(1-i/its)+1e-3;k=rnd.randrange(len(sy));o=p[k];p[k]=fr[int(len(fr)*rnd.random()**2)];c=score(p[x])[0]/len(x)
        if c>=cur or rnd.random()<math.exp((c-cur)/t):
            cur=c
            if cur>best: best,bp=cur,p.copy()
        else: p[k]=o
    return best,bp
sh=x0.copy();np.random.default_rng(4).shuffle(sh)
for s in range(3):
    b,p=run(x0,s,int(sys.argv[1]));c,_=run(sh,s+50,int(sys.argv[1]));print('real',round(b,3),'ctrl',round(c,3),''.join(A[i] for i in p[x0])[:150],flush=True)
