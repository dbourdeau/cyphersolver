"""Lost start: letters missing before the first received letter means the first columns are short. Try each prefix length at width w."""
import sys,json
from joint import *
f,w,its=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]);a,b=int(sys.argv[4]),int(sys.argv[5])
base=load(f);res=[]
for pre in range(a,b):
    m=np.concatenate((np.full(pre,-1),base))
    r=max((solve([m],w,its,s) for s in range(2)),key=lambda x:x[0]);res.append((r[0],pre,r[1]));print(pre,round(r[0],3),show(m,r[1])[:100],flush=True)
res.sort(key=lambda x:-x[0]);json.dump({'pre':res[0][1],'order':res[0][2]},open(f'P_{f[:5]}_{w}.json','w'));print('BEST',res[0][1],round(res[0][0],3))
