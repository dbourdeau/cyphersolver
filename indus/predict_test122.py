"""Hundred-and-twenty-second registered prediction set (PREDICTIONS.md, GM1-GM15): the model as a predictor. Writes
results/predict_test122.md."""
import math
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test61 import units
from predict_test104 import template
from predict_test108 import genre

random.seed(142)


def split(lines):
    ls = list(lines)
    random.shuffle(ls)
    k = int(0.8 * len(ls))
    return ls[:k], ls[k:]


def xent(train, test, order):
    vocab = {g for t in train for g in t} | {'<unk>'}
    V = len(vocab) + 1
    norm = lambda g: g if g in vocab else '<unk>'
    uni = Counter(norm(g) for t in train for g in ['</s>'] + list(t))
    bi = defaultdict(Counter)
    tri = defaultdict(Counter)
    for t in train:
        s = ['<s>', '<s>'] + [norm(g) for g in t] + ['</s>']
        for i in range(2, len(s)):
            bi[s[i - 1]][s[i]] += 1
            tri[(s[i - 2], s[i - 1])][s[i]] += 1
    N = sum(uni.values())
    tot = n = 0
    for t in test:
        s = ['<s>', '<s>'] + [norm(g) for g in t] + ['</s>']
        for i in range(2, len(s)):
            w = s[i]
            pu = (uni[w] + 1) / (N + V)
            if order == 1:
                p = pu
            else:
                c = bi[s[i - 1]]
                pb = (c[w] + 1) / (sum(c.values()) + V)
                if order == 2:
                    p = pb
                else:
                    c3 = tri[(s[i - 2], s[i - 1])]
                    lam = sum(c3.values()) / (sum(c3.values()) + 2)
                    p = lam * (c3[w] / max(1, sum(c3.values()))) + (1 - lam) * pb
            tot += -math.log2(p)
            n += 1
    return tot / n


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-twenty-second registered predictions: the model as a predictor', 'predict_test122')
    DL = sorted({tuple(t) for t in AB})
    tr, te = split(DL)
    rd.say('- training lines %d, test lines %d.' % (len(tr), len(te)))
    rd.say()
    names = lambda L: [R.name_of(list(t)) for t in L if R.name_of(list(t)) and R.name_of(list(t))[0]]
    ntr, nte = names(tr), names(te)
    nxt = defaultdict(Counter)
    for b, e in ntr:
        if len(b) >= 2:
            nxt[b[-2]][b[-1]] += 1
    top = Counter(b[-1] for b, e in ntr).most_common(1)[0][0]
    t2 = [(b, e) for b, e in nte if len(b) >= 2]
    acc_bi = sum(bool(nxt[b[-2]]) and nxt[b[-2]].most_common(1)[0][0] == b[-1] for b, e in t2) / len(t2)
    acc_base = sum(b[-1] == top for b, e in t2) / len(t2)
    rd.rec('GM1', 'the neighbour predicts the head', 'accuracy %.1f%% against %.1f%% (commonest head); threshold +10 points' % (100 * acc_bi, 100 * acc_base), acc_bi - acc_base >= 0.10)

    def head_ending(trn, tst):
        hc = defaultdict(Counter)
        for b, e in trn:
            hc[b[-1]][e] += 1
        x = [(b, e) for b, e in tst if b[-1] in hc]
        return sum(hc[b[-1]].most_common(1)[0][0] == e for b, e in x) / max(1, len(x)), len(x)
    a1, n1 = head_ending(ntr, nte)
    rd.rec('GM2', 'the head predicts the ending', 'accuracy %.1f%% over %d names; threshold 85%%' % (100 * a1, n1), a1 >= 0.85)
    oc = defaultdict(Counter)
    for b, e in ntr:
        oc[b[0]][e] += 1
    xo = [(b, e) for b, e in nte if b[0] in oc]
    a2 = sum(oc[b[0]].most_common(1)[0][0] == e for b, e in xo) / max(1, len(xo))
    rd.rec('GM3', 'the head beats the opener', 'head %.1f%%, opener %.1f%%; threshold +10 points' % (100 * a1, 100 * a2), a1 - a2 >= 0.10)

    def genre_acc(trn, tst, pos):
        gc = defaultdict(Counter)
        for t in trn:
            gc[t[pos]][genre(t)] += 1
        x = [t for t in tst if t[pos] in gc]
        return sum(gc[t[pos]].most_common(1)[0][0] == genre(t) for t in x) / max(1, len(x))
    gl, gf = genre_acc(tr, te, -1), genre_acc(tr, te, 0)
    rd.rec('GM4', 'the last sign tells the genre', 'accuracy %.1f%%; threshold 80%%' % (100 * gl), gl >= 0.8)
    rd.rec('GM5', 'last beats first', 'last %.1f%%, first %.1f%%; threshold +20 points' % (100 * gl, 100 * gf), gl - gf >= 0.2)
    tt = {k for k, _ in Counter(template(t) for t in tr).most_common(10)}
    rd.thr('GM6', 'the templates generalise', 'test lines in the training top-10 templates', sum(template(t) in tt for t in te), len(te), 0.45)
    h1, h2, h3 = xent(tr, te, 1), xent(tr, te, 2), xent(tr, te, 3)
    rd.rec('GM7', 'order predicts', 'unigram %.2f, bigram %.2f bits per sign; threshold 1 bit gain' % (h1, h2), h1 - h2 >= 1)
    rd.rec('GM8', 'longer context helps', 'bigram %.2f, trigram %.2f; threshold 0.2 bit gain' % (h2, h3), h2 - h3 >= 0.2)
    U = units(sorted({b for b, e in ntr if len(b) >= 2}))
    b3 = [b for b, e in nte if len(b) >= 3]
    rd.thr('GM9', 'units generalise', 'test bodies of 3+ with a training unit', sum(any(p in U for p in zip(b, b[1:])) for b in b3), len(b3), 0.6)
    hs = {b[-1] for b, e in ntr}
    rd.thr('GM10', 'heads are a closed set', 'test heads seen in training', sum(b[-1] in hs for b, e in nte), len(nte), 0.9)
    os_ = {b[0] for b, e in ntr if len(b) >= 2}
    o2 = [b for b, e in nte if len(b) >= 2]
    rd.thr('GM11', 'openers are mostly known', 'test openers seen in training', sum(b[0] in os_ for b in o2), len(o2), 0.7)
    Fn = [r for r in F if r['type'] != 'TAB:C']
    nm = lambda site: sorted({(b, e) for r in Fn if r['site'].strip() == site for b, e in R.names_in(r) if b})
    a3, n3 = head_ending(nm('Mohenjo-daro'), nm('Harappa'))
    rd.rec('GM12', 'Mohenjo-daro heads predict Harappa endings', 'accuracy %.1f%% over %d names; threshold 85%%' % (100 * a3, n3), a3 >= 0.85)
    a4, n4 = head_ending(sorted({(b, e) for b, e in T.names(A) if b}), sorted({(b, e) for b, e in T.names(B) if b}))
    rd.rec('GM13', 'A heads predict B endings', 'accuracy %.1f%% over %d names; threshold 85%%' % (100 * a4, n4), a4 >= 0.85)
    trB, teB = split(sorted({tuple(t) for t in B}))
    gB = genre_acc(trB, teB, -1)
    rd.rec('GM14', 'the last sign tells the genre (B)', 'accuracy %.1f%%; threshold 80%%' % (100 * gB), gB >= 0.8)
    trF, teF = split(sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln}))
    f1, f2 = xent(trF, teF, 1), xent(trF, teF, 2)
    rd.rec('GM15', "order predicts (F')", 'unigram %.2f, bigram %.2f; threshold 1 bit gain' % (f1, f2), f1 - f2 >= 1)
    rd.finish()


if __name__ == '__main__':
    main()
