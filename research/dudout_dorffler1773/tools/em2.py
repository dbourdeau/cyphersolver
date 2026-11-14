# Soft EM (forward-backward) monotone segmental alignment: cipher codes -> gloss substrings.
import sys, math, json, collections
import numpy as np
sys.path.insert(0,__file__.rsplit('/',1)[0])
from parse import load
LMAX=7
NEG=-1e30
LENP={1:0.25,2:0.3,3:0.25,4:0.09,5:0.06,6:0.03,7:0.02}
def emis_matrix(C,S,E,base_cache,lu):
    n=len(C); m=len(S)
    EM=np.full((n,LMAX+1,m+1),NEG)   # EM[i,L,j]: code i emits S[j-L:j]
    for i,c in enumerate(C):
        d=E.get(c) if not c.startswith('?') else None
        for L in range(1,LMAX+1):
            for j in range(L,m+1):
                t=S[j-L:j]
                b=base_cache.get(t)
                if b is None:
                    b=math.log(LENP[L])+sum(lu.get(ch,-12) for ch in t); base_cache[t]=b
                if d is None: EM[i,L,j]=b
                else:
                    v=d.get(t)
                    EM[i,L,j]= v if v is not None else d['__floor']+b
    return EM
def fb(C,S,EM,skipc,skips):
    n=len(C); m=len(S)
    js=np.arange(m+1)*skips
    F=np.full((n+1,m+1),NEG)
    F[0]=js  # skip gloss chars at start
    for i in range(1,n+1):
        G=F[i-1]+skipc
        for L in range(1,LMAX+1):
            tmp=np.full(m+1,NEG); tmp[L:]=F[i-1][:m+1-L]+EM[i-1,L,L:]
            G=np.logaddexp(G,tmp)
        F[i]=np.logaddexp.accumulate(G-js)+js
    Z=F[n,m]
    B=np.full((n+1,m+1),NEG)
    rj=(m-np.arange(m+1))*skips
    B[n]=rj
    for i in range(n-1,-1,-1):
        G=B[i+1]+skipc
        for L in range(1,LMAX+1):
            tmp=np.full(m+1,NEG); tmp[:m+1-L]=B[i+1][L:]+EM[i,L,L:]
            G=np.logaddexp(G,tmp)
        # B[i][j]=logsum_k>=j G[k]+(k-j)*skips
        B[i]=(np.logaddexp.accumulate((G+np.arange(m+1)*skips)[::-1])[::-1])-np.arange(m+1)*skips
    return F,B,Z
def run(blocks,iters=30,skipc=math.log(0.03),skips=math.log(0.03),E=None,verbose=True,fixed=False):
    allg=''.join(b['G'] for b in blocks)
    uni=collections.Counter(allg); tot=sum(uni.values())
    lu={ch:math.log(v/tot) for ch,v in uni.items()}
    E=E or {}; base_cache={}
    for it in range(iters):
        counts=collections.defaultdict(lambda: collections.defaultdict(float)); LL=0
        for b in blocks:
            C=b['C']; S=b['G']
            if not S or not C: continue
            EM=emis_matrix(C,S,E,base_cache,lu)
            F,B,Z=fb(C,S,EM,skipc,skips); LL+=Z
            n=len(C); m=len(S)
            for i in range(n):
                c=C[i]
                if c.startswith('?'): continue
                for L in range(1,LMAX+1):
                    post=F[i][:m+1-L]+EM[i,L,L:]+B[i+1][L:]-Z
                    idx=np.nonzero(post>-6)[0]
                    for j in idx: counts[c][S[j:j+L]]+=math.exp(post[j])
        if fixed: return E,counts,LL
        newE={}
        for c,d in counts.items():
            tt=sum(d.values())
            dd={t:math.log(v/(tt+0.3)) for t,v in d.items() if v>0.02}
            dd['__floor']=math.log(0.3/(tt+0.3))
            newE[c]=dd
        E=newE
        if verbose: print('iter',it,'LL',round(LL,1),flush=True)
    return E,counts,LL
if __name__=='__main__':
    blocks=load(sys.argv[1])
    E,counts,LL=run(blocks,iters=int(sys.argv[2]))
    json.dump(E,open(sys.argv[3],'w'))
    for c,d in sorted(counts.items(),key=lambda x:-sum(x[1].values())):
        tt=sum(d.values()); top=sorted(d.items(),key=lambda x:-x[1])[:4]
        print(c,round(tt,1),' '.join('%s:%.2f'%(t,v/tt) for t,v in top))
