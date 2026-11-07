"""Benchmark loop for the alphabetical inspectors' code (Steenackers to Mercadier, Tours 2 Nov 1870).
Benchmark: 10 independently supported items; the solver sees only the group values and the clear neighbours and must rank the gold string
among ~29,000 candidates. Score = mean reciprocal rank (MRR); also top-10 count.  Hypotheses are fixed a priori (no tuning on the items) and are
kept only if MRR rises by >= EPS; stop after 3 consecutive rejections.
usage: python bench_loop.py [only_baseline]"""
import re,collections,bisect,math,sys,unicodedata,functools,json
sys.stdout.reconfigure(encoding="utf8")
EPS=0.01; PATIENCE=3
def strip(s): return "".join(c for c in unicodedata.normalize("NFD",s) if unicodedata.category(c)!="Mn")
def toks(t): return [re.sub(r"[^a-z]","",strip(x)) for x in re.findall(r"[\wéèêëàâîïôùûüçœ]+",t.lower().replace("'"," ").replace("’"," "))]
files=[(r"C:\Users\dbour\enquete\%s.txt"%f) for f in ("gouvernementdela01favr","gouvernementdela02favr","sc_0001326967_0000001317479","sc_0001326967_00000001739290","sc_0000928533_00000001739293")]+[r"C:\Users\dbour\pigeon_src\bulletindelasoci0209soci.txt"]
corp=[]; capc=collections.Counter(); lowc=collections.Counter()
for f in files:
    t=open(f,encoding="utf8",errors="replace").read()
    corp+=[w for w in toks(t) if w]
    for m in re.finditer(r"[A-Za-zÀ-ÿ]{2,}",t):
        w=m.group(0); s=re.sub(r"[^a-z]","",strip(w.lower()))
        if not s: continue
        pre=t[max(0,m.start()-3):m.start()]
        if w[0].isupper() and not w.isupper() and not re.search(r"[.!?»:]\s*$|\n\s*$",pre): capc[s]+=1
        elif w[0].islower(): lowc[s]+=1
uni=collections.Counter(corp); bi=collections.Counter(zip(corp,corp[1:])); NT=len(corp); VOC=len(uni)
V=sorted(w for w,n in uni.items() if n>=3 and len(w)>=2); NV=len(V)
# fixed historical prior list (known from the printed heading and the siege): extra candidate strings, independent of the cipher
EXTRA="steenackers mercadier trochu rampont dagron gambetta favre picard cremieux ducrot vinoy clement thomas schmitz tamisier chanzy bourbaki faidherbe".split()
CANDS=list(dict.fromkeys(EXTRA+[w for w,n in uni.items() if 2<=len(w)<=14 and n>=2]))
@functools.lru_cache(maxsize=None)
def rawpos(s): return bisect.bisect_left(V,s)/NV
def lp_bi(a,b):
    ca=uni[a]; p1=(uni[b]+0.5)/(NT+0.5*VOC); p2=bi[(a,b)]/ca if ca else 0
    return math.log(0.72*p2+0.28*p1)
def lp_uni(w): return math.log((uni[w]+0.5)/(NT+0.5*VOC))
# gold items: (name, groups, gold strings, left clear word, right clear word)
ITEMS=[
 ("general",["4007"],{"general"},"au",None),
 ("est",["3407"],{"est"},None,"bien"),
 ("bonne",["1026"],{"bonne"},"en",None),
 ("sante",["8416"],{"sante"},None,"frere"),
 ("portante",["7027","0312"],{"portante"},"bien","a"),
 ("trochu",["9113","8317","1504"],{"trochu"},None,None),
 ("mercadier",["5504","1122","2514","3316"],{"mercadier"},None,None),
 ("pigeons",["6816","4001","6129","8328"],{"pigeons"},"par","dabord"),
 ("steenackers",["8328","9214","0218","4906","3316","8328"],{"steenackers","steenakers"},"inspecteurs","a"),
 ("ballon",["0919","5121","6129"],{"ballon","ballons"},None,None),
]
CFG=dict(bias=0.015,sigma=0.02,calib=None,unigram=False,bigram=False,plen=False,names=False,syl=False,k1_common=False)
def calib_map():
    """isotonic map position-in-my-word-list -> fraction of R1's numbering (R1 is a real alphabetical lexicon, independent of the items)"""
    import openpyxl
    wb=openpyxl.load_workbook(r"C:\Users\dbour\pigeon_dl\data\Repertoire1.xlsx",read_only=True,data_only=True)
    pts=[]
    for r in wb.worksheets[0].iter_rows(values_only=True):
        if r[0] is None or len(r)<2 or not r[1]: continue
        k=str(r[0]).strip()
        if re.fullmatch(r"\d{4}",k) and not str(r[1]).startswith("-"):
            w=re.sub(r"[^a-z]","",strip(str(r[1]).lower()))
            if len(w)>=2: pts.append((rawpos(w),(int(k)-131)/(5893-131)))
    pts.sort()
    xs=[p for p,_ in pts]; ys=[q for _,q in pts]
    # pool adjacent violators
    blocks=[[y,1] for y in ys]; out=[]
    for b in blocks:
        out.append(b)
        while len(out)>1 and out[-2][0]/out[-2][1]>out[-1][0]/out[-1][1]:
            b2=out.pop(); out[-1][0]+=b2[0]; out[-1][1]+=b2[1]
    iso=[]
    for s,n in out: iso+=[s/n]*n
    return xs,iso
_cal=None
def pos(s):
    p=rawpos(s)
    if CFG["calib"]:
        global _cal
        if _cal is None: _cal=calib_map()
        xs,iso=_cal
        i=bisect.bisect_left(xs,p)
        if i<=0: return iso[0]
        if i>=len(xs): return iso[-1]
        x0,x1=xs[i-1],xs[i]; y0,y1=iso[i-1],iso[i]
        return y0 if x1==x0 else y0+(y1-y0)*(p-x0)/(x1-x0)
    return p
def target(g):
    return int(g)/9999.0 + (0.0 if CFG["calib"] else CFG["bias"])
def syl(w):
    cl=list(re.finditer(r"[aeiouy]+",w)); n=len(cl)
    if w.endswith("e") and n>1 and cl[-1].start()==len(w)-1: n-=1
    return max(n,1)
def split_cost(x,groups):
    n=len(x);k=len(groups); INF=1e9
    if k>n: return None
    tg=[target(g) for g in groups]; sig=CFG["sigma"]
    dp=[[INF]*(n+1) for _ in range(k+1)]; dp[0][0]=0.0
    for i in range(1,k+1):
        for j in range(i,n+1):
            for t in range(max(i-1,j-10),j):
                if dp[i-1][t]>=INF: continue
                e=(pos(x[t:j])-tg[i-1])/sig
                c=0.5*e*e
                if CFG["plen"] and k>1 and j-t>4: c+=0.6*(j-t-4)
                if dp[i-1][t]+c<dp[i][j]: dp[i][j]=dp[i-1][t]+c
    return None if dp[k][n]>=INF else dp[k][n]
def score(x,groups,left,right):
    c=split_cost(x,groups)
    if c is None: return None
    s=-c
    if CFG["unigram"]: s+=lp_uni(x)
    if CFG["bigram"]:
        if left: s+=lp_bi(left,x)
        if right: s+=lp_bi(x,right)
    if CFG["names"] and len(groups)>=3:
        cp=capc[x]; lo=lowc[x]
        if cp>=2 and cp>=2*lo: s+=2.0
    if CFG["syl"]:
        s-=0.8*abs(syl(x)-len(groups))
    return s
def evaluate(verbose=False):
    ranks=[];rows=[]
    for name,groups,gold,left,right in ITEMS:
        sc=[]
        for x in CANDS:
            if len(groups)==1 and len(x)<2: continue
            s=score(x,groups,left,right)
            if s is not None: sc.append((s,x))
        sc.sort(reverse=True)
        r=next((i+1 for i,(s,x) in enumerate(sc) if x in gold),None) or len(sc)+1
        ranks.append(r); rows.append((name,r,len(sc),[x for s,x in sc[:3]]))
    mrr=sum(1.0/r for r in ranks)/len(ranks); top10=sum(1 for r in ranks if r<=10)
    if verbose:
        for name,r,n,top in rows: print("    %-12s rank %6d of %d   top3 %s"%(name,r,n,top))
    return mrr,top10,ranks
HYPS=[
 ("H1 frequency prior: common words are more likely (add log unigram probability)",dict(unigram=True)),
 ("H2 context: bigram LM with the clear neighbouring words",dict(bigram=True)),
 ("H3 calibration: replace the +0.015 bias by an isotonic map fitted on R1's own numbering",dict(calib=True)),
 ("H4 spelled pieces are short: penalise pieces longer than 4 letters in runs",dict(plen=True)),
 ("H5 runs of 3 or more groups are proper names: bonus for capitalised words",dict(names=True)),
 ("H6 one group per syllable: penalise syllable-count mismatch",dict(syl=True)),
]
if __name__=="__main__":
    log=[]
    print("candidates %d, vocabulary %d"%(len(CANDS),NV))
    mrr,top10,ranks=evaluate(True)
    best=mrr; print("LOOP 0 baseline (position only, sigma 0.02, bias +0.015): MRR %.4f  top-10 %d/10  ranks %s"%(mrr,top10,ranks))
    log.append(("baseline",mrr,top10,ranks,"kept"))
    if len(sys.argv)>1: sys.exit()
    noprog=0; loop=0
    for name,change in HYPS:
        loop+=1
        old={k:CFG[k] for k in change}
        CFG.update(change); _cal=None if "calib" in change else _cal
        m,t10,rk=evaluate(True)
        gain=m-best
        verdict="KEPT" if gain>=EPS else "rejected"
        print("LOOP %d  %s\n    MRR %.4f (%+.4f)  top-10 %d/10  ranks %s  -> %s"%(loop,name,m,gain,t10,rk,verdict))
        log.append((name,m,t10,rk,verdict))
        if gain>=EPS: best=m; noprog=0
        else:
            CFG.update(old); noprog+=1
            if "calib" in change: _cal=None
        if noprog>=PATIENCE: print("STOP: %d loops without progress"%PATIENCE); break
    print("\nFINAL benchmark MRR %.4f ; config %s"%(best,{k:v for k,v in CFG.items() if v}))
    json.dump(log,open("bench_loop_log.json","w"),ensure_ascii=False)
