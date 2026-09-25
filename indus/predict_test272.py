"""Two-hundred-and-seventy-second registered prediction set (PREDICTIONS.md, MK1-MK4): decipherment loop 97, modified
Kneser-Ney discounts for the sign trigram (Chen & Goodman 1998): discounts D1, D2, D3+ for counts 1, 2, 3+, estimated
from the training trigrams' count-of-counts, in place of the single D = 0.75 of trik (set 211). Component 'trimk'
replaces 'trik' in the model. Writes results/predict_test272.md."""
from collections import Counter

import rtools as R
from famlm import M3, fit3, score3
from prizebench import _lp
from progress import MODEL, data
from signs import load

NEW = ['trimk' if k == 'trik' else k for k in MODEL['keys']]


class MK(M3):
    def __init__(self, train):
        super().__init__(train)
        n = Counter(c for ctx in self.tri.values() for c in ctx.values())
        y = n[1] / (n[1] + 2 * n[2])
        self.D = {1: 1 - 2 * y * n[2] / n[1], 2: 2 - 3 * y * n[3] / n[2], 3: 3 - 4 * y * n[4] / n[3]}

    def rows(self, t, kn=False):
        out = super().rows(t, kn)
        s = ['<s>', '<s>'] + [g if g in self.vocab else '<unk>' for g in t] + ['</s>']
        for r, i in zip(out, range(2, len(s))):
            w = s[i]
            t3 = self.tri[(s[i - 2], s[i - 1])]
            nt = sum(t3.values())
            if not nt:
                r['trimk'] = r['bi']
                continue
            d = lambda c: self.D[min(c, 3)] if c else 0.0
            gam = sum(d(c) for c in t3.values()) / nt
            r['trimk'] = max(t3[w] - d(t3[w]), 0) / nt + gam * r['bi']
        return out


def sign_top1(tr, te, keys, cls, ncand=150):
    w, _ = fit3(tr, keys, cls=cls)
    m = cls(tr)
    rtr = [tuple(reversed(x)) for x in tr]
    wb, _ = fit3(rtr, keys, cls=cls)
    mb = cls(rtr)
    freq = Counter(g for t in tr for g in t)
    cands = [g for g, c in freq.most_common(ncand)]
    top1 = n = 0
    for t in te:
        for i, g in enumerate(t):
            sc = max(cands, key=lambda c: (_lp(m, t[:i] + (c,) + t[i + 1:], w) + _lp(mb, tuple(reversed(t[:i] + (c,) + t[i + 1:])), wb), c))
            n += 1
            top1 += sc == g
    return top1 / n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-seventy-second registered predictions: decipherment loop 97, modified Kneser-Ney discounts', 'predict_test272')
    DL, tr, te = data()
    rd.say('- discounts on the training lines: %s.' % ', '.join('D%d %.3f' % kv for kv in MK(tr).D.items()))
    s0, _ = score3(tr, te, MODEL['keys'])
    s1, w1 = score3(tr, te, NEW, cls=MK)
    rd.rec('MK1', 'S on the fixed test falls by 0.002 bits or more', 'S %.4f -> %.4f (gain %.4f; weights %s)' % (s0, s1, s0 - s1, {k: round(v, 3) for k, v in w1.items()}), s0 - s1 >= 0.002)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, MODEL['keys'])
    b1, _ = score3(DA, DBx, NEW, cls=MK)
    rd.rec('MK2', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    a1 = sign_top1(tr, te, MODEL['keys'], M3)
    c1 = sign_top1(tr, te, NEW, MK)
    rd.rec('MK3', 'SIGN top-1 does not fall', 'before %.1f%%, after %.1f%%' % (100 * a1, 100 * c1), c1 >= a1)
    ok = s0 - s1 >= 0.002 and b1 < b0 and c1 >= a1
    rd.rec('MK4', 'progress rule: MK1, MK2 and MK3', 'MK1 %s, MK2 %s, MK3 %s' % (s0 - s1 >= 0.002, b1 < b0, c1 >= a1), ok)
    rd.finish()


if __name__ == '__main__':
    main()
