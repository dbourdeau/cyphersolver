"""EM d'alignement chiffré <-> clair contemporain (séance C01).
Chaque groupe émet une sous-chaîne de 0..LMAX lettres du clair (0 = nul). Forward-backward en log, bande diagonale,
fin libre. Sortie : table groupe -> sous-chaînes (comptes attendus) + alignement Viterbi."""
import sys, re, math, json, unicodedata, collections
LMAX=11
import os
ANCHFILE=os.environ.get('ANCH')
def norm(s):
    s=unicodedata.normalize('NFD',s); s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z]','',s.lower())
def toks(paths):
    out=[]
    for p in paths:
        for l in open(p):
            if l.startswith('L'):
                out+=[('999X' if '[' in t else t.replace('?','')) for t in re.split(r'[.|]',l.split(' ',1)[1].strip()) if t]
    return out
def num(t):
    d=re.sub(r'\D','',t); return int(d) if d else 999
def lse(a,b):
    if a==-1e18: return b
    if b==-1e18: return a
    m=max(a,b); return m+math.log(math.exp(a-m)+math.exp(b-m))
def run(T,C,iters,ratio,band):
    N,M=len(T),len(C)
    lenp={k:(math.log(0.35**abs(k-2)) if k<=4 else math.log(0.35**2)-2.5*(k-4)) for k in range(LMAX+1)}
    ANCH=json.load(open(ANCHFILE)) if ANCHFILE else {}
    model=None
    def lp(t,s):
        if t in ANCH: return 0.0 if s in ANCH[t] else -30.0
        if model is None:
            v=lenp[len(s)]
            if len(s)==0: v+= 3 if num(t)<100 else -4
            return v
        d=model.get(t)
        base=lenp[len(s)]+(( 3 if num(t)<100 else -4) if len(s)==0 else 0)-6
        if not d: return base
        return lse(math.log(d.get(s,0)+1e-9)-math.log(d['_tot']+0.5), base+math.log(0.5/(d['_tot']+0.5)))
    for it in range(iters):
        lo=lambda i:max(0,int(i*ratio)-band); hi=lambda i:min(M,int(i*ratio)+band)
        F=[dict() for _ in range(N+1)]; F[0][0]=0.0
        for i in range(N):
            for j,v in F[i].items():
                for k in range(LMAX+1):
                    if j+k>M: break
                    jj=j+k
                    if jj<lo(i+1) or jj>hi(i+1): continue
                    F[i+1][jj]=lse(F[i+1].get(jj,-1e18),v+lp(T[i],C[j:jj]))
        B=[dict() for _ in range(N+1)]
        for j in F[N]: B[N][j]=0.0
        for i in range(N-1,-1,-1):
            for j in F[i]:
                acc=-1e18
                for k in range(LMAX+1):
                    jj=j+k
                    if jj in B[i+1]: acc=lse(acc,lp(T[i],C[j:jj])+B[i+1][jj])
                B[i][j]=acc
        Z=-1e18
        for j,v in F[N].items(): Z=lse(Z,v)
        cnt=collections.defaultdict(lambda:collections.defaultdict(float))
        for i in range(N):
            for j,v in F[i].items():
                for k in range(LMAX+1):
                    jj=j+k
                    if jj in B[i+1]:
                        p=math.exp(v+lp(T[i],C[j:jj])+B[i+1][jj]-Z)
                        if p>1e-3: cnt[T[i]][C[j:jj]]+=p
        model={}
        for t,d in cnt.items():
            dd=dict(d); dd['_tot']=sum(d.values()); model[t]=dd
        print('iter',it,'logZ',round(Z,1),file=sys.stderr)
    # Viterbi
    V=[dict() for _ in range(N+1)]; V[0][0]=(0.0,None)
    for i in range(N):
        for j,(v,_) in V[i].items():
            for k in range(LMAX+1):
                jj=j+k
                if jj>M: break
                if jj<lo(i+1) or jj>hi(i+1): continue
                s=v+lp(T[i],C[j:jj])
                if jj not in V[i+1] or V[i+1][jj][0]<s: V[i+1][jj]=(s,j)
    j=max(V[N],key=lambda x:V[N][x][0]); path=[]
    for i in range(N,0,-1):
        pj=V[i][j][1]; path.append((T[i-1],C[pj:j])); j=pj
    return model,path[::-1]
if __name__=='__main__':
    clear=norm(''.join(l for l in open(sys.argv[1]) if not l.startswith('#')))
    T=toks(sys.argv[3:])
    iters,ratio=int(sys.argv[2].split(",")[0]),float(sys.argv[2].split(",")[1])
    pass
    print(len(T),'groupes',len(clear),'lettres',file=sys.stderr)
    model,path=run(T,clear,iters,ratio,150)
    json.dump({'path':path,'model':{t:{s:round(v,3) for s,v in d.items()} for t,d in model.items()}},open('align_out.json','w'),ensure_ascii=False,indent=0)
    print(' '.join(f'{t}={s or "∅"}' for t,s in path))
