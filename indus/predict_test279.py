"""Two-hundred-and-seventy-ninth registered prediction set (PREDICTIONS.md, HU1-HU5): decipherment loop 104, the heading
unit. (1) The heading (817 / 820 / 861 + 2 / 60 / 1, set 161) is a two-sign unit, but only its first sign has a role;
on B, 817 / 820 / 861 opening a line of 3+ signs are followed by 2 / 60 / 1 in 80%+. (2) In HEADING-BODY lines (heading
+ lexical body, no ending; set 263) the last sign is head-class more often than the earlier body signs, A and B.
Writes results/predict_test279.md."""
from scipy.stats import fisher_exact

import rtools as R
from grammar import head_stats, lexical
from progress import data, roles
from signs import load


def hb(lines, H):
    last, early = [], []
    for t in lines:
        t = tuple(t)
        if len(t) >= 4 and t[0] in ('817', '820', '861') and t[1] in ('2', '60', '1') and all(lexical(g) for g in t[2:]):
            last.append(t[-1])
            early.extend(t[2:-1])
    a, b = sum(g in H for g in last), sum(g in H for g in early)
    p = fisher_exact([[a, len(last) - a], [b, len(early) - b]], alternative='greater')[1] if last and early else 1.0
    return a, len(last), b, len(early), p


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-seventy-ninth registered predictions: decipherment loop 104, the heading unit', 'predict_test279')
    DL, tr, te = data()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    op = [t for t in DB if len(t) >= 3 and t[0] in ('817', '820', '861')]
    k = sum(t[1] in ('2', '60', '1') for t in op)
    rd.rec('HU1', 'B: 817 / 820 / 861 opening a 3+ line are followed by 2 / 60 / 1 in 80%+', '%d of %d (%.0f%%)' % (k, len(op), 100 * k / max(1, len(op))), k >= 0.8 * len(op))
    hc, mc = head_stats(DA)
    H = {g for g in hc if hc[g] >= 5 and hc[g] > mc[g]}
    ra, rb = hb(DA, H), hb(DB, H)
    f = lambda r: '%d/%d against %d/%d, p = %.2g' % r
    rd.rec('HU2', 'A HEADING-BODY: the last sign is head-class more often than earlier body signs', f(ra), ra[4] < 0.05)
    rd.rec('HU3', 'B: the same', f(rb), rb[4] < 0.05)
    r0 = roles(DL, edges=True)[0]
    r1 = roles(DL, edges=True, head2=True)[0]
    rd.rec('HU4', 'progress rule (unit): HU1 holds and R rises with the second heading sign', 'R %.2f%% -> %.2f%%' % (100 * r0, 100 * r1), k >= 0.8 * len(op) and r1 > r0)
    rd.rec('HU5', 'progress rule (head): HU2 and HU3 hold', 'HU2 %s, HU3 %s' % (ra[4] < 0.05, rb[4] < 0.05), ra[4] < 0.05 and rb[4] < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
