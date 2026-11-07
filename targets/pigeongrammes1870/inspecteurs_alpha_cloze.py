"""Alphabetical-position-constrained fill-in of the inspectors' telegram (Steenackers to Mercadier, 2 Nov 1870).
Group value v/9999 ~ alphabetical position of its entry (calibrated: mean error 0.014 on 13 syllable anchors).
Candidates for each whole-word group: common words whose alphabetical position is within W of v/9999; clear words fixed; bigram LM; one word per group."""
import re,collections,bisect,math,random,sys,unicodedata
sys.stdout.reconfigure(encoding="utf8")
W_WIN=float(sys.argv[1]) if len(sys.argv)>1 else 0.03
def strip(s): return "".join(c for c in unicodedata.normalize("NFD",s) if unicodedata.category(c)!="Mn")
def toks(t): return [re.sub(r"[^a-z0-9]","",strip(x)) for x in re.findall(r"[\wéèêëàâîïôùûüçœ]+",t.lower().replace("'"," ").replace("’"," "))]
corp=[]
for f in ("gouvernementdela01favr","gouvernementdela02favr","sc_0001326967_0000001317479","sc_0001326967_00000001739290","sc_0000928533_00000001739293"):
    corp+=[w for w in toks(open(r"C:\Users\dbour\enquete\%s.txt"%f,encoding="utf8",errors="replace").read()) if w and not w.isdigit()]
uni=collections.Counter(corp); bi=collections.Counter(zip(corp,corp[1:])); NT=len(corp); VOC=len(uni)
V=sorted(w for w,n in uni.items() if n>=3 and len(w)>=2); NV=len(V)
pos=lambda w: bisect.bisect_left(V,w)/NV
raw=open("inspecteurs_2nov_partial.txt",encoding="utf8").read().replace("’","'")
seq=[]
for w in raw.replace("'"," ").split():
    if re.fullmatch(r"\d{4}",w): seq.append(("G",w))
    else:
        ww=re.sub(r"[^a-z0-9]","",strip(w.lower()))
        if ww: seq.append(("W",ww))
BEAC={"0101","0201","0301","0102","0202","0302","0103","0203","0303","0109","0113","0130","0131","0136","0137","0138"}
groups=sorted({w for t,w in seq if t=="G" and w not in BEAC})
common=[w for w,n in uni.items() if n>=6 and len(w)>=2]
cand={}
for g in groups:
    p=int(g)/9999.0
    c=[w for w in common if abs(pos(w)-p)<=W_WIN]
    cand[g]=c if c else [w for w in common if abs(pos(w)-p)<=2*W_WIN]
print("candidate list sizes: median %d, max %d"%(sorted(len(v) for v in cand.values())[len(cand)//2],max(len(v) for v in cand.values())))
lam=0.72
def lp(a,b):
    ca=uni[a]; p1=(uni[b]+0.5)/(NT+0.5*VOC); p2=bi[(a,b)]/ca if ca else 0
    return math.log(lam*p2+(1-lam)*p1)
posn=collections.defaultdict(list)
for i,(t,w) in enumerate(seq):
    if t=="G" and w not in BEAC: posn[w].append(i)
def tok(i,m):
    t,w=seq[i]
    if t=="W": return w
    return "|" if w in BEAC else m[w]
ALPHA=0.8
def local(m,g,val):
    s=0.0
    for i in posn[g]:
        if i>0: s+=lp(tok(i-1,m),val)
        if i+1<len(seq): s+=lp(val,tok(i+1,m))
    s-=ALPHA*len(posn[g])*((pos(val)-int(g)/9999.0)/0.015)**2*0.1
    return s
random.seed(11)
m={g:random.choice(cand[g]) for g in groups}
for sw in range(8):
    ch=0
    for g in sorted(groups,key=lambda g:-len(posn[g])):
        cur=m[g]; best=cur; bs=local(m,g,cur)
        for c in cand[g]:
            s=local(m,g,c)
            if s>bs+1e-9: bs=s; best=c
        if best!=cur: m[g]=best; ch+=1
    if ch==0: break
print("sweeps",sw+1)
out=[]
for t,w in seq: out.append(w if t=="W" else ("|" if w in BEAC else "[%s=%s]"%(w,m[w])))
open("inspecteurs_alpha_cloze_out.txt","w",encoding="utf8").write(" ".join(out))
print("most frequent whole-word groups:",[(g,len(posn[g]),m[g],"%.3f/%.3f"%(pos(m[g]),int(g)/9999)) for g in sorted(groups,key=lambda g:-len(posn[g]))[:16]])
print()
print(" ".join(out[:330]))
