"""Two-hundred-and-sixty-second registered prediction set (PREDICTIONS.md, GE1-GE4): decipherment loop 87, three more
grammar rules for lines parse8 leaves unparsed, each scored by the G margin (grammar.margin), A and B.
  END-PRONE   1+ lexical signs, then a sign that ends 50%+ of its 5+ A occurrences (not already an ending or closer)
  CLOSER-740  1+ lexical signs, a closer, then 740
  TWO-BARE    exactly two lexical signs, the second a name head at least once in A
Writes results/predict_test262.md."""
from collections import Counter

import rtools as R
from grammar import head_stats, heads_from, lexical, margin, parse8
from predict_test103 import CL
from predict_test108 import genre
from predict_test215 import slots
from signs import load


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-sixty-second registered predictions: decipherment loop 87, three more grammar rules', 'predict_test262')
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
    p8 = lambda t: parse8(t, heads, hc, mc, labels, low)
    last = Counter(t[-1] for t in DA)
    endp = {g for g in occ if occ[g] >= 5 and last[g] / occ[g] >= 0.5 and lexical(g)}
    rd.say('- end-prone signs (%d): %s.' % (len(endp), ' '.join(sorted(endp, key=lambda g: -occ[g]))))
    base = lambda t: p8(t) is not None
    mA, mB = margin(DL, base), margin(DB, base)
    rd.say('- parse8 margin: A %.1f, B %.1f.' % (100 * mA, 100 * mB))
    rules = {
        'END-PRONE': lambda t: len(t) >= 2 and t[-1] in endp and all(lexical(g) for g in t[:-1]),
        'CLOSER-740': lambda t: len(t) >= 3 and t[-1] == '740' and t[-2] in CL and all(lexical(g) for g in t[:-2]),
        'TWO-BARE': lambda t: len(t) == 2 and lexical(t[0]) and lexical(t[1]) and t[1] in heads,
    }
    keep = []
    for k, (name, f) in enumerate(rules.items()):
        g = lambda t, f=f: base(t) or f(tuple(t))
        a, b = margin(DL, g), margin(DB, g)
        ok = a - mA >= 0.003 and b > mB
        rd.rec('GE%d' % (k + 1), '%s raises the margin on A by 0.3 point or more and on B' % name, 'A %.2f -> %.2f; B %.2f -> %.2f' % (100 * mA, 100 * a, 100 * mB, 100 * b), ok)
        if ok:
            keep.append(f)
    g = lambda t: base(t) or any(f(tuple(t)) for f in keep)
    a, b = margin(DL, g), margin(DB, g)
    rd.rec('GE4', 'progress rule: the held rules together raise the margin on A (0.3+) and B', 'A %.2f -> %.2f; B %.2f -> %.2f (%d rules)' % (100 * mA, 100 * a, 100 * mB, 100 * b, len(keep)), bool(keep) and a - mA >= 0.003 and b > mB)
    rd.finish()


if __name__ == '__main__':
    main()
