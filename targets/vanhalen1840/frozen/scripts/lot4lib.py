"""lot4lib.py — fonctions communes à calib_lot4.py et mesure_lot4.py (avenant LOT4, vanhalen-1840).
Ne lit jamais H par lui-même : load_runs(part) ne renvoie que la partie demandée.
Réutilise measure.py (PROTOCOLE P01, SHA 8b82c31d…) pour lexique, clé, décodage et couverture.
"""
import os, sys, math, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import measure as M  # noqa: E402

VEILLE = os.path.dirname(os.path.dirname(ROOT))
LEX = os.path.join(VEILLE, '_shared', 'cyphersolver', 'lang', 'lexicons', 'es.json.gz')
CORPUS = os.path.join(ROOT, '..', 'PISTES-AUTO', 'fable-api', 'lots', 'lot3', '_communs',
                      'corpus-es-quijote-extrait-1.9Mo.txt')
KEYF = os.path.join(ROOT, 'KEY.tsv')
LM_N = 4


def load_runs(path, part):
    """Suites de la partie demandée ; '58|5.8' (artefact de notation, HANDOFF §4) lu '58' ; a|b -> a ; n? -> n."""
    runs = []
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        sid, pt, nums = line.split('\t')
        if pt != part:
            continue
        nums = nums.replace('58|5.8', '58')
        toks = []
        for t in nums.split('.'):
            t = t.strip().split('|')[0].rstrip('?')
            toks.append(t if t else '?')
        runs.append((sid, toks))
    return runs


class LM:
    """Modèle de lettres a-z à 4-grammes, interpolation linéaire fixe (poids 1,2,4,8 par ordre + plancher uniforme),
    appris sur l'extrait du Quijote (lettres seules, espaces ôtés : le chiffre n'a pas de séparateur)."""
    W = {1: 1.0, 2: 2.0, 3: 4.0, 4: 8.0}

    def __init__(self, path=CORPUS, n=LM_N):
        txt = M.norm(open(path, encoding='utf-8').read())
        self.n = n
        self.C = [collections.Counter() for _ in range(n + 1)]
        self.C[0][''] = len(txt)
        for k in range(1, n + 1):
            c = self.C[k]
            for i in range(len(txt) - k + 1):
                c[txt[i:i + k]] += 1
        self.cache = {}

    def lp(self, h, ch):
        tot, ws = 0.01 / 26, 0.01
        for k in range(1, self.n + 1):
            ctx = h[len(h) - (k - 1):] if k > 1 else ''
            if len(ctx) < k - 1:
                continue
            den = self.C[k - 1][ctx]
            if den:
                tot += self.W[k] * self.C[k][ctx + ch] / den
                ws += self.W[k]
        return math.log10(tot / ws)

    def score(self, s):
        """somme des log10 ; le '?' coupe le contexte et n'est pas compté."""
        if s in self.cache:
            return self.cache[s]
        v = 0.0
        for piece in s.split('?'):
            for i in range(len(piece)):
                v += self.lp(piece[max(0, i - self.n + 1):i], piece[i])
        self.cache[s] = v
        return v


def strings(runs, key):
    return [''.join(ws) for ws in M.decode(runs, key)]


def metrics(runs, key, lex, lm):
    """(car, lmpl) : car = couverture lexicale P01 (measure.car, '?' jamais couvert) ;
    lmpl = log10-probabilité moyenne par lettre décodée (hors '?')."""
    ss = strings(runs, key)
    tot = sum(len(s) for s in ss)
    cov = sum(M.coverage(s, lex) for s in ss)
    nl = sum(len(s.replace('?', '')) for s in ss)
    lmv = sum(lm.score(s) for s in ss)
    return (cov / tot if tot else 0.0), (lmv / nl if nl else -99.0)


def shuffled_key(key, rng):
    """témoin P01 : valeurs (hors séparateur/nulle) permutées entre les nombres de la clé."""
    nums = [n for n, v in key.items() if v not in ('_', '-')]
    vals = [key[n] for n in nums]
    rng.shuffle(vals)
    k2 = dict(key)
    k2.update(zip(nums, vals))
    return k2


def shuffled_groups(runs, rng):
    """témoin « permutation de groupes » : tous les nombres de la portion mélangés entre leurs positions,
    longueurs de suites conservées, clé inchangée."""
    flat = [t for _, ts in runs for t in ts]
    rng.shuffle(flat)
    out, i = [], 0
    for sid, ts in runs:
        out.append((sid, flat[i:i + len(ts)]))
        i += len(ts)
    return out


def witnesses(runs, key, lex, lm, nk, ng, seed_k, seed_g):
    rk, rg = random.Random(seed_k), random.Random(seed_g)
    K = [metrics(runs, shuffled_key(key, rk), lex, lm) for _ in range(nk)]
    G = [metrics(shuffled_groups(runs, rg), key, lex, lm) for _ in range(ng)]
    return K, G


def rule(car, lmpl, K, G, c1, dK, dG):
    """Règle calibrée LOT4 : C1 car >= c1 ; C2 lmpl >= max(lm clés mélangées) + dK ;
    C3 lmpl >= max(lm permutations de groupes) + dG."""
    mK = max(x[1] for x in K)
    mG = max(x[1] for x in G)
    return (car >= c1, lmpl >= mK + dK, lmpl >= mG + dG, mK, mG)
