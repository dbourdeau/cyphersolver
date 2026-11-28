"""Calibration sur chiffres SYNTHETIQUES tires du diwan d'Ibn Nubata (hors corpus du modele).
Aucune donnee LJS 51."""
import sys, os, random, difflib, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from solve import solve
lam=float(sys.argv[1]); R=int(sys.argv[2]); IT=int(sys.argv[3]); lens=list(map(int,sys.argv[4].split(','))); reps=int(sys.argv[5])
t=strip_meta(open(CORPUS+CALIB,encoding='utf8').read())
ws=words(t)
rnd=random.Random(777)
def acc(a,b):
    a=a.replace(' ',''); b=b.replace(' ','')
    m=sum(x.size for x in difflib.SequenceMatcher(None,a,b,autojunk=False).get_matching_blocks())
    return m/max(len(a),len(b))
for L in lens:
    res=[]; t0=time.time()
    for r in range(reps):
        i=rnd.randrange(len(ws)-200); seq=[]; j=i
        while sum(len(w) for w in seq)<L: seq.append(ws[j]); j+=1
        plain=' '.join(seq)
        letters=sorted(set(plain.replace(' ','')))
        cls={}; k=0
        for c in letters:
            cls[c]=[k]; k+=1
            if rnd.random()<0.12: cls[c].append(k); k+=1
        toks=[]
        for w in seq:
            toks += [rnd.choice(cls[c]) for c in w]; toks.append(-1)
        toks=toks[:-1]
        d,o,l,dec,_=solve(toks,k,True,lam,R,IT,r)
        res.append(acc(dec,plain))
    print(f"L={L} lam={lam} R={R} IT={IT} acc moy={sum(res)/len(res):.2f} >=0.85: {sum(x>=0.85 for x in res)}/{reps} ({time.time()-t0:.1f}s)", flush=True)
