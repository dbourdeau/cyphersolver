"""Three-hundred-and-fifth registered prediction set (PREDICTIONS.md, SB1-SB2): decipherment loop 130, strict skip-pairs
added to set 304's referent units (which include the strict family units). Combined FDR against 100 picture shuffles.
Writes results/predict_test305.md."""
import rtools as R
import referents as X
from predict_test304 import coverage, fdr, with_fam
from progress import data


def both(P):
    u = with_fam(P)
    for lab, (clean, b) in P.items():
        u[(lab, -2)] = X.q_pairs(b, 3, 0.8, -2)
    return u


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-fifth registered predictions: decipherment loop 130, strict skip-pairs with the family units', 'predict_test305')
    DL, tr, te = data()
    P = X.pools(F, recs)
    c0 = coverage(DL, P, with_fam(P))
    u = both(P)
    f = fdr(P, both, 305)
    c1 = coverage(DL, P, u)
    rd.say('- %d units, FDR %.1f%%, coverage %.2f%% -> %.2f%%.' % (X.count(u), 100 * f, 100 * c0, 100 * c1))
    rd.say()
    rd.rec('SB1', 'combined FDR <= 10% and coverage rises', 'FDR %.1f%%, %.2f%% -> %.2f%%' % (100 * f, 100 * c0, 100 * c1), f <= 0.10 and c1 > c0)
    rd.rec('SB2', 'progress rule: SB1 (strict skip-pairs join)', 'SB1 %s' % (f <= 0.10 and c1 > c0), f <= 0.10 and c1 > c0)
    rd.finish()


if __name__ == '__main__':
    main()
