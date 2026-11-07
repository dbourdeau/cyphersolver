"""Windowed hard-EM alignment, elision-aware.  Tokens: elisions (l' d' qu' j' ...) are separate tokens; a unit is one token,
or an elision token + the next word coded together.  A group has ONE meaning (consistency cost); words are coded by 1 group or
~syllable-count groups.  usage: align_slide2.py [seed_groups] [window] [commit] [null_cost]"""
import re,json,sys,collections,unicodedata,math,bisect
import numpy as np
sys.stdout.reconfigure(encoding="utf8")
SEED=int(sys.argv[1]) if len(sys.argv)>1 else 100
G=int(sys.argv[2]) if len(sys.argv)>2 else 70
COMMIT=int(sys.argv[3]) if len(sys.argv)>3 else 40
NULLG=float(sys.argv[4]) if len(sys.argv)>4 else 3.0
SKIPW=3.2; KMAX=6; INF=1e18
def strip(s): return "".join(c for c in unicodedata.normalize("NFD",s) if unicodedata.category(c)!="Mn")
TOK=re.compile(r"((?:jusqu|lorsqu|puisqu|qu|[ldjnsmtc])['’])|([\wéèêëàâîïôùûüçœ]+)")
def tokenize(text):
    text=text.lower().replace("aujourd'hui","aujourdhui").replace("aujourd’hui","aujourdhui")
    out=[]
    for m in TOK.finditer(text):
        el=bool(m.group(1)); s=re.sub(r"[^a-z0-9]","",strip(m.group(0)))
        if s: out.append((s,el,m.group(0)))
    return out
seg=open("chaudordy_18dec_plain.txt",encoding="utf8").read()
toks=tokenize(seg); W=[t[0] for t in toks]; ELI=[t[1] for t in toks]; RAW=[t[2] for t in toks]; N=len(W)
C=json.load(open("chaudordy_nums.json")); T=len(C)
def syl(w):
    if w.isdigit(): return [w]
    cl=list(re.finditer(r"[aeiouy]+",w))
    if len(cl)<=1: return [w]
    cuts=[]
    for a,b in zip(cl,cl[1:]):
        gap=b.start()-a.end(); cuts.append(a.end()+(1 if gap>=2 else 0) if gap>=1 else b.start())
    if w.endswith("e") and cl[-1].start()==len(w)-1 and len(cl)>1: cuts=cuts[:-1]
    parts=[];p=0
    for c in cuts: parts.append(w[p:c]); p=c
    parts.append(w[p:]); return [x for x in parts if x]
SYC={}
def sylc(s):
    if s not in SYC: SYC[s]=syl(s)
    return SYC[s]
def chunks(s,k):
    if k==1: return [s]
    sy=sylc(s)
    if len(sy)==k: return sy
    if len(sy)>k:
        per=len(sy)/k; return ["".join(sy[int(round(q*per)):int(round((q+1)*per))]) for q in range(k)]
    L=len(s); return [s[int(round(q*L/k)):int(round((q+1)*L/k))] for q in range(k)]
meaning=collections.defaultdict(collections.Counter); unitlex=collections.defaultdict(collections.Counter)
ANCH={1792:"conference",1980:"ballon",944:"question",723:"premiere",977:"sauf",998:"partir",835:"cependant",2232:"bruxelles",862:"comme",182:"negociations"}
for g,w in ANCH.items(): meaning[g][w]+=6
def gcost(g,ch):
    m=meaning[g]; t=sum(m.values())
    return 0.0 if t==0 else -math.log((m[ch]+0.05)/(t+0.15))*0.9
def ucost(s,tup):
    k=len(tup); sy=len(sylc(s)); c=0.0
    kn=unitlex[s][tup]
    if kn: c-=min(kn,3)*0.6
    if k==1: c+=1.8
    elif k==sy: c+=1.2
    else: c+=2.6+0.9*abs(k-sy)
    for g,x in zip(tup,chunks(s,k)): c+=gcost(g,x)
    return c
def unit_str(j,span): return W[j] if span==1 else W[j]+W[j+1]
# position prior from anchors
ratio=T/N
def window_dp(i0,j0,Gw,Jmax,slope):
    best={(i0,j0):0.0}; back={}; iend=min(T,i0+Gw)
    for i in range(i0,iend+1):
        for j in range(j0,min(N,Jmax)+1):
            cur=best.get((i,j))
            if cur is None: continue
            if i<iend:
                v=cur+NULLG; key=(i+1,j)
                if v<best.get(key,INF): best[key]=v; back[key]=(i,j,"n",(),1)
            if j<N and j<Jmax:
                v=cur+SKIPW; key=(i,j+1)
                if v<best.get(key,INF): best[key]=v; back[key]=(i,j,"s",(),1)
                spans=(1,2) if (ELI[j] and j+1<N) else (1,)
                for span in spans:
                    s=unit_str(j,span)
                    for k in range(1,KMAX+1):
                        if i+k>iend: break
                        tup=tuple(C[i:i+k]); v=cur+ucost(s,tup)+(0.0 if span==1 else 0.3); key=(i+k,j+span)
                        if v<best.get(key,INF): best[key]=v; back[key]=(i,j,"w",tup,span)
    ends=[(best[(iend,j)]+0.03*(j-(j0+(iend-i0)*slope))**2,j) for j in range(j0,min(N,Jmax)+1) if (iend,j) in best]
    sc,je=min(ends); key=(iend,je); path=[]
    while key!=(i0,j0):
        i,j,t,tup,span=back[key]; path.append((i,j,t,tup,span)); key=(i,j)
    return path[::-1]
def commit(path):
    for i,j,t,tup,span in path:
        if t=="w":
            s=unit_str(j,span); unitlex[s][tup]+=1
            for g,x in zip(tup,chunks(s,len(tup))): meaning[g][x]+=1
# seed: first SEED groups of the word-level HMM alignment, mapped to the new tokens
hm=json.load(open("align_hmm2_out.json"))
old=[re.sub(r"[^a-z0-9]","",strip(x.replace("’","'"))) for x in re.findall(r"[\wéèêëàâîïôùûüçœ'’]+",seg.lower())]
old=[x for x in old if x]
# map old index -> new token span by walking both lists
mp={}; jn=0
for jo,w in enumerate(old):
    acc=""; start=jn
    while jn<N and len(acc)<len(w): acc+=W[jn]; jn+=1
    mp[jo]=(start,jn-start)
grp=[]
for r in hm[:SEED]:
    if r["w"] is None: continue
    if grp and grp[-1][0]==r["j"]: grp[-1][1].append(r["g"])
    else: grp.append([r["j"],[r["g"]]])
for jo,gs in grp:
    st,n=mp[jo]
    s="".join(W[st:st+n]); unitlex[s][tuple(gs)]+=1
    for g,x in zip(gs,chunks(s,len(gs))): meaning[g][x]+=1
i0=SEED; jo,_=grp[-1]; st,n=mp[jo]; j0=st+n
slope=0.9; allp=[]
while i0<T:
    path=window_dp(i0,j0,G,min(N,j0+int(G*1.2)+10),slope)
    cut=[];n=0
    for p in path:
        cut.append(p); n+=len(p[3]) if p[2]=="w" else (1 if p[2]=="n" else 0)
        if n>=COMMIT and p[2]=="w": break
    if i0+G>=T: cut=path
    commit(cut); allp+=cut
    l=cut[-1]; i0=l[0]+(len(l[3]) if l[2]=="w" else (1 if l[2]=="n" else 0))
    j0=l[1]+(l[4] if l[2]=="w" else (1 if l[2]=="s" else 0))
cons=tot=0
for g,m in meaning.items():
    n=sum(m.values())
    if n>=2: tot+=1; cons+=m.most_common(1)[0][1]/n>=0.8
nul=collections.Counter(p[0]//50 for p in allp if p[2]=="n")
print("tokens",N,"consistent groups(>=2 uses): %d/%d"%(cons,tot),"final token",j0,"of",N,"nulls",sum(nul.values()),"skipped",sum(1 for p in allp if p[2]=="s"))
print("nulls per 50 groups:",[nul[b] for b in range(T//50+1)])
out=[{"i":p[0],"j":p[1],"t":p[2],"span":p[4],"groups":list(p[3]),"unit":unit_str(p[1],p[4]) if p[2]!="n" and p[1]<N else None} for p in allp]
json.dump(out,open("align_slide2_out.json","w"),ensure_ascii=False)
json.dump({str(g):dict(m.most_common(3)) for g,m in meaning.items() if m},open("codebook_chaudordy.json","w"),ensure_ascii=False)
def show(a,b): print(" | ".join(("%s=%s"%("+".join(map(str,p["groups"])),p["unit"]) if p["t"]=="w" else ("NULL %s"%C[p["i"]] if p["t"]=="n" else "skip(%s)"%W[p["j"]])) for p in out if a<=p["i"]<b))
show(100,420)
