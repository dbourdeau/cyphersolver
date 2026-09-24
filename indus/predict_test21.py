"""Test of the twenty-first registered prediction set (PREDICTIONS.md, R1-R25): the lines that fit no template.

Usage: python predict_test21.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test21.md.
"""
import os
import random
import sys
from collections import Counter

import icit_full
import predict_test13 as T
from numerals import NUMS
from predict_test4 import name_of
from predict_test14 import cat_of, classes, hyper_ge
from predict_test15 import binom_ge, strat_perm
from predict_test17 import headed, rank_perm
from predict_test18 import level, lstrat, n700
from signs import FISH

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
END = ('740', '520')
POST = ('90', '400', '151')
GRAMMAR = {'740', '520', '90', '400', '151', '817', '820', '861', '2'}
FORMULA = {'705', '706', '33'}
random.seed(41)


def say(s=''):
    OUT.append(s)
    print(s)


def bare(t):
    return (len(t) >= 2 and not name_of(t) and not any(x in NUMS and y == '700' for x, y in zip(t, t[1:]))
            and not all(g in NUMS for g in t))


def fline(lab, a, na, c, nc, p):
    return '%s %d of %d (%.1f%%) against %d of %d (%.1f%%), p = %.4f' % (
        lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


def paired_last(lines, pred):
    """Sign test: last sign satisfies pred vs a random other sign of the line."""
    b10 = b01 = k_last = 0
    for t in lines:
        j = random.randrange(len(t) - 1)
        x, y = pred(t[-1]), pred(t[j])
        k_last += x
        b10 += x and not y
        b01 += y and not x
    return k_last, b10, b01, binom_ge(b10, b10 + b01)


def shuffle_count(lines, target):
    obs = sum(tuple(t) in target for t in lines)
    ge = 0
    for _ in range(N):
        k = 0
        for t in lines:
            s = list(t)
            random.shuffle(s)
            k += tuple(s) in target
        ge += k >= obs
    return obs, (ge + 1) / (N + 1)


def main(path):
    A, B = T.sample('A'), T.sample('B')
    AB = A + B
    cat = cat_of()
    head, attr = classes(A)
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    kind = lambda r: r['type'].split(':')[0]
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    say('# Twenty-first registered predictions: the lines that fit no template')
    say()
    say('- bare lines: A %d of %d, B %d of %d.' % (sum(map(bare, A)), len(A), sum(map(bare, B)), len(B)))
    say()

    def both(key, title, fn):
        say('## %s %s' % (key, title))
        ok = True
        for lab, L in (('A', A), ('B', B)):
            line, good = fn(L)
            ok = ok and good
            say('- %s: %s.' % (lab, line))
        rec_(key, ok)

    def r1(L):
        k, a, b, p = paired_last([t for t in L if bare(t)], lambda g: g in head)
        return 'last sign head-class %d; discordant %d / %d; p = %.4f' % (k, a, b, p), a > b and p < 0.05
    both('R1', 'the last sign of a bare line is a head', r1)

    def r2(L):
        ends = {b[-1] for b, _ in T.names(L)}
        k, a, b, p = paired_last([t for t in L if bare(t)], lambda g: g in ends)
        return 'last sign a name-final sign %d; discordant %d / %d; p = %.4f' % (k, a, b, p), a > b and p < 0.05
    both('R2', 'the last sign of a bare line ends names elsewhere', r2)

    def r3(L):
        bodies = {b for b, _ in T.names(L)}
        bl = [t for t in L if bare(t)]
        o, p = shuffle_count(bl, bodies)
        return 'bare lines equal to a name body %d of %d; p = %.4f' % (o, len(bl), p), p < 0.05
    both('R3', 'bare lines are attested name bodies', r3)

    def r4(L):
        bp = {(x, y) for b, _ in T.names(L) for x, y in zip(b, b[1:])}
        bl = [t for t in L if bare(t)]
        share = lambda ls: sum((x, y) in bp for t in ls for x, y in zip(t, t[1:])) / sum(len(t) - 1 for t in ls)
        obs = share(bl)
        ge = 0
        for _ in range(N):
            sh = []
            for t in bl:
                s = list(t)
                random.shuffle(s)
                sh.append(s)
            ge += share(sh) >= obs
        p = (ge + 1) / (N + 1)
        return 'pairs found inside name bodies %.1f%%; p = %.4f' % (100 * obs, p), p < 0.05
    both('R4', 'bare-line pairs are name-body pairs', r4)

    def r5(L):
        items = [(bare(t), lstrat(len(t)), 1 if any(g in NUMS for g in t) else 0) for t in L if bare(t) or name_of(t)]
        o, p = strat_perm(items)
        return 'stratified difference (bare minus name lines) in numeral share %+.1f points; p = %.4f' % (100 * o, p), \
            o > 0 and p < 0.05
    both('R5', 'bare lines carry numerals', r5)

    say('## R6 body + 400 without an ending')
    bodies = {b for b, _ in T.names(AB)}
    pre = []
    for t in AB:
        if len(t) >= 3 and t[-1] == '400' and t[-2] not in END:
            s = t[:-1]
            if len(s) >= 3 and s[0] in ('817', '820', '861') and s[1] in ('2', '60', '1'):
                s = s[2:]
            if s:
                pre.append(s)
    o, p = shuffle_count(pre, bodies)
    say('- lines %d; the part before 400 a name body %d; p = %.4f.' % (len(pre), o, p))
    rec_('R6', p < 0.05)

    say('## R19 bare lines are shorter than names')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        bl = [len(t) for t in L if bare(t)]
        nl = [len(b) for b, _ in T.names(L)]
        o, p = rank_perm(nl, bl)
        ok = ok and o > 0 and p < 0.05
        say('- %s: bare mean %.2f, name bodies %.2f; rank difference %+.1f; p = %.4f.' % (
            lab, sum(bl) / len(bl), sum(nl) / len(nl), o, p))
    rec_('R19', ok)

    bl_ab = [t for t in AB if bare(t)]
    say('## R22 human figures stand last in bare lines')
    last = sum(1 for t in bl_ab for i, g in enumerate(t) if cat.get(g) == 'A' and i == len(t) - 1)
    alln = sum(1 for t in bl_ab for g in t if cat.get(g) == 'A')
    say('- human-figure tokens in bare lines: %d; last %d (%.0f%%); threshold 70%%.' % (alln, last, 100 * last / max(1, alln)))
    rec_('R22', alln and last / alln >= 0.7)

    say('## R23 fish stand last in bare lines')
    fl = sum(1 for t in bl_ab if t[-1] in FISH)
    ff = sum(1 for t in bl_ab if t[0] in FISH)
    p = binom_ge(fl, fl + ff)
    say('- bare lines ending in a fish %d, beginning with one %d; sign test p = %.4f.' % (fl, ff, p))
    rec_('R23', fl > ff and p < 0.05)

    say('## R24 a jar variant as ending')
    k, a, b, p = paired_last(bl_ab, lambda g: g in ('741', '742', '745'))
    say('- bare lines ending in 741 / 742 / 745: %d; discordant %d / %d; p = %.4f.' % (k, a, b, p))
    rec_('R24', a > b and p < 0.05)

    # F-based
    fl_ = [(r, ln) for r in intact for ln in r['seq']]
    seal_b = [ln for r, ln in fl_ if kind(r) == 'SEAL' and bare(ln)]
    tab_b = [ln for r, ln in fl_ if kind(r) == 'TAB' and bare(ln)]
    say('## R7 bare seal lines end in a head')
    a, c = sum(t[-1] in head for t in seal_b), sum(t[-1] in head for t in tab_b)
    p = hyper_ge(a, len(seal_b) - a, c, len(tab_b) - c)
    say('- %s.' % fline('bare seal lines ending in a head', a, len(seal_b), c, len(tab_b), p))
    rec_('R7', p < 0.05 and a / len(seal_b) > c / len(tab_b))
    say('## R8 bare tablet lines end in an attribute')
    a, c = sum(t[-1] in attr for t in tab_b), sum(t[-1] in attr for t in seal_b)
    p = hyper_ge(a, len(tab_b) - a, c, len(seal_b) - c)
    say('- %s.' % fline('bare tablet lines ending in an attribute', a, len(tab_b), c, len(seal_b), p))
    rec_('R8', p < 0.05 and a / len(tab_b) > c / len(seal_b))

    seal_l = [(r, ln) for r, ln in fl_ if kind(r) == 'SEAL' and len(ln) >= 2]
    say('## R9 bare seal lines outside the two cities')
    out = [bare(ln) for r, ln in seal_l if r['site'].strip() not in ('Mohenjo-daro', 'Harappa')]
    inn = [bare(ln) for r, ln in seal_l if r['site'].strip() in ('Mohenjo-daro', 'Harappa')]
    p = hyper_ge(sum(out), len(out) - sum(out), sum(inn), len(inn) - sum(inn))
    say('- %s.' % fline('seal lines bare outside Mohenjo-daro and Harappa', sum(out), len(out), sum(inn), len(inn), p))
    rec_('R9', p < 0.05 and sum(out) / len(out) > sum(inn) / len(inn))

    say('## R10 bare seal lines are later')
    ok = True
    for site in ('Mohenjo-daro', 'Harappa'):
        e = [bare(ln) for r, ln in seal_l if r['site'].strip() == site and level(site, recs[r['sealid']]) == 'E']
        l_ = [bare(ln) for r, ln in seal_l if r['site'].strip() == site and level(site, recs[r['sealid']]) == 'L']
        p = hyper_ge(sum(l_), len(l_) - sum(l_), sum(e), len(e) - sum(e))
        ok = ok and p < 0.05 and sum(l_) / max(1, len(l_)) > sum(e) / max(1, len(e))
        say('- %s.' % fline('%s later seal lines bare' % site, sum(l_), len(l_), sum(e), len(e), p))
    rec_('R10', ok)

    say('## R11 bare seals are not unicorn seals')
    mot = lambda r: ('' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip())
    known = [(r, ln) for r, ln in seal_l if mot(r) and mot(r) not in ('-', 'None')]
    bb = [not mot(r).startswith('Bull1') for r, ln in known if bare(ln)]
    nn = [not mot(r).startswith('Bull1') for r, ln in known if name_of(ln)]
    p = hyper_ge(sum(bb), len(bb) - sum(bb), sum(nn), len(nn) - sum(nn))
    say('- %s.' % fline('bare seal lines on other animals', sum(bb), len(bb), sum(nn), len(nn), p))
    rec_('R11', p < 0.05 and sum(bb) / len(bb) > sum(nn) / len(nn))

    say('## R12 bare seal lines lack the heading')
    items = [(bool(name_of(ln)), lstrat(len(ln)), 1 if headed(ln) else 0) for r, ln in seal_l
             if len(ln) >= 3 and (bare(ln) or name_of(ln))]
    o, p = strat_perm(items)
    say('- stratified difference (names minus bare) in headed share %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('R12', o > 0 and p < 0.05)

    say('## R18 bare tablet texts recur')
    tabs = [r for r in intact if kind(r) == 'TAB']
    tc = Counter(tuple(r['flat']) for r in tabs)
    bt = [c >= 2 for t, c in tc.items() if bare(list(t))]
    nt = [c >= 2 for t, c in tc.items() if name_of(list(t))]
    p = hyper_ge(sum(bt), len(bt) - sum(bt), sum(nt), len(nt) - sum(nt))
    say('- %s.' % fline('distinct bare tablet texts found 2+ times', sum(bt), len(bt), sum(nt), len(nt), p))
    rec_('R18', p < 0.05 and sum(bt) / len(bt) > sum(nt) / len(nt))

    say('## R25 a clitic without an ending is a tablet trait')
    tb = [t[-1] in ('400', '90') for t in tab_b]
    sb = [t[-1] in ('400', '90') for t in seal_b]
    p = hyper_ge(sum(tb), len(tb) - sum(tb), sum(sb), len(sb) - sum(sb))
    say('- %s.' % fline('bare tablet lines ending 400 / 90', sum(tb), len(tb), sum(sb), len(sb), p))
    rec_('R25', p < 0.05 and sum(tb) / len(tb) > sum(sb) / len(sb))

    # R13, R14
    say('## R13 position classes carry across transcriptions')

    def pos(L):
        c = {}
        for b, _ in T.names(L):
            for i, g in enumerate(b):
                w = 'last' if i == len(b) - 1 else ('first' if i == 0 else 'inside')
                c.setdefault(g, Counter())[w] += 1
        return c
    pa, pb = pos(A), pos(B)
    S = [g for g in pa if g in pb and sum(pa[g].values()) >= 10 and sum(pb[g].values()) >= 10]
    agree = [g for g in S if pa[g].most_common(1)[0][0] == pb[g].most_common(1)[0][0]]
    say('- signs with 10+ name tokens in both: %d; same majority position: %d (%.0f%%); threshold 80%%.' % (
        len(S), len(agree), 100 * len(agree) / len(S)))
    rec_('R13', len(agree) / len(S) >= 0.8)
    say('## R14 the classes cover most of B')
    known_cls = set(NUMS) | GRAMMAR | FORMULA | head | attr
    tb_ = [g for t in B for g in t]
    k = sum(g in known_cls for g in tb_)
    say('- B tokens in a class from A: %d of %d (%.1f%%); threshold 70%%. Classes: %d numerals, %d grammar, %d formula, '
        '%d heads, %d attributes.' % (k, len(tb_), 100 * k / len(tb_), len(NUMS), len(GRAMMAR), len(FORMULA), len(head),
                                      len(attr)))
    rec_('R14', k / len(tb_) >= 0.7)

    # R15-R17
    pots = [r for r in intact if kind(r) == 'POT']
    say('## R15 pot numerals are short-stroke')
    pn = [NUMS[g][1] == 'short' for r in pots for g in r['flat'] if g in NUMS]
    tn = [NUMS[g][1] == 'short' for r in tabs for g in r['flat'] if g in NUMS]
    p = hyper_ge(sum(pn), len(pn) - sum(pn), sum(tn), len(tn) - sum(tn))
    say('- %s.' % fline('short-stroke numerals on pots', sum(pn), len(pn), sum(tn), len(tn), p))
    rec_('R15', p < 0.05 and sum(pn) / len(pn) > sum(tn) / len(tn))
    say('## R16 pot values differ from tablet values')
    pv = [NUMS[g][0] for r in pots for ln in r['seq'] if all(x in NUMS for x in ln) for g in ln]
    tv = [NUMS[g][0] for r in tabs for g in r['flat'] if g in NUMS]
    X = ['pot'] * len(pv) + ['tab'] * len(tv)
    Y = pv + tv
    obs = T.mi(X, Y)
    ge = 0
    xx = X[:]
    for _ in range(N):
        random.shuffle(xx)
        ge += T.mi(xx, Y) >= obs
    p = (ge + 1) / (N + 1)
    say('- pot values %s; tablet values %s; MI %.4f; p = %.4f.' % (
        dict(Counter(pv).most_common(6)), dict(Counter(tv).most_common(6)), obs, p))
    rec_('R16', p < 0.05)
    say('## R17 pot numbers are single signs')
    no = [ln for r in pots for ln in r['seq'] if all(x in NUMS for x in ln)]
    k = sum(len(ln) == 1 for ln in no)
    say('- numbers-only pot lines: %d; single sign %d (%.0f%%); threshold 80%%.' % (len(no), k, 100 * k / max(1, len(no))))
    rec_('R17', no and k / len(no) >= 0.8)

    say('## R20 other signs follow the count')
    after = before = 0
    for r in tabs:
        f = r['flat']
        if not n700(r) or len(f) <= 2:
            continue
        i = next(i for i in range(len(f) - 1) if f[i] in NUMS and f[i + 1] == '700')
        after += i + 2 < len(f) and i == 0
        before += i > 0 and i + 2 == len(f)
    p = binom_ge(after, after + before)
    say('- count tokens with signs only after the count %d, only before %d; sign test p = %.4f.' % (after, before, p))
    rec_('R20', after > before and p < 0.05)

    say('## R21 Mohenjo-daro tablets carry names')
    items = [(r['site'].strip() == 'Mohenjo-daro', lstrat(len(r['flat'])),
              1 if any(name_of(ln) for ln in r['seq']) else 0) for r in tabs
             if not n700(r) and r['site'].strip() in ('Mohenjo-daro', 'Harappa')]
    o, p = strat_perm(items)
    say('- stratified difference (Mohenjo-daro minus Harappa) in tablets with an ending %+.1f points; p = %.4f.' % (
        100 * o, p))
    rec_('R21', o > 0 and p < 0.05)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test21.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
