import json,re,collections,random,sys,unicodedata
sys.stdout.reconfigure(encoding="utf8")
def strip(s): return "".join(c for c in unicodedata.normalize("NFD",s) if unicodedata.category(c)!="Mn")
def toks(t): return [re.sub(r"[^a-z0-9]","",strip(x)) for x in re.findall(r"[\wéèêëàâîïôùûüçœ]+",t.lower().replace("'"," ").replace("’"," "))]
o=json.load(open("align_slide2_out.json"))
LIM=int(sys.argv[1]) if len(sys.argv)>1 else 200
cb={}
for p in o:
    if p["i"]<LIM and p["t"]=="w" and len(p["groups"])==1 and p["span"]==1 and p["unit"]: cb[p["groups"][0]]=p["unit"]
print("codebook entries (single-group words, first %d groups): %d"%(LIM,len(cb)))
corpus=[]
for f in ("gouvernementdela01favr","gouvernementdela02favr"):
    corpus+=[w for w in toks(open(r"C:\Users\dbour\enquete\%s.txt"%f,encoding="utf8",errors="replace").read()) if w]
bi=collections.Counter(zip(corpus,corpus[1:])); uni=collections.Counter(corpus)
print("reference corpus",len(corpus),"words")
def score(seq):
    """fraction of adjacent decoded pairs seen in the reference corpus (both words must be known groups)"""
    pairs=[(a,b) for a,b in zip(seq,seq[1:]) if a and b]
    return sum(1 for p in pairs if bi[p]>0),len(pairs)
pool=json.load(open("pool.json"))
random.seed(7)
words=list(cb.values())
rows=[]
for name,seq in pool.items():
    dec=[cb.get(g) for g in seq]
    k,n=score(dec)
    # control: same groups, codebook words shuffled among entries
    ks=[]
    for _ in range(30):
        vals=words[:]; random.shuffle(vals); cs=dict(zip(cb.keys(),vals))
        ks.append(score([cs.get(g) for g in seq])[0])
    known=sum(1 for d in dec if d)
    rows.append((name,len(seq),known,n,k,sum(ks)/len(ks)))
print("%-12s %6s %6s %6s %6s %8s"%("letter","groups","known","pairs","real","shuffled"))
for r in rows: print("%-12s %6d %6d %6d %6d %8.1f"%r)
# print decoded runs of >=3 consecutive known groups in other letters
print()
for name,seq in pool.items():
    if name=="chaudordy": continue
    runs=[];cur=[]
    for g in seq:
        if g in cb: cur.append(cb[g])
        else:
            if len(cur)>=3: runs.append(" ".join(cur))
            cur=[]
    print(name,len(runs),"runs>=3:",runs[:6])
