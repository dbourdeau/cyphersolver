"""HMM alignment with null groups.  States: W_j (word j emits a group) and Z_j (a null group inserted after word j).
Usage: align_hmm2.py [sigma] [iters] [cipher.json] [plain.txt] [out.json]"""
import re,json,sys,collections,numpy as np
sys.stdout.reconfigure(encoding="utf8")
SIG=float(sys.argv[1]) if len(sys.argv)>1 else 120.0
ITER=int(sys.argv[2]) if len(sys.argv)>2 else 30
cf=sys.argv[3] if len(sys.argv)>3 else "chaudordy_nums.json"
pf=sys.argv[4] if len(sys.argv)>4 else "chaudordy_18dec_plain.txt"
of=sys.argv[5] if len(sys.argv)>5 else "align_hmm2_out.json"
seg=open(pf,encoding="utf8").read()
W=[x.replace("’","'") for x in re.findall(r"[\wéèêëàâîïôùûüçœ'’]+",seg.lower())]
C=json.load(open(cf))
N,T=len(W),len(C)
wt=sorted(set(W)); wid={w:i for i,w in enumerate(wt)}; W_id=np.array([wid[w] for w in W])
gt=sorted(set(C)); gid={g:i for i,g in enumerate(gt)}; C_id=np.array([gid[g] for g in C])
nW,nG=len(wt),len(gt)
J=np.arange(N)
ANCH=[(1792,"conférence"),(1980,"ballon"),(944,"question"),(723,"première"),(977,"sauf"),(998,"partir"),(835,"cependant"),(2232,"bruxelles"),(862,"comme"),(740,"l'angleterre"),(182,"négociations"),(863,"sommes")]
pts=[]
ratio=T/N
for g,w in ANCH:
    cp=[i for i,x in enumerate(C) if x==g]; wp=[j for j,x in enumerate(W) if x==w]
    k=0
    for c in cp:
        while k<len(wp) and ratio*wp[k]<c-90: k+=1
        if k<len(wp) and abs(ratio*wp[k]-c)<90: pts.append((c,wp[k])); k+=1
pts=sorted(set(pts))
# keep a monotone chain (longest increasing in j)
import bisect
best=[];tails=[];idx=[]
prev=[-1]*len(pts)
for n,(c,j) in enumerate(pts):
    pos=bisect.bisect_left(tails,j)
    if pos==len(tails): tails.append(j); idx.append(n)
    else: tails[pos]=j; idx[pos]=n
    prev[n]=idx[pos-1] if pos>0 else -1
n=idx[-1]; chain=[]
while n!=-1: chain.append(pts[n]); n=prev[n]
chain=chain[::-1]
print("anchor points",len(pts),"chain",len(chain),file=sys.stderr)
ci=[0]+[c for c,j in chain]+[T-1]; cj=[0]+[j for c,j in chain]+[N-1]
meanv=np.interp(np.arange(T),ci,cj)
prior=np.array([np.exp(-0.5*((J-meanv[i])/SIG)**2) for i in range(T)])+1e-9
K=np.array([0.03,0.80,0.10,0.04,0.02,0.01]); K/=K.sum(); nK=len(K)   # d=0 (syllable),1,2..
pz=0.10; pzz=0.10     # W->Z, Z->Z
E=np.full((nG,nW),1.0/nG); Pn=np.full(nG,1.0/nG)
for g,w in ANCH:
    if g in gid and w in wid: E[gid[g],wid[w]]=5.0
def shift(a,d):
    o=np.zeros_like(a)
    if d==0: return a.copy()
    o[d:]=a[:-d]; return o
def run(E,Pn,K,pz,pzz):
    ew=np.empty((T,N)); en=np.empty(T)
    for i in range(T):
        ew[i]=E[C_id[i]][W_id]*prior[i]; en[i]=Pn[C_id[i]]
    # forward. aW[i,j]: prob in W_j having emitted group i ; aZ[i,j]: in Z_j
    aW=np.zeros((T,N)); aZ=np.zeros((T,N)); sc=np.zeros(T)
    w0=ew[0]*(J<8)+1e-30; z0=np.zeros(N); z0[0]=en[0]*0.3
    s=w0.sum()+z0.sum(); aW[0]=w0/s; aZ[0]=z0/s; sc[0]=s
    for i in range(1,T):
        fromW=np.zeros(N)                     # mass to W_{j} from W / Z
        for d in range(nK): fromW+=K[d]*(1-pz)*shift(aW[i-1],d)
        for d in range(1,nK): fromW+=K[d]*shift(aZ[i-1],d)*(1-pzz) if d>=1 else 0
        toZ=pz*aW[i-1]+pzz*aZ[i-1]
        nW_=fromW*ew[i]; nZ_=toZ*en[i]
        s=nW_.sum()+nZ_.sum(); aW[i]=nW_/s; aZ[i]=nZ_/s; sc[i]=s
    bW=np.zeros((T,N)); bZ=np.zeros((T,N)); bW[-1]=1; bZ[-1]=1
    for i in range(T-2,-1,-1):
        tw=ew[i+1]*bW[i+1]; tz=en[i+1]*bZ[i+1]
        nb=np.zeros(N); nz=np.zeros(N)
        for d in range(nK):
            nb+=K[d]*(1-pz)*np.concatenate([tw[d:],np.zeros(d)])
        nb+=pz*tz
        for d in range(1,nK):
            nz+=K[d]*(1-pzz)*np.concatenate([tw[d:],np.zeros(d)])
        nz+=pzz*tz
        s=nb.sum()+nz.sum(); bW[i]=nb/s; bZ[i]=nz/s
    gW=aW*bW; gZ=aZ*bZ; tot=gW.sum(1)+gZ.sum(1)
    gW/=tot[:,None]; gZ/=tot[:,None]
    return gW,gZ,np.log(sc).sum(),aW,aZ,bW,bZ,ew,en
for it in range(ITER):
    gW,gZ,ll,aW,aZ,bW,bZ,ew,en=run(E,Pn,K,pz,pzz)
    cnt=np.full((nG,nW),1e-4); cn=np.full(nG,1e-4)
    for i in range(T):
        np.add.at(cnt[C_id[i]],W_id,gW[i]); cn[C_id[i]]+=gZ[i].sum()
    E=cnt/cnt.sum(0,keepdims=True); Pn=cn/cn.sum()
    pnull=gZ.sum()/T
    # re-estimate jump kernel & null probs (approx from posteriors)
    pz=min(0.4,max(0.02,pnull)); pzz=min(0.5,max(0.02,pnull*0.9))
    # jump kernel from expected word-index differences between consecutive W-emitted groups (approximate via argmax)
    if it%5==0 or it==ITER-1: print("iter",it,"ll %.1f"%ll,"expected null groups %.0f"%(gZ.sum()),flush=True)
best=gW.argmax(1); isnull=gZ.sum(1)>gW.sum(1)
out=[{"i":i,"g":C[i],"w":(None if isnull[i] else W[best[i]]),"j":(None if isnull[i] else int(best[i])),"pn":round(float(gZ[i].sum()),3)} for i in range(T)]
json.dump(out,open(of,"w"),ensure_ascii=False)
print("null groups",int(isnull.sum()))
nl=collections.Counter(C[i] for i in range(T) if isnull[i]); print("top nulls",nl.most_common(15))
lex=collections.defaultdict(collections.Counter)
for r in out:
    if r["w"]: lex[r["g"]][r["w"]]+=1
rep=[(g,c) for g,c in lex.items() if sum(c.values())>=2]
cons=[g for g,c in rep if c.most_common(1)[0][1]/sum(c.values())>=0.99]
print("groups>=2 (non-null):",len(rep),"consistent:",len(cons))
print(" ".join("%s=%s"%(o["g"],o["w"] or "∅") for o in out[:140]))
print(" ".join("%s=%s"%(o["g"],o["w"] or "∅") for o in out[1000:1100]))
