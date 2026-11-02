# One-part test: numeric order = alphabetical order of entries, homophones in consecutive blocks; word-bigram objective.
import os,sys,time,pickle,json; os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,random,collections as C,multiprocessing as mp
from numba import njit
import solve2 as S, wsa
def vocab(nw=3000,ns=350):
    wc=pickle.load(open(S.W+'wc.pkl','rb')); sc=C.Counter()
    for w,c in wc.items():
        for x in S.syll(w): sc[x]+=c
    E=set(w for w,_ in wc.most_common(nw) if len(w)>1 or w in 'adlnsmjcy')|set(s for s,_ in sc.most_common(ns) if len(s)<=5)|set('abcdefghijlmnopqrstuvxz')
    V=sorted(E); pr=np.array([np.log(1+max(sc.get(v,0),wc.get(v,0))) for v in V]); return V,pr-pr.mean()
def caps(V):
    wc=pickle.load(open(S.W+'wc.pkl','rb')); tot=sum(wc.values())
    return np.array([653*2.5*wc.get(v,0)/tot+3 for v in V])
@njit(cache=True)
def am(a,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT,iters,T0,T1,seed):
    np.random.seed(seed);nv=len(a);m=len(off)-1
    cur=wsa.objective(a,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT);best=cur;ba=a.copy()
    p=(cnt+1.0)/(cnt+1.0).sum();cum=np.cumsum(p)
    for it in range(iters):
        T=T0*(T1/T0)**(it/iters)
        i=int(np.searchsorted(cum,np.random.random()));i=min(i,nv-1)
        lo=a[i-1] if i>0 else 0;hi=a[i+1] if i<nv-1 else m-1
        if hi<=lo: continue
        old=a[i];r=np.random.random()
        if r<0.2: nn=lo
        elif r<0.4: nn=hi
        elif r<0.7: nn=max(lo,min(hi,old+np.random.randint(-6,7)))
        else: nn=np.random.randint(lo,hi+1)
        if nn==old: continue
        a[i]=nn
        x=wsa.objective(a,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT)
        if x>=cur or np.random.random()<np.exp((x-cur)/T):
            cur=x
            if x>best: best=x;ba[:]=a
        else: a[i]=old
    return best,ba
def holdpos(seed):
    T=open(S.W+'turner_fr.txt',encoding='utf8').read();r=random.Random(seed);return r.randrange(1000,len(T)-5000)
def synth(seed,V):
    T=open(S.W+'turner_fr.txt',encoding='utf8').read();i=holdpos(seed)
    vi={v:k for k,v in enumerate(V)};units=[]
    for w in T[i:i+3500].split()[1:]:
        if w in vi: units.append(w)
        else:
            for s in S.syll(w):
                if s in vi: units.append(s)
                else: units+=[c for c in s if c in vi]
        if len(units)>=653: break
    units=units[:653];c=C.Counter(units)
    # table of 1198 numbers over the sorted entries actually used + silent entries: scale positions; frequent entries own blocks
    used=sorted(c); pos={};cur=2
    for u in V:
        m=max(1,min(5,int(c.get(u,0)*0.45)))
        pos[u]=(cur,m); cur+=m
    sc=1198/cur
    toks=[];rng=random.Random(seed+1)
    for u in units:
        p,m=pos[u];toks.append(int((p+rng.randrange(m))*1.0))
    vals=sorted(set(toks));ix={v:k for k,v in enumerate(vals)}
    a0=np.array([0]*len(vals),dtype=np.int32)
    for u in used:
        p,m=pos[u]
        for q in range(p,p+m):
            if q in ix: a0[ix[q]]=vi[u]
    return np.array([ix[t] for t in toks],dtype=np.int32),vals,a0
def setup(vals,toks,V,pr,hold=None):
    d=len(vals);off,buf=S.pack(V);buf=buf.astype(np.int32);cap=caps(V);cnt=np.bincount(toks,minlength=d).astype(np.float64)
    w=np.array([1.0 if vals[i+1]-vals[i]==1 else (0.4 if vals[i+1]-vals[i]==2 else 0.0) for i in range(d-1)]+[0.0])
    hk,hv,bk,bv,up,uc,_=wsa.tables(hold)
    return (toks,off,buf,cnt,cap,3.0,w,3.0,pr,0.15,hk,hv,bk,bv,up,uc,-14.0,1500.0)
def init(vals,m,seed):
    rng=np.random.default_rng(seed);return np.sort(np.clip(((np.array(vals)/max(vals))*m+rng.normal(0,m*0.01,len(vals))).astype(np.int32),0,m-1))
def job(x):
    mode,seed,iters=x
    V,pr=vocab()
    if mode=='synth':
        toks,vals,a0=synth(seed,V);h=holdpos(seed);args=setup(vals,toks,V,pr,(h-200,h+3700));tr=float(wsa.objective(a0,*args))
    elif mode=='null':
        vs=list(range(2,1199));random.Random(1000+seed).shuffle(vs);m=dict(zip(S.vals,vs[:len(S.vals)]))
        nv=sorted(m.values());re_={g:k for k,g in enumerate(nv)};toks=np.array([re_[m[S.vals[t]]] for t in S.toks],dtype=np.int32);vals=nv;args=setup(vals,toks,V,pr);tr=0.0;a0=None
    else:
        toks,vals=S.toks,S.vals;args=setup(vals,toks,V,pr);tr=0.0;a0=None
    a=init(vals,len(V),seed)
    best,ba=am(a,*args,iters,12.0,0.5,seed)
    txt=' '.join(V[ba[t]] for t in toks)
    acc=float(np.mean([V[ba[t]]==V[a0[t]] for t in toks])) if a0 is not None else -1
    return mode,seed,round(tr),round(float(best)),round(acc,3),txt
if __name__=='__main__':
    iters=int(sys.argv[1]);modes=sys.argv[2].split(',');res=[]
    with mp.Pool(10) as P:
        for r in P.imap_unordered(job,[(m,s,iters) for m in modes for s in range(5)]):
            print(r[0],r[1],'truth',r[2],'found',r[3],'acc',r[4],'|',r[5][:300],flush=True);res.append(r)
    json.dump(res,open(S.W+'mono_'+'_'.join(modes)+'.json','w'))
