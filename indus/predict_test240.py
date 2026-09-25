"""Two-hundred-and-fortieth registered prediction set (PREDICTIONS.md, GV1-GV3): decipherment loop 65, do pairs with a
grammatical sign go with more different pictures than pairs of two lexical signs? Writes results/predict_test240.md."""
from collections import defaultdict

import rtools as R
from predict_test103 import CL
from predict_test200 import objects
from progress import CAGED

GRAM = set(R.END) | set(CL) | CAGED | {'400', '90'}


def diversity(objs):
    occ = defaultdict(list)
    for t, m in objs:
        for p in {t[i:i + 2] for i in range(len(t) - 1)}:
            occ[p].append(m)
    g, l = [], []
    for p, ms in occ.items():
        if len(ms) >= 3:
            d = len(set(ms)) / len(ms)
            (g if any(x in GRAM or x in R.NUMS for x in p) else l).append(d)
    return g, l


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-fortieth registered predictions: decipherment loop 65, the pictures check the grammar', 'predict_test240')
    g1, l1 = diversity(objects(F, recs, ('TAB:C', 'TAB:I')))
    rd.rank('GV1', 'grammatical pairs more picture-diverse (individually made tablets)', 'distinct pictures per occurrence, grammatical against lexical pairs', g1, l1)
    g2, l2 = diversity(objects(F, recs, ('TAB:B',)))
    rd.rank('GV2', 'the same on moulded tablets', 'distinct pictures per occurrence, grammatical against lexical pairs (TAB:B)', g2, l2)
    import predict_test13 as T
    rd.rec('GV3', 'progress rule', 'see GV2', rd.res[-1][1])
    rd.finish()


if __name__ == '__main__':
    main()
