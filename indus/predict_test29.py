"""Test of the twenty-ninth registered prediction set (PREDICTIONS.md, J1-J25).

Usage: python predict_test29.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test29.md. The fuller corpus is read with lines reversed.
"""
import math
import os
import random
import sys
from collections import Counter, defaultdict

import icit_full
import predict_test13 as T
from gulf import IRAN_WEST, WEST
from numerals import NUMS
from predict_test4 import name_of
from predict_test7 import fisher_less
from predict_test14 import cat_of, classes, hyper_ge
from predict_test15 import binom_ge, strat_perm
from predict_test16 import m_break
from predict_test17 import headed
from predict_test18 import level, lstrat, n700
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
END = ('740', '520')
random.seed(49)


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


def spf(t):
    return any(x == '2' and y in FISH for x, y in zip(t, t[1:]))


def main(path):
    A, B = T.sample('A'), T.sample('B')
    AB = A + B
    cat = cat_of()
    head, _ = classes(A)
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
    hasnum = lambda t: any(g in NUMS for g in t)
    mot = lambda r: recs[r['sealid']][18].strip()
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    def show(k, title, lo):
        say('## %s %s' % (k, title))
        say('- %s.' % lo[0])
        rec_(k, lo[1])

    say('# Twenty-ninth registered predictions: receipts, number idioms, titled names')
    say()

    # receipts
    rb = [names_in(r)[0][0] for r in rcp]
    seal_names = [(r['site'].strip(), b, e) for r in seals for b, e in names_in(r)]
    ends_sites = defaultdict(set)
    for s_, b, _ in seal_names:
        for k in range(1, len(b)):
            ends_sites[b[k:]].add(s_)
    m = [b for b in rb if b in ends_sites]
    k = sum('Harappa' in ends_sites[b] for b in m)
    base = sum(1 for s_, _, _ in seal_names if s_ == 'Harappa') / len(seal_names)
    p = sum(math.comb(len(m), i) * base ** i * (1 - base) ** (len(m) - i) for i in range(k, len(m) + 1)) if m else 1
    say('## J1 receipts name Harappa people')
    say('- receipt names matching a seal-name end %d; at Harappa %d (%.0f%%); Harappa share of seal names %.0f%%; p = %.4f.' % (
        len(m), k, 100 * k / max(1, len(m)), 100 * base, p))
    rec_('J1', m and p < 0.05)
    one = [b[0] in head for b in rb if len(b) == 1]
    say('## J2 single-sign receipt names are heads')
    say('- single-sign receipt names %d; head-class %d (%.0f%%); threshold 50%%.' % (len(one), sum(one), 100 * sum(one) / max(1, len(one))))
    rec_('J2', one and sum(one) / len(one) >= 0.5)
    rset = set(rb)
    endsr = lambda b: any(b[k:] in rset for k in range(1, len(b)))
    a = [e == '740' for _, b, e in seal_names if endsr(b)]
    c = [e == '740' for _, b, e in seal_names if not endsr(b)]
    show('J3', 'the receipt people are persons', gt('740, seal names ending in a receipt name', sum(a), len(a), sum(c), len(c)))
    say('## J4 copies and number')
    tc = Counter(tuple(r['flat']) for r in rcp)
    it = [(next(NUMS[g][0] for g in t if g in NUMS), n_) for t, n_ in tc.items() if hasnum(t)]
    if len(it) >= 3:
        xs, ys = [a for a, _ in it], [b for _, b in it]
        rho = T.spearman(xs, ys)
        ge = 0
        yy = ys[:]
        for _ in range(N):
            random.shuffle(yy)
            ge += T.spearman(xs, yy) >= rho
        p = (ge + 1) / (N + 1)
        say('- distinct receipts with a number %d (value, copies: %s); Spearman %.3f; p = %.4f.' % (len(it), it, rho, p))
        rec_('J4', rho > 0 and p < 0.05)
    else:
        say('- too few distinct receipts with a number.')
        rec_('J4', False)
    say('## J5 the receipt heads are titled on seals')
    rheads = {b[-1] for b in rb}
    items = [(name_of(ln)[0][-1] in rheads, lstrat(len(ln)), 1 if headed(ln) else 0) for r in seals for ln in r['seq']
             if name_of(ln) and len(ln) >= 3]
    o, p = strat_perm(items)
    say('- stratified difference %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('J5', o > 0 and p < 0.05)
    say('## J6 receipt heads are a different kind')
    x1 = [cat[b[-1]] for b in rb if b[-1] in cat]
    x2 = [cat[b[-1]] for _, b, _ in seal_names if b[-1] in cat]
    o, p = mi_perm(['r'] * len(x1) + ['s'] * len(x2), x1 + x2)
    say('- receipt heads %s; MI %.4f; p = %.4f.' % (dict(Counter(x1)), o, p))
    rec_('J6', p < 0.05)

    # idioms
    say('## J7 a number and its sign are one unit')
    m77 = [r['seq'] for r in load(only_m77=True) if len(r['seq']) >= 2 and not any('?' in ln for ln in r['seq'])]
    ok = True
    for lab, texts in (('as listed', m77), ('reversed', [t[::-1] for t in m77])):
        a, na, c, nc = m_break(texts, lambda t: {g for g in range(1, len(t)) if t[g - 1] in NUMS and t[g] not in NUMS})
        p = fisher_less(a, na - a, c, nc - c)
        ok = ok and p < 0.05 and a / max(1, na) < c / nc
        say('- lines %s: numeral | sign broken %d of %d (%.1f%%), other gaps %d of %d (%.1f%%); p = %.4f.' % (
            lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / nc, p))
    rec_('J7', ok)
    say('## J8 each sign has its number')
    bs = defaultdict(Counter)
    for t in AB:
        for x, y in zip(t, t[1:]):
            if x in NUMS and y not in NUMS:
                bs[y][NUMS[x][0]] += 1
    shares = [c.most_common(1)[0][1] / sum(c.values()) for c in bs.values() if sum(c.values()) >= 10]
    mean_ = sum(shares) / len(shares)
    say('- signs after a numeral 10+ times: %d; mean share of the commonest value %.2f; threshold 0.60.' % (len(shares), mean_))
    rec_('J8', mean_ >= 0.6)
    say('## J9 tablets count, seals name')
    ts, ss = defaultdict(Counter), defaultdict(Counter)
    for objs, d in ((tabs, ts), (seals, ss)):
        for r in objs:
            for ln in r['seq']:
                for x, y in zip(ln, ln[1:]):
                    if x in NUMS and kind(x) == 'long' and y not in NUMS:
                        d[y][NUMS[x][0]] += 1
    units = [u for u in ts if sum(ts[u].values()) >= 5 and sum(ss[u].values()) >= 5]
    more = sum(T.entropy(ts[u]) > T.entropy(ss[u]) for u in units)
    less_ = sum(T.entropy(ts[u]) < T.entropy(ss[u]) for u in units)
    p = binom_ge(more, more + less_)
    say('- shared units %d (%s); tablets more varied %d, seals %d; p = %.4f.' % (len(units), ', '.join(units), more, less_, p))
    rec_('J9', units and more > less_ and p < 0.05)
    k = sum(1 for r in seals if n700(r))
    say('## J25 seals do not count 700')
    say('- seals with numeral + 700: %d of %d (%.2f%%); threshold under 1%%.' % (k, len(seals), 100 * k / len(seals)))
    rec_('J25', k / len(seals) < 0.01)

    # titled names
    sl = [(r, ln) for r in seals for ln in r['seq'] if name_of(ln)]
    a = [r['site'].strip() == 'Mohenjo-daro' for r, ln in sl if spf(ln)]
    c = [r['site'].strip() == 'Mohenjo-daro' for r, ln in sl if not spf(ln)]
    show('J10', 'titled fish names are Mohenjo-daro', gt('Mohenjo-daro, stroke-pair fish names', sum(a), len(a), sum(c), len(c)))
    kn = [(r, ln) for r, ln in sl if mot(r) and mot(r) not in ('-', 'None')]
    a = [mot(r).startswith('Bull1') for r, ln in kn if spf(ln)]
    c = [mot(r).startswith('Bull1') for r, ln in kn if not spf(ln)]
    show('J11', 'titled fish names are on unicorn seals', gt('unicorn, stroke-pair fish names', sum(a), len(a), sum(c), len(c)))
    a = [spf(ln) for r in tabs for ln in r['seq'] if name_of(ln)]
    c = [spf(ln) for r, ln in sl]
    show('J12', 'titled fish names are not on tablets', lt('stroke-pair fish, tablet names', sum(a), len(a), sum(c), len(c)))
    say('## J13 the opener differs for titled fish names')
    it = [(t[0], spf(t)) for t in AB if name_of(t) and headed(t)]
    o, p = mi_perm([a for a, _ in it], [b for _, b in it])
    say('- headed lines %d (stroke-pair fish %d); %s; MI %.4f; p = %.4f.' % (
        len(it), sum(b for _, b in it), dict(Counter(it)), o, p))
    rec_('J13', p < 0.05)

    # where numbers occur
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = {r['sealid'] for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST}
    home = [r for r in rows if r['sealid'] not in west and recs[r['sealid']][2] not in ('Other',)]
    wl = [ln for r in rows if r['sealid'] in west for ln in r['seq'] if len(ln) >= 2]
    bylen = defaultdict(list)
    for r in home:
        for ln in r['seq']:
            if len(ln) >= 2:
                bylen[len(ln)].append(ln)

    def draw(n):
        while n not in bylen:
            n -= 1
        return random.choice(bylen[n])
    obs = sum(map(hasnum, wl)) / len(wl)
    null = [sum(hasnum(draw(len(t))) for t in wl) / len(wl) for _ in range(N)]
    p = (sum(1 for x in null if x <= obs) + 1) / (N + 1)
    say('## J14 foreign texts carry no numbers')
    say('- West Asian lines with a numeral %.0f%% (%d lines); home draws %.0f%%; p = %.4f.' % (100 * obs, len(wl), 100 * sum(null) / N, p))
    rec_('J14', p < 0.05)

    def strat_type(key, title, lab_fn, keep):
        say('## %s %s' % (key, title))
        items = [(lab_fn(r), lstrat(len(ln)), 1 if hasnum(ln) else 0) for r in intact if keep(r) for ln in r['seq'] if len(ln) >= 2]
        o, p = strat_perm(items)
        say('- labelled lines %d; stratified difference %+.1f points; p = %.4f.' % (sum(l for l, _, _ in items), 100 * o, p))
        rec_(key, o > 0 and p < 0.05)
    strat_type('J15', 'cylinder seals carry no numbers', lambda r: r['type'] == 'SEAL:S',
               lambda r: r['type'] in ('SEAL:S', 'SEAL:C', 'SEAL:CY'))
    ha = [r for r in tabs if r['site'].strip() == 'Harappa' and n700(r) and r['type'] in ('TAB:B', 'TAB:I')]
    a = [r['type'] == 'TAB:B' for r in ha if level('Harappa', recs[r['sealid']]) == 'L']
    c = [r['type'] == 'TAB:B' for r in ha if level('Harappa', recs[r['sealid']]) == 'E']
    show('J16', 'later tokens are moulded', gt('moulded, later tokens', sum(a), len(a), sum(c), len(c)))
    sn = lambda site: [kind(g) for r in seals if r['site'].strip() == site for g in r['flat'] if g in NUMS]
    md, hp = sn('Mohenjo-daro'), sn('Harappa')
    show('J17', 'tiered numbers are Mohenjo-daro', gt('tiered, Mohenjo-daro seals', md.count('tiered'), len(md), hp.count('tiered'), len(hp)))
    show('J18', 'long numbers are Harappa', gt('long, Harappa seals', hp.count('long'), len(hp), md.count('long'), len(md)))
    strat_type('J19', 'bar seals count', lambda r: r['type'] == 'SEAL:R', lambda r: r['type'] in ('SEAL:S', 'SEAL:R'))
    strat_type('J20', 'unicorn seals carry fewer numbers', lambda r: not mot(r).startswith('Bull1'),
               lambda r: r['type'].startswith('SEAL') and mot(r) and mot(r) not in ('-', 'None'))
    say('## J21 the heading and numbers exclude each other')
    ls_ = [ln for r in seals for ln in r['seq'] if len(ln) >= 3]
    a = sum(1 for ln in ls_ if headed(ln) and hasnum(ln))
    b = sum(1 for ln in ls_ if headed(ln) and not hasnum(ln))
    c = sum(1 for ln in ls_ if not headed(ln) and hasnum(ln))
    d = sum(1 for ln in ls_ if not headed(ln) and not hasnum(ln))
    p = fisher_less(a, b, c, d)
    say('- headed lines with a numeral %d of %d; headless %d of %d; p = %.4f.' % (a, a + b, c, c + d, p))
    rec_('J21', p < 0.05 and a / (a + b) < c / (c + d))

    nm = T.names(AB)
    h = [hasnum(b) for b, _ in nm if cat.get(b[-1]) == 'A']
    say('## J22 persons are not counted')
    say('- human-headed names with a numeral %d of %d (%.1f%%); threshold under 5%%.' % (sum(h), len(h), 100 * sum(h) / len(h)))
    rec_('J22', sum(h) / len(h) < 0.05)
    say('## J23 fish names carry numbers')
    items = [(b[-1] in FISH, min(len(b), 4), 1 if hasnum(b) else 0) for b, _ in nm if len(b) >= 2]
    o, p = strat_perm(items)
    say('- stratified difference %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('J23', o > 0 and p < 0.05)
    a = [e == '520' for b, e in nm if any(g in NUMS and kind(g) == 'tiered' for g in b)]
    c = [e == '520' for b, e in nm if any(g in NUMS and kind(g) == 'short' for g in b) and not any(g in NUMS and kind(g) == 'tiered' for g in b)]
    show('J24', 'tiered-number names take 520', gt('520, names with a tiered numeral', sum(a), len(a), sum(c), len(c)))

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test29.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
