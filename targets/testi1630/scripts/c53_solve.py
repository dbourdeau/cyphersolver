# c53_solve.py : ciphertext-only annealing on the key-free copy of c. 53r. Letter model: joint trigrams from this folder's own Italian
# readings with doubled letters collapsed, because the copy shows almost no doubled signs. Bijection on the 20 letters, surplus signs free.
import re,random,math,glob,collections,unicodedata,sys
import numpy as np
txt=''
for f in glob.glob('reading_*.md'):
    s=open(f,encoding='utf8').read().split('## Italian')[1].split('## English')[0].replace('*','')
    txt+=' '+s
txt=unicodedata.normalize('NFD',txt.lower()); txt=re.sub(r'[^a-z]','',txt).replace('v','u').replace('j','i').replace('k','').replace('w','').replace('x','s').replace('y','i')
txt=re.sub(r'(.)\1+',r'\1',txt)
A='abcdefghilmnopqrstuz'; ix={c:i for i,c in enumerate(A)}
T=np.full((20,20,20),0.2)
for i in range(len(txt)-2): T[ix[txt[i]],ix[txt[i+1]],ix[txt[i+2]]]+=1
T=np.log(T/T.sum())
seq=[]
for l in open('scans/blind/read_c53.txt',encoding='utf8'):
    m=re.match(r'53r \d+:\s*(.*)',l)
    if m:
        for t in re.sub(r'\{[^}]*\}',' ',m[1]).split():
            t=re.sub(r'\[blot:(.*)\]',r'\1',t)
            if t!='?': seq.append(t)
c=collections.Counter(seq); S=sorted(c,key=lambda k:-c[k]); idx={k:i for i,k in enumerate(S)}; q=np.array([idx[x] for x in seq])
n=len(S)
FR=[k for k,_ in collections.Counter(txt).most_common()]
def score(k):
    p=k[q]; return T[p[:-2],p[1:-1],p[2:]].sum()
rng=np.random.default_rng(1634); best=None; res=[]
for rs in range(40):
    base=[ix[x] for x in FR][:n]+[int(rng.integers(20)) for _ in range(max(0,n-20))]
    k=np.array(rng.permutation(base)); s=score(k); Tm=6.0
    for it in range(40000):
        a=int(rng.integers(n)); old=k.copy()
        if rng.random()<.8:
            b=int(rng.integers(n)); k[a],k[b]=k[b],k[a]
        else: k[a]=int(rng.integers(20))
        t=score(k)
        if t>=s or rng.random()<math.exp((t-s)/Tm): s=t
        else: k=old
        Tm=max(0.15,Tm*0.99985)
    res.append(s)
    if best is None or s>best[0]:
        best=(s,k.copy()); print(rs,round(s/len(q),3),''.join(A[i] for i in k[q])[:150],flush=True)
s,k=best
print('scores',sorted(round(x/len(q),3) for x in res)[-6:])
print({S[i]:A[k[i]] for i in range(n)}); print(''.join(A[i] for i in k[q]))
# control: the same model and search on the known 1630 plaintext of the same length, shuffled key
