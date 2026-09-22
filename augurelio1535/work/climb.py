import sys,json;sys.path.insert(0,'../..')
from lang import lm
M=lm.load('de-1500s',spaces=False)
K10=dict(kv.split('=') for kv in "#=g +=r 2=r 3=u 4=e 5=a 6=d 7=m 8=n 9=o @=w A=u B=s D=f H=a J=k L=s O=t Q=g S=h Y=r Z=u a=e b=l c=c d=l g=r m=i n=w o=a p=i q=n t=z v=r w=e x=s y=t X=e E=d".split())
K13=dict(kv.split('=') for kv in open('../r9413/key_v3.txt').read().split())
t=open(sys.argv[1],encoding='utf8').read().replace(' ','')
toks=sorted(set(t))
LET=list('abcdefghiklmnopqrstuwz')+['ch']
import math
from collections import Counter
G=dict(e=17.0,n=10.0,i=7.5,r=7.0,s=7.0,t=6.2,a=6.0,d=5.0,h=4.8,u=4.4,l=3.4,c=3.0,g=3.0,m=2.5,o=2.5,b=1.9,w=1.9,f=1.7,k=1.2,z=1.1,p=0.8,v=0.6,j=0.2,y=0.1,q=0.05,x=0.05)
Z=sum(G.values()); G={k:v/Z for k,v in G.items()}
W=float(sys.argv[3]) if len(sys.argv)>3 else 1.5
def sc(K):
    s=''.join(K.get(c,'') for c in t); n=len(s); C=Counter(s)
    kl=sum(v/n*math.log((v/n)/G.get(k,1e-4)) for k,v in C.items())
    return M.score_idx(M.encode(s)) - W*n*kl
PIN=set(sys.argv[5]) if len(sys.argv)>5 else set()
best=None
K0=json.load(open(sys.argv[4])) if len(sys.argv)>4 else K10
for start in (K0,):
    K={c:start.get(c,'e') for c in toks}
    for c in toks:
        if len(K[c])>1 and K[c] not in LET: K[c]='e'
    cur=sc(K)
    for sweep in range(6):
        ch=0
        for c in [c for c in sorted(toks,key=lambda c:-t.count(c)) if c not in PIN]:
            o=K[c]
            for L in LET:
                K[c]=L; s=sc(K)
                if s>cur+1e-9: cur,o,ch=s,L,1
            K[c]=o
        if not ch: break
    print(cur, cur/len(t))
    if best is None or cur>best[0]: best=(cur,dict(K))
K=best[1]
json.dump(K,open(sys.argv[2],'w'),ensure_ascii=False)
print(' '.join(f'{c}={K[c]}' for c in toks))
print(''.join(K[c] for c in t)[:1500])
