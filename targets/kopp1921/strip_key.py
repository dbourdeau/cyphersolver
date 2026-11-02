"""Hypothesis: the clustered 4-figure messages are the plain table code of kopp0876/0877/lutowinoff plus a periodic numerical key.
For period p and each column pick the key maximising log-likelihood under the plain code's token model. Compare with shuffled controls."""
import json,re,collections,sys,math,random
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
P=[g for f in ('lutowinoff417_ct.txt','kopp0876_ct.txt','kopp0877_ct.txt') for g in open(f).read().split() if '?' not in g]
# smoothed model over 10000 tokens: whole-group counts + independent F,S
F=collections.Counter(g[:2] for g in P);S=collections.Counter(g[2:] for g in P);C=collections.Counter(P);n=len(P)
LP=np.zeros(10000)
for v in range(10000):
    a=f'{v:04d}';fa,sa=a[:2],a[2:]
    pm=(C[a]+.0)/n*.5+((F[fa]+.05)/(n+5))*((S[sa]+.05)/(n+5))*.5
    LP[v]=math.log(pm)
def dsub(arr,k):  # digitwise subtraction without carry, vectorised over key k
    d=[(arr//1000)%10,(arr//100)%10,(arr//10)%10,arr%10]
    kd=[k//1000,(k//100)%10,(k//10)%10,k%10]
    return ((d[0]-kd[0])%10)*1000+((d[1]-kd[1])%10)*100+((d[2]-kd[2])%10)*10+(d[3]-kd[3])%10
def best_key(col,mode):
    col=np.array(col);bk,bs=None,-1e18
    for k in range(10000):
        v=(col-k)%10000 if mode=='mod' else dsub(col,k)
        s=LP[v].sum()
        if s>bs: bs,bk=s,k
    return bk,bs
M=[json.loads(l) for l in open('messages_ocr.jsonl',encoding='utf-8')]
want=sys.argv[1];mn=int(sys.argv[2]);mode=sys.argv[3]
m=[m for m in M if want in m['file'] and m['n']>=mn][0]
g=[int(x) for x in m['groups'] if len(x)==4 and x.isdigit()]
print(m['file'],len(g),m['head'][-50:])
pmax=int(sys.argv[4])
for shuffled in (False,True):
    h=g[:]
    if shuffled: random.seed(3);random.shuffle(h)
    res=[]
    for p in range(1,pmax+1):
        tot=0;ks=[]
        for c in range(p):
            k,s=best_key(h[c::p],mode);tot+=s;ks.append(k)
        res.append((round(tot/len(h),3),p,ks if p<=8 else ks[:8]))
    print('shuffled' if shuffled else 'real')
    for r in res: print(r)
