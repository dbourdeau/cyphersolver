"""Six hypotheses: a check of the twin-derived candidate values of decipher6l.py L4 on independent words, and whether
the richer vowel set after R/T (decipher6j J3) appears in the other Minoan-related records.

Each has a prediction stated before the test ran and one primary test with its own null. Benjamini-Hochberg at
5% runs across the six.

M1  Candidate values from L4 (an unread sign's value taken from a 3+-sign twin word with one known sign in that
    slot), substituted into the sign's *other* words, turn them into attested Linear A or Linear B words more often
    than random values do.
M6  Knossos personal names show the R/T vowel-entropy gap more than Pylos personal names.
M7  Knossos-only place names and ethnics show it more than Pylos-only ones.
M8  Pre-Greek stems show it more than length-matched ordinary Greek stems.
M9  Eteocretan shows it more than Greek.
M10 Linear B words containing the same numbered signs become attested Linear B words under the candidate values
    more often than under random values.
"""
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher6l as L6  # noqa: E402

K, J, I, X, T, B, D, V = L6.K, L6.J, L6.I, L6.X, L6.T, L6.B, L6.D, L6.V
E = X.E
ROOT = B.ROOT
rng = L6.rng
REPS = 2000
out = D.out
out.clear()
record = D.record
grid = D.grid
LA, LB = X.LA, X.LB
gap = K.entropy_gap
VALUES = sorted({x for w in LA for x in w if grid(x)})


def candidates():
    known = defaultdict(set)
    for w in D.LA:
        for i in range(len(w)):
            if grid(w[i]):
                known[(len(w), i, w[:i] + w[i + 1:])].add(w[i])
    cand = {}
    for w in D.LA:
        ur = [i for i, x in enumerate(w) if D.UNREAD.match(x)]
        if len(w) >= 3 and len(ur) == 1:
            i = ur[0]
            tw = known.get((len(w), i, w[:i] + w[i + 1:]), set())
            if len(tw) == 1:
                cand.setdefault(w[i], (next(iter(tw)), w))
    return cand


CAND = candidates()
TARGET = set(D.LA) | set(B.LB_SITES)


def substituted_hits(sign, value, words, source):
    hits = []
    for w in words:
        if sign in w and w != source:
            nw = tuple(value if x == sign else x for x in w)
            if not any(D.UNREAD.match(x) or x.startswith('*') for x in nw) and nw in TARGET:
                hits.append('-'.join(nw))
    return hits


def M1():
    real_hits = {s: substituted_hits(s, v, D.LA, src) for s, (v, src) in CAND.items()}
    real = sum(len(h) for h in real_hits.values())
    null = []
    for _ in range(REPS):
        null.append(sum(len(substituted_hits(s, rng.choice(VALUES), D.LA, src)) for s, (v, src) in CAND.items()))
    p = B.pv(null, real)
    record('M1 twin values on other words', 'Twin-derived values turn the signs\' other words into attested words more than random values',
           {'hits': real, 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4), 'signs': len(CAND)},
           {'candidates (sign: value from twin)': {s: f"{v} (from {'-'.join(src).upper()})" for s, (v, src) in CAND.items()},
            'hits': {s: h for s, h in real_hits.items() if h}})
    return p


def M10():
    lb_words = [w for w in B.LB_SITES if any(x.startswith('*') for x in w)]
    lb_cand = {s.lower().lstrip('*'): v for s, (v, _) in CAND.items()}

    def hits(assign):
        n = 0
        for w in lb_words:
            nw = tuple(assign.get(x.lstrip('*'), x) if x.startswith('*') else x for x in w)
            if nw != w and not any(x.startswith('*') for x in nw) and nw in B.LB_SITES:
                n += 1
        return n
    shared = {k: v for k, v in lb_cand.items() if any(('*' + k) in w for w in lb_words)}
    real = hits(shared)
    null = [hits({k: rng.choice(VALUES) for k in shared}) for _ in range(REPS)]
    p = B.pv(null, real)
    record('M10 twin values in Linear B', 'Linear B words with the same numbered signs become attested words under the candidate values',
           {'hits': real, 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4), 'shared_signs': sorted(shared)}, {})
    return p


def gap_test(a, b, key, text):
    real, p, nm = T.label_perm(lambda x, y: gap(x) - gap(y), a, b, reps=REPS)
    record(key, text, {'gap_target': round(gap(a), 3), 'gap_comparison': round(gap(b), 3), 'p': round(p, 4), 'n': [len(a), len(b)]},
           {'Linear A gap': round(gap(LA), 3)})
    return p


def M6():
    return gap_test(T.KN_N, T.PY_N, 'M6 R/T vowels in Knossos names', 'Knossos names show the R/T vowel-entropy gap more than Pylos names')


def M7():
    kn = [w for w in V.kn_only if T.CAT.get(w) in ('toponym', 'ethnic') and T.clean(w)]
    py = [w for w in V.py_only if T.CAT.get(w) in ('toponym', 'ethnic') and T.clean(w)]
    return gap_test(kn, py, 'M7 R/T vowels in Cretan place names', 'Knossos-only place names show the gap more than Pylos-only ones')


def M8():
    return gap_test(T.PRE, T.GRK, 'M8 R/T vowels in Pre-Greek', 'Pre-Greek stems show the gap more than ordinary Greek stems')


def M9():
    ete = []
    for text in E.ET.ETEOCRETAN.values():
        for chunk in text.split():
            for piece in chunk.split('|'):
                ete += E.ET.stretches(piece)
    gre = []
    for text in (E.ET.GREEK, E.ET.HOMER):
        gre += [s for w in text.split() for s in E.ET.greek_stretches(w)]
    return gap_test(E.spelled(ete), E.spelled(gre), 'M9 R/T vowels in Eteocretan', 'Eteocretan shows the gap more than Greek')


TESTS = [M1, M6, M7, M8, M9, M10]


def main():
    ps = {}
    for fn in TESTS:
        try:
            ps[fn.__name__] = fn()
        except Exception as ex:
            import traceback
            traceback.print_exc()
            out[fn.__name__] = {'error': str(ex)}
    tested = sorted([(p, k) for k, p in ps.items() if p is not None])
    m, cut = len(tested), 0
    for i, (p, k) in enumerate(tested, 1):
        if p <= 0.05 * i / m:
            cut = i
    supported = [k for _, k in tested[:cut]]
    res = {'method': __doc__.strip(), 'primary_p': ps, 'bh_supported': supported, 'details': out}
    (ROOT / 'reading/decipher6m_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
