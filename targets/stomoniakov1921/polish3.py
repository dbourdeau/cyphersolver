"""Local search on plain-column positions: slide or swap columns within the row, keeping each column's read-out rank."""
import sys,json
from joint import *
M=load('msgA.txt');w=24
o=json.load(open('keyA2.json'))
def to_rank(o):
    r=[0]*w
    for i,k in enumerate(o): r[k]=i
    return r
def to_order(r):
    o=[0]*w
    for k,i in enumerate(r): o[i]=k
    return o
r=to_rank(o);cur=obj([M],to_order(r),'col');print('start',round(cur,3))
imp=True
while imp:
    imp=False
    for a in range(w):
        for l in range(1,w-a+1):
            for b in range(w-l+1):
                q=r[:];ch=q[a:a+l];del q[a:a+l];q[b:b]=ch
                c=obj([M],to_order(q),'col')
                if c>cur+1e-9: r,cur=q,c;imp=True
    for a in range(w):
        for b in range(a+1,w):
            q=r[:];q[a],q[b]=q[b],q[a];c=obj([M],to_order(q),'col')
            if c>cur+1e-9: r,cur=q,c;imp=True
    print(round(cur,3),flush=True)
o=to_order(r);json.dump(o,open('keyA3.json','w'));print('read-out order',o);print('rank by column',r)
t=show(M,o);print(len(t))
for i in range(0,len(t),w): print(t[i:i+w])
