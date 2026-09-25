"""Three-hundred-and-seventh registered prediction set (PREDICTIONS.md, MI1-MI2): decipherment loop 132, the strict-tier
unit kinds of sets 303-306 (single signs, family pairs / 3-sign runs / single signs / skip-pairs, skip-pairs) at an
intermediate criterion (3+ objects in 2+ texts, 67%+) instead of 80%+; pairs and 3-sign runs unchanged. Combined FDR
against 100 picture shuffles. Writes results/predict_test307.md."""
import rtools as R
import referents as X
from predict_test304 import coverage, fam, fdr
from predict_test306 import more
from progress import data

KK, SS = 3, 0.67


def mid(P):
    u = X.units(P, 2, 0.67, (2, 3))
    for lab, (clean, b) in P.items():
        u[(lab, 1)] = X.q_pairs(b, KK, SS, 1)
        u[(lab, -2)] = X.q_pairs(b, KK, SS, -2)
        fb = [(fam(t), m) for t, m in b]
        for n in (1, 2, 3, -2):
            u[('F' + lab, n)] = X.q_pairs(fb, KK, SS, n)
    return u


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-seventh registered predictions: decipherment loop 132, the strict-tier units at an intermediate criterion', 'predict_test307')
    DL, tr, te = data()
    P = X.pools(F, recs)
    c0 = coverage(DL, P, more(P))
    u = mid(P)
    f = fdr(P, mid, 307)
    c1 = coverage(DL, P, u)
    rd.say('- %d units, FDR %.1f%%, coverage %.2f%% -> %.2f%%.' % (X.count(u), 100 * f, 100 * c0, 100 * c1))
    rd.say()
    rd.rec('MI1', 'combined FDR <= 10% and coverage rises', 'FDR %.1f%%, %.2f%% -> %.2f%%' % (100 * f, 100 * c0, 100 * c1), f <= 0.10 and c1 > c0)
    rd.rec('MI2', 'progress rule: MI1 (the intermediate criterion replaces 80%+ for these kinds)', 'MI1 %s' % (f <= 0.10 and c1 > c0), f <= 0.10 and c1 > c0)
    rd.finish()


if __name__ == '__main__':
    main()
