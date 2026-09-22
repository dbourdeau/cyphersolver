"""EM alignment of cipher tokens to the printed plaintext: each token either emits the next crib letter or is a null.
P(token type -> letter) and P(null | type) learned by forward-backward over (token i, letter j)."""
import sys, numpy as np, random
from collections import Counter, defaultdict
tokfile = sys.argv[1] if len(sys.argv)>1 else 'tokens_v1.txt'
crib = open('crib.txt').read().strip()
T=[t for l in open(tokfile) if l.strip() and not l.startswith('#') for t in l.split()]
types=sorted(set(T)); ti={t:i for i,t in enumerate(types)}
L=sorted(set(crib)); li={c:i for i,c in enumerate(L)}
X=[ti[t] for t in T]; Y=[li[c] for c in crib]
n,m=len(X),len(Y); K=len(types); A=len(L)
def run(seed):
    rng=np.random.default_rng(seed)
    E=rng.dirichlet(np.ones(A),size=K)   # emission P(letter|type)
    pn=np.full(K,0.5)                    # P(null|type)
    for it in range(200):
        # forward: f[i,j] = prob tokens[:i] emit crib[:j]
        f=np.zeros((n+1,m+1)); f[0,0]=1
        for i in range(n):
            x=X[i]
            f[i+1,:]+=f[i,:]*pn[x]
            f[i+1,1:]+=f[i,:-1]*(1-pn[x])*E[x,Y]
            s=f[i+1].sum(); f[i+1]/=s
        b=np.zeros((n+1,m+1)); b[n,m]=1
        for i in range(n-1,-1,-1):
            x=X[i]
            b[i,:]=b[i+1,:]*pn[x]
            b[i,:-1]+=b[i+1,1:]*(1-pn[x])*E[x,Y]
            s=b[i].sum(); b[i]/=s
        Z=f[n,m]
        cn=np.full(K,1e-3); ce=np.full((K,A),1e-3); ctot=np.full(K,2e-3)
        for i in range(n):
            x=X[i]
            post_null=(f[i,:]*pn[x]*b[i+1,:]).sum()
            em=f[i,:-1]*(1-pn[x])*E[x,Y]*b[i+1,1:]
            tot=post_null+em.sum()
            if tot==0: continue
            cn[x]+=post_null/tot; ctot[x]+=1
            np.add.at(ce[x],Y,em/tot)
        pn=np.clip(cn/ctot,0.01,0.99); E=ce/ce.sum(1,keepdims=True)
    # log-likelihood proxy: viterbi
    return pn,E
best=None
for seed in range(int(sys.argv[2]) if len(sys.argv)>2 else 5):
    pn,E=run(seed)
    # viterbi decode
    NEG=-1e9
    V=np.full((n+1,m+1),NEG); V[0,0]=0; bp=np.zeros((n+1,m+1),dtype=int)
    lpn=np.log(pn); lpe=np.log(1-pn)[:,None]+np.log(E+1e-12)
    for i in range(n):
        x=X[i]
        a=V[i,:]+lpn[x]
        c=np.full(m+1,NEG); c[1:]=V[i,:-1]+lpe[x,Y]
        V[i+1]=np.maximum(a,c); bp[i+1]=(c>a)
    sc=V[n,m]
    if best is None or sc>best[0]: best=(sc,seed,pn,E,bp)
sc,seed,pn,E,bp=best
print('score',sc,'seed',seed)
# backtrace
i,j=n,m; out=[]
while i>0:
    if bp[i,j]: out.append((T[i-1],crib[j-1])); j-=1
    else: out.append((T[i-1],'.'))
    i-=1
out.reverse()
print(' '.join(f'{t}={c}' for t,c in out))
m2=defaultdict(Counter)
for t,c in out: m2[t][c]+=1
for t in sorted(m2,key=lambda t:-sum(m2[t].values())): print(t,dict(m2[t]))
