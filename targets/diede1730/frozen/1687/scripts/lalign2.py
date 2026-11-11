# Alignement lettre à lettre (homophonique) par EM dur, sauts rares. Usage: python3 lalign.py UNITS... > out
import sys, math, collections, re
def norm(s):
    s=s.lower().replace('ß','ss')
    for a,b in (('ä','a'),('ö','o'),('ü','u'),('ÿ','y'),('j','i'),('y','i'),('w','u'),('v','u')): s=s.replace(a,b)
    return re.sub('[^a-z]','',s)
U=[]
for f in sys.argv[1:]:
    for ln in open(f,encoding='utf-8'):
        p=ln.rstrip('\n').split('\t')
        if len(p)>=3: U.append((p[0],[c.strip('?') for c in p[1].split('.') if c.strip('?')],norm(p[2]),p[3] if len(p)>3 else 'SEMI'))
L='abcdefghiklmnopqrstuxz'
cnt=collections.defaultdict(collections.Counter)
def lp(c,s):
    C=cnt[c]; n=sum(C.values())
    if len(s)==1: return math.log((C[s]+0.2)/(n+0.2*22+0.5))
    if s=='': return math.log((C['']+0.1)/(n+5))-2.0
    return math.log((C[s]+0.01)/(n+5))-(4.0 if len(s)==2 else 9.0)
DEL=-6.0
KS=(0,1,2)+tuple(range(3,15))
def align(codes,t,mode):
    n,m=len(codes),len(t); NEG=-1e18
    V=[[NEG]*(m+1) for _ in range(n+1)]; B=[[None]*(m+1) for _ in range(n+1)]; V[0][0]=0
    for i in range(n+1):
        for j in range(m+1):
            v=V[i][j]
            if v<=NEG/2: continue
            if j<m and v+DEL>V[i][j+1]: V[i][j+1]=v+DEL; B[i][j+1]=(i,j,None)
            if i<n:
                if mode in ('SEMI','PREFIX') and j==m:
                    if v>V[i+1][j]: V[i+1][j]=v; B[i+1][j]=(i,j,'_')
                if mode=='SEMI' and j==0:
                    if v-1>V[i+1][j]: V[i+1][j]=v-1; B[i+1][j]=(i,j,'_')
                for k in KS:
                    if j+k<=m:
                        w=v+lp(codes[i],t[j:j+k])
                        if w>V[i+1][j+k]: V[i+1][j+k]=w; B[i+1][j+k]=(i,j,t[j:j+k])
    i,j=n,m; path=[]
    while (i,j)!=(0,0):
        pi,pj,s=B[i][j]
        if pi<i: path.append((codes[pi],s))
        else: path.append((None,t[pj]))
        i,j=pi,pj
    return list(reversed(path)), V[n][m]
for it in range(40):
    new=collections.defaultdict(collections.Counter); res=[]
    for name,codes,t,mode in U:
        a,sc=align(codes,t,mode); res.append(a)
        for c,s in a:
            if c is not None and s!='_': new[c][s]+=1
    cnt=new
for (name,codes,t,mode),a in zip(U,res):
    print(name,' '.join(f"{c}={s if s else '·'}" if c else f"[-{s}]" for c,s in a))
print('#KEY')
for c in sorted(cnt,key=lambda x:int(x)):
    C=cnt[c]; n=sum(C.values()); b,bn=C.most_common(1)[0]
    print(c,n,round(bn/n,2),' '.join(f"{s or '·'}:{k}" for s,k in C.most_common(4)))
