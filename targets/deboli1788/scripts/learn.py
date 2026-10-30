"""DP alignment of cipher groups (key values) to the clear text; proposes values for unread groups.
usage: python3 learn.py KEY out.tsv cip1 clear1 [cip2 clear2 ...]"""
import sys,re,unicodedata,collections
from dec import look   # uses the key given as argv[1]
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.replace('ł','l').replace('j','i').replace('y','i'); return re.sub('[^a-z0-9]','',s)
def lev(a,b):
    p=list(range(len(b)+1))
    for i,x in enumerate(a,1):
        c=[i]
        for j,y in enumerate(b,1): c.append(min(p[j]+1,c[j-1]+1,p[j-1]+(x!=y)))
        p=c
    return p[-1]
def groups(fn):
    out=[]
    for line in open(fn,encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        out+= [g.rstrip('?') for g in line.split()[1:]]
    return out
def val(g):
    gg=re.sub('[abce]$','',g)
    vs=[gg.replace('X','0'),gg.replace('X','8')] if 'X' in gg else [gg]
    f,v=look(g)
    if v is None and any(x.isdigit() and (1775<=int(x)<=1788 or x=='4000') for x in vs): return 'P',''
    if gg=='4000': return 'P',''
    return ('K','|'.join(norm(x) for x in v.split('|'))) if v is not None else ('U',None)
BAND=120
from functools import lru_cache
lev=lru_cache(maxsize=None)(lev)
def align(gs,C):
    n=len(gs); m=len(C); INF=1e9
    D=[[INF]*(m+1) for _ in range(n+1)]; B=[[None]*(m+1) for _ in range(n+1)]
    D[0][0]=0
    for j in range(1,m+1): D[0][j]=INF
    info=[val(g) for g in gs]
    for i in range(1,n+1):
        t,v=info[i-1]
        c0=int((i-1)*m/n); lo=max(0,c0-BAND); hi=min(m,c0+BAND)
        for j in range(lo,hi+1):
            if D[i-1][j]>=INF: continue
            if t=='P':
                L=[0]; 
            elif t=='K':
                mx=max(len(x) for x in v.split('|')); mn=min(len(x) for x in v.split('|')); L=range(max(0,mn-3),mx+4)
            else: L=range(0,9)
            for l in L:
                if j+l>m: break
                s=C[j:j+l]
                c=(0 if t=='P' else min(lev(x,s) for x in v.split('|')) if t=='K' else 1.5+0.05*l)
                if D[i-1][j]+c<D[i][j+l]: D[i][j+l]=D[i-1][j]+c; B[i][j+l]=(j,s)
    # fin libre : meilleur j
    j=min(range(m+1),key=lambda x:D[n][x])
    if D[n][j]>=INF: raise ValueError('no path')
    res=[]
    for i in range(n,0,-1):
        pj,s=B[i][j]; res.append((gs[i-1],info[i-1],s)); j=pj
    return res[::-1]
if __name__=='__main__':
    out=sys.argv[2]; obs=collections.defaultdict(list)
    for k in range(3,len(sys.argv),2):
        gs=groups(sys.argv[k]); C=norm(open(sys.argv[k+1],encoding='utf-8').read())
        for g,(t,v),s in align(gs,C):
            base=re.sub('[abce]$','',g)
            if t=='U' or (t=='K' and v!=s): obs[base].append((t,v,s))
    with open(out,'w',encoding='utf-8') as f:
        for g,l in sorted(obs.items()):
            f.write(g+'\t'+' | '.join(f'{t}:{v}->{s}' for t,v,s in l)+'\n')
    print(open(out).read())
