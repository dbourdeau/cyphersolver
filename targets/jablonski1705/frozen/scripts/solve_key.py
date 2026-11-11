"""Rebuild the Jablonski-Ráday syllabary from figure/plaintext pairs (pairs.tsv).
Viterbi segmentation of each plaintext over its groups, iterated (hard EM)."""
import sys, math, collections, json
def norm(s):
    s=s.lower().replace('j','i').replace('v','u').replace('w','u').replace('y','i')
    return ''.join(c for c in s if c.isalpha())
pairs=[]
for line in open(sys.argv[1],encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    f=line.rstrip('\n').split('\t')
    if f[1]=='?' : continue
    g=[x for x in f[2].split('.') if x]
    pairs.append((f[0],norm(f[1]),g,f[3] if len(f)>3 else ''))
MAXL=12
counts=collections.defaultdict(collections.Counter)
def score(g,s,it):
    c=counts[g]; tot=sum(c.values())
    if it==0:
        base={0:-2.5,1:-1.0,2:-0.8,3:-2.0}.get(len(s),-4.0-0.3*len(s))
        return base
    p=(c[s]+0.05)/(tot+1.0)
    prior={0:-2.0,1:-0.5,2:-0.4,3:-1.5}.get(len(s),-3.0-0.2*len(s))
    return math.log(p)+0.3*prior
def seg(word,g,it):
    n=len(word); m=len(g); NEG=-1e18
    best=[[NEG]*(n+1) for _ in range(m+1)]; bp=[[None]*(n+1) for _ in range(m+1)]
    best[0][0]=0
    for i in range(m):
        for j in range(n+1):
            if best[i][j]==NEG: continue
            for L in range(0,min(MAXL,n-j)+1):
                v=best[i][j]+score(g[i],word[j:j+L],it)
                if v>best[i+1][j+L]: best[i+1][j+L]=v; bp[i+1][j+L]=(j,L)
    if best[m][n]==NEG: return None,NEG
    out=[]; j=n
    for i in range(m,0,-1):
        pj,L=bp[i][j]; out.append(word[pj:pj+L]); j=pj
    return out[::-1],best[m][n]
for it in range(12):
    new=collections.defaultdict(collections.Counter); segs=[]
    for sc,w,g,nt in pairs:
        s,v=seg(w,g,it); segs.append(s)
        if s:
            for gg,ss in zip(g,s): new[gg][ss]+=1
    counts=new
key={}
for g,c in sorted(counts.items(),key=lambda x:int(x[0])):
    val,n=c.most_common(1)[0]; tot=sum(c.values())
    key[g]={'value':val,'n':n,'total':tot,'alts':{k:v for k,v in c.items() if k!=val}}
json.dump(key,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
for (sc,w,g,nt),s in zip(pairs,segs):
    print(sc,w,' '.join(f'{a}={b or "·"}' for a,b in zip(g,s)) if s else 'FAIL')
