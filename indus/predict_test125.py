"""Hundred-and-twenty-fifth registered prediction set (PREDICTIONS.md, BB1-BB10): beating the benchmark. Writes
results/predict_test125.md."""
import itertools
import math
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test102 import blk
from predict_test122 import split

random.seed(142)


def pcls(i, n):
    return 'F' if i == 0 else ('L' if i == n - 1 else ('E' if i == n - 2 else 'M'))


def dend(i, n):
    return min(3, n - 1 - i)


def dstart(i):
    return min(3, i)


class M2:
    """Components over positions i = 0..len(t) (len(t) = the end marker)."""

    def __init__(self, train):
        tok = Counter(g for t in train for g in t)
        self.rare = {g for g, n in tok.items() if n < 3}
        self.vocab = {g for g in tok} | {'<unk>', '</s>'}
        self.V = len(self.vocab)
        self.c = defaultdict(Counter)
        self.bi = defaultdict(Counter)
        self.tri = defaultdict(Counter)
        self.cont = defaultdict(set)
        self.blk = defaultdict(Counter)
        for t in train:
            s = ['<s>', '<s>'] + list(t) + ['</s>']
            n = len(t) + 1
            for i in range(2, len(s)):
                w, k = s[i], i - 2
                self.c['uni'][w] += 1
                self.c[('pos', pcls(k, n))][w] += 1
                self.c[('end', dend(k, n))][w] += 1
                self.c[('start', dstart(k))][w] += 1
                self.c[('len', min(len(t), 5), pcls(k, n))][w] += 1
                self.c[('first', s[2])][w] += 1
                self.bi[s[i - 1]][w] += 1
                self.tri[(s[i - 2], s[i - 1])][w] += 1
                self.cont[w].add(s[i - 1])
                b = blk(w) if w not in ('</s>',) else None
                self.blk[b][w] += 1
        self.ncont = sum(len(v) for v in self.cont.values())

    def sm(self, c, w):
        return (c[w] + 1) / (sum(c.values()) + self.V)

    def kn(self, a, w):
        c = self.bi[a]
        n = sum(c.values())
        pc = (len(self.cont[w]) + 0.5) / (self.ncont + 0.5 * self.V)
        if n == 0:
            return pc
        d = 0.75
        return max(c[w] - d, 0) / n + d * len(c) / n * pc

    def rows(self, t, kn=False):
        s = ['<s>', '<s>'] + [g if g in self.vocab else '<unk>' for g in t] + ['</s>']
        raw = ['<s>', '<s>'] + list(t) + ['</s>']
        n = len(t) + 1
        out = []
        for i in range(2, len(s)):
            w, k = s[i], i - 2
            pb = self.kn(s[i - 1], w) if kn else self.sm(self.bi[s[i - 1]], w)
            c3 = self.tri[(s[i - 2], s[i - 1])]
            lam = sum(c3.values()) / (sum(c3.values()) + 2)
            b = blk(raw[i]) if raw[i] not in ('</s>',) else None
            cb = self.blk[b]
            pblk = (sum(cb.values()) + 1) / (sum(len(x) for x in self.blk.values()) + self.V) / max(1, len(cb)) if (raw[i] in self.rare or w == '<unk>') and b is not None else self.sm(self.c['uni'], w)
            out.append({'tri': lam * (c3[w] / max(1, sum(c3.values()))) + (1 - lam) * pb, 'pos': self.sm(self.c[('pos', pcls(k, n))], w),
                        'end': self.sm(self.c[('end', dend(k, n))], w), 'start': self.sm(self.c[('start', dstart(k))], w),
                        'len': self.sm(self.c[('len', min(len(t), 5), pcls(k, n))], w), 'first': self.sm(self.c[('first', s[2])], w),
                        'bi': pb, 'blk': pblk})
        return out


def xent(rows, w):
    return sum(-math.log2(max(sum(w[k] * r[k] for k in w), 1e-12)) for r in rows) / len(rows)


def fit(train, keys, kn=False):
    tr, dv = split(train)
    m = M2(tr)
    rows = [r for t in dv for r in m.rows(t, kn)]
    best = None
    for ws in itertools.product([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6], repeat=len(keys)):
        if sum(ws) == 0:
            continue
        w = {k: v / sum(ws) for k, v in zip(keys, ws)}
        x = xent(rows, w)
        if best is None or x < best[0]:
            best = (x, w)
    return best[1]


def run(train, test, keys, kn=False):
    w = fit(train, keys, kn)
    m = M2(train)
    return xent([r for t in test for r in m.rows(t, kn)], w), w


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-twenty-fifth registered predictions: beating the benchmark', 'predict_test125')
    DL = sorted({tuple(t) for t in AB})
    tr, te = split(DL)
    m = M2(tr)
    rows = [r for t in te for r in m.rows(t)]
    bench, _ = run(tr, te, ['tri', 'pos'])
    rd.say('- benchmark (tri + pos) %.3f bits per sign.' % bench)
    rd.say()
    e, s = xent(rows, {'end': 1.0}), xent(rows, {'start': 1.0})
    rd.rec('BB1', 'lines are anchored at the end', 'distance-from-end %.3f, from-start %.3f; threshold 0.1' % (e, s), s - e >= 0.1)
    be, _ = run(tr, te, ['tri', 'end'])
    rd.rec('BB2', 'end distance in the benchmark', 'tri + end %.3f against %.3f; threshold 0.05' % (be, bench), bench - be >= 0.05)
    krows = [r for t in te for r in m.rows(t, kn=True)]
    a1, k1 = xent(rows, {'bi': 1.0}), xent(krows, {'bi': 1.0})
    rd.rec('BB3', 'better smoothing', 'add-one bigram %.3f, discounted %.3f; threshold 0.5' % (a1, k1), a1 - k1 >= 0.5)
    bk, _ = run(tr, te, ['tri', 'pos'], kn=True)
    rd.rec('BB4', 'better smoothing inside the benchmark', 'with discounting %.3f against %.3f; threshold 0.1' % (bk, bench), bench - bk >= 0.1)
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FX = sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln} - set(DL))
    fb, _ = run(DL, FX, ['tri', 'pos'])
    fbb, _ = run(DL, FX, ['tri', 'pos', 'blk'])
    rd.rec('BB5', 'shape blocks help unseen signs', 'new F lines: %.3f without, %.3f with block backoff; threshold 0.1' % (fb, fbb), fb - fbb >= 0.1)
    bl, _ = run(tr, te, ['tri', 'pos', 'len'])
    rd.rec('BB6', 'line length matters', 'with length-position %.3f against %.3f; threshold 0.05' % (bl, bench), bench - bl >= 0.05)
    bf, _ = run(tr, te, ['tri', 'pos', 'first'])
    rd.rec('BB7', 'the first sign sets the line', 'with first-sign term %.3f against %.3f; threshold 0.05' % (bf, bench), bench - bf >= 0.05)
    cands = {'end': be, 'kn': bk, 'len': bl, 'first': bf}
    best_key = min(cands, key=cands.get)
    keys = {'end': ['tri', 'end'], 'kn': ['tri', 'pos'], 'len': ['tri', 'pos', 'len'], 'first': ['tri', 'pos', 'first']}[best_key]
    kn = best_key == 'kn'
    full, w = run(tr, te, keys + (['end'] if best_key != 'end' else []), kn)
    rd.rec('BB8', 'under 4.8 bits', 'best model (%s + extra end term) %.3f; threshold 4.8' % (best_key, full), full < 4.8)
    ff, _ = run(DL, FX, keys + (['end'] if best_key != 'end' else []), kn)
    rd.rec('BB9', 'under 5.5 on new lines', 'new F lines %.3f; threshold 5.5' % ff, ff < 5.5)
    BL = sorted({tuple(t) for t in B})
    btr, bte = split(BL)
    b0, _ = run(btr, bte, ['tri', 'pos'])
    b1, _ = run(btr, bte, keys + (['end'] if best_key != 'end' else []), kn)
    rd.rec('BB10', 'the gain holds on B', 'B benchmark %.3f, best %.3f' % (b0, b1), b1 < b0)
    rd.finish()


if __name__ == '__main__':
    main()
