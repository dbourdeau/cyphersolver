"""Two-hundred-and-seventy-seventh registered prediction set (PREDICTIONS.md, GO1-GO4): decipherment loop 102, three more
grammar rules for lines parse11 leaves unparsed, each scored by the G margin (grammar.margin), A and B.
  CLOSER-OPEN  a closer sign opens the line; the rest (2+ signs) parses as a name (as CAGE-OPEN, set 261)
  POST-OPEN    400 / 90 opens the line; the rest parses as a name
  ENDING-OPEN  740 / 520 opens the line; the rest parses as a name
Writes results/predict_test277.md."""
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
    rd = R.Round('Two-hundred-and-seventy-seventh registered predictions: decipherment loop 102, three more grammar rules', 'predict_test277')
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
        'CLOSER-OPEN': lambda t: len(t) >= 3 and t[0] in CL and p8(t[1:]) in ('name', 'formula', 'bare'),
        'POST-OPEN': lambda t: len(t) >= 3 and t[0] in ('400', '90') and p8(t[1:]) in ('name', 'formula', 'bare'),
        'ENDING-OPEN': lambda t: len(t) >= 3 and t[0] in R.END and p8(t[1:]) in ('name', 'formula', 'bare'),
    }
    keep = []
    for k, (name, f) in enumerate(rules.items()):
        g = lambda t, f=f: base(t) or f(tuple(t))
        a, b = margin(DL, g), margin(DB, g)
        ok = a - mA >= 0.003 and b > mB
        rd.rec('GO%d' % (k + 1), '%s raises the margin on A by 0.3 point or more and on B' % name, 'A %.2f -> %.2f; B %.2f -> %.2f' % (100 * mA, 100 * a, 100 * mB, 100 * b), ok)
        if ok:
            keep.append(f)
    g = lambda t: base(t) or any(f(tuple(t)) for f in keep)
    a, b = margin(DL, g), margin(DB, g)
    rd.rec('GO4', 'progress rule: the held rules together raise the margin on A (0.3+) and B', 'A %.2f -> %.2f; B %.2f -> %.2f (%d rules)' % (100 * mA, 100 * a, 100 * mB, 100 * b, len(keep)), bool(keep) and a - mA >= 0.003 and b > mB)
    rd.finish()


if __name__ == '__main__':
    main()
