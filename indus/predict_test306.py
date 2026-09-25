"""Three-hundred-and-sixth registered prediction set (PREDICTIONS.md, FS1-FS2): decipherment loop 131, family single
signs and family skip-pairs under the stricter criterion (3+ objects in 2+ texts, 80%+) added to set 305's referent
units. Combined FDR against 100 picture shuffles. Writes results/predict_test306.md."""
import rtools as R
import referents as X
from predict_test304 import coverage, fam, fdr
from predict_test305 import both
from progress import data


def more(P):
    u = both(P)
    for lab, (clean, b) in P.items():
        fb = [(fam(t), m) for t, m in b]
        for n in (1, -2):
            u[('F' + lab, n)] = X.q_pairs(fb, 3, 0.8, n)
    return u


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-sixth registered predictions: decipherment loop 131, family single signs and skip-pairs under the stricter criterion', 'predict_test306')
    DL, tr, te = data()
    P = X.pools(F, recs)
    c0 = coverage(DL, P, both(P))
    u = more(P)
    f = fdr(P, more, 306)
    c1 = coverage(DL, P, u)
    rd.say('- %d units, FDR %.1f%%, coverage %.2f%% -> %.2f%%.' % (X.count(u), 100 * f, 100 * c0, 100 * c1))
    rd.say()
    rd.rec('FS1', 'combined FDR <= 10% and coverage rises', 'FDR %.1f%%, %.2f%% -> %.2f%%' % (100 * f, 100 * c0, 100 * c1), f <= 0.10 and c1 > c0)
    rd.rec('FS2', 'progress rule: FS1 (family single signs and skip-pairs join)', 'FS1 %s' % (f <= 0.10 and c1 > c0), f <= 0.10 and c1 > c0)
    rd.finish()


if __name__ == '__main__':
    main()
