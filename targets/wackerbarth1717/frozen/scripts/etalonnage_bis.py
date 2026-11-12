# ÉTALONNAGE BIS (Avenant 2-bis) : candidats supplémentaires, apprentissage hors V seulement, clé b.
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lm import *
E_SCANS = ['0017', '0062', '0071', '0072', '0080', '0081', '0086', '0087', '0088']
ns = []
for s in E_SCANS:
    for p in read_releve(os.path.join(REL, f'T-{s}.txt')):
        for lid, toks, g in p['lines']: ns += [v for k, v in toks if k == 'n']
Kb = load_key('KEY-W1717b.tsv'); M = LM()
def U(s):
    t = 0; n = 0
    for ch in s:
        if ch == '#': continue
        t += math.log((M.C[1][ch] + KADD) / (M.N1 + KADD * M.V)); n += 1
    return t / max(1, n)
def L5(s): return M.L1(s) - U(s)   # information séquentielle : 4-grammes moins unigrammes
R = {'groupes_E': len(ns)}
R['L5'] = {k: round(v, 4) for k, v in stats(L5, Kb, ns).items()}
print(json.dumps(R))
# L6/L7 : mêmes mesures, mais toute valeur de longueur ≥ 3 (nomenclateur, polygramme long) remplacée par « # »
# (une permutation qui envoie « votreexcellence » sur un nombre fréquent fabrique du français : bruit des témoins).
def strip(K): return {n: (v if len(v) <= 2 else '#') for n, v in K.items()}
Kb6 = strip(Kb)
R['L6'] = {k: round(v, 4) for k, v in stats(M.L1, Kb6, ns).items()}
R['L7'] = {k: round(v, 4) for k, v in stats(L5, Kb6, ns).items()}
print(json.dumps(R))
