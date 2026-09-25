"""Two-hundred-and-fifty-third registered prediction set (PREDICTIONS.md, DM1-DM6): decipherment loop 78, the main
findings re-tested on sample D (damaged texts' independent legible runs, damaged.py). Writes results/predict_test253.md."""
import math
import random
from collections import Counter

import rtools as R
from damaged import segments
from famlm import M3
from predict_test178 import depiction
from predict_test7 import fisher_less
from progress import CAGED, data
from scipy.stats import binomtest


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-fifty-third registered predictions: decipherment loop 78, the main findings on the damaged texts', 'predict_test253')
    D = segments()
    runs = [s['signs'] for s in D]
    rd.say('- D: %d runs, %d signs, %d objects.' % (len(runs), sum(map(len, runs)), len({s['sealid'] for s in D})))
    rd.say()
    DL, tr, te = data()
    m = M3(DL)
    bits = lambda t: [-math.log2(max(r['trik'], 1e-12)) for r in m.rows(t, True)[2:len(t)]]
    rnd = random.Random(253)
    better = n = 0
    for t in runs:
        if len(t) < 3:
            continue
        real = sum(bits(t)) / (len(t) - 2)
        sh = []
        for _ in range(20):
            u = tuple(rnd.sample(t, len(t)))
            sh.append(sum(bits(u)) / (len(u) - 2))
        n += 1
        better += real < sum(sh) / len(sh)
    p1 = binomtest(better, n, 0.5, alternative='greater').pvalue if n else 1
    rd.rec('DM1', 'order is predictable in D', 'real runs more predictable than their shuffles in %d of %d runs (3+ signs); sign test p = %.4g' % (better, n, p1), p1 < 0.05)
    nxt = [(t[i], t[i + 1]) for t in runs for i in range(len(t) - 1)]
    cg = [b in R.END for a, b in nxt if a in CAGED]
    rd.rec('DM2', 'caged signs do not take 740 / 520', '%d of %d caged signs followed by 740 / 520' % (sum(cg), len(cg)), len(cg) > 0 and sum(cg) / len(cg) <= 0.05)
    has_next = lambda S: [(i < len(t) - 1) for t in runs for i, g in enumerate(t) if g in S]
    s, p = has_next({'741', '742', '745'}), has_next({'740'})
    pv = fisher_less(sum(p), len(p) - sum(p), sum(s), len(s) - sum(s))
    rd.rec('DM3', 'stroked jars followed by more signs than 740', 'stroked %d of %d, plain %d of %d; p = %.4f' % (sum(s), len(s), sum(p), len(p), pv), pv < 0.05 and sum(s) / max(1, len(s)) > sum(p) / max(1, len(p)))
    dep = depiction()
    he = [(a, b) for a, b in nxt if b in R.END and dep.get(a)]
    f = [b == '520' for a, b in he if dep[a] == 'fish']
    o = [b == '520' for a, b in he if dep[a] != 'fish']
    pf = fisher_less(sum(o), len(o) - sum(o), sum(f), len(f) - sum(f))
    rd.rec('DM4', 'fish heads take 520 more', 'fish %d of %d, other heads %d of %d; p = %.4f' % (sum(f), len(f), sum(o), len(o), pf), pf < 0.05 and sum(f) / max(1, len(f)) > sum(o) / max(1, len(o)))

    def pre(rs):
        out = []
        for t in rs:
            i = next((i for i, g in enumerate(t) if g in R.NUMS), None)
            if i and t[i - 1] not in R.NUMS:
                out.append(t[i - 1])
        return out
    pc = pre(runs)
    top = lambda xs: sum(v for k, v in Counter(xs).most_common(10)) / max(1, len(xs))
    obs = top(pc)
    null = []
    for _ in range(1000):
        sh = []
        for t in runs:
            idx = [i for i, g in enumerate(t) if g not in R.NUMS]
            vals = [t[i] for i in idx]
            rnd.shuffle(vals)
            u = list(t)
            for i, v in zip(idx, vals):
                u[i] = v
            sh.append(u)
        null.append(top(pre(sh)))
    q95 = sorted(null)[949]
    rd.rec('DM5', 'the pre-count slot is concentrated', 'top-ten share %.1f%% of %d; shuffles 95th percentile %.1f%%' % (100 * obs, len(pc), 100 * q95), obs > q95)
    held = sum(1 for k, ok in rd.res if ok)
    rd.rec('DM6', 'progress rule (consistency evidence only)', '%d of 5 re-tests hold on D; no bench component moves' % held, False)
    rd.finish()


if __name__ == '__main__':
    main()
