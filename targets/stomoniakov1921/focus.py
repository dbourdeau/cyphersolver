import col,random,re,sys,numpy as np
from col import *
s=re.sub(r'\s','',open('voikov1883.txt').read()).lower();ct=np.array([idx[c] for c in s])
sh=ct.copy();np.random.seed(5);np.random.shuffle(sh)
its=int(sys.argv[1])
for w in (22,23,24,25,26):
    rs=[solve(ct,w,its,r) for r in range(4)];rc=[solve(sh,w,its,r) for r in range(2)]
    b=max(rs,key=lambda t:t[0])
    print(w,'real',[round(x[0],2) for x in rs],'ctrl',[round(x[0],2) for x in rc],''.join(A[i] for i in dec(ct,b[1]))[:150],'key',b[1],flush=True)
