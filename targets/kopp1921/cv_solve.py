"""Anneal the Karakhan->Kopp message as a two-table syllabary: first pair -> one letter, second pair -> one letter or nothing."""
import os,sys,random,math,re,collections
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(HERE,'..','..'))
from lang import lm
A='абвгдежзийклмнопрстуфхцчшщыьэюя'
def corpus():
    t=open(os.path.join(HERE,'ru_corpus.txt'),encoding='utf-8').read().lower().replace('ё','е').replace('ъ','ь')
    return re.sub('[^'+A+']','',t)
T=corpus();print('corpus',len(T))
LM=lm.DenseLM.build(T,4,A);print('lm built')
idx=LM.index
G=[g for g in open(os.path.join(HERE,'karakhan_ct.txt')).read().split() if '?' not in g]
HI=sorted({g[:2] for g in G});LO=sorted({g[2:] for g in G})
print(len(G),len(HI),len(LO))
N=len(A)  # N = null
def dec(mh,ml):
    x=[]
    for g in G:
        x.append(mh[g[:2]])
        v=ml[g[2:]]
        if v<N: x.append(v)
    return np.array(x,dtype=int)
def score(mh,ml):
    x=dec(mh,ml);return LM.score_idx(x)/1,len(x)
def obj(mh,ml):
    s,n=score(mh,ml);return s/max(n,1)
fr=[idx[c] for c in T[:200000]]
def run(seed,iters):
    random.seed(seed)
    mh={h:random.randrange(N) for h in HI};ml={l:random.randrange(N+1) for l in LO}
    cur=obj(mh,ml);best=(cur,dict(mh),dict(ml))
    t0,t1=0.25,0.01
    for i in range(iters):
        T_=t0*(t1/t0)**(i/iters)
        if random.random()<.45:
            k=random.choice(HI);o=mh[k];mh[k]=random.randrange(N);c=obj(mh,ml)
            if c>=cur or random.random()<math.exp((c-cur)/T_): cur=c
            else: mh[k]=o
        else:
            k=random.choice(LO);o=ml[k];ml[k]=random.randrange(N+1);c=obj(mh,ml)
            if c>=cur or random.random()<math.exp((c-cur)/T_): cur=c
            else: ml[k]=o
        if cur>best[0]: best=(cur,dict(mh),dict(ml))
    return best
res=[]
for s in range(int(sys.argv[1]),int(sys.argv[2])):
    b=run(s,int(sys.argv[3]));x=dec(b[1],b[2]);res.append((b[0],''.join(A[i] for i in x)));print(s,round(b[0],3),res[-1][1][:150],flush=True)
# control: same scorer on shuffled-group ciphertext could be run with --shuffle
