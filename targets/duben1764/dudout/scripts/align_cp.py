"""EM d'alignement ancré par points de passage (C03, système B). Adapté de c01/scripts/align_em.py :
même modèle (chaque groupe émet 0..LMAX lettres du clair ; nuls <100 favorisés), mais la bande suit
une interpolation linéaire par morceaux entre points de passage (index groupe -> position clair), ±BAND.
Usage: align_cp.py clear.txt checkpoints.json iters band out.json cipherfile...
cipherfile: lignes 'L<lab> g.g.g' ."""
import sys, re, math, json, collections, unicodedata, os
LMAX=9
def norm(s):
    s=unicodedata.normalize('NFD',s); s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z]','',s.lower())
def toks(paths):
    out=[]
    for p in paths:
        for l in open(p):
            if l.startswith('L'):
                out+=[t for t in l.split(' ',1)[1].strip().split('.') if t]
    return out
def lse(a,b):
    if a==-1e18: return b
    if b==-1e18: return a
    m=max(a,b); return m+math.log(math.exp(a-m)+math.exp(b-m))
def main():
    clear=norm(''.join(l for l in open(sys.argv[1]) if not l.startswith('#')))
    cps=sorted(json.load(open(sys.argv[2])))
    iters=int(sys.argv[3]); band=int(sys.argv[4]); outp=sys.argv[5]
    T=toks(sys.argv[6:]); N,M=len(T),len(clear)
    def centre(i):
        for (a,pa),(b,pb) in zip(cps,cps[1:]):
            if a<=i<=b: return pa+(pb-pa)*(i-a)/(b-a)
        (a,pa),(b,pb)=cps[-2],cps[-1]; return pb+(pb-pa)/(b-a)*(i-b)
    lo=lambda i:max(0,int(centre(i))-band); hi=lambda i:min(M,int(centre(i))+band)
    lenp={k:(math.log(0.4**abs(k-2)) if k<=4 else math.log(0.4**2)-2.0*(k-4)) for k in range(LMAX+1)}
    model=None
    NULLMODE=os.environ.get("NULLMODE","lt100")
    def isnull(t): return int(t)<100 if NULLMODE=="lt100" else False
    ANCH=json.load(open(os.environ['ANCH'])) if os.environ.get('ANCH') else {}
    def lp(t,s):
        if t in ANCH: return 0.0 if s in ANCH[t] else -30.0
        base=lenp[len(s)]+((3 if isnull(t) else -3) if len(s)==0 else (-3 if isnull(t) else 0))
        if model is None: return base
        d=model.get(t)
        if not d: return base-6
        return lse(math.log(d.get(s,0)+1e-9)-math.log(d['_tot']+0.5), base-6+math.log(0.5/(d['_tot']+0.5)))
    for it in range(iters+1):
        F=[dict() for _ in range(N+1)]; F[0][0]=0.0
        for i in range(N):
            l1,h1=lo(i+1),hi(i+1)
            for j,v in F[i].items():
                for k in range(LMAX+1):
                    jj=j+k
                    if jj>M: break
                    if jj<l1 or jj>h1: continue
                    F[i+1][jj]=lse(F[i+1].get(jj,-1e18),v+lp(T[i],clear[j:jj]))
        if it==iters: break
        B=[dict() for _ in range(N+1)]
        for j in F[N]: B[N][j]=0.0
        for i in range(N-1,-1,-1):
            for j in F[i]:
                acc=-1e18
                for k in range(LMAX+1):
                    jj=j+k
                    if jj in B[i+1]: acc=lse(acc,lp(T[i],clear[j:jj])+B[i+1][jj])
                B[i][j]=acc
        Z=-1e18
        for j,v in F[N].items(): Z=lse(Z,v)
        cnt=collections.defaultdict(lambda:collections.defaultdict(float))
        for i in range(N):
            for j,v in F[i].items():
                for k in range(LMAX+1):
                    jj=j+k
                    if jj in B[i+1]:
                        p=math.exp(v+lp(T[i],clear[j:jj])+B[i+1][jj]-Z)
                        if p>1e-3: cnt[T[i]][clear[j:jj]]+=p
        model={t:dict(d,_tot=sum(d.values())) for t,d in cnt.items()}
        print('iter',it,'logZ',round(Z,1),file=sys.stderr)
    V=[dict() for _ in range(N+1)]; V[0][0]=(0.0,None)
    for i in range(N):
        for j,(v,_) in V[i].items():
            for k in range(LMAX+1):
                jj=j+k
                if jj>M: break
                if jj<lo(i+1) or jj>hi(i+1): continue
                s=v+lp(T[i],clear[j:jj])
                if jj not in V[i+1] or V[i+1][jj][0]<s: V[i+1][jj]=(s,j)
    j=max(V[N],key=lambda x:V[N][x][0]); path=[]
    for i in range(N,0,-1):
        pj=V[i][j][1]; path.append((T[i-1],clear[pj:j],pj)); j=pj
    path=path[::-1]
    json.dump({'path':path,'model':{t:{s:round(v,3) for s,v in d.items()} for t,d in model.items()}},open(outp,'w'),ensure_ascii=False)
    print(' '.join(f'{t}={s or "∅"}' for t,s,_ in path))
main()
