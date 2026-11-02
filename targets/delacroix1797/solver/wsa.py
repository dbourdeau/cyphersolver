# Annealer under a word-bigram Viterbi objective (numba). Tables built from Turner's French, optionally minus a held-out slice.
import os; os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,collections as C,math,pickle,sys,re
from numba import njit
W=r'C:/Users/dbour/cypher/.work/delacroix1797/'
MAXL=18; HB=1<<18; BB=1<<21
def hs(s):
    h=0
    for c in s: h=(h*31+ord(c)-96)&0xFFFFFFF
    return h
def tables(hold=None):
    t=open(W+'turner_fr.txt',encoding='utf8').read()
    if hold: t=t[:hold[0]]+' '+t[hold[1]:]
    t=t.split(); U=C.Counter(t); Bi=C.Counter(zip(t,t[1:]))
    words=[w for w,c in U.items() if c>=2 and len(w)<=MAXL and (len(w)>1 or w in 'adlnsmjcy')]
    wid={w:i for i,w in enumerate(words)}; tot=sum(U[w] for w in words)
    up=np.array([U[w]/tot for w in words]); uc=np.array([U[w] for w in words],dtype=np.float64)
    hk=-np.ones(HB,dtype=np.int64); hv=-np.ones(HB,dtype=np.int32)
    for w,i in wid.items():
        h=hs(w); p=h&(HB-1)
        while hk[p]!=-1: p=(p+1)&(HB-1)
        hk[p]=h*64+len(w); hv[p]=i
    bk=-np.ones(BB,dtype=np.int64); bv=np.zeros(BB,dtype=np.float32)
    for (a,b),c in Bi.items():
        if a in wid and b in wid:
            k=wid[a]*100000+wid[b]+1; p=(k*2654435761)&(BB-1)
            while bk[p]!=-1: p=(p+1)&(BB-1)
            bk[p]=k; bv[p]=c
    return hk,hv,bk,bv,up,uc,words
@njit(cache=True)
def vit(chars,hk,hv,bk,bv,up,uc,oov):
    HBm=hk.shape[0]-1;BBm=bk.shape[0]-1
    n=len(chars);K=4
    sw=-np.ones((n+1,K),dtype=np.int32)-1  # -2 empty, -1 oov state
    sv=np.full((n+1,K),-1e18)
    sw[0,0]=-1;sv[0,0]=0.0
    for i in range(n):
        # best prev
        bp=-1e18;bk0=-1
        for q in range(K):
            if sw[i,q]!=-2 and sv[i,q]>bp: bp=sv[i,q];bk0=q
        if bk0<0: continue
        h=0
        for L in range(1,min(18,n-i)+1):
            h=(h*31+chars[i+L-1]+1)&0xFFFFFFF
            key=h*64+L;p=h&HBm;w=-1
            while hk[p]!=-1:
                if hk[p]==key: w=hv[p];break
                p=(p+1)&HBm
            if w<0: continue
            e=i+L
            for q in range(K):
                pw=sw[i,q]
                if pw==-2: continue
                u=up[w]
                if pw>=0:
                    k=pw*100000+w+1;r=(k*2654435761)&BBm;cnt=0.0
                    while bk[r]!=-1:
                        if bk[r]==k: cnt=bv[r];break
                        r=(r+1)&BBm
                    x=sv[i,q]+math.log((cnt+8*u)/(uc[pw]+8))
                    if pw==w: x-=8.0
                else:
                    x=sv[i,q]+math.log(u)
                # insert
                slot=-1;worst=0;wv=1e18
                for z in range(K):
                    if sw[e,z]==w: slot=z;break
                    if sv[e,z]<wv: wv=sv[e,z];worst=z
                if slot>=0:
                    if x>sv[e,slot]: sv[e,slot]=x
                elif x>wv: sw[e,worst]=w;sv[e,worst]=x
        # oov char
        x=bp+oov;e=i+1
        slot=-1;worst=0;wv=1e18
        for z in range(K):
            if sw[e,z]==-1: slot=z;break
            if sv[e,z]<wv: wv=sv[e,z];worst=z
        if slot>=0:
            if x>sv[e,slot]: sv[e,slot]=x
        elif x>wv: sw[e,worst]=-1;sv[e,worst]=x
    return sv[n].max()
@njit(cache=True)
def objective(a,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT):
    n=0
    for t in toks: n+=off[a[t]+1]-off[a[t]]
    ch=np.zeros(n,dtype=np.int32);k=0
    for t in toks:
        for j in range(off[a[t]],off[a[t]+1]): ch[k]=buf[j];k+=1
    v=vit(ch,hk,hv,bk,bv,up,uc,oov)
    s=NT*v/n
    use=np.zeros(len(cap));gc=np.zeros(len(cap))
    for i in range(len(a)):
        use[a[i]]+=cnt[i];gc[a[i]]+=1
        if i<len(a)-1 and w[i]>0 and a[i]==a[i+1]: s+=lam*w[i]
        s+=mu*pr[a[i]]
    for e in range(len(cap)):
        if use[e]>cap[e]: s-=pen*(use[e]-cap[e])
        if gc[e]>5: s-=15.0*(gc[e]-5)
        if gc[e]>0: s+=2.0
    if n<1200: s-=3.0*(1200-n)
    if n>2200: s-=3.0*(n-2200)
    return s
@njit(cache=True)
def anneal(a,free,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT,iters,T0,T1,seed):
    np.random.seed(seed);nv=len(a);m=len(off)-1;F=len(free)
    cur=objective(a,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT);best=cur;ba=a.copy()
    p=cnt[free]/cnt[free].sum()
    cum=np.cumsum(p)
    for it in range(iters):
        T=T0*(T1/T0)**(it/iters)
        i=free[np.searchsorted(cum,np.random.random())] if np.random.random()<0.5 else free[np.random.randint(F)]
        old=a[i];r=np.random.random()
        if r<0.2 and i>0 and w[i-1]>0: nn=a[i-1]
        elif r<0.4 and i<nv-1 and w[i]>0: nn=a[i+1]
        else: nn=np.random.randint(m)
        if nn==old: continue
        a[i]=nn
        s=objective(a,toks,off,buf,cnt,cap,pen,w,lam,pr,mu,hk,hv,bk,bv,up,uc,oov,NT)
        if s>=cur or np.random.random()<np.exp((s-cur)/T):
            cur=s
            if s>best: best=s;ba[:]=a
        else: a[i]=old
    return best,ba
