"""Many long restarts at width 20, gaps given; print the best of each with rows; write jsonl."""
import sys,json
from joint import *
B1=load('msgB1.txt');B2=load('msgB2.txt');w=20
g0,s0,s1,its=map(int,sys.argv[1:5])
m=np.concatenate((B1,np.full(g0,-1),B2))
for s in range(s0,s1):
    b=solve([m],w,its,s,'col',.025)
    print(json.dumps({'g':g0,'seed':s,'score':round(b[0],3),'order':b[1],'text':show(m,b[1])}),flush=True)
