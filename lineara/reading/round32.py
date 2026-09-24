"""Round 32 (loop round 4 of 10): Minoan-shaped names across the Linear B archives.

Score: a syllable model of Linear A list names against Linear B common words, applied to the stem (final syllable
removed; decipher15c.score_common), so that Greek endings cannot drive the result. Each test compares AUCs by
label permutation.

U1  Knossos personal names are more Minoan-shaped than Thebes/Mycenae/Tiryns personal names.
U2  Knossos names also attested on the mainland are less Minoan-shaped than Knossos-only names.
U3  Knossos names with a Greek etymology are less Minoan-shaped than those without (a check on the measure).
U4  Pylos names without a Greek etymology are more Minoan-shaped than Pylos names with one.
U5  Knossos theonyms are more Minoan-shaped than Pylos theonyms.
U6  Stems of Knossos ethnics are more Minoan-shaped than stems of Pylos ethnics.
U7  Knossos names written with undeciphered signs are more Minoan-shaped in their readable signs.
U8  Pylos names also attested at Knossos are more Minoan-shaped than Pylos-only names.
U9  Knossos names containing special signs (ra2, pu2, ta2, a2, a3, au, ro2, nwa) are more Minoan-shaped.
U10 Knossos names attested only in the Room of the Chariot Tablets are more Minoan-shaped than later ones.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402

B, T, V, F = R.B, R.T, R.V, R.F
CAT, SITES = B.LB_CAT, B.LB_SITES
score = F.score_common
MAIN = {'Thebes', 'Mycenae', 'Tiryns', 'Vases - Thebes', 'Vases - Tiryns', 'Vases - Mycenae', 'Midea'}
SPECIAL = {'ra2', 'pu2', 'ta2', 'a2', 'a3', 'au', 'ro2', 'nwa', 'ra3', 'pte'}
clean = T.clean
names = lambda pred: [w for w, s in SITES.items() if CAT.get(w) == 'anthroponym' and len(w) >= 2 and pred(w, s)]


def auc_test(a, b, text, sc=score):
    f = lambda x, y: R.V.auc([sc(w) for w in x], [sc(w) for w in y])
    real = f(a, b)
    pool, k, null = list(a) + list(b), len(a), []
    for _ in range(R.REPS):
        R.rng.shuffle(pool)
        null.append(f(pool[:k], pool[k:]))
    p = R.pv_hi(null, real)
    return p, text, {'auc': round(real, 3), 'p': round(p, 4), 'n': [len(a), len(b)]}, {}


def U1():
    kn = names(lambda w, s: s == {'Knossos'} and clean(w))
    ma = names(lambda w, s: s <= MAIN and clean(w))
    return auc_test(kn, ma, 'Knossos names are more Minoan-shaped than Thebes/Mycenae/Tiryns names')


def U2():
    only = names(lambda w, s: s == {'Knossos'} and clean(w))
    shared = names(lambda w, s: 'Knossos' in s and len(s) > 1 and clean(w))
    return auc_test(only, shared, 'Knossos-only names are more Minoan-shaped than Knossos names shared with the mainland')


def U3():
    kn = T.KN_N
    ng = [w for w in kn if w not in B.GREEK]
    gk = [w for w in kn if w in B.GREEK]
    return auc_test(ng, gk, 'Knossos names without a Greek etymology are more Minoan-shaped than Greek ones')


def U4():
    py = T.PY_N
    ng = [w for w in py if w not in B.GREEK]
    gk = [w for w in py if w in B.GREEK]
    return auc_test(ng, gk, 'Pylos names without a Greek etymology are more Minoan-shaped than Greek ones')


def U5():
    kn = [w for w, s in SITES.items() if CAT.get(w) == 'theonym' and 'Knossos' in s and 'Pylos' not in s and clean(w)]
    py = [w for w, s in SITES.items() if CAT.get(w) == 'theonym' and 'Pylos' in s and 'Knossos' not in s and clean(w)]
    return auc_test(kn, py, 'Knossos theonyms are more Minoan-shaped than Pylos theonyms')


def U6():
    stem2 = lambda w: w[:-2] if len(w) >= 4 else w[:-1]
    kn = [w for w in V.kn_only if CAT.get(w) == 'ethnic' and clean(w) and len(w) >= 3]
    py = [w for w in V.py_only if CAT.get(w) == 'ethnic' and clean(w) and len(w) >= 3]
    sc = lambda w: score(stem2(w) + ('x',))
    return auc_test(kn, py, 'Stems of Knossos ethnics are more Minoan-shaped than stems of Pylos ethnics', sc)


def U7():
    star = [tuple(x for x in w if not x.startswith('*')) for w in names(lambda w, s: s == {'Knossos'} and not clean(w))]
    star = [w for w in star if len(w) >= 2]
    plain = names(lambda w, s: s == {'Knossos'} and clean(w))
    return auc_test(star, plain, 'Knossos names with undeciphered signs are more Minoan-shaped in their readable signs')


def U8():
    both = names(lambda w, s: 'Pylos' in s and 'Knossos' in s and clean(w))
    only = names(lambda w, s: s == {'Pylos'} and clean(w))
    return auc_test(both, only, 'Pylos names also attested at Knossos are more Minoan-shaped than Pylos-only names')


def U9():
    kn = T.KN_N
    sp = [w for w in kn if any(x in SPECIAL for x in w)]
    ot = [w for w in kn if not any(x in SPECIAL for x in w)]
    return auc_test(sp, ot, 'Knossos names with special signs are more Minoan-shaped')


def U10():
    fs = R.G.F.X.T.V  # placeholder to keep imports uniform
    import vigorous2 as W
    spots = W.knossos_findspots()
    rct = [w for w in T.KN_N if spots.get(w) == {'RCT'}]
    later = [w for w in T.KN_N if spots.get(w) == {'later'}]
    return auc_test(rct, later, 'Room of the Chariot Tablets names are more Minoan-shaped (stem-scored) than later Knossos names')


if __name__ == '__main__':
    R.run('round32', 'Minoan-shaped names across the Linear B archives', __doc__, [U1, U2, U3, U4, U5, U6, U7, U8, U9, U10])
