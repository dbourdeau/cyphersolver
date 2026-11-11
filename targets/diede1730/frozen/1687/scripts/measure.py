# Mesure unique (PREREG.md + PREREG-3). Usage: python3 measure.py <dossier>
import sys, random, os
D=sys.argv[1]; seed=1730; key={}
for ln in open(os.path.join(D,'KEY.tsv'),encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    c,v,st,n,r=ln.rstrip('\n').split('\t')
    if st in ('sûr','probable'): key[c]='' if v=='·' else v
def norm(s):
    s=s.lower().replace('ß','ss')
    for a,b in (('ä','a'),('ö','o'),('ü','u'),('ÿ','y'),('j','i'),('y','i'),('w','u'),('v','u')): s=s.replace(a,b)
    return ''.join(ch if ('a'<=ch<='z' or ch=='?') else '' for ch in s)
codes=[t.strip('?') for l in open(os.path.join(D,'H-CHIFFRE.txt'),encoding='utf-8') if l.startswith('L') for t in l.split()[1:] if t!='|'][:160]
glose=open(os.path.join(D,'G-GLOSE.txt'),encoding='utf-8').read().split('\n',1)[1]
clear=norm(glose)
def decode(k):
    out=[]
    for c in codes:
        v=k.get(c)
        if v is None: out.append('?')
        else: out.extend(norm(v))
    return out
def sw(a,b):
    n,m=len(a),len(b); H=[[0]*(m+1) for _ in range(n+1)]; best=(0,0,0)
    for i in range(1,n+1):
        for j in range(1,m+1):
            d=H[i-1][j-1]+(1 if a[i-1]==b[j-1] and a[i-1]!='?' else -1)
            v=max(0,d,H[i-1][j]-1,H[i][j-1]-1); H[i][j]=v
            if v>best[0]: best=(v,i,j)
    i,j=best[1],best[2]; eq=0; A=[]; B=[]
    while i>0 and j>0 and H[i][j]>0:
        s=1 if a[i-1]==b[j-1] and a[i-1]!='?' else -1
        if H[i][j]==H[i-1][j-1]+s: eq+=(s==1); A.append(a[i-1]); B.append(b[j-1]); i-=1; j-=1
        elif H[i][j]==H[i-1][j]-1: A.append(a[i-1]); B.append('-'); i-=1
        else: A.append('-'); B.append(b[j-1]); j-=1
    return best[0],eq,''.join(reversed(A)),''.join(reversed(B))
dec=decode(key); N=len(dec)
sc,eq,A,B=sw(dec,clear); car=eq/N
present=sorted({c for c in codes if c in key}); vals=[key[c] for c in present]
rnd=random.Random(seed); ctl=[]
for _ in range(200):
    p=vals[:]; rnd.shuffle(p); k2=dict(key); k2.update(zip(present,p))
    d2=decode(k2); ctl.append(sw(d2,clear)[1]/len(d2))
mx=max(ctl); mean=sum(ctl)/len(ctl); marge=car-mx
verdict='VALIDÉ' if car>=0.85 and marge>=0.30 else ('PARTIEL' if marge>=0.30 else 'ÉCHEC')
print(f'groupes={len(codes)} positions={N} hors clé={sum(1 for c in codes if c not in key)} glose={len(clear)} lettres')
print(f'car={car:.3f} témoins n=200 moy={mean:.3f} max={mx:.3f} marge={marge:.3f} -> {verdict}')
print('décodage:',''.join(dec)); print('align H :',A); print('align G :',B)
