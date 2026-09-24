"""Eighty-fourth registered prediction set (PREDICTIONS.md, PE1-PE20): how the writing changed at Harappa. Writes
results/predict_test84.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test41 import dbl
from predict_test42 import dom, pairs
from predict_test44 import nonname
from predict_test78 import parse
from predict_test82 import suffix_lines
from signs import FISH

random.seed(104)
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Eighty-fourth registered predictions: how the writing changed at Harappa', 'predict_test84')
    full = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    lv = lambda r: R.level('Harappa', recs[r['sealid']])
    objs = [r for r in F if r['site'].strip() == 'Harappa' and lv(r) in ('E', 'L')]
    D = sorted({(lv(r), r['type'][:3], tuple(ln)) for r in objs for ln in r['seq'] if ln})
    E = [t for p_, ty, t in D if p_ == 'E']
    L = [t for p_, ty, t in D if p_ == 'L']
    rd.say('- Harappa objects with a period %d; distinct lines earlier %d, later %d.' % (len(objs), len(E), len(L)))
    rd.say()

    def two(key, title, lab, a, c):
        p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
        rd.rec(key, title, '%s, later %s' % (lab, R.fl(sum(a), len(a), sum(c), len(c), p)), p < 0.05)
    isn = lambda t: bool(R.name_of(list(t)) and R.name_of(list(t))[0])
    two('PE1', 'the share of names changes', 'name lines', [isn(t) for t in L], [isn(t) for t in E])
    fm = lambda X: [t for t in X if nonname(list(t))]
    two('PE2', 'numeral-first changes', 'numeral first, formulas', [t[0] in R.NUMS for t in fm(L)], [t[0] in R.NUMS for t in fm(E)])
    nb = lambda X: [R.name_of(list(t)) for t in X if isn(t)]
    rd.rank('PE3', 'names grow', 'later against earlier bodies', [len(b) for b, e in nb(L)], [len(b) for b, e in nb(E)])
    two('PE4', 'the 520 share changes', '520 names', [e == '520' for b, e in nb(L)], [e == '520' for b, e in nb(E)])
    two('PE5', 'fish names change', 'fish names', [any(g in FISH for g in b) for b, e in nb(L)], [any(g in FISH for g in b) for b, e in nb(E)])
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    two('PE6', 'headings change', 'heading unit, name lines', [hu(t) for t in L if isn(t)], [hu(t) for t in E if isn(t)])
    sf = lambda X: [f for b, e, f in suffix_lines(X)]
    rd.gtl('PE7', '90 grows', '90, later name lines', [f == '90' for f in sf(L)], [f == '90' for f in sf(E)])
    rd.gtl('PE8', '400 fades', '400, earlier name lines', [f == '400' for f in sf(E)], [f == '400' for f in sf(L)])
    nk = lambda X: [R.kind(g) == 'tiered' for t in X for g in t if g in R.NUMS]
    two('PE9', 'the tiered form changes', 'tiered numerals', nk(L), nk(E))
    se = {g for t in E for g in t}
    sl = {g for t in L for g in t}
    rd.thr('PE10', 'new signs appear', 'later sign types not earlier', len(sl - se), len(sl), 0.2)
    he = {b[-1] for b, e in nb(E)}
    hl = {b[-1] for b, e in nb(L)}
    rd.thr('PE11', 'the heads persist', 'head types in both periods', len(he & hl), len(he | hl), 0.5)

    def cls(X):
        hc = defaultdict(Counter)
        for b, e in nb(X):
            hc[b[-1]][e] += 1
        return {h: c.most_common(1)[0][0] for h, c in hc.items() if sum(c.values()) >= 3}
    ce, cl_ = cls(E), cls(L)
    bh = [h for h in ce if h in cl_]
    rd.thr('PE12', 'the classes persist', 'heads keeping their class', sum(ce[h] == cl_[h] for h in bh), len(bh), 0.9)
    de = dom(pairs(set(nb(E)), 3))
    dl = dom(pairs(set(nb(L)), 3))
    bp = [p_ for p_ in de if p_ in dl]
    rd.thr('PE13', 'the order persists', 'pairs with the same order', sum(de[p_] == dl[p_] for p_ in bp), len(bp), 0.85)
    ct = lambda t: len(t) >= 2 and t[-1] == '700' and all(g in R.NUMS for g in t[:-1])
    rd.gtl('PE14', 'count tokens fade', 'count tokens, earlier', [ct(t) for t in E], [ct(t) for t in L])
    two('PE15', 'doubling changes', 'lines with a double', [bool(dbl(list(t))) for t in L], [bool(dbl(list(t))) for t in E])
    rd.rank('PE16', 'lines grow', 'later against earlier lines', [len(t) for t in L], [len(t) for t in E])
    rd.gtl('PE17', 'seals grow', 'seals, later objects', [r['type'].startswith('SEAL') for r in objs if lv(r) == 'L'], [r['type'].startswith('SEAL') for r in objs if lv(r) == 'E'])
    tb = [r for r in objs if r['type'].startswith('TAB')]
    rd.gtl('PE18', 'moulding grows', 'TAB:B, later tablets', [r['type'] == 'TAB:B' for r in tb if lv(r) == 'L'], [r['type'] == 'TAB:B' for r in tb if lv(r) == 'E'])
    rd.gtl('PE19', 'pictures grow on tablets', 'picture, later tablets', [bool(full(r)) for r in tb if lv(r) == 'L'], [bool(full(r)) for r in tb if lv(r) == 'E'])
    hp = lambda X: [bool(parse(t)[0]) for t in fm(X) if parse(t)]
    rd.gtl('PE20', 'headers grow', 'header, later numeral formulas', hp(L), hp(E))
    rd.finish()


if __name__ == '__main__':
    main()
