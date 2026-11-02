"""Joint columnar solver: one key, several messages, unknown letters masked (-1) and skipped in scoring.
Routes: col = plain written in rows, columns taken in key order; bou = odd-numbered output columns read upward."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import re,sys,random,math,json
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'C:/Users/dbour/cypher')
from lang import lm
TR=dict(zip('абвгдезиклмнопрстуфыэ','abvgdeziklmnoprstufye'))
TR.update({'ё':'e','й':'i','ж':'zh','х':'h','ц':'c','ч':'ch','ш':'sh','щ':'shch','ю':'iu','я':'ia','ь':'q','ъ':'q'})
A='abcdefghijklmnopqrstuvwxyz';IDX={c:i for i,c in enumerate(A)}
def corpus():
    t=open('ru_corpus.txt',encoding='utf-8').read().lower()
    return ''.join(TR.get(c,'') for c in t)
T=corpus();LM=lm.DenseLM.build(T,4,A);LP=LM.lp;K=4
def enc(s): return np.array([IDX.get(c,-1) for c in s.lower()],dtype=int)
def score(x):
    n=len(x)-K+1
    if n<=0: return 0.,0
    w=np.lib.stride_tricks.sliding_window_view(x,K);ok=(w>=0).all(1);w=w[ok]
    ctx=w[:,0]*17576+w[:,1]*676+w[:,2]*26+w[:,3]
    return float(LP[ctx].sum()),len(w)
def mapping(n,w,order,route='col'):
    h,r=divmod(n,w);lens=np.full(w,h);lens[:r]+=1
    o=np.asarray(order);st=np.zeros(w,dtype=int);st[o]=np.concatenate(([0],np.cumsum(lens[o])[:-1]))
    i=np.arange(n);col=i%w;row=i//w
    if route=='bou':
        rank=np.empty(w,dtype=int);rank[o]=np.arange(w)
        rev=rank%2==1
        return np.where(rev[col],st[col]+lens[col]-1-row,st[col]+row)
    return st[col]+row
def obj(msgs,order,route):
    a=b=0.
    for m in msgs:
        s,c=score(m[mapping(len(m),len(order),order,route)]);a+=s;b+=c
    return a/max(b,1)
def solve(msgs,w,its,seed,route='col',t0=.02):
    rnd=random.Random(seed);o=list(range(w));rnd.shuffle(o);cur=obj(msgs,o,route);best=(cur,o[:])
    for i in range(its):
        t=t0*(1-i/its)+1e-4;q=o[:];a,b=rnd.randrange(w),rnd.randrange(w);m=rnd.random()
        if m<.4: q[a],q[b]=q[b],q[a]
        elif m<.8:
            l=rnd.randrange(1,max(2,w//2));ch=q[a:a+l];del q[a:a+l];b=rnd.randrange(len(q)+1);q[b:b]=ch
        else:
            l=rnd.randrange(2,max(3,w//2));ch=q[a:a+l][::-1];q[a:a+l]=ch
        c=obj(msgs,q,route)
        if c>=cur or rnd.random()<math.exp((c-cur)/t):
            o,cur=q,c
            if cur>best[0]: best=(cur,q[:])
    return best
def show(m,o,route='col'):
    return ''.join(A[i] if i>=0 else '?' for i in m[mapping(len(m),len(o),o,route)])
def load(f): return enc(re.sub(r'\s','',open(f).read()))
