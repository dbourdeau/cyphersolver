import os,sys,time; os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,multiprocessing as mp,collections as C
import solve2 as S, calib, wsa
def job(seed):
    V,pr,units=calib.mk(seed)
    s,d,n,toks,w,a0=calib.truth_score(units,V,pr)
    off,buf=S.pack(V); cap=S.caps(V); cnt=np.bincount(toks,minlength=d).astype(np.float64)
    buf=buf.astype(np.int32)
    hk,hv,bk,bv,up,uc,_=wsa.tables()
    args=(toks,off,buf,cnt,cap,3.0,w,3.0,pr,0.15,hk,hv,bk,bv,up,uc,-14.0,1500.0)
    tr=wsa.objective(a0,*args)
    a=np.random.default_rng(seed).integers(0,len(V),d).astype(np.int32)
    t=time.time(); best,ba=wsa.anneal(a,np.arange(d,dtype=np.int32),*args,int(sys.argv[1]),15.0,0.6,seed); t=time.time()-t
    acc=np.mean([V[ba[x]]==V[a0[x]] for x in toks])
    return seed,round(tr),round(best),round(float(acc),3),round(t),''.join(V[ba[x]] for x in toks)[:120]
if __name__=='__main__':
    with mp.Pool(6) as P:
        for r in P.imap(job,range(6)): print(r)
