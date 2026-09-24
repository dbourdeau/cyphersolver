"""Hundred-and-twenty-third registered prediction set (PREDICTIONS.md, BM1-BM12): does structure improve prediction?
Writes results/predict_test123.md."""
import math
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test103 import CL
from predict_test108 import genre
from predict_test122 import split
from signs import FISH

random.seed(142)
HEAD = ('817', '820', '861')
CITY = ('Mohenjo-daro', 'Harappa')


def role(t, i):
    g = t[i]
    if g in R.NUMS:
        return 'N' + R.kind(g)
    if i == 0 and g in HEAD:
        return 'H'
    if g in R.END:
        return 'E'
    if g in ('400', '90', '151') and i > 0 and t[i - 1] in R.END:
        return 'S'
    if g in CL:
        return 'C'
    if g in FISH:
        return 'F'
    return 'X'


class Model:
    def __init__(self, train):
        self.vocab = {g for t in train for g in t} | {'<unk>', '</s>'}
        self.V = len(self.vocab)
        self.uni = Counter()
        self.bi = defaultdict(Counter)
        self.rbi = defaultdict(Counter)
        self.emit = defaultdict(Counter)
        self.pos = defaultdict(Counter)
        for t in train:
            s = ['<s>'] + list(t) + ['</s>']
            rs = ['<s>'] + [role(t, i) for i in range(len(t))] + ['</s>']
            for i in range(1, len(s)):
                self.uni[s[i]] += 1
                self.bi[s[i - 1]][s[i]] += 1
                self.rbi[rs[i - 1]][rs[i]] += 1
                self.emit[rs[i]][s[i]] += 1
                p = 'F' if i == 1 else ('L' if i == len(s) - 1 else ('E' if i == len(s) - 2 else 'M'))
                self.pos[p][s[i]] += 1
        self.N = sum(self.uni.values())

    def n(self, g):
        return g if g in self.vocab else '<unk>'

    def p_uni(self, w):
        return (self.uni[w] + 1) / (self.N + self.V)

    def p_bi(self, a, w):
        c = self.bi[a]
        return (c[w] + 1) / (sum(c.values()) + self.V)

    def p_role(self, ra, rw, w):
        c = self.rbi[ra]
        e = self.emit[rw]
        return (c[rw] + 0.1) / (sum(c.values()) + 1) * (e[w] + 0.1) / (sum(e.values()) + 0.1 * self.V)

    def p_pos(self, p, w):
        c = self.pos[p]
        return (c[w] + 1) / (sum(c.values()) + self.V)


def score(m, lines, mode, lam=0.0, norep=False):
    tot = k = 0
    for t in lines:
        s = ['<s>'] + [m.n(g) for g in t] + ['</s>']
        rs = ['<s>'] + [role(t, i) for i in range(len(t))] + ['</s>']
        for i in range(1, len(s)):
            w = s[i]
            if mode == 'uni':
                p = m.p_uni(w)
            elif mode == 'pos':
                p = m.p_pos('F' if i == 1 else ('L' if i == len(s) - 1 else ('E' if i == len(s) - 2 else 'M')), w)
            else:
                p = m.p_bi(s[i - 1], w)
                if lam:
                    p = (1 - lam) * p + lam * m.p_role(rs[i - 1], rs[i], w)
            if norep and w in s[1:max(1, i - 1)]:
                p *= 0.5
            tot += -math.log2(p)
            k += 1
    return tot / k


def fit_lam(train):
    tr, dv = split(train)
    m = Model(tr)
    return min((0.05, 0.1, 0.2, 0.3, 0.5), key=lambda l_: score(m, dv, 'bi', l_))


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-twenty-third registered predictions: does structure improve prediction?', 'predict_test123')
    DL = sorted({tuple(t) for t in AB})
    tr, te = split(DL)
    m = Model(tr)
    base = score(m, te, 'bi')
    lam = fit_lam(tr)
    rd.say('- bigram %.3f bits; role weight fitted on training slice %.2f.' % (base, lam))
    rd.say()
    rb = score(m, te, 'bi', lam)
    rd.rec('BM1', 'roles improve prediction', 'bigram %.3f, with roles %.3f; threshold 0.1 bit' % (base, rb), base - rb >= 0.1)
    gm = {}
    for g in ('name', 'count', 'closer', 'bare', 'other'):
        sub = [t for t in tr if genre(t) == g]
        gm[g] = Model(sub) if sub else m
    tot = k = 0
    for t in te:
        g = genre(t)
        mm = gm[g]
        s = ['<s>'] + [mm.n(x) for x in t] + ['</s>']
        for i in range(1, len(s)):
            p = 0.5 * mm.p_bi(s[i - 1], s[i]) + 0.5 * m.p_bi(m.n(s[i - 1]) if s[i - 1] != '<s>' else '<s>', m.n(s[i]) if s[i] != '</s>' else '</s>')
            tot += -math.log2(p)
            k += 1
    gb = tot / k
    rd.rec('BM2', 'genre helps', 'bigram %.3f, genre-mixed %.3f; threshold 0.1 bit' % (base, gb), base - gb >= 0.1)
    u, pu = score(m, te, 'uni'), score(m, te, 'pos')
    rd.rec('BM3', 'position helps', 'unigram %.3f, position-aware %.3f; threshold 0.5 bit' % (u, pu), u - pu >= 0.5)
    mr = Model([tuple(reversed(t)) for t in tr])
    rv = score(mr, [tuple(reversed(t)) for t in te], 'bi')
    rd.rec('BM4', 'the recorded direction reads better', 'forward %.3f, reverse %.3f; threshold 0.05 bit' % (base, rv), rv - base >= 0.05)
    names = lambda L: [R.name_of(list(t)) for t in L if R.name_of(list(t)) and R.name_of(list(t))[0]]
    ntr, nte = names(tr), names(te)
    c1, c2 = defaultdict(Counter), defaultdict(Counter)
    for b, e in ntr:
        if len(b) >= 2:
            c1[b[-2]][b[-1]] += 1
            c2[(b[-2], e)][b[-1]] += 1
    t2 = [(b, e) for b, e in nte if len(b) >= 2]
    a1 = sum(bool(c1[b[-2]]) and c1[b[-2]].most_common(1)[0][0] == b[-1] for b, e in t2) / len(t2)
    a2 = sum((c2[(b[-2], e)].most_common(1)[0][0] if c2[(b[-2], e)] else (c1[b[-2]].most_common(1)[0][0] if c1[b[-2]] else None)) == b[-1] for b, e in t2) / len(t2)
    rd.rec('BM5', 'the ending helps find the head', 'without %.1f%%, with %.1f%%; threshold +5 points' % (100 * a1, 100 * a2), a2 - a1 >= 0.05)
    hc = defaultdict(Counter)
    for b, e in ntr:
        hc[b[-1]][e] += 1
    x = [(b, e) for b, e in nte if sum(hc[b[-1]].values()) >= 5]
    a = sum(hc[b[-1]].most_common(1)[0][0] == e for b, e in x) / max(1, len(x))
    rd.rec('BM6', 'common heads fix the ending', 'accuracy %.1f%% over %d names; threshold 95%%' % (100 * a, len(x)), a >= 0.95)
    nr = score(m, te, 'bi', norep=True)
    rd.rec('BM7', 'signs avoid repeating', 'bigram %.3f, no-repeat %.3f; threshold 0.02 bit' % (base, nr), base - nr >= 0.02)

    def tri_gain(lines):
        from predict_test122 import xent
        return xent(tr, lines, 2) - xent(tr, lines, 3)
    gn = tri_gain([t for t in te if genre(t) == 'name'])
    gc = tri_gain([t for t in te if genre(t) == 'count'])
    rd.rec('BM8', 'names have longer dependencies', 'trigram gain names %.3f, counts %.3f bits' % (gn, gc), gn > gc)
    Fn = [r for r in F if r['type'] != 'TAB:C']
    L = lambda s: sorted({tuple(ln) for r in Fn if r['site'].strip() == s for ln in r['seq'] if ln})
    H, M = L('Harappa'), L('Mohenjo-daro')
    htr, hte = split(H)
    mtr = random.sample(M, min(len(htr), len(M)))
    e_in = score(Model(htr), hte, 'bi')
    e_out = score(Model(mtr), hte, 'bi')
    rd.rec('BM9', 'each city has its own sequences', 'Harappa test: Harappa-trained %.3f, Mohenjo-daro-trained %.3f; threshold 0.3 bit' % (e_in, e_out), e_out - e_in >= 0.3)
    ntrL = [t for t in tr if genre(t) == 'name']
    mn = Model(ntrL)
    en = score(mn, [t for t in te if genre(t) == 'name'], 'bi')
    ec = score(mn, [t for t in te if genre(t) == 'count'], 'bi')
    rd.rec('BM10', 'names and counts are different sequences', 'names %.3f, counts %.3f; threshold 1 bit' % (en, ec), ec - en >= 1)
    BL = sorted({tuple(t) for t in B})
    btr, bte = split(BL)
    AL = sorted({tuple(t) for t in A})
    atr = random.sample(AL, min(len(btr), len(AL)))
    eb, ea = score(Model(btr), bte, 'bi'), score(Model(atr), bte, 'bi')
    rd.rec('BM11', 'the transcriptions write alike', 'B test: B-trained %.3f, A-trained %.3f; threshold within 1 bit' % (eb, ea), ea - eb <= 1)
    OS = sorted({tuple(ln) for r in Fn if r['site'].strip() not in CITY for ln in r['seq'] if ln})
    go = score(m, OS, 'bi') - score(m, OS, 'bi', lam)
    gt = base - rb
    rd.rec('BM12', 'roles help most where data is thin', 'role gain on small sites %.3f, on held-out lines %.3f' % (go, gt), go > gt)
    rd.finish()


if __name__ == '__main__':
    main()
