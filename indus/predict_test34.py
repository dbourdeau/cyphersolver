"""Test of the thirty-fourth registered prediction set (PREDICTIONS.md, LB1-LB25): labels against names, and dates.

Usage: python predict_test34.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test34.md. A for the label tests, F (lines reversed) for dates and findspots.
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
from predict_test18 import level
from predict_test29 import spf
from predict_test32 import ANIMALS, ends520, ends740, pic
from predict_test33 import label_head
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
END = ('740', '520')
MO_ANIMAL = {'Bull1', 'Gavi', 'Bult', 'Gaur', 'Fish', 'Zebu', 'Bull', 'Goat', 'Rhin', 'Bull2'}
random.seed(54)


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
    rows = [r for r in load() if r['flat']]
    cat = cat_of()
    head, _ = classes(T.sample('A'))
    good = lambda r: pic(r) and pic(r) not in ('Othr', 'Unknown')
    cu = [r for r in rows if r['type'] == 'TAB:C' and good(r)]
    mo = [r for r in rows if r['type'] == 'TAB:B' and good(r)]
    labels = cu + mo
    sealsA = [r for r in rows if r['type'].startswith('SEAL')]
    snames = [name_of(t) for r in sealsA for t in r['seq'] if name_of(t)]
    stok = Counter(g for r in sealsA for g in r['flat'])
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    def show(k, title, lo):
        say('## %s %s' % (k, title))
        say('- %s.' % lo[0])
        rec_(k, lo[1])

    def thr(k, title, num, den, t, above=True):
        say('## %s %s' % (k, title))
        say('- %d of %d (%.0f%%); threshold %s %.0f%%.' % (num, den, 100 * num / max(1, den), 'at least' if above else 'at most', 100 * t))
        rec_(k, den > 0 and ((num / den >= t) if above else (num / den <= t)))

    say('# Thirty-fourth registered predictions: labels against names, and the labels\' dates')
    say()
    ch = {label_head(r['flat']) for r in cu} - {None}
    mh = {label_head(r['flat']) for r in mo} - {None}

    def firstlast(hs):
        f = sum(1 for b, _ in snames for i, g in enumerate(b) if g in hs and i == 0 and len(b) >= 2)
        l_ = sum(1 for b, _ in snames for i, g in enumerate(b) if g in hs and i == len(b) - 1 and len(b) >= 2)
        return f, l_
    from predict_test15 import binom_ge
    for k, title, hs in (('LB1', 'copper label heads are attributes in seal names', ch),
                         ('LB2', 'moulded label heads are attributes in seal names', mh)):
        f, l_ = firstlast(hs)
        p = binom_ge(f, f + l_)
        say('## %s %s' % (k, title))
        say('- label heads %d; in seal names first %d, last %d; p = %.4f.' % (len(hs), f, l_, p))
        rec_(k, f > l_ and p < 0.05)

    say('## LB3 copper label heads are rare on seals')
    sh_ = {b[-1] for b, _ in snames}
    pool = sorted(ch | sh_)
    lab = [g in ch for g in pool]
    vals = [stok[g] for g in pool]

    def st(l_):
        a = [v for v, x in zip(vals, l_) if x]
        b = [v for v, x in zip(vals, l_) if not x]
        return sum(b) / len(b) - sum(a) / len(a)
    obs = st(lab)
    ge = 0
    s2 = lab[:]
    for _ in range(N):
        random.shuffle(s2)
        ge += st(s2) >= obs
    p = (ge + 1) / (N + 1)
    say('- copper label heads %d; mean seal count, seal heads minus label heads %+.1f; p = %.4f.' % (len(ch), obs, p))
    rec_('LB3', obs > 0 and p < 0.05)
    say('## LB4 moulded labels are closer to seal names than copper labels are')
    ct = [g for r in cu for g in r['flat']]
    mt = [g for r in mo for g in r['flat']]
    st_ = [g for r in sealsA for g in r['flat']]
    m = len(ct)
    pos = 0
    for _ in range(1000):
        ss = Counter(random.sample(st_, m))
        pos += T.jsd(Counter(random.sample(mt, m)), ss) < T.jsd(Counter(random.choice(ct) for _ in range(m)), ss)
    say('- draws with moulded closer to seals than copper %d of 1000.' % pos)
    rec_('LB4', pos >= 950)
    a = [ends520(nm[0] + (nm[1],)) for nm in snames if set(nm[0]) & ch]
    c = [ends520(nm[0] + (nm[1],)) for nm in snames if not set(nm[0]) & ch]
    show('LB18', 'names with a copper label head are 520 names', gt('520, seal names with a copper label head', sum(a), len(a), sum(c), len(c)))
    a = [ends520(nm[0] + (nm[1],)) for nm in snames if set(nm[0]) & mh]
    c = [ends520(nm[0] + (nm[1],)) for nm in snames if not set(nm[0]) & mh]
    show('LB19', 'names with a moulded label head are 520 names', gt('520, seal names with a moulded label head', sum(a), len(a), sum(c), len(c)))
    a = [spf(r['flat']) for r in labels]
    c = [spf(r['flat']) for r in sealsA]
    show('LB20', 'labels lack the titled fish', lt('stroke pair + fish, labels', sum(a), len(a), sum(c), len(c)))

    a = [ends740(r['flat']) for r in cu]
    c = [ends740(r['flat']) for r in mo]
    show('LB5', 'copper labels end in 740', gt('740, copper labels', sum(a), len(a), sum(c), len(c)))
    a = [ends520(r['flat']) for r in mo if pic(r) == 'Bull1']
    c = [ends520(r['flat']) for r in mo if pic(r) != 'Bull1']
    show('LB11', 'unicorn labels are 520 labels', gt('520, unicorn moulded labels', sum(a), len(a), sum(c), len(c)))
    a = [spf(r['flat']) for r in mo if pic(r) == 'Bull1']
    c = [spf(r['flat']) for r in mo if pic(r) != 'Bull1']
    show('LB12', 'unicorn labels carry the titled fish', gt('stroke pair + fish, unicorn labels', sum(a), len(a), sum(c), len(c)))
    v = [('347' in r['flat']) for r in mo if pic(r) == 'Mult']
    thr('LB13', 'the multi-headed animal is 347', sum(v), len(v), 0.5)
    v = [('318' in r['flat']) for r in mo if pic(r) == 'Gavi']
    thr('LB14', 'the gharial is 318', sum(v), len(v), 0.3)
    a = [ends740(r['flat']) for r in mo if pic(r) == 'Phyt']
    c = [ends740(r['flat']) for r in mo if pic(r) in MO_ANIMAL]
    show('LB15', 'plant labels are not 740 labels', lt('740, plant labels', sum(a), len(a), sum(c), len(c)))
    hu = lambda r: any(cat.get(g) == 'A' for g in r['flat'])
    a = [hu(r) for r in mo if pic(r) == 'Scene']
    c = [hu(r) for r in mo if pic(r) != 'Scene']
    show('LB16', 'scene labels have human signs', gt('human sign, scene labels', sum(a), len(a), sum(c), len(c)))
    a = [ends740(r['flat']) for r in cu if pic(r) == 'Anth']
    c = [ends740(r['flat']) for r in cu if pic(r) in ANIMALS]
    show('LB17', 'the anthropomorph label is a 740 label', gt('740, Anth labels', sum(a), len(a), sum(c), len(c)))
    v = [r['flat'][0] in NUMS for r in cu if any(g in NUMS for g in r['flat'])]
    thr('LB21', 'numbers open copper labels', sum(v), len(v), 0.5)
    v = [r['flat'][0] in NUMS for r in mo if any(g in NUMS for g in r['flat'])]
    thr('LB22', 'numbers open moulded labels', sum(v), len(v), 0.5)
    k = sum(1 for r in labels for t in r['seq'] if name_of(t) and name_of(t)[1] == '520' and len(name_of(t)[0]) >= 2
            and name_of(t)[0][-1] == '33' and name_of(t)[0][-2] in ('705', '706'))
    say('## LB23 the closing formula is not on labels')
    say('- labels with the formula: %d; threshold at most 1.' % k)
    rec_('LB23', k <= 1)
    f400 = sum(any(x in END and y == '400' for x, y in zip(r['flat'], r['flat'][1:])) for r in labels)
    f90 = sum(any(x in END and y == '90' for x, y in zip(r['flat'], r['flat'][1:])) for r in labels)
    thr('LB24', '400 is not on labels', f400, len(labels), 0.02, above=False)
    thr('LB25', '90 is not on labels', f90, len(labels), 0.02, above=False)

    # F
    icit_full.LINES_REVERSED = True
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    objs = [r for r in icit_full.objects(path) if r['flat']]
    fp = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].split(':')[0].strip()
    fgood = lambda r: fp(r) not in ('', 'None', '-', 'Othr', 'Unknown')
    md = lambda r: r['site'].strip() == 'Mohenjo-daro'
    lvm = lambda r: level('Mohenjo-daro', recs[r['sealid']])
    a = [lvm(r) == 'L' for r in objs if md(r) and r['type'] == 'TAB:C' and lvm(r)]
    c = [lvm(r) == 'L' for r in objs if md(r) and r['type'].startswith('SEAL') and lvm(r)]
    show('LB6', 'copper tablets are late', gt('later level, Mohenjo-daro copper tablets', sum(a), len(a), sum(c), len(c)))
    lvh = lambda r: level('Harappa', recs[r['sealid']])
    hm = [r for r in objs if r['site'].strip() == 'Harappa' and r['type'] == 'TAB:B' and fgood(r) and lvh(r)]
    say('## LB7 the moulded pictures change over time')
    xs, ys = [lvh(r) for r in hm], [fp(r) for r in hm]
    obs = T.mi(xs, ys)
    ge = 0
    x2 = xs[:]
    for _ in range(N):
        random.shuffle(x2)
        ge += T.mi(x2, ys) >= obs
    p = (ge + 1) / (N + 1)
    say('- Harappa pictured moulded tablets with a level %d; MI %.4f; p = %.4f.' % (len(hm), obs, p))
    rec_('LB7', p < 0.05)

    def same_level(items):
        prs = [(i, j) for i, j in combinations(range(len(items)), 2) if items[i][0] == items[j][0]]
        lv = [l_ for _, l_ in items]
        obs = sum(lv[i] == lv[j] for i, j in prs) / max(1, len(prs))
        ge = 0
        for _ in range(N):
            random.shuffle(lv)
            ge += sum(lv[i] == lv[j] for i, j in prs) / max(1, len(prs)) >= obs
        return len(prs), obs, (ge + 1) / (N + 1)
    cm = [(fp(r), lvm(r)) for r in objs if md(r) and r['type'] == 'TAB:C' and fgood(r) and lvm(r)]
    n_, o, p = same_level(cm)
    say('## LB8 same-picture copper tablets share a level')
    say('- pairs %d; same level %.0f%%; p = %.4f.' % (n_, 100 * o, p))
    rec_('LB8', n_ > 0 and p < 0.05)
    n_, o, p = same_level([(fp(r), lvh(r)) for r in hm])
    say('## LB9 same-picture moulded tablets share a level')
    say('- pairs %d; same level %.0f%%; p = %.4f.' % (n_, 100 * o, p))
    rec_('LB9', n_ > 0 and p < 0.05)
    say('## LB10 same-text pictured tablets lie together')
    pd = [(tuple(r['flat']), r['depth']) for r in objs if r['type'] == 'TAB:B' and fgood(r) and r['depth'] is not None]
    allp = list(combinations(range(len(pd)), 2))
    same = [(i, j) for i, j in allp if pd[i][0] == pd[j][0]]
    if same:
        dd = lambda ps: statistics.median(abs(pd[i][1] - pd[j][1]) for i, j in ps)
        obs = dd(same)
        ge = sum(dd(random.sample(allp, len(same))) <= obs for _ in range(N // 10))
        p = (ge + 1) / (N // 10 + 1)
        say('- pictured moulded tablets with a depth %d; same-text pairs %d; median %.2f; p = %.4f (1,000 draws).' % (
            len(pd), len(same), obs, p))
        rec_('LB10', p < 0.05)
    else:
        say('- no same-text pairs with depths.')
        rec_('LB10', False)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test34.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
