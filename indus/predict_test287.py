"""Two-hundred-and-eighty-seventh registered prediction set (PREDICTIONS.md, RX1-RX4): decipherment loop 112, the
referent method's criteria calibrated by false-discovery rate. For each criterion (k objects, share s) the qualifying
units (texts, pairs) are counted on the real pictures and on 100 shuffles of the pictures within each pool; FDR = mean
shuffled count / real count. The loosest criterion with FDR <= 10% is chosen (largest token coverage among those), and
the Linear B control (set 235's four words) is re-run with it. Writes results/predict_test287.md."""
import rtools as R
import referents as X
from predict_test234 import lines
from predict_test235 import KEY
from progress import data

GRID = [(3, 0.8), (3, 0.67), (2, 1.0), (2, 0.67)]


def lb_qualify(ls, k, s):
    from collections import defaultdict
    occ = defaultdict(list)
    for ws, i in ls:
        for w in set(ws):
            occ[w].append(i)
    return {w: m for w, ii in occ.items() for m in [X.ok(ii, k, s)] if m}


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-eighty-seventh registered predictions: decipherment loop 112, referent criteria calibrated by false-discovery rate', 'predict_test287')
    DL, tr, te = data()
    P = X.pools(F, recs)
    res = {}
    for k, s in GRID:
        u = X.units(P, k, s)
        real = X.count(u)
        null = X.null_count(P, k, s)
        fdr = null / max(1, real)
        cov = X.coverage(DL, P, u)
        res[(k, s)] = (real, null, fdr, cov)
        rd.say('- k %d, s %.2f: %d units, shuffled mean %.1f, FDR %.1f%%, coverage %.2f%%.' % (k, s, real, null, 100 * fdr, 100 * cov))
    rd.say()
    base = res[(3, 0.8)]
    good = [c for c in GRID if res[c][2] <= 0.10]
    best = max(good, key=lambda c: (res[c][3], -GRID.index(c))) if good else None
    rd.rec('RX1', 'the current criterion (k 3, s 0.8) has FDR <= 10%', 'FDR %.1f%%' % (100 * base[2]), base[2] <= 0.10)
    rx2 = best is not None and best != (3, 0.8) and res[best][3] > base[3]
    rd.rec('RX2', 'a looser criterion with FDR <= 10% raises the coverage', 'chosen %s: coverage %.2f%% -> %.2f%%' % (best, 100 * base[3], 100 * res[best][3] if best else 0), rx2)
    q = lb_qualify(lines(), *(best or (3, 0.8)))
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rx3 = len(rec) >= 2 and not wrong
    rd.rec('RX3', 'Linear B with the chosen criterion: 2+ of the 4 control words recovered, none wrong', 'recovered %s; wrong %s' % (', '.join(rec) or 'none', ', '.join('%s -> %s' % (w, q[w]) for w in wrong) or 'none'), rx3)
    rd.rec('RX4', 'progress rule: RX2 and RX3 (the referent line uses the chosen criterion)', 'RX2 %s, RX3 %s' % (rx2, rx3), rx2 and rx3)
    rd.finish()


if __name__ == '__main__':
    main()
