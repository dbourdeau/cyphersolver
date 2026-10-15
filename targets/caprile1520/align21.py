"""Monotone EM alignment of sign tokens to known plaintext letters (homophonic key from cribs)."""
import re, math, collections, sys
def toks(src, merge=True):
    out=[]
    for line in open('caprile1521_transcription.txt',encoding='utf8'):
        if not line.startswith(src+' '): continue
        s=re.sub(r'\[[^\]]*\]',' ',line.split(':',1)[1])
        t=[x.rstrip('?') for x in s.split() if x!='#']
        out+=t
    if merge:
        j=' '.join(out).replace('o SL o','OSO').replace('n t','NT').replace('m t','MT')
        out=j.split()
    return out
def plain(txt): return re.sub(r'[^a-z]','',txt.lower().replace('j','i').replace('v','u'))
def em(pairs, iters=12):
    P=collections.defaultdict(lambda:1e-2)
    for it in range(iters):
        C=collections.defaultdict(float); aligns=[]
        for T,L in pairs:
            n,m=len(T),len(L); INF=-1e18
            D=[[INF]*(m+1) for _ in range(n+1)];B=[[None]*(m+1) for _ in range(n+1)]
            D[0][0]=0
            gapT,gapL=-6,-6   # null sign / letter omitted
            for i in range(n+1):
                for j in range(m+1):
                    if i==j==0: continue
                    best=(INF,None)
                    if i and j:
                        v=D[i-1][j-1]+math.log(P[(T[i-1],L[j-1])] if it else (0.2 if True else 0))
                        best=max(best,(v,'d'))
                    if i: best=max(best,(D[i-1][j]+gapT,'t'))
                    if j: best=max(best,(D[i][j-1]+gapL,'l'))
                    D[i][j],B[i][j]=best
            i,j=n,m;al=[]
            while i or j:
                b=B[i][j]
                if b=='d': al.append((T[i-1],L[j-1]));i-=1;j-=1
                elif b=='t': al.append((T[i-1],None));i-=1
                else: al.append((None,L[j-1]));j-=1
            al.reverse();aligns.append(al)
            for t,l in al:
                if t and l: C[(t,l)]+=1
        tot=collections.Counter()
        for (t,l),c in C.items(): tot[t]+=c
        P=collections.defaultdict(lambda:1e-3,{(t,l):(c+0.01)/(tot[t]+0.3) for (t,l),c in C.items()})
    return P,C,aligns
