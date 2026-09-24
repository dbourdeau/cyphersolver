"""Test of the twenty-eighth registered prediction set (PREDICTIONS.md, E1-E25).

Usage: python predict_test28.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test28.md. The fuller corpus is read with lines reversed.
"""
import os
import random
import statistics
import sys
from collections import Counter, defaultdict
from itertools import combinations

import icit_full
import predict_test13 as T
from numerals import NUMS
from predict_test4 import name_of
from predict_test7 import fisher_less
from predict_test14 import cat_of, classes, hyper_ge
from predict_test15 import strat_perm
from predict_test17 import headed
from predict_test18 import level, lstrat, n700
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
END = ('740', '520')
random.seed(48)


def say(s=''):
    OUT.append(s)
    print(s)


def fline(lab, a, na, c, nc, p):
    return '%s %d of %d (%.1f%%) against %d of %d (%.1f%%), p = %.4f' % (
        lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


def gt(lab, a, na, c, nc):
    p = hyper_ge(a, na - a, c, nc - c)
    return fline(lab, a, na, c, nc, p), p < 0.05 and a / max(1, na) > c / max(1, nc)


def lt(lab, a, na, c, nc):
    p = fisher_less(a, na - a, c, nc - c)
    return fline(lab, a, na, c, nc, p), p < 0.05 and a / max(1, na) < c / max(1, nc)


def mi_perm(xs, ys):
    obs = T.mi(xs, ys)
    ge = 0
    xx = list(xs)
    for _ in range(N):
        random.shuffle(xx)
        ge += T.mi(xx, ys) >= obs
    return obs, (ge + 1) / (N + 1)


def main(path):
    A, B = T.sample('A'), T.sample('B')
    AB = A + B
    rowsA = load()
    cat = cat_of()
    head, attr = classes(A)
    icit_full.LINES_REVERSED = True
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    names_in = lambda r: [name_of(ln) for ln in r['seq'] if name_of(ln)]
    w400 = lambda r: any(x in END and y == '400' for ln in r['seq'] for x, y in zip(ln, ln[1:]))
    rcp = [r for r in intact if r['type'] == 'TAB:I' and names_in(r) and w400(r)]
    seals = [r for r in intact if r['type'].startswith('SEAL')]
    tabs = [r for r in intact if r['type'].startswith('TAB')]
    kind = lambda g: NUMS[g][1]
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    def show(k, title, lo):
        say('## %s %s' % (k, title))
        say('- %s.' % lo[0])
        rec_(k, lo[1])

    say('# Twenty-eighth registered predictions: receipts, the fish split, units, habits')
    say()
    say('- receipts: %d.' % len(rcp))
    say()

    # E1
    say('## E1 receipt copies lie together')
    it = [(names_in(r)[0][0], r['depth']) for r in rcp if r['depth'] is not None]
    body = [b for b, _ in it]
    dep = [d for _, d in it]
    allp = list(combinations(range(len(it)), 2))
    same = [(i, j) for i, j in allp if body[i] == body[j]]
    diffs = {(i, j): abs(dep[i] - dep[j]) for i, j in allp}
    obs = statistics.median(diffs[p_] for p_ in same) if same else None
    if same:
        ge = 0
        for _ in range(N):
            smp = random.sample(allp, len(same))
            ge += statistics.median(diffs[p_] for p_ in smp) <= obs
        p = (ge + 1) / (N + 1)
        say('- receipts with a depth %d; same-name pairs %d; median difference %.2f, random pairs %.2f; p = %.4f.' % (
            len(it), len(same), obs, statistics.median(diffs.values()), p))
        rec_('E1', p < 0.05)
    else:
        say('- no same-name pairs with depths.')
        rec_('E1', False)

    # E2
    har = lambda r: r['site'].strip() == 'Harappa'
    a = [level('Harappa', recs[r['sealid']]) == 'E' for r in rcp if har(r) and level('Harappa', recs[r['sealid']])]
    c = [level('Harappa', recs[r['sealid']]) == 'E' for r in tabs if har(r) and n700(r) and level('Harappa', recs[r['sealid']])]
    show('E2', 'receipts are earlier than tokens', gt('earlier level, receipts', sum(a), len(a), sum(c), len(c)))

    # E3
    say('## E3 receipt names are the ends of seal names')
    sb = [b for r in seals for b, _ in names_in(r)]
    ends = set()
    for b in sb:
        for k in range(1, len(b)):
            ends.add(b[k:])
    rb = [names_in(r)[0][0] for r in rcp]
    obs = sum(b in ends for b in rb)
    ge = 0
    for _ in range(N):
        k2 = 0
        for b in rb:
            s_ = list(b)
            random.shuffle(s_)
            k2 += tuple(s_) in ends
        ge += k2 >= obs
    p = (ge + 1) / (N + 1)
    say('- receipt names %d; equal to the end of a longer seal name %d; p = %.4f.' % (len(rb), obs, p))
    rec_('E3', p < 0.05)

    a = [len(b) == 1 for b in rb]
    c = [len(b) == 1 for b in sb]
    show('E4', 'receipt names are single signs', gt('one-sign names, receipts', sum(a), len(a), sum(c), len(c)))

    say('## E5 the number depends on the name')
    vals = [(next(NUMS[g][0] for g in r['flat'] if g in NUMS), names_in(r)[0][0][-1]) for r in rcp if any(g in NUMS for g in r['flat'])]
    o, p = mi_perm([v for v, _ in vals], [h for _, h in vals])
    say('- receipts with a number %d; MI(value; last sign) %.3f bits; p = %.4f.' % (len(vals), o, p))
    rec_('E5', p < 0.05)

    say('## E21 receipt numbers are 1 or 2')
    k = sum(v <= 2 for v, _ in vals)
    say('- values %s; 1 or 2: %d of %d (%.0f%%); threshold 70%%.' % (dict(Counter(v for v, _ in vals)), k, len(vals), 100 * k / max(1, len(vals))))
    rec_('E21', vals and k / len(vals) >= 0.7)

    a = [cat.get(b[-1]) == 'A' for b in rb]
    c = [cat.get(b[-1]) == 'A' for b in sb]
    show('E22', 'receipt names are human-headed', gt('human head, receipts', sum(a), len(a), sum(c), len(c)))
    say('## E23 receipt names start differently')
    o, p = mi_perm(['r'] * len(rb) + ['s'] * len(sb), [b[0] for b in rb] + [b[0] for b in sb])
    say('- MI %.4f bits; p = %.4f.' % (o, p))
    rec_('E23', p < 0.05)

    has3274 = lambda r: any(x == '32' and y == '740' for ln in r['seq'] for x, y in zip(ln, ln[1:]))
    a = [has3274(r) for r in intact if r['type'] == 'TAB:B']
    c = [has3274(r) for r in intact if r['type'] != 'TAB:B']
    show('E6', "'32 740' is a moulded formula", gt("'32 740', moulded tablets", sum(a), len(a), sum(c), len(c)))
    say('## E7 the two formulas differ in level')
    it = [(level('Harappa', recs[r['sealid']]), 'f' if has3274(r) else 't') for r in tabs if har(r) and (has3274(r) or n700(r))]
    it = [(l, f) for l, f in it if l]
    o, p = mi_perm([l for l, _ in it], [f for _, f in it])
    say('- %s; MI %.4f; p = %.4f.' % (dict(Counter(it)), o, p))
    rec_('E7', p < 0.05)
    a = [len(r['flat']) <= 3 for r in tabs if has3274(r)]
    c = [len(r['flat']) <= 3 for r in tabs if not has3274(r)]
    show('E8', "'32 740' texts are short", gt("3 signs or fewer, '32 740' tablets", sum(a), len(a), sum(c), len(c)))
    say('## E20 token values change with depth')
    val = {'32': 2, '33': 3, '34': 4}
    it = [(next(val[x] for ln in r['seq'] for x, y in zip(ln, ln[1:]) if y == '700' and x in val), r['depth'])
          for r in tabs if har(r) and n700(r) and r['depth'] is not None and
          any(y == '700' and x in val for ln in r['seq'] for x, y in zip(ln, ln[1:]))]
    xs, ys = [a for a, _ in it], [b for _, b in it]
    rho = T.spearman(xs, ys)
    ge = 0
    yy = ys[:]
    for _ in range(N):
        random.shuffle(yy)
        ge += abs(T.spearman(xs, yy)) >= abs(rho)
    p = (ge + 1) / (N + 1)
    say('- tokens with a depth %d; Spearman %.3f; two-sided p = %.4f.' % (len(it), rho, p))
    rec_('E20', p < 0.05)

    # fish
    nm = T.names(AB)
    say('## E9 the long-pair fish take 520')
    items = []
    for b, e in nm:
        if b[-1] in FISH and len(b) >= 2:
            inner = b[:-1]
            if '32' in inner:
                items.append((True, min(len(b), 4), 1 if e == '520' else 0))
            elif not any(g in NUMS for g in inner):
                items.append((False, min(len(b), 4), 1 if e == '520' else 0))
    o, p = strat_perm(items)
    say('- with 32 %d; stratified difference in 520 share %+.1f points; p = %.4f.' % (sum(l for l, _, _ in items), 100 * o, p))
    rec_('E9', o > 0 and p < 0.05)
    say('## E10 the plain fish are persons')
    v = [e == '740' for b, e in nm if b[-1] == '220' and not any(g in NUMS for g in b)]
    say('- plain-fish names without a numeral %d; 740 %d (%.0f%%); threshold 60%%.' % (len(v), sum(v), 100 * sum(v) / max(1, len(v))))
    rec_('E10', v and sum(v) / len(v) >= 0.6)
    say('## E11 the stroke pair belongs to the fish')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        a = [y in FISH for t in L for x, y in zip(t, t[1:]) if x == '2']
        c = [y in FISH for t in L for x, y in zip(t, t[1:]) if x == '3']
        line, good = gt('fish after the stroke pair', sum(a), len(a), sum(c), len(c))
        ok = ok and good
        say('- %s: %s.' % (lab, line))
    rec_('E11', ok)
    say('## E12 the stroke-pair fish carry the heading')
    items = [(any(x == '2' and y in FISH for x, y in zip(t, t[1:])), lstrat(len(t)), 1 if headed(t) else 0)
             for t in AB if name_of(t) and len(t) >= 3]
    o, p = strat_perm(items)
    say('- stratified difference %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('E12', o > 0 and p < 0.05)

    # units
    say('## E14 on seals the unit decides the long count')
    prs = [(NUMS[x][0], y) for r in seals for ln in r['seq'] for x, y in zip(ln, ln[1:]) if x in NUMS and kind(x) == 'long' and y not in NUMS]
    o, p = mi_perm([a for a, _ in prs], [b for _, b in prs])
    say('- pairs %d; MI %.3f; p = %.4f.' % (len(prs), o, p))
    rec_('E14', p < 0.05)
    say('## E15 the unit decides the short count')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        prs = [(NUMS[x][0], y) for t in L for x, y in zip(t, t[1:]) if x in NUMS and kind(x) == 'short' and y not in NUMS]
        o, p = mi_perm([a for a, _ in prs], [b for _, b in prs])
        ok = ok and p < 0.05
        say('- %s: pairs %d; MI %.3f; p = %.4f.' % (lab, len(prs), o, p))
    rec_('E15', ok)
    say('## E16 the unit decides the tiered count')
    prs = [(NUMS[x][0], y) for t in AB for x, y in zip(t, t[1:]) if x in NUMS and kind(x) == 'tiered' and y not in NUMS]
    o, p = mi_perm([a for a, _ in prs], [b for _, b in prs])
    say('- pairs %d; MI %.3f; p = %.4f.' % (len(prs), o, p))
    rec_('E16', p < 0.05)
    lines = [ln for r in seals for ln in r['seq'] if name_of(ln)]
    a = [name_of(ln)[1] == '520' for ln in lines for g in ln if g in NUMS and kind(g) == 'long']
    c = [name_of(ln)[1] == '520' for ln in lines]
    show('E13', 'seal long numerals stand in 520 lines', gt('520 lines, long-numeral tokens', sum(a), len(a), sum(c), len(c)))

    # direction, labels
    lr = lambda r: r['direction'] == 'L/R'
    pots = [r for r in rowsA if r['type'].startswith('POT')]
    a = [r['site'] not in ('Mohenjo-daro', 'Harappa') for r in pots if lr(r)]
    c = [r['site'] not in ('Mohenjo-daro', 'Harappa') for r in pots if not lr(r)]
    show('E17', 'left-to-right pots are local', gt('outside the two cities, left-to-right pots', sum(a), len(a), sum(c), len(c)))
    say('## E18 left-to-right lines carry numbers')
    items = [(lr(r), lstrat(len(t)), 1 if any(g in NUMS for g in t) else 0) for r in rowsA for t in r['seq'] if len(t) >= 2 and '?' not in t]
    o, p = strat_perm(items)
    say('- stratified difference %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('E18', o > 0 and p < 0.05)
    say('## E19 copper tablets carry no numbers')
    items = [(r['type'].startswith('SEAL'), lstrat(len(t)), 1 if any(g in NUMS for g in t) else 0) for r in rowsA
             for t in r['seq'] if len(t) >= 2 and '?' not in t and (r['type'] == 'TAB:C' or r['type'].startswith('SEAL'))]
    o, p = strat_perm(items)
    say('- stratified difference (seals minus copper tablets) %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('E19', o > 0 and p < 0.05)

    # habits
    sn = [(r['site'].strip(), ln) for r in seals for ln in r['seq'] if name_of(ln)]
    f400 = lambda ln: len(ln) >= 2 and ln[-1] == '400' and ln[-2] in END
    f90 = lambda ln: len(ln) >= 2 and ln[-1] == '90' and ln[-2] in END
    a = [s_ == 'Harappa' for s_, ln in sn if f400(ln)]
    c = [s_ == 'Harappa' for s_, ln in sn if not f400(ln)]
    show('E24', 'the seal 400 is a Harappa habit', gt('Harappa, seal names with 400', sum(a), len(a), sum(c), len(c)))
    a = [f90(ln) for s_, ln in sn if s_ == 'Harappa']
    c = [f90(ln) for s_, ln in sn if s_ == 'Mohenjo-daro']
    show('E25', 'the seal 90 is a Mohenjo-daro habit', lt('90 after the name, Harappa seals', sum(a), len(a), sum(c), len(c)))

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test28.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
