import sys, json, math, collections
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from common import *; from passages import passages
P=passages(sys.argv[1]); out=sys.argv[2]
data=[(n,norm(g)) for refs,n,g in P if norm(g)]
LMAX=int(__import__("os").environ.get("LMAX","8"))
plen={0:0.02,1:0.35,2:0.35,3:0.17,4:0.06,5:0.025,6:0.012,7:0.006,8:0.004}
uni=collections.Counter(''.join(t for n,t in data)); tot=sum(uni.values())
def base(s):
    p=plen[len(s)]
    for c in s: p*=uni[c]/tot
    return p
counts=collections.defaultdict(lambda: collections.defaultdict(float))
alpha=0.5
TOT={}
import functools
def emit(n,s):
    if n is None: return base(s)
    c=counts.get(n)
    if not c: return base(s)
    C=TOT[n]
    return (c.get(s,0.0)+alpha*base(s))/(C+alpha)
for it in range(int(sys.argv[3]) if len(sys.argv)>3 else 15):
    new=collections.defaultdict(lambda: collections.defaultdict(float)); LL=0
    for n,t in data:
        N=len(n); T=len(t)
        # forward
        F=[[0.0]*(T+1) for _ in range(N+1)]; F[0][0]=1.0; sc=[1.0]*(N+1)
        E={}
        for i in range(N):
            row=F[i]; nxt=F[i+1]
            c0=int(i*T/N); lo=max(0,c0-80); hi=min(T,c0+80)
            for j in range(lo,hi+1):
                if row[j]==0: continue
                for l in range(0,LMAX+1):
                    if j+l>T: break
                    key=(i,j,l)
                    e=emit(n[i],t[j:j+l]); E[key]=e
                    nxt[j+l]+=row[j]*e
            s=sum(nxt) or 1e-300; sc[i+1]=s
            F[i+1]=[x/s for x in nxt]
        Z=F[N][T]
        if Z<=0: continue
        LL+=math.log(Z)+sum(math.log(x) for x in sc[1:])
        B=[[0.0]*(T+1) for _ in range(N+1)]; B[N][T]=1.0
        for i in range(N-1,-1,-1):
            c0=int(i*T/N); lo=max(0,c0-80); hi=min(T,c0+80)
            for j in range(lo,hi+1):
                if F[i][j]==0: continue
                acc=0.0
                for l in range(0,LMAX+1):
                    if j+l>T: break
                    if B[i+1][j+l]==0: continue
                    v=E[(i,j,l)]*B[i+1][j+l]
                    acc+=v
                    if n[i] is not None:
                        new[n[i]][t[j:j+l]]+=F[i][j]*v/sc[i+1]/Z
                B[i][j]=acc/sc[i+1]
        # posterior already normalized because F scaled; B scaled consistently
    counts=new; TOT={k:sum(v.values()) for k,v in counts.items()}
    print('iter',it,'LL',round(LL,1),file=sys.stderr,flush=True)
key={}
for n,c in sorted(counts.items()):
    tot_=sum(c.values()); best=max(c.items(),key=lambda x:x[1])
    alts=sorted(c.items(),key=lambda x:-x[1])[:3]
    key[n]={'v':best[0],'p':round(best[1]/tot_,3),'n':round(tot_,1),'alts':[(a,round(b/tot_,2)) for a,b in alts]}
json.dump(key,open(out,'w'),ensure_ascii=False,indent=0)
# viterbi dump
if len(sys.argv)>4:
    fo=open(sys.argv[4],'w')
    for (refs,n,g) in [p for p in P if norm(p[2])]:
        t=norm(g); N=len(n); T=len(t)
        V=[[-1e18]*(T+1) for _ in range(N+1)]; BP=[[None]*(T+1) for _ in range(N+1)]; V[0][0]=0
        for i in range(N):
            for j in range(T+1):
                if V[i][j]<-1e17: continue
                for l in range(0,LMAX+1):
                    if j+l>T: break
                    e=emit(n[i],t[j:j+l])
                    if e<=0: continue
                    v=V[i][j]+math.log(e)
                    if v>V[i+1][j+l]: V[i+1][j+l]=v; BP[i+1][j+l]=(j,l)
        j=T; seg=[]
        for i in range(N,0,-1):
            if BP[i][j] is None: seg=None; break
            pj,l=BP[i][j]; seg.append((n[i-1],t[pj:pj+l])); j=pj
        fo.write('## %s\n'%(refs[0],))
        if seg: fo.write(' '.join('%s=%s'%(a,b if b else '_') for a,b in reversed(seg))+'\n')
