"""Two-hundred-and-seventy-third registered prediction set (PREDICTIONS.md, GZ1-GZ4): decipherment loop 98, three more
grammar rules for lines parse11 leaves unparsed, each scored by the G margin (grammar.margin), A and B.
  NAME-COUNT  a name (lexical body + 740 / 520), then a numeral run and 0-2 lexical signs
  PRE-NAME    1-2 lexical signs, 400 / 90, then a rest that parses as a name
  TWO-400     exactly two lexical signs, then 400
Writes results/predict_test273.md."""
from collections import Counter

import rtools as R
from grammar import CAGED, head_stats, heads_from, lexical, margin, parse11
from predict_test103 import CL
from predict_test108 import genre
from predict_test215 import slots
from signs import load


def multi(t):
    k = n = 0
    while k < len(t):
        j = k
        while j < len(t) and t[j] in R.NUMS:
            j += 1
        if j == k or j >= len(t) or not lexical(t[j]):
            return False
        k, n = j + 1, n + 1
    return n >= 2


def count_n(t, s, lo, hi):
    k = s
    while k < len(t) and t[k] in R.NUMS:
        k += 1
    return k > s and lo <= len(t) - k <= hi and all(lexical(g) for g in t[k:])


def label_any(t):
    if len(t) < 2 or not lexical(t[0]) or t[1] not in R.NUMS:
        return False
    k = 1
    while k < len(t) and t[k] in R.NUMS:
        k += 1
    return len(t) - k <= 2 and all(lexical(g) for g in t[k:])


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-seventy-third registered predictions: decipherment loop 98, three more grammar rules', 'predict_test273')
    import progress as P
    DL, tr, te = P.data()
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    heads = heads_from(DL)
    hc, mc = head_stats(DL)
    DA = sorted({tuple(t) for t in A})
    labels = {g for g, v in Counter(sl[0] for sl in (slots(t) for t in DA if genre(t) == 'count') if sl).most_common(10)}
    occ = Counter(g for t in DA for g in t)
    hd = Counter(t[i - 1] for t in DA for i, g in enumerate(t) if g in R.END and i > 0)
    low = {g for g in occ if occ[g] >= 3 and hd[g] / occ[g] < 0.05 and lexical(g)}
    last = Counter(t[-1] for t in DA)
    endp = {g for g in occ if occ[g] >= 5 and last[g] / occ[g] >= 0.5 and lexical(g)}
    first = Counter(t[0] for t in DA)
    openp = {g for g in occ if occ[g] >= 5 and first[g] / occ[g] >= 0.5 and lexical(g)}
    p8 = lambda t: parse11(t, heads, hc, mc, labels, low, endp, openp)
    base = lambda t: p8(t) is not None
    mA, mB = margin(DL, base), margin(DB, base)
    rd.say('- parse11 margin: A %.1f, B %.1f.' % (100 * mA, 100 * mB))
    H = {g for g in hc if hc[g] >= 5 and hc[g] > mc[g] and lexical(g)}
    rules = {
        'NAME-COUNT': lambda t: any(t[k] in R.END and all(lexical(g) or g in R.NUMS for g in t[:k]) and count_n(t, k + 1, 0, 2) for k in range(1, len(t) - 1)),
        'PRE-NAME': lambda t: any(t[k] in ('400', '90') and all(lexical(g) for g in t[:k]) and p8(t[k + 1:]) == 'name' for k in (1, 2) if k < len(t) - 1),
        'TWO-400': lambda t: len(t) == 3 and lexical(t[0]) and lexical(t[1]) and t[2] == '400',
    }
    keep = []
    for k, (name, f) in enumerate(rules.items()):
        g = lambda t, f=f: base(t) or f(tuple(t))
        a, b = margin(DL, g), margin(DB, g)
        ok = a - mA >= 0.003 and b > mB
        rd.rec('GZ%d' % (k + 1), '%s raises the margin on A by 0.3 point or more and on B' % name, 'A %.2f -> %.2f; B %.2f -> %.2f' % (100 * mA, 100 * a, 100 * mB, 100 * b), ok)
        if ok:
            keep.append(f)
    g = lambda t: base(t) or any(f(tuple(t)) for f in keep)
    a, b = margin(DL, g), margin(DB, g)
    rd.rec('GZ4', 'progress rule: the held rules together raise the margin on A (0.3+) and B', 'A %.2f -> %.2f; B %.2f -> %.2f (%d rules)' % (100 * mA, 100 * a, 100 * mB, 100 * b, len(keep)), bool(keep) and a - mA >= 0.003 and b > mB)
    rd.finish()


if __name__ == '__main__':
    main()
