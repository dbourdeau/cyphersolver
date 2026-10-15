import pickle, numpy as np, sys, math, random, collections, os
# moved here from targets/esp318/ on 14 Oct 2026 (one key per entry); the Spanish model (lm.py, lm_tabs.pkl,
# git-ignored) stays in targets/esp318/, shared with the no. 95 pipeline
HERE = os.path.dirname(os.path.abspath(__file__)); ESP318 = os.path.join(HERE, '..', 'esp318')
sys.path.insert(0, ESP318)
from lm import ALPHA, IDX
L=len(ALPHA)
tabs=pickle.load(open(os.path.join(ESP318, 'lm_tabs.pkl'),'rb')); lp5=tabs[5]; p1=np.exp(tabs[1])
toks=[t for l in open(os.path.join(HERE, 'ct93_eye.txt'),encoding='utf-8') if not l.startswith('#') for t in l.split()]
syms=sorted(set(toks)); S=len(syms); sid={s:i for i,s in enumerate(syms)}
seq=np.array([sid[t] for t in toks]); N=len(seq)
freq=np.bincount(seq,minlength=S)
print('tokens',N,'signs',S)
CAP=max(3,int(np.ceil(S/22*1.6)))
def score(key):
    d=key[seq]
    s=lp5[d[:-4],d[1:-3],d[2:-2],d[3:-1],d[4:]].sum()
    obs=np.bincount(d,minlength=L)/N; kl=(obs*np.log(np.maximum(obs,1e-9)/p1)).sum()
    return s-0.6*N*kl
def anneal(seed,iters):
    rng=random.Random(seed)
    # init: frequency-rank match to spanish letter ranks
    order=np.argsort(-freq); lets=np.argsort(-p1)
    key=np.zeros(S,int)
    for r,s in enumerate(order): key[s]=lets[min(r, L-1)] if r<L else rng.randrange(L)
    cur=score(key); best=cur; bk=key.copy()
    for it in range(iters):
        T=3.0*(0.03/3.0)**(it/iters)
        s=rng.randrange(S); old=key[s]
        if rng.random()<0.2:
            s2=rng.randrange(S); key[s],key[s2]=key[s2],key[s]; new=score(key)
            if new>=cur or rng.random()<math.exp((new-cur)/T): cur=new
            else: key[s],key[s2]=key[s2],key[s]
        else:
            key[s]=rng.randrange(L)
            if key[s]==old: continue
            new=score(key)
            if new>=cur or rng.random()<math.exp((new-cur)/T): cur=new
            else: key[s]=old
        if cur>best: best,bk=cur,key.copy()
    return best,bk
res=[]
for sd in range(int(sys.argv[1]) if len(sys.argv)>1 else 8):
    b,k=anneal(sd,int(sys.argv[2]) if len(sys.argv)>2 else 60000); res.append((b,k)); print('seed',sd,round(b,1),round(b/N,3),flush=True)
res.sort(key=lambda r:-r[0]); b,k=res[0]
print('best per token',round(b/N,3))
print('key:',{syms[s]:ALPHA[k[s]] for s in np.argsort(-freq)})
dec=''.join(ALPHA[k[t]] for t in seq)
# print by line
pos=0
for l in open(os.path.join(HERE, 'ct93_eye.txt'),encoding='utf-8'):
    if l.startswith('#'): continue
    n=len(l.split()); print(dec[pos:pos+n]); pos+=n
# agreement among top 3
for b2,k2 in res[1:3]:
    print('alt',round(b2/N,3),''.join(ALPHA[k2[t]] for t in seq[:80]))
