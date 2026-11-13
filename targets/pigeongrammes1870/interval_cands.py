"""Inspectors' code as a paged alphabetical book: group PPLL = page PP (01-99), line LL (01-30), rank = (PP-1)*30+LL.
For each unknown group list French words that sort strictly between the nearest anchors below and above it, ranked by
closeness to the interpolated position and by frequency. Needs `pip install wordfreq` (word list only)."""
import re,sys,unicodedata,bisect,json,os,math
from wordfreq import top_n_list, word_frequency
H=os.path.dirname(os.path.abspath(__file__))
def strip(s): return "".join(c for c in unicodedata.normalize("NFD",s) if unicodedata.category(c)!="Mn")
N=int(os.environ.get("NV","12000"))
W={}
for w in top_n_list("fr",60000):
    k=strip(w.lower())
    if re.fullmatch("[a-z]+",k) and k not in W: W[k]=word_frequency(w,"fr")
V=sorted(sorted(W,key=W.get,reverse=True)[:N])
ANCH=json.load(open(os.path.join(H,"anchors_inspecteurs.json"),encoding="utf8"))
def rank(g): return (int(g[:2])-1)*30+int(g[2:])
A=sorted((rank(g),w) for g,w in ANCH.items() if not g.startswith("_"))
def cands(g,n=8):
    if g in ANCH: return "="+ANCH[g]
    r=rank(g); i=bisect.bisect_left(A,(r,""))
    lo=A[i-1] if i>0 else (0,"a"); hi=A[i] if i<len(A) else (2971,"zzzz")
    a=bisect.bisect_right(V,lo[1]); b=bisect.bisect_left(V,hi[1])
    pool=V[a:b]
    if not pool: return "(%s|%s) -"%(lo[1],hi[1])
    f=(r-lo[0])/max(1,hi[0]-lo[0]); 
    sc=[]
    for j,w in enumerate(pool):
        p=(j+0.5)/len(pool); sc.append((-((p-f)/0.25)**2+0.6*math.log10(W[w]),w))
    sc.sort(reverse=True)
    return "(%s|%s %d) "%(lo[1],hi[1],len(pool))+" ".join(w for _,w in sc[:n])
if __name__=="__main__":
    T=open(os.path.join(H,"inspecteurs_2nov_partial.txt"),encoding="utf8").read()
    if len(sys.argv)>1 and sys.argv[1]=="text":
        print(re.sub(r"\b\d{4}\b",lambda m:"["+ANCH[m.group(0)]+"]" if m.group(0) in ANCH else m.group(0),T))
    else:
        import collections
        c=collections.Counter(re.findall(r"\b\d{4}\b",T))
        for g in sorted(c): print(g,c[g],cands(g))
