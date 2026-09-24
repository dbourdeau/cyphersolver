"""Test of the thirty-first registered prediction set (PREDICTIONS.md, I1-I25).

Usage: python predict_test31.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test31.md. The fuller corpus is read with lines reversed.
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
from predict_test7 import fisher_less
from predict_test14 import classes, hyper_ge
from predict_test15 import strat_perm
from predict_test17 import headed
from predict_test18 import level, lstrat, n700
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
END = ('740', '520')
random.seed(51)


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
    head, attr = classes(A)
    icit_full.LINES_REVERSED = True
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    names_in = lambda r: [name_of(ln) for ln in r['seq'] if name_of(ln)]
    w400 = lambda r: any(x in END and y == '400' for ln in r['seq'] for x, y in zip(ln, ln[1:]))
    rcp = [r for r in intact if r['type'] == 'TAB:I' and names_in(r) and w400(r)]
    mnt = [r for r in intact if r['type'] == 'TAB:B' and names_in(r)]
    seals = [r for r in intact if r['type'].startswith('SEAL')]
    tabs = [r for r in intact if r['type'].startswith('TAB')]
    mot = lambda r: ('' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip())
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

    def strat(k, title, items):
        o, p = strat_perm(items)
        say('## %s %s' % (k, title))
        say('- labelled %d of %d; stratified difference %+.1f points; p = %.4f.' % (
            sum(l_ for l_, _, _ in items), len(items), 100 * o, p))
        rec_(k, o > 0 and p < 0.05)

    say('# Thirty-first registered predictions: labels, moulded names, idioms, the heading')
    say()

    # copper tablets (A)
    cu = [r for r in rowsA if r['type'] == 'TAB:C']
    sealsA = [r for r in rowsA if r['type'].startswith('SEAL')]
    say('## I1 copper labels are names')
    bodies = {name_of(t)[0] for r in sealsA for t in r['seq'] if name_of(t)}
    ct = [tuple(t) for r in cu for t in r['seq'] if len(t) >= 2 and '?' not in t]
    obs = sum(t in bodies for t in ct)
    ge = 0
    for _ in range(N):
        k = 0
        for t in ct:
            s_ = list(t)
            random.shuffle(s_)
            k += tuple(s_) in bodies
        ge += k >= obs
    p = (ge + 1) / (N + 1)
    say('- copper lines %d; equal to a seal name body %d; p = %.4f.' % (len(ct), obs, p))
    rec_('I1', p < 0.05)
    strat('I2', 'copper labels avoid fish', [(r['type'].startswith('SEAL'), lstrat(len(t)), 1 if any(g in FISH for g in t) else 0)
                                             for r in cu + sealsA for t in r['seq'] if len(t) >= 2 and '?' not in t])
    say('## I3 one label, one picture')
    cm = [(tuple(r['flat']), r['motif'].strip()) for r in cu if r['motif'].strip()]
    prs = [(i, j) for i, j in combinations(range(len(cm)), 2) if cm[i][0] == cm[j][0]]
    ms = [m for _, m in cm]
    obs = sum(ms[i] == ms[j] for i, j in prs) / max(1, len(prs))
    ge = 0
    for _ in range(N):
        random.shuffle(ms)
        ge += sum(ms[i] == ms[j] for i, j in prs) / max(1, len(prs)) >= obs
    p = (ge + 1) / (N + 1)
    say('- copper tablets with a motif %d; same-text pairs %d; same motif %.0f%%; p = %.4f.' % (len(cm), len(prs), 100 * obs, p))
    rec_('I3', len(prs) > 0 and p < 0.05)
    say('## I4 copper labels open differently')
    x1 = [t[0] for r in cu for t in r['seq'] if t and '?' not in t]
    x2 = [t[0] for r in sealsA for t in r['seq'] if t and '?' not in t]
    o, p = mi_perm(['c'] * len(x1) + ['s'] * len(x2), x1 + x2)
    say('- MI %.4f; p = %.4f.' % (o, p))
    rec_('I4', p < 0.05)

    # other-animal seals (F)
    sn = [(r, names_in(r)[0]) for r in seals if names_in(r) and mot(r) and mot(r) not in ('-', 'None')]
    oth = [(mot(r).split(':')[0], e) for r, (b, e) in sn if not mot(r).startswith('Bull1')]
    say('## I5 the animal decides the ending')
    o, p = mi_perm([a for a, _ in oth], [e for _, e in oth])
    say('- %s; MI %.4f; p = %.4f.' % (dict(Counter(a for a, _ in oth).most_common(6)), o, p))
    rec_('I5', p < 0.05)
    say('## I6 other animals are later')
    ok = True
    for site in ('Mohenjo-daro', 'Harappa'):
        ss = [r for r in seals if r['site'].strip() == site and mot(r) and mot(r) not in ('-', 'None') and level(site, recs[r['sealid']])]
        a = [not mot(r).startswith('Bull1') for r in ss if level(site, recs[r['sealid']]) == 'L']
        c = [not mot(r).startswith('Bull1') for r in ss if level(site, recs[r['sealid']]) == 'E']
        line, good = gt('%s other animals, later' % site, sum(a), len(a), sum(c), len(c))
        ok = ok and good
        say('- %s.' % line)
    rec_('I6', ok)
    a = [b[-1] in head for r, (b, e) in sn if not mot(r).startswith('Bull1')]
    c = [b[-1] in head for r, (b, e) in sn if mot(r).startswith('Bull1')]
    show('I7', 'other-animal names lack heads', lt('head-final, other-animal seals', sum(a), len(a), sum(c), len(c)))

    # moulded name tablets
    ends = lambda objs: [e == '520' for r in objs for b, e in names_in(r)[:1]]
    a, c = ends(mnt), ends(rcp)
    show('I8', 'moulded names are 520 names', gt('520, moulded name tablets', sum(a), len(a), sum(c), len(c)))
    hd = lambda objs: [any(headed(ln) for ln in r['seq']) for r in objs]
    a, c = hd(mnt), hd(rcp)
    show('I9', 'moulded names carry the heading', gt('heading, moulded name tablets', sum(a), len(a), sum(c), len(c)))
    rec_n = lambda objs: [n_ >= 2 for n_ in Counter(tuple(r['flat']) for r in objs).values()]
    a, c = rec_n(mnt), rec_n(rcp)
    show('I10', 'moulded names recur', gt('distinct moulded name texts on 2+', sum(a), len(a), sum(c), len(c)))
    a = [any(g in FISH for g in b) for r in mnt for b, _ in names_in(r)[:1]]
    c = [any(g in FISH for g in b) for r in seals for b, _ in names_in(r)[:1]]
    show('I11', 'moulded names are fish names', gt('fish in the name, moulded name tablets', sum(a), len(a), sum(c), len(c)))
    lv = lambda r: level('Harappa', recs[r['sealid']])
    a = [lv(r) == 'L' for r in mnt if r['site'].strip() == 'Harappa' and lv(r)]
    c = [lv(r) == 'L' for r in rcp if r['site'].strip() == 'Harappa' and lv(r)]
    show('I12', 'moulded names are later', gt('later level, moulded name tablets', sum(a), len(a), sum(c), len(c)))
    lr = lambda r: r['direction'] == 'L/R'
    a = [lr(r) for r in rowsA if r['type'] == 'TAB:B' and any(name_of(t) for t in r['seq'])]
    c = [lr(r) for r in sealsA]
    show('I23', 'moulded names run left to right', gt('left-to-right, moulded name tablets', sum(a), len(a), sum(c), len(c)))

    # receipts
    a = [any(g in NUMS for g in b) for r in rcp for b, _ in names_in(r)[:1]]
    c = [any(g in NUMS for g in b) for r in seals for b, _ in names_in(r)[:1]]
    show('I13', 'receipt names hold a numeral', gt('numeral in the name, receipts', sum(a), len(a), sum(c), len(c)))
    a = [any(g in FISH for g in b) for r in rcp for b, _ in names_in(r)[:1]]
    c = [any(g in FISH for g in b) for r in seals for b, _ in names_in(r)[:1]]
    show('I14', 'receipt names avoid fish', lt('fish in the name, receipts', sum(a), len(a), sum(c), len(c)))

    # idioms
    nm = T.names(AB)
    ns_ = lambda x, y: x in NUMS and y not in NUMS
    a = [ns_(*b) for b, _ in nm if len(b) == 2]
    c = [ns_(x, y) for b, _ in nm if len(b) >= 3 for x, y in zip(b, b[1:])]
    show('I15', 'a numeral idiom is a whole name', gt('numeral + sign, two-sign names', sum(a), len(a), sum(c), len(c)))
    a = [i + 1 == len(b) - 1 for b, _ in nm for i in range(len(b) - 1) if ns_(b[i], b[i + 1])]
    c = [i + 1 == len(b) - 1 for b, _ in nm for i in range(len(b) - 1) if not ns_(b[i], b[i + 1])]
    show('I16', 'the idiom closes the name', gt('idiom sign last in the name', sum(a), len(a), sum(c), len(c)))
    say('## I17 fish numbers differ by site')
    it = [(r['site'].strip(), NUMS[x][0]) for r in seals if r['site'].strip() in ('Mohenjo-daro', 'Harappa')
          for ln in r['seq'] for x, y in zip(ln, ln[1:]) if x in NUMS and y in FISH]
    o, p = mi_perm([a for a, _ in it], [b for _, b in it])
    say('- pairs %d; MI %.4f; p = %.4f.' % (len(it), o, p))
    rec_('I17', p < 0.05)

    # heading
    say('## I18 the heading does not change the ending')
    hdd, und = defaultdict(Counter), defaultdict(Counter)
    for t in AB:
        x = name_of(t)
        if x:
            (hdd if headed(t) else und)[x[0][-1]][x[1]] += 1
    hs = [h for h in hdd if sum(hdd[h].values()) >= 5 and sum(und[h].values()) >= 5]
    agree = [h for h in hs if hdd[h].most_common(1)[0][0] == und[h].most_common(1)[0][0]]
    say('- heads %d; same majority ending %d (%.0f%%); threshold 80%%.' % (len(hs), len(agree), 100 * len(agree) / max(1, len(hs))))
    rec_('I18', hs and len(agree) / len(hs) >= 0.8)
    say('## I19 the opener depends on the site')
    it = [(r['site'].strip() if r['site'].strip() in ('Mohenjo-daro', 'Harappa') else 'other', ln[0]) for r in seals
          for ln in r['seq'] if headed(ln)]
    o, p = mi_perm([a for a, _ in it], [b for _, b in it])
    say('- headed seal lines %d; MI %.4f; p = %.4f.' % (len(it), o, p))
    rec_('I19', p < 0.05)
    a = [t[-1] == '90' for t in AB if len(t) >= 3 and headed(t) and (t[-1] == '740' or (t[-2] == '740' and t[-1] == '90'))]
    c = [t[-1] == '90' for t in AB if len(t) >= 2 and not headed(t) and (t[-1] == '740' or (len(t) >= 2 and t[-2] == '740' and t[-1] == '90'))]
    show('I20', 'titled names take the man sign', gt('90 after 740, headed names', sum(a), len(a), sum(c), len(c)))
    sh_ = [(r['site'].strip(), ln[0]) for r in seals for ln in r['seq'] if headed(ln)]
    a = [s_ == 'Mohenjo-daro' for s_, o_ in sh_ if o_ == '861']
    c = [s_ == 'Mohenjo-daro' for s_, o_ in sh_ if o_ == '817']
    show('I21', '861 is a Mohenjo-daro opener', gt('Mohenjo-daro, 861-headed', sum(a), len(a), sum(c), len(c)))
    strat('I25', 'Kalibangan seals lack the heading',
          [(r['site'].strip() == 'Mohenjo-daro', lstrat(len(ln)), 1 if headed(ln) else 0) for r in seals
           if r['site'].strip() in ('Mohenjo-daro', 'Kalibangan') for ln in r['seq'] if len(ln) >= 3])

    # tokens, pots
    val = {'32': 2, '33': 3, '34': 4}
    tv = [(r['type'], next(val[x] for ln in r['seq'] for x, y in zip(ln, ln[1:]) if y == '700' and x in val)) for r in tabs
          if r['type'] in ('TAB:B', 'TAB:I') and any(y == '700' and x in val for ln in r['seq'] for x, y in zip(ln, ln[1:]))]
    a = [v == 4 for t_, v in tv if t_ == 'TAB:I']
    c = [v == 4 for t_, v in tv if t_ == 'TAB:B']
    show('I22', 'incised tokens count four', gt('value 4, incised tokens', sum(a), len(a), sum(c), len(c)))
    a = [r['site'].strip() == 'Harappa' for r in intact if r['type'].startswith('POT') and names_in(r)]
    c = [r['site'].strip() == 'Harappa' for r in seals if names_in(r)]
    show('I24', 'pot names are from Harappa', gt('Harappa, pots with a name', sum(a), len(a), sum(c), len(c)))

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test31.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
