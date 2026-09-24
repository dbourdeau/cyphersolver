"""Hundred-and-forty-ninth registered prediction set (PREDICTIONS.md, CF1-CF5): a closer as a head and its ending in one
sign. Writes results/predict_test149.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test103 import CL

random.seed(169)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-forty-ninth registered predictions: a closer as a head and its ending in one sign', 'predict_test149')
    DL = sorted({tuple(t) for t in A + B})
    cst = defaultdict(set)   # closer -> stems
    for t in DL:
        u = t[:-1] if t and t[-1] == '400' else t
        if len(u) >= 2 and u[-1] in CL and not any(g in R.END for g in u):
            cst[u[-1]].add(u[:-1])
    x740 = defaultdict(set)  # stem -> X with stem + X + 740
    s520 = set()
    for b, e in {nm for nm in T.names(DL) if nm[0]}:
        if len(b) >= 2:
            if e == '740':
                x740[b[:-1]].add(b[-1])
            else:
                s520.add(b[:-1])
    cstems = set().union(*cst.values())
    a = [s in x740 for s in cstems]
    c = [s in x740 for s in s520]
    rd.gtl('CF1', 'closer stems also take X + 740', 'closer stems attested as stem + X + 740', a, c)
    both = [(C, s) for C in cst for s in cst[C] if s in x740]
    byc = defaultdict(list)
    for C, s in both:
        byc[C].append(s)

    def share(assign):
        top = tot = 0
        for C, ss in assign.items():
            if len(ss) >= 3:
                xc = Counter(x for s in ss for x in x740[s])
                best = xc.most_common(1)[0][0]
                top += sum(best in x740[s] for s in ss)
                tot += len(ss)
        return top / max(1, tot), tot
    obs, tot = share(byc)
    rd.say('- stems attested both ways: %d; by closer %s.' % (len(both), dict(Counter(C for C, s in both))))
    rd.say('- commonest X per closer: %s.' % '; '.join('%s: %s' % (C, Counter(x for s in ss for x in x740[s]).most_common(3)) for C, ss in byc.items() if len(ss) >= 3))
    rd.thr('CF2', 'a closer replaces one head', 'stems whose X set holds the closer\'s commonest X', round(obs * tot), tot, 0.5)
    labs = [C for C, s in both]
    ge = 0
    for _ in range(1000):
        random.shuffle(labs)
        d = defaultdict(list)
        for C, (_, s) in zip(labs, both):
            d[C].append(s)
        ge += share(d)[0] >= obs
    p = (ge + 1) / 1001
    rd.rec('CF3', 'the pairing beats chance', 'observed share %.3f; p = %.4f (1,000 permutations of closer labels)' % (obs, p), p < 0.05)
    bs = [s for C in ('154', '156') for s in byc.get(C, [])]
    rd.thr('CF4', 'the bearer closers replace 690', 'bearer-closer stems with X = 690 (%s)' % dict(Counter(x for s in bs for x in x740[s]).most_common(5)),
           sum('690' in x740[s] for s in bs), len(bs), 0.5)
    la = [len(s) for s in cstems]
    lb = [len(b) - 1 for b, e in {nm for nm in T.names(DL) if nm[0]} if e == '740' and len(b) >= 2]
    d1, p1 = R.rank_perm(la, lb)
    d2, p2 = R.rank_perm(lb, la)
    p = min(1, 2 * min(p1, p2))
    rd.rec('CF5', 'closer stems as long as 740 bodies minus the head', 'closer stems %d (mean %.2f), 740 bodies - 1 %d (mean %.2f); two-sided p = %.4f' % (
        len(la), sum(la) / len(la), len(lb), sum(lb) / len(lb), p), p >= 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
