"""Simulated annealing: map each sign type to a letter or null (0) so the decrypt (nulls dropped) matches the crib.
Cost = alignment edit cost (token->wrong letter 1, unmatched token 1, missing letter 1)."""
import sys, numpy as np, random, math
tokfile=sys.argv[1]; iters=int(sys.argv[2]); seed=int(sys.argv[3])
crib=open('crib.txt').read().strip()
T=[t for l in open(tokfile) if l.strip() and not l.startswith('#') for t in l.split()]
types=sorted(set(T)); ti={t:i for i,t in enumerate(types)}
X=np.array([ti[t] for t in T]); Y=np.array([ord(c)-96 for c in crib]); n,m=len(X),len(Y)
K=len(types); ar=np.arange(m+1)
def cost(M):
    D=ar.astype(np.int32).copy()
    for i in range(n):
        v=M[X[i]]
        A=np.empty(m+1,np.int32)
        A[0]=D[0]+(0 if v==0 else 1)
        A[1:]=np.minimum(D[1:]+(0 if v==0 else 1), D[:-1]+(Y!=v))
        D=np.minimum.accumulate(A-ar)+ar
    return int(D[m])
random.seed(seed); rng=np.random.default_rng(seed)
letters=list(range(1,27))
M=np.array([random.choice([0]+letters) for _ in range(K)])
c=cost(M); best=(c,M.copy()); Tt=3.0
for it in range(iters):
    k=random.randrange(K); old=M[k]
    M[k]=random.choice([0,0,0]+letters)
    c2=cost(M)
    if c2<=c or random.random()<math.exp((c-c2)/Tt): c=c2
    else: M[k]=old
    Tt=max(0.05,3.0*(1-it/iters))
    if c<best[0]: best=(c,M.copy())
c,M=best
print('best',c)
print(' '.join(f'{t}={"." if M[ti[t]]==0 else chr(96+M[ti[t]])}' for t in types))
print(''.join('' if M[x]==0 else chr(96+M[x]) for x in X))
