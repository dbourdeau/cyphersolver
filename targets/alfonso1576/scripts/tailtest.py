# Language-free check of the tail reads. Uses only the sign positions from align_signs.py and ink under the line.
# Feature: dark pixels in a box below the foot level, to the left of the sign (a loop reaches it, a foot does not).
import json
import numpy as np
from PIL import Image
Q=json.load(open('work/qpos.json'))
T={int(l.split()[0]):l.split()[2] for l in open('work/tails/tails_final.tsv').read().splitlines()[1:]}
G={p:np.array(Image.open(f'scans/{p}_full.jpg').convert('L')) for p in ('f76r','f76v','f77r')}
F=[]
for k,q in enumerate(Q):
    g=G[q['p']];x,y=q['x'],q['y']
    B=g[y+92:y+126, x-210:x-50]
    F.append((B<120).mean())
F=np.array(F);Y=np.array([T[k]=='L' for k in range(len(Q))])
def auc(s,y):
    r=s.argsort().argsort()+1;n1=y.sum();n0=len(y)-n1
    return (r[y].sum()-n1*(n1+1)/2)/(n1*n0)
pg=np.array([q['p'] for q in Q])
for name,m in (('all',pg!=''),('76r+76v',pg!='f77r'),('77r',pg=='f77r')):
    a=auc(F[m],Y[m]);rng=np.random.default_rng(1)
    sh=[auc(F[m],rng.permutation(Y[m])) for _ in range(500)]
    print(name,m.sum(),'AUC',round(a,3),'shuffled max',round(max(sh),3))
