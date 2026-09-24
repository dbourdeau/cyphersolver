"""Hundred-and-fifty-sixth registered prediction set (PREDICTIONS.md, BO1-BO4): numerals in names as birth-order or
clan numbers. Writes results/predict_test156.md."""
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test108 import genre
from predict_test112 import runs


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-fifty-sixth registered predictions: numerals in names as birth-order or clan numbers', 'predict_test156')
    DL = sorted({tuple(t) for t in A + B})
    ns = sorted({(b, e) for b, e in T.names(DL) if b})
    val = lambda r: sum(R.NUMS[g][0] for g in r)
    nv = [val(r) for b, e in ns for i, j, r in runs(b)]
    cv = [val(r) for t in DL if genre(t) == 'count' for i, j, r in runs(t)]
    rd.gtl('BO1', 'name numerals are small', 'value 4 or less, name runs (%s)' % dict(Counter(nv).most_common(6)), [v <= 4 for v in nv], [v <= 4 for v in cv])
    op = [(b, e, i, j, r) for b, e in ns for i, j, r in runs(b) if i == 0 and j < len(b)]
    rd.thr('BO2', 'name-opening numbers are small', 'name-opening runs worth 4 or less (%s)' % dict(Counter(val(r) for *_, r in op).most_common(6)),
           sum(val(r) <= 4 for *_, r in op), len(op), 0.8)
    cv_ = []
    for r in F:
        s = recs[r['sealid']][3]
        if s in ('Mohenjo-daro', 'Harappa') and r['type'] != 'TAB:C':
            for b, e in R.names_in(r):
                for i, j, rr in runs(b):
                    if i == 0 and j < len(b):
                        cv_.append((val(rr), s))
    rd.mi('BO3', 'opening numbers depend on the city', 'name-opening runs in F (%s)' % dict(Counter(s for v, s in cv_)), [v for v, s in cv_], [s for v, s in cv_])
    rest = defaultdict(set)
    for b, e, i, j, r in op:
        rest[(b[j:], e)].add(val(r))
    mp = {k: v for k, v in rest.items() if len(v) >= 2}
    npairs = sum(len(v) * (len(v) - 1) // 2 for v in mp.values())
    rd.rec('BO4', 'numbered siblings', 'name pairs differing only in the opening value: %d (%s)' % (npairs, '; '.join(
        '%s %s: %s' % (' '.join(k[0]), k[1], sorted(v)) for k, v in list(mp.items())[:10])), npairs >= 5)
    rd.finish()


if __name__ == '__main__':
    main()
