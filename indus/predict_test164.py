"""Hundred-and-sixty-fourth registered prediction set (PREDICTIONS.md, TS1-TS10): standardisation over time and the
seal types. Writes results/predict_test164.md."""
from collections import Counter

import rtools as R
from predict_test144 import strat_diff
from predict_test157 import profile
from predict_test161 import CITIES, shared_openers
from predict_test18 import level


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-sixty-fourth registered predictions: standardisation over time and the seal types', 'predict_test164')
    SO = shared_openers(F, recs)
    seals = [r for r in F if r['type'].startswith('SEAL') and recs[r['sealid']][3] in CITIES]
    lv = lambda r: level(recs[r['sealid']][3], recs[r['sealid']])
    n3 = lambda r: [(b, e) for b, e in R.names_in(r) if b and len(b) >= 3]
    it = [(recs[r['sealid']][3], lv(r), b) for r in seals if lv(r) for b, e in n3(r)]
    for key, c in (('TS1', 'Mohenjo-daro'), ('TS2', 'Harappa')):
        rd.gtl(key, 'the rise at %s' % c, 'shared opener, late names', [b[0] in SO for s, l_, b in it if s == c and l_ == 'L'],
               [b[0] in SO for s, l_, b in it if s == c and l_ == 'E'])
    d1, p1 = strat_diff([(s, l_, b[0] in R.NUMS) for s, l_, b in it])
    d2, p2 = strat_diff([(s, l_, b[0] in SO and b[0] not in R.NUMS) for s, l_, b in it])
    rd.rec('TS3', 'numeral openers carry the rise', 'numeral openers late minus early %+.3f (one-sided p %.4f); non-numeral shared openers %+.3f (two-sided p %.4f)' % (
        d1, p1 / 2, d2, p2), d1 > 0 and p1 / 2 < 0.05 and p2 >= 0.05)
    rec_ = {'E': Counter(), 'L': Counter()}
    for r in seals:
        if lv(r):
            for nm in {x for x in R.names_in(r) if x[0]}:
                rec_[lv(r)][nm] += 1
    rd.gtl('TS4', 'late names recur more', 'names on 2+ seals, late', [v >= 2 for v in rec_['L'].values()], [v >= 2 for v in rec_['E'].values()])
    pl = {}
    for L in ('E', 'L'):
        cat = {c: Counter() for c in CITIES}
        for r in seals:
            if lv(r) == L:
                for nm in {x for x in R.names_in(r) if x[0]}:
                    cat[recs[r['sealid']][3]][nm] += 1
        pl[L] = profile(cat)
    rd.rec('TS5', 'late names are less open', 'early %s ratio %.2f; late %s ratio %.2f' % (pl['E']['n'], pl['E']['ratio'], pl['L']['n'], pl['L']['ratio']), pl['L']['ratio'] < pl['E']['ratio'])
    ty = [(recs[r['sealid']][3], 'L' if r['type'] == 'SEAL:R' else 'E', lv(r) == 'L') for r in seals if lv(r) and r['type'] in ('SEAL:R', 'SEAL:S')]
    d, p = strat_diff(ty)
    rd.rec('TS6', 'rectangular seals are later', 'late share, rectangular minus square %+.3f; two-sided p %.4f (rectangular %d, square %d)' % (
        d, p, sum(1 for x in ty if x[1] == 'L'), sum(1 for x in ty if x[1] == 'E')), d > 0 and p / 2 < 0.05)
    rd.gtl('TS7', 'rectangular seals use the frequent openers', 'shared opener, rectangular-seal names', [b[0] in SO for r in seals if r['type'] == 'SEAL:R' for b, e in n3(r)],
           [b[0] in SO for r in seals if r['type'] == 'SEAL:S' for b, e in n3(r)])
    sq = [(recs[r['sealid']][3], lv(r), b[0] in SO) for r in seals if r['type'] == 'SEAL:S' and lv(r) for b, e in n3(r)]
    d, p = strat_diff(sq)
    rd.rec('TS8', 'the rise on square seals alone', 'late minus early %+.3f; one-sided p %.4f (%d names)' % (d, p / 2, len(sq)), d > 0 and p / 2 < 0.05)
    tags = [len(r['flat']) for r in F if r['type'].startswith('TAG')]
    sl = [len(r['flat']) for r in F if r['type'].startswith('SEAL')]
    rd.rank('TS9', 'sealings carry shorter texts', 'seal against tag text length (positive = seals longer)', sl, tags)
    res = []
    ok = True
    for s in ('Lothal', 'Kalibangan'):
        x = [b[0] in SO for r in F if r['type'].startswith('TAG') and recs[r['sealid']][3] == s for b, e in n3(r)]
        res.append('%s %d of %d' % (s, sum(x), len(x)))
        ok = ok and len(x) > 0 and sum(x) / len(x) >= 0.7
    rd.rec('TS10', 'sealings at each site use the frequent openers', res, ok)
    rd.finish()


if __name__ == '__main__':
    main()
