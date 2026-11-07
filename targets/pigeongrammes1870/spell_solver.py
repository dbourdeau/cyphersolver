"""Spelled-run solver for the inspectors' alphabetical code: split a candidate string into k pieces so that each piece's alphabetical
position matches value/9999.  Validation on the known runs, then the unknown ones."""
import re,collections,bisect,sys,unicodedata,math
sys.stdout.reconfigure(encoding="utf8")
def strip(s): return "".join(c for c in unicodedata.normalize("NFD",s) if unicodedata.category(c)!="Mn")
def toks(t): return [re.sub(r"[^a-z]","",strip(x)) for x in re.findall(r"[\wéèêëàâîïôùûüçœ]+",t.lower().replace("'"," ").replace("’"," "))]
files=[(r"C:\Users\dbour\enquete\%s.txt"%f) for f in ("gouvernementdela01favr","gouvernementdela02favr","sc_0001326967_0000001317479","sc_0001326967_00000001739290","sc_0000928533_00000001739293")]
files.append(r"C:\Users\dbour\pigeon_src\bulletindelasoci0209soci.txt")
corp=[]
for f in files: corp+=[w for w in toks(open(f,encoding="utf8",errors="replace").read()) if len(w)>=1]
c=collections.Counter(corp)
V=sorted(w for w,n in c.items() if n>=3 and len(w)>=2); NV=len(V)
pos=lambda s: bisect.bisect_left(V,s)/NV
cands=[w for w,n in c.items() if 3<=len(w)<=16 and (n>=2)]
extra=["steenakers","steenackers","mercadier","ernest","pigeons","pigeon","ballons","ballon","traclet","nobecourt","cassiers","thomas","vanrosebeke","rampont","dagron","feillet","gambetta","favre","picard","keratry","cremieux","trochu","chassinat","segalas","lafollye","blay","lefort"]
cands=list(dict.fromkeys(extra+cands))
BIAS=0.015
def best_split(x,vals):
    n=len(x);k=len(vals)
    if k>n: return None
    INF=1e9
    dp=[[INF]*(n+1) for _ in range(k+1)]; dp[0][0]=0.0; bk={}
    for i in range(1,k+1):
        for j in range(i,n+1):
            for t in range(i-1,j):
                if dp[i-1][t]>=INF: continue
                e=abs(pos(x[t:j])-vals[i-1])
                if dp[i-1][t]+e<dp[i][j]: dp[i][j]=dp[i-1][t]+e; bk[(i,j)]=t
    if dp[k][n]>=INF: return None
    cuts=[];j=n
    for i in range(k,0,-1):
        t=bk[(i,j)]; cuts.append(x[t:j]); j=t
    return dp[k][n]/k,cuts[::-1]
def solve(run,top=6):
    vals=[int(g)/9999.0+BIAS for g in run]
    res=[]
    for x in cands:
        r=best_split(x,vals)
        if r: res.append((r[0],x,r[1]))
    res.sort()
    return res[:top],res
tests={
 "Steenackers run (6)":["8328","9214","0218","4906","3316","8328"],
 "Mercadier run (4)":["5504","1122","2514","3316"],
 "pigeons run (4)":["6816","4001","6129","8328"],
 "ballon run (3)":["0919","5121","6129"],
 "first-name run (2)":["6819","3412"],
}
print("vocabulary %d entries, candidate strings %d"%(NV,len(cands)))
for name,run in tests.items():
    top,allr=solve(run)
    ranks={x:i+1 for i,(e,x,_) in enumerate(allr)}
    print("\n%s  values %s"%(name," ".join(run)))
    for e,x,cuts in top: print("   err %.3f  %-14s %s"%(e,x,"|".join(cuts)))
    for probe in ("steenakers","steenackers","mercadier","pigeons","ballon","ballons","ernest"):
        if probe in ranks: print("   rank of %s: %d of %d (err %.3f)"%(probe,ranks[probe],len(allr),[e for e,x,_ in allr if x==probe][0]))

print("\n\n=========== UNKNOWN RUNS, candidates restricted to the pigeon-post article vocabulary ===========")
art=open(r"C:\Users\dbour\pigeon_src\bulletindelasoci0209soci.txt",encoding="utf8",errors="replace").read()
a0=art.find("LA POSTE PAR PIGEONS VOYAGEURS"); 
idx=[m.start() for m in re.finditer("POSTE PAR PIGEONS VOYAGEURS",art)]
seg=art[idx[0]-3000:idx[-1]+6000]
ac=collections.Counter(w for w in toks(seg) if 3<=len(w)<=16)
pool=[w for w,n in ac.items() if n>=1]
print("article vocabulary:",len(pool))
cands_save=cands
cands=list(dict.fromkeys(extra+pool))
unknown={
 "Nantes correspondent (2): 9802 6124":["9802","6124"],
 "Rennes correspondent (3): 1114 5911 0131":["1114","5911","0131"],
 "Rennes-type (4): 1114 5911 0131 0423":["1114","5911","0131","0423"],
 "second spelled name (3): 9113 8317 1504":["9113","8317","1504"],
 "after 'a Monsieur' (2): 6819 3412":["6819","3412"],
 "0101 8518 0706 4225 0803":["8518","0706","4225","0803"],
}
for name,run in unknown.items():
    top,allr=solve(run,top=10)
    print("\n%s"%name)
    for e,x,cuts in top: print("   err %.3f  %-16s %s"%(e,x,"|".join(cuts)))
# single groups: words near the position
print("\nsingle-group positions (common words within +-0.012):")
cw=[w for w,n in c.items() if n>=8 and len(w)>=3]
for g in ("4007","5511","5711","2215","5926","0603","0131","0423","1206"):
    p=int(g)/9999.0+BIAS
    near=sorted((abs(pos(w)-p),w) for w in cw if abs(pos(w)-p)<=0.012)[:14]
    print(" ",g,"%.3f"%p,[w for e,w in near])
