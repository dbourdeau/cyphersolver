"""Three-hundred-and-twenty-ninth registered prediction set (PREDICTIONS.md, SP1-SP3): decipherment loop 154, seals and
tags in the one pool. The base-rate configuration (set 325, alpha 0.01) on one pool of all pictured tablets (set 328)
plus pictured seals (SEAL:S, SEAL:R, SEAL, SEAL:C, SEAL:CY) and tags (TAG and subtypes), fragments included, part-texts
merged; the base-rate test makes a unit for the default bull need a share well above the bull's own. Combined FDR
against 100 picture shuffles; coverage on the real tokens of all these objects. Writes results/predict_test329.md."""
import rtools as R
import referents as X
from predict_test200 import objects
from predict_test237 import merged
from predict_test254 import frag_objects
from predict_test304 import coverage, fdr
from predict_test325 import build
from progress import data

TYPES = ('SEAL:S', 'SEAL:R', 'SEAL', 'SEAL:C', 'SEAL:CY', 'TAG')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-twenty-ninth registered predictions: decipherment loop 154, seals and tags in the one pool', 'predict_test329')
    DL, tr, te = data()
    P = X.pools(F, recs)
    clean = P['made'][0] + P['moulded'][0]
    base = merged(P['made'][1] + P['moulded'][1])
    P1 = {'made': (clean, base)}
    f = build(0.01)
    c0 = coverage(DL, P1, f(P1))
    sc = objects(F, recs, TYPES)
    P2 = {'made': (clean + sc, merged(P['made'][1] + P['moulded'][1] + sc + frag_objects(TYPES)))}
    u = f(P2)
    fd = fdr(P2, f, 329)
    c1 = coverage(DL, P2, u)
    rd.say('- objects %d -> %d; %d units, FDR %.1f%%, coverage %.2f%% -> %.2f%%.' % (len(base), len(P2['made'][1]), X.count(u), 100 * fd, 100 * c0, 100 * c1))
    rd.say()
    rd.rec('SP1', 'combined FDR <= 10%', '%.1f%%' % (100 * fd), fd <= 0.10)
    rd.rec('SP2', 'coverage rises above 5.43%', '%.2f%%' % (100 * c1), c1 > c0)
    rd.rec('SP3', 'progress rule: SP1 and SP2 (seals and tags join the referent pool)', 'SP1 %s, SP2 %s' % (fd <= 0.10, c1 > c0), fd <= 0.10 and c1 > c0)
    rd.finish()


if __name__ == '__main__':
    main()
