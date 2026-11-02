"""Columnar transposition hill-climb against transliterated Russian. python col.py <frame> [wmin wmax restarts] ; pools adjacent OCR runs of a frame into messages listed in MSG."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,re,sys,random,math,collections
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'C:/Users/dbour/cypher')
from lang import lm
TR=dict(zip('абвгдезийклмнопрстуфхцыэ','abvgdeziiklmnoprstufhcye'));TR.update({'ё':'e','ж':'j','ч':'q','ш':'w','щ':'w','ь':'x','ъ':'x','ю':'u','я':'a'})
TR2=dict(TR);TR2.update({'ж':'zh','ч':'tch','ш':'sh','щ':'sch','ю':'iu','я':'ia','й':'i','х':'kh','ь':'','ъ':'','ы':'y','в':'v','ц':'ts'})
A='abcdefghijklmnopqrstuvwxyz'
def corpus(tr):
    t=open('ru_corpus.txt',encoding='utf-8').read().lower()
    return ''.join(tr.get(c,'') for c in t if c in tr)
T2=corpus(TR2);LM=lm.DenseLM.build(T2,4,A);print('corpus',len(T2),flush=True)
idx={c:i for i,c in enumerate(A)}
def read_cols(ct,order):
    n=len(ct);w=len(order);h,r=divmod(n,w)
    pos=0;cols=[None]*w
    for k in order:
        L=h+(1 if k<r else 0);cols[k]=ct[pos:pos+L];pos+=L
    return cols
def dec(ct,order):
    cols=read_cols(ct,order);L=max(len(c) for c in cols)
    x=np.empty(len(ct),dtype=int);p=0
    for i in range(L):
        for c in cols:
            if i<len(c): x[p]=c[i];p+=1
    return x
def solve(ct,w,iters=4000,seed=0):
    rnd=random.Random(seed);order=list(range(w));rnd.shuffle(order)
    cur=LM.score_idx(dec(ct,order))/len(ct);best=(cur,order[:])
    for i in range(iters):
        t=.02*(1-i/iters)+1e-4
        o=order[:];m=rnd.random()
        a,b=rnd.randrange(w),rnd.randrange(w)
        if m<.5: o[a],o[b]=o[b],o[a]
        else:
            s=rnd.randrange(1,max(2,w//2));ch=o[a:a+s];del o[a:a+s];b=rnd.randrange(len(o)+1);o[b:b]=ch
        c=LM.score_idx(dec(ct,o))/len(ct)
        if c>=cur or rnd.random()<math.exp((c-cur)/t):
            order,cur=o,c
            if cur>best[0]: best=(cur,o[:])
    return best
if __name__=='__main__':
    R=json.load(open('letter_runs.json',encoding='utf-8'))
    frame=sys.argv[1];wmin,wmax=int(sys.argv[2]),int(sys.argv[3]);rs=int(sys.argv[4]);its=int(sys.argv[5])
    runs=[r for r in R if frame in r['file']]
    s=''.join(''.join(r['groups']) for r in runs)
    s=re.sub('[^A-Z]','',s).lower();print(frame,len(s),len(runs),flush=True)
    ct=np.array([idx[c] for c in s])
    ctrl=ct.copy();np.random.seed(1);np.random.shuffle(ctrl)
    out=[]
    for w in range(wmin,wmax+1):
        b=max((solve(ct,w,its,r) for r in range(rs)),key=lambda t:t[0])
        c=max((solve(ctrl,w,its,r) for r in range(1)),key=lambda t:t[0])
        print(w,round(b[0],3),'ctrl',round(c[0],3),''.join(A[i] for i in dec(ct,b[1]))[:90],flush=True)
