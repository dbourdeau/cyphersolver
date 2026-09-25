"""Two-hundred-and-eighty-eighth registered prediction set (PREDICTIONS.md, RN1-RN4): decipherment loop 113, single signs
and 3-sign runs as referent units beside pairs, with set 287's criterion (k 2, s 0.67) and its false-discovery rule.
Writes results/predict_test288.md."""
import rtools as R
import referents as X
from progress import data

K, S = 2, 0.67
SETS = [(2,), (1, 2), (2, 3), (1, 2, 3)]


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-eighty-eighth registered predictions: decipherment loop 113, single signs and 3-sign runs as referent units', 'predict_test288')
    DL, tr, te = data()
    P = X.pools(F, recs)
    res = {}
    for ns in SETS:
        u = X.units(P, K, S, ns)
        real = X.count(u)
        null = X.null_count(P, K, S, ns=ns)
        res[ns] = (real, null, null / max(1, real), X.coverage(DL, P, u), u)
        rd.say('- units %s: %d, shuffled mean %.1f, FDR %.1f%%, coverage %.2f%%.' % (ns, real, null, 100 * null / max(1, real), 100 * res[ns][3]))
    u1 = res[(1, 2)][4]
    singles = sorted(((key[0], g[0], m) for key, qq in u1.items() if key != 'texts' and key[1] == 1 for g, m in qq.items()))
    rd.say('- single-sign units: %s.' % ('; '.join('%s %s -> %s' % x for x in singles) or 'none'))
    rd.say()
    b = res[(2,)]
    ok1 = res[(1, 2)][2] <= 0.10 and res[(1, 2)][3] > b[3]
    ok2 = res[(2, 3)][2] <= 0.10 and res[(2, 3)][3] > b[3]
    rd.rec('RN1', 'single signs added: FDR <= 10% and coverage rises', 'FDR %.1f%%, coverage %.2f%% -> %.2f%%' % (100 * res[(1, 2)][2], 100 * b[3], 100 * res[(1, 2)][3]), ok1)
    rd.rec('RN2', '3-sign runs added: FDR <= 10% and coverage rises', 'FDR %.1f%%, coverage %.2f%% -> %.2f%%' % (100 * res[(2, 3)][2], 100 * b[3], 100 * res[(2, 3)][3]), ok2)
    good = [ns for ns in SETS if res[ns][2] <= 0.10]
    best = max(good, key=lambda ns: (res[ns][3], -len(ns)))
    rd.rec('RN3', 'the best unit set with FDR <= 10% beats pairs alone', 'chosen %s: %.2f%%' % (best, 100 * res[best][3]), best != (2,) and res[best][3] > b[3])
    rd.rec('RN4', 'progress rule: RN3 (the referent line uses the chosen unit set)', 'RN3 %s' % (best != (2,) and res[best][3] > b[3]), best != (2,) and res[best][3] > b[3])
    rd.finish()


if __name__ == '__main__':
    main()
