import col,random,numpy as np,sys,re
from col import *
s=re.sub(r'\s','',open(sys.argv[1]).read()).lower();ct=np.array([idx[c] for c in s])
a,b,its,rs=map(int,sys.argv[2:6]);mode=sys.argv[6]
def invert_solve(ct,w,its,seed):
    # encipher by writing into columns in key order and reading rows: decode = read rows into key-ordered columns
    n=len(ct);h,r=divmod(n,w)
    rnd=random.Random(seed);o=list(range(w));rnd.shuffle(o)
    def D(order):
        # ct written row by row in width w; columns then read in order
        cols=[ct[i::w] for i in range(w)]
        return np.concatenate([cols[k] for k in order])
    cur=LM.score_idx(D(o))/n;best=(cur,o[:])
    for i in range(its):
        t=.02*(1-i/its)+1e-4;q=o[:];x,y=rnd.randrange(w),rnd.randrange(w)
        if rnd.random()<.5: q[x],q[y]=q[y],q[x]
        else:
            l=rnd.randrange(1,max(2,w//2));ch=q[x:x+l];del q[x:x+l];y=rnd.randrange(len(q)+1);q[y:y]=ch
        c=LM.score_idx(D(q))/n
        if c>=cur or rnd.random()<math.exp((c-cur)/t):
            o,cur=q,c
            if cur>best[0]: best=(cur,q[:])
    return best,D(best[1])
for w in range(a,b+1):
    if mode=='col':
        B=max((solve(ct,w,its,r) for r in range(rs)),key=lambda t:t[0]);txt=''.join(A[i] for i in dec(ct,B[1]))
    else:
        B,d=max((invert_solve(ct,w,its,r) for r in range(rs)),key=lambda t:t[0][0]);txt=''.join(A[i] for i in d)
    print(mode,w,round(B[0],3),txt[:110],flush=True)
