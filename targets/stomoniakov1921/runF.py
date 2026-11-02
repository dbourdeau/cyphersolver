"""python runF.py <file> <its> <restarts> <prefix-lost> w1 w2 ... ; prints score and text, shuffled control per width."""
import sys,json
from joint import *
f,its,rs,pre=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]);ws=map(int,sys.argv[5:])
m=np.concatenate((np.full(pre,-1),load(f)));v=m[m>=0].copy();np.random.default_rng(2).shuffle(v);c=m.copy();c[c>=0]=v
print(f,len(m),flush=True)
for w in ws:
    r=[solve([m],w,its,i) for i in range(rs)];b=max(r,key=lambda x:x[0]);k=solve([c],w,its,77)
    print(f[:5],'pre',pre,w,round(b[0],3),'ctrl',round(k[0],3),show(m,b[1])[:120],flush=True)
    json.dump(b[1],open(f'F_{f[:5]}_{pre}_{w}.json','w'))
