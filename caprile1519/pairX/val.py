import json,random,collections
from em import load
T,P=load()
train=[('S4',['i','n','te','r','te','ne','re']),
 ('S6',['i','n','c','he','te','r','mi','ne','si',None,None,None,'le','co','se']),
 ('S8',['co','me','si','go','ve','r','ni','que','s','to','o','ra','to','re']),
 ('S1',[None]*14+['o','ra','to','re','i','n'])]
C=collections.defaultdict(collections.Counter)
for s,vals in train:
    for t,v in zip(T[s],vals):
        if v: C[t][v]+=1
key={t:c.most_common(1)[0][0] for t,c in C.items()}
json.dump({t:dict(c) for t,c in C.items()},open('key.json','w'),indent=0)
def hits(cols,plain):
    # monotone matching: count columns whose key value can be placed in order in plain
    n,m=len(cols),len(plain);D=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        v=key.get(cols[i-1])
        for j in range(m+1):
            b=max(D[i-1][j],D[i][j-1] if j else 0)
            if v and j>=len(v) and plain[j-len(v):j]==v: b=max(b,D[i-1][j-len(v)]+1)
            D[i][j]=b
    return D[n][m]
held=['S2','S5','S7']
tot=sum(1 for s in held for t in T[s] if t in key)
real=sum(hits(T[s],P[s]) for s in held)
random.seed(1);sh=[]
for r in range(200):
    x=0
    for s in held:
        L=list(P[s]);random.shuffle(L);x+=hits(T[s],''.join(L))
    sh.append(x)
print('held-out columns with a trained value:',tot,'placed in order in true plaintext:',real)
print('shuffled plaintext mean %.1f max %d'%(sum(sh)/len(sh),max(sh)))
for s in held: print(s,' '.join(key.get(t,'.') for t in T[s]),'|',P[s])
