# Homophonic syllabic annealer. Entries = syllables + common words; adjacent numbers softly tied; cribs pinned.
import os; os.environ['OPENBLAS_NUM_THREADS']='1'; os.environ['OMP_NUM_THREADS']='1'
import numpy as np,pickle,sys,time,re,json,collections as C,multiprocessing as mp
from numba import njit
W=r'C:/Users/dbour/cypher/.work/delacroix1797/'
CT=r'C:/Users/dbour/cypher/targets/delacroix1797/ciphertext.txt'
L=[int(x) for l in open(CT,encoding='utf8') if l[0] not in '#f' for x in l.split()]
vals=sorted(set(L)); ix={v:i for i,v in enumerate(vals)}
toks=np.array([ix[v] for v in L],dtype=np.int32)
A={c:i for i,c in enumerate('abcdefghijklmnopqrstuvwxyz')}
V_='aeiouy'
def syll(w):
    # split before a consonant (cluster) followed by a vowel: maximal onset for muta cum liquida and digraphs
    out=[];i=0;cur=''
    parts=re.findall(r'[aeiouy]+|[^aeiouy]+',w)
    segs=[]
    for p in parts: segs.append(p)
    res=[];buf=''
    for k,p in enumerate(segs):
        if p[0] in V_:
            buf+=p
        else:
            if not buf: buf=p; continue
            if k==len(segs)-1: buf+=p; continue
            if len(p)==1: res.append(buf); buf=p
            else:
                on=2 if p[-2:] in ('ch','ph','gn','qu','bl','br','cl','cr','dr','fl','fr','gl','gr','pl','pr','tr','vr','th') else 1
                res.append(buf+p[:-on]); buf=p[-on:]
    if buf: res.append(buf)
    return res
def lm_nospace():
    p=W+'lm5ns.npy'
    if os.path.exists(p): return
    t=open(W+'turner_fr.txt',encoding='utf8').read().replace(' ','')
    x=np.array([A[c] for c in t],dtype=np.int64); O=5;K=26
    idx=np.zeros(len(x)-O+1,dtype=np.int64)
    for k in range(O): idx=idx*K+x[k:len(x)-O+1+k]
    c5=np.bincount(idx,minlength=K**5).astype(float); c4=c5.reshape(-1,K).sum(1);c3=c4.reshape(-1,K).sum(1);c2=c3.reshape(-1,K).sum(1);c1=c2.reshape(-1,K).sum(1)
    p1=(c1+1)/(c1.sum()+K);p2=(c2.reshape(K,K)+13*p1[None,:])/(c1[:,None]+13)
    p3=(c3.reshape(K**2,K)+5*np.tile(p2,(K,1)))/(c2[:,None]+5)
    p4=(c4.reshape(K**3,K)+3*np.tile(p3,(K,1)))/(c3[:,None]+3)
    p5=(c5.reshape(K**4,K)+2*np.tile(p4,(K,1)))/(c4[:,None]+2)
    np.save(p,np.log(p5).astype(np.float32))
def vocab(ns=450,nw=150):
    wc=pickle.load(open(W+'wc.pkl','rb')); sc=C.Counter()
    for w,c in wc.items():
        for s in syll(w): sc[s]+=c
    S=[s for s,_ in sc.most_common(ns) if len(s)<=5]
    Wd=[w for w,_ in wc.most_common(nw) if 1<len(w)<=6]
    V=sorted(set(S)|set(Wd)|set('abcdefghijlmnopqrstuvxz'))
    pr=np.array([np.log(1+max(sc.get(v,0),wc.get(v,0))) for v in V]); pr=pr-pr.mean()
    return V,pr
def caps(V):
    wc=pickle.load(open(W+'wc.pkl','rb')); sc=C.Counter()
    for w,c in wc.items():
        for x in syll(w): sc[x]+=c
    tot=sum(sc.values())
    return np.array([653*1.8*max(sc.get(v,0),wc.get(v,0))/tot+2 for v in V])
def pack(V):
    off=np.zeros(len(V)+1,dtype=np.int32); buf=[]
    for i,s in enumerate(V):
        buf+=[A[c] for c in s]; off[i+1]=len(buf)
    return off,np.array(buf,dtype=np.int8)
@njit(cache=True)
def sc(a,toks,off,buf,lm,b):
    h=0;M=26**4;s=0.0;n=0
    for t in toks:
        v=a[t]
        for j in range(off[v],off[v+1]):
            c=buf[j]; 
            if n>=4: s+=lm[h,c]
            h=(h*26+c)%M; n+=1
    NT=1830
    return s+b*min(n,NT)
@njit(cache=True)
def over(a,cnt,cap,pen):
    use=np.zeros(len(cap))
    for i in range(len(a)): use[a[i]]+=cnt[i]
    s=0.0
    for e in range(len(cap)):
        if use[e]>cap[e]: s+=pen*(use[e]-cap[e])
    return s
@njit(cache=True)
def tie(a,nvals,lam,w):
    s=0.0
    for i in range(nvals-1):
        if w[i]>0 and a[i]==a[i+1]: s+=lam*w[i]
    return s
@njit(cache=True)
def run_sa(a,free,toks,off,buf,lm,b,lam,w,pr,mu,iters,T0,T1,seed,cap,pen):
    np.random.seed(seed);nv=len(a);m=len(off)-1;F=len(free)
    cnt=np.bincount(toks,minlength=nv)
    cur=sc(a,toks,off,buf,lm,b)+tie(a,nv,lam,w)+mu*pr[a].sum()-over(a,cnt,cap,pen)
    best=cur;ba=a.copy()
    for it in range(iters):
        T=T0*(T1/T0)**(it/iters)
        i=free[np.random.randint(F)];old=a[i]
        r=np.random.random()
        if r<0.25 and i>0 and w[i-1]>0: nn=a[i-1]
        elif r<0.5 and i<nv-1 and w[i]>0: nn=a[i+1]
        else: nn=np.random.randint(m)
        if nn==old: continue
        a[i]=nn
        s=sc(a,toks,off,buf,lm,b)+tie(a,nv,lam,w)+mu*pr[a].sum()-over(a,cnt,cap,pen)
        if s>=cur or np.random.random()<np.exp((s-cur)/T):
            cur=s
            if s>best: best=s;ba[:]=a
        else: a[i]=old
    return best,ba
def run(args):
    seed,iters,b,lam,mu,pins,T0,T1=args
    lm=np.asarray(np.load(W+'lm5ns.npy',mmap_mode='r'))
    V,pr=vocab();off,buf=pack(V);vi={v:i for i,v in enumerate(V)}
    rng=np.random.default_rng(seed)
    a=rng.integers(0,len(V),len(vals)).astype(np.int32)
    fixed=[]
    for g,s in pins.items():
        g=int(g)
        if g in ix: a[ix[g]]=vi[s]; fixed.append(ix[g])
    free=np.array([i for i in range(len(vals)) if i not in fixed],dtype=np.int32)
    w=np.array([1.0 if vals[i+1]-vals[i]==1 else (0.4 if vals[i+1]-vals[i]==2 else 0.0) for i in range(len(vals)-1)]+[0.0])
    cap=caps(V);best,ba=run_sa(a,free,toks,off,buf,lm,b,lam,w,pr,mu,iters,T0,T1,seed,cap,3.0)
    return best,seed,ba
def text(V,ba): return ''.join(V[ba[t]] for t in toks)
if __name__=='__main__':
    lm_nospace()
    iters=int(sys.argv[1]);b=float(sys.argv[2]);lam=float(sys.argv[3]);mu=float(sys.argv[4]);pins=json.load(open(sys.argv[5],encoding='utf8'))
    V,pr=vocab();print('vocab',len(V))
    t=time.time()
    vi={v:i for i,v in enumerate(V)}
    for g,s in pins.items():
        if s not in vi: print('MISSING',s); 
    with mp.Pool(12) as P: R=P.map(run,[(s,iters,b,lam,mu,pins,6.0,0.25) for s in range(12)])
    R.sort(key=lambda r:-r[0]);print('t',round(time.time()-t),[round(r[0]) for r in R])
    for r in R[:4]:
        print(round(r[0]),text(V,r[2]));print()
    # consensus across top 6 runs
    cons=C.defaultdict(C.Counter)
    for r in R[:8]:
        for i,v in enumerate(vals): cons[v][V[r[2][i]]]+=1
    cc=C.Counter(L)
    print(' '.join(f'{v}:{cons[v].most_common(1)[0][0]}/{cons[v].most_common(1)[0][1]}' for v in vals if cc[v]>=3))
    pickle.dump((R,V,vals),open(W+'r2.pkl','wb'))
