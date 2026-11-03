# ciphertext-only: permutation over the frequent signs, free values for rare signs. No crib.
import random,math,sys,json,collections
import numpy as np
A='abcdefghilmnopqrstuz'; idx={c:i for i,c in enumerate(A)}; N=20
Q=np.load('scans/corpus/q4.npy')
ct=open(sys.argv[1]).read().strip().replace('3','B')
R=int(sys.argv[2]); IT=int(sys.argv[3]) if len(sys.argv)>3 else 150000
cnt=collections.Counter(ct); signs=[s for s,_ in cnt.most_common()]; si={s:i for i,s in enumerate(signs)}
C=np.array([si[x] for x in ct]); ns=len(signs)
nfreq=min(20,ns)
def score(key):
    P=key[C]; return Q[P[:-3],P[1:-2],P[2:-1],P[3:]].sum()
rng=random.Random(int(sys.argv[4]) if len(sys.argv)>4 else 1)
res=[]
for rs in range(R):
    perm=list(range(N)); rng.shuffle(perm)
    key=np.array([perm[i] if i<nfreq else rng.randrange(N) for i in range(ns)])
    cur=score(key); T=25.0; dec=(0.4/25)**(1/IT)
    for it in range(IT):
        if ns>nfreq and rng.random()<0.08:
            k=rng.randrange(nfreq,ns); old=key[k]; key[k]=rng.randrange(N); s=score(key)
            if s>=cur or rng.random()<math.exp((s-cur)/T): cur=s
            else: key[k]=old
        else:
            a,b=rng.randrange(nfreq),rng.randrange(nfreq)
            key[a],key[b]=key[b],key[a]; s=score(key)
            if s>=cur or rng.random()<math.exp((s-cur)/T): cur=s
            else: key[a],key[b]=key[b],key[a]
        T*=dec
    pt=''.join(A[key[x]] for x in C)
    print(rs,round(cur),pt[:100],flush=True); res.append((cur,key.copy(),pt))
res.sort(key=lambda r:-r[0]); b=res[0]
k={signs[i]:A[b[1][i]] for i in range(ns)}
print(round(b[0]),sorted(k.items())); print(b[2][:900])
json.dump(k,open(sys.argv[5] if len(sys.argv)>5 else 'work/key_auto.json','w'))
