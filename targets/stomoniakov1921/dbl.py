"""Double columnar with small widths, exhaustive: both 'read off by columns' stages. Also the header digits as numeric keys."""
import col,sys,re,itertools,numpy as np,time
from col import *
s=re.sub(r'\s','',open(sys.argv[1]).read()).lower();ct=np.array([idx[c] for c in s]);n=len(ct)
def decode_map(n,w,order):
    # positions: returns array p so that plain[i]=ct[p[i]] for columnar read in 'order'
    h,r=divmod(n,w);start={};pos=0
    for k in order:
        L=h+(1 if k<r else 0);start[k]=pos;pos+=L
    p=np.empty(n,dtype=np.int32)
    for i in range(n):
        p[i]=start[i%w]+i//w
    return p
res=[]
W=int(sys.argv[2])
maps={w:[(o,decode_map(n,w,o)) for o in itertools.permutations(range(w))] for w in range(2,W+1)}
print({w:len(v) for w,v in maps.items()},flush=True)
for w1 in range(2,W+1):
    for w2 in range(2,W+1):
        best=(-99,)
        t=time.time()
        for o2,p2 in maps[w2]:
            y=ct[p2]
            for o1,p1 in maps[w1]:
                x=y[p1]
                sc=LM.score_idx(x[:220])/220
                if sc>best[0]: best=(sc,o1,o2)
        o1,o2=best[1],best[2]
        x=ct[decode_map(n,w2,o2)][decode_map(n,w1,o1)]
        print(w1,w2,round(best[0],3),''.join(A[i] for i in x)[:90],round(time.time()-t),'s',flush=True)
