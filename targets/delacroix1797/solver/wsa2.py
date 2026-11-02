# Word-placement annealer: compound moves set a run of groups to the units of one dictionary word; numeric blocks can move together.
import os; os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,pickle,collections as C
from numba import njit
import solve2 as S, wsa
def wordtable(V,hold_words=None,top=6000):
    wc=pickle.load(open(S.W+'wc.pkl','rb')); vi={v:i for i,v in enumerate(V)}
    st=[0];fl=[];wt=[]
    for w,c in wc.most_common(top):
        u=[w] if w in vi else S.syll(w)
        ids=[]
        for x in u:
            if x in vi: ids.append(vi[x])
            else: ids+=[vi[ch] for ch in x if ch in vi]
        if not ids or len(ids)>8: continue
        fl+=ids; st.append(len(fl)); wt.append(c**0.6)
    wt=np.array(wt,dtype=np.float64); return np.array(st,dtype=np.int32),np.array(fl,dtype=np.int32),np.cumsum(wt/wt.sum())
@njit(cache=True)
def anneal2(a,fixed,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT,wst,wfl,wcum,iters,T0,T1,seed):
    np.random.seed(seed);nv=len(a);m=len(off)-1;N=len(toks)
    cur=wsa.objective(a,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT);best=cur;ba=a.copy()
    old=a.copy();req=-np.ones(nv,dtype=np.int32)
    for it in range(iters):
        T=T0*(T1/T0)**(it/iters)
        old[:]=a;r=np.random.random();ok=True;ch=False
        if r<0.6:
            k=np.searchsorted(wcum,np.random.random());s=wst[k];L=wst[k+1]-s
            p=np.random.randint(N-L+1);req[:]=-1
            for j in range(L):
                g=toks[p+j];u=wfl[s+j]
                if fixed[g]:
                    if a[g]!=u: ok=False;break
                elif req[g]>=0 and req[g]!=u: ok=False;break
                req[g]=u
            if not ok: continue
            for g in range(nv):
                if req[g]>=0 and not fixed[g] and a[g]!=req[g]:
                    a[g]=req[g];ch=True
                    # spread to numeric neighbours in the same block sometimes
                    if np.random.random()<0.5:
                        h=g
                        while h>0 and w[h-1]>=1.0 and not fixed[h-1] and req[h-1]<0: h-=1;a[h]=req[g]
                        h=g
                        while h<nv-1 and w[h]>=1.0 and not fixed[h+1] and req[h+1]<0: h+=1;a[h]=req[g]
        else:
            g=np.random.randint(nv)
            if fixed[g]: continue
            q=np.random.random()
            if q<0.25 and g>0 and w[g-1]>0: nn=a[g-1]
            elif q<0.5 and g<nv-1 and w[g]>0: nn=a[g+1]
            else: nn=np.random.randint(m)
            if nn!=a[g]: a[g]=nn;ch=True
        if not ch: continue
        x=wsa.objective(a,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT)
        if x>=cur or np.random.random()<np.exp((x-cur)/T):
            cur=x
            if x>best: best=x;ba[:]=a
        else: a[:]=old
    return best,ba
