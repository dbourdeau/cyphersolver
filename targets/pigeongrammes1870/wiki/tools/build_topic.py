"""Build wiki/topic_counts.json: word counts of the topic corpus (pigeon post / telegraph administration) used as a topic prior by the engine.
Sources (each used if present): Dagron 1871 (Gutenberg 19588), Societe d'acclimatation 1872 article, Steenackers 1883 OCR (HathiTrust hvd.hn6bui, downloaded via Chrome)."""
import re,os,json,sys,collections,unicodedata,glob
sys.stdout.reconfigure(encoding="utf8")
def strip(s): return "".join(c for c in unicodedata.normalize("NFD",s) if unicodedata.category(c)!="Mn")
def norm(w): return re.sub(r"[^a-z]","",strip(w.lower()))
D=collections.Counter(); used=[]
def add(path,label,cut=None):
    if not os.path.exists(path): return
    t=open(path,encoding="utf8",errors="replace").read()
    if cut: t=cut(t)
    n=0
    for w in re.findall(r"[A-Za-zÀ-ÿ]{2,}",t):
        k=norm(w)
        if k: D[k]+=1; n+=1
    used.append((label,n))
add(r"C:\Users\dbour\pigeon_src\dagron.txt","Dagron 1871")
def art_cut(a):
    idx=[m.start() for m in re.finditer("POSTE PAR PIGEONS VOYAGEURS",a)]
    return a[idx[0]-3000:idx[-1]+6000]
add(r"C:\Users\dbour\pigeon_src\bulletindelasoci0209soci.txt","Societe d'acclimatation 1872 article",art_cut)
for cand in (r"C:\Users\dbour\pigeon_src\steenackers_full.txt",):
    add(cand,"Steenackers 1883 (HathiTrust OCR)")
json.dump(dict(counts=dict(D),sources=used),open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"topic_counts.json"),"w",encoding="utf8"),ensure_ascii=False)
print("topic corpus:",used,"distinct words",len(D),"tokens",sum(D.values()))
