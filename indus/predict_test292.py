"""Two-hundred-and-ninety-second registered prediction set (PREDICTIONS.md, SK1-SK3): decipherment loop 117, skip-pairs
(A _ B: two signs one position apart, any sign between) as referent units beside pairs and 3-sign runs, with set 287's
criterion and FDR rule. Writes results/predict_test292.md."""
import rtools as R
import referents as X
from progress import data

K, S = 2, 0.67


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-ninety-second registered predictions: decipherment loop 117, skip-pairs as referent units', 'predict_test292')
    DL, tr, te = data()
    P = X.pools(F, recs)
    res = {}
    for ns in ((2, 3), (2, 3, -2)):
        u = X.units(P, K, S, ns)
        real, null = X.count(u), X.null_count(P, K, S, ns=ns)
        res[ns] = (real, null, null / max(1, real), X.coverage(DL, P, u))
        rd.say('- units %s: %d, shuffled mean %.1f, FDR %.1f%%, coverage %.2f%%.' % (ns, real, null, 100 * res[ns][2], 100 * res[ns][3]))
    rd.say()
    a, b = res[(2, 3)], res[(2, 3, -2)]
    rd.rec('SK1', 'with skip-pairs FDR stays <= 10%', 'FDR %.1f%%' % (100 * b[2]), b[2] <= 0.10)
    rd.rec('SK2', 'coverage rises', '%.2f%% -> %.2f%%' % (100 * a[3], 100 * b[3]), b[3] > a[3])
    rd.rec('SK3', 'progress rule: SK1 and SK2 (skip-pairs join the referent units)', 'SK1 %s, SK2 %s' % (b[2] <= 0.10, b[3] > a[3]), b[2] <= 0.10 and b[3] > a[3])
    rd.finish()


if __name__ == '__main__':
    main()
