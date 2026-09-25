"""Two-hundred-and-sixty-first registered prediction set (PREDICTIONS.md, GR1-GR4): decipherment loop 86, three grammar
rules for lines parse6 leaves unparsed, each scored by the G margin (real minus within-line shuffled, grammar.margin).
  CAGE-OPEN  a caged sign opens the line; the rest (2+ signs) parses as a name
  MID-POST   1-3 lexical signs, then 400 / 90, then a rest that parses
  NAME-NAME  a name (body + 740 / 520) followed by a rest that parses as a name
Writes results/predict_test261.md."""
from collections import Counter

import rtools as R
from grammar import CAGED, head_stats, heads_from, lexical, margin, parse6
from predict_test108 import genre
from predict_test215 import slots
from signs import load

NAMES = ('name', 'formula', 'bare')


def setup(DL):
    heads = heads_from(DL)
    hc, mc = head_stats(DL)
    DA = sorted({tuple(t) for t in R.load_all()[0]})
    labels = {g for g, v in Counter(sl[0] for sl in (slots(t) for t in DA if genre(t) == 'count') if sl).most_common(10)}
    occ = Counter(g for t in DA for g in t)
    hd = Counter(t[i - 1] for t in DA for i, g in enumerate(t) if g in R.END and i > 0)
    low = {g for g in occ if occ[g] >= 3 and hd[g] / occ[g] < 0.05 and lexical(g)}
    p6 = lambda t: parse6(t, heads, hc, mc, labels, low)
    return p6


def rules(p6):
    def cage_open(t):
        return len(t) >= 3 and t[0] in CAGED and p6(t[1:]) in NAMES

    def mid_post(t):
        for k in range(1, min(4, len(t) - 1)):
            if t[k] in ('400', '90') and all(lexical(g) for g in t[:k]) and len(t) - k - 1 >= 2 and p6(t[k + 1:]) is not None:
                return True
        return False

    def name_name(t):
        for k in range(1, len(t) - 2):
            if t[k] in R.END and p6(t[:k + 1]) == 'name' and p6(t[k + 1:]) in NAMES:
                return True
        return False
    return {'CAGE-OPEN': cage_open, 'MID-POST': mid_post, 'NAME-NAME': name_name}


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-sixty-first registered predictions: decipherment loop 86, three grammar rules for unparsed lines', 'predict_test261')
    import progress as P
    DL, tr, te = P.data()
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    p6 = setup(DL)
    base = lambda t: p6(t) is not None
    mA, mB = margin(DL, base), margin(DB, base)
    rd.say('- parse6 margin: A %.1f, B %.1f.' % (100 * mA, 100 * mB))
    rs = rules(p6)
    keep = []
    for k, (name, f) in enumerate(rs.items()):
        g = lambda t, f=f: base(t) or f(tuple(t))
        a, b = margin(DL, g), margin(DB, g)
        ok = a - mA >= 0.003 and b > mB
        rd.rec('GR%d' % (k + 1), '%s raises the margin on A by 0.3 point or more and on B' % name, 'A %.1f -> %.1f; B %.1f -> %.1f' % (100 * mA, 100 * a, 100 * mB, 100 * b), ok)
        if ok:
            keep.append(f)
    g = lambda t: base(t) or any(f(tuple(t)) for f in keep)
    a, b = margin(DL, g), margin(DB, g)
    rd.rec('GR4', 'progress rule: the held rules together raise the margin on A (0.3+) and B', 'A %.1f -> %.1f; B %.1f -> %.1f (%d rules)' % (100 * mA, 100 * a, 100 * mB, 100 * b, len(keep)), bool(keep) and a - mA >= 0.003 and b > mB)
    rd.finish()


if __name__ == '__main__':
    main()
