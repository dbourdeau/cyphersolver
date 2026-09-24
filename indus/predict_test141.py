"""Hundred-and-forty-first registered prediction set (PREDICTIONS.md, TY1-TY10): language type from sign order.
Writes results/predict_test141.md."""
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test103 import CL
from predict_test112 import runs

M = set(R.END) | set(CL) | {'400', '90'}


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-forty-first registered predictions: language type from sign order', 'predict_test141')
    DL = sorted({tuple(t) for t in AB})
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    heads = {b[-1] for b, e in ns}
    lex = lambda g: g not in R.NUMS and g not in M
    aft = bef = 0
    for b, e in ns:
        for i, j, r in runs(b):
            if j < len(b) and lex(b[j]):
                aft += 1
            elif i > 0 and lex(b[i - 1]):
                bef += 1
    rd.rec('TY1', 'numeral before the counted sign', 'runs with a lexical sign after %d, before only %d' % (aft, bef), aft >= 2 * bef and aft > 0)
    a = [t[i + 1] in heads for t in DL for i in range(len(t) - 1) if t[i] == '740' and lex(t[i + 1])]
    c = [t[i] in heads for t in DL for i in range(1, len(t) - 1) if lex(t[i]) and t[i - 1] != '740']
    p = R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))
    rd.rec('TY2', 'a preposed genitive', 'sign after an inner 740 is a head %s' % R.fl(sum(a), len(a), sum(c), len(c), p),
           p < 0.05 and sum(a) / max(1, len(a)) > sum(c) / max(1, len(c)) and sum(a) >= 0.5 * len(a))
    po = Counter()
    for t in DL:
        ms = [g for g in t if g in M]
        seen = set()
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                if ms[i] != ms[j] and (ms[i], ms[j]) not in seen:
                    seen.add((ms[i], ms[j]))
                    po[(ms[i], ms[j])] += 1
    pairs = {tuple(sorted(k)) for k in po}
    maj = sum(max(po[(x, y)], po[(y, x)]) for x, y in pairs)
    tot = sum(po[(x, y)] + po[(y, x)] for x, y in pairs)
    mixed = sorted(((min(po[(x, y)], po[(y, x)]), x, y) for x, y in pairs), reverse=True)[:6]
    rd.thr('TY3', 'rigid marker order', 'marker co-occurrences in the majority order (most mixed: %s)' % ', '.join(
        '%s/%s %d:%d' % (x, y, po[(x, y)], po[(y, x)]) for _, x, y in mixed), maj, tot, 0.95)
    dbl = [(t, i) for t in DL for i in range(len(t) - 1) if t[i] == t[i + 1] and lex(t[i])]
    rd.thr('TY4', 'reduplication exists', 'distinct lines with a doubled lexical sign (%s)' % dict(Counter(t[i] for t, i in dbl).most_common(6)),
           len({t for t, i in dbl}), len(DL), 0.01)
    hd = 0
    nd = 0
    for b, e in ns:
        for i in range(len(b) - 1):
            if b[i] == b[i + 1] and lex(b[i]):
                nd += 1
                hd += i + 1 == len(b) - 1
    rd.thr('TY5', 'reduplication marks the head', 'doubled signs in name bodies whose second copy is the head', hd, nd, 0.5)
    em = [t for t in DL if t and t[-1] in M]
    # markers only: numerals after the last lexical sign are not counted
    tail = lambda t: sum(g in M for g in t[max([i for i, g in enumerate(t) if lex(g)] + [-1]) + 1:])
    rd.thr('TY6', 'agglutinative chains', 'marker-final lines with 3+ markers after the last lexical sign (%s)' % dict(Counter(tail(t) for t in em)),
           sum(tail(t) >= 3 for t in em), len(em), 0.01)
    b3 = [b for b, e in ns if len(b) >= 3]
    rd.thr('TY7', 'markers close the whole name', 'names of 3+ with 740 or 520 inside the body', sum(any(g in R.END for g in b[:-1]) for b in b3), len(b3), 0.02, above=False)
    op = Counter(b[0] for b in b3)
    top = sum(n for g, n in op.most_common(10))
    rd.thr('TY8', 'openers are lexical', 'bodies covered by the ten commonest openers (%s)' % dict(op.most_common(10)), top, len(b3), 0.5, above=False)
    ch = n9 = 0
    for b, e in ns:
        for i, j, r in runs(b):
            if j < len(b) and lex(b[j]):
                n9 += 1
                ch += j == len(b) - 1
    rd.thr('TY9', 'the counted sign is the head', 'lexical signs after a numeral run that are the body head', ch, n9, 0.5)
    one, many = [], []
    for b, e in ns:
        rs = [(i, j, r) for i, j, r in runs(b) if j == len(b) - 1]
        if rs and lex(b[-1]):
            v = sum(R.NUMS[g][0] for g in rs[-1][2])
            (one if v == 1 else many).append(e == '740')
    p = min(1, 2 * min(R.hyper_ge(sum(one), len(one) - sum(one), sum(many), len(many) - sum(many)),
                       R.fisher_less(sum(one), len(one) - sum(one), sum(many), len(many) - sum(many))))
    rd.rec('TY10', 'no number agreement', 'ending 740, value 1 %s' % R.fl(sum(one), len(one), sum(many), len(many), p), p >= 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
