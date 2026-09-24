"""Hundred-and-forty-fourth registered prediction set (PREDICTIONS.md, TM1-TM8): does the ending slot change over time?
Writes results/predict_test144.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test103 import CL
from predict_test108 import genre
from predict_test18 import level
from predict_test43 import sp_perm

random.seed(164)
STACK = ('151', '161', '527', '565', '621', '679')
N = 10000


def fine(p):
    p = p.replace('Period', '').strip()
    if p.startswith('3A'):
        return 1
    if p.startswith('3B') and p != '3B/C':
        return 2
    if p.startswith('3C'):
        return 3
    if p.startswith('4'):
        return 4
    if p.startswith('5'):
        return 5
    return None


def strat_diff(items):
    """items: (site, level 'E'/'L', 0/1). Late minus early share, labels permuted within site; two-sided p."""
    def d(it):
        e = [v for s, l, v in it if l == 'E']
        l_ = [v for s, l, v in it if l == 'L']
        return sum(l_) / max(1, len(l_)) - sum(e) / max(1, len(e))
    obs = d(items)
    by = defaultdict(list)
    for i, (s, l, v) in enumerate(items):
        by[s].append(i)
    ge = 0
    for _ in range(N):
        labs = [l for s, l, v in items]
        for s, ix in by.items():
            v = [labs[i] for i in ix]
            random.shuffle(v)
            for i, x in zip(ix, v):
                labs[i] = x
        ge += abs(d([(s, l, v) for (s, _, v), l in zip(items, labs)])) >= abs(obs)
    return obs, (ge + 1) / (N + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-forty-fourth registered predictions: does the ending slot change over time?', 'predict_test144')
    rows = set()
    for r in F:
        s = recs[r['sealid']][3]
        lv = level(s, recs[r['sealid']])
        if r['type'] != 'TAB:C' and lv and r['seq'] and r['seq'][0]:
            rows.add((tuple(r['seq'][0]), s, lv))
    rows = sorted(rows)
    rd.say('- distinct (text, site, level): %d (%s).' % (len(rows), dict(Counter((s, l) for t, s, l in rows))))
    rd.say()
    nm = [(t, s, l, R.name_of(list(t))) for t, s, l in rows if R.name_of(list(t))]

    def test(key, title, items, lab):
        o, p = strat_diff(items)
        e = [v for s, l, v in items if l == 'E']
        l_ = [v for s, l, v in items if l == 'L']
        rd.rec(key, title, '%s: early %d of %d (%.1f%%), late %d of %d (%.1f%%); difference %+.3f; p = %.4f' % (
            lab, sum(e), len(e), 100 * sum(e) / max(1, len(e)), sum(l_), len(l_), 100 * sum(l_) / max(1, len(l_)), o, p), p < 0.05)
    test('TM1', 'the 520 share changes', [(s, l, e == '520') for t, s, l, (b, e) in nm], '520 names')
    test('TM2', 'the closer share changes', [(s, l, genre(t) == 'closer') for t, s, l in rows], 'closer texts')
    test('TM3', 'the 400 / 90 share changes', [(s, l, t[-1] in ('400', '90') and len(t) >= 2 and t[-2] in R.END) for t, s, l, x in nm], 'names with 400/90 after the ending')
    # 740 texts: 740 final, or followed only by markers (name_of drops the stacking closers other than 151)
    mk = set(R.END) | set(CL) | {'400', '90'}
    n7 = [(t, s, l) for t, s, l in rows if '740' in t and t.index('740') > 0 and all(g in mk for g in t[t.index('740') + 1:])]
    test('TM4', 'the stacking share changes', [(s, l, '740' in t and t.index('740') + 1 < len(t) and t[t.index('740') + 1] in STACK) for t, s, l in n7], '740 names with a stacking closer')
    he = defaultdict(lambda: {'E': Counter(), 'L': Counter()})
    for t, s, l, (b, e) in nm:
        if b:
            he[b[-1]][l][e] += 1
    both = [h for h in he if sum(he[h]['E'].values()) >= 3 and sum(he[h]['L'].values()) >= 3]
    keep = sum(he[h]['E'].most_common(1)[0][0] == he[h]['L'].most_common(1)[0][0] for h in both)
    rd.thr('TM5', 'heads keep their ending', 'heads with 3+ names in both levels', keep, len(both), 0.9)
    early = {b[-1] for t, s, l, (b, e) in nm if b and l == 'E'}
    new = [e == '740' for t, s, l, (b, e) in nm if b and l == 'L' and b[-1] not in early]
    old = [e == '740' for t, s, l, (b, e) in nm if b and l == 'L' and b[-1] in early]
    p = min(1, 2 * min(R.hyper_ge(sum(new), len(new) - sum(new), sum(old), len(old) - sum(old)),
                       R.fisher_less(sum(new), len(new) - sum(new), sum(old), len(old) - sum(old))))
    rd.rec('TM6', 'new heads take 740 as often', 'late names, new heads %s' % R.fl(sum(new), len(new), sum(old), len(old), p), p >= 0.05)
    hp = set()
    for r in F:
        if recs[r['sealid']][3] == 'Harappa' and r['type'] != 'TAB:C' and r['seq'] and r['seq'][0]:
            f = fine(recs[r['sealid']][8])
            nmx = R.name_of(list(r['seq'][0]))
            if f and nmx and nmx[1] in R.END:
                hp.add((tuple(r['seq'][0]), f, nmx[1]))
    hp = sorted(hp)
    o, p = sp_perm([f for t, f, e in hp], [e == '520' for t, f, e in hp], n=N)
    per = defaultdict(list)
    for t, f, e in hp:
        per[f].append(e == '520')
    rd.rec('TM7', 'a trend at Harappa', '%d names; 520 share by period %s; Spearman %.3f; p = %.4f' % (
        len(hp), ', '.join('%d: %d/%d' % (f, sum(v), len(v)) for f, v in sorted(per.items())), o, p), p < 0.05)
    test('TM8', 'the count share changes', [(s, l, genre(t) == 'count') for t, s, l in rows], 'count texts')
    rd.finish()


if __name__ == '__main__':
    main()
