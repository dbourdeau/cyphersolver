# Partly ordered table test: alphabetical only inside numeric blocks of size B; real ciphertext against scrambled numbers.
import os,sys,json,random; os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,multiprocessing as mp
from numba import njit
import solve2 as S, wsa, mono
@njit(cache=True)
def ab(a,blk,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT,iters,T0,T1,seed):
    np.random.seed(seed);nv=len(a);m=len(off)-1
    cur=wsa.objective(a,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT);best=cur;ba=a.copy()
    cum=np.cumsum((cnt+1.0)/(cnt+1.0).sum())
    for it in range(iters):
        T=T0*(T1/T0)**(it/iters)
        i=min(int(np.searchsorted(cum,np.random.random())),nv-1)
        lo=a[i-1] if i>0 and blk[i-1]==blk[i] else 0
        hi=a[i+1] if i<nv-1 and blk[i+1]==blk[i] else m-1
        if hi<=lo: continue
        old=a[i];r=np.random.random()
        if r<0.3: nn=max(lo,min(hi,old+np.random.randint(-6,7)))
        else: nn=np.random.randint(lo,hi+1)
        if nn==old: continue
        a[i]=nn
        x=wsa.objective(a,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT)
        if x>=cur or np.random.random()<np.exp((x-cur)/T):
            cur=x
            if x>best: best=x;ba[:]=a
        else: a[i]=old
    return best,ba
def job(x):
    mode,B,seed,iters=x
    V,pr=mono.vocab()
    if mode=='real': toks,vals=S.toks,S.vals
    else:
        vs=list(range(2,1199));random.Random(1000+seed).shuffle(vs);m=dict(zip(S.vals,vs[:len(S.vals)]))
        nv=sorted(m.values());re_={g:k for k,g in enumerate(nv)};toks=np.array([re_[m[S.vals[t]]] for t in S.toks],dtype=np.int32);vals=nv
    args=mono.setup(vals,toks,V,pr);blk=np.array([v//B for v in vals],dtype=np.int32)
    rng=np.random.default_rng(seed);a=rng.integers(0,len(V),len(vals)).astype(np.int32)
    for b in set(blk.tolist()):
        ii=np.where(blk==b)[0];a[ii]=np.sort(a[ii])
    best,ba=ab(a,blk,*args,iters,12.0,0.5,seed)
    return mode,B,seed,round(float(best)),' '.join(V[ba[t]] for t in toks)
if __name__=='__main__':
    iters=int(sys.argv[1]);res=[]
    jobs=[(m,B,s,iters) for B in map(int,sys.argv[2].split(',')) for m in ('real','null') for s in range(3)]
    with mp.Pool(10) as P:
        for r in P.imap_unordered(job,jobs):
            print(r[0],r[1],r[2],r[3],'|',r[4][:170],flush=True);res.append(r)
    for B in map(int,sys.argv[2].split(',')):
        for m in ('real','null'):
            print(B,m,sorted(r[3] for r in res if r[0]==m and r[1]==B))
    json.dump(res,open(S.W+'blocks.json','w'))
