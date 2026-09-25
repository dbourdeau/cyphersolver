"""Three-hundred-and-eleventh registered prediction set (PREDICTIONS.md, TP1-TP3): decipherment loop 136, two more
pictured pools for the referent method: tags (TAG and its subtypes) and the SEAL:C / SEAL:CY objects, each with set
307's configuration (C7) beside the two tablet pools. Combined FDR against 100 picture shuffles; coverage on the real
tokens. Writes results/predict_test311.md."""
import referents as X
import rtools as R
from predict_test200 import objects
from predict_test237 import merged
from predict_test254 import frag_objects
from predict_test304 import coverage, fdr
from predict_test307 import mid
from progress import data

EXTRA = {'tag': ('TAG',), 'sealc': ('SEAL:C', 'SEAL:CY')}


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-eleventh registered predictions: decipherment loop 136, tags and SEAL:C as referent pools', 'predict_test311')
    DL, tr, te = data()
    P = X.pools(F, recs)
    c0 = coverage(DL, P, mid(P))
    P2 = dict(P)
    for lab, types in EXTRA.items():
        clean = objects(F, recs, types)
        P2[lab] = (clean, merged(clean + frag_objects(types)))
        rd.say('- pool %s: %d objects.' % (lab, len(P2[lab][1])))
    u = mid(P2)
    f = fdr(P2, mid, 311)
    c1 = coverage(DL, P2, u)
    new = sum(len(v) for k, v in u.items() if k != 'texts' and (k[0].lstrip('F') in EXTRA))
    rd.say('- %d units (%d in the new pools), FDR %.1f%%, coverage %.2f%% -> %.2f%%.' % (X.count(u), new, 100 * f, 100 * c0, 100 * c1))
    rd.say()
    rd.rec('TP1', 'combined FDR <= 10%', '%.1f%%' % (100 * f), f <= 0.10)
    rd.rec('TP2', 'coverage rises above 2.28%', '%.2f%%' % (100 * c1), c1 > c0)
    rd.rec('TP3', 'progress rule: TP1 and TP2 (the new pools join)', 'TP1 %s, TP2 %s' % (f <= 0.10, c1 > c0), f <= 0.10 and c1 > c0)
    rd.finish()


if __name__ == '__main__':
    main()
