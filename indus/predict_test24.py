"""Test of the twenty-fourth registered prediction set (PREDICTIONS.md, M1-M12): reading order, numbers, seals as
owned objects.

Usage: python predict_test24.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test24.md.
"""
import os
import random
import sys
from collections import Counter, defaultdict
from itertools import combinations

import icit_full
import predict_test13 as T
from numerals import NUMS
from predict_test4 import name_of
from predict_test14 import hyper_ge
from predict_test15 import binom_ge, strat_perm
from predict_test17 import headed
from predict_test18 import lstrat
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
random.seed(44)


def say(s=''):
    OUT.append(s)
    print(s)


def fline(lab, a, na, c, nc, p):
    return '%s %d of %d (%.1f%%) against %d of %d (%.1f%%), p = %.4f' % (
        lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


def junction_test(texts, single):
    pairs = Counter((x, y) for t in single for x, y in zip(t, t[1:]))
    b10 = b01 = 0
    for lines in texts:
        for k in range(len(lines) - 1):
            a = pairs[(lines[k][-1], lines[k + 1][0])] > 0
            r = pairs[(lines[k + 1][-1], lines[k][0])] > 0
            b10 += a and not r
            b01 += r and not a
    return b10, b01, binom_ge(b10, b10 + b01)


def main(path):
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    say('# Twenty-fourth registered predictions: reading order, numbers, seals as owned objects')
    say()
    rowsA = load()
    A, B = T.sample('A'), T.sample('B')

    # M1
    say('## M1 the recorded direction is right')
    single = [ln for r in rowsA if len(r['seq']) == 1 for ln in r['seq'] if '?' not in ln]
    allp = Counter((x, y) for t in single for x, y in zip(t, t[1:]))
    b10 = b01 = n = 0
    for r in rowsA:
        if r['direction'] != 'L/R':
            continue
        for t in r['seq']:
            if len(t) < 2 or '?' in t:
                continue
            own = Counter(zip(t, t[1:])) if len(r['seq']) == 1 else Counter()
            att = lambda x, y: allp[(x, y)] - own[(x, y)] > 0
            f = sum(att(x, y) for x, y in zip(t, t[1:])) / (len(t) - 1)
            rv = t[::-1]
            g = sum(att(x, y) for x, y in zip(rv, rv[1:])) / (len(t) - 1)
            n += 1
            b10 += f > g
            b01 += g > f
    p = binom_ge(b10, b10 + b01)
    say('- left-to-right lines: %d; recorded order more familiar %d, reversed %d; sign test p = %.4f.' % (n, b10, b01, p))
    rec_('M1', b10 > b01 and p < 0.05)

    # M2
    say('## M2 left-to-right texts come from smaller places')
    big = ('Mohenjo-daro', 'Harappa')
    lr = [r['site'] not in big for r in rowsA if r['direction'] == 'L/R']
    rl = [r['site'] not in big for r in rowsA if r['direction'] == 'R/L']
    p = hyper_ge(sum(lr), len(lr) - sum(lr), sum(rl), len(rl) - sum(rl))
    say('- %s.' % fline('left-to-right texts outside the two cities', sum(lr), len(lr), sum(rl), len(rl), p))
    rec_('M2', p < 0.05 and sum(lr) / len(lr) > sum(rl) / len(rl))

    # M3, M4
    say('## M3 line order in M77')
    rowsB = load(only_m77=True)
    multi = [r['seq'] for r in rowsB if len(r['seq']) >= 2 and not any('?' in ln for ln in r['seq'])]
    singleB = [r['seq'][0] for r in rowsB if len(r['seq']) == 1 and '?' not in r['seq'][0]]
    a, b, p = junction_test(multi, singleB)
    say('- junctions attested only as listed %d, only reversed %d; p = %.4f.' % (a, b, p))
    rec_('M3', a > b and p < 0.05)
    say('## M4 line order in the fuller corpus')
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    multiF = [r['seq'] for r in intact if len(r['seq']) >= 2]
    singleF = [r['seq'][0] for r in intact if len(r['seq']) == 1]
    a, b, p = junction_test(multiF, singleF)
    say('- junctions attested only as listed %d, only reversed %d; p = %.4f.' % (a, b, p))
    rec_('M4', a > b and p < 0.05)

    # M5-M7
    def both(key, title, fn):
        say('## %s %s' % (key, title))
        ok = True
        for lab, L in (('A', A), ('B', B)):
            line, good = fn(L)
            ok = ok and good
            say('- %s: %s.' % (lab, line))
        rec_(key, ok)

    def m5(L):
        d = u = 0
        for t in L:
            for x, y in zip(t, t[1:]):
                if x in NUMS and y in NUMS and NUMS[x][0] != NUMS[y][0]:
                    d += NUMS[x][0] > NUMS[y][0]
                    u += NUMS[x][0] < NUMS[y][0]
        p = binom_ge(d, d + u)
        return 'larger first %d, smaller first %d; p = %.4f' % (d, u, p), d > u and p < 0.05
    both('M5', 'compound numbers descend', m5)

    def m6(L):
        hi = [NUMS[g][1] == 'tiered' for t in L for g in t if g in NUMS and 5 <= NUMS[g][0] <= 8]
        lo = [NUMS[g][1] == 'tiered' for t in L for g in t if g in NUMS and 3 <= NUMS[g][0] <= 4]
        p = hyper_ge(sum(hi), len(hi) - sum(hi), sum(lo), len(lo) - sum(lo))
        return fline('tiered among values 5-8', sum(hi), len(hi), sum(lo), len(lo), p), \
            p < 0.05 and sum(hi) / max(1, len(hi)) > sum(lo) / max(1, len(lo))
    both('M6', 'the tiered form is for larger numbers', m6)

    def m7(L):
        f = [NUMS[x][0] for t in L for x, y in zip(t, t[1:]) if x in NUMS and y in FISH]
        o = [NUMS[x][0] for t in L for x, y in zip(t, t[1:]) if x in NUMS and y not in FISH and y not in NUMS]
        obs = sum(f) / len(f) - sum(o) / len(o)
        allv = f + o
        ge = 0
        for _ in range(N):
            random.shuffle(allv)
            ge += sum(allv[:len(f)]) / len(f) - sum(allv[len(f):]) / len(o) >= obs
        p = (ge + 1) / (N + 1)
        return 'mean value before fish %.2f (%d), before other signs %.2f (%d); p = %.4f' % (
            sum(f) / len(f), len(f), sum(o) / len(o), len(o), p), obs > 0 and p < 0.05
    both('M7', 'numbers before fish are larger', m7)

    # M8
    say('## M8 the clitics have a fixed order')
    o400 = o90 = 0
    for t in A + B:
        for x, y, z in zip(t, t[1:], t[2:]):
            if x in ('740', '520'):
                o400 += y == '400' and z == '90'
                o90 += y == '90' and z == '400'
    p = binom_ge(o400, o400 + o90)
    say('- ending + 400 + 90: %d; ending + 90 + 400: %d; p = %.4f.' % (o400, o90, p))
    rec_('M8', o400 > o90 and p < 0.05)

    # M9-M11
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    seals = []
    for r in intact:
        if not r['type'].startswith('SEAL'):
            continue
        for ln in r['seq']:
            nm = name_of(ln)
            if nm:
                mot = '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip().split(':')[0].strip()
                typ = r['type'] if r['type'] in ('SEAL:S', 'SEAL:R') else 'other'
                seals.append({'name': nm, 'mot': mot if mot and mot not in ('-', 'None') else None,
                              'typ': typ, 'head': headed(ln)})
                break
    byname = defaultdict(list)
    for i, s in enumerate(seals):
        byname[s['name']].append(i)
    for key, title, attr in (('M9', 'one name, one emblem', 'mot'), ('M10', 'one name, one seal shape', 'typ'),
                             ('M11', 'one name, one heading', 'head')):
        say('## %s %s' % (key, title))
        idx = [i for i, s in enumerate(seals) if s[attr] is not None]
        val = {i: seals[i][attr] for i in idx}
        pairs = [(a, b) for v in byname.values() for a, b in combinations([i for i in v if i in val], 2)]
        obs = sum(val[a] == val[b] for a, b in pairs) / max(1, len(pairs))
        ge = 0
        vals = [val[i] for i in idx]
        for _ in range(N):
            random.shuffle(vals)
            v2 = dict(zip(idx, vals))
            ge += sum(v2[a] == v2[b] for a, b in pairs) / max(1, len(pairs)) >= obs
        p = (ge + 1) / (N + 1)
        say('- same-name seal pairs: %d; agreeing %.0f%%; p = %.4f.' % (len(pairs), 100 * obs, p))
        rec_(key, len(pairs) > 0 and p < 0.05)

    # M12
    say('## M12 bar seals carry bare names')
    items = []
    for r in intact:
        if r['type'] not in ('SEAL:S', 'SEAL:R'):
            continue
        for ln in r['seq']:
            if len(ln) >= 2:
                items.append((r['type'] == 'SEAL:R', lstrat(len(ln)), 0 if name_of(ln) else 1))
    o, p = strat_perm(items)
    a_ = [x for l, _, x in items if l]
    b_ = [x for l, _, x in items if not l]
    say('- rectangular lines without an ending %d of %d, square %d of %d; stratified difference %+.1f points; p = %.4f.' % (
        sum(a_), len(a_), sum(b_), len(b_), 100 * o, p))
    rec_('M12', o > 0 and p < 0.05)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test24.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
