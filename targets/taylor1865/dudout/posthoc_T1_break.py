# POST HOC (not pre-registered): T1 with one phase break. For each key: max over break word b and offsets o1,o2 of S.
import sys, random; sys.path.insert(0, __file__.rsplit('/',1)[0])
from prereg_measure import load, dec, S
import os, pathlib
_h=pathlib.Path(__file__).resolve().parent
T=load(next(c for c in [str(_h/'blind_transcription_frozen.txt'),str(_h.parent/'TRANSCRIPTION-AVEUGLE.txt')] if os.path.isfile(c)))['T1']
def best(key):
    L=len(key); bestv=-9
    starts=[0]; 
    for w in T: starts.append(starts[-1]+len(w))
    flat=''.join(T)
    for b in range(1,len(T)):
        cut=starts[b]
        for o1 in range(L):
            a=dec(flat[:cut],key,o1)
            for o2 in range(L):
                p=a+dec(flat[cut:],key,cut+o2)
                v=S(p); bestv=max(bestv,v)
    return bestv
rnd=random.Random(6810)
ctrl=sorted(best(''.join(rnd.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(15))) for _ in range(200))
for k in ["COMERETRIBUTION","COMPLETEVICTORY","MANCHESTERBLUFF","THENAVYOURPRIDE","OURNAVYOURPRIDE"]:
    v=best(k); print(k, round(v,4), "rank", 1+sum(c>=v for c in ctrl), "/201")
print("controls max", round(ctrl[-1],4), "median", round(ctrl[100],4))
