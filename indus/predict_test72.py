"""Seventy-second registered prediction set (PREDICTIONS.md, NA1-NA20): does the ending agree with the number? Writes
results/predict_test72.md. All name counts are over distinct (body, ending) names."""
import math
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from signs import FISH

random.seed(92)


def cval(b):
    """(value, kind) of the numeral run directly before the head, or None."""
    if len(b) < 2 or b[-1] in R.NUMS or b[-2] not in R.NUMS:
        return None
    j = len(b) - 2
    while j > 0 and b[j - 1] in R.NUMS:
        j -= 1
    return sum(R.NUMS[g][0] for g in b[j:-1]), R.kind(b[-2])


def hcond(xs, ys):
    """H(Y|X) in bits."""
    n = len(xs)
    cx = Counter(xs)
    cxy = Counter(zip(xs, ys))
    return -sum(v / n * math.log2(v / cx[x]) for (x, _), v in cxy.items())


def cmi(hs, ps, es):
    return hcond(hs, es) - hcond(list(zip(hs, ps)), es)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Seventy-second registered predictions: does the ending agree with the number?', 'predict_test72')
    ns = {(b, e) for b, e in T.names(AB) if b}
    is5 = lambda e: e == '520'
    cf = [(cval(b)[0], e) for b, e in ns if b[-1] in FISH and cval(b)]
    rd.say('- distinct names %d; counted fish heads %d (values %s).' % (len(ns), len(cf), dict(Counter(v for v, _ in cf))))
    rd.say()
    rd.gtl('NA1', 'two fish take 520, three take 740', '520, value 2', [is5(e) for v, e in cf if v == 2], [is5(e) for v, e in cf if v >= 3])
    rd.gtl('NA2', 'two against one', '520, value 2', [is5(e) for v, e in cf if v == 2], [is5(e) for v, e in cf if v == 1])
    rd.gtl('NA3', 'two against uncounted', '520, value 2', [is5(e) for v, e in cf if v == 2],
           [is5(e) for b, e in ns if b[-1] in FISH and not cval(b)])

    def na1(names, key, lab):
        c = [(cval(b)[0], e) for b, e in names if b and b[-1] in FISH and cval(b)]
        rd.gtl(key, 'value 2 against 3+ %s' % lab, '520, value 2', [is5(e) for v, e in c if v == 2], [is5(e) for v, e in c if v >= 3])
    na1({(b, e) for b, e in T.names(B)}, 'NA4', 'in B')
    fs = lambda site: {(b, e) for r in F if r['site'].strip() == site for b, e in R.names_in(r)}
    na1(fs('Harappa'), 'NA5', 'at Harappa')
    na1(fs('Mohenjo-daro'), 'NA6', 'at Mohenjo-daro')
    ch = [(b[-1], cval(b)[0], e) for b, e in ns if cval(b)]
    rd.gtl('NA7', 'value 2 takes 520 on any head', '520, value 2', [is5(e) for h, v, e in ch if v == 2], [is5(e) for h, v, e in ch if v != 2])
    hv = defaultdict(set)
    for h, v, e in ch:
        hv[h].add(v == 2)
    rd.strat('NA8', 'the value effect within heads', 'by head: 520, value 2 minus other', [(v == 2, h, 1 if is5(e) else 0) for h, v, e in ch if len(hv[h]) == 2])
    vb = lambda v: min(v, 4)
    rd.mi('NA9', 'the value sets the ending', 'counted heads', [vb(v) for h, v, e in ch], [e for h, v, e in ch])
    inner = []
    for b, e in ns:
        for i in range(1, len(b) - 1):
            if b[i] not in R.NUMS and b[i - 1] in R.NUMS and i != len(b) - 1:
                j = i - 1
                while j > 0 and b[j - 1] in R.NUMS:
                    j -= 1
                inner.append((sum(R.NUMS[g][0] for g in b[j:i]) == 2, e))
                break
    a = [is5(e) for t, e in inner if t]
    c = [is5(e) for t, e in inner if not t]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('NA10', 'control: a number elsewhere does not matter', '520, value 2 inside the body %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p >= 0.05)

    def paired(key, title, val, want5):
        w = l_ = 0
        heads = {h for h, v, e in ch if v == val}
        for h in heads:
            cc = [is5(e) for b, e in ns if b[-1] == h and cval(b) and cval(b)[0] == val]
            uu = [is5(e) for b, e in ns if b[-1] == h and not cval(b)]
            if not uu:
                continue
            d = sum(cc) / len(cc) - sum(uu) / len(uu)
            if not want5:
                d = -d
            w += d > 0
            l_ += d < 0
        p_ = R.binom_ge(w, w + l_)
        rd.rec(key, title, 'heads in the predicted direction %d, against %d; p = %.4f' % (w, l_, p_), w > l_ and p_ < 0.05)
    paired('NA11', 'the 2 form takes 520', 2, True)
    paired('NA12', 'the 3 form takes 740', 3, False)
    rd.mi('NA13', 'the notation sets the ending', 'counted heads', [cval(b)[1] for b, e in ns if cval(b)], [e for b, e in ns if cval(b)])
    fh = [(b[-2], e) for b, e in ns if len(b) >= 2 and b[-1] in FISH]
    rd.gtl('NA14', '415 + fish takes 520', '520, after 415', [is5(e) for p_, e in fh if p_ == '415'], [is5(e) for p_, e in fh if p_ != '415'])
    rd.gtl('NA15', '235 + fish takes 740', '740, after 235', [not is5(e) for p_, e in fh if p_ == '235'], [not is5(e) for p_, e in fh if p_ != '235'])

    def cmitest(key, title, names):
        hs = [b[-1] for b, e in names]
        ps = [b[-2] for b, e in names]
        es = [e for b, e in names]
        obs = cmi(hs, ps, es)
        grp = defaultdict(list)
        for i, h in enumerate(hs):
            grp[h].append(i)
        ge = 0
        for _ in range(R.N):
            pp = ps[:]
            for ii in grp.values():
                v = [ps[i] for i in ii]
                random.shuffle(v)
                for i, x in zip(ii, v):
                    pp[i] = x
            ge += cmi(hs, pp, es) >= obs
        p_ = (ge + 1) / (R.N + 1)
        rd.rec(key, title, 'names %d; conditional MI %.3f bits; p = %.4f' % (len(names), obs, p_), p_ < 0.05)
    cmitest('NA16', 'the neighbour matters for fish heads', [(b, e) for b, e in ns if len(b) >= 2 and b[-1] in FISH])
    cmitest('NA17', 'the neighbour matters for other heads', [(b, e) for b, e in ns if len(b) >= 2 and b[-1] not in FISH])
    kk = [cval(b)[1] for b, e in ns if b[-1] in FISH and cval(b)]
    rd.thr('NA18', 'fish are counted with strokes', 'short numerals before a fish head', sum(k == 'short' for k in kk), len(kk), 0.9)
    c2 = lambda site: {b for b, e in fs(site) if e == '520' and b[-1] in FISH and cval(b) and cval(b)[0] == 2}
    m, h = c2('Mohenjo-daro'), c2('Harappa')
    rd.rec('NA19', 'two-fish-520 in both cities', 'distinct bodies: Mohenjo-daro %d, Harappa %d; threshold 3 each' % (len(m), len(h)), len(m) >= 3 and len(h) >= 3)
    ff = []
    for t in AB:
        if nonname(t):
            for i in range(1, len(t)):
                if t[i] in FISH and t[i - 1] in R.NUMS and R.NUMS[t[i - 1]][0] in (2, 3) and not (i >= 2 and t[i - 2] in R.NUMS):
                    ff.append((R.NUMS[t[i - 1]][0], i == len(t) - 1))
    rd.gtl('NA20', 'two fish close formulas', 'line-final, fish after 2 in formulas', [x for v, x in ff if v == 2], [x for v, x in ff if v == 3])
    rd.finish()


if __name__ == '__main__':
    main()
