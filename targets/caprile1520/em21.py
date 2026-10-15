DEF=0.04
import align21 as A, math, collections, re, sys
crib=open('crib_somogyi.md',encoding='utf8').read()
def caps(s):  # enciphered part = capitals (plus 'et' inside) ; take all letters after salutation
    return A.plain(s)
V20=A.plain(crib.split('## V1920')[1].split('\n',1)[1].replace('„se v. ex.a',''))
def tk(src):
    out=[]
    for line in open('caprile1521_transcription.txt',encoding='utf8'):
        if not line.startswith(src+' '): continue
        s=re.sub(r'\[[^\]]*\]',' ',line.split(':',1)[1])
        out+=[x.rstrip('?') for x in s.split() if x!='#']
    return ' '.join(out).replace('m t','MT').replace('n t','NT').split()
def viterbi(T,L,P,gap=-4.5):
    n,m=len(T),len(L);INF=-1e18
    D=[[INF]*(m+1) for _ in range(n+1)];B=[[0]*(m+1) for _ in range(n+1)];D[0][0]=0
    for i in range(n+1):
        Di=D[i];Bi=B[i]
        for j in range(m+1):
            if i==0 and j==0: continue
            best=INF;bb=0
            if i and j:
                v=D[i-1][j-1]+math.log(P.get((T[i-1],L[j-1]),DEF))
                if v>best: best,bb=v,1
            if i:
                v=D[i-1][j]+gap
                if v>best: best,bb=v,2
            if j:
                v=Di[j-1]+gap
                if v>best: best,bb=v,3
            Di[j]=best;Bi[j]=bb
    i,j=n,m;al=[]
    while i or j:
        b=B[i][j]
        if b==1: al.append((T[i-1],L[j-1]));i-=1;j-=1
        elif b==2: al.append((T[i-1],None));i-=1
        else: al.append((None,L[j-1]));j-=1
    return D[n][m],al[::-1]
def reest(C):
    tot=collections.Counter()
    for (t,l),c in C.items(): tot[t]+=c
    return {(t,l):(c+0.02)/(tot[t]+0.5) for (t,l),c in C.items()}
if __name__=='__main__':
    pairs=[(tk('V1920'),V20)]
    seed={'B':'s','MT':'o','QB':'i','z':'u','LAM':'r'}
    P={(t,l):0.6 for t,l in seed.items()}
    for it in range(15):
        C=collections.Counter();tot=0;als=[]
        for T,L in pairs:
            sc,al=viterbi(T,L,P);tot+=sc;als.append(al)
            for t,l in al:
                if t and l: C[(t,l)]+=1
        for t,l in seed.items(): C[(t,l)]+=2
        P=reest(C)
        key=collections.defaultdict(collections.Counter)
        for (t,l),c in C.items(): key[t][l]+=c
        pure=sum(max(c.values()) for c in key.values())/sum(sum(c.values()) for c in key.values())
        print(it,round(tot),round(pure,3))
    for t,c in sorted(key.items(),key=lambda x:-sum(x[1].values())): print(t,dict(c.most_common(3)))
    al=als[0]
    print(' '.join(f"{t or '-'}={l or '-'}" for t,l in al[:120]))
