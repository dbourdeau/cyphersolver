import random,sys,re,os
sys.path.insert(0,'..'); sys.path.insert(0,'.')
from msolve import INV
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 5)
single=[u for u in INV if len(u)==1]
others=[u for u in INV if len(u)>1]
tab=sorted(set(single)|set(rnd.sample(others,180)))
codes={};c=100
for u in tab:
    codes[u]=[c]; c+=1
    if rnd.random()<0.08: codes[u].append(c); c+=1
txt="""le prince a fait savoir hier au magistrat que les troupes francaises devoient quitter la ville avant la fin du mois et que l'on attendoit de nouveaux ordres de la cour pour regler les quartiers d'hiver de l'armee on assure que le marechal a demande des vivres et du fourrage pour quinze jours mais les habitans se plaignent beaucoup des contributions qu'on exige d'eux et craignent que la guerre ne se porte bientot de ce cote ci l'electeur garde un grand silence sur tout cela et ne veut point se declarer avant d'avoir recu des nouvelles de vienne ni de versailles"""
t=re.sub('[^a-z]','',txt)
out=[];i=0
while i<len(t):
    for L in (4,3,2,1):
        s=t[i:i+L]
        if s in codes and (L==1 or rnd.random()<0.85):
            out.append(str(rnd.choice(codes[s]))); i+=L; break
print(len(out),'tokens')
h=len(out)//2
open('synth_runs.txt','w').write('S1: '+' '.join(out[:h])+'\nS2: '+' '.join(out[h:])+'\n')
