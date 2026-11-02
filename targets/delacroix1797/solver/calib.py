# Calibration: does the true key of a synthetic letter outscore annealed junk under the same objective?
import os; os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,pickle,sys,random,collections as C,re,multiprocessing as mp
import solve2 as S
W=S.W
T=open(W+'turner_fr.txt',encoding='utf8').read()
def mk(seed):
    r=random.Random(seed)
    i=r.randrange(1000,len(T)-5000); t=T[i:i+3000].split()[1:]
    V,pr=S.vocab(); vs=set(V)
    units=[]
    for w in t:
        if w in vs: units.append(w)
        else:
            for s in S.syll(w):
                if s in vs: units.append(s)
                else: units+=[x for x in s if x in vs]
        if len(units)>=653: break
    units=units[:653]
    return V,pr,units
def truth_score(units,V,pr):
    # homophones: each unit gets 1-5 values by frequency, in adjacent blocks; distinct about 297
    vi={v:i for i,v in enumerate(V)}
    c=C.Counter(units)
    ids=[];vals=[];k=0;mp_={}
    a=[];toks=[]
    rng=random.Random(1)
    for u,n in c.items():
        m=max(1,min(5,int(n*0.45)))
        mp_[u]=list(range(k,k+m)); a+= [vi[u]]*m; k+=m
    toks=[rng.choice(mp_[u]) for u in units]
    used=sorted(set(toks)); re_={v:i for i,v in enumerate(used)}
    toks=np.array([re_[t] for t in toks],dtype=np.int32); a=np.array([a[v] for v in used],dtype=np.int32)
    w=np.array([1.0 if used[i+1]-used[i]==1 else (0.4 if used[i+1]-used[i]==2 else 0.0) for i in range(len(used)-1)]+[0.0])
    off,buf=S.pack(V); lm=np.asarray(np.load(W+'lm5ns.npy',mmap_mode='r')); cap=S.caps(V)
    cnt=np.bincount(toks,minlength=len(a))
    s=S.sc(a,toks,off,buf,lm,2.2)+S.tie(a,len(a),3.0,w)+0.15*pr[a].sum()-S.over(a,cnt,cap,3.0)
    n=sum(len(V[a[t]]) for t in toks)
    return s,len(a),n,toks,w,a
def job(seed):
    V,pr,units=mk(seed)
    s,d,n,toks,w,a0=truth_score(units,V,pr)
    off,buf=S.pack(V); lm=np.asarray(np.load(W+'lm5ns.npy',mmap_mode='r')); cap=S.caps(V)
    rng=np.random.default_rng(seed); a=rng.integers(0,len(V),d).astype(np.int32)
    free=np.arange(d,dtype=np.int32)
    best,ba=S.run_sa(a,free,toks,off,buf,lm,2.2,3.0,w,pr,0.15,int(sys.argv[1]),6.0,0.25,seed,cap,3.0)
    acc=np.mean([V[ba[t]]==V[a0[t]] for t in toks])
    return seed,round(float(s)),d,n,round(float(best)),round(float(acc),3)
if __name__=='__main__':
    with mp.Pool(8) as P:
        for r in P.imap(job,range(8)): print('seed %d truth=%d distinct=%d chars=%d annealed=%d token_acc=%.3f'%r)
