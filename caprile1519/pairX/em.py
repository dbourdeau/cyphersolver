import math,collections,random,json,sys
sys.path.insert(0,'..')
def load():
    T={l.split('|')[0].strip():[x.replace('?','') for x in l.split('|')[2].split()] for l in open('t.txt') if l.startswith('S')}
    P={l.split()[0]:''.join(l.split()[1:]) for l in open('plain.txt') if l.startswith('S')}
    return T,P
def align(T,L,P,Kc,Kw=16,gap=-6.0):
    n,m=len(T),len(L);INF=-1e18
    D=[[INF]*(m+1) for _ in range(n+1)];B=[[None]*(m+1) for _ in range(n+1)];D[0][0]=0
    for i in range(n+1):
        for j in range(m+1):
            if i==0 and j==0: continue
            best,bb=INF,None
            if i:
                t=T[i-1];K=Kw if '[' in t else Kc
                for k in range(1,min(K,j)+1):
                    v=D[i-1][j-k]+P.get((t,L[j-k:j]),-4.0-1.0*k)
                    if v>best:best,bb=v,k
                v=D[i-1][j]+gap
                if v>best:best,bb=v,-1
            if j:
                v=D[i][j-1]+gap
                if v>best:best,bb=v,-2
            D[i][j],B[i][j]=best,bb
    i,j=n,m;al=[]
    while i or j:
        b=B[i][j]
        if b>0: al.append((T[i-1],L[j-b:j]));i-=1;j-=b
        elif b==-1: al.append((T[i-1],None));i-=1
        else: al.append((None,L[j-1]));j-=1
    return D[n][m],al[::-1]
def run(T,P,segs,Kc,it=15):
    Pm={}
    for _ in range(it):
        C=collections.Counter();tot=0;als={}
        for s in segs:
            sc,al=align(T[s],P[s],Pm,Kc);tot+=sc;als[s]=al
            for t,x in al:
                if t and x and '#' not in t: C[(t,x)]+=1
        N=collections.Counter()
        for (t,x),c in C.items(): N[t]+=c
        Pm={(t,x):math.log((c+0.1)/(N[t]+1)) for (t,x),c in C.items()}
    return tot,als,C
if __name__=='__main__':
    T,P=load();Kc=int(sys.argv[1]) if len(sys.argv)>1 else 2
    segs=list(T)
    tot,als,C=run(T,P,segs,Kc)
    key=collections.defaultdict(collections.Counter)
    for (t,x),c in C.items(): key[t][x]+=c
    for s in segs: print(s,' '.join('%s=%s'%(t,x) for t,x in als[s]))
    print('score',round(tot))
    rep=sum(max(v.values()) for v in key.values() if sum(v.values())>1);n=sum(sum(v.values()) for v in key.values() if sum(v.values())>1)
    print('repeat-sign consistency',rep,n)
