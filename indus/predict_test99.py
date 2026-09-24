"""Ninety-ninth registered prediction set (PREDICTIONS.md, PZ1-PZ20): position specialists. Writes
results/predict_test99.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test81 import classes_of
from signs import FISH

random.seed(119)
HEAD = ('817', '820', '861')


def roles(lines, k=10):
    c, ini, fin = Counter(), Counter(), Counter()
    for t in lines:
        if len(t) < 2:
            continue
        for i, g in enumerate(t):
            c[g] += 1
            ini[g] += i == 0
            fin[g] += i == len(t) - 1
    out = {}
    for g in c:
        if c[g] >= k and g not in R.NUMS:
            out[g] = 'I' if ini[g] / c[g] >= 0.7 else ('F' if fin[g] / c[g] >= 0.7 else 'M')
    return out, c, ini, fin


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Ninety-ninth registered predictions: position specialists', 'predict_test99')
    DL = [t for t in sorted({tuple(t) for t in AB}) if len(t) >= 2]
    ro, c, ini, fin = roles(DL)
    I = sorted(g for g in ro if ro[g] == 'I')
    Fi = sorted(g for g in ro if ro[g] == 'F')
    M = [g for g in ro if ro[g] == 'M']
    rd.say('- signs %d; initial %s; final %s.' % (len(ro), ', '.join(I), ', '.join(Fi)))
    rd.say()
    rd.thr('PZ1', 'some signs have a place', 'specialists', len(I) + len(Fi), len(ro), 0.2)
    rd.rec('PZ2', 'more closers than openers', 'final %d, initial %d' % (len(Fi), len(I)), len(Fi) > len(I))
    rn, ln_ = defaultdict(set), defaultdict(set)
    for t in DL:
        for i, g in enumerate(t):
            if i + 1 < len(t):
                rn[g].add(t[i + 1])
            if i > 0:
                ln_[g].add(t[i - 1])
    rd.rank('PZ3', 'openers open onto anything', 'initial against medial, right neighbours per token', [len(rn[g]) / c[g] for g in I], [len(rn[g]) / c[g] for g in M])
    rd.rank('PZ4', 'closers close anything', 'final against medial, left neighbours per token', [len(ln_[g]) / c[g] for g in Fi], [len(ln_[g]) / c[g] for g in M])
    heads = {b[-1] for b, e in T.names(AB) if b}
    rd.thr('PZ5', 'closers are heads or endings', 'final specialists that are heads or endings', sum(g in heads or g in R.END for g in Fi), len(Fi), 0.7)
    rd.rec('PZ6', 'the headings are openers', 'heading signs among initial specialists: %s' % [h for h in HEAD if h in I], all(h in I for h in HEAD))
    tk = [(t, i) for t in DL for i in range(len(t))]
    nx = lambda t, i: i + 1 < len(t) and t[i + 1] in R.NUMS
    pv = lambda t, i: i > 0 and t[i - 1] in R.NUMS
    rd.gtl('PZ7', 'openers precede numbers', 'numeral after, initial specialists', [nx(t, i) for t, i in tk if t[i] in I], [nx(t, i) for t, i in tk if t[i] in M])
    rd.gtl('PZ8', 'closers follow numbers', 'numeral before, final specialists', [pv(t, i) for t, i in tk if t[i] in Fi], [pv(t, i) for t, i in tk if t[i] in M])
    rA = roles([t for t in sorted({tuple(t) for t in A}) if len(t) >= 2])[0]
    rB = roles([t for t in sorted({tuple(t) for t in B}) if len(t) >= 2])[0]
    both = [g for g in rA if g in rB]
    rd.thr('PZ9', 'places hold across transcriptions', 'same role in A and B', sum(rA[g] == rB[g] for g in both), len(both), 0.8)
    Fn = [r for r in F if r['type'] != 'TAB:C']
    fl = lambda site: [tuple(ln) for ln in sorted({tuple(ln) for r in Fn if r['site'].strip() == site for ln in r['seq'] if len(ln) >= 2})]
    rM, rH = roles(fl('Mohenjo-daro'))[0], roles(fl('Harappa'))[0]
    b2 = [g for g in rM if g in rH]
    rd.thr('PZ10', 'places hold across cities', 'same role at both', sum(rM[g] == rH[g] for g in b2), len(b2), 0.7)
    ft = [(r['type'][:3], g) for r in Fn for ln in r['seq'] for g in ln]
    rd.gtl('PZ11', 'closers are tablet signs', 'tablet, final specialists', [ty == 'TAB' for ty, g in ft if g in Fi], [ty == 'TAB' for ty, g in ft if g in M])
    rd.gtl('PZ12', 'openers are seal signs', 'seal, initial specialists', [ty == 'SEA' for ty, g in ft if g in I], [ty == 'SEA' for ty, g in ft if g in M])
    rd.rank('PZ13', 'closers are common', 'final against medial tokens', [c[g] for g in Fi], [c[g] for g in M])
    rd.rank('PZ14', 'openers are rare', 'medial against initial tokens', [c[g] for g in M], [c[g] for g in I])
    rd.rank('PZ15', 'opened lines are long', 'with against without an initial specialist', [len(t) for t in DL if t[0] in I], [len(t) for t in DL if t[0] not in I])
    rd.rank('PZ16', 'closed lines are short', 'other against final-specialist endings', [len(t) for t in DL if t[-1] not in Fi], [len(t) for t in DL if t[-1] in Fi])
    fs = lambda X: [i == len(t) - 1 for t in X for i in range(len(t)) if t[i] in Fi]
    rd.gtl('PZ17', 'closers close formulas harder', 'final, formula tokens', fs([t for t in DL if nonname(list(t))]), fs([t for t in DL if R.name_of(list(t))]))
    cl = classes_of(sorted({(b, e) for b, e in T.names(AB) if b}))
    rd.thr('PZ18', 'closers are the 520 class, suffixes or endings', 'final specialists that are 520-class, 400/90/151 or endings',
           sum(cl.get(g) == '520' or g in ('400', '90', '151') or g in R.END for g in Fi), len(Fi), 0.5)
    ff = [g for g in ro if g in FISH]
    rd.thr('PZ19', 'fish sit inside', 'fish types that are medial', sum(ro[g] == 'M' for g in ff), len(ff), 0.8)
    IB = [g for g in rB if rB[g] == 'I']
    FB = [g for g in rB if rB[g] == 'F']
    rd.rec('PZ20', 'more closers than openers (B)', 'final %d, initial %d' % (len(FB), len(IB)), len(FB) > len(IB))
    rd.finish()


if __name__ == '__main__':
    main()
