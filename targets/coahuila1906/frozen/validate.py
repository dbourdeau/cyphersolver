import re,sys,gzip,json,random,hashlib,math
LEX='lang/lexicons/'
es={w for w,c in json.load(gzip.open(LEX+'es.json.gz')).items() if (len(w)>=2 and c>=3) or w in ('a','y','o','e')}
en={w for w,c in json.load(gzip.open(LEX+'en.json.gz')).items() if (len(w)>=2 and c>=3) or w in ('a','i')}
# K1 : valeurs fixées sur T36 + T104 seulement
K1={10:'d',13:'a',17:'x',18:'n',19:'t',30:'o',32:'g',33:'a',34:'c',35:'r',38:'f',39:'l',40:'e',42:'u',43:'i',44:'m',45:'s',48:'b',49:'p',
    70:'o',72:'g',73:'a',74:'c',75:'r',76:'v',79:'l',83:'i',84:'m',85:'s',89:'p',90:'d',98:'n',99:'t'}
# extension par la règle d'appariement des dizaines 1<->9, 3<->7, 4<->8 (règle observée sur T36/T104)
P={1:9,9:1,3:7,7:3,4:8,8:4}
K=dict(K1)
for n,l in K1.items():
    t,u=divmod(n,10); m=P[t]*10+u
    K.setdefault(m,l)
print('K1 SHA256', hashlib.sha256(json.dumps(sorted(K.items())).encode()).hexdigest()[:16], 'valeurs', len(K))
HOLD={'T35','T53','T67','T82','T99','T124'}
runs=[]; cur=None
for line in open(sys.argv[1]):
    if line.startswith('#'): continue
    if line.startswith('T'): cur=line.split()[0]; continue
    for seg in re.split(r'<[^>]*>|\b[a-z]+\b',line):
        nums=[int(x[:2]) for x in re.findall(r'\b\d\d\??',seg)]
        if nums and cur in HOLD: runs.append((cur,nums))
def cover(s,lex):
    n=len(s); best=[0]*(n+1)
    for i in range(1,n+1):
        best[i]=best[i-1]
        for j in range(max(0,i-15),i):
            w=s[j:i]
            if '?' not in w and w in lex: best[i]=max(best[i],best[j]+len(w))
    return best[n]
def score(key):
    tot=cov=0
    for t,nums in runs:
        s=''.join(key.get(x,'?') for x in nums)
        cov+=cover(s,en if t=='T99' else es); tot+=len(s)
    return cov/tot
s0=score(K); print('couverture K1 tenu a l ecart', round(s0,3), 'lettres', sum(len(n) for _,n in runs))
random.seed(758); keys=list(K); W=[]
for i in range(1000):
    vals=[K[k] for k in keys]; random.shuffle(vals); W.append(score(dict(zip(keys,vals))))
W.sort(); print('temoins max',round(W[-1],3),'p99',round(W[989],3),'moy',round(sum(W)/len(W),3))
