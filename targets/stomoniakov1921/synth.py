import col,random,numpy as np,time,sys
from col import *
T=col.T2
s=T[200000:200615];real=np.array([idx[c] for c in s]);print('real text score',round(LM.score_idx(real)/len(real),3),s[:80])
for w in (12,24,35):
    rnd=random.Random(w);key=list(range(w));rnd.shuffle(key)
    n=len(real);h,r=divmod(n,w)
    cols=[real[i::w] for i in range(w)]
    ct=np.concatenate([cols[k] for k in key])
    t=time.time();b=max((solve(ct,w,int(sys.argv[1]),i) for i in range(2)),key=lambda t:t[0])
    print(w,'found',round(b[0],3),'true key ok',b[1]==key,round(time.time()-t,1),'s',''.join(A[i] for i in dec(ct,b[1]))[:70])
