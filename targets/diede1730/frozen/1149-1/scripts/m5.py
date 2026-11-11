# Mesure M5 (PREREG-1730-A1). Usage: python3 m5.py KEY.tsv CODES.txt LEX-M5.txt [ncodes]
# Couverture = lettres décodées couvertes par une segmentation optimale (DP) en mots du lexique / positions totales.
# Groupe hors clé (absent, ou « douteux ») = 1 position '?' jamais couverte. Nulle « · » = rien.
import sys,random
kf,cf,lf=sys.argv[1:4]; NC=int(sys.argv[4]) if len(sys.argv)>4 else 160
def norm(s):
    s=s.lower().replace('ß','ss')
    for a,b in (('ä','a'),('ö','o'),('ü','u'),('ÿ','y'),('j','i'),('y','i'),('w','u'),('v','u')): s=s.replace(a,b)
    return ''.join(ch for ch in s if 'a'<=ch<='z')
key={}
for ln in open(kf,encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    c,v,st,n,r=ln.rstrip('\n').split('\t')
    if st in ('sûr','probable'): key[c]='' if v=='·' else v
codes=[t.strip('?') for t in open(cf,encoding='utf-8').read().split() if t.strip('?').isdigit()][:NC]
lex=set(open(lf).read().split()); ML=max(map(len,lex))
def decode(k):
    out=[]
    for c in codes:
        v=k.get(c); out.extend(['?'] if v is None else list(norm(v)))
    return out
def cover(d):
    n=len(d); best=[0]*(n+1)
    for i in range(1,n+1):
        b=best[i-1]
        for L in range(1,min(ML,i)+1):
            w=''.join(d[i-L:i])
            if w in lex and best[i-L]+L>b: b=best[i-L]+L
        best[i]=b
    return best[n]/n if n else 0
def seg(d):
    n=len(d); best=[(0,None)]*(n+1)
    for i in range(1,n+1):
        b=(best[i-1][0],None)
        for L in range(1,min(ML,i)+1):
            w=''.join(d[i-L:i])
            if w in lex and best[i-L][0]+L>b[0]: b=(best[i-L][0]+L,L)
        best[i]=b
    out=[];i=n
    while i>0:
        L=best[i][1]
        if L: out.append(''.join(d[i-L:i]).upper()); i-=L
        else: out.append(d[i-1]); i-=1
    return ' '.join(reversed(out))
dec=decode(key); cov=cover(dec)
present=sorted({c for c in codes if c in key}); vals=[key[c] for c in present]
rnd=random.Random(1730); ctl=[]
for _ in range(200):
    p=vals[:]; rnd.shuffle(p); k2=dict(key); k2.update(zip(present,p)); ctl.append(cover(decode(k2)))
mx=max(ctl); mean=sum(ctl)/200; marge=cov-mx
verdict='VALIDÉ' if cov>=0.60 and marge>=0.30 else ('PARTIEL' if marge>=0.30 else 'ÉCHEC')
print(f'groupes={len(codes)} positions={len(dec)} hors clé={sum(1 for c in codes if c not in key)}')
print(f'couverture={cov:.3f} témoins n=200 moy={mean:.3f} max={mx:.3f} marge={marge:.3f} -> {verdict}')
print('décodage :',''.join(dec)); print('segmentation :',seg(dec))
