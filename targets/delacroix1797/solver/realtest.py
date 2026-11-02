# Real ciphertext under the word-bigram objective, for competing cribs of the 7x repeat, plus a nonsense control.
import os,sys,json; os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,multiprocessing as mp,collections as C
import solve2 as S, wsa
H={'republique':{705:'re',806:'pu',711:'bli',400:'bli',405:'que',265:'la',266:'la',267:'la',268:'la',269:'la'},
   'gouvernement':{705:'gou',806:'ver',711:'ne',400:'ne',405:'ment',265:'le',266:'le',267:'le',268:'le',269:'le'},
   'control':{705:'pa',806:'ri',711:'so',400:'so',405:'te',265:'mi',266:'mi',267:'mi',268:'mi',269:'mi'}}
def job(x):
    name,seed=x
    V,pr=S.vocab(); vi={v:i for i,v in enumerate(V)}
    off,buf=S.pack(V); buf=buf.astype(np.int32); cap=S.caps(V); d=len(S.vals); toks=S.toks
    cnt=np.bincount(toks,minlength=d).astype(np.float64)
    w=np.array([1.0 if S.vals[i+1]-S.vals[i]==1 else (0.4 if S.vals[i+1]-S.vals[i]==2 else 0.0) for i in range(d-1)]+[0.0])
    hk,hv,bk,bv,up,uc,_=wsa.tables()
    a=np.random.default_rng(seed).integers(0,len(V),d).astype(np.int32); fixed=set()
    for g,s in H[name].items():
        if s not in vi: return name,seed,None,'missing '+s
        a[S.ix[g]]=vi[s]; fixed.add(S.ix[g])
    free=np.array([i for i in range(d) if i not in fixed],dtype=np.int32)
    best,ba=wsa.anneal(a,free,toks,off,buf,cnt,cap,3.0,w,3.0,pr,0.15,hk,hv,bk,bv,up,uc,-14.0,1500.0,int(sys.argv[1]),12.0,0.6,seed)
    return name,seed,round(float(best)),''.join(V[ba[t]] for t in toks)
if __name__=='__main__':
    jobs=[(n,s) for n in (sys.argv[2:] or list(H)) for s in range(4)]
    res=C.defaultdict(list)
    with mp.Pool(12) as P:
        for r in P.imap_unordered(job,jobs):
            res[r[0]].append(r); print(r[0],r[1],r[2],(r[3] or '')[:200],flush=True)
    print({k:sorted(x[2] or -9e9 for x in v) for k,v in res.items()})
    json.dump(res,open(S.W+'realtest_'+'_'.join(sys.argv[2:] or ['all'])+'.json','w'))
