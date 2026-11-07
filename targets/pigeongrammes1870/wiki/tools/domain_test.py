"""Does a topic prior improve the benchmark? Run from the target folder.
Topic corpus: pigeon-post texts held locally (Dagron 1871, Gutenberg 19588; Societe d'acclimatation 1872 article pp. 624-664). NOT the Steenackers text (wiki C039).
Prior = log( lam*P_topic + (1-lam)*P_general ), lam fixed in advance. Benchmark and config as in bench_loop (position + prior + bigram), MRR over the 10 supported items."""
import sys,os,json,math,re,collections
sys.path.insert(0,os.getcwd())
import bench_loop as B
sys.stdout.reconfigure(encoding="utf8")
def norm(w): return re.sub(r"[^a-z]","",B.strip(w.lower()))
D=collections.Counter()
t=open(r"C:\Users\dbour\pigeon_src\dagron.txt",encoding="utf8",errors="replace").read()
for w in re.findall(r"[A-Za-zÀ-ÿ]{2,}",t): D[norm(w)]+=1
art=open(r"C:\Users\dbour\pigeon_src\bulletindelasoci0209soci.txt",encoding="utf8",errors="replace").read()
idx=[m.start() for m in re.finditer("POSTE PAR PIGEONS VOYAGEURS",art)]
for w in re.findall(r"[A-Za-zÀ-ÿ]{2,}",art[idx[0]-3000:idx[-1]+6000]): D[norm(w)]+=1
D={k:v for k,v in D.items() if k}
ND=sum(D.values()); VD=len(D)
print("topic words %d, tokens %d; counts: pigeons %d ballon(s) %d bataillon %d depeche(s) %d sante %d bonne %d portante %d"%(VD,ND,D.get("pigeons",0),D.get("ballon",0)+D.get("ballons",0),D.get("bataillon",0),D.get("depeche",0)+D.get("depeches",0),D.get("sante",0),D.get("bonne",0),D.get("portante",0)))
base_lp=B.lp_uni
def make(lam):
    def lp(w):
        pd=(D.get(w,0)+0.1)/(ND+0.1*VD); pg=math.exp(base_lp(w))
        return math.log(lam*pd+(1-lam)*pg)
    return lp
B.CFG.update(dict(unigram=True,bigram=True,bias=0.015,sigma=0.02))
names=[i[0] for i in B.ITEMS]; print("items:",names)
for lam in (0.0,0.25,0.5):
    B.lp_uni=make(lam) if lam>0 else base_lp
    m,t10,ranks=B.evaluate(False)
    print("lambda %.2f: MRR %.4f top-10 %d/10 ranks %s"%(lam,m,t10,ranks)); sys.stdout.flush()
