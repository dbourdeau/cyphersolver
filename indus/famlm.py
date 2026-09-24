"""Family back-off features for the S model (set 194): the previous sign replaced by its graphic family (the ICIT
decade block, g // 10: 740-745 jars, 700-706 U's, 220-240 fish ...), so marked variants share contexts."""
import itertools
from collections import Counter, defaultdict

from predict_test122 import split
from predict_test125 import M2, xent


def fam(g):
    return 'f%d' % (int(g) // 10) if g.isdigit() else g


class M3(M2):
    famfn = staticmethod(fam)

    def __init__(self, train):
        super().__init__(train)
        fam = self.famfn
        self.fb = defaultdict(Counter)
        self.ft = defaultdict(Counter)
        self.fw = defaultdict(Counter)
        for t in train:
            s = ['<s>', '<s>'] + list(t) + ['</s>']
            for i in range(2, len(s)):
                self.fb[fam(s[i - 1])][s[i]] += 1
                self.ft[(fam(s[i - 2]), fam(s[i - 1]))][s[i]] += 1
                self.fw[fam(s[i - 1])][fam(s[i])] += 1

    def rows(self, t, kn=False):
        fam = self.famfn
        out = super().rows(t, kn)
        s = ['<s>', '<s>'] + [g if g in self.vocab else '<unk>' for g in t] + ['</s>']
        for r, i in zip(out, range(2, len(s))):
            w = s[i]
            r['fbi'] = self.sm(self.fb[fam(s[i - 1])], w)
            c = self.ft[(fam(s[i - 2]), fam(s[i - 1]))]
            lam = sum(c.values()) / (sum(c.values()) + 2)
            r['ftri'] = lam * c[w] / max(1, sum(c.values())) + (1 - lam) * r['fbi']
        return out


def with_fam(fn):
    return type('M3f', (M3,), {'famfn': staticmethod(fn)})


def fit3(train, keys, kn=True, grid=(0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6), cls=M3):
    tr, dv = split(train)
    m = cls(tr)
    rows = [r for t in dv for r in m.rows(t, kn)]
    best = None
    for ws in itertools.product(grid, repeat=len(keys)):
        if sum(ws) == 0:
            continue
        w = {k: v / sum(ws) for k, v in zip(keys, ws)}
        x = xent(rows, w)
        if best is None or x < best[0]:
            best = (x, w)
    return best[1], best[0]


def score3(train, test, keys, kn=True, cls=M3):
    w, _ = fit3(train, keys, kn, cls=cls)
    m = cls(train)
    return xent([r for t in test for r in m.rows(t, kn)], w), w
