"""Round 42 (second loop, round 4 of 10): do Knossos names share the Linear A habits found in this loop?

All comparisons are Knossos-only against Pylos-only Linear B words; names exclude words with undeciphered signs
unless stated. Stems = final syllable removed.

EE1  Knossos names repeat the consonant of neighbouring syllables more often than Pylos names.
EE2  Knossos names begin with a J-row sign more often than Pylos names.
EE3  Knossos personal names contain undeciphered signs more often than Pylos personal names.
EE4  Knossos names contain special signs (ra2, ra3, pu2, ta2, a2, a3, au, ro2, nwa, pte) more often.
EE5  Knossos place names repeat the consonant of neighbouring syllables more often than Pylos place names.
EE6  Knossos names end in -ti more often than Pylos names.
EE7  Control: Knossos common words repeat neighbouring consonants more often than Pylos common words.
EE8  Knossos names contain a Q-row sign (anywhere) more often than Pylos names.
EE9  Knossos names contain a Z-row sign more often than Pylos names.
EE10 Knossos name stems end on a narrower set of consonants relative to their initials than Pylos name stems.
"""
from collections import Counter
from math import log
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round29 as P  # noqa: E402
import round39 as BB  # noqa: E402

B, T, V = R.B, R.T, R.V
cons = P.cons
KN, PY = T.KN_N, T.PY_N
SPECIAL = {'ra2', 'ra3', 'pu2', 'ta2', 'a2', 'a3', 'au', 'ro2', 'nwa', 'pte'}
rep = lambda ws: sum(1 for w in ws for i in range(len(w) - 1) if cons(w[i]) and cons(w[i]) == cons(w[i + 1])) / max(1, sum(len(w) - 1 for w in ws))
share = lambda pred: (lambda ws: sum(1 for w in ws if pred(w)) / max(1, len(ws)))


def cmp(a, b, f, text, lower=False):
    r, p, nm = R.compare(a, b, f, lower=lower)
    return p, text, {'KN': round(f(a), 4), 'PY': round(f(b), 4), 'p': round(p, 4), 'n': [len(a), len(b)]}, {}


def EE1():
    return cmp(KN, PY, rep, 'Knossos names repeat neighbouring consonants more often')


def EE2():
    return cmp(KN, PY, share(lambda w: cons(w[0]) == 'j'), 'Knossos names begin with J more often')


def EE3():
    kn = [w for w in V.kn_only if T.CAT.get(w) == 'anthroponym']
    py = [w for w in V.py_only if T.CAT.get(w) == 'anthroponym']
    return cmp(kn, py, share(lambda w: any(x.startswith('*') for x in w)), 'Knossos names contain undeciphered signs more often')


def EE4():
    return cmp(KN, PY, share(lambda w: any(x in SPECIAL for x in w)), 'Knossos names contain special signs more often')


def topo(site_only):
    return [w for w in site_only if T.CAT.get(w) in ('toponym', 'ethnic') and T.clean(w) and len(w) >= 2]


def EE5():
    return cmp(topo(V.kn_only), topo(V.py_only), rep, 'Knossos place names repeat neighbouring consonants more often')


def EE6():
    return cmp(KN, PY, share(lambda w: w[-1] == 'ti'), 'Knossos names end in -ti more often')


def EE7():
    kc = [w for w in V.kn_only if T.CAT.get(w) == 'other' and T.clean(w) and len(w) >= 2]
    pc = [w for w in V.py_only if T.CAT.get(w) == 'other' and T.clean(w) and len(w) >= 2]
    return cmp(kc, pc, rep, 'Knossos common words repeat neighbouring consonants more often (control)')


def EE8():
    return cmp(KN, PY, share(lambda w: any(cons(x) == 'q' for x in w)), 'Knossos names contain Q-row signs more often')


def EE9():
    return cmp(KN, PY, share(lambda w: any(cons(x) == 'z' for x in w)), 'Knossos names contain Z-row signs more often')


def EE10():
    stems = lambda ws: [w[:-1] for w in ws if len(w) >= 3]
    f = lambda ws: BB.ent(BB.dist(stems(ws), -1)) - BB.ent(BB.dist(stems(ws), 0))
    return cmp(KN, PY, f, 'Knossos name stems end on a narrower set of consonants', lower=True)


if __name__ == '__main__':
    R.run('round42', 'Linear A habits in Knossos names', __doc__, [EE1, EE2, EE3, EE4, EE5, EE6, EE7, EE8, EE9, EE10])
