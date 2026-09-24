"""Test of the twenty-fifth registered prediction set (PREDICTIONS.md, O1-O25).

Usage: python predict_test25.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test25.md. The fuller corpus is read with lines reversed (icit_full.LINES_REVERSED = True).
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
from predict_test18 import level, lstrat
from predict_test23 import lig_test
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
random.seed(45)
SINDH = {'Mohenjo-daro', 'Chanhu-daro', 'Chanhujo-daro', 'Allahdino', 'Amri', 'Kot Diji', 'Lakhanjo-daro'}
GUJ = {'Lothal', 'Dholavira', 'Surkotada', 'Desalpur', 'Kanmer', 'Gola Dhoro (Bagasra)', 'Gola Dhoro', 'Rangpur'}
NORTH = {'Harappa', 'Kalibangan', 'Banawali', 'Rakhigarhi', 'Farmana', 'Bhirrana', 'Rupar'}


def say(s=''):
    OUT.append(s)
    print(s)


def fline(lab, a, na, c, nc, p):
    return '%s %d of %d (%.1f%%) against %d of %d (%.1f%%), p = %.4f' % (
        lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


def fisher_gt(lab, a, na, c, nc):
    p = hyper_ge(a, na - a, c, nc - c)
    return fline(lab, a, na, c, nc, p), p < 0.05 and a / max(1, na) > c / max(1, nc)


def main(path):
    A, B = T.sample('A'), T.sample('B')
    rowsA = load()
    cat = cat_of()
    head, _ = classes(A)
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    say('# Twenty-fifth registered predictions: affixed signs, direction, numbers, bar seals')
    say()

    # O1-O5
    seq_gt = []
    for key, lig, x, y in (('O1', '235', '220', '480'), ('O2', '231', '220', '1'), ('O3', '415', '400', '1'),
                           ('O4', '741', '740', '1')):
        say('## %s %s as %s + %s' % (key, lig, x, y))
        rA = lig_test(A, lig, x, y)
        if rA is None:
            say('- A: under 10 tokens; not testable.')
            rec_(key, False)
            continue
        o, p, base, n_ = rA
        seq_gt.append(o > base)
        ok = p < 0.05
        say('- A: %s tokens %d; sequence score %.3f (modified-base %.3f); p = %.4f.' % (lig, n_, o, base, p))
        rB = lig_test(B, lig, x, y)
        if rB is not None:
            o, p, base, n_ = rB
            ok = ok and p < 0.05
            say('- B: %s tokens %d; sequence score %.3f; p = %.4f.' % (lig, n_, o, p))
        else:
            say('- B: under 10 tokens; A decides.')
        rec_(key, ok)
    say('## O5 sequence rather than modification, affixed signs')
    say('- testable %d; sequence above modified-base in %d.' % (len(seq_gt), sum(seq_gt)))
    rec_('O5', len(seq_gt) > 0 and all(seq_gt))

    # direction
    lr = lambda r: r['direction'] == 'L/R'
    region = lambda s: 'sindh' if s in SINDH else ('guj' if s in GUJ else ('north' if s in NORTH else None))
    say('## O6 left-to-right texts are Gujarati')
    out = [r for r in rowsA if r['site'] not in ('Mohenjo-daro', 'Harappa') and region(r['site'])]
    g = [lr(r) for r in out if region(r['site']) == 'guj']
    o_ = [lr(r) for r in out if region(r['site']) != 'guj']
    line, ok = fisher_gt('left-to-right share, Gujarat', sum(g), len(g), sum(o_), len(o_))
    say('- %s.' % line)
    rec_('O6', ok)
    say('## O7 left-to-right lines lack endings')
    items = [(not lr(r), lstrat(len(t)), 1 if name_of(t) else 0) for r in rowsA for t in r['seq'] if len(t) >= 2 and '?' not in t]
    o, p = strat_perm(items)
    say('- stratified difference (right-to-left minus left-to-right) in ending share %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('O7', o > 0 and p < 0.05)
    say('## O8 left-to-right seals carry other animals')
    sl = [r for r in rowsA if r['type'].startswith('SEAL') and r['motif'].strip()]
    a = [not r['motif'].startswith('Bull1') for r in sl if lr(r)]
    c = [not r['motif'].startswith('Bull1') for r in sl if not lr(r)]
    line, ok = fisher_gt('other animal, left-to-right seals', sum(a), len(a), sum(c), len(c))
    say('- %s.' % line)
    rec_('O8', ok)
    say('## O9 left-to-right texts are shorter')
    o, p = rank_perm([len(r['flat']) for r in rowsA if not lr(r)], [len(r['flat']) for r in rowsA if lr(r)])
    say('- rank difference (right-to-left minus left-to-right) %+.1f; p = %.4f.' % (o, p))
    rec_('O9', o > 0 and p < 0.05)
    say('## O23 moulded tablets run left to right')
    a = [lr(r) for r in rowsA if r['type'] == 'TAB:B']
    c = [lr(r) for r in rowsA if r['type'] != 'TAB:B']
    line, ok = fisher_gt('left-to-right, moulded tablets', sum(a), len(a), sum(c), len(c))
    say('- %s.' % line)
    rec_('O23', ok)
    say('## O24 seals and other objects differ in direction')
    a = [lr(r) for r in rowsA if r['type'].startswith('SEAL')]
    c = [lr(r) for r in rowsA if not r['type'].startswith('SEAL')]
    p = min(1, 2 * min(hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)),
                       hyper_ge(sum(c), len(c) - sum(c), sum(a), len(a) - sum(a))))
    say('- %s.' % fline('left-to-right, seals', sum(a), len(a), sum(c), len(c), p))
    rec_('O24', p < 0.05)

    # numbers
    def both(key, title, fn):
        say('## %s %s' % (key, title))
        ok = True
        for lab, L in (('A', A), ('B', B)):
            line, good = fn(L)
            ok = ok and good
            say('- %s: %s.' % (lab, line))
        rec_(key, ok)

    kind = lambda g: NUMS[g][1]

    def o10(L):
        prs = [(x, y) for t in L for x, y in zip(t, t[1:]) if x in NUMS and y in NUMS]
        obs = sum(kind(x) != kind(y) for x, y in prs) / len(prs)
        toks = [g for pr in prs for g in pr]
        ge = 0
        for _ in range(N):
            random.shuffle(toks)
            ge += sum(kind(toks[2 * i]) != kind(toks[2 * i + 1]) for i in range(len(prs))) / len(prs) >= obs
        p = (ge + 1) / (N + 1)
        return 'numeral pairs %d; mixed notation %.0f%%; p = %.4f' % (len(prs), 100 * obs, p), p < 0.05
    both('O10', 'side-by-side numerals mix notations', o10)

    say('## O11 smaller-first pairs end in a long stroke')
    a = na = c = nc = 0
    for t in A + B:
        for x, y in zip(t, t[1:]):
            if x in NUMS and y in NUMS and NUMS[x][0] != NUMS[y][0]:
                if NUMS[x][0] < NUMS[y][0]:
                    a += kind(y) == 'long'
                    na += 1
                else:
                    c += kind(y) == 'long'
                    nc += 1
    line, ok = fisher_gt('second numeral long, smaller-first pairs', a, na, c, nc)
    say('- %s.' % line)
    rec_('O11', ok)
    say('## O12 long strokes count containers and devices')
    a = na = c = nc = 0
    for t in A + B:
        for x, y in zip(t, t[1:]):
            if x in NUMS and y not in NUMS:
                jk = cat.get(y) in ('J', 'K')
                if kind(x) == 'long':
                    a += jk
                    na += 1
                elif kind(x) == 'short':
                    c += jk
                    nc += 1
    line, ok = fisher_gt('long numerals before J / K signs', a, na, c, nc)
    say('- %s.' % line)
    rec_('O12', ok)

    def o13(L):
        a = na = c = nc = 0
        for t in L:
            for x, y in zip(t, t[1:]):
                if x in NUMS and y not in NUMS:
                    s = kind(x) == 'short'
                    if y in FISH:
                        a += s
                        na += 1
                    else:
                        c += s
                        nc += 1
        return fisher_gt('short numerals before fish', a, na, c, nc)
    both('O13', 'numerals before fish are short-stroke', o13)

    def o25(L):
        a = na = c = nc = 0
        for b, _ in T.names(L):
            for i, g in enumerate(b):
                if g in NUMS:
                    inside = i < len(b) - 1
                    if kind(g) == 'tiered':
                        a += inside
                        na += 1
                    elif kind(g) == 'short':
                        c += inside
                        nc += 1
        return fisher_gt('tiered numerals inside names', a, na, c, nc)
    both('O25', 'tiered numerals stand inside names', o25)

    # bar seals, F with lines reversed
    icit_full.LINES_REVERSED = True
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    bs = [r for r in intact if r['type'] in ('SEAL:R', 'SEAL:S')]
    bar = lambda r: r['type'] == 'SEAL:R'
    say('## O15 bar seals are later')
    ok = True
    for site in ('Mohenjo-daro', 'Harappa'):
        l_ = [bar(r) for r in bs if r['site'].strip() == site and level(site, recs[r['sealid']]) == 'L']
        e = [bar(r) for r in bs if r['site'].strip() == site and level(site, recs[r['sealid']]) == 'E']
        line, good = fisher_gt('%s bar seals, later' % site, sum(l_), len(l_), sum(e), len(e))
        ok = ok and good
        say('- %s.' % line)
    rec_('O15', ok)
    say('## O16 bar seals come from smaller places')
    a = [r['site'].strip() not in ('Mohenjo-daro', 'Harappa') for r in bs if bar(r)]
    c = [r['site'].strip() not in ('Mohenjo-daro', 'Harappa') for r in bs if not bar(r)]
    line, ok = fisher_gt('bar seals outside the two cities', sum(a), len(a), sum(c), len(c))
    say('- %s.' % line)
    rec_('O16', ok)
    say('## O17 bar seals lack the heading')
    items = [(not bar(r), lstrat(len(ln)), 1 if headed(ln) else 0) for r in bs for ln in r['seq'] if len(ln) >= 3]
    o, p = strat_perm(items)
    say('- stratified difference (square minus bar) in headed share %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('O17', o > 0 and p < 0.05)
    say('## O18 bar-seal texts are longer')
    o, p = rank_perm([len(r['flat']) for r in bs if bar(r)], [len(r['flat']) for r in bs if not bar(r)])
    say('- bar mean %.2f, square %.2f; rank difference %+.1f; p = %.4f.' % (
        sum(len(r['flat']) for r in bs if bar(r)) / sum(map(bar, bs)),
        sum(len(r['flat']) for r in bs if not bar(r)) / (len(bs) - sum(map(bar, bs))), o, p))
    rec_('O18', o > 0 and p < 0.05)
    say('## O19 bar-seal lines end in a head')
    b10 = b01 = 0
    for r in bs:
        if not bar(r):
            continue
        for t in r['seq']:
            if len(t) < 2:
                continue
            j = random.randrange(len(t) - 1)
            x, y = t[-1] in head, t[j] in head
            b10 += x and not y
            b01 += y and not x
    p = binom_ge(b10, b10 + b01)
    say('- discordant %d / %d; p = %.4f.' % (b10, b01, p))
    rec_('O19', b10 > b01 and p < 0.05)
    say('## O20 bar seals run left to right')
    a = [lr(r) for r in rowsA if r['type'] == 'SEAL:R']
    c = [lr(r) for r in rowsA if r['type'] == 'SEAL:S']
    line, ok = fisher_gt('left-to-right, bar seals', sum(a), len(a), sum(c), len(c))
    say('- %s.' % line)
    rec_('O20', ok)

    # tablets
    tabs = [r for r in intact if r['type'] in ('TAB:B', 'TAB:I')]
    say('## O21 moulded texts recur')
    tc = Counter((r['type'], tuple(r['flat'])) for r in tabs)
    a = [c_ >= 2 for (ty, _), c_ in tc.items() if ty == 'TAB:B']
    c = [c_ >= 2 for (ty, _), c_ in tc.items() if ty == 'TAB:I']
    line, ok = fisher_gt('distinct moulded texts on 2+ tablets', sum(a), len(a), sum(c), len(c))
    say('- %s.' % line)
    rec_('O21', ok)
    say('## O22 tablets with 400 are incised')
    items = [('400' in r['flat'], lstrat(len(r['flat'])), 1 if r['type'] == 'TAB:I' else 0) for r in tabs]
    o, p = strat_perm(items)
    say('- stratified difference (with 400 minus without) in incised share %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('O22', o > 0 and p < 0.05)
    say('## O14 incised name tablets carry 400')
    named = [r for r in tabs if any(g in ('740', '520') for g in r['flat'])]
    has = lambda r: any(x in ('740', '520') and y == '400' for ln in r['seq'] for x, y in zip(ln, ln[1:]))
    a = [has(r) for r in named if r['type'] == 'TAB:I']
    c = [has(r) for r in named if r['type'] == 'TAB:B']
    line, ok = fisher_gt('ending + 400, incised name tablets', sum(a), len(a), sum(c), len(c))
    say('- %s.' % line)
    rec_('O14', ok)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test25.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
