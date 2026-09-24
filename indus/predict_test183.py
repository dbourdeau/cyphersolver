"""Hundred-and-eighty-third registered prediction set (PREDICTIONS.md, DI1-DI8): decipherment loop 8, are the depiction
identifications coherent in shape (font renderings, set 137) and in use (context similarity, set 62)? Writes
results/predict_test183.md."""
import random
from collections import defaultdict
from itertools import combinations

import predict_test13 as T
import rtools as R
from noun_class import HUMAN
from predict_test137 import glyphs, iou
from predict_test182 import categories
from predict_test62 import sims
from signs import FISH

random.seed(233)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-eighty-third registered predictions: decipherment loop 8, are the depiction identifications coherent?', 'predict_test183')
    G = glyphs()
    allg = sorted(g for g in G if g.isdigit() and g not in R.NUMS)
    cat = categories()

    def shape(members, n=1000):
        m = [g for g in members if g in G]
        if len(m) < 3:
            return None, None, len(m)
        mm = sum(iou(G[a], G[b]) for a, b in combinations(m, 2)) / (len(m) * (len(m) - 1) / 2)
        ge = 0
        for _ in range(n):
            s = random.sample(allg, len(m))
            ge += sum(iou(G[a], G[b]) for a, b in combinations(s, 2)) / (len(s) * (len(s) - 1) / 2) >= mm
        return mm, (ge + 1) / (n + 1), len(m)
    tc, S, C = sims(A + B, 20)
    Sset = set(S)

    def use(members, n=1000):
        m = [g for g in members if g in Sset]
        if len(m) < 3:
            return None, None, len(m)
        mm = sum(C[(a, b)] for a, b in combinations(m, 2)) / (len(m) * (len(m) - 1) / 2)
        ge = 0
        for _ in range(n):
            s = random.sample(S, len(m))
            ge += sum(C[(a, b)] for a, b in combinations(s, 2)) / (len(s) * (len(s) - 1) / 2) >= mm
        return mm, (ge + 1) / (n + 1), len(m)
    fmt = lambda r: 'n %d, too few' % r[2] if r[0] is None else 'mean %.3f over %d signs; p = %.4f' % (r[0], r[2], r[1])
    ok = lambda r: r[0] is not None and r[1] < 0.05
    r1 = shape(HUMAN)
    rd.rec('DI1', 'human figures look alike', fmt(r1), ok(r1))
    extra = [g for g, c in cat.items() if c == 'A' and g not in HUMAN and g in G]
    hum = [g for g in HUMAN if g in G]
    if extra and hum:
        best = sum(max(iou(G[e], G[h]) for h in hum) for e in extra) / len(extra)
        rnd = []
        for _ in range(500):
            s = random.sample(allg, len(extra))
            rnd.append(sum(max(iou(G[e], G[h]) for h in hum) for e in s) / len(s))
        q = sum(x >= best for x in rnd)
        rd.rec('DI2', "Fairservis's other human signs resemble them", 'mean best IoU %.3f over %d signs; random %d of 500 as high' % (best, len(extra), q), q < 25)
    else:
        rd.rec('DI2', "Fairservis's other human signs resemble them", 'no such signs', False)
    tools = [g for g, c in cat.items() if c in ('H', 'I')]
    r3 = shape(tools)
    rd.rec('DI3', 'weapons and implements look alike', fmt(r3), ok(r3))
    r4 = shape(FISH)
    rd.rec('DI4', 'control: fish look alike', fmt(r4), ok(r4))
    r5 = use(HUMAN)
    rd.rec('DI5', 'human figures are used alike', fmt(r5), ok(r5))
    r6 = use(tools)
    rd.rec('DI6', 'weapons and implements are used alike', fmt(r6), ok(r6))
    byc = defaultdict(list)
    for g, c in cat.items():
        byc[c].append(g)
    pts = []
    for c, ms in byc.items():
        s_, u_ = shape(ms, n=200), use(ms, n=200)
        if s_[0] is not None and u_[0] is not None:
            pts.append((c, s_[0], u_[0]))
    rho = T.spearman([p[1] for p in pts], [p[2] for p in pts]) if len(pts) >= 3 else 0
    rd.rec('DI7', 'shape cohesion goes with use cohesion', 'categories %s; Spearman %.2f' % (', '.join('%s %.2f/%.2f' % p for p in pts), rho), rho > 0)
    r8 = use(FISH)
    rd.rec('DI8', 'control: fish are used alike', fmt(r8), ok(r8))
    rd.finish()


if __name__ == '__main__':
    main()
