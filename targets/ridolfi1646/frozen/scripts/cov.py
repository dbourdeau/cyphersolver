# cov.py — métrique COV (reprise exacte de ctrl.py de Fable) : part des lettres décodées couvertes par des mots
# >= 4 lettres du lexique italien de cyphersolver (lexique-it-cyphersolver.json, entrées de fréquence >= 3,
# v->u, j->i, accents ôtés), couverture maximale par programmation dynamique dans chaque segment.
# Témoins : clé mélangée = permutation des valeurs entre codes (lettres entre lettres, syllabes entre syllabes,
# fonction shuffled() de ctrl.py) ; mélange des groupes = permutation des groupes décodables entre leurs positions
# (coupures X / 3 chiffres / inconnus laissées en place).
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json, os, re, random
from decode import KEY, segments, ROOT
lex = json.load(open(os.path.join(ROOT, 'lexique-it-cyphersolver.json')))
W = set()
for w, n in lex.items():
    w = w.lower().replace('v', 'u').replace('j', 'i')
    for a, b in zip('àèéìòù', 'aeeiou'): w = w.replace(a, b)
    if re.fullmatch('[a-z]+', w) and len(w) >= 4 and n >= 3: W.add(w)
MAXL = max(map(len, W))

def cover(s):
    n = len(s); best = [0] * (n + 1)
    for i in range(1, n + 1):
        best[i] = best[i - 1]
        for l in range(4, min(MAXL, i) + 1):
            if s[i - l:i] in W and best[i - l] + l > best[i]: best[i] = best[i - l] + l
    return best[n]

def COV(toks, K=KEY):
    S = segments(toks, K); tot = sum(map(len, S))
    return (sum(cover(s) for s in S) / tot) if tot else 0.0, tot

def shuffled_key(K, rng):
    let = [g for g in K if len(K[g]) == 1]; syl = [g for g in K if len(K[g]) > 1]
    K2 = {}
    for grp in (let, syl):
        v = [K[g] for g in grp]; rng.shuffle(v); K2.update(dict(zip(grp, v)))
    return K2

def shuffled_groups(toks, rng, K=KEY):
    idx = [i for i, t in enumerate(toks) if len(t) == 2 and t in K]
    v = [toks[i] for i in idx]; rng.shuffle(v)
    out = list(toks)
    for i, t in zip(idx, v): out[i] = t
    return out
