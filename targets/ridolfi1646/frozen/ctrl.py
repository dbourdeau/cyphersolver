import json,random,re,collections,numpy as np,sys
from load import *
from lm import AL,IDX
Z=np.load('lm.npz'); L4=Z['L4']
lex=json.load(open('lexique-it-cyphersolver.json'))
W=set()
for w,n in lex.items():
    w=w.lower().replace('v','u').replace('j','i')
    for a,b in zip('àèéìòù','aeeiou'): w=w.replace(a,b)
    if re.fullmatch('[a-z]+',w) and len(w)>=4 and n>=3: W.add(w)
MAXL=max(map(len,W))
K=json.load(open('k.json'))
t,pos=load()
def segs(K,pages=(1,2,3,4)):
    out=[];cur=''
    for tok,(p,li,j,raw) in zip(t,pos):
        if p not in pages: continue
        if tok in K and len(tok)==2: cur+=K[tok]
        else:
            if cur: out.append(cur)
            cur=''
    if cur: out.append(cur)
    return out
def cover(s):
    n=len(s); best=[0]*(n+1)
    for i in range(1,n+1):
        best[i]=best[i-1]
        for l in range(4,min(MAXL,i)+1):
            if s[i-l:i] in W and best[i-l]+l>best[i]: best[i]=best[i-l]+l
    return best[n]
def metrics(K,pages=(1,2,3,4)):
    S=segs(K,pages); tot=sum(map(len,S)); cov=sum(cover(s) for s in S)
    q=0;nq=0
    for s in S:
        x=[IDX[ch] for ch in s if ch in IDX]
        for i in range(len(x)-3): q+=L4[x[i],x[i+1],x[i+2],x[i+3]]; nq+=1
    return cov/tot, q/max(nq,1)
def shuffled(K,rng):
    let=[g for g in K if len(K[g])==1]; syl=[g for g in K if len(K[g])>1]
    K2={}
    for grp in (let,syl):
        v=[K[g] for g in grp]; rng.shuffle(v); K2.update(dict(zip(grp,v)))
    return K2
if __name__=='__main__':
    for pages in ((1,2,3,4),(1,2),(3,4)):
        c,q=metrics(K,pages)
        rng=random.Random(1); R=[metrics(shuffled(K,rng),pages) for _ in range(200)]
        cs=[r[0] for r in R]; qs=[r[1] for r in R]
        print('pages',pages,'CLE PROPOSEE: couverture lexique(mots>=4) %.3f  quadrigr/car %.3f'%(c,q))
        print('   200 cles melangees: couverture max %.3f moy %.3f ; quadrigr max %.3f moy %.3f'%(max(cs),np.mean(cs),max(qs),np.mean(qs)))
    # reference: real Italian corpus chunk
    s=open('it.txt').read().replace('v','u').replace(' ','')[20000:23000]
    x=[IDX[ch] for ch in s if ch in IDX]; print('reference corpus 1629: couverture %.3f quadrigr %.3f'%(cover(s)/len(s), np.mean([L4[x[i],x[i+1],x[i+2],x[i+3]] for i in range(len(x)-3)])))
