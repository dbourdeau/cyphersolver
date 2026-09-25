"""Three-hundred-and-twenty-eighth registered prediction set (PREDICTIONS.md, MP1-MP2): decipherment loop 153, the
base-rate referent configuration (set 325, alpha 0.01) with all pictured tablets in one pool (individually made and
moulded together; base rates over all; whole texts over the individually made clean objects as before). Combined FDR
against 100 picture shuffles; coverage on the real tokens. Writes results/predict_test328.md."""
import rtools as R
import referents as X
from predict_test237 import merged
from predict_test304 import coverage, fdr
from predict_test325 import build
from progress import data


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-twenty-eighth registered predictions: decipherment loop 153, one pool for all pictured tablets', 'predict_test328')
    DL, tr, te = data()
    P = X.pools(F, recs)
    c0 = coverage(DL, P, build(0.01)(P))
    clean = P['made'][0] + P['moulded'][0]
    both = merged(P['made'][1] + P['moulded'][1])
    P1 = {'made': (clean, both)}
    f = build(0.01)
    u = f(P1)
    fd = fdr(P1, f, 328)
    c1 = coverage(DL, P1, u)
    rd.say('- one pool of %d objects; %d units, FDR %.1f%%, coverage %.2f%% -> %.2f%%.' % (len(both), X.count(u), 100 * fd, 100 * c0, 100 * c1))
    rd.say()
    rd.rec('MP1', 'combined FDR <= 10% and coverage above 4.79%', 'FDR %.1f%%, %.2f%% -> %.2f%%' % (100 * fd, 100 * c0, 100 * c1), fd <= 0.10 and c1 > c0)
    rd.rec('MP2', 'progress rule: MP1 (one pool for all pictured tablets)', 'MP1 %s' % (fd <= 0.10 and c1 > c0), fd <= 0.10 and c1 > c0)
    rd.finish()


if __name__ == '__main__':
    main()
