"""Two-hundred-and-eighty-first registered prediction set (PREDICTIONS.md, ED1-ED4): decipherment loop 106, edge doubles
as a role. Adjacent doubled pairs of a non-numeral sign in lines of 4+ signs: share standing at a line edge (first two
or last two positions) against the share of adjacent-pair positions that are edge positions (2 of n - 1 per line).
Writes results/predict_test281.md."""
from scipy.stats import binomtest

import rtools as R
from progress import data, roles
from signs import load


def edge_share(lines):
    k = n = 0
    exp = 0.0
    for t in lines:
        t = tuple(t)
        if len(t) < 4:
            continue
        for i in range(len(t) - 1):
            if t[i] == t[i + 1] and t[i] not in R.NUMS:
                n += 1
                k += i == 0 or i == len(t) - 2
                exp += 2 / (len(t) - 1)
    p0 = exp / max(1, n)
    p = binomtest(k, n, p0, alternative='greater').pvalue if n else 1.0
    return k, n, p0, p


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-eighty-first registered predictions: decipherment loop 106, edge doubles as a role', 'predict_test281')
    DL, tr, te = data()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    ra, rb = edge_share(DA), edge_share(DB)
    f = lambda r: '%d of %d doubles at an edge (%.0f%%) against %.0f%% expected, p = %.2g' % (r[0], r[1], 100 * r[0] / max(1, r[1]), 100 * r[2], r[3])
    rd.rec('ED1', 'A: doubled non-numeral pairs stand at a line edge more often than chance', f(ra), ra[3] < 0.05)
    rd.rec('ED2', 'B: the same', f(rb), rb[3] < 0.05)
    r0 = roles(DL, edges=True, head2=True)[0]
    r1 = roles(DL, edges=True, head2=True, dbl=True)[0]
    rd.rec('ED3', 'R rises with the edge-double role', 'R %.2f%% -> %.2f%%' % (100 * r0, 100 * r1), r1 > r0)
    ok = ra[3] < 0.05 and rb[3] < 0.05 and r1 > r0
    rd.rec('ED4', 'progress rule: ED1-ED3', 'ED1 %s, ED2 %s, ED3 %s' % (ra[3] < 0.05, rb[3] < 0.05, r1 > r0), ok)
    rd.finish()


if __name__ == '__main__':
    main()
