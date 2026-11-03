import numpy as np, collections, math, sys
tok=[x for x in open('c40r_tokens.txt').read().split() if x not in('N','|')]
pl=open('c41r_plain.txt').read().replace(' ','')
for a,b in [('z','c'),('ç','c'),('ph','f'),('y','y')]: pl=pl.replace(a,b)
mode=sys.argv[1] if len(sys.argv)>1 else 'cons'
P=[c for c in pl if c not in 'aeiou'] if mode=='cons' else list(pl)
T=tok; n,m=len(T),len(P)
toks=sorted(set(T)); lets=sorted(set(P))
ti={t:i for i,t in enumerate(toks)}; li={l:i for i,l in enumerate(lets)}
Ti=np.array([ti[t] for t in T]); Li=np.array([li[l] for l in P])
prob=np.ones((len(lets),len(toks)))/len(toks)
SKT,SKL=math.log(0.03),math.log(0.03)   # skip token / skip letter (log prob)
B=int(sys.argv[2]) if len(sys.argv)>2 else 120
def run(prob):
    lp=np.log(prob)
    INF=-1e18
    D=np.full((n+1,m+1),INF); bp=np.zeros((n+1,m+1),dtype=np.int8)
    D[0,0]=0
    for i in range(n+1):
        for j in range(max(0,int(i*m/n)-B),min(m,int(i*m/n)+B)+1):
            if i==0 and j==0: continue
            best=INF;bk=0
            if i>0 and j>0 and D[i-1,j-1]>INF:
                v=D[i-1,j-1]+lp[Li[j-1],Ti[i-1]]
                if v>best:best,bk=v,1
            if i>0 and D[i-1,j]>INF:
                v=D[i-1,j]+SKT
                if v>best:best,bk=v,2
            if j>0 and D[i,j-1]>INF:
                v=D[i,j-1]+SKL
                if v>best:best,bk=v,3
            D[i,j]=best;bp[i,j]=bk
    i,j=n,m;pairs=[]
    while i>0 or j>0:
        k=bp[i,j]
        if k==1: pairs.append((i-1,j-1));i-=1;j-=1
        elif k==2:i-=1
        elif k==3:j-=1
        else: break
    return D[n,m],pairs[::-1]
for it in range(8):
    sc,pairs=run(prob)
    cnt=np.full((len(lets),len(toks)),0.05)
    for a,b in pairs: cnt[Li[b],Ti[a]]+=1
    prob=cnt/cnt.sum(1,keepdims=True)
    print(it,round(sc,1),len(pairs),file=sys.stderr)
# report
tab=collections.defaultdict(collections.Counter)
for a,b in pairs: tab[T[a]][P[b]]+=1
for t in sorted(tab,key=lambda x:-sum(tab[x].values())):
    c=tab[t]; tot=sum(c.values())
    print(t,tot,' '.join(f'{l}{v}' for l,v in c.most_common(5)))
