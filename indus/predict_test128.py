"""Hundred-and-twenty-eighth registered prediction set (PREDICTIONS.md, FA1-FA10): forbidden pairs and a family grammar.
Writes results/predict_test128.md."""
import math
import random
from collections import Counter

import rtools as R
from predict_test102 import blk

random.seed(148)
HEAD = ('817', '820', '861')
SUF = ('400', '90', '151')


def adj(lines):
    return Counter(p for t in lines for p in zip(t, t[1:]))


def gaps_excess(lines, common):
    a = adj(lines)
    L = Counter(x for (x, y), n in a.items() for _ in range(n))
    Rr = Counter(y for (x, y), n in a.items() for _ in range(n))
    N = sum(a.values())
    gaps, exc = [], []
    for x in common:
        for y in common:
            e = L[x] * Rr[y] / N
            o = a[(x, y)]
            if e >= 5 and o == 0:
                gaps.append((x, y))
            if o >= 5 and o >= 5 * e:
                exc.append((x, y))
    return gaps, exc


def mi(pairs):
    c = Counter(pairs)
    n = sum(c.values())
    L = Counter(x for x, y in pairs)
    Rr = Counter(y for x, y in pairs)
    return sum(v / n * math.log2(v * n / (L[x] * Rr[y])) for (x, y), v in c.items())


def shuffled(lines):
    out = []
    for t in lines:
        s = list(t)
        random.shuffle(s)
        out.append(tuple(s))
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-twenty-eighth registered predictions: forbidden pairs and a family grammar', 'predict_test128')
    DL = sorted({tuple(t) for t in AB})

    def common_of(lines):
        tc = Counter(g for t in lines for g in t)
        return sorted(g for g in tc if tc[g] >= 20 and g not in R.NUMS)

    def fa1(lines, key, lab):
        cm = common_of(lines)
        g, e = gaps_excess(lines, cm)
        sh = [len(gaps_excess(shuffled(lines), cm)[0]) for _ in range(R.N // 10)]
        m = sum(sh) / len(sh)
        rd.rec(key, 'some pairs are forbidden%s' % lab, 'gaps %d; shuffled mean %.1f; ratio %.2f; threshold 2' % (len(g), m, len(g) / max(0.1, m)), len(g) >= 2 * m)
        return g, e
    g, e = fa1(DL, 'FA1', '')
    rd.say('- example gaps: %s; example excess pairs: %s.' % (', '.join('%s-%s' % p for p in g[:10]), ', '.join('%s-%s' % p for p in e[:10])))
    role = lambda s: s in R.END or s in SUF or s in R.NUMS
    rd.thr('FA2', 'strong pairs are grammatical', 'excess pairs with an ending, suffix or numeral', sum(role(x) or role(y) for x, y in e), len(e), 0.5)
    cm = common_of(DL)
    pre740 = {x for t in DL for x, y in zip(t, t[1:]) if y == '740'}
    ne = [s for s in cm if s not in R.END]
    rd.thr('FA3', 'many signs never precede 740', 'common non-ending signs never before 740', sum(s not in pre740 for s in ne), len(ne), 0.2)
    aft = {y for t in DL for x, y in zip(t, t[1:]) if x in R.NUMS and y not in R.NUMS}
    j = len(pre740 & aft) / max(1, len(pre740 | aft))
    rd.rec('FA4', 'heads and counted things differ', 'Jaccard %.3f; threshold 0.3' % j, j <= 0.3)
    bp = lambda lines: [(blk(x), blk(y)) for t in lines for x, y in zip(t, t[1:]) if blk(x) is not None and blk(y) is not None]

    def fa5(lines, key, lab):
        obs = mi(bp(lines))
        ge = sum(mi(bp(shuffled(lines))) >= obs for _ in range(R.N // 10))
        p = (ge + 1) / (R.N // 10 + 1)
        rd.rec(key, 'the families have a grammar%s' % lab, 'block MI %.4f; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
        return obs
    bm = fa5(DL, 'FA5', '')
    sm = mi([p for t in DL for p in zip(t, t[1:])])
    rd.rec('FA6', 'families carry much of the order', 'block MI %.3f, sign MI %.3f; share %.2f; threshold 0.2' % (bm, sm, bm / sm), bm / sm >= 0.2)
    sb = lambda ps: [blk(x) == blk(y) for x, y in ps if blk(x) is not None and blk(y) is not None]
    rd.ltl('FA7', 'forbidden pairs cross families', 'same block, gaps', sb(g), sb(e))
    fa1(sorted({tuple(t) for t in B}), 'FA8', ' (B)')
    Fn = [r for r in F if r['type'] != 'TAB:C']
    fa5(sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln}), 'FA9', " (F')")
    rd.thr('FA10', 'gaps involve headings or numbers', 'gaps with a heading sign or numeral', sum(x in HEAD or y in HEAD or x in R.NUMS or y in R.NUMS for x, y in g), len(g), 0.3)
    rd.finish()


if __name__ == '__main__':
    main()
