"""Two-hundred-and-forty-fourth registered prediction set (PREDICTIONS.md, FF1-FF3): decipherment loop 69, are pairs with
a fish sign more picture-diverse than other lexical pairs? Writes results/predict_test244.md."""
from collections import defaultdict

import rtools as R
from predict_test17 import rank_perm
from predict_test200 import objects
from predict_test240 import GRAM
from signs import FISH


def split(objs):
    occ = defaultdict(list)
    for t, m in objs:
        for p in {t[i:i + 2] for i in range(len(t) - 1)}:
            occ[p].append(m)
    div = {p: len(set(ms)) / len(ms) for p, ms in occ.items() if len(ms) >= 3}
    lexp = {p: d for p, d in div.items() if not any(x in GRAM or x in R.NUMS for x in p)}
    fish = [d for p, d in lexp.items() if any(x in FISH for x in p)]
    other = [d for p, d in lexp.items() if not any(x in FISH for x in p)]
    return fish, other


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-forty-fourth registered predictions: decipherment loop 69, do fish names float free of the pictures?', 'predict_test244')
    res = []
    for key, types, lab in (('FF1', ('TAB:B',), 'moulded tablets'), ('FF2', ('TAB:C', 'TAB:I'), 'individually made tablets')):
        f, o = split(objects(F, recs, types))
        if not f or not o:
            rd.rec(key, 'fish pairs more picture-diverse (%s)' % lab, '%d fish pairs, %d other - too few' % (len(f), len(o)), False)
            res.append((False, None))
            continue
        d, p = rank_perm(f, o)
        ok = d > 0 and p < 0.05
        rd.rec(key, 'fish pairs more picture-diverse (%s)' % lab, '%d against %d pairs; means %.2f and %.2f; rank difference %+.1f; p = %.4f' % (len(f), len(o), sum(f) / len(f), sum(o) / len(o), d, p), ok)
        res.append((ok, d > 0))
    ok = res[0][0] and res[1][1] is True
    rd.rec('FF3', 'progress rule', '%s' % res, ok)
    rd.finish()


if __name__ == '__main__':
    main()
