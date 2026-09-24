"""Hundred-and-second registered prediction set (PREDICTIONS.md, SB1-SB20): shape blocks and what they do. Writes
results/predict_test102.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test81 import classes_of
from predict_test99 import roles
from signs import FISH

random.seed(122)


def blk(g):
    return int(g) // 100 if g.isdigit() else None


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    cat = R.cat_of()
    rd = R.Round('Hundred-and-second registered predictions: shape blocks and what they do', 'predict_test102')
    DL = sorted({tuple(t) for t in AB})
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    ok = lambda g: g not in R.NUMS and blk(g) is not None
    ro, c, ini, fin = roles([t for t in DL if len(t) >= 2])
    sg = [g for g in ro if ok(g)]
    rd.say('- signs with a role %d.' % len(sg))
    rd.say()
    rd.mi('SB1', 'the block sets the position', 'signs', [blk(g) for g in sg], [ro[g] for g in sg])
    tk = [(t, i) for t in DL for i in range(len(t)) if ok(t[i])]
    gen = lambda t: 'n' if R.name_of(list(t)) else ('f' if nonname(list(t)) else 'o')
    x = [(blk(t[i]), gen(t)) for t, i in tk if gen(t) != 'o']
    rd.mi('SB2', 'the block sets the genre', 'tokens', [a for a, _ in x], [b for _, b in x])
    rd.mi('SB3', 'the block sets counting', 'tokens', [blk(t[i]) for t, i in tk], [i > 0 and t[i - 1] in R.NUMS for t, i in tk])
    cl = classes_of(ns)
    ch = [h for h in cl if ok(h)]
    rd.mi('SB4', 'the block sets the class', 'classed heads', [blk(h) for h in ch], [cl[h] for h in ch])
    Fn = [r for r in F if r['type'] != 'TAB:C']
    ft = [(r['type'][:3], r['site'].strip(), g) for r in Fn for ln in r['seq'] for g in ln if ok(g)]
    st = [(blk(g), ty) for ty, s, g in ft if ty in ('SEA', 'TAB')]
    rd.mi('SB5', 'the block sets the medium', 'F tokens', [a for a, _ in st], [b for _, b in st])
    cs = [(blk(g), s) for ty, s, g in ft if s in ('Mohenjo-daro', 'Harappa')]
    rd.mi('SB6', 'the block sets the city', 'F tokens', [a for a, _ in cs], [b for _, b in cs])
    hb = Counter(blk(b[-1]) for b, e in T.names(AB) if b and ok(b[-1]))
    rd.thr('SB7', 'heads come from two blocks', 'two commonest blocks (%s)' % dict(hb.most_common(4)), sum(n for _, n in hb.most_common(2)), sum(hb.values()), 0.5)
    f2 = [g for g in sg if g in FISH]
    rd.thr('SB8', 'fish are medial', 'block-2 fish that are medial', sum(ro[g] == 'M' for g in f2), len(f2), 0.8)
    cnt = lambda t, i: i > 0 and t[i - 1] in R.NUMS
    rd.gtl('SB9', 'block 7 is counted', 'counted, block-7 tokens', [cnt(t, i) for t, i in tk if blk(t[i]) == 7], [cnt(t, i) for t, i in tk if blk(t[i]) != 7])
    rd.gtl('SB10', 'block 8 holds the ends', 'specialist, block-8 signs', [ro[g] != 'M' for g in sg if blk(g) == 8], [ro[g] != 'M' for g in sg if blk(g) != 8])
    bt = [(b, i) for b, e in T.names(AB) for i in range(len(b)) if ok(b[i])]
    rd.gtl('SB11', 'block 1 heads names', 'last body sign, block-1 tokens', [i == len(b) - 1 for b, i in bt if blk(b[i]) == 1], [i == len(b) - 1 for b, i in bt if blk(b[i]) != 1])
    same = lambda t: sum(1 for x, y in zip(t, t[1:]) if ok(x) and ok(y) and blk(x) == blk(y))
    obs = sum(map(same, DL))
    le = 0
    for _ in range(R.N // 10):
        k = 0
        for t in DL:
            s = list(t)
            random.shuffle(s)
            k += same(s)
        le += k <= obs
    p = (le + 1) / (R.N // 10 + 1)
    rd.rec('SB12', 'neighbours come from different blocks', 'same-block adjacent pairs %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    oh = [(b[0], b[-1]) for b, e in ns if len(b) >= 2 and ok(b[0]) and ok(b[-1])]
    hs = [h for _, h in oh]
    d = lambda hh: sum(blk(o) != blk(h) for (o, _), h in zip(oh, hh))
    obs = d(hs)
    ge = 0
    sh = hs[:]
    for _ in range(R.N):
        random.shuffle(sh)
        ge += d(sh) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('SB13', 'opener and head from different families', 'names %d; different blocks %d; p = %.4f' % (len(oh), obs, p), p < 0.05)
    he = [(blk(b[-1]), e) for b, e in ns if ok(b[-1])]
    rd.mi('SB14', 'the block sets the ending', 'distinct names', [a for a, _ in he], [e for _, e in he])
    rA = roles([t for t in sorted({tuple(t) for t in A}) if len(t) >= 2])[0]
    rB = roles([t for t in sorted({tuple(t) for t in B}) if len(t) >= 2])[0]

    def maj(r_):
        m = defaultdict(Counter)
        for g, x in r_.items():
            if ok(g):
                m[blk(g)][x] += 1
        return {k: v.most_common(1)[0][0] for k, v in m.items() if sum(v.values()) >= 5}
    ma, mb = maj(rA), maj(rB)
    bb = [k for k in ma if k in mb]
    rd.thr('SB15', 'block roles hold in B', 'blocks with the same majority role', sum(ma[k] == mb[k] for k in bb), len(bb), 0.8)
    cg = [g for g in sg if g in cat]
    rd.mi('SB16', 'the category sets the position', 'categorised signs', [cat[g] for g in cg], [ro[g] for g in cg])
    ct = [(cat[t[i]], cnt(t, i)) for t, i in tk if t[i] in cat]
    rd.mi('SB17', 'the category sets counting', 'tokens', [a for a, _ in ct], [b for _, b in ct])
    rd.gtl('SB18', 'block 3 is a formula block', 'formula, block-3 tokens', [gen(t) == 'f' for t, i in tk if blk(t[i]) == 3], [gen(t) == 'f' for t, i in tk if blk(t[i]) != 3])
    rd.gtl('SB19', 'block 5 heads more than block 3', 'last body sign, block 5', [i == len(b) - 1 for b, i in bt if blk(b[i]) == 5], [i == len(b) - 1 for b, i in bt if blk(b[i]) == 3])
    allg = [g for g in c if ok(g)]
    rd.rank('SB20', 'block 9 is rare', 'other against block-9 signs', [c[g] for g in allg if blk(g) != 9], [c[g] for g in allg if blk(g) == 9])
    rd.finish()


if __name__ == '__main__':
    main()
