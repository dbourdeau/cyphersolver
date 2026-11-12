"""Mesure unique PREREG-R1101-p1 (sadoleto-1482). Lit la chaîne aveugle et R, imprime S_car, S_mot, témoins."""
import random, re, sys, json
from pathlib import Path
D = Path(__file__).resolve().parent
hyp = (D/'TRANSCRIPTION-AVEUGLE-R1101-p1.md').read_text().split("telle qu'elle sera mesurée\n")[1].strip()
ref = (D/'COLLATION-R1101-p1.md').read_text().split('## R (référence mesurée)\n')[1].strip()
def norm(s):
    s = s.lower().replace('&', ' et ')
    s = s.replace('j','i').replace('y','i').replace('v','u')
    return [w for w in re.sub('[^a-z ]',' ',s).split() if w]
def lev(a,b):
    p=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        c=[i]
        for j,cb in enumerate(b,1):
            c.append(min(p[j]+1,c[j-1]+1,p[j-1]+(ca!=cb)))
        p=c
    return p[-1]
def align(H,R):
    n,m=len(H),len(R)
    INF=1e9
    D_=[[0.0]*(m+1) for _ in range(n+1)]; B=[[None]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1): D_[i][0]=i; B[i][0]='u'
    for j in range(1,m+1): D_[0][j]=j; B[0][j]='l'
    for i in range(1,n+1):
        for j in range(1,m+1):
            h,r=H[i-1],R[j-1]
            sub=lev(h,r)/max(len(h),len(r))
            opts=[(D_[i-1][j-1]+sub,'d'),(D_[i-1][j]+1,'u'),(D_[i][j-1]+1,'l')]
            D_[i][j],B[i][j]=min(opts)
    i,j=n,m; pairs=[]
    while i>0 or j>0:
        b=B[i][j]
        if b=='d': pairs.append((H[i-1],R[j-1])); i-=1; j-=1
        elif b=='u': pairs.append((H[i-1],None)); i-=1
        else: pairs.append((None,R[j-1])); j-=1
    return pairs[::-1]
def score(H,R):
    pairs=align(H,R)
    tot=sum(len(r) for r in R)
    car=sum(max(0,len(r)-lev(h,r)) for h,r in pairs if h and r)/tot
    mot=sum(1 for h,r in pairs if h and r and h==r)/len(R)
    return car,mot,pairs
H,R=norm(hyp),norm(ref)
car,mot,pairs=score(H,R)
alpha='abcdefghijklmnopqrstuvwxyz'
c1=[]
for s in range(1,251):
    rnd=random.Random(s); perm=list(alpha); rnd.shuffle(perm); t=str.maketrans(alpha,''.join(perm))
    c1.append(score([w.translate(t) for w in H],R)[0])
c2=[]
for s in range(1001,1251):
    rnd=random.Random(s); RR=R[:]; rnd.shuffle(RR)
    c2.append(score(H,RR)[0])
mx=max(c1+c2)
out={'hyp_words':len(H),'hyp_letters':sum(map(len,H)),'ref_words':len(R),'ref_letters':sum(map(len,R)),
     'S_car':round(car,4),'S_mot':round(mot,4),'max_C1':round(max(c1),4),'max_C2':round(max(c2),4),'max_temoins':round(mx,4),
     'marge':round(car-mx,4),'critere_085':car>=0.85,'critere_marge_030':car>=mx+0.30}
print(json.dumps(out,indent=1))
for h,r in pairs: print(f'{h or "—":14s} {r or "—"}')
