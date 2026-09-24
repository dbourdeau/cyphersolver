"""Test of the eighteenth registered prediction set (PREDICTIONS.md, W1-W25).

Usage: python predict_test18.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test18.md.
"""
import os
import random
import sys
from collections import Counter, defaultdict

import icit_full
import predict_test13 as T
from numerals import NUMS
from predict_test4 import name_of
from predict_test7 import fisher_less
from predict_test14 import cat_of, classes, hyper_ge
from predict_test15 import strat_perm
from predict_test17 import headed, obj_perm

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
END = ('740', '520')
POST = ('90', '400', '151')
random.seed(38)


def say(s=''):
    OUT.append(s)
    print(s)


def n700(r):
    return any(x in NUMS and y == '700' for ln in r['seq'] for x, y in zip(ln, ln[1:]))


def lstrat(n):
    return 0 if n <= 3 else (1 if n <= 5 else 2)


def level(site, rc):
    if site == 'Mohenjo-daro':
        pr = rc[9].strip()
        return 'E' if pr.startswith(('Early', 'Interm')) else ('L' if pr.startswith('Late') else None)
    if site == 'Harappa':
        f10 = rc[10].strip()
        if rc[9].strip() == '3' and f10 in ('B', 'C'):
            return 'E' if f10 == 'B' else 'L'
        if f10 in ('Stratum IV', 'Stratum V', 'Stratum VI', 'Stratum VII'):
            return 'E'
        if f10 in ('Stratum I', 'Stratum II', 'Stratum III'):
            return 'L'
    return None


def fisher_ge_line(lab, a, na, c, nc):
    p = hyper_ge(a, na - a, c, nc - c)
    return p, '%s %d of %d (%.0f%%) against %d of %d (%.0f%%), p = %.4f' % (
        lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


def main(path):
    A, B = T.sample('A'), T.sample('B')
    AB = A + B
    cat = cat_of()
    head, attr = classes(A)
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    kind = lambda r: r['type'].split(':')[0]
    tabs = [r for r in intact if kind(r) == 'TAB']
    seals = [r for r in intact if kind(r) == 'SEAL']
    mot = lambda r: recs[r['sealid']][18].strip()
    known = lambda r: mot(r) and mot(r) not in ('-', 'None')
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    say('# Eighteenth registered predictions: twenty-five hypotheses on the two genres')
    say()
    say('- intact tablets %d (N700 %d), seals %d, sealings %d, pots %d.' % (
        len(tabs), sum(map(n700, tabs)), len(seals), sum(kind(r) == 'TAG' for r in intact),
        sum(kind(r) == 'POT' for r in intact)))
    say()

    # W1
    say('## W1 N700 tablets use a smaller inventory')
    toks = [Counter(g for g in r['flat'] if g not in NUMS and g != '700') for r in tabs]
    lab = [n700(r) for r in tabs]

    def st1(lb):
        a, b = Counter(), Counter()
        for c, l in zip(toks, lb):
            (a if l else b).update(c)
        return T.entropy(b) - T.entropy(a)
    o, p = obj_perm(tabs, lab, st1)
    say('- entropy of other signs, other tablets minus N700 tablets %+.2f bits; p = %.4f.' % (o, p))
    rec_('W1', o > 0 and p < 0.05)

    # W2
    say('## W2 one unit per text')
    withnum = [r for r in tabs if any(g in NUMS for g in r['flat'])]
    a = na = c = nc = 0
    for r in withnum:
        pairs = [(x, y) for ln in r['seq'] for x, y in zip(ln, ln[1:]) if x in NUMS and y not in NUMS]
        if n700(r):
            a += any(y != '700' for _, y in pairs)
            na += 1
        else:
            c += bool(pairs)
            nc += 1
    p = fisher_less(a, na - a, c, nc - c)
    say('- N700 tablets with another count pair %d of %d (%.0f%%); other numeral tablets with a count pair %d of %d '
        '(%.0f%%); p = %.4f.' % (a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p))
    rec_('W2', p < 0.05 and a / max(1, na) < c / max(1, nc))

    # W3
    say('## W3 N700 on moulded tablets')
    items = [(r['type'] == 'TAB:B', lstrat(len(r['flat'])), 1 if n700(r) else 0) for r in tabs
             if r['type'] in ('TAB:B', 'TAB:I')]
    o, p = strat_perm(items)
    say('- moulded N700 %d of %d, incised %d of %d; stratified difference %+.1f points; p = %.4f.' % (
        sum(x for l, _, x in items if l), sum(l for l, _, _ in items), sum(x for l, _, x in items if not l),
        sum(not l for l, _, _ in items), 100 * o, p))
    rec_('W3', o > 0 and p < 0.05)

    # W4
    say('## W4 N700 depends on the level at Harappa')
    lv = [(level('Harappa', recs[r['sealid']]), n700(r)) for r in tabs if r['site'].strip() == 'Harappa']
    lv = [(l, x) for l, x in lv if l]
    X, Y = [l for l, _ in lv], [x for _, x in lv]
    obs = T.mi(X, Y)
    ge = 0
    xx = X[:]
    for _ in range(N):
        random.shuffle(xx)
        ge += T.mi(xx, Y) >= obs
    p = (ge + 1) / (N + 1)
    say('- Harappa tablets with a level: %d; N700 earlier %d of %d, later %d of %d; MI %.4f; p = %.4f.' % (
        len(lv), sum(x for l, x in lv if l == 'E'), X.count('E'), sum(x for l, x in lv if l == 'L'), X.count('L'),
        obs, p))
    rec_('W4', p < 0.05)

    # W5
    say('## W5 700 on tablets is always counted')
    k = n = 0
    for r in tabs:
        for ln in r['seq']:
            for i, g in enumerate(ln):
                if g == '700':
                    n += 1
                    k += i > 0 and ln[i - 1] in NUMS
    say('- 700 on tablets preceded by a numeral: %d of %d (%.0f%%); threshold 80%%.' % (k, n, 100 * k / n))
    rec_('W5', k / n >= 0.8)

    # W6, W7, W9
    for key, title, labf, outf, flip in (
            ('W6', 'tablets with 400 carry numerals', lambda r: '400' in r['flat'],
             lambda r: any(g in NUMS for g in r['flat']), False),
            ('W7', 'N700 tablets lack endings', lambda r: not n700(r), lambda r: any(g in END for g in r['flat']), False),
            ('W9', 'N700 tablets carry a head sign', n700, lambda r: any(g in head for g in r['flat']), False)):
        say('## %s %s' % (key, title))
        items = [(labf(r), lstrat(len(r['flat'])), 1 if outf(r) else 0) for r in tabs]
        o, p = strat_perm(items)
        say('- labelled %d of %d; stratified difference %+.1f points; p = %.4f.' % (
            sum(l for l, _, _ in items), len(items), 100 * o, p))
        rec_(key, o > 0 and p < 0.05)

    # W8
    say('## W8 N700 is a Harappa genre')
    md = [n700(r) for r in tabs if r['site'].strip() == 'Mohenjo-daro']
    ha = [n700(r) for r in tabs if r['site'].strip() == 'Harappa']
    p = fisher_less(sum(md), len(md) - sum(md), sum(ha), len(ha) - sum(ha))
    say('- Mohenjo-daro tablets N700 %d of %d (%.0f%%), Harappa %d of %d (%.0f%%); p = %.4g.' % (
        sum(md), len(md), 100 * sum(md) / max(1, len(md)), sum(ha), len(ha), 100 * sum(ha) / len(ha), p))
    rec_('W8', p < 0.05 and sum(md) / max(1, len(md)) < sum(ha) / len(ha))

    # W10
    say('## W10 N700 texts come in batches')
    tc = Counter(tuple(r['flat']) for r in tabs)
    first = {}
    for r in tabs:
        first.setdefault(tuple(r['flat']), r)
    multi = [n700(first[t]) for t, c in tc.items() if c >= 2]
    single = [n700(first[t]) for t, c in tc.items() if c == 1]
    p, line = fisher_ge_line('distinct texts on 2+ tablets that are N700', sum(multi), len(multi), sum(single), len(single))
    say('- %s.' % line)
    rec_('W10', p < 0.05 and sum(multi) / max(1, len(multi)) > sum(single) / max(1, len(single)))

    # W11
    say('## W11 sealings are closer to seals than to tablets')
    tg = [g for r in intact if kind(r) == 'TAG' for g in r['flat']]
    sl = [g for r in seals for g in r['flat']]
    tb = [g for r in tabs for g in r['flat']]
    m = len(tg)
    pos = 0
    D = 1000
    for _ in range(D):
        bt = Counter(random.choice(tg) for _ in range(m))
        pos += T.jsd(bt, Counter(random.sample(tb, m))) - T.jsd(bt, Counter(random.sample(sl, m))) > 0
    say('- sealing tokens %d; draws in which the sealings are closer to seals than to tablets: %d of %d.' % (m, pos, D))
    rec_('W11', pos >= 0.95 * D)

    # W12
    say('## W12 sealings carry 400 after the ending')
    def post_counts(objs):
        c = Counter(y for r in objs for ln in r['seq'] for x, y in zip(ln, ln[1:]) if x in END and y in POST)
        return c['400'], sum(c.values())
    a, na = post_counts([r for r in intact if kind(r) == 'TAG'])
    c, nc = post_counts(seals)
    p, line = fisher_ge_line('400 among post-ending signs, sealings', a, na, c, nc)
    say('- %s.' % line)
    rec_('W12', p < 0.05 and a / max(1, na) > c / max(1, nc))

    # W13
    say('## W13 pot lines end in 740')
    def end740(objs):
        e = [name_of(ln)[1] for r in objs for ln in r['seq'] if name_of(ln)]
        return sum(x == '740' for x in e), len(e)
    a, na = end740([r for r in intact if kind(r) == 'POT'])
    c, nc = end740(tabs)
    p, line = fisher_ge_line('pot lines with an ending that end 740', a, na, c, nc)
    say('- %s.' % line)
    rec_('W13', p < 0.05 and a / max(1, na) > c / max(1, nc))

    # W14, W15
    say('## W14 long numerals on seals are the 33 of 33-520')
    k = n = 0
    for r in seals:
        for ln in r['seq']:
            for i, g in enumerate(ln):
                if g in NUMS and NUMS[g][1] == 'long':
                    n += 1
                    k += g == '33' and i + 1 < len(ln) and ln[i + 1] == '520'
    say('- seal long-stroke numerals: %d; 33 before 520: %d (%.0f%%); threshold 50%%.' % (n, k, 100 * k / n))
    rec_('W14', k / n > 0.5)
    say('## W15 tiered numerals are seal numerals')
    def tiered(objs):
        v = [NUMS[g][1] == 'tiered' for r in objs for g in r['flat'] if g in NUMS]
        return sum(v), len(v)
    a, na = tiered(seals)
    c, nc = tiered(tabs)
    p, line = fisher_ge_line('tiered numerals, seals', a, na, c, nc)
    say('- %s.' % line)
    rec_('W15', p < 0.05 and a / na > c / nc)

    # W16, W17
    say('## W16 a small set before 33-520')
    before = []
    for t in AB:
        for i, g in enumerate(t):
            if g == '520':
                if i >= 2 and t[i - 1] == '33':
                    before.append((True, t[i - 2]))
                elif i >= 1 and t[i - 1] != '33':
                    before.append((False, t[i - 1]))
    lb = [x for x, _ in before]
    sg = [s for _, s in before]

    def st16(l_):
        return T.entropy(Counter(s for s, x in zip(sg, l_) if not x)) - T.entropy(Counter(s for s, x in zip(sg, l_) if x))
    o, p = obj_perm(before, lb, st16)
    say('- before 33-520: %d tokens (%s); entropy plain-520 minus 33-520 %+.2f bits; p = %.4f.' % (
        sum(lb), ', '.join('%s x%d' % kv for kv in Counter(s for x, s in before if x).most_common(6)), o, p))
    rec_('W16', o > 0 and p < 0.05)
    say('## W17 an attribute before 33-520')
    a = na = c = nc = 0
    for t in AB:
        for i, g in enumerate(t):
            if g == '520' and i >= 2 and t[i - 1] == '33':
                a += t[i - 2] in attr
                na += 1
            elif g == '740' and i >= 1:
                c += t[i - 1] in attr
                nc += 1
    p, line = fisher_ge_line('sign before 33-520 in the attribute class', a, na, c, nc)
    say('- %s.' % line)
    rec_('W17', p < 0.05 and a / max(1, na) > c / nc)

    # W18
    say('## W18 33-520 seals are not unicorn seals')
    a = na = c = nc = 0
    for r in seals:
        if not known(r):
            continue
        nms = [name_of(ln) for ln in r['seq'] if name_of(ln)]
        if not nms:
            continue
        f = any(e == '520' and b[-1] == '33' for b, e in nms)
        nu = not mot(r).startswith('Bull1')
        if f:
            a += nu
            na += 1
        else:
            c += nu
            nc += 1
    p, line = fisher_ge_line('33-520 seals with another animal', a, na, c, nc)
    say('- %s.' % line)
    rec_('W18', p < 0.05 and a / max(1, na) > c / max(1, nc))

    # W19, W20
    say('## W19 33-520 lines lack the heading')
    items = []
    for t in AB:
        nm = name_of(t)
        if nm and len(t) >= 3:
            items.append((nm[1] == '520' and nm[0][-1] == '33', lstrat(len(t)), 0 if headed(t) else 1))
    o, p = strat_perm(items)
    say('- 33-520 lines %d; stratified difference in headless share %+.1f points; p = %.4f.' % (
        sum(l for l, _, _ in items), 100 * o, p))
    rec_('W19', o > 0 and p < 0.05)
    say('## W20 human-headed names carry the heading')
    items = []
    for t in AB:
        nm = name_of(t)
        if nm and len(t) >= 3:
            items.append((cat.get(nm[0][-1]) == 'A', lstrat(len(t)), 1 if headed(t) else 0))
    o, p = strat_perm(items)
    say('- human-headed lines %d; stratified difference %+.1f points; p = %.4f.' % (
        sum(l for l, _, _ in items), 100 * o, p))
    rec_('W20', o > 0 and p < 0.05)

    # W21-W24
    named = []
    for r in seals:
        if not known(r):
            continue
        for ln in r['seq']:
            nm = name_of(ln)
            if nm:
                named.append((r, ln, nm))
                break
    uni = lambda r: mot(r).startswith('Bull1')
    say('## W21 human-headed seals are unicorn seals')
    a = sum(uni(r) for r, _, nm in named if cat.get(nm[0][-1]) == 'A')
    na = sum(1 for _, _, nm in named if cat.get(nm[0][-1]) == 'A')
    c = sum(uni(r) for r, _, nm in named if cat.get(nm[0][-1]) != 'A')
    nc = len(named) - na
    p, line = fisher_ge_line('human-headed seals with a unicorn', a, na, c, nc)
    say('- %s.' % line)
    rec_('W21', p < 0.05 and a / max(1, na) > c / nc)
    say('## W22 unicorn and other seals use different heads')
    hs = [nm[0][-1] for _, _, nm in named]
    lb = [uni(r) for r, _, _ in named]

    def d22(l_):
        return T.jsd(Counter(h for h, x in zip(hs, l_) if x), Counter(h for h, x in zip(hs, l_) if not x))
    o, p = obj_perm(named, lb, d22)
    say('- seals: %d unicorn, %d other; JSD of heads %.3f; p = %.4f.' % (sum(lb), len(lb) - sum(lb), o, p))
    rec_('W22', p < 0.05)
    say('## W23 unicorn seals end in 740')
    items = [(uni(r), min(len(nm[0]), 4), 1 if nm[1] == '740' else 0) for r, _, nm in named]
    o, p = strat_perm(items)
    say('- stratified difference (unicorn minus other) in 740 share %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('W23', o > 0 and p < 0.05)
    say('## W24 names followed by 90 are on unicorn seals')
    f90 = lambda ln: len(ln) >= 3 and ln[-1] == '90' and ln[-2] in END
    a = sum(uni(r) for r, ln, _ in named if f90(ln))
    na = sum(1 for _, ln, _ in named if f90(ln))
    c = sum(uni(r) for r, ln, _ in named if not f90(ln))
    nc = len(named) - na
    p, line = fisher_ge_line('seals with a 90 after the ending that are unicorn', a, na, c, nc)
    say('- %s.' % line)
    rec_('W24', p < 0.05 and a / max(1, na) > c / nc)

    # W25
    say('## W25 the heading is commoner in later levels')
    ok = True
    for site in ('Mohenjo-daro', 'Harappa'):
        e = l_ = ne = nl = 0
        for r in intact:
            if r['site'].strip() != site:
                continue
            g = level(site, recs[r['sealid']])
            if not g:
                continue
            for ln in r['seq']:
                if len(ln) < 3:
                    continue
                if g == 'E':
                    e += headed(ln)
                    ne += 1
                else:
                    l_ += headed(ln)
                    nl += 1
        p, line = fisher_ge_line('%s later lines with the heading' % site, l_, nl, e, ne)
        ok = ok and p < 0.05 and l_ / max(1, nl) > e / max(1, ne)
        say('- %s.' % line)
    rec_('W25', ok)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test18.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
