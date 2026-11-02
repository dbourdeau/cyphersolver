"""two-table solver: python tworun.py <ctfile> <seed0> <seed1> <iters> [shuffle] [order]"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,random,math,re,collections
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(HERE,'..','..'))
from lang import lm
A='абвгдежзийклмнопрстуфхцчшщыьэюя'
T=re.sub('[^'+A+']','',open(os.path.join(HERE,'ru_corpus.txt'),encoding='utf-8').read().lower().replace('ё','е').replace('ъ','ь'))
order=int(sys.argv[6]) if len(sys.argv)>6 else 3
LM=lm.DenseLM.build(T,order,A)
G=[g for g in open(sys.argv[1]).read().split() if '?' not in g]
if len(sys.argv)>5 and sys.argv[5]=='shuffle':
    random.seed(99);random.shuffle(G)
HI=[k for k,_ in collections.Counter(g[:2] for g in G).most_common()]
LO=[k for k,_ in collections.Counter(g[2:] for g in G).most_common()]
N=len(A)
H={h:i for i,h in enumerate(HI)};L={l:i for i,l in enumerate(LO)}
gh=np.array([H[g[:2]] for g in G]);gl=np.array([L[g[2:]] for g in G])
def run(seed,iters):
    random.seed(seed)
    ph=[random.randrange(N) for _ in HI];pl=[random.randrange(N+1) for _ in LO]
    # start from a permutation, moves may reassign; a soft penalty keeps tables near one-to-one
    def ev():
        a=np.array(ph)[gh];b=np.array(pl)[gl]
        x=np.empty(2*len(G),dtype=int);x[0::2]=a;x[1::2]=b
        x=x[x<N]
        pen=(len(ph)-len(set(ph)))+max(0,(len(pl)-len(set(pl)))-3)
        return LM.score_idx(x)/len(G)-.25*pen,x
    cur,x=ev();best=(cur,x,list(ph),list(pl))
    t0,t1=.8,.02
    for i in range(iters):
        t=t0*(t1/t0)**(i/iters)
        p=ph if random.random()<.5 else pl
        a=random.randrange(len(p));o=p[a]
        if random.random()<.5:
            b=random.randrange(len(p));p[a],p[b]=p[b],p[a]
        else:
            b=None;p[a]=random.randrange(N+(0 if p is ph else 1))
        c,y=ev()
        if c>=cur or random.random()<math.exp((c-cur)/t): cur,x=c,y
        else:
            if b is None: p[a]=o
            else: p[a],p[b]=p[b],p[a]
        if cur>best[0]: best=(cur,x,list(ph),list(pl))
    return best
for s in range(int(sys.argv[2]),int(sys.argv[3])):
    b=run(s,int(sys.argv[4]));print(s,round(b[0],3),len(b[1]),''.join(A[i] for i in b[1])[:260],flush=True)
