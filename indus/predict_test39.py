"""Thirty-ninth registered prediction set (PREDICTIONS.md, HT1-HT10): Harappa over time. Writes
results/predict_test39.md."""
import random
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test36 import G, make_tests

random.seed(59)


def main():
    A, B, rowsA, recs, F = R.load_all()
    cat = R.cat_of()
    rd = R.Round('Thirty-ninth registered predictions: Harappa over time', 'predict_test39')
    lv = lambda r: R.level('Harappa', recs[r['sealid']])
    har = [r for r in F if r['site'].strip() == 'Harappa' and lv(r)]
    E, L_ = G([r for r in har if lv(r) == 'E']), G([r for r in har if lv(r) == 'L'])
    rd.say('- Harappa objects with a level: earlier %d, later %d.' % (len(E.objs), len(L_.objs)))
    rd.say()
    mot = lambda r: recs[r['sealid']][18].strip()
    tests = make_tests(cat, {}, mot)

    def both(key, title, tk):
        out, ok = [], True
        for lab, g in (('earlier', E), ('later', L_)):
            line, good, n = tests[tk](g)
            out.append('%s: %s%s' % (lab, line, '; under 20 cases, not testable' if n < 20 else ''))
            ok = ok and good and n >= 20
        rd.rec(key, title, out, ok)
    both('HT1', 'the last sign decides the ending', '1')
    both('HT2', 'long strokes count containers', '11')
    both('HT3', 'the sign decides the number', '12')
    both('HT4', 'the tiered form is for larger numbers', '10')
    w400 = lambda r: any(x in R.END and y == '400' for ln in r['seq'] for x, y in zip(ln, ln[1:]))
    rc = lambda r: r['type'] == 'TAB:I' and R.names_in(r) and w400(r)
    tabs = [r for r in har if r['type'].startswith('TAB')]
    rd.gtl('HT5', 'receipts are earlier', 'receipts among earlier tablets',
           [bool(rc(r)) for r in tabs if lv(r) == 'E'], [bool(rc(r)) for r in tabs if lv(r) == 'L'])
    val = {'32': 2, '33': 3, '34': 4}
    tv = [(lv(r), next(val[x] for ln in r['seq'] for x, y in zip(ln, ln[1:]) if y == '700' and x in val)) for r in tabs
          if any(y == '700' and x in val for ln in r['seq'] for x, y in zip(ln, ln[1:]))]
    lab = [l_ == 'E' for l_, _ in tv]
    vv = [v for _, v in tv]

    def st(lb):
        a = [v for v, x in zip(vv, lb) if x]
        b = [v for v, x in zip(vv, lb) if not x]
        return sum(a) / len(a) - sum(b) / len(b)
    obs = st(lab)
    ge = 0
    sh = lab[:]
    for _ in range(R.N):
        random.shuffle(sh)
        ge += st(sh) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('HT6', 'earlier tokens count more', 'tokens %d; mean value earlier minus later %+.2f; p = %.4f' % (len(tv), obs, p),
           obs > 0 and p < 0.05)
    e5 = [n[1] == '520' for r in E.objs for n in R.names_in(r)]
    l5 = [n[1] == '520' for r in L_.objs for n in R.names_in(r)]
    p = min(1, 2 * min(R.hyper_ge(sum(e5), len(e5) - sum(e5), sum(l5), len(l5) - sum(l5)),
                       R.fisher_less(sum(e5), len(e5) - sum(e5), sum(l5), len(l5) - sum(l5))))
    rd.rec('HT7', 'the 520 share changes', '520, earlier %s' % R.fl(sum(e5), len(e5), sum(l5), len(l5), p), p < 0.05)
    both('HT8', 'the stroke pair goes with the fish', '9')
    dirs = {r['cisi']: r['direction'] for r in rowsA if r.get('cisi')}
    dl = [(lv(r), dirs[r['cisi']] == 'L/R') for r in har if r.get('cisi') in dirs]
    e = [d for l_, d in dl if l_ == 'E']
    l2 = [d for l_, d in dl if l_ == 'L']
    p = min(1, 2 * min(R.hyper_ge(sum(e), len(e) - sum(e), sum(l2), len(l2) - sum(l2)),
                       R.fisher_less(sum(e), len(e) - sum(e), sum(l2), len(l2) - sum(l2))))
    rd.rec('HT9', 'direction changes over time', 'left-to-right, earlier %s' % R.fl(sum(e), len(e), sum(l2), len(l2), p), p < 0.05)
    hs = [(lv(r), n[0][-1]) for r in har for n in R.names_in(r)]
    rd.mi('HT10', 'the heads change over time', 'Harappa names', [a for a, _ in hs], [b for _, b in hs])
    rd.finish()


if __name__ == '__main__':
    main()
