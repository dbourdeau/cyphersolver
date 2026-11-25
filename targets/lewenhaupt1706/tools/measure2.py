"""MESURE UNIQUE v2 (PREREG-v2). usage (depuis v2/work) :
measure2.py <cle_K2.json> <calib_UR.json> <lexique Lx.txt> <transcriptions H2...>
Décisif : N = (L - U)/(R - U), L = log2-vraisemblance moyenne par lettre (modèle 5-grammes sur corpus_train.txt), U = log2(1/29),
R = constante gelée (calib_UR.json). Témoins : 200 clés permutées (valeurs de K2 permutées entre codes, graine 20261117).
Succès ssi N(K2) >= 0,60 ET N(K2) >= max(témoins) + 0,30.
Informatif (non décisif) : 200 mélanges de l'ordre des groupes (graine 20261118) ; part de groupes inconnus ;
couverture lexicale par mots >= 4 lettres de Lx (segmentation DP) pour K2 et témoins."""
import sys, os, json, random, statistics as st
sys.path.insert(0, os.path.dirname(__file__))
from ngram import LM, norm
from score2 import *
key = json.load(open(sys.argv[1], encoding='utf-8')); UR = json.load(open(sys.argv[2])); R = UR['R']
LX = set(w for w in (norm(l.strip()) for l in open(sys.argv[3], encoding='utf-8')) if len(w) >= 4)
runs = read_runs(sys.argv[4:]); ng = sum(map(len, runs)); unk = sum(1 for r in runs for c in r if c not in key)
lm = LM(open('corpus_train.txt').read())
N = lambda k, rr=runs: (score(lm, decode(rr, k)) - U) / (R - U)
def lexcov(k):
    tot = cov = 0
    for s in decode(runs, k):
        n = len(s); b = [0]*(n+1)
        for i in range(1, n+1):
            b[i] = b[i-1]
            for L in range(4, min(16, i)+1):
                if s[i-L:i] in LX and b[i-L] + L > b[i]: b[i] = b[i-L] + L
        tot += n; cov += b[n]
    return cov / tot if tot else 0
nK = N(key); ctr = [N(k) for k in permuted_keys(key, 200, 20261117)]; mx = max(ctr)
rng = random.Random(20261118); flat = [c for r in runs for c in r]; shf = []
for _ in range(200):
    f = flat[:]; rng.shuffle(f); shf.append(N(key, [f]))
lK = lexcov(key); lc = [lexcov(k) for k in permuted_keys(key, 200, 20261117)]
out = {"groupes_H2": ng, "groupes_inconnus": unk, "part_inconnus": round(unk/ng, 4), "N_K2": round(nK, 4),
       "temoins_permutes_moy": round(st.mean(ctr), 4), "temoins_permutes_max": round(mx, 4), "seuil_1": 0.60, "seuil_2": round(mx + 0.30, 4),
       "succes": bool(nK >= 0.60 and nK >= mx + 0.30),
       "info_melanges_ordre_moy": round(st.mean(shf), 4), "info_melanges_ordre_max": round(max(shf), 4),
       "info_couverture_lex4_K2": round(lK, 4), "info_couverture_lex4_temoins_moy": round(st.mean(lc), 4), "info_couverture_lex4_temoins_max": round(max(lc), 4)}
print(json.dumps(out, ensure_ascii=False, indent=1))
