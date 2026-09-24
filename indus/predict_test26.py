"""Test of the twenty-sixth registered prediction set (PREDICTIONS.md): tablet records, numbers, direction, variants.

Usage: python predict_test26.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test26.md. The fuller corpus is read with lines reversed.
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
from predict_test15 import binom_ge, strat_perm
from predict_test17 import headed
from predict_test18 import level, lstrat
from predict_test25 import GUJ, NORTH, SINDH
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
END = ('740', '520')
random.seed(46)


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
    head, _ = classes(A)
    icit_full.LINES_REVERSED = True
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    def show(k, title, line_ok):
        say('## %s %s' % (k, title))
        say('- %s.' % line_ok[0])
        rec_(k, line_ok[1])

    say('# Twenty-sixth registered predictions: tablet records, numbers, direction, variants')
    say()

    names_in = lambda r: [name_of(ln) for ln in r['seq'] if name_of(ln)]
    w400 = lambda r: any(x in END and y == '400' for ln in r['seq'] for x, y in zip(ln, ln[1:]))
    hasnum = lambda r: any(g in NUMS for g in r['flat'])
    ntabs = [r for r in intact if r['type'] == 'TAB:I' and names_in(r)]
    seals = [r for r in intact if r['type'].startswith('SEAL')]
    tabs = [r for r in intact if r['type'].startswith('TAB')]
    say('- name tablets (incised, with an ending): %d; with 400: %d.' % (len(ntabs), sum(map(w400, ntabs))))
    say()

    # T1
    say('## T1 name tablets with 400 carry a number')
    items = [(w400(r), lstrat(len(r['flat'])), 1 if hasnum(r) else 0) for r in ntabs]
    o, p = strat_perm(items)
    say('- stratified difference (with 400 minus without) in numeral share %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('T1', o > 0 and p < 0.05)

    # T2
    say('## T2 the number follows the name')
    after = before = 0
    for r in ntabs:
        if not (w400(r) and hasnum(r)):
            continue
        f = r['flat']
        e = max(i for i, g in enumerate(f) if g in END)
        ni = [i for i, g in enumerate(f) if g in NUMS]
        after += all(i > e for i in ni)
        before += all(i < e for i in ni)
    p = binom_ge(after, after + before)
    say('- numbers all after the ending %d, all before it %d; p = %.4f.' % (after, before, p))
    rec_('T2', after > before and p < 0.05)

    kind = lambda g: NUMS[g][1]
    lng = lambda objs: ([kind(g) == 'long' for r in objs for g in r['flat'] if g in NUMS])
    a, c = lng(ntabs), lng(seals)
    show('T3', 'name-tablet numbers are long-stroke', gt('long-stroke, name tablets', sum(a), len(a), sum(c), len(c)))

    # T4
    sb = {nm[0] for r in seals for nm in names_in(r)}
    inc = [nm[0] in sb for r in ntabs for nm in names_in(r)]
    mou = [nm[0] in sb for r in tabs if r['type'] == 'TAB:B' for nm in names_in(r)]
    show('T4', 'incised-tablet names are seal names', gt('incised names found on seals', sum(inc), len(inc), sum(mou), len(mou)))

    # T5
    say('## T5 name tablets lack the heading')
    items = []
    for r in ntabs + seals:
        for ln in r['seq']:
            if len(ln) >= 3 and name_of(ln):
                items.append((r['type'].startswith('SEAL'), lstrat(len(ln)), 1 if headed(ln) else 0))
    o, p = strat_perm(items)
    say('- stratified difference (seals minus name tablets) in headed share %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('T5', o > 0 and p < 0.05)

    # T6
    ha = [r for r in tabs if r['site'].strip() == 'Harappa' and r['type'] in ('TAB:I', 'TAB:B')]
    lat = [r['type'] == 'TAB:I' for r in ha if level('Harappa', recs[r['sealid']]) == 'L']
    ear = [r['type'] == 'TAB:I' for r in ha if level('Harappa', recs[r['sealid']]) == 'E']
    show('T6', 'incised tablets are later', gt('incised share, later levels', sum(lat), len(lat), sum(ear), len(ear)))

    # T7
    a = [nm[1] == '740' for r in ntabs for nm in names_in(r)]
    c = [nm[1] == '740' for r in seals for nm in names_in(r)]
    show('T7', 'name-tablet names are persons', gt('740, name tablets', sum(a), len(a), sum(c), len(c)))

    # T8
    say('## T8 a bare 400 follows a head')
    b10 = b01 = 0
    for r in tabs:
        for ln in r['seq']:
            for i, g in enumerate(ln):
                if g == '400' and i >= 1 and ln[i - 1] not in END:
                    others = [j for j in range(len(ln)) if j not in (i, i - 1)]
                    if not others:
                        continue
                    j = random.choice(others)
                    x, y = ln[i - 1] in head, ln[j] in head
                    b10 += x and not y
                    b01 += y and not x
    p = binom_ge(b10, b10 + b01)
    say('- discordant %d / %d; p = %.4f.' % (b10, b01, p))
    rec_('T8', b10 > b01 and p < 0.05)

    # T9
    say('## T9 name tablets count in 700')
    k = n = 0
    for r in ntabs:
        for ln in r['seq']:
            for i, g in enumerate(ln):
                if g in NUMS and kind(g) == 'long':
                    n += 1
                    k += i + 1 < len(ln) and ln[i + 1] == '700'
    say('- long numerals on name tablets %d; followed by 700 %d (%.0f%%); threshold 50%%.' % (n, k, 100 * k / max(1, n)))
    rec_('T9', n > 0 and k / n >= 0.5)

    # T10
    a = [r['site'].strip() == 'Harappa' for r in ntabs if w400(r)]
    c = [r['site'].strip() == 'Harappa' for r in tabs if not (r in ntabs and w400(r))]
    show('T10', 'name tablets with 400 are from Harappa', gt('from Harappa, name tablets with 400', sum(a), len(a), sum(c), len(c)))

    # N1, N2, N7
    def both(key, title, fn):
        say('## %s %s' % (key, title))
        ok = True
        for lab, L in (('A', A), ('B', B)):
            line, good = fn(L)
            ok = ok and good
            say('- %s: %s.' % (lab, line))
        rec_(key, ok)

    def n1(L):
        prs = [(NUMS[x][0], y) for t in L for x, y in zip(t, t[1:]) if x in NUMS and kind(x) == 'long' and y not in NUMS]
        o, p = mi_perm([v for v, _ in prs], [y for _, y in prs])
        return '%d pairs; MI(value; next sign) %.3f bits; p = %.4f' % (len(prs), o, p), p < 0.05
    both('N1', 'the unit decides the long count', n1)

    def n2(L):
        prs = [(NUMS[x][0], y in FISH) for t in L for x, y in zip(t, t[1:]) if x in NUMS and y not in NUMS]
        o, p = mi_perm([v for v, _ in prs], [f for _, f in prs])
        vf = Counter(v for v, f in prs if f)
        return 'values before fish %s; MI %.4f bits; p = %.4f' % (dict(vf.most_common(6)), o, p), p < 0.05
    both('N2', 'fish take their own numbers', n2)

    def n7(L):
        a = na = c = nc = 0
        for t in L:
            for x, y in zip(t, t[1:]):
                if x in NUMS and kind(x) == 'tiered':
                    a += y in END
                    na += 1
                elif x in NUMS and kind(x) == 'short':
                    c += y in END
                    nc += 1
        return gt('tiered numerals directly before the ending', a, na, c, nc)
    both('N7', 'tiered numbers stand before the ending', n7)

    # N5
    a = na = c = nc = 0
    for t in AB:
        for i in range(len(t) - 1):
            x, y = t[i], t[i + 1]
            if x in NUMS and y not in NUMS:
                fin = i + 1 == len(t) - 1
                if kind(x) == 'long' and cat.get(y) in ('J', 'K'):
                    a += fin
                    na += 1
                elif kind(x) == 'short':
                    c += fin
                    nc += 1
    show('N5', 'counts close their line', gt('long + J / K pairs ending the line', a, na, c, nc))

    # N6
    a, c = lng(tabs), lng(seals)
    show('N6', 'tablet numbers are long-stroke', gt('long-stroke, tablets', sum(a), len(a), sum(c), len(c)))

    # D1-D3
    lr = lambda r: r['direction'] == 'L/R'
    a = [lr(r) for r in rowsA if r['type'] == 'TAB:C']
    c = [lr(r) for r in rowsA if r['type'] != 'TAB:C']
    show('D1', 'copper tablets run left to right', gt('left-to-right, copper tablets', sum(a), len(a), sum(c), len(c)))
    direct = lambda ty: ty in ('TAB:I', 'TAB:C') or ty.startswith(('POT', 'TAG'))
    carved = lambda ty: ty.startswith('SEAL') or ty == 'TAB:B'
    a = [lr(r) for r in rowsA if direct(r['type'])]
    c = [lr(r) for r in rowsA if carved(r['type'])]
    show('D2', 'written directly, left to right', gt('left-to-right, objects written directly', sum(a), len(a), sum(c), len(c)))
    say('## D3 left-to-right lines lack the heading')
    items = [(not lr(r), lstrat(len(t)), 1 if headed(t) else 0) for r in rowsA for t in r['seq'] if len(t) >= 3 and '?' not in t]
    o, p = strat_perm(items)
    say('- stratified difference (right-to-left minus left-to-right) %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('D3', o > 0 and p < 0.05)

    # V2
    toks = [(i == len(t) - 1) for t in AB for i, g in enumerate(t) if g in ('741', '742', '745')]
    say('## V2 the jar variants do not end lines')
    say('- tokens %d; line-final %d (%.1f%%); threshold under 10%%.' % (len(toks), sum(toks), 100 * sum(toks) / len(toks)))
    rec_('V2', sum(toks) / len(toks) < 0.1)

    # V3
    say('## V3 base and variant alternate in the same names')
    ns = set(T.names(AB))
    keyc = defaultdict(Counter)
    for body, end in ns:
        for i in range(len(body)):
            keyc[(end, len(body), body[:i], body[i + 1:])][body[i]] += 1
    by_sign = defaultdict(dict)
    for k_, c_ in keyc.items():
        for g, n_ in c_.items():
            by_sign[g][k_] = n_

    def pc(a, b):
        da, db = by_sign.get(a, {}), by_sign.get(b, {})
        if len(da) > len(db):
            da, db = db, da
        return sum(n_ * db.get(k_, 0) for k_, n_ in da.items())
    pairs = [('220', '231'), ('400', '415'), ('740', '741')]
    obs = sum(pc(a, b) for a, b in pairs)
    tk = Counter(g for b, _ in ns for g in b)
    S = [g for g in tk if tk[g] >= 5]
    q = T.quintiles(tk, S)
    byq = defaultdict(list)
    for g in S:
        byq[q[g]].append(g)
    ge = 0
    for _ in range(N):
        tot = 0
        for a, b in pairs:
            while True:
                x, y = random.choice(byq[q[a]]), random.choice(byq[q[b]])
                if x != y:
                    break
            tot += pc(x, y)
        ge += tot >= obs
    p = (ge + 1) / (N + 1)
    say('- substitution pairs: %s; total %d; p = %.4f.' % (', '.join('%s/%s %d' % (a, b, pc(a, b)) for a, b in pairs), obs, p))
    rec_('V3', p < 0.05)

    # V4
    a = [i == len(b) - 1 for b, _ in T.names(AB) for i, g in enumerate(b) if g in ('231', '233', '235', '240')]
    c = [i == len(b) - 1 for b, _ in T.names(AB) for i, g in enumerate(b) if g == '220']
    show('V4', 'affixed fish are attributes', lt('last in name, affixed fish', sum(a), len(a), sum(c), len(c)))

    # X1, X2
    a = [nm[1] == '740' for r in intact if r['type'].startswith('TAG') for nm in names_in(r)]
    c = [nm[1] == '740' for r in seals for nm in names_in(r)]
    show('X1', 'sealing names are persons', gt('740, sealings', sum(a), len(a), sum(c), len(c)))
    say('## X2 copper tablets carry no endings')
    items = [(r['type'].startswith('SEAL'), lstrat(len(t)), 1 if name_of(t) else 0) for r in rowsA
             for t in r['seq'] if len(t) >= 2 and '?' not in t and (r['type'] == 'TAB:C' or r['type'].startswith('SEAL'))]
    o, p = strat_perm(items)
    say('- stratified difference (seals minus copper tablets) in ending share %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('X2', o > 0 and p < 0.05)

    # S5, S6
    say('## S5 the ending balance differs by region')
    reg = lambda s: 'sindh' if s in SINDH else ('guj' if s in GUJ else ('north' if s in NORTH else None))
    it = []
    for r in seals:
        nm = names_in(r)
        g = reg(r['site'].strip())
        if nm and g:
            it.append((g, nm[0][1]))
    o, p = mi_perm([a for a, _ in it], [b for _, b in it])
    say('- %s; MI %.4f; p = %.4f.' % (', '.join('%s 520 %d of %d' % (g, sum(1 for a, b in it if a == g and b == '520'),
                                                                   sum(1 for a, _ in it if a == g)) for g in ('sindh', 'guj', 'north')), o, p))
    rec_('S5', p < 0.05)
    say('## S6 the ending balance changes over time at Mohenjo-daro')
    e = [names_in(r)[0][1] == '520' for r in seals if r['site'].strip() == 'Mohenjo-daro' and names_in(r)
         and level('Mohenjo-daro', recs[r['sealid']]) == 'E']
    l_ = [names_in(r)[0][1] == '520' for r in seals if r['site'].strip() == 'Mohenjo-daro' and names_in(r)
          and level('Mohenjo-daro', recs[r['sealid']]) == 'L']
    p = min(1, 2 * min(hyper_ge(sum(l_), len(l_) - sum(l_), sum(e), len(e) - sum(e)),
                       fisher_less(sum(l_), len(l_) - sum(l_), sum(e), len(e) - sum(e))))
    say('- %s.' % fline('520, later', sum(l_), len(l_), sum(e), len(e), p))
    rec_('S6', p < 0.05)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test26.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
