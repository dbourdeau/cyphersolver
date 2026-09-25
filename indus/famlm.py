"""Family back-off features for the S model (set 194): the previous sign replaced by its graphic family (the ICIT
decade block, g // 10: 740-745 jars, 700-706 U's, 220-240 fish ...), so marked variants share contexts."""
import itertools
from collections import Counter, defaultdict

from predict_test122 import split
from predict_test125 import M2, pcls, xent


def fam(g):
    return 'f%d' % (int(g) // 10) if g.isdigit() else g


class M3(M2):
    famfn = staticmethod(fam)
    K = 1.0  # add-K smoothing of the count components (set 212 tests K = 0.3)

    def sm(self, c, w):
        return (c[w] + self.K) / (sum(c.values()) + self.K * self.V)

    def __init__(self, train):
        super().__init__(train)
        fam = self.famfn
        self.fb = defaultdict(Counter)
        self.ft = defaultdict(Counter)
        self.fw = defaultdict(Counter)
        self.f4 = defaultdict(Counter)
        self.fpos = defaultdict(Counter)  # set 214: opening sign x position class
        self.f2s = defaultdict(Counter)  # set 217: the line's first two signs
        for t in train:
            for w in list(t[1:]) + ['</s>']:
                self.f2s[tuple(t[:2])][w] += 1
        for t in train:
            s = ['<s>', '<s>'] + list(t) + ['</s>']
            for i in range(2, len(s)):
                self.fb[fam(s[i - 1])][s[i]] += 1
                self.ft[(fam(s[i - 2]), fam(s[i - 1]))][s[i]] += 1
                self.fw[fam(s[i - 1])][fam(s[i])] += 1
                self.f4[(fam(s[i - 3]) if i >= 3 else '<s>', fam(s[i - 2]), fam(s[i - 1]))][s[i]] += 1
                self.fpos[(s[2], pcls(i - 2, len(t) + 1))][s[i]] += 1

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
            c4 = self.f4[(fam(s[i - 3]) if i >= 3 else '<s>', fam(s[i - 2]), fam(s[i - 1]))]
            l4 = sum(c4.values()) / (sum(c4.values()) + 2)
            r['f4'] = l4 * c4[w] / max(1, sum(c4.values())) + (1 - l4) * r['ftri']  # set 199
            # set 210: absolute discounting, D = 0.5
            n3, n4 = sum(c.values()), sum(c4.values())
            p3 = (max(c[w] - 0.5, 0) / n3 + 0.5 * len(c) / n3 * r['fbi']) if n3 else r['fbi']
            r['f4k'] = (max(c4[w] - 0.5, 0) / n4 + 0.5 * len(c4) / n4 * p3) if n4 else p3
            r['firstpos'] = self.sm(self.fpos[(s[2], pcls(i - 2, len(t) + 1))], w)
            if i == 2:
                r['first2'] = r['first']
            else:
                c2 = self.f2s[tuple(t[:2])]
                n2 = sum(c2.values())
                l2 = n2 / (n2 + 3)
                r['first2'] = l2 * c2[w] / max(1, n2) + (1 - l2) * r['first']
            # set 211: the sign trigram absolutely discounted, D = 0.75, onto the Kneser-Ney bigram
            t3 = self.tri[(s[i - 2], s[i - 1])]
            nt = sum(t3.values())
            r['trik'] = (max(t3[w] - 0.75, 0) / nt + 0.75 * len(t3) / nt * r['bi']) if nt else r['bi']
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


def learned_classes(train, k, seed=0, iters=30):
    """k-means classes from left/right neighbour distributions (set 201), a control for the graphic families."""
    import numpy as np
    tok = Counter(g for t in train for g in t)
    V = list(tok)
    idx = {g: i for i, g in enumerate(V)}
    ctx = sorted(g for g, n in tok.items() if n >= 5) + ['<s>', '</s>']
    ci = {g: i for i, g in enumerate(ctx)}
    X = np.zeros((len(V), 2 * len(ctx)))
    for t in train:
        s = ['<s>'] + list(t) + ['</s>']
        for i in range(1, len(s) - 1):
            if s[i - 1] in ci:
                X[idx[s[i]], ci[s[i - 1]]] += 1
            if s[i + 1] in ci:
                X[idx[s[i]], len(ctx) + ci[s[i + 1]]] += 1
    X = X / np.maximum(1, X.sum(1, keepdims=True))
    rng = np.random.default_rng(seed)
    C = X[rng.choice(len(V), k, replace=False)]
    for _ in range(iters):
        lab = ((X[:, None, :] - C[None]) ** 2).sum(2).argmin(1)
        for j in range(k):
            if (lab == j).any():
                C[j] = X[lab == j].mean(0)
    return {g: 'c%d' % lab[idx[g]] for g in V}


class M4(M3):
    """M3 plus a second family component 'f4d' over another family map (set 208: Parpola-description families)."""
    fam2 = staticmethod(lambda g: g)

    def __init__(self, train):
        super().__init__(train)
        f2 = self.fam2
        self.d4 = defaultdict(Counter)
        self.d3 = defaultdict(Counter)
        for t in train:
            s = ['<s>', '<s>', '<s>'] + list(t) + ['</s>']
            for i in range(3, len(s)):
                self.d4[(f2(s[i - 3]), f2(s[i - 2]), f2(s[i - 1]))][s[i]] += 1
                self.d3[(f2(s[i - 2]), f2(s[i - 1]))][s[i]] += 1

    def rows(self, t, kn=False):
        f2 = self.fam2
        out = super().rows(t, kn)
        s = ['<s>', '<s>', '<s>'] + [g if g in self.vocab else '<unk>' for g in t] + ['</s>']
        for r, i in zip(out, range(3, len(s))):
            w = s[i]
            c3 = self.d3[(f2(s[i - 2]), f2(s[i - 1]))]
            l3 = sum(c3.values()) / (sum(c3.values()) + 2)
            p3 = l3 * c3[w] / max(1, sum(c3.values())) + (1 - l3) * r['fbi']
            c4 = self.d4[(f2(s[i - 3]), f2(s[i - 2]), f2(s[i - 1]))]
            l4 = sum(c4.values()) / (sum(c4.values()) + 2)
            r['f4d'] = l4 * c4[w] / max(1, sum(c4.values())) + (1 - l4) * p3
        return out


def with_fam2(fn):
    return type('M4f', (M4,), {'fam2': staticmethod(fn)})


def with_k(k, base=None):
    return type('M3k', (base or M3,), {'K': k})
