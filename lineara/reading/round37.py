"""Round 37 (loop round 9 of 10): do Minoan-derived words outside Linear A share the patterns found in this loop?

Hiatus here means a pure vowel sign after the first position of a word (in Linear B-style spelling a vowel sign
inside a word marks a vowel sequence).

Z1  Knossos personal names begin with a Q-row sign more often than Pylos personal names.
Z2  Knossos personal names have fewer internal pure vowel signs (hiatus) than Pylos names.
Z3  Knossos personal names end in a pure vowel sign less often than Pylos names.
Z4  Pre-Greek stems have fewer internal pure vowel signs than length-matched ordinary Greek stems.
Z5  Eteocretan has fewer internal pure vowel signs than Greek.
Z6  Knossos-only place names and ethnics have fewer internal pure vowel signs than Pylos-only ones.
Z7  Linear A's vowel profile is closer to Pre-Greek stems than to ordinary Greek stems (JSD).
Z8  Linear A's consonant profile is closer to Pre-Greek stems than to ordinary Greek stems (JSD).
Z9  Knossos common words without a Greek etymology are more Linear A-like (stem-scored) than those with one.
Z10 On Knossos tablets, words with undeciphered signs stand beside Minoan-shaped names more than chance.
"""
from collections import Counter
from math import log2
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402

B, T, V, E, F = R.B, R.T, R.V, R.E, R.F
grid = R.grid
vow = lambda x: bool(grid(x)) and grid(x)[0] == ''
hiatus = lambda ws: sum(1 for w in ws if any(vow(x) for x in w[1:])) / max(1, len(ws))


def cmp(a, b, f, text, lower=False):
    r, p, nm = R.compare(a, b, f, lower=lower)
    return p, text, {'target': round(f(a), 4), 'comparison': round(f(b), 4), 'p': round(p, 4), 'n': [len(a), len(b)]}, {}


def Z1():
    q = lambda ws: sum(1 for w in ws if grid(w[0]) and grid(w[0])[0] == 'q') / len(ws)
    return cmp(T.KN_N, T.PY_N, q, 'Knossos names begin with a Q-row sign more often than Pylos names')


def Z2():
    return cmp(T.KN_N, T.PY_N, hiatus, 'Knossos names have fewer internal vowel signs than Pylos names', lower=True)


def Z3():
    f = lambda ws: sum(1 for w in ws if vow(w[-1])) / len(ws)
    return cmp(T.KN_N, T.PY_N, f, 'Knossos names end in a pure vowel sign less often than Pylos names', lower=True)


def Z4():
    return cmp(T.PRE, T.GRK, hiatus, 'Pre-Greek stems have fewer internal vowel signs than Greek stems', lower=True)


def eteo():
    ete, gre = [], []
    for text in E.ET.ETEOCRETAN.values():
        for chunk in text.split():
            for piece in chunk.split('|'):
                ete += E.ET.stretches(piece)
    for text in (E.ET.GREEK, E.ET.HOMER):
        gre += [s for w in text.split() for s in E.ET.greek_stretches(w)]
    return E.spelled(ete), E.spelled(gre)


def Z5():
    a, b = eteo()
    return cmp(a, b, hiatus, 'Eteocretan has fewer internal vowel signs than Greek', lower=True)


def Z6():
    kn = [w for w in V.kn_only if T.CAT.get(w) in ('toponym', 'ethnic') and T.clean(w) and len(w) >= 2]
    py = [w for w in V.py_only if T.CAT.get(w) in ('toponym', 'ethnic') and T.clean(w) and len(w) >= 2]
    return cmp(kn, py, hiatus, 'Cretan place names have fewer internal vowel signs than Pylos place names', lower=True)


def prof(ws, part):
    c = Counter((grid(x)[1] if part == 'v' else (grid(x)[0] or 'V')) for w in ws for x in w if grid(x))
    n = sum(c.values())
    return {k: v / n for k, v in c.items()}


def jsd(p, q):
    keys = set(p) | set(q)
    m = {k: (p.get(k, 0) + q.get(k, 0)) / 2 for k in keys}
    kl = lambda a: sum(a[k] * log2(a[k] / m[k]) for k in keys if a.get(k, 0) > 0)
    return (kl(p) + kl(q)) / 2


def closer(part, text):
    la = prof(R.LA, part)
    f = lambda pre, grk: jsd(la, prof(grk, part)) - jsd(la, prof(pre, part))
    real = f(T.PRE, T.GRK)
    pool, k, null = list(T.PRE) + list(T.GRK), len(T.PRE), []
    for _ in range(R.REPS):
        R.rng.shuffle(pool)
        null.append(f(pool[:k], pool[k:]))
    p = R.pv_hi(null, real)
    return p, text, {'jsd_LA_PreGreek': round(jsd(la, prof(T.PRE, part)), 4), 'jsd_LA_Greek': round(jsd(la, prof(T.GRK, part)), 4), 'p': round(p, 4)}, {}


def Z7():
    return closer('v', 'Linear A\'s vowel profile is closer to Pre-Greek than to Greek')


def Z8():
    return closer('c', 'Linear A\'s consonant profile is closer to Pre-Greek than to Greek')


def Z9():
    oth = [w for w in V.kn_only if T.CAT.get(w) == 'other' and T.clean(w) and len(w) >= 2]
    ng = [w for w in oth if w not in B.GREEK]
    gk = [w for w in oth if w in B.GREEK]
    f = lambda x, y: V.auc([F.score_common(w) for w in x], [F.score_common(w) for w in y])
    real = f(ng, gk)
    pool, k, null = ng + gk, len(ng), []
    for _ in range(R.REPS):
        R.rng.shuffle(pool)
        null.append(f(pool[:k], pool[k:]))
    p = R.pv_hi(null, real)
    return p, 'Knossos common words without a Greek etymology are more Linear A-like', {'auc': round(real, 3), 'p': round(p, 4), 'n': [len(ng), len(gk)]}, {}


def Z10():
    kn = set(T.KN_N)
    rows = []
    for logos, words in T.KREC:
        star = any(any(x.startswith('*') for x in w) for w in words)
        names = [w for w in words if w in kn]
        if names:
            rows.append((star, sum(map(R.X.stem_score, names)) / len(names)))
    r_, p, a, b = R.flag_compare(rows, lambda x: x[0], lambda x: x[1])
    return p, 'Knossos tablets with undeciphered-sign words carry more Minoan-shaped names', {'with_star_words': a, 'without': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round37', 'Minoan-derived words outside Linear A', __doc__, [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10])
