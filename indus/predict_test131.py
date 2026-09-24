"""Hundred-and-thirty-first registered prediction set (PREDICTIONS.md, SZ1-SZ12): size beyond text length, and seal
shapes. Writes results/predict_test131.md."""
import random
from collections import defaultdict

import rtools as R
from predict_test43 import sp_perm
from predict_test108 import genre

random.seed(151)
HEAD = ('817', '820', '861')
NONE = ('', 'None', '-', 'Unknown')
CITY = ('Mohenjo-daro', 'Harappa')


def strat_size(items, n=R.N):
    """items: (label, stratum, size). Statistic: mean size of label True minus label False, within-stratum shuffles."""
    def stat(its):
        a = [s for l_, st, s in its if l_]
        b = [s for l_, st, s in its if not l_]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    obs = stat(items)
    by = defaultdict(list)
    for i, (l_, st, s) in enumerate(items):
        by[st].append(i)
    labs = [l_ for l_, st, s in items]
    ge = 0
    for _ in range(n):
        new = labs[:]
        for ii in by.values():
            v = [labs[i] for i in ii]
            random.shuffle(v)
            for i, x in zip(ii, v):
                new[i] = x
        ge += stat([(new[i], st, s) for i, (l_, st, s) in enumerate(items)]) >= obs
    return obs, (ge + 1) / (n + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-thirty-first registered predictions: size beyond text length, and seal shapes', 'predict_test131')
    size = lambda r: float(recs[r['sealid']][31]) if recs[r['sealid']][31].strip() not in ('0', '', '-') else None
    mot = lambda r: '' if recs[r['sealid']][18].strip() in NONE else recs[r['sealid']][18].split(':')[0].strip()
    lines = lambda r: [tuple(ln) for ln in r['seq'] if ln]
    L = lambda r: sum(len(t) for t in lines(r))
    st = lambda r: min(max(L(r), 2), 6)
    seals = [r for r in F if r['type'].startswith('SEAL') and size(r) and lines(r)]
    hd = lambda r: any(len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1') for t in lines(r))

    def rec_strat(key, title, items, want_pos=True):
        o, p = strat_size(items)
        if not want_pos:
            o2, p2 = strat_size([(not l_, s_, z) for l_, s_, z in items])
            rd.rec(key, title, 'mean size difference %+.2f mm at equal length; p = %.4f' % (-o2, p2), p2 < 0.05)
        else:
            rd.rec(key, title, 'mean size difference %+.2f mm at equal length; p = %.4f' % (o, p), o > 0 and p < 0.05)
    rec_strat('SZ1', 'headed seals are bigger at equal length', [(hd(r), st(r), size(r)) for r in seals])
    gs = lambda r, g: any(genre(t) == g for t in lines(r))
    rec_strat('SZ2', 'closer seals are smaller at equal length', [(gs(r, 'closer'), st(r), size(r)) for r in seals if gs(r, 'closer') or gs(r, 'name')], want_pos=False)
    lv = lambda r: R.level('Harappa', recs[r['sealid']])
    hs = [r for r in seals if r['site'].strip() == 'Harappa' and lv(r) in ('E', 'L')]
    rec_strat('SZ3', 'later seals are bigger at equal length', [(lv(r) == 'L', st(r), size(r)) for r in hs])
    o, p = sp_perm([size(r) for r in seals], [-L(r) / size(r) for r in seals])
    rd.rec('SZ4', 'small seals are packed tighter', 'Spearman(size, -density) %.3f; p = %.4f' % (o, p), o > 0 and p < 0.05)
    e = lambda r: [e_ for b, e_ in R.names_in(r) if b]
    s5 = [r for r in seals if e(r)]
    rec_strat('SZ5', '520 seals are smaller at equal length', [('520' in e(r), st(r), size(r)) for r in s5], want_pos=False)
    rd.rank('SZ6', 'small-site seals are smaller', 'city against small-site seals', [size(r) for r in seals if r['site'].strip() in CITY],
            [size(r) for r in seals if r['site'].strip() not in CITY])
    sq = [r for r in F if r['type'] == 'SEAL:S' and lines(r)]
    rc = [r for r in F if r['type'] == 'SEAL:R' and lines(r)]
    rd.rank('SZ7', 'rectangular seals say more', 'rectangular against square lines', [len(t) for r in rc for t in lines(r)], [len(t) for r in sq for t in lines(r)])
    rd.gtl('SZ8', 'rectangular seals have no picture', 'no motif, rectangular', [not mot(r) for r in rc], [not mot(r) for r in sq])
    rd.gtl('SZ9', 'rectangular seals count', 'count lines, rectangular', [genre(t) == 'count' for r in rc for t in lines(r)], [genre(t) == 'count' for r in sq for t in lines(r)])
    cs = lambda site: [r['type'] == 'SEAL:R' for r in F if r['type'] in ('SEAL:S', 'SEAL:R') and r['site'].strip() == site]
    rd.gtl('SZ10', 'rectangular seals are Harappan', 'rectangular, Harappa seals', cs('Harappa'), cs('Mohenjo-daro'))
    tb = lambda ty: [size(r) for r in F if r['type'] == ty and size(r)]
    rd.rank('SZ11', 'moulded tablets are small', 'incised against moulded', tb('TAB:I'), tb('TAB:B'))
    rd.rank('SZ12', 'copper tablets are big', 'copper against moulded', tb('TAB:C'), tb('TAB:B'))
    rd.finish()


if __name__ == '__main__':
    main()
