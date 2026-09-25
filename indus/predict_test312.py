"""Three-hundred-and-twelfth registered prediction set (PREDICTIONS.md, F41-F42): decipherment loop 137, 4-sign runs
(3+ objects in 2+ texts, 67%+) added to set 307's referent units. Combined FDR against 100 picture shuffles.
Writes results/predict_test312.md."""
import rtools as R
import referents as X
from predict_test304 import coverage, fdr
from predict_test307 import mid
from progress import data


def plus4(P):
    u = mid(P)
    for lab, (clean, b) in P.items():
        u[(lab, 4)] = X.q_pairs(b, 3, 0.67, 4)
    return u


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-twelfth registered predictions: decipherment loop 137, 4-sign runs as referent units', 'predict_test312')
    DL, tr, te = data()
    P = X.pools(F, recs)
    c0 = coverage(DL, P, mid(P))
    u = plus4(P)
    f = fdr(P, plus4, 312)
    c1 = coverage(DL, P, u)
    rd.say('- %d units, FDR %.1f%%, coverage %.2f%% -> %.2f%%.' % (X.count(u), 100 * f, 100 * c0, 100 * c1))
    rd.say()
    rd.rec('F41', 'combined FDR <= 10% and coverage rises', 'FDR %.1f%%, %.2f%% -> %.2f%%' % (100 * f, 100 * c0, 100 * c1), f <= 0.10 and c1 > c0)
    rd.rec('F42', 'progress rule: F41 (4-sign runs join)', 'F41 %s' % (f <= 0.10 and c1 > c0), f <= 0.10 and c1 > c0)
    rd.finish()


if __name__ == '__main__':
    main()
