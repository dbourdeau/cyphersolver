"""Hundred-and-thirty-sixth registered prediction set (PREDICTIONS.md, WA1-WA10): the West Asian texts against the
later grammar. Writes results/predict_test136.md."""
from collections import Counter

import predict_test13 as T
import rtools as R
from gulf import IRAN_WEST, WEST
from predict_test61 import units
from predict_test81 import classes_of
from predict_test103 import CL
from predict_test125 import M2, fit, xent
from signs import FISH


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-thirty-sixth registered predictions: the West Asian texts against the later grammar', 'predict_test136')
    west = lambda r: recs[r['sealid']][2] in WEST or r['site'].strip() in IRAN_WEST
    W = [tuple(ln) for r in F if west(r) for ln in r['seq'] if len(ln) >= 2]
    home_objs = [r for r in F if r['type'] != 'TAB:C' and not west(r) and recs[r['sealid']][2] not in ('Other',)]
    H = sorted({tuple(ln) for r in home_objs for ln in r['seq'] if len(ln) >= 2})
    H28 = [t for t in H if 2 <= len(t) <= 8]
    rd.say('- West Asian lines %d (%s); home lines %d.' % (len(W), '; '.join(' '.join(t) for t in W), len(H)))
    rd.say()
    fill = lambda t: t[-1] in R.END or t[-1] in CL or (len(t) >= 2 and t[-1] in ('400', '90', '151') and t[-2] in R.END)
    rd.ltl('WA1', 'foreign names lack the ending', 'ending slot, West Asian', [fill(t) for t in W], [fill(t) for t in H28])
    rd.rec('WA2', 'no closers abroad', 'West Asian lines ending in a closer: %d' % sum(t[-1] in CL for t in W), sum(t[-1] in CL for t in W) == 0)
    hn = sorted({(b, e) for r in home_objs for b, e in R.names_in(r) if b})
    op = {b[0] for b, e in hn if len(b) >= 2}
    hd = {b[-1] for b, e in hn}
    rd.thr('WA3', 'foreign openers', 'West Asian first signs never home openers', sum(t[0] not in op for t in W), len(W), 0.3)
    last = [t[-2] if t[-1] in R.END else t[-1] for t in W]
    rd.thr('WA4', 'foreign heads', 'West Asian final signs that are home heads', sum(g in hd for g in last), len(last), 0.8, above=False)
    U = units(sorted({b for b, e in T.names(AB) if len(b) >= 2}))
    hu = lambda t: any(p in U for p in zip(t, t[1:]))
    rd.ltl('WA5', 'foreign names avoid the name units', 'unit, West Asian lines of 3+', [hu(t) for t in W if len(t) >= 3], [hu(t) for t in H if len(t) >= 3])
    w = fit(H, ['tri', 'pos', 'end'], True)
    m = M2(H)
    x = xent([r for t in W for r in m.rows(t, True)], w)
    rd.rec('WA6', 'foreign lines are unpredictable', 'West Asian %.2f bits per sign; threshold 6.5' % x, x >= 6.5)
    num = lambda t: any(g in R.NUMS for g in t)
    rd.ltl('WA7', 'foreign lines do not count', 'numeral, West Asian', [num(t) for t in W], [num(t) for t in H])
    fi = lambda t: any(g in FISH for g in t)
    a, c = [fi(t) for t in W], [fi(t) for t in H]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('WA8', 'foreign names use fish as often', 'fish, West Asian %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p >= 0.05)
    cl = classes_of(hn)
    e7 = [t for t in W if t[-1] == '740']
    rd.rec('WA9', 'the 740 lines use a 740 head', 'heads before 740: %s' % ', '.join('%s (%s)' % (t[-2], cl.get(t[-2], 'unclassed')) for t in e7),
           bool(e7) and all(cl.get(t[-2]) == '740' for t in e7))
    rd.rank('WA10', 'foreign lines are longer', 'West Asian against home', [len(t) for t in W], [len(t) for t in H])
    rd.finish()


if __name__ == '__main__':
    main()
