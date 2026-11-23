"""Viterbi alignment of each chunk (3 lines) under a key: per code occurrence, which gloss substring it covers.
usage: align.py scriptsdir key pages [nlines]"""
import sys,collections
sys.path.insert(0,sys.argv[1]); from vlib import *
key={}
for ln in open(sys.argv[2]):
    c,v=ln.split(); key[c]='' if v=='-' else v
pages=sys.argv[3].split(','); nl=int(sys.argv[4]) if len(sys.argv)>4 else 3
CH=chunks(rows(pages),nl)
def align(codes,g):
    # each code i emits a segment g[j:j+l], cost = edit(seg, key[c]) ; GAP absorbs 0..15 free; '#' absorbs any code free
    n,m=len(codes),len(g); INF=10**9
    D=[[INF]*(m+1) for _ in range(n+1)]; B=[[None]*(m+1) for _ in range(n+1)]
    D[0][0]=0
    def ed(a,b):
        if a==b: return 0
        p=list(range(len(b)+1))
        for i,x in enumerate(a):
            q=[i+1]
            for j,y in enumerate(b): q.append(min(p[j+1]+1,q[j]+1,p[j]+(x!=y)))
            p=q
        return p[-1]
    for i in range(n+1):
        for j in range(m+1):
            v=D[i][j]
            if v>=INF: continue
            if j<m and g[j]=='#':
                if D[i][j+1]>v: D[i][j+1]=v; B[i][j+1]=(i,j,'#')
                if i<n and D[i+1][j+1]>v: D[i+1][j+1]=v; B[i+1][j+1]=(i,j,'#c')
            if j<m and D[i][j+1]>v+1: D[i][j+1]=v+1; B[i][j+1]=(i,j,'ins')
            if i==n: continue
            c=codes[i]
            if c=='GAP':
                for l in range(0,16):
                    if j+l>m or '#' in g[j:j+l]: break
                    if D[i+1][j+l]>v: D[i+1][j+l]=v; B[i+1][j+l]=(i,j,'gap')
                continue
            val=key.get(c)
            for l in range(0,9):
                if j+l>m or '#' in g[j:j+l]: break
                cost=ed(g[j:j+l],val) if val is not None else (1 if l else 1)
                if D[i+1][j+l]>v+cost: D[i+1][j+l]=v+cost; B[i+1][j+l]=(i,j,'code')
    # backtrace
    i,j=n,m; segs=[]
    while (i,j)!=(0,0):
        pi,pj,t=B[i][j]
        if t=='code': segs.append((codes[pi],g[pj:j]))
        i,j=pi,pj
    return D[n][m],segs[::-1]
occ=collections.defaultdict(collections.Counter); tot=0
for ch in CH:
    d,segs=align(ch['codes'],ch['g'] or '#'); tot+=d
    for c,s in segs: occ[c][s]+=1
print('total cost',tot)
for c in sorted(occ,key=lambda x:int(x) if x.isdigit() else 0):
    k=key.get(c); cnt=occ[c]; n=sum(cnt.values()); agree=cnt.get(k,0)
    flag='' if agree==n else (' <<' if agree<n/2 else ' <')
    print(f"{c:>4} key={k!s:8} n={n:2} agree={agree:2}  {dict(cnt.most_common(5))}{flag}")
if len(sys.argv)>5:
    new=dict(key)
    for c,cnt in occ.items():
        if not c.isdigit(): continue
        best,bn=cnt.most_common(1)[0]
        if c=='318': continue
        if best=='' : 
            # null only if nothing else; keep previous
            alts=[(s,n) for s,n in cnt.most_common() if s]
            if alts and alts[0][1]>=1 and key.get(c) is None: new[c]=alts[0][0]
            continue
        if bn>cnt.get(key.get(c),0): new[c]=best
    with open(sys.argv[5],'w') as f:
        for c in sorted(new,key=lambda x:int(x)):
            f.write(f"{c} {new[c] or '-'}\n")
