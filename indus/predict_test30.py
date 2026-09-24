"""Test of the thirtieth registered prediction set (PREDICTIONS.md, HA1-HA25): the Harappa system in detail.

Usage: python predict_test30.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test30.md. The fuller corpus is read with lines reversed.
"""
import os
import random
import statistics
import sys
from collections import Counter, defaultdict

import icit_full
import predict_test13 as T
from numerals import NUMS
from predict_test4 import name_of
from predict_test7 import fisher_less
from predict_test14 import classes, hyper_ge
from predict_test15 import strat_perm
from predict_test17 import headed, rank_perm
from predict_test18 import level, lstrat, n700
from predict_test29 import spf
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
END = ('740', '520')
random.seed(50)


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


def main(path):
    A, B = T.sample('A'), T.sample('B')
    AB = A + B
    rowsA = load()
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
    har = lambda r: r['site'].strip() == 'Harappa'
    hseals = [r for r in seals if har(r) and names_in(r)]
    ends = lambda b, rb: len(b) >= len(rb) and b[-len(rb):] == rb
    kind = lambda g: NUMS[g][1]
    mot = lambda r: ('' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip())
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    def show(k, title, lo):
        say('## %s %s' % (k, title))
        say('- %s.' % lo[0])
        rec_(k, lo[1])

    say('# Thirtieth registered predictions: the Harappa system in detail')
    say()

    # HA1, HA2
    rb = lambda r: names_in(r)[0][0]
    match = {id(r): [s for s in hseals if ends(names_in(s)[0][0], rb(r))] for r in rcp}
    say('## HA1 receipts lie near their seals')
    hs_d = [s for s in hseals if s['depth'] is not None]
    pairs = [(r['depth'], s['depth']) for r in rcp if r['depth'] is not None for s in match[id(r)] if s['depth'] is not None]
    if pairs:
        obs = statistics.median(abs(a - b) for a, b in pairs)
        per = [(r['depth'], sum(1 for s in match[id(r)] if s['depth'] is not None)) for r in rcp if r['depth'] is not None]
        ge = 0
        for _ in range(N):
            ds = [abs(d - random.choice(hs_d)['depth']) for d, k in per for _ in range(k)]
            ge += statistics.median(ds) <= obs
        p = (ge + 1) / (N + 1)
        say('- receipt-seal pairs with depths %d; median difference %.2f ft; p = %.4f.' % (len(pairs), obs, p))
        rec_('HA1', p < 0.05)
    else:
        say('- no pairs with depths.')
        rec_('HA1', False)
    say('## HA2 receipts share their seals\' level')
    lv = lambda r: level('Harappa', recs[r['sealid']])
    hs_l = [s for s in hseals if lv(s)]
    pairs = [(lv(r), lv(s)) for r in rcp if lv(r) for s in match[id(r)] if lv(s)]
    if pairs:
        obs = sum(a == b for a, b in pairs) / len(pairs)
        per = [(lv(r), sum(1 for s in match[id(r)] if lv(s))) for r in rcp if lv(r)]
        ge = 0
        for _ in range(N):
            v = [l_ == lv(random.choice(hs_l)) for l_, k in per for _ in range(k)]
            ge += sum(v) / len(v) >= obs
        p = (ge + 1) / (N + 1)
        say('- pairs %d; same level %.0f%%; p = %.4f.' % (len(pairs), 100 * obs, p))
        rec_('HA2', p < 0.05)
    else:
        say('- no pairs with levels.')
        rec_('HA2', False)

    all_seal_names = [b for r in seals for b, _ in names_in(r)]
    say('## HA3 receipt heads are shared by many seal-holders')
    heads_r = {rb(r)[-1] for r in rcp}
    many = [h for h in heads_r if len({b for b in all_seal_names if b[-1] == h}) >= 3]
    say('- receipt heads %d; ending 3+ different seal names %d (%.0f%%); threshold 50%%.' % (
        len(heads_r), len(many), 100 * len(many) / len(heads_r)))
    rec_('HA3', len(many) / len(heads_r) >= 0.5)
    hnames = [names_in(s)[0][0] for s in hseals]
    m_h = lambda b: any(ends(h, b) for h in hnames)
    rc = [m_h(rb(r)) for r in rcp]
    nt = [m_h(names_in(r)[0][0]) for r in tabs if r['type'] == 'TAB:I' and names_in(r) and not w400(r)]
    show('HA4', 'the 400 marks the seal-holder', lt('name tablets without 400 matching a Harappa seal', sum(nt), len(nt), sum(rc), len(rc)))
    mt = [m_h(names_in(r)[0][0]) for r in tabs if r['type'] == 'TAB:B' and names_in(r)]
    show('HA5', 'moulded name tablets are not receipts', lt('moulded name tablets matching a Harappa seal', sum(mt), len(mt), sum(rc), len(rc)))

    say('## HA6 the number stands right before the name')
    k = n = 0
    for r in rcp:
        f, b = r['flat'], rb(r)
        if not any(g in NUMS for g in f):
            continue
        for i in range(len(f) - len(b)):
            if tuple(f[i:i + len(b)]) == b and f[i + len(b)] in END:
                n += 1
                k += i > 0 and f[i - 1] in NUMS
                break
    say('- receipts with a number %d; number directly before the name %d (%.0f%%); threshold 70%%.' % (n, k, 100 * k / max(1, n)))
    rec_('HA6', n and k / n >= 0.7)

    say('## HA10 receipt heads are heads on seals')
    toks = [i == len(b) - 1 for b in all_seal_names for i, g in enumerate(b) if g in heads_r]
    say('- receipt-head tokens in seal names %d; last %d (%.0f%%); threshold 80%%.' % (len(toks), sum(toks), 100 * sum(toks) / max(1, len(toks))))
    rec_('HA10', toks and sum(toks) / len(toks) >= 0.8)
    rset = [rb(r) for r in rcp]
    mr = lambda b: any(ends(b, x) for x in rset)
    a = [mr(names_in(s)[0][0]) for s in hseals if s['type'] == 'SEAL:R']
    c = [mr(names_in(s)[0][0]) for s in hseals if s['type'] == 'SEAL:S']
    show('HA24', 'bar-seal names are receipt names', gt('matched by a receipt, Harappa bar seals', sum(a), len(a), sum(c), len(c)))
    a = [lv(s) == 'L' for s in hseals if lv(s) and mr(names_in(s)[0][0])]
    c = [lv(s) == 'L' for s in hseals if lv(s) and not mr(names_in(s)[0][0])]
    show('HA25', 'the receipt people are later', gt('later level, seals matched by a receipt', sum(a), len(a), sum(c), len(c)))

    # idioms
    say('## HA7 the same idioms on seals and tablets')
    vs, vt = defaultdict(Counter), defaultdict(Counter)
    for objs, d in ((seals, vs), (tabs, vt)):
        for r in objs:
            for ln in r['seq']:
                for x, y in zip(ln, ln[1:]):
                    if x in NUMS and y not in NUMS:
                        d[y][NUMS[x][0]] += 1
    sh = [y for y in vs if sum(vs[y].values()) >= 5 and sum(vt[y].values()) >= 5]
    same = [y for y in sh if vs[y].most_common(1)[0][0] == vt[y].most_common(1)[0][0]]
    say('- shared signs %d; same commonest value %d (%.0f%%); threshold 75%%.' % (len(sh), len(same), 100 * len(same) / max(1, len(sh))))
    rec_('HA7', sh and len(same) / len(sh) >= 0.75)
    say('## HA8 the number opens the name')
    ps, k = [], 0
    for b, _ in T.names(AB):
        idx = [i for i, g in enumerate(b) if g in NUMS]
        if len(b) >= 2 and len(idx) == 1:
            ps.append(1 / len(b))
            k += idx[0] == 0
    dist = [1.0]
    for q in ps:
        nd = [0.0] * (len(dist) + 1)
        for j, v in enumerate(dist):
            nd[j] += v * (1 - q)
            nd[j + 1] += v * q
        dist = nd
    p = sum(dist[k:])
    say('- names with one numeral %d; numeral first %d, expected %.1f; p = %.4f.' % (len(ps), k, sum(ps), p))
    rec_('HA8', p < 0.05)
    a = na = c = nc = 0
    for t in AB:
        for i in range(len(t) - 2):
            if t[i] in NUMS and t[i + 1] not in NUMS:
                e = t[i + 2] in END
                if t[i + 1] in FISH:
                    a += e
                    na += 1
                else:
                    c += e
                    nc += 1
    show('HA9', "'numeral + fish' is a whole name", gt('numeral + fish directly before the ending', a, na, c, nc))

    # tokens and time
    val = {'32': 2, '33': 3, '34': 4}
    toks_h = [r for r in tabs if har(r) and n700(r) and r['type'] in ('TAB:B', 'TAB:I')]
    tv = [(r['type'], next(val[x] for ln in r['seq'] for x, y in zip(ln, ln[1:]) if y == '700' and x in val)) for r in toks_h
          if any(y == '700' and x in val for ln in r['seq'] for x, y in zip(ln, ln[1:]))]
    say('## HA11 moulded tokens count less')
    lab = [t_ == 'TAB:B' for t_, _ in tv]
    vv = [v for _, v in tv]

    def st(lb):
        a_ = [v for v, l_ in zip(vv, lb) if l_]
        b_ = [v for v, l_ in zip(vv, lb) if not l_]
        return sum(b_) / len(b_) - sum(a_) / len(a_)
    obs = st(lab)
    ge = 0
    sh2 = lab[:]
    for _ in range(N):
        random.shuffle(sh2)
        ge += st(sh2) >= obs
    p = (ge + 1) / (N + 1)
    say('- incised minus moulded mean value %+.2f; p = %.4f.' % (obs, p))
    rec_('HA11', obs > 0 and p < 0.05)
    say('## HA12 moulded tokens come in larger batches')
    tc = Counter((r['type'], tuple(r['flat'])) for r in toks_h)
    it = [(ty == 'TAB:B', n_) for (ty, _), n_ in tc.items()]
    lab = [l_ for l_, _ in it]
    cn = [n_ for _, n_ in it]

    def st2(lb):
        a_ = [v for v, l_ in zip(cn, lb) if l_]
        b_ = [v for v, l_ in zip(cn, lb) if not l_]
        return sum(a_) / len(a_) - sum(b_) / len(b_)
    obs = st2(lab)
    ge = 0
    sh2 = lab[:]
    for _ in range(N):
        random.shuffle(sh2)
        ge += st2(sh2) >= obs
    p = (ge + 1) / (N + 1)
    say('- distinct token texts %d; mean copies moulded minus incised %+.2f; p = %.4f.' % (len(it), obs, p))
    rec_('HA12', obs > 0 and p < 0.05)
    inc = [r for r in tabs if har(r) and r['type'] == 'TAB:I' and lv(r)]
    rid = {id(r) for r in rcp}
    a = [id(r) in rid for r in inc if lv(r) == 'L']
    c = [id(r) in rid for r in inc if lv(r) == 'E']
    show('HA13', 'receipts fade later', lt('receipts among later incised tablets', sum(a), len(a), sum(c), len(c)))

    # titles
    hl = [(t[0], name_of(t)[1], spf(t)) for t in AB if name_of(t) and headed(t)]
    a = [e == '520' for o, e, _ in hl if o == '861']
    c = [e == '520' for o, e, _ in hl if o != '861']
    show('HA14', '861 heads the 520 names', gt('520, names headed by 861', sum(a), len(a), sum(c), len(c)))
    v = [e == '520' for _, e, s_ in hl if s_]
    say('## HA15 headed titled fish take 520')
    say('- headed stroke-pair fish names %d; 520 %d (%.0f%%); threshold 80%%.' % (len(v), sum(v), 100 * sum(v) / max(1, len(v))))
    rec_('HA15', v and sum(v) / len(v) >= 0.8)

    # seals, direction, labels
    sn = [(r, names_in(r)[0]) for r in seals if names_in(r) and mot(r) and mot(r) not in ('-', 'None')]
    a = [e == '520' for r, (b, e) in sn if not mot(r).startswith('Bull1')]
    c = [e == '520' for r, (b, e) in sn if mot(r).startswith('Bull1')]
    show('HA16', 'other-animal seals carry 520 names', gt('520, other-animal seals', sum(a), len(a), sum(c), len(c)))
    say('## HA17 other-animal seal names are shorter')
    o, p = rank_perm([len(b) for r, (b, e) in sn if mot(r).startswith('Bull1')], [len(b) for r, (b, e) in sn if not mot(r).startswith('Bull1')])
    say('- rank difference (unicorn minus other) %+.1f; p = %.4f.' % (o, p))
    rec_('HA17', o > 0 and p < 0.05)
    a = [names_in(r)[0][1] == '520' for r in seals if r['type'] == 'SEAL:R' and names_in(r)]
    c = [names_in(r)[0][1] == '520' for r in seals if r['type'] == 'SEAL:S' and names_in(r)]
    show('HA23', 'bar seals carry 520 names', gt('520, bar seals', sum(a), len(a), sum(c), len(c)))
    lr = lambda r: r['direction'] == 'L/R'
    pots = [r for r in rowsA if r['type'].startswith('POT')]
    a = [any(g in NUMS for g in r['flat']) for r in pots if lr(r)]
    c = [any(g in NUMS for g in r['flat']) for r in pots if not lr(r)]
    show('HA18', 'left-to-right pots carry numbers', gt('numeral, left-to-right pots', sum(a), len(a), sum(c), len(c)))
    a = [all(g in NUMS for g in r['flat']) for r in rowsA if lr(r)]
    c = [all(g in NUMS for g in r['flat']) for r in rowsA if not lr(r)]
    show('HA19', 'left-to-right texts are numbers', gt('numbers only, left-to-right', sum(a), len(a), sum(c), len(c)))
    a = [headed(t) for r in rowsA if r['type'] == 'TAB:C' for t in r['seq'] if len(t) >= 3]
    c = [headed(t) for r in rowsA if r['type'].startswith('SEAL') for t in r['seq'] if len(t) >= 3]
    show('HA20', 'copper tablets carry no heading', lt('headed, copper-tablet lines', sum(a), len(a), sum(c), len(c)))
    ct = [r['site'] for r in rowsA if r['type'] == 'TAB:C']
    say('## HA21 copper tablets are from Mohenjo-daro')
    say('- copper tablets %d; Mohenjo-daro %d (%.0f%%); threshold 90%%.' % (len(ct), ct.count('Mohenjo-daro'), 100 * ct.count('Mohenjo-daro') / len(ct)))
    rec_('HA21', ct.count('Mohenjo-daro') / len(ct) >= 0.9)
    say('## HA22 small objects carry labels')
    items = [(r['type'].startswith('SEAL'), lstrat(len(ln)), 1 if name_of(ln) else 0) for r in intact
             if r['type'].startswith(('SEAL', 'ROD', 'BNGL', 'MISC')) for ln in r['seq'] if len(ln) >= 2]
    o, p = strat_perm(items)
    say('- small-object lines %d; stratified difference (seals minus small objects) %+.1f points; p = %.4f.' % (
        sum(not l_ for l_, _, _ in items), 100 * o, p))
    rec_('HA22', o > 0 and p < 0.05)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test30.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
