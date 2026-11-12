"""Contrôles PREREG : score crib de la lecture en lignes vs 1000 permutations aléatoires
des 25 groupes, 1000 additifs aléatoires 4 chiffres, et lecture en colonnes."""
import random
from groups import *
T=table()
CRIB=['電悉','大總統','總統','已','准','恢復','達賴','喇嘛','名號','封號','回','來京','進京','赴京','感激','優待','厚待','速','覆','復','通過','與否','否']
def dec(s,add=None):
    out=''
    for i in range(0,len(s)-3,4):
        c=s[i:i+4]
        if add: c=''.join(str((int(a)-int(b))%10) for a,b in zip(c,add))
        out+=(T.get(c,('',''))[1] or T.get(c,('',''))[0] or '□')[:1]
    return out
def score(t): return sum(t.count(w)*len(w) for w in CRIB if len(w)>1)+sum(t.count(w) for w in CRIB if len(w)==1)
rows=[[c[r] for c in COLS if r<len(c)] for r in range(7)]
groups=[g for r in rows for g in r]
srow=''.join(groups); scol=''.join(g for c in COLS for g in c)
tr,tc=dec(srow),dec(scol)
print('lignes  ',score(tr),tr); print('colonnes',score(tc),tc)
random.seed(2465)
perm=[score(dec(''.join(random.sample(groups,25)))) for _ in range(1000)]
addk=[score(dec(srow,''.join(random.choice('0123456789') for _ in range(4)))) for _ in range(1000)]
for n,v in (('permutations',perm),('additifs aléatoires',addk)):
    print(n,'max',max(v),'moyenne %.2f'%(sum(v)/len(v)),'p(>=lignes)=',sum(x>=score(tr) for x in v)/len(v))
h=len(tr)//2
print('moitié 1:',tr[:h],score(tr[:h]),' moitié 2:',tr[h:],score(tr[h:]))
