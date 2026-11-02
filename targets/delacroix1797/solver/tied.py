# Two-part code with hard-merged consecutive numbers, word-placement search; realistic held-out synthetic letters and the real text.
import os,sys,json,random; os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,collections as C,multiprocessing as mp
import solve2 as S, wsa, wsa2, calib, mono
def chains(L):
    vals=sorted(set(L));lab={};c=-1;prev=-9
    for v in vals:
        if v-prev>1: c+=1
        lab[v]=c;prev=v
    return np.array([lab[x] for x in L],dtype=np.int32),c+1
def job(x):
    mode,seed,iters=x
    V,pr=S.vocab();hold=None;a0=None;tr=0.0
    if mode=='synth':
        h=mono.holdpos(seed);V0,pr0,units=calib.mk(seed);hold=None
        rng=random.Random(seed);c=C.Counter(units);free=list(range(2,1199));rng.shuffle(free);occ=set();pos={}
        for u,n in c.most_common():
            m=max(1,min(5,int(n*0.45)))
            for st in free:
                if all(q not in occ and q<1199 for q in range(st,st+m)):
                    pos[u]=list(range(st,st+m));occ|=set(pos[u]);break
        L=[rng.choice(pos[u]) for u in units];toks,d=chains(L)
        vi={v:i for i,v in enumerate(V)};maj=[C.Counter() for _ in range(d)]
        for t,u in zip(toks,units): maj[t][u]+=1
        a0=np.array([vi[m.most_common(1)[0][0]] for m in maj],dtype=np.int32)
        pure=sum(m.most_common(1)[0][1] for m in maj)/len(units)
    else:
        toks,d=chains(S.L);pure=-1
    off,buf=S.pack(V);buf=buf.astype(np.int32);cap=S.caps(V);cnt=np.bincount(toks,minlength=d).astype(np.float64)
    w=np.zeros(d);hk,hv,bk,bv,up,uc,_=wsa.tables(hold);wst,wfl,wcum=wsa2.wordtable(V)
    args=(toks,off,buf,cnt,cap,3.0,w,0.0,pr,0.15,hk,hv,bk,bv,up,uc,-14.0,1500.0)
    if a0 is not None: tr=float(wsa.objective(a0,*args))
    a=np.random.default_rng(seed).integers(0,len(V),d).astype(np.int32)
    best,ba=wsa2.anneal2(a,np.zeros(d,dtype=np.bool_),*args,wst,wfl,wcum,iters,15.0,0.6,seed)
    acc=float(np.mean([V[ba[t]]==V[a0[t]] for t in toks])) if a0 is not None else -1
    return mode,seed,d,round(pure,3),round(tr),round(float(best)),round(acc,3),' '.join(V[ba[t]] for t in toks)
if __name__=='__main__':
    iters=int(sys.argv[1]);res=[]
    with mp.Pool(10) as P:
        for r in P.imap_unordered(job,[('synth',s,iters) for s in range(5)]+[('real',s,iters) for s in range(5)]):
            print(*r[:7],'|',r[7][:190],flush=True);res.append(r)
    json.dump(res,open(S.W+'tied.json','w'))
