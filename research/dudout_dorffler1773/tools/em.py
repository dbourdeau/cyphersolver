import sys, math, json, collections
sys.path.insert(0,__file__.rsplit('/',1)[0])
from parse import load
LMAX=7
def lse(a,b):
    if a==-1e300: return b
    if b==-1e300: return a
    m=max(a,b); return m+math.log(math.exp(a-m)+math.exp(b-m))
NEG=-1e300
def run(blocks,iters=30,skipc=math.log(0.02),skips=math.log(0.02),verbose=True):
    # unigram
    allg=''.join(b['G'] for b in blocks)
    uni=collections.Counter(allg); tot=sum(uni.values())
    lu={ch:math.log(v/tot) for ch,v in uni.items()}
    lenprior={0:0.05,1:0.25,2:0.3,3:0.25,4:0.08,5:0.04,6:0.02,7:0.01}
    E={}  # code -> dict substring->logp ; default via base
    def base(t): return math.log(lenprior[len(t)])+sum(lu.get(ch,-12) for ch in t)
    def emis(c,t):
        if c=='?' or c=='?+': return base(t)+ (0 if c=='?' else 0)
        d=E.get(c)
        if d is None: return base(t)
        v=d.get(t)
        if v is None: return d['__floor']+base(t)
        return v
    for it in range(iters):
        counts=collections.defaultdict(lambda: collections.defaultdict(float))
        LL=0
        for b in blocks:
            C=b['C']; S=b['G']; n=len(C); m=len(S)
            if m==0: continue
            # forward
            F=[[NEG]*(m+1) for _ in range(n+1)]
            F[0][0]=0.0
            em_cache={}
            for i in range(n+1):
                for j in range(m+1):
                    v=F[i][j]
                    if i==0 and j==0: pass
                    else:
                        acc=NEG
                        if j>0: acc=lse(acc,F[i][j-1]+skips)  # skip gloss char
                        if i>0:
                            acc=lse(acc,F[i-1][j]+skipc)
                            c=C[i-1]
                            for L in range(1,min(LMAX,j)+1):
                                t=S[j-L:j]
                                key=(i-1,j-L,L)
                                e=emis(c,t); em_cache[key]=e
                                acc=lse(acc,F[i-1][j-L]+e)
                        F[i][j]=acc
            Z=F[n][m]; LL+=Z
            B=[[NEG]*(m+1) for _ in range(n+1)]
            B[n][m]=0.0
            for i in range(n,-1,-1):
                for j in range(m,-1,-1):
                    if i==n and j==m: continue
                    acc=NEG
                    if j<m: acc=lse(acc,B[i][j+1]+skips)
                    if i<n:
                        acc=lse(acc,B[i+1][j]+skipc)
                        for L in range(1,min(LMAX,m-j)+1):
                            e=em_cache.get((i,j,L))
                            acc=lse(acc,B[i+1][j+L]+e)
                    B[i][j]=acc
            for (i,j,L),e in em_cache.items():
                p=F[i][j]+e+B[i+1][j+L]-Z
                if p>-12:
                    c=C[i]
                    if c.startswith('?'): continue
                    counts[c][S[j:j+L]]+=math.exp(p)
        # M step
        newE={}
        for c,d in counts.items():
            tot=sum(d.values())
            dd={t:math.log((v+0.0)/(tot+0.5)) for t,v in d.items() if v>0.05}
            dd['__floor']=math.log(0.5/(tot+0.5))
            newE[c]=dd
        E=newE
        if verbose: print('iter',it,'LL',round(LL,1),flush=True)
    return E,counts
def viterbi(C,S,E,skipc=math.log(0.02),skips=math.log(0.02)):
    pass
if __name__=='__main__':
    blocks=load(sys.argv[1])
    E,counts=run(blocks,iters=int(sys.argv[2]) if len(sys.argv)>2 else 20)
    out={}
    for c,d in sorted(counts.items(),key=lambda x:-sum(x[1].values())):
        tot=sum(d.values()); top=sorted(d.items(),key=lambda x:-x[1])[:4]
        out[c]=(round(tot,1),[(t,round(v/tot,2)) for t,v in top])
        print(c,round(tot,1),' '.join('%s:%.2f'%(t,v/tot) for t,v in top))
    json.dump(out,open(sys.argv[3] if len(sys.argv)>3 else '/dev/null','w'))
