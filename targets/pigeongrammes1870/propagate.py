"""Anchor propagation: accept (group, word) pairs whose every occurrence lines up near the expected plaintext position,
tighten the position map, repeat.  Output: anchors_chaudordy.json (group -> word, occurrences, p-value)."""
import re,json,collections,sys,unicodedata,math,bisect
import numpy as np
sys.stdout.reconfigure(encoding="utf8")
seg=open("chaudordy_18dec_plain.txt",encoding="utf8").read()
def strip(s): return "".join(c for c in unicodedata.normalize("NFD",s) if unicodedata.category(c)!="Mn")
raw=[x.replace("’","'") for x in re.findall(r"[\wéèêëàâîïôùûüçœ'’]+",seg.lower())]
W=[re.sub(r"[^a-z0-9]","",strip(x)) for x in raw]; raw=[r for r,w in zip(raw,W) if w]; W=[w for w in W if w]
C=json.load(open("chaudordy_nums.json")); N,T=len(W),len(C)
pg=collections.defaultdict(list); pw=collections.defaultdict(list)
for i,g in enumerate(C): pg[g].append(i)
for j,w in enumerate(W): pw[w].append(j)
def lis(points):
    pts=sorted(set(points)); tails=[];idx=[];prev=[-1]*len(pts)
    for q,(c,j) in enumerate(pts):
        pos=bisect.bisect_left(tails,j)
        if pos==len(tails): tails.append(j); idx.append(q)
        else: tails[pos]=j; idx[pos]=q
        prev[q]=idx[pos-1] if pos>0 else -1
    q=idx[-1]; ch=[]
    while q!=-1: ch.append(pts[q]); q=prev[q]
    return ch[::-1]
def binom_tail(n,k,p):
    return sum(math.comb(n,x)*p**x*(1-p)**(n-x) for x in range(k,n+1))
ratio=T/N
accepted={}      # group -> (word, hits, p)
points=[]
ANCH0={1792:"conference",1980:"ballon",944:"question",723:"premiere",977:"sauf",998:"partir",835:"cependant",2232:"bruxelles",862:"comme",182:"negociations"}
def add_points(g,w,delta):
    k=0
    for c in pg[g]:
        # nearest occurrence of w to expected pos
        pass
for g,w in ANCH0.items():
    k=0
    for c in pg[g]:
        while k<len(pw[w]) and ratio*pw[w][k]<c-90: k+=1
        if k<len(pw[w]) and abs(ratio*pw[w][k]-c)<90: points.append((c,pw[w][k])); k+=1
chain=lis(points)
for rnd in range(8):
    ci=[0]+[c for c,j in chain]+[T]; cj=[0]+[j for c,j in chain]+[N]
    e=np.interp(np.arange(T),ci,cj)
    delta=14 if rnd<3 else 10
    new={}
    for g,occ in pg.items():
        n=len(occ)
        if n<2 or g in accepted: continue
        cand=[]
        for w,wps in pw.items():
            if len(w)<3 and not w.isdigit(): continue
            hits=0; pts=[]
            for c in occ:
                near=[j for j in wps if abs(j-e[c])<=delta]
                if near: hits+=1; pts.append((c,min(near,key=lambda j:abs(j-e[c]))))
            if hits<max(2,n-(1 if n>=5 else 0)): continue
            p=min(1.0,len(wps)*(2*delta+1)/N)
            pv=binom_tail(n,hits,p)
            if pv<2e-5: cand.append((pv,w,hits,pts))
        if cand:
            cand.sort(key=lambda x:x[0]); pv,w,hits,pts=cand[0]
            if len(cand)>1 and cand[1][0]<pv*30: continue      # ambiguous
            new[g]=(w,hits,pv,pts)
    if not new: break
    for g,(w,hits,pv,pts) in new.items(): accepted[g]=(w,hits,pv); points+=pts
    chain=lis(points)
    print("round",rnd,"delta",delta,"new pairs",len(new),"total",len(accepted),"chain",len(chain),flush=True)
json.dump({str(g):{"word":w,"hits":h,"p":pv} for g,(w,h,pv) in accepted.items()},open("anchors_chaudordy.json","w"),ensure_ascii=False)
json.dump(chain,open("anchor_chain.json","w"))
print(sorted(((g,w,h) for g,(w,h,pv) in accepted.items()),key=lambda x:x[1]))
