import os; os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,sys,multiprocessing as mp,collections as C
import solve2 as S, calib, wordscore as WS, pickle
def job(seed):
    V,pr,units=calib.mk(seed)
    s,d,n,toks,w,a0=calib.truth_score(units,V,pr)
    off,buf=S.pack(V); lm=np.asarray(np.load(S.W+'lm5ns.npy',mmap_mode='r')); cap=S.caps(V)
    a=np.random.default_rng(seed).integers(0,len(V),d).astype(np.int32)
    best,ba=S.run_sa(a,np.arange(d,dtype=np.int32),toks,off,buf,lm,2.2,3.0,w,pr,0.15,800000,6.0,0.25,seed,cap,3.0)
    tt=''.join(V[a0[t]] for t in toks); jj=''.join(V[ba[t]] for t in toks)
    return seed,round(WS.score(tt),3),round(WS.score(jj),3),tt[:90],jj[:90]
if __name__=='__main__':
    with mp.Pool(6) as P:
        for r in P.imap(job,range(6)): print(r)
    R,V,vals=pickle.load(open(S.W+'r2R.pkl','rb'))
    print('real annealed',[round(WS.score(S.text(V,r[2])),3) for r in R[:4]])
