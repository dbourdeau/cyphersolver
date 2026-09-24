"""Hundred-and-twenty-fourth registered prediction set (PREDICTIONS.md, CM1-CM10): one combined model. Writes
results/predict_test124.md."""
import itertools
import math
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test108 import genre
from predict_test122 import split
from predict_test123 import role

random.seed(142)


def pcls(i, n):
    return 'F' if i == 0 else ('L' if i == n - 1 else ('E' if i == n - 2 else 'M'))


def rbucket(i, n):
    return 'end' if i == n else min(4, int(5 * i / max(1, n)))


class Combo:
    def __init__(self, train):
        self.vocab = {g for t in train for g in t} | {'<unk>', '</s>'}
        self.V = len(self.vocab)
        self.uni, self.bi, self.tri = Counter(), defaultdict(Counter), defaultdict(Counter)
        self.rbi, self.emit, self.pos, self.pbi, self.rpos = defaultdict(Counter), defaultdict(Counter), defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)
        self.gbi = defaultdict(lambda: defaultdict(Counter))
        for t in train:
            s = ['<s>', '<s>'] + list(t) + ['</s>']
            rs = ['<s>', '<s>'] + [role(t, i) for i in range(len(t))] + ['</s>']
            n = len(t) + 1
            g = genre(t)
            for i in range(2, len(s)):
                w = s[i]
                k = i - 2
                self.uni[w] += 1
                self.bi[s[i - 1]][w] += 1
                self.tri[(s[i - 2], s[i - 1])][w] += 1
                self.rbi[rs[i - 1]][rs[i]] += 1
                self.emit[rs[i]][w] += 1
                self.pos[pcls(k, n)][w] += 1
                self.pbi[(s[i - 1], pcls(k, n))][w] += 1
                self.rpos[rbucket(k, len(t))][w] += 1
                self.gbi[g][s[i - 1]][w] += 1
        self.N = sum(self.uni.values())

    def comps(self, t):
        s = ['<s>', '<s>'] + [g if g in self.vocab else '<unk>' for g in t] + ['</s>']
        rs = ['<s>', '<s>'] + [role(t, i) for i in range(len(t))] + ['</s>']
        n = len(t) + 1
        g = genre(t)
        out = []
        sm = lambda c, w: (c[w] + 1) / (sum(c.values()) + self.V)
        for i in range(2, len(s)):
            w, k = s[i], i - 2
            c3 = self.tri[(s[i - 2], s[i - 1])]
            pb = sm(self.bi[s[i - 1]], w)
            lam = sum(c3.values()) / (sum(c3.values()) + 2)
            ptri = lam * (c3[w] / max(1, sum(c3.values()))) + (1 - lam) * pb
            cr, e = self.rbi[rs[i - 1]], self.emit[rs[i]]
            prole = (cr[rs[i]] + 0.1) / (sum(cr.values()) + 1) * (e[w] + 0.1) / (sum(e.values()) + 0.1 * self.V)
            out.append({'bi': pb, 'tri': ptri, 'role': prole, 'pos': sm(self.pos[pcls(k, n)], w), 'pbi': sm(self.pbi[(s[i - 1], pcls(k, n))], w),
                        'gen': sm(self.gbi[g][s[i - 1]], w), 'rpos': sm(self.rpos[rbucket(k, len(t))], w)})
        return out


def xent(rows, w):
    tot = 0
    for r in rows:
        p = sum(w[k] * r[k] for k in w)
        tot += -math.log2(max(p, 1e-12))
    return tot / len(rows)


def fit(model, dev, keys):
    rows = [r for t in dev for r in model.comps(t)]
    grid = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
    best = None
    for ws in itertools.product(grid, repeat=len(keys)):
        if sum(ws) == 0:
            continue
        w = {k: v / sum(ws) for k, v in zip(keys, ws)}
        x = xent(rows, w)
        if best is None or x < best[0]:
            best = (x, w)
    return best[1]


def run(train, test, keys):
    tr, dv = split(train)
    w = fit(Combo(tr), dv, keys)
    m = Combo(train)
    return xent([r for t in test for r in m.comps(t)], w), w


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-twenty-fourth registered predictions: one combined model', 'predict_test124')
    DL = sorted({tuple(t) for t in AB})
    tr, te = split(DL)
    m = Combo(tr)
    rows = [r for t in te for r in m.comps(t)]
    single = {k: xent(rows, {k: 1.0}) for k in ('bi', 'tri', 'role', 'pos')}
    rd.say('- single components (held-out bits per sign): %s.' % {k: round(v, 3) for k, v in single.items()})
    rd.say()
    base = ['bi', 'tri', 'role', 'pos']
    comb, w = run(tr, te, base)
    best1 = min(single.values())
    rd.rec('CM1', 'the combination beats every part', 'combined %.3f (weights %s), best single %.3f; threshold 0.3 bit' % (comb, {k: round(v, 2) for k, v in w.items()}, best1),
           best1 - comb >= 0.3)
    rd.rec('CM2', 'under five bits', 'combined %.3f; threshold 5.0' % comb, comb < 5.0)
    cg, _ = run(tr, te, base + ['gen'])
    rd.rec('CM3', 'genre adds', 'with genre %.3f against %.3f; threshold 0.05' % (cg, comb), comb - cg >= 0.05)
    cp, _ = run(tr, te, base + ['pbi'])
    rd.rec('CM4', 'position-aware bigram adds', 'with position bigram %.3f against %.3f; threshold 0.05' % (cp, comb), comb - cp >= 0.05)
    Fn = [r for r in F if r['type'] != 'TAB:C']
    ab = set(DL)
    FX = sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln} - ab)
    cf, _ = run(DL, FX, base)
    rd.rec('CM5', 'the model transfers to new lines', 'F lines absent from A + B (%d): %.3f; threshold 5.5' % (len(FX), cf), cf < 5.5)
    BL = sorted({tuple(t) for t in B})
    btr, bte = split(BL)
    mb = Combo(btr)
    bbi = xent([r for t in bte for r in mb.comps(t)], {'bi': 1.0})
    bc, _ = run(btr, bte, base)
    rd.rec('CM6', 'the model helps on B', 'B bigram %.3f, combined %.3f; threshold 0.5' % (bbi, bc), bbi - bc >= 0.5)
    for key, drop, th in (('CM7', 'role', 0.1), ('CM8', 'pos', 0.2), ('CM9', 'tri', 0.1)):
        c, _ = run(tr, te, [k for k in base if k != drop])
        rd.rec(key, 'the %s part matters' % drop, 'without %s %.3f against %.3f; threshold %.2f' % (drop, c, comb, th), c - comb >= th)
    rp = xent(rows, {'rpos': 1.0})
    rd.rec('CM10', 'finer position helps', 'five-bucket %.3f, four-way %.3f; threshold 0.1' % (rp, single['pos']), single['pos'] - rp >= 0.1)
    rd.finish()


if __name__ == '__main__':
    main()
