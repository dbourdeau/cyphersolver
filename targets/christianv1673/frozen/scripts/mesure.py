"""Mesure unique (PROTOCOLE.md). Usage : python3 scripts/mesure.py calib|mesure
Décodage déterministe par KEY-v1.json ; COV = part des lettres décodées (hors mots en clair) couvertes
par une segmentation optimale en mots du lexique (longueur >= 3, ou mots de 2 lettres de la liste courte)."""
import json,re,gzip,random,sys,csv,glob
W="working/"
MINW=4
SHORT={"at","og","de","er","en","et","om","os","af","nu","til","mod","som","med","den","det","der","sig","saa","sa","dem","hvor","wi","vi","for","ved","fra","kan","jo","ja"}
K=json.load(open(W+"KEY-v1.json"))
def norm(s):
    s=s.lower()
    for a,b in (("w","v"),("ø","o"),("ö","o"),("æ","e"),("å","aa"),("ck","k"),("c","k"),("q","k"),("ff","f"),("y","i"),("j","i"),("ß","s")): s=s.replace(a,b)
    s=re.sub(r"(.)\1+",r"\1",s)
    return re.sub(r"[^a-z]","",s)
def lexicon():
    L=set(norm(w) for w in json.load(gzip.open(W+"da.json.gz")))
    for f in glob.glob(W+"pairs/1674_img*.tsv"):
        for r in csv.reader(open(f),delimiter="\t"):
            if len(r)>=5 and r[0]!="img":
                for w in re.findall(r"[A-Za-zæøöåÆØÅ]+",r[4]+" "+(r[3] if r[3].startswith("[clair") else "")): L.add(norm(w))
    for f in (W+"transcr/FEUILLE_clair_img9R.txt",):
        for w in re.findall(r"[A-Za-zæøöåÆØÅ]+",open(f).read()): L.add(norm(w))
    return {w for w in L if len(w)>=MINW}|SHORT
def segments(path,labels=None):
    segs=[];cur=[]
    for l in open(path):
        if l.startswith("#") or not l.strip(): continue
        lab,s=l.split(None,1)
        if labels and lab not in labels: continue
        for t in re.findall(r"\[[^\]]*\]|\S+",s):
            if t.startswith("["):
                if cur: segs.append(cur); cur=[]
            else: cur.append(t.rstrip("?"))
    if cur: segs.append(cur)
    return segs
def dec(seg,key): return "".join(key.get(t,"?") for t in seg)
def cov(text,L,maxw=18):
    t=norm(text.replace("?","#")) if "?" not in text else re.sub(r"[^a-z#]","",text.lower().replace("?","#"))
    t=norm(t) if "#" not in t else "".join(norm(c) if c!="#" else "#" for c in t)
    n=len(t.replace("#",""));
    if n==0: return 0,0
    best=[0]*(len(t)+1)
    for i in range(1,len(t)+1):
        best[i]=best[i-1]
        for j in range(max(0,i-maxw),i-1):
            if t[j:i] in L: best[i]=max(best[i],best[j]+(i-j))
        
    return best[-1],n
def score(segs,key,L):
    c=n=0
    for s in segs:
        a,b=cov(dec(s,key),L); c+=a; n+=b
    return c/max(n,1),n
def controls(segs,L,seed=20261111,N=200):
    rnd=random.Random(seed); toks=sorted({t for s in segs for t in s if t in K})
    num=[t for t in toks if t.isdigit() and len(t)==3]; oth=[t for t in toks if t not in num]
    pk=[];sh=[]
    for _ in range(N):
        k=dict(K); 
        for grp in (num,oth):
            v=[K[t] for t in grp]; rnd.shuffle(v); k.update(zip(grp,v))
        pk.append(score(segs,k,L)[0])
        flat=[t for s in segs for t in s]; rnd.shuffle(flat); it=iter(flat)
        sh.append(score([[next(it) for _ in s] for s in segs],K,L)[0])
    return max(pk),max(sh)
if __name__=="__main__":
    L=lexicon()
    if sys.argv[1]=="calib":
        segs=segments(W+"transcr/FEUILLE_chiffre_img8-9.txt")
        print("lexique",len(L)); print("bloc 1 entier COV=%.3f lettres=%d"%score(segs,K,L))
        # fenêtres de ~ 150 groupes
        flat=[(i,t) for i,s in enumerate(segs) for t in s]
        for a in range(0,len(flat)-120,60):
            w=flat[a:a+150]; ss={}
            for i,t in w: ss.setdefault(i,[]).append(t)
            sg=list(ss.values()); c,n=score(sg,K,L); pk,sh=controls(sg,L,N=50)
            print("fenêtre %d COV=%.3f n=%d  max clés perm.=%.3f  max mélanges=%.3f"%(a,c,n,pk,sh))
    else:
        segs=segments(W+"transcr/CIBLE_img10-11.txt")
        c,n=score(segs,K,L); pk,sh=controls(segs,L)
        print("CIBLE groupes=%d lettres décodées=%d COV=%.3f ; max 200 clés permutées=%.3f ; max 200 mélanges=%.3f"%(sum(map(len,segs)),n,c,pk,sh))
