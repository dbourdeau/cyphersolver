"""Contrôles PREREG partie A : score crib (mots fixés dans PREREG) en lecture CTC directe
vs 1000 permutations des groupes et 1000 additifs aléatoires de 4 chiffres (graine 1359)."""
import random
exec(open('decode_ctc.py').read().split('for f in')[0])
CRIB=['達賴','喇嘛','蔣','中正','馬福祥','棍堪布','中央','誠','統一','擁護','悉','電']
def dec(g,add=None):
    out=''
    for c in g:
        if add: c=''.join(str((int(a)-int(b))%10) for a,b in zip(c,add))
        out+=T.get(c,'□')
    return out
def score(t): return sum(t.count(w)*len(w) for w in CRIB)
random.seed(1359)
for f in ('groups_14.txt','groups_15.txt'):
    g=open(f).read().split(); s0=score(dec(g))
    perm=[score(dec(random.sample(g,len(g)))) for _ in range(1000)]
    # bigram coherence: permutation destroys words but keeps chars, so use words of length>=2 only
    perm2=[sum(dec(random.sample(g,len(g))).count(w)*len(w) for w in CRIB if len(w)>1) for _ in range(1000)]
    s2=sum(dec(g).count(w)*len(w) for w in CRIB if len(w)>1)
    addk=[score(dec(g,''.join(random.choice('0123456789') for _ in range(4)))) for _ in range(1000)]
    h=len(g)//2
    print(f,'score',s0,'| mots>=2 car.',s2,'perm max',max(perm2),'p=',sum(x>=s2 for x in perm2)/1000,
          '| additifs max',max(addk),'p=',sum(x>=s0 for x in addk)/1000,
          '| moitiés',score(dec(g[:h])),score(dec(g[h:])))
