"""Test of the twenty-seventh registered prediction set (PREDICTIONS.md, L1-L25).

Usage: python predict_test27.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test27.md. The fuller corpus is read with lines reversed.
"""
import math
import os
import random
import sys
from collections import Counter, defaultdict
from itertools import combinations

import icit_full
import predict_test13 as T
from numerals import NUMS
from predict_test4 import name_of
from predict_test7 import fisher_less
from predict_test14 import cat_of, hyper_ge
from predict_test15 import strat_perm
from predict_test16 import m_break
from predict_test17 import headed, rank_perm
from predict_test18 import level, lstrat, n700
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
END = ('740', '520')
AFF = ('231', '233', '235', '240')
random.seed(47)


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
    icit_full.LINES_REVERSED = True
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    names_in = lambda r: [name_of(ln) for ln in r['seq'] if name_of(ln)]
    ntabs = [r for r in intact if r['type'] == 'TAB:I' and names_in(r)]
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

    say('# Twenty-seventh registered predictions: the Harappa name records, numbers, labels')
    say()
    say('- name tablets: %d.' % len(ntabs))
    say()

    withn = [r for r in ntabs if any(g in NUMS for g in r['flat'])]
    say('## L1 the number opens the record')
    k = sum(r['flat'][0] in NUMS for r in withn)
    say('- name tablets with a number %d; number first %d (%.0f%%); threshold over 50%%.' % (len(withn), k, 100 * k / max(1, len(withn))))
    rec_('L1', withn and k / len(withn) > 0.5)

    say('## L2 the same person, different counts')
    grp = defaultdict(list)
    for r in withn:
        grp[names_in(r)[0][0]].append(tuple(NUMS[g][0] for g in r['flat'] if g in NUMS))
    prs = [(a, b) for v in grp.values() for a, b in combinations(v, 2)]
    d = sum(a != b for a, b in prs)
    say('- pairs %d; different numbers %d (%.0f%%); threshold over 50%%.' % (len(prs), d, 100 * d / max(1, len(prs))))
    rec_('L2', prs and d / len(prs) > 0.5)

    say('## L3 the same person, the same level')
    hl = [(names_in(r)[0][0], level('Harappa', recs[r['sealid']])) for r in ntabs if r['site'].strip() == 'Harappa']
    hl = [(b, l) for b, l in hl if l]
    idx = defaultdict(list)
    for i, (b, _) in enumerate(hl):
        idx[b].append(i)
    prs = [p_ for v in idx.values() for p_ in combinations(v, 2)]
    labs = [l for _, l in hl]
    obs = sum(labs[i] == labs[j] for i, j in prs) / max(1, len(prs))
    ge = 0
    for _ in range(N):
        random.shuffle(labs)
        ge += sum(labs[i] == labs[j] for i, j in prs) / max(1, len(prs)) >= obs
    p = (ge + 1) / (N + 1)
    say('- same-name pairs with a level %d; same level %.0f%%; p = %.4f.' % (len(prs), 100 * obs, p))
    rec_('L3', prs and p < 0.05)

    say('## L4 the named people held seals at Harappa')
    seal_sites = defaultdict(set)
    for r in seals:
        for b, _ in names_in(r):
            seal_sites[b].add(r['site'].strip())
    tb = {names_in(r)[0][0] for r in ntabs}
    both_ = [b for b in tb if b in seal_sites]
    k = sum('Harappa' in seal_sites[b] for b in both_)
    base = sum('Harappa' in s_ for s_ in seal_sites.values()) / len(seal_sites)
    n_ = len(both_)
    p = sum(math.comb(n_, i) * base ** i * (1 - base) ** (n_ - i) for i in range(k, n_ + 1)) if n_ else 1
    say('- names on both: %d; on a Harappa seal %d (%.0f%%); Harappa share of seal names %.0f%%; p = %.4f.' % (
        n_, k, 100 * k / max(1, n_), 100 * base, p))
    rec_('L4', n_ and p < 0.05)

    say('## L5 400 closes the record')
    t400 = [(i == len(r['flat']) - 1) for r in ntabs for i, g in enumerate(r['flat']) if g == '400' and i > 0 and r['flat'][i - 1] in END]
    say('- 400 after an ending on name tablets %d; text-final %d (%.0f%%); threshold 80%%.' % (len(t400), sum(t400), 100 * sum(t400) / max(1, len(t400))))
    rec_('L5', t400 and sum(t400) / len(t400) >= 0.8)

    say('## L6 tablet names are shorter')
    o, p = rank_perm([len(b) for r in seals for b, _ in names_in(r)], [len(b) for r in ntabs for b, _ in names_in(r)])
    say('- rank difference (seals minus name tablets) %+.1f; p = %.4f.' % (o, p))
    rec_('L6', o > 0 and p < 0.05)

    say('## L7 name-tablet numbers differ from seal numbers')
    xs = ['t'] * 0
    vt = [NUMS[g][0] for r in ntabs for g in r['flat'] if g in NUMS]
    vs = [NUMS[g][0] for r in seals for g in r['flat'] if g in NUMS]
    o, p = mi_perm(['t'] * len(vt) + ['s'] * len(vs), vt + vs)
    say('- name-tablet values %s; MI %.4f; p = %.4f.' % (dict(Counter(vt).most_common(6)), o, p))
    rec_('L7', p < 0.05)

    bare_t = [r for r in tabs if r['type'] in ('TAB:I', 'TAB:B') and not names_in(r) and len(r['flat']) >= 2]
    a = [r['flat'][-1] == '400' for r in bare_t if r['type'] == 'TAB:I']
    c = [r['flat'][-1] == '400' for r in bare_t if r['type'] == 'TAB:B']
    show('L8', 'bare incised tablets end in 400', gt('ending in 400, bare incised', sum(a), len(a), sum(c), len(c)))

    say('## L9 name-tablet counts differ from token counts')
    vc = [NUMS[x][0] for r in tabs if n700(r) for ln in r['seq'] for x, y in zip(ln, ln[1:]) if x in NUMS and y == '700']
    o, p = mi_perm(['t'] * len(vt) + ['c'] * len(vc), vt + vc)
    say('- count-token values %s; MI %.4f; p = %.4f.' % (dict(Counter(vc).most_common(4)), o, p))
    rec_('L9', p < 0.05)

    mot = lambda r: ('' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip())
    hs = [r for r in seals if r['site'].strip() == 'Harappa' and names_in(r) and mot(r) and mot(r) not in ('-', 'None')]
    a = [mot(r).startswith('Bull1') for r in hs if names_in(r)[0][0] in tb]
    c = [mot(r).startswith('Bull1') for r in hs if names_in(r)[0][0] not in tb]
    show('L23', 'the recorded people hold unicorn seals', gt('unicorn, Harappa seals named on tablets', sum(a), len(a), sum(c), len(c)))
    a = [e == '740' for r in seals for b, e in names_in(r) if b in tb]
    c = [e == '740' for r in seals for b, e in names_in(r) if b not in tb]
    show('L24', 'the recorded seal names are persons', gt('740, seal names also on tablets', sum(a), len(a), sum(c), len(c)))

    # numbers
    say('## L10 the stroke pair and fish are one unit')
    m77 = [r['seq'] for r in load(only_m77=True) if len(r['seq']) >= 2 and not any('?' in ln for ln in r['seq'])]
    ok = True
    for lab, texts in (('as listed', m77), ('reversed', [t[::-1] for t in m77])):
        a, na, c, nc = m_break(texts, lambda t: {g for g in range(1, len(t)) if t[g - 1] == '2' and t[g] in FISH})
        p = fisher_less(a, na - a, c, nc - c)
        ok = ok and p < 0.05 and a / max(1, na) < c / nc
        say('- lines %s: 2 | fish broken %d of %d, other gaps %d of %d (%.1f%%); p = %.4f.' % (lab, a, na, c, nc, 100 * c / nc, p))
    rec_('L10', ok)

    say('## L11 the stroke-pair fish are the 520 names')
    items = []
    for b, e in T.names(AB):
        if b[-1] in FISH and len(b) >= 2:
            inner = b[:-1]
            if '2' in inner:
                items.append((True, min(len(b), 4), 1 if e == '520' else 0))
            elif not any(g in NUMS for g in inner):
                items.append((False, min(len(b), 4), 1 if e == '520' else 0))
    o, p = strat_perm(items)
    say('- with the pair %d, without a numeral %d; stratified difference in 520 share %+.1f points; p = %.4f.' % (
        sum(l for l, _, _ in items), sum(not l for l, _, _ in items), 100 * o, p))
    rec_('L11', o > 0 and p < 0.05)

    say('## L12 each unit has its usual count')
    uc = defaultdict(Counter)
    for t in AB:
        for x, y in zip(t, t[1:]):
            if x in NUMS and kind(x) == 'long' and cat.get(y) in ('J', 'K'):
                uc[y][NUMS[x][0]] += 1
    units = {u: c for u, c in uc.items() if sum(c.values()) >= 10}
    modal = [u for u, c in units.items() if c.most_common(1)[0][1] / sum(c.values()) >= 0.5]
    say('- units with 10+ long counts: %s; with a modal value in half or more: %d of %d; threshold 80%%.' % (
        '; '.join('%s %s' % (u, dict(c)) for u, c in units.items()), len(modal), len(units)))
    rec_('L12', units and len(modal) / len(units) >= 0.8)

    theaded = lambda ln: name_of(ln) and name_of(ln)[0][-1] in NUMS and kind(name_of(ln)[0][-1]) == 'tiered'
    a = [bool(theaded(ln)) for r in seals for ln in r['seq'] if name_of(ln)]
    c = [bool(theaded(ln)) for r in tabs for ln in r['seq'] if name_of(ln)]
    show('L13', 'tiered-headed names are on seals', gt('tiered-headed, seal names', sum(a), len(a), sum(c), len(c)))
    say('## L14 tiered-headed names carry the heading')
    items = [(bool(theaded(t)), lstrat(len(t)), 1 if headed(t) else 0) for t in AB if name_of(t) and len(t) >= 3]
    o, p = strat_perm(items)
    say('- tiered-headed lines %d; stratified difference %+.1f points; p = %.4f.' % (sum(l for l, _, _ in items), 100 * o, p))
    rec_('L14', o > 0 and p < 0.05)

    say('## L15 long counts open the line')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        a = [i == 0 for t in L for i, g in enumerate(t) if g in NUMS and kind(g) == 'long']
        c = [i == 0 for t in L for i, g in enumerate(t) if g in NUMS and kind(g) == 'short']
        line, good = gt('long numerals opening the line', sum(a), len(a), sum(c), len(c))
        ok = ok and good
        say('- %s: %s.' % (lab, line))
    rec_('L15', ok)

    a = na = c = nc = 0
    for r in seals:
        for ln in r['seq']:
            for x, y in zip(ln, ln[1:]):
                if x in NUMS and y not in NUMS:
                    jk = cat.get(y) in ('J', 'K')
                    if kind(x) == 'long':
                        a += jk
                        na += 1
                    elif kind(x) == 'short':
                        c += jk
                        nc += 1
    show('L25', 'on seals too, long strokes count containers', gt('long before J / K, seals', a, na, c, nc))

    # variants
    say('## L16 the fish variants alternate with the plain fish')
    ns = set(T.names(AB))
    keyc = defaultdict(Counter)
    for body, end in ns:
        for i in range(len(body)):
            keyc[(end, len(body), body[:i], body[i + 1:])][body[i]] += 1
    by_sign = defaultdict(dict)
    for k_, c_ in keyc.items():
        for g, n2 in c_.items():
            by_sign[g][k_] = n2

    def pc(x, y):
        da, db = by_sign.get(x, {}), by_sign.get(y, {})
        if len(da) > len(db):
            da, db = db, da
        return sum(n2 * db.get(k_, 0) for k_, n2 in da.items())
    pairs = [('220', '233'), ('220', '235'), ('220', '240')]
    obs = sum(pc(x, y) for x, y in pairs)
    tk = Counter(g for b, _ in ns for g in b)
    S = [g for g in tk if tk[g] >= 5]
    q = T.quintiles(tk, S)
    byq = defaultdict(list)
    for g in S:
        byq[q[g]].append(g)
    ge = 0
    for _ in range(N):
        tot = 0
        for x, y in pairs:
            while True:
                u, v = random.choice(byq[q[x]]), random.choice(byq[q[y]])
                if u != v:
                    break
            tot += pc(u, v)
        ge += tot >= obs
    p = (ge + 1) / (N + 1)
    say('- pairs: %s; total %d; p = %.4f.' % (', '.join('%s/%s %d' % (x, y, pc(x, y)) for x, y in pairs), obs, p))
    rec_('L16', p < 0.05)
    nm = T.names(AB)
    a = [e == '520' for b, e in nm if b[-1] in AFF]
    c = [e == '520' for b, e in nm if b[-1] == '220']
    show('L17', 'names ending in an affixed fish take 520 less', lt('520, affixed-fish heads', sum(a), len(a), sum(c), len(c)))

    lr = lambda r: r['direction'] == 'L/R'
    a = [lr(r) for r in rowsA if r['type'] == 'TAB:I']
    c = [lr(r) for r in rowsA if r['type'] == 'TAB:B']
    show('L18', 'incised tablets run left to right', gt('left-to-right, incised', sum(a), len(a), sum(c), len(c)))
    a = [lr(r) for r in rowsA if r['type'].startswith('POT')]
    c = [lr(r) for r in rowsA if r['type'].startswith('SEAL')]
    show('L19', 'pots run left to right', gt('left-to-right, pots', sum(a), len(a), sum(c), len(c)))

    say('## L20 copper-tablet texts are short')
    o, p = rank_perm([len(r['flat']) for r in rowsA if r['type'].startswith('SEAL')],
                     [len(r['flat']) for r in rowsA if r['type'] == 'TAB:C'])
    say('- rank difference (seals minus copper tablets) %+.1f; p = %.4f.' % (o, p))
    rec_('L20', o > 0 and p < 0.05)
    tc = Counter((r['type'] == 'TAB:C', tuple(r['flat'])) for r in rowsA if r['type'] == 'TAB:C' or r['type'].startswith('SEAL'))
    a = [n2 >= 2 for (ct, _), n2 in tc.items() if ct]
    c = [n2 >= 2 for (ct, _), n2 in tc.items() if not ct]
    show('L21', 'copper-tablet texts recur', gt('distinct copper-tablet texts on 2+', sum(a), len(a), sum(c), len(c)))

    say('## L22 pot names carry no numbers')
    items = []
    for r in intact:
        k2 = 'pot' if r['type'].startswith('POT') else ('tab' if r['type'].startswith('TAB') else None)
        if not k2:
            continue
        for ln in r['seq']:
            if name_of(ln):
                items.append((k2 == 'tab', lstrat(len(ln)), 1 if any(g in NUMS for g in ln) else 0))
    o, p = strat_perm(items)
    say('- pot lines with an ending %d; stratified difference (tablets minus pots) %+.1f points; p = %.4f.' % (
        sum(not l for l, _, _ in items), 100 * o, p))
    rec_('L22', o > 0 and p < 0.05)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test27.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
