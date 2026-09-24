"""Forty-sixth registered prediction set (PREDICTIONS.md, RP1-RP10): replicating rounds 5-9 on held-out data.
Writes results/predict_test46.md."""
import random
from collections import Counter, defaultdict
from itertools import combinations

import predict_test13 as T
import rtools as R
from predict_test41 import dbl
from predict_test42 import binom_le, dom, pairs
from predict_test43 import ranks
from predict_test44 import nonname

random.seed(66)


def shuf(items, stat, n=R.N // 10, lower=False):
    obs = sum(map(stat, items))
    c = 0
    for _ in range(n):
        k = 0
        for t in items:
            s = list(t)
            random.shuffle(s)
            k += stat(s)
        c += (k <= obs) if lower else (k >= obs)
    return obs, (c + 1) / (n + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    head, attr = R.classes(A)
    rd = R.Round('Forty-sixth registered predictions: replicating rounds 5-9 on held-out data', 'predict_test46')
    oth = [r for r in F if r['site'].strip() not in ('Mohenjo-daro', 'Harappa')]
    OL = [ln for r in oth for ln in r['seq']]
    rd.say('- other-site objects %d, lines %d; B lines %d.' % (len(oth), len(OL), len(B)))
    rd.say()
    o, p = shuf(OL, lambda t: len(dbl(t)))
    rd.rec('RP1', 'doubling is deliberate (DB1)', 'other sites: doubles %d; p = %.4f (1,000 shuffles)' % (o, p), p < 0.05)
    bs = [b for r in oth for b, _ in R.names_in(r) if len(b) >= 3]
    rep = lambda b: any(b[i] == b[j] and b[i] not in R.NUMS for i in range(len(b)) for j in range(i + 2, len(b)))
    o, p = shuf(bs, rep, lower=True)
    rd.rec('RP2', 'names do not repeat a sign (DB6)', 'other sites: bodies %d; repeats %d; p = %.4f (1,000 shuffles)' % (
        len(bs), o, p), p < 0.05)
    nsB = set(T.names(B))
    d = dom(pairs(nsB, 3))
    idx = defaultdict(set)
    for p_ in d:
        idx[p_[0]].add(p_[1])
        idx[p_[1]].add(p_[0])
    tri = cyc = 0
    for x in sorted(idx):
        for y, z in combinations(sorted(idx[x]), 2):
            if not (x < y < z) or z not in idx[y]:
                continue
            tri += 1
            win = Counter(d[tuple(sorted(q))][0] for q in ((x, y), (x, z), (y, z)))
            cyc += max(win.values()) == 1
    p = binom_le(cyc, tri)
    rd.rec('RP3', 'the orders are transitive (OR2)', 'B: triples %d; cyclic %d (%.1f%%); p = %.4f' % (
        tri, cyc, 100 * cyc / max(1, tri), p), tri > 0 and cyc / tri < 0.25 and p < 0.05)
    tail = front = 0
    for b, e in nsB:
        if len(b) == 3:
            t_, h_ = (b[1:], e) in nsB, (b[:2], e) in nsB
            tail += t_ and not h_
            front += h_ and not t_
    p = R.binom_ge(tail, tail + front)
    rd.rec('RP4', 'names grow at the front (OR7)', 'B: tail %d, front %d; p = %.4f' % (tail, front, p), tail > front and p < 0.05)
    be = defaultdict(set)
    for b, e in nsB:
        be[e].add(b)
    fin = ini = 0
    for b, e in nsB:
        if len(b) >= 4:
            f_ = any(b[k:] in be[e] for k in range(1, len(b) - 1))
            i_ = any(b[:k] in be[e] for k in range(2, len(b)))
            fin += f_ and not i_
            ini += i_ and not f_
    p = R.binom_ge(fin, fin + ini)
    rd.rec('RP5', 'the name ends in a known name (OR8)', 'B: final %d, initial %d; p = %.4f' % (fin, ini, p), fin > ini and p < 0.05)
    rk = ranks(set(T.names(A)))
    cnt = Counter(T.names(B))
    inv = lambda b: any(x in rk and y in rk and rk[x] - rk[y] >= 0.2 for x, y in zip(b, b[1:]))
    rd.gtl('RP6', 'inversions are rare names (SK7)', 'B: attested once, bodies with an inversion',
           [cnt[nm] == 1 for nm in nsB if len(nm[0]) >= 2 and inv(nm[0])],
           [cnt[nm] == 1 for nm in nsB if len(nm[0]) >= 2 and not inv(nm[0])])
    nnB = [t for t in B if nonname(t)]
    nlB = [t for t in B if R.name_of(t)]
    rd.ltl('RP7', 'non-names are not names without the ending (NN1)', 'B: head-class last sign, non-name lines',
           [t[-1] in head for t in nnB], [R.name_of(t)[0][-1] in head for t in nlB if R.name_of(t)[0]])
    nnO = [t for t in OL if nonname(t)]
    nlO = [t for t in OL if R.name_of(t)]
    num = lambda t: any(g in R.NUMS for g in t)
    rd.gtl('RP8', 'non-names carry numbers (NN4)', 'other sites: numeral, non-name lines', [num(t) for t in nnO], [num(t) for t in nlO])
    rd.gtl('RP9', 'the number opens the formula (EM7)', 'other sites: numeral first, non-name lines with a numeral',
           [t[0] in R.NUMS for t in nnO if num(t)], [t[0] in R.NUMS for t in nlO if num(t)])
    rd.gtl('RP10', 'short formulas are counts (EM9)', 'B: numeral + sign, 2-sign non-name lines',
           [t[0] in R.NUMS and t[1] not in R.NUMS for t in nnB if len(t) == 2],
           [b[0] in R.NUMS and b[1] not in R.NUMS for b, _ in T.names(B) if len(b) == 2])
    rd.finish()


if __name__ == '__main__':
    main()
