# Homophonic annealer: token -> letter (many to one), scored by Italian 4-grams. Numba. usage in other scripts: from hsolve import *
import numpy as np, numba as nb, re, sys, random, collections
AL='abcdefghilmnopqrstuz'
IDX={c:i for i,c in enumerate(AL)}
def load4(path='work/corpus.txt'):
    t=open(path).read()
    a=np.array([IDX[c] for c in t],dtype=np.int32)
    n=len(AL)
    c4=np.ones((n,n,n,n),dtype=np.float64)*0.05
    np.add.at(c4,(a[:-3],a[1:-2],a[2:-1],a[3:]),1)
    lp=np.log(c4/c4.sum())   # joint P(abcd), so a monotone text scores badly
    return lp.astype(np.float32)
@nb.njit(cache=True)
def score(seq,mp,lp,prior,alpha):
    s=0.0
    cnt=np.zeros(lp.shape[0]); N=0
    for i in range(len(seq)):
        if seq[i]>=0:
            cnt[mp[seq[i]]]+=1; N+=1
        if i<3: continue
        a,b,c,d=seq[i-3],seq[i-2],seq[i-1],seq[i]
        if a<0 or b<0 or c<0 or d<0: continue
        s+=lp[mp[a],mp[b],mp[c],mp[d]]
    # penalty: N*KL(observed||corpus)
    kl=0.0
    for k in range(lp.shape[0]):
        if cnt[k]>0:
            q=cnt[k]/N
            kl+=q*np.log(q/prior[k])
    return s-alpha*N*kl
@nb.njit(cache=True)
def anneal(seq,ntok,lp,iters,T0,T1,seed,prior,alpha=3.0):
    np.random.seed(seed)
    n=lp.shape[0]
    mp=np.zeros(ntok,dtype=np.int32)
    # start from prior frequency
    cum=np.cumsum(prior)
    for t in range(ntok):
        mp[t]=np.searchsorted(cum,np.random.random()*cum[-1])
    cur=score(seq,mp,lp,prior,alpha); best=cur; bm=mp.copy()
    # positions of each token
    for it in range(iters):
        T=T0*(T1/T0)**(it/iters)
        t=np.random.randint(ntok); old=mp[t]
        if np.random.random()<0.5:
            new=np.searchsorted(cum,np.random.random()*cum[-1])
            t2=-1
        else:
            t2=np.random.randint(ntok); new=mp[t2]
        if new==old: continue
        mp[t]=new
        if t2>=0: mp[t2]=old
        s=score(seq,mp,lp,prior,alpha)
        d=s-cur
        if d>=0 or np.random.random()<np.exp(d/T):
            cur=s
            if cur>best: best=cur; bm=mp.copy()
        else:
            mp[t]=old
            if t2>=0: mp[t2]=new
    return best,bm
def freqprior(path='work/corpus.txt'):
    t=open(path).read();c=collections.Counter(t);return np.array([c[x]/len(t) for x in AL],dtype=np.float64)
def encode(runs):
    toks=sorted({x for r in runs for x in r}); ix={t:i for i,t in enumerate(toks)}
    seq=[]
    for r in runs:
        seq+= [ix[x] for x in r]+[-1]
    return np.array(seq,dtype=np.int32),toks
def plain(seq,mp): return ''.join('|' if s<0 else AL[mp[s]] for s in seq)
def load_runs(files,mode='drop'):
    NAMES=['Q u a n','b u r','b o r','b a r','m u r','u l i r','i m a','s e d','L u s']
    runs=[]
    for f in files:
        for ln in open(f,encoding='utf8'):
            if ln.startswith('#') or ' ' not in ln: continue
            t=ln.split(' ',1)[1]
            for p in re.split(r'\[[^\]]*\]',t):
                s=' '+' '.join(p.split())+' '
                s=re.sub(r' e r ',' ER ',s)
                for nm in NAMES:
                    s=re.sub(' '+' (?:_[89] )*'.join(nm.split())+' ',' | ',s)
                for piece in s.split('|'):
                    toks=piece.split()
                    if mode=='drop': toks=[x for x in toks if not x.startswith('_')]
                    elif mode=='merge':
                        o=[]
                        for x in toks:
                            if x.startswith('_') and o: o[-1]=o[-1]+x
                            elif not x.startswith('_'): o.append(x)
                        toks=o
                    if toks: runs.append(toks)
    return runs
