import numpy as np, collections, math, sys
tokfile=sys.argv[1]; mode=sys.argv[2]; stripmarks=len(sys.argv)>3 and sys.argv[3]=='base'
T=[x for l in open(tokfile) for x in l.split() if x not in('N','|')]
if stripmarks:
    import re; T=[re.match(r'\d+|[A-Za-z]+',t).group(0) for t in T]
pl=open('c41r_plain.txt').read().split()
V='aeiou'
def units(words,mode):
    out=[]
    for w in words:
        i=0
        while i<len(w):
            c=w[i]
            if c in V:
                if i==0 and mode=='cvv': out.append(c)
                i+=1; continue
            if mode in('cv','cvv') and i+1<len(w) and w[i+1] in V: out.append(c+w[i+1]); i+=2
            else: out.append(c); i+=1
    return out
P=units(pl,mode)
n=len(T); m=min(len(P),int(n*1.12)+20); P=P[:m]
toks=sorted(set(T)); lets=sorted(set(P))
ti={t:i for i,t in enumerate(toks)}; li={l:i for i,l in enumerate(lets)}
Ti=np.array([ti[t] for t in T]); Li=np.array([li[l] for l in P])
prob=np.ones((len(lets),len(toks)))/len(toks)
SK=math.log(0.04); B=40
def run(prob):
    lp=np.log(prob); INF=-1e18
    D=np.full((n+1,m+1),INF); bp=np.zeros((n+1,m+1),dtype=np.int8); D[0,0]=0
    for i in range(n+1):
        for j in range(max(0,int(i*m/n)-B),min(m,int(i*m/n)+B)+1):
            if i==0 and j==0: continue
            best=INF;bk=0
            if i>0 and j>0 and D[i-1,j-1]>INF:
                v=D[i-1,j-1]+lp[Li[j-1],Ti[i-1]]
                if v>best:best,bk=v,1
            if i>0 and D[i-1,j]>INF:
                v=D[i-1,j]+SK
                if v>best:best,bk=v,2
            if j>0 and D[i,j-1]>INF:
                v=D[i,j-1]+SK
                if v>best:best,bk=v,3
            D[i,j]=best;bp[i,j]=bk
    # free end on plaintext
    j=int(np.argmax(D[n,:])); i=n; sc=D[n,j]; pairs=[]
    while i>0 or j>0:
        k=bp[i,j]
        if k==1: pairs.append((i-1,j-1));i-=1;j-=1
        elif k==2:i-=1
        elif k==3:j-=1
        else: break
    return sc,pairs[::-1]
for it in range(10):
    sc,pairs=run(prob)
    cnt=np.full((len(lets),len(toks)),0.02)
    for a,b in pairs: cnt[Li[b],Ti[a]]+=1
    prob=cnt/cnt.sum(1,keepdims=True)
    print(it,round(sc,1),len(pairs),file=sys.stderr)
print('plain units used',pairs[-1][1]+1,'of',m)
tab=collections.defaultdict(collections.Counter)
for a,b in pairs: tab[T[a]][P[b]]+=1
for t in sorted(tab,key=lambda x:-sum(tab[x].values())):
    c=tab[t]; print(t,sum(c.values()),' '.join(f'{l}{v}' for l,v in c.most_common(4)))
