import sys,json,random,re,unicodedata
# measure_main2.py key.json heldout.txt lexique.json corpus... — measure_v4 généralisée pour la main 2 (16/11 soir) :
# valeur « x|y » = ambiguïté tranchée au lexique (ordre x puis y) ; valeur « ? » dans la clé = code de nomenclateur déclaré =
# coupure de mot hors dénominateur ; signe absent de la clé ou transcrit « ? » = lettre non couverte (dans le dénominateur).
key=json.load(open(sys.argv[1]))
def norm(s):
    s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
    return s.replace('v','u').replace('j','i').replace('y','i')
lex=json.load(open(sys.argv[3]))
MINL=4; MINF=10
words={norm(w) for w,f in lex.items() if f>=MINF and re.fullmatch('[a-zA-Z]+',norm(w))}
from collections import Counter
cw=Counter()
for cf in sys.argv[4:]:
    cw.update(re.findall('[a-z]+',norm(open(cf,encoding='utf-8',errors='ignore').read().replace('ſ','s'))))
words|={w for w,f in cw.items() if f>=3}
SHORT={'de','le','la','et','en','il','ne','se','ce','ie','me','te','ma','sa','ta','du','au','un','ou','si','on','ni','qu','les','des','que','qui','par','pas','est','son','ses','sur','une','aux','car','lui','eux','mes','nos','vos','ont','dit','peu','bon','ces','cas','luy','leur','tant','sont','fait','tout','mais','plus','dont','nous','vous','elle','auec','bien','sans','dire','estre','faire','auoir','comme','iay','ay','ai','or','ia','fort'}
words={w for w in words if len(w)>=MINL}|SHORT
MAXL=max(len(w) for w in words)
toks=[]
for line in open(sys.argv[2]):
    if line.startswith('L'): toks+=[t for t in line.split(':',1)[1].split() if t not in ('|','/')]
CODES={t for t,v in key.items() if v=='?'}
def decode(k):
    out=[]
    for t in toks:
        if t in CODES: out.append('|'); continue
        v=k.get(t,'#') if t!='?' else '#'
        if v in ('#','?'): out.append(['#'])
        elif '|' in v: out.append([norm(x) for x in v.split('|')])
        else: out.append([norm(v)])     # valeur multi-lettres = une unité fixe
    return out
def expand(units):
    res=['']
    for u in units:
        res=[r+c for r in res for c in u]
        if len(res)>64: return []
    return res
def cover(units):
    # units: liste de listes d'options (chaînes). DP sur les unités ; une option de mot = concaténation ;
    # arbitrage mécanique : couverture maximale ; à égalité, première option dans l'ordre (s avant m), mot le plus long.
    n=len(units); best=[0]*(n+1); choice=[None]*(n+1)
    for i in range(1,n+1):
        best[i]=best[i-1]; choice[i]=(i-1,None)
        for j in range(i-1,-1,-1):
            seg=units[j:i]
            if sum(len(u[0]) for u in seg)>MAXL: break
            for w in expand(seg):
                if w in words:
                    if best[j]+len(w)>best[i]: best[i]=best[j]+len(w); choice[i]=(j,w)
                    break
    # reconstruction
    out=[]; i=n
    while i>0:
        j,w=choice[i]
        out.append(w if w else units[i-1][0]); i=j
    return best[n], ''.join(reversed(out))
def score(k):
    d=decode(k); parts=[]; cur=[]
    for u in d:
        if u=='|': parts.append(cur); cur=[]
        else: cur.append(u)
    parts.append(cur)
    n=sum(len(u[0]) for p in parts for u in p)
    cs=[cover(p) for p in parts]
    return sum(c for c,_ in cs)/n, '|'.join(s for _,s in cs)
sc,s=score(key)
pool=[t for t in key if (len(key[t])==1 and key[t]!='?') or '|' in key[t]]
vals=[key[t] for t in pool]
random.seed(20261116)
ctl=[]
for i in range(200):
    v=vals[:]; random.shuffle(v); k2=dict(key); k2.update(zip(pool,v)); ctl.append(score(k2)[0])
print(json.dumps({'n_signs':len(toks),'score':round(sc,4),'ctl_max':round(max(ctl),4),'ctl_mean':round(sum(ctl)/len(ctl),4),
 'pass': sc>=0.85 and sc>=max(ctl)+0.30,'decoded':s},ensure_ascii=False,indent=1))
