import sys,json,glob
from joint import *
B1=load('msgB1.txt');B2=load('msgB2.txt');w=20
R=[json.loads(l) for f in glob.glob('Bb_*.jsonl') for l in open(f,encoding='utf-8') if l.startswith('{')]
R.sort(key=lambda r:-r['score'])
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
        # read-order slides too
        o=to_order(r)
        for a in range(w):
            for l in range(1,w-a+1):
                for b in range(w-l+1):
                    q=o[:];ch=q[a:a+l];del q[a:a+l];q[b:b]=ch
                    c=obj([m],q,'col')
                    if c>cur+1e-9: o,cur=q,c;imp=True
        r=to_rank(o)
    return cur,to_order(r)
best=None
for x in R[:3]:
    m=np.concatenate((B1,np.full(x['g'],-1),B2));c,o=polish(m,x['order']);print(x['score'],'->',round(c,3),flush=True)
    if best is None or c>best[0]: best=(c,x['g'],o)
c,g,o=best;m=np.concatenate((B1,np.full(g,-1),B2));print('FINAL',round(c,3),'gap',g,'order',o,'rank',to_rank(o))
json.dump({'gap':g,'order':o},open('keyB.json','w'));t=show(m,o);print(len(t))
for i in range(0,len(t),w): print(t[i:i+w])
