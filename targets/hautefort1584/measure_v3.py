import sys,json,random,re,unicodedata,math
# measure.py key.json heldout.txt lexique.json corpus.txt
key=json.load(open(sys.argv[1]))
def norm(s):
    s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
    return s.replace('v','u').replace('j','i').replace('y','i')
lex=json.load(open(sys.argv[3]))
MINL=4; MINF=int('10')
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
CODES={'14','15','16','17','C2','f2'}   # nomenclator signs without value: word boundary, outside the denominator
def decode(k):
    return ''.join('|' if t in CODES else (norm(k.get(t,'?')) if k.get(t,'?')!='?' else '?') for t in toks)
def cover(s):
    n=len(s); best=[0]*(n+1)
    for i in range(1,n+1):
        best[i]=best[i-1]
        for L in range(1,min(MAXL,i)+1):
            w=s[i-L:i]
            if w in words: best[i]=max(best[i],best[i-L]+L)
    return best[n]
def score(k):
    s=decode(k); parts=s.split('|'); n=sum(len(p) for p in parts)
    return sum(cover(p) for p in parts)/n, s
sc,s=score(key)
singles=[t for t in key if len(key[t])==1 and key[t]!='?']
vals=[key[t] for t in singles]
random.seed(20261116)
ctl=[]
for i in range(200):
    v=vals[:]; random.shuffle(v); k2=dict(key); k2.update(zip(singles,v)); ctl.append(score(k2)[0])
print(json.dumps({'n_signs':len(toks),'score':round(sc,4),'ctl_max':round(max(ctl),4),'ctl_mean':round(sum(ctl)/len(ctl),4),
 'pass': sc>=0.85 and sc>=max(ctl)+0.30,'decoded':s},ensure_ascii=False,indent=1))
