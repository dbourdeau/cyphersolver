"""Injective version of cv_solve: each first pair one letter, each second pair one letter or null; swaps, not free replacement."""
import os,sys,random,math,re,collections
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(HERE,'..','..'))
from lang import lm
A='абвгдежзийклмнопрстуфхцчшщыьэюя'
T=re.sub('[^'+A+']','',open(os.path.join(HERE,'ru_corpus.txt'),encoding='utf-8').read().lower().replace('ё','е').replace('ъ','ь'))
LM=lm.DenseLM.build(T,4,A)
G=[g for g in open(os.path.join(HERE,'karakhan_ct.txt')).read().split() if '?' not in g]
if len(sys.argv)>4 and sys.argv[4]=='shuffle':
    random.seed(99);random.shuffle(G)
HI=[k for k,_ in collections.Counter(g[:2] for g in G).most_common()]
LO=[k for k,_ in collections.Counter(g[2:] for g in G).most_common()]
N=len(A)
def run(seed,iters):
    random.seed(seed)
    ph=list(range(N));random.shuffle(ph)      # first pair: position -> letter, spare letters kept at the end
    pl=list(range(N+1+40));random.shuffle(pl) # second pair: >=N means null (many nulls allowed)
    H={h:i for i,h in enumerate(HI)};L={l:i for i,l in enumerate(LO)}
    gh=np.array([H[g[:2]] for g in G]);gl=np.array([L[g[2:]] for g in G])
    def ev():
        a=np.array(ph)[gh];b=np.array(pl)[gl]
        x=np.empty(2*len(G),dtype=int);x[0::2]=a;x[1::2]=b
        x=x[x<N]
        return LM.score_idx(x)/len(G),x   # per group: a null is not rewarded
    cur,x=ev();best=(cur,x)
    t0,t1=.9,.03
    for i in range(iters):
        t=t0*(t1/t0)**(i/iters)
        p=ph if random.random()<.5 else pl
        lim=len(HI) if p is ph else len(LO)
        a=random.randrange(lim);b=random.randrange(len(p))
        p[a],p[b]=p[b],p[a]
        c,y=ev()
        if c>=cur or random.random()<math.exp((c-cur)/t): cur,x=c,y
        else: p[a],p[b]=p[b],p[a]
        if cur>best[0]: best=(cur,x)
    return best
for s in range(int(sys.argv[1]),int(sys.argv[2])):
    b=run(s,int(sys.argv[3]));print(s,round(b[0],3),len(b[1]),''.join(A[i] for i in b[1])[:300],flush=True)
