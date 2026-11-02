"""Message B at width 20: anneal each gap near the hit, polish by column position, keep the best. Print rows."""
import sys,json
from joint import *
B1=load('msgB1.txt');B2=load('msgB2.txt');w=20
def to_rank(o):
    r=[0]*w
    for i,k in enumerate(o): r[k]=i
    return r
def to_order(r):
    o=[0]*w
    for k,i in enumerate(r): o[i]=k
    return o
def polish(m,o):
    r=to_rank(o);cur=obj([m],o,'col');imp=True
    while imp:
        imp=False
        for a in range(w):
            for l in range(1,w-a+1):
                for b in range(w-l+1):
                    q=r[:];ch=q[a:a+l];del q[a:a+l];q[b:b]=ch
                    c=obj([m],to_order(q),'col')
                    if c>cur+1e-9: r,cur=q,c;imp=True
        for a in range(w):
            for b in range(a+1,w):
                q=r[:];q[a],q[b]=q[b],q[a];c=obj([m],to_order(q),'col')
                if c>cur+1e-9: r,cur=q,c;imp=True
    return cur,to_order(r)
st=json.load(open('KB_20.json'));best=None
for g in range(int(sys.argv[1]),int(sys.argv[2])):
    m=np.concatenate((B1,np.full(g,-1),B2))
    runs=[st['o']]+[solve([m],w,int(sys.argv[3]),s)[1] for s in range(2)]
    for o in runs:
        c,q=polish(m,o)
        if best is None or c>best[0]: best=(c,g,q)
    print(g,round(max(obj([m],x,'col') for x in runs),3),'best so far',round(best[0],3),best[1],flush=True)
c,g,o=best;m=np.concatenate((B1,np.full(g,-1),B2));print('FINAL',round(c,3),'gap',g,'order',o,'rank',to_rank(o))
json.dump({'gap':g,'order':o},open('keyB.json','w'));t=show(m,o);print(len(t))
for i in range(0,len(t),w): print(t[i:i+w])
