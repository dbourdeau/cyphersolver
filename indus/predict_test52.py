"""Fifty-second registered prediction set (PREDICTIONS.md, PO1-PO10): where the order is free. Writes
results/predict_test52.md."""
import math
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test42 import dom, pairs
from predict_test43 import ranks, sp_perm
from signs import FISH

random.seed(72)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    cat = R.cat_of()
    rd = R.Round('Fifty-second registered predictions: where the order is free', 'predict_test52')
    nsA, nsB, ns = set(T.names(A)), set(T.names(B)), set(T.names(AB))
    rk = ranks(nsA)
    srt = sorted(rk, key=lambda g: rk[g])
    ter = {g: 3 * i // len(srt) for i, g in enumerate(srt)}
    bp = [(x, y) for b, _ in nsB for x, y in zip(b, b[1:]) if x in rk and y in rk and rk[x] != rk[y]]
    fol = lambda x, y: rk[x] < rk[y]
    rd.gtl('PO1', 'order is fixed between slots', 'following the rank, cross-tercile pairs',
           [fol(x, y) for x, y in bp if ter[x] != ter[y]], [fol(x, y) for x, y in bp if ter[x] == ter[y]])
    e0 = [fol(x, y) for x, y in bp if ter[x] == ter[y] == 0]
    k, n = sum(e0), len(e0)
    p = min(1, 2 * min(R.binom_ge(k, n), R.binom_ge(n - k, n)))
    rd.rec('PO2', 'the early slot is free', 'early-tercile pairs following the rank %d of %d; two-sided p = %.4f' % (k, n, p), n > 0 and p >= 0.05)
    adj = defaultdict(list)
    for b, e in ns:
        for x, y in zip(b, b[1:]):
            if x != y:
                adj[(x, y)].append((b, e))
    rev = {tuple(sorted(p_)) for p_ in adj if p_[::-1] in adj}
    rd.say('- reversible pairs %d.' % len(rev))
    rd.thr('PO3', 'numbers float', 'reversible pairs with a numeral', sum(x in R.NUMS or y in R.NUMS for x, y in rev), len(rev), 0.3)
    same = lambda x, y: x in cat and y in cat and cat[x] == cat[y]
    nonrev = {tuple(sorted(p_)) for p_ in adj} - rev
    rd.gtl('PO4', 'reversible pairs are alike', 'same category, reversible pairs', [same(x, y) for x, y in rev], [same(x, y) for x, y in nonrev])
    bl = sorted(ns)
    endi = {nm: i for i, nm in enumerate(bl)}
    ends = [e for _, e in bl]

    def dis(lab):
        k_ = 0
        for x, y in rev:
            a = {lab[endi[nm]] for nm in adj[(x, y)]}
            b = {lab[endi[nm]] for nm in adj[(y, x)]}
            k_ += not (a & b)
        return k_
    obs = dis(ends)
    ee = ends[:]
    ge = 0
    for _ in range(R.N):
        random.shuffle(ee)
        ge += dis(ee) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('PO5', 'the ending sets the order', 'reversible pairs with disjoint endings %d of %d; p = %.4f' % (obs, len(rev), p), p < 0.05)
    fn = [(nm, r['site'].strip()) for r in F if r['site'].strip() in ('Mohenjo-daro', 'Harappa') for nm in R.names_in(r)]
    sites = [s for _, s in fn]

    def dis2(ss):
        g = defaultdict(set)
        for (nm, _), s in zip(fn, ss):
            for x, y in zip(nm[0], nm[0][1:]):
                g[(x, y)].add(s)
        return sum(1 for x, y in rev if g[(x, y)] and g[(y, x)] and not (g[(x, y)] & g[(y, x)])), \
            sum(1 for x, y in rev if g[(x, y)] and g[(y, x)])
    obs, nn = dis2(sites)
    ss = sites[:]
    ge = 0
    for _ in range(R.N // 10):
        random.shuffle(ss)
        ge += dis2(ss)[0] >= obs
    p = (ge + 1) / (R.N // 10 + 1)
    rd.rec('PO6', 'each city has its order', 'reversible pairs seen both ways in F %d; orders in different cities %d; p = %.4f (1,000 shuffles)' % (
        nn, obs, p), p < 0.05)
    pos = defaultdict(list)
    for b, _ in ns:
        if len(b) >= 2:
            for i, g in enumerate(b):
                pos[g].append(i / (len(b) - 1))
    gs = [g for g in pos if len(pos[g]) >= 5]
    sd = lambda v: math.sqrt(sum((x - sum(v) / len(v)) ** 2 for x in v) / len(v))
    o, p = sp_perm([len(pos[g]) for g in gs], [sd(pos[g]) for g in gs])
    rd.rec('PO7', 'frequent signs move', 'signs %d; Spearman %.3f; p = %.4f' % (len(gs), o, p), o > 0 and p < 0.05)
    rkAB = ranks(ns)
    inv = lambda b: any(x in rkAB and y in rkAB and rkAB[x] - rkAB[y] >= 0.2 for x, y in zip(b, b[1:]))
    rd.rank('PO8', 'inversions are in long names', 'with against without an inversion',
            [len(b) for b, _ in ns if len(b) >= 2 and inv(b)], [len(b) for b, _ in ns if len(b) >= 2 and not inv(b)])
    ip = [(x, y) for b, _ in ns for x, y in zip(b, b[1:]) if x in rkAB and y in rkAB and rkAB[x] - rkAB[y] >= 0.2]
    rd.thr('PO9', 'inversions involve numbers or fish', 'inverted pairs with a numeral or fish sign',
           sum(any(g in R.NUMS or g in FISH for g in pr) for pr in ip), len(ip), 0.4)
    dA = dom(pairs(nsA, 3))
    pw = sc = 0
    for x, y in bp:
        key = tuple(sorted((x, y)))
        if key not in dA:
            continue
        a_ = dA[key] == (x, y)
        b_ = fol(x, y)
        pw += a_ and not b_
        sc += b_ and not a_
    p = R.binom_ge(pw, pw + sc)
    rd.rec('PO10', 'pairs beat the rank', 'discordant: pairwise right %d, rank right %d; p = %.4f' % (pw, sc, p), pw > sc and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
