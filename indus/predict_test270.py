"""Two-hundred-and-seventieth registered prediction set (PREDICTIONS.md, RH1-RH5): decipherment loop 95, head roles inside
the new frames. OPEN-PRONE lines (set 264: all lexical, opening-prone first sign, last sign heads a name) and BODY-400
lines (set 263: 3+ lexical signs + 400): is the last lexical sign head-class (H: heads 5+ A names, more often head than
modifier) more often than the signs before it (the opener excluded)? A and B. Writes results/predict_test270.md."""
from collections import Counter

from scipy.stats import fisher_exact

import rtools as R
from grammar import head_stats, heads_from, lexical
from progress import edge_sets
from signs import load


def frames(lines, openp, heads):
    op, bo = ([], []), ([], [])
    for t in lines:
        t = tuple(t)
        if len(t) >= 3 and all(lexical(g) for g in t) and t[0] in openp and t[-1] in heads:
            op[0].append(t[-1])
            op[1].extend(t[1:-1])
        if len(t) >= 4 and t[-1] == '400' and all(lexical(g) for g in t[:-1]):
            bo[0].append(t[-2])
            bo[1].extend(t[1:-2] if t[0] in openp else t[:-2])
    return op, bo


def test(frame, H):
    a, n1 = sum(g in H for g in frame[0]), len(frame[0])
    b, n2 = sum(g in H for g in frame[1]), len(frame[1])
    p = fisher_exact([[a, n1 - a], [b, n2 - b]], alternative='greater')[1] if n1 and n2 else 1.0
    return a, n1, b, n2, p


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-seventieth registered predictions: decipherment loop 95, head roles inside the new frames', 'predict_test270')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    hc, mc = head_stats(DA)
    H = {g for g in hc if hc[g] >= 5 and hc[g] > mc[g]}
    heads = heads_from(DA)
    endp, openp = edge_sets()
    res = {}
    for nm, L in (('A', DA), ('B', DB)):
        op, bo = frames(L, openp, heads)
        res[nm] = (test(op, H), test(bo, H))
        for lab, r in zip(('OPEN-PRONE', 'BODY-400'), res[nm]):
            rd.say('- %s %s: last sign head-class %d of %d; earlier %d of %d; p = %.2g.' % (nm, lab, *r))
    rd.say()
    f = lambda r: '%d/%d against %d/%d, p = %.2g' % r
    ok = {}
    for k, (lab, j) in enumerate((('OPEN-PRONE', 0), ('BODY-400', 1))):
        a, b = res['A'][j], res['B'][j]
        ok[lab] = a[4] < 0.05 and b[4] < 0.05
        rd.rec('RH%d' % (2 * k + 1), 'A %s: last sign head-class more often than earlier signs' % lab, f(a), a[4] < 0.05)
        rd.rec('RH%d' % (2 * k + 2), 'B %s: the same' % lab, f(b), b[4] < 0.05)
    rd.rec('RH5', 'progress rule: a frame holding on A and B gives its last sign the name-head role', ', '.join('%s %s' % kv for kv in ok.items()), any(ok.values()))
    rd.finish()


if __name__ == '__main__':
    main()
