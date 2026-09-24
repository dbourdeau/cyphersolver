"""Forty-second registered prediction set (PREDICTIONS.md, OR1-OR10): sign order inside the name. Writes
results/predict_test42.md. Bodies are counted as distinct (body, ending) names."""
import random
from collections import Counter, defaultdict
from itertools import combinations

import predict_test13 as T
import rtools as R

random.seed(62)


def pairs(ns, k=5):
    c = Counter()
    for b, _ in ns:
        seen = set()
        for i in range(len(b)):
            for j in range(i + 1, len(b)):
                if b[i] != b[j]:
                    seen.add((b[i], b[j]))
        c.update(seen)
    out = {}
    for x, y in {tuple(sorted(p)) for p in c}:
        n = c[(x, y)] + c[(y, x)]
        if n >= k:
            out[(x, y)] = (c[(x, y)], c[(y, x)])
    return out


def dom(pr):
    return {p: (p if a >= b else p[::-1]) for p, (a, b) in pr.items() if a != b}


def binom_le(k, n):
    from math import comb
    return sum(comb(n, i) * 0.25 ** i * 0.75 ** (n - i) for i in range(k + 1))


def relvar(bs):
    pos = defaultdict(list)
    for b in bs:
        for i, g in enumerate(b):
            pos[g].append(i / (len(b) - 1))
    tot = 0
    for v in pos.values():
        m = sum(v) / len(v)
        tot += sum((x - m) ** 2 for x in v)
    return tot


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Forty-second registered predictions: sign order inside the name', 'predict_test42')
    ns = set(T.names(AB))
    pr = pairs(ns)
    fixed = sum(max(a, b) / (a + b) >= 0.9 for a, b in pr.values())
    rd.thr('OR1', 'one order holds', 'pairs (5+ bodies) with one order in 90%+', fixed, len(pr), 0.7)
    d = dom(pr)
    signs = sorted({s for p in d for s in p})
    idx = defaultdict(set)
    for p in d:
        idx[p[0]].add(p[1])
        idx[p[1]].add(p[0])
    tri = cyc = 0
    for x in signs:
        for y, z in combinations(sorted(idx[x]), 2):
            if not (x < y < z) or z not in idx[y]:
                continue
            tri += 1
            win = Counter(d[tuple(sorted(p))][0] for p in ((x, y), (x, z), (y, z)))
            cyc += max(win.values()) == 1
    p = binom_le(cyc, tri)
    rd.rec('OR2', 'the orders are transitive', 'triples %d; cyclic %d (%.1f%%); p = %.4f against 25%%' % (
        tri, cyc, 100 * cyc / max(1, tri), p), tri > 0 and cyc / tri < 0.25 and p < 0.05)
    bs = [b for b, _ in ns if len(b) >= 2]
    obs = relvar(bs)
    le = 0
    for _ in range(R.N // 10):
        sh = []
        for b in bs:
            s = list(b)
            random.shuffle(s)
            sh.append(s)
        le += relvar(sh) <= obs
    p = (le + 1) / (R.N // 10 + 1)
    rd.rec('OR3', 'each sign has its place', 'bodies %d; summed within-sign variance %.1f; p = %.4f (1,000 shuffles)' % (
        len(bs), obs, p), p < 0.05)

    def agree(key, title, n1, n2, k):
        d1, d2 = dom(pairs(n1, k)), dom(pairs(n2, k))
        both = [p for p in d1 if p in d2]
        ag = sum(d1[p] == d2[p] for p in both)
        return ag, len(both)
    ag, n = agree('OR4', '', set(T.names(A)), set(T.names(B)), 5)
    rd.thr('OR4', 'the orders agree between transcriptions', 'pairs qualifying in A and B with the same order', ag, n, 0.85)
    fn = lambda site: {nm for r in F if r['site'].strip() == site for nm in R.names_in(r)}
    ag, n = agree('OR5', '', fn('Mohenjo-daro'), fn('Harappa'), 3)
    rd.thr('OR5', 'the orders agree between the cities', 'pairs qualifying at both with the same order', ag, n, 0.8)
    b2 = [b for b, _ in ns if len(b) >= 2]

    def heads_per_prefix(bl, lasts):
        g = defaultdict(set)
        cnt = Counter(tuple(b[:-1]) for b in bl)
        for b, l_ in zip(bl, lasts):
            if cnt[tuple(b[:-1])] >= 3:
                g[tuple(b[:-1])].add(l_)
        return sum(len(v) for v in g.values())
    lasts = [b[-1] for b in b2]
    obs = heads_per_prefix(b2, lasts)
    byl = defaultdict(list)
    for i, b in enumerate(b2):
        byl[len(b)].append(i)
    ge = 0
    for _ in range(R.N):
        sh = lasts[:]
        for ii in byl.values():
            vals = [lasts[i] for i in ii]
            random.shuffle(vals)
            for i, v in zip(ii, vals):
                sh[i] = v
        ge += heads_per_prefix(b2, sh) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('OR6', 'the prefix is a free unit', 'distinct last signs over recurrent prefixes %d; p = %.4f' % (obs, p), p < 0.05)
    tail = head_ = 0
    for b, e in ns:
        if len(b) != 3:
            continue
        t_, h_ = (b[1:], e) in ns, (b[:2], e) in ns
        tail += t_ and not h_
        head_ += h_ and not t_
    p = R.binom_ge(tail, tail + head_)
    rd.rec('OR7', 'names grow at the front', 'tail attested %d, front attested %d; p = %.4f' % (tail, head_, p),
           tail > head_ and p < 0.05)
    fin = ini = 0
    bodies_by_e = defaultdict(set)
    for b, e in ns:
        bodies_by_e[e].add(b)
    for b, e in ns:
        if len(b) < 4:
            continue
        f_ = any(b[k:] in bodies_by_e[e] for k in range(1, len(b) - 1))
        i_ = any(b[:k] in bodies_by_e[e] for k in range(2, len(b)))
        fin += f_ and not i_
        ini += i_ and not f_
    p = R.binom_ge(fin, fin + ini)
    rd.rec('OR8', 'the name ends in a known name', 'final segment only %d, initial segment only %d; p = %.4f' % (fin, ini, p),
           fin > ini and p < 0.05)
    b3 = [b for b in (b for b, _ in T.names(AB)) if len(b) >= 3]
    o1, p1 = R.mi_perm([b[-2] for b in b3], [b[-1] for b in b3])
    o2, p2 = R.mi_perm([b[0] for b in b3], [b[-1] for b in b3])
    rd.rec('OR9', 'the neighbour predicts the last sign', 'bodies %d; MI adjacent %.3f (p = %.4f), first %.3f (p = %.4f)' % (
        len(b3), o1, p1, o2, p2), o1 > o2 and p1 < 0.05)
    fr, bk = set(), set()
    for b, _ in ns:
        if len(b) >= 4:
            fr.add((b[0], b[1]))
            bk.add((b[-2], b[-1]))
    allp = set()
    for b, _ in ns:
        for i in range(len(b) - 1):
            allp.add((b[i], b[i + 1]))
    rev = lambda s: [(y, x) in allp and x != y for x, y in s]
    a, c = rev(fr), rev(bk)
    p = R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))
    rd.rec('OR10', 'order is looser at the front', 'reversible pairs, first two %s' % R.fl(sum(a), len(a), sum(c), len(c), p),
           p < 0.05 and sum(a) / len(a) > sum(c) / len(c))
    rd.finish()


if __name__ == '__main__':
    main()
