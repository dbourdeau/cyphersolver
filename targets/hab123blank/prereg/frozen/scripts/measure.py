"""Mesure UNIQUE sur la portion réservée (L19-L46) — NE PAS LANCER avant feu vert (gel publié).
Usage : python3 -I measure.py <passe_A> <passe_B> <cle.json> <lexique.txt> <scripts_dir> [--calib Lmin Lmax]"""
import sys,json,random,re
sys.path.insert(0,sys.argv[5])
from groups import groups
A_path,B_path,K_path,L_path=sys.argv[1:5]  # A_path = ARBITREE (principal), B_path = passe B (secondaire, rapportée)
lo,hi=19,46
if '--calib' in sys.argv:
    i=sys.argv.index('--calib'); lo,hi=int(sys.argv[i+1]),int(sys.argv[i+2])
K={k:v for k,v in json.load(open(K_path,encoding='utf-8')).items() if not k.startswith('_')}
def canon(w): return w.lower().replace('v','u').replace('j','i').replace('y','i')
LEX=set()
for line in open(L_path,encoding='utf-8'):
    if line.startswith('#'): continue
    LEX.update(canon(w) for w in line.split())
# lexique = lexique.txt SEUL (ni mots de la portion de clé ni mots clairs), identique pour l'étalonnage et la mesure
SEUIL=float(open(sys.argv[5]+'/SEUIL.txt').read().split()[0])
END={'a','ae','am','as','e','em','es','i','is','o','os','um','us','ibus','orum','arum','en','er','n','s','t','is'}
LEXL=[w for w in LEX if len(w)>=4]
def read(tok):
    if '?' in tok: return False
    if tok in LEX: return True
    if len(tok)>=4 and any(w.startswith(tok) for w in LEX if len(w)>len(tok)): return True
    if len(tok)>=5 and any(tok.startswith(w) and tok[len(w):] in END for w in LEXL): return True
    for i in range(2,len(tok)-1):
        if tok[:i] in LEX and tok[i:] in LEX and len(tok[i:])>=2: return True
    return False
def accord(G,key):
    tot=ok=0
    for n,g in G:
        tok=canon(''.join(key.get(c,'?') for c in g))
        tot+=len(g); ok+=len(g) if read(tok) else 0
    return ok/tot if tot else 0, tot
GA=[x for x in groups(A_path) if lo<=x[0]<=hi]; GB=[x for x in groups(B_path) if lo<=x[0]<=hi]
aA,nA=accord(GA,K); aB,nB=accord(GB,K); real=aA
rng=random.Random(3807); syms=list(K); vals=[K[s] for s in syms]; ctr=[]
for _ in range(200):
    v=vals[:]; rng.shuffle(v); k2=dict(zip(syms,v))
    ctr.append(accord(GA,k2)[0])
best=max(ctr)
print(f"portion L{lo:02d}-L{hi:02d} ; lettres A={nA} B={nB}")
print(f"accord ARBITREE={aA:.3f} (principal) ; passe B={aB:.3f} (rapporté)")
print(f"témoins 200 : meilleur={best:.3f} moyenne={sum(ctr)/len(ctr):.3f}")
print(f"CRITERE (>= {SEUIL:.3f} ET >= meilleur+0.30) :", "REMPLI" if (real>=SEUIL and real>=best+0.30) else "NON REMPLI")
