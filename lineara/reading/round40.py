"""Round 40 (second loop, round 2 of 10): the e/o rule with the refined consonant sets of round 30.

TAKE = {t, r, s, n, q} (consonants followed by e/o), AVOID = {k, p, m, j, w}. logOR = odds of e/o after TAKE against
after AVOID.

CC1  The rule holds in first syllables (Linear A against Linear B).
CC2  The rule holds in final syllables.
CC4  i/u are depleted after TAKE relative to AVOID more than in Linear B.
CC5  Within e/o syllables, the choice of e or o depends on the consonant more than in Linear B (normalised MI).
CC6  Knossos personal names show the rule more than Pylos personal names.
CC7  Knossos-only place names show it more than Pylos-only ones.
CC8  Pre-Greek stems show it more than length-matched Greek stems.
CC9  The rule replicates on SigLA's transcription (against Linear B).
CC10 Eteocretan shows it more than Greek.
CC11 Khania's Linear A shows it (against Linear B).
"""
from collections import Counter
from math import log
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round37 as Z  # noqa: E402

grid, LA, LB, X, T, V, D = R.grid, R.LA, R.LB, R.X, R.T, R.V, R.D
TAKE, AVOID = set('trsnq'), set('kpmjw')
lor = lambda ws, target=R.RARE, pool=None: X.log_or_v(ws, target, pool=pool, cons_sets=(TAKE, AVOID))


def cmp(a, b, f, text):
    r, p, nm = R.compare(a, b, f)
    return p, text, {'target': round(f(a), 3), 'comparison': round(f(b), 3), 'p': round(p, 4), 'n': [len(a), len(b)]}, {}


def CC1():
    return cmp([w[:1] for w in LA], [w[:1] for w in LB], lor, 'The rule holds in first syllables')


def CC2():
    return cmp([w[-1:] for w in LA], [w[-1:] for w in LB], lor, 'The rule holds in final syllables')


def CC4():
    r, p, nm = R.compare(LB, LA, lambda ws: lor(ws, set('iu')))
    return p, 'i/u are depleted after the e/o-taking consonants more than in Linear B', {'logOR_iu_LA': round(lor(LA, set('iu')), 3), 'logOR_iu_LB': round(lor(LB, set('iu')), 3), 'p': round(p, 4)}, {}


def nmi(ws):
    pairs = [(grid(x)[0], grid(x)[1]) for w in ws for x in w if grid(x) and grid(x)[0] and grid(x)[1] in 'eo']
    n = len(pairs)
    a, b, ab = Counter(x for x, _ in pairs), Counter(y for _, y in pairs), Counter(pairs)
    h = -sum(c / n * log(c / n) for c in b.values())
    return sum(c / n * log(c * n / (a[x] * b[y])) for (x, y), c in ab.items()) / h, n


def CC5():
    real, n = nmi(LA)
    null = []
    for _ in range(500):
        smp, k = [], 0
        while k < n:
            w = R.rng.choice(LB)
            smp.append(w)
            k += sum(1 for x in w if grid(x) and grid(x)[0] and grid(x)[1] in 'eo')
        null.append(nmi(smp)[0])
    p = R.pv_hi(null, real)
    return p, 'e versus o depends on the consonant more than in Linear B', {'nmi_LA': round(real, 3), 'nmi_LB_subsampled': round(sum(null) / len(null), 3), 'p': round(p, 4)}, {}


def CC6():
    stem = lambda ws: [w[:-1] for w in ws if len(w) >= 2]
    return cmp(stem(T.KN_N), stem(T.PY_N), lor, 'Knossos names (ending removed) show the rule more than Pylos names')


def CC7():
    kn = [w[:-1] for w in V.kn_only if T.CAT.get(w) in ('toponym', 'ethnic') and T.clean(w) and len(w) >= 3]
    py = [w[:-1] for w in V.py_only if T.CAT.get(w) in ('toponym', 'ethnic') and T.clean(w) and len(w) >= 3]
    return cmp(kn, py, lor, 'Cretan place names show the rule more than Pylos place names')


def CC8():
    return cmp(T.PRE, T.GRK, lor, 'Pre-Greek stems show the rule more than Greek stems')


def CC9():
    return cmp(R.G.SIG, LB, lor, 'The rule holds on SigLA\'s transcription')


def CC10():
    a, b = Z.eteo()
    return cmp(a, b, lor, 'Eteocretan shows the rule more than Greek')


def CC11():
    kh = D.site_words(lambda s: s == 'Khania')
    return cmp(kh, LB, lor, 'Khania\'s Linear A shows the rule')


if __name__ == '__main__':
    R.run('round40', 'the e/o rule with the refined consonant sets', __doc__, [CC1, CC2, CC4, CC5, CC6, CC7, CC8, CC9, CC10, CC11])
