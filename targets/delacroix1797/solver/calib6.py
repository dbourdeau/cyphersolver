import os,sys,time; os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,multiprocessing as mp
import solve2 as S, calib, wsa, wsa2
def job(x):
    seed,npin=x
    V,pr,units=calib.mk(seed)
    s,d,n,toks,w,a0=calib.truth_score(units,V,pr)
    off,buf=S.pack(V);cap=S.caps(V);cnt=np.bincount(toks,minlength=d).astype(np.float64);buf=buf.astype(np.int32)
    hk,hv,bk,bv,up,uc,_=wsa.tables();wst,wfl,wcum=wsa2.wordtable(V)
    args=(toks,off,buf,cnt,cap,3.0,w,3.0,pr,0.15,hk,hv,bk,bv,up,uc,-14.0,1500.0)
    tr=wsa.objective(a0,*args)
    a=np.random.default_rng(seed).integers(0,len(V),d).astype(np.int32)
    pins=np.argsort(-cnt)[:npin];a[pins]=a0[pins];fx=np.zeros(d,dtype=np.bool_);fx[pins]=True
    best,ba=wsa2.anneal2(a,fx,*args,wst,wfl,wcum,int(sys.argv[1]),8.0,0.5,seed)
    acc=np.mean([V[ba[t]]==V[a0[t]] for t in toks])
    return seed,npin,round(float(cnt[pins].sum()/len(toks)),2),round(float(tr)),round(float(best)),round(float(acc),3),''.join(V[ba[t]] for t in toks)[:90]
if __name__=='__main__':
    with mp.Pool(9) as P:
        for r in P.imap(job,[(s,k) for k in (20,40,80) for s in (0,1,2)]): print(r,flush=True)
