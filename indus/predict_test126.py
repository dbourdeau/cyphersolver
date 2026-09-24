"""Hundred-and-twenty-sixth registered prediction set (PREDICTIONS.md, RL1-RL9): is the line composed from the end?
Writes results/predict_test126.md."""
import math
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test108 import genre
from predict_test122 import split
from predict_test125 import run

random.seed(142)


def ent(c):
    n = sum(c.values())
    return -sum(v / n * math.log2(v / n) for v in c.values())


def pred_acc(train, test, ctx, target):
    c = defaultdict(Counter)
    for t in train:
        c[ctx(t)][target(t)] += 1
    x = [t for t in test if c[ctx(t)]]
    return sum(c[ctx(t)].most_common(1)[0][0] == target(t) for t in x) / max(1, len(x)), len(x)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-twenty-sixth registered predictions: is the line composed from the end?', 'predict_test126')
    DL = sorted({tuple(t) for t in AB})
    tr, te = split(DL)
    fwd, _ = run(tr, te, ['tri', 'pos', 'end'], True)
    rev, _ = run([tuple(reversed(t)) for t in tr], [tuple(reversed(t)) for t in te], ['tri', 'pos', 'start'], True)
    rd.say('- forward %.3f, reversed %.3f bits per sign.' % (fwd, rev))
    rd.say()
    rd.rec('RL1', 'reading backwards predicts better', 'forward %.3f, end-to-start %.3f; threshold 0.05' % (fwd, rev), fwd - rev >= 0.05)

    def rl2(lines, key, lab):
        trn, tst = split(lines)
        L4 = lambda X: [t for t in X if len(t) >= 4]
        b, nb = pred_acc(L4(trn), L4(tst), lambda t: t[-2:], lambda t: t[-3])
        f, nf = pred_acc(L4(trn), L4(tst), lambda t: t[:2], lambda t: t[2])
        rd.rec(key, 'the end determines backwards%s' % lab, 'third-from-last %.1f%% (%d), third %.1f%% (%d); threshold +5 points' % (100 * b, nb, 100 * f, nf), b - f >= 0.05)
    rl2(DL, 'RL2', '')
    rl2(sorted({tuple(t) for t in B}), 'RL3', ' (B)')
    Fn = [r for r in F if r['type'] != 'TAB:C']
    rl2(sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln}), 'RL4', " (F')")

    def profile(lines, from_end):
        L = [t for t in lines if len(t) >= 4]
        return [ent(Counter((t[-1 - k] if from_end else t[k]) for t in L)) for k in range(4)]
    nl = [t for t in DL if genre(t) == 'name']
    pf = profile(nl, False)
    rd.rec('RL5', 'names are fixed at the end, free at the start', 'entropy by position from the start: %s' % ', '.join('%.2f' % x for x in pf) +
           '; last-position entropy %.2f' % profile(nl, True)[0], profile(nl, True)[0] < min(pf) and pf[0] == max(pf + [profile(nl, True)[0]]))
    pe = profile(DL, True)
    rd.rec('RL6', 'predictability falls away from the end', 'entropy from the end: %s' % ', '.join('%.2f' % x for x in pe[:3]), pe[0] < pe[1] < pe[2])
    cl = [t for t in DL if genre(t) == 'count']
    pc = profile(cl, True)
    ps = profile(cl, False)
    rd.rec('RL7', 'counts are fixed at the end too', 'count lines: last %.2f; by position from start %s' % (pc[0], ', '.join('%.2f' % x for x in ps)), pc[0] < min(ps[:3]))

    def rl8(lines, key, lab):
        trn, tst = split(lines)
        L3 = lambda X: [t for t in X if len(t) >= 3]
        b, nb = pred_acc(L3(trn), L3(tst), lambda t: t[-1], lambda t: t[-2])
        f, nf = pred_acc(L3(trn), L3(tst), lambda t: t[0], lambda t: t[1])
        rd.rec(key, 'the last sign calls its neighbour%s' % lab, 'second-last %.1f%%, second %.1f%%; threshold +5 points' % (100 * b, 100 * f), b - f >= 0.05)
    rl8(DL, 'RL8', '')
    rl8(sorted({tuple(t) for t in B}), 'RL9', ' (B)')
    rd.finish()


if __name__ == '__main__':
    main()
