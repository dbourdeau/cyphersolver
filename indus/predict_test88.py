"""Eighty-eighth registered prediction set (PREDICTIONS.md, TN1-TN20): lines with two names. Writes
results/predict_test88.md. Distinct lines."""
import random
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test4 import OPEN
from predict_test44 import nonname
from predict_test76 import fcounted

random.seed(108)
HEAD = ('817', '820', '861')


def split2(t):
    t = list(t)
    ends = [i for i, g in enumerate(t) if g in R.END]
    if len(ends) != 2:
        return None
    s = 2 if len(t) >= 3 and t[0] in OPEN and t[1] in ('2', '60', '1') else 0
    a = tuple(t[s:ends[0]])
    j = ends[0] + 1
    fol = t[j] if j < len(t) and t[j] in ('400', '90', '151') else None
    if fol:
        j += 1
    b = tuple(t[j:ends[1]])
    if not a or not b:
        return None
    return a, t[ends[0]], fol, b, t[ends[1]]


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Eighty-eighth registered predictions: lines with two names', 'predict_test88')
    DL = sorted({tuple(t) for t in AB})
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    bodies = {b for b, e in ns}
    one = [t for t in DL if sum(g in R.END for g in t) == 1 and R.name_of(list(t)) and R.name_of(list(t))[0]]
    tw = [(t, split2(t)) for t in DL if split2(t)]
    wend = [t for t in DL if any(g in R.END for g in t)]
    rd.say('- two-name lines %d; one-name lines %d.' % (len(tw), len(one)))
    rd.say()
    rd.thr('TN1', 'two names happen', 'two-name lines among lines with an ending', len(tw), len(wend), 0.02)
    rd.thr('TN2', 'both parts are names', 'both segments attested bodies', sum(s[0] in bodies and s[3] in bodies for t, s in tw), len(tw), 0.3)

    def tn3(rows, key, lab):
        x = sum(len(s[3]) < len(s[0]) for t, s in rows)
        y = sum(len(s[3]) > len(s[0]) for t, s in rows)
        p = R.binom_ge(x, x + y)
        rd.rec(key, 'the second part is shorter%s' % lab, 'shorter %d, longer %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
    tn3(tw, 'TN3', '')
    bl = [b for b in bodies]

    def pair_test(key, title, f):
        obs = sum(f(s[0], s[3]) for t, s in tw)
        ge = 0
        for _ in range(R.N):
            k = sum(f(random.choice(bl), random.choice(bl)) for _ in tw)
            ge += k >= obs
        p = (ge + 1) / (R.N + 1)
        rd.rec(key, title, 'lines %d; sharing %d; p = %.4f' % (len(tw), obs, p), p < 0.05)
    pair_test('TN4', 'the two share a head', lambda a, b: a[-1] == b[-1])
    pair_test('TN5', 'the two share an opener', lambda a, b: a[0] == b[0])
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in F for ln in r['seq'] if ln})
    kind = lambda t: 'two' if split2(t) else ('one' if sum(g in R.END for g in t) == 1 and R.name_of(list(t)) and R.name_of(list(t))[0] else None)
    fk = [(s, ty, kind(t)) for s, ty, t in FD if kind(t)]
    rd.ltl('TN6', 'two names are not on seals', 'seal, two-name lines', [ty == 'SEA' for s, ty, k in fk if k == 'two'], [ty == 'SEA' for s, ty, k in fk if k == 'one'])
    rd.gtl('TN7', 'two names at Mohenjo-daro', 'Mohenjo-daro, two-name lines', [s == 'Mohenjo-daro' for s, ty, k in fk if k == 'two'], [s == 'Mohenjo-daro' for s, ty, k in fk if k == 'one'])
    rd.thr('TN8', 'the first ending is 740', 'first ending 740', sum(s[1] == '740' for t, s in tw), len(tw), 0.9)
    rd.thr('TN9', 'a suffix separates the names', 'first ending followed by 400/90/151 (%s)' % dict(Counter(s[2] for t, s in tw)),
           sum(bool(s[2]) for t, s in tw), len(tw), 0.2)
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    rd.gtl('TN10', 'two-name lines are titled', 'heading unit, two-name lines', [hu(t) for t, s in tw], [hu(t) for t in one])
    top = {h for h, _ in Counter(b[-1] for b, e in ns).most_common(10)}
    x = sum(s[3][-1] in top and s[0][-1] not in top for t, s in tw)
    y = sum(s[0][-1] in top and s[3][-1] not in top for t, s in tw)
    p = R.binom_ge(x, x + y)
    rd.rec('TN11', 'the second part names a role', 'second only %d, first only %d; p = %.4f' % (x, y, p), x > y and p < 0.05)

    def tn12(rows, key, lab):
        rd.thr(key, 'the second part is one sign%s' % lab, 'one-sign second segments', sum(len(s[3]) == 1 for t, s in rows), len(rows), 0.3)
    tn12(tw, 'TN12', '')
    c2 = Counter(s[3] for t, s in tw)
    c1 = Counter(s[0] for t, s in tw)
    rd.gtl('TN13', 'second parts recur', 'recurring, second segments', [c2[s[3]] >= 2 for t, s in tw], [c1[s[0]] >= 2 for t, s in tw])
    items = {s_ for v, k, s_ in fcounted([t for t in DL if nonname(list(t))])}
    rd.gtl('TN14', 'second parts end in counted things', 'formula item, second-segment last signs', [s[3][-1] in items for t, s in tw], [s[0][-1] in items for t, s in tw])
    num = lambda x: any(g in R.NUMS for g in x)
    rd.gtl('TN15', 'two-name lines count', 'numeral, two-name lines', [num(t) for t, s in tw], [num(t) for t in one])
    x = sum(num(s[3]) and not num(s[0]) for t, s in tw)
    y = sum(num(s[0]) and not num(s[3]) for t, s in tw)
    p = R.binom_ge(x, x + y)
    rd.rec('TN16', 'the count is in the second part', 'second only %d, first only %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
    ob = {R.name_of(list(t))[0] for t in one}
    rd.thr('TN17', 'the second part stands alone', 'second segments also a one-name body', sum(s[3] in ob for t, s in tw), len(tw), 0.3)
    rd.thr('TN18', 'the first part stands alone', 'first segments also a one-name body', sum(s[0] in ob for t, s in tw), len(tw), 0.3)
    twB = [(t, split2(t)) for t in sorted({tuple(t) for t in B}) if split2(t)]
    tn3(twB, 'TN19', ' (B)')
    tn12(twB, 'TN20', ' (B)')
    rd.finish()


if __name__ == '__main__':
    main()
