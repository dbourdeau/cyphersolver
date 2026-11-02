"""Polish a found key: python pol.py <msgfile> <keyjson> [prefix]; column-position and read-order moves; prints rows, saves <msgfile>.key.json"""
import sys,json
from joint import *
f=sys.argv[1];o=json.load(open(sys.argv[2]));pre=int(sys.argv[3]) if len(sys.argv)>3 else 0
m=np.concatenate((np.full(pre,-1),load(f)));w=len(o)
def rk(o):
    r=[0]*w
    for i,k in enumerate(o): r[k]=i
    return r
def od(r):
    x=[0]*w
    for k,i in enumerate(r): x[i]=k
    return x
cur=obj([m],o,'col');imp=True
while imp:
    imp=False
    for mode in ('rank','order'):
        s=rk(o) if mode=='rank' else o[:]
        cv=(lambda q:od(q)) if mode=='rank' else (lambda q:q)
        for a in range(w):
            for l in range(1,w-a+1):
                for b in range(w-l+1):
                    q=s[:];ch=q[a:a+l];del q[a:a+l];q[b:b]=ch
                    c=obj([m],cv(q),'col')
                    if c>cur+1e-9: s,cur=q,c;imp=True
        for a in range(w):
            for b in range(a+1,w):
                q=s[:];q[a],q[b]=q[b],q[a];c=obj([m],cv(q),'col')
                if c>cur+1e-9: s,cur=q,c;imp=True
        o=cv(s)
print(round(cur,3),'order',o,'rank',rk(o));json.dump(o,open(f+'.key.json','w'))
t=show(m,o)
for i in range(0,len(t),w): print(t[i:i+w])
print(t)
