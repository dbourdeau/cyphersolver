"""Variante de build_lm.py (ljs51-aveugle) : liste de textes en argument 2 (corpus elargi). Meme lissage."""
"""Modele 4-grammes lettres, interpolation fixe (0.70/0.20/0.07/0.03) sur comptes add-0.01.
Deux variantes : avec espaces (sp) et sans espaces (nosp). Ecrit des tables float32 29^4."""
import sys, os, struct, math
sys.path.insert(0, "../../blind-confirmation/scripts")
from common import *
from array import array
outdir = sys.argv[1]; TRAIN = sys.argv[2].split(",")
V = 29
def seqs(spaces):
    for f in TRAIN:
        t = strip_meta(open(CORPUS + f, encoding="utf8", errors="ignore").read())
        for line in t.split('\n'):
            ws = words(line)
            if not ws: continue
            if spaces: yield [0] + [x for w in ws for x in ([IDX[c] for c in w] + [0])]
            else: yield [IDX[c] for w in ws for c in w]
for spaces, name in ((True, 'sp'), (False, 'nosp')):
    c1=[0]*V; c2=[0]*V**2; c3=[0]*V**3; c4=[0]*V**4; n=0
    prev = []
    for s in seqs(spaces):
        if not spaces:
            s = prev[-3:] + s  # texte continu sans espaces : enchaine les lignes
        else:
            s = [0,0] + s
        for i, x in enumerate(s):
            c1[x]+=1; n+=1
            if i>=1: c2[s[i-1]*V+x]+=1
            if i>=2: c3[(s[i-2]*V+s[i-1])*V+x]+=1
            if i>=3: c4[((s[i-3]*V+s[i-2])*V+s[i-1])*V+x]+=1
        prev = s
    k=0.01
    def P(cnt, ctx_tot): return (cnt+k)/(ctx_tot+k*V)
    t2=[sum(c2[a*V:(a+1)*V]) for a in range(V)]
    t3=[sum(c3[a*V:(a+1)*V]) for a in range(V*V)]
    t4=[sum(c4[a*V:(a+1)*V]) for a in range(V**3)]
    tab = array('f', [0.0]*V**4)
    for a in range(V):
      for b in range(V):
        for c in range(V):
          ctx3=(a*V+b)*V+c; ctx2=b*V+c
          for d in range(V):
            if not spaces and d==0: tab[ctx3*V+d]=-30.0; continue
            p = (0.70*P(c4[ctx3*V+d],t4[ctx3]) + 0.20*P(c3[ctx2*V+d],t3[ctx2])
                 + 0.07*P(c2[c*V+d],t2[c]) + 0.03*(c1[d]+k)/(n+k*V))
            tab[ctx3*V+d]=math.log(p)
    with open(os.path.join(outdir, f'lm4_{name}.bin'),'wb') as f: tab.tofile(f)
    print(name, 'symboles', n)
