import os,sys,time; os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,multiprocessing as mp,collections as C
import solve2 as S, calib, wsa
def job(a_):
    seed,npin=a_
    V,pr,units=calib.mk(seed)
    s,d,n,toks,w,a0=calib.truth_score(units,V,pr)
    off,buf=S.pack(V); cap=S.caps(V); cnt=np.bincount(toks,minlength=d).astype(np.float64)
    buf=buf.astype(np.int32)
    hk,hv,bk,bv,up,uc,_=wsa.tables()
    args=(toks,off,buf,cnt,cap,3.0,w,3.0,pr,0.15,hk,hv,bk,bv,up,uc,-14.0,1500.0)
    tr=wsa.objective(a0,*args)
    a=np.random.default_rng(seed).integers(0,len(V),d).astype(np.int32)
    order=np.argsort(-cnt); pins=order[:npin]; a[pins]=a0[pins]
    free=np.array([i for i in range(d) if i not in set(pins.tolist())],dtype=np.int32)
    best,ba=wsa.anneal(a,free,*args,int(sys.argv[1]),8.0,0.6,seed)
    acc=np.mean([V[ba[x]]==V[a0[x]] for x in toks])
    return seed,npin,round(float(cnt[pins].sum()/len(toks)),2),round(tr),round(best),round(float(acc),3),''.join(V[ba[x]] for x in toks)[:100]
if __name__=='__main__':
    with mp.Pool(8) as P:
        for r in P.imap(job,[(s,k) for k in (40,80) for s in (0,1,2,3)]): print(r)
