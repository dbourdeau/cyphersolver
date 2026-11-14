# C04 training-only tool: align groups of a block to its gloss (DP), list per-group the gloss substring it covers.
import json, re, sys, collections
sys.path.insert(0, 'fable')
from measure import norm, blocks
def dec(g, T):
    k = re.sub(r'[^0-9]', '', g)
    v = T.get(k) if k and '?' not in g else None
    if isinstance(v, list): v = v[0]
    return None if v is None else norm(v)
def lev(a,b):
    p=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        c=[i]
        for j,cb in enumerate(b,1): c.append(min(p[j]+1,c[j-1]+1,p[j-1]+(ca!=cb)))
        p=c
    return p[-1]
def align(groups, gl, T):
    # each group consumes gloss substring of length 0..6; cost = lev(dec, sub) (unknown: len diff from 2)
    n, m = len(groups), len(gl); INF=10**9
    D=[[INF]*(m+1) for _ in range(n+1)]; B=[[None]*(m+1) for _ in range(n+1)]
    D[0][0]=0
    for j in range(1,m+1): D[0][j]=j; B[0][j]=('skip',)
    for i in range(1,n+1):
        d=dec(groups[i-1],T)
        for j in range(m+1):
            best=(INF,None)
            if j>0 and D[i][j-1]+1<best[0]: best=(D[i][j-1]+1,('skip',))
            for L in range(0,min(8,j)+1):
                sub=gl[j-L:j]
                c = lev(d,sub) if d is not None else abs(L-2)*0.5+0.5
                if D[i-1][j-L]+c<best[0]: best=(D[i-1][j-L]+c,('g',L))
            D[i][j]=best[0]; B[i][j]=best[1]
    out=[]; i,j=n,m
    while i>0 or j>0:
        b=B[i][j]
        if b[0]=='skip': j-=1; continue
        L=b[1]; out.append((groups[i-1], gl[j-L:j])); i-=1; j-=L
    return out[::-1], D[n][m]
if __name__=='__main__':
    T={k:v for k,v in json.load(open(sys.argv[1])).items() if not k.startswith('_')}
    C,G=blocks(sys.argv[2],'C'),blocks(sys.argv[3],'G')
    stats=collections.defaultdict(collections.Counter)
    for b in G:
        if b not in C: continue
        al,cost=align(C[b],norm(''.join(G[b])),T)
        print('##',b,cost)
        print(' '.join(f"{g}={dec(g,T)}/{s}" for g,s in al))
        for g,s in al: stats[re.sub(r'[^0-9?]','',g)][s]+=1
    print('\n## per group mismatches')
    for g in sorted(stats,key=lambda x:(len(x),x)):
        d=dec(g,T); c=stats[g]
        bad=sum(v for s,v in c.items() if s!=d)
        if bad: print(g, d, dict(c.most_common()))
