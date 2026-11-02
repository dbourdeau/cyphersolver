# Monotone (one-part) annealer: group value order = alphabetical order of its entry; scored by a Turner 5-gram.
import os; os.environ['OPENBLAS_NUM_THREADS']='1'; os.environ['OMP_NUM_THREADS']='1'
import numpy as np,pickle,sys,time,re,collections as C,multiprocessing as mp
from numba import njit
W=r'C:/Users/dbour/cypher/.work/delacroix1797/'
CT=r'C:/Users/dbour/cypher/targets/delacroix1797/ciphertext.txt'
L=[int(x) for l in open(CT,encoding='utf8') if l[0] not in '#f' for x in l.split()]
vals=sorted(set(L)); ix={v:i for i,v in enumerate(vals)}
toks=np.array([ix[v] for v in L],dtype=np.int32)
def vocab(minc=3,nfrag=500):
    wc=pickle.load(open(W+'wc.pkl','rb'))
    words=[w for w,c in wc.items() if c>=minc and (len(w)>1 or w in 'adlnsmjcy')]
    pre=C.Counter();suf=C.Counter()
    for w,c in wc.items():
        for k in range(2,6):
            if len(w)>k: pre[w[:k]]+=c; suf[w[-k:]]+=c
    ent={w+' ' for w in words}
    ent|={p for p,_ in pre.most_common(nfrag)}
    ent|={s+' ' for s,_ in suf.most_common(nfrag)}
    return sorted(ent,key=lambda s:(s.strip(),s))
A={c:i for i,c in enumerate('abcdefghijklmnopqrstuvwxyz ')}
def pack(V):
    off=np.zeros(len(V)+1,dtype=np.int32); buf=[]
    for i,s in enumerate(V):
        buf+= [A[c] for c in s]; off[i+1]=len(buf)
    return off,np.array(buf,dtype=np.int8)
@njit(cache=True)
def score(a,toks,off,buf,lm,b):
    h=26*27**3+26*27**2+26*27+26  # four spaces
    M=27**4; s=0.0
    for t in toks:
        v=a[t]
        for j in range(off[v],off[v+1]):
            c=buf[j]; s+=lm[h,c]+b; h=(h*27+c)%M
    return s
@njit(cache=True)
def anneal(a,toks,off,buf,lm,b,iters,T0,T1,seed):
    np.random.seed(seed); n=len(a); m=len(off)-1
    cur=score(a,toks,off,buf,lm,b); best=cur; ba=a.copy()
    for it in range(iters):
        T=T0*(T1/T0)**(it/iters)
        i=np.random.randint(n)
        lo=a[i-1] if i>0 else 0
        hi=a[i+1] if i<n-1 else m-1
        old=a[i]
        if hi<=lo: continue
        if np.random.random()<0.5:
            nv=np.random.randint(lo,hi+1)
        else:
            nv=old+np.random.randint(-8,9); nv=max(lo,min(hi,nv))
        if nv==old: continue
        a[i]=nv
        s=score(a,toks,off,buf,lm,b)
        if s>=cur or np.random.random()<np.exp((s-cur)/T):
            cur=s
            if s>best: best=s; ba[:]=a
        else: a[i]=old
    return best,ba
def run(args):
    seed,iters,b,T0,T1,V=args
    lm=np.load(W+'lm5.npy',mmap_mode='r'); off,buf=pack(V)
    rng=np.random.default_rng(seed); m=len(V)
    a=np.clip(((np.array(vals)/1200.0)*m+rng.normal(0,m*0.01,len(vals))).astype(np.int32),0,m-1); a=np.sort(a)
    best,ba=anneal(a,toks,off,buf,np.asarray(lm),b,iters,T0,T1,seed)
    return best,seed,ba
def show(V,ba):
    return ''.join(V[ba[t]] for t in toks)
if __name__=='__main__':
    iters=int(sys.argv[1]);b=float(sys.argv[2]);V=vocab()
    print('vocab',len(V),V[:5])
    t=time.time()
    with mp.Pool(10) as P: R=P.map(run,[(s,iters,b,8.0,0.3,V) for s in range(10)])
    R.sort(key=lambda r:-r[0]); print('t',time.time()-t,[round(r[0]) for r in R])
    for r in R[:3]:
        print(round(r[0]),show(V,r[2])[:700]);print()
    pickle.dump((R,V,vals),open(W+'r1.pkl','wb'))
    # agreement of top runs at entry level
    ag=C.Counter()
