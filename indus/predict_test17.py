"""Test of the seventeenth registered prediction set (PREDICTIONS.md, U1-U25).

Usage: python predict_test17.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test17.md.
"""
import math
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
from predict_test16 import m_break
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
OPEN = ('817', '820', '861')
END = ('740', '520')
POST = ('90', '400', '151')
random.seed(37)


def say(s=''):
    OUT.append(s)
    print(s)


def headed(t):
    return len(t) >= 3 and t[0] in OPEN and t[1] in ('2', '60', '1')


def obj_perm(objs, lab, stat):
    """Permute a boolean label among objects; one-sided p for stat >= observed."""
    obs = stat(lab)
    ge = 0
    sh = lab[:]
    for _ in range(N):
        random.shuffle(sh)
        ge += stat(sh) >= obs
    return obs, (ge + 1) / (N + 1)


def rank_diff(a, b):
    r = T.ranks(a + b)
    return sum(r[:len(a)]) / len(a) - sum(r[len(a):]) / len(b)


def rank_perm(a, b):
    obs = rank_diff(a, b)
    allv = a + b
    ge = 0
    for _ in range(N):
        random.shuffle(allv)
        ge += rank_diff(allv[:len(a)], allv[len(a):]) >= obs
    return obs, (ge + 1) / (N + 1)


def main(path):
    A, B = T.sample('A'), T.sample('B')
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

    say('# Seventeenth registered predictions: twenty-five hypotheses on the surviving leads')
    say()

    # U1
    say('## U1 tablet numerals are larger')
    objs = [r for r in intact if kind(r) in ('TAB', 'SEAL') and any(g in NUMS for g in r['flat'])]
    vals = [[NUMS[g][0] for g in r['flat'] if g in NUMS] for r in objs]
    lab = [kind(r) == 'TAB' for r in objs]

    def st1(lb):
        a = [v for vs, l in zip(vals, lb) if l for v in vs]
        b = [v for vs, l in zip(vals, lb) if not l for v in vs]
        return sum(a) / len(a) - sum(b) / len(b)
    o, p = obj_perm(objs, lab, st1)
    say('- objects with a numeral: %d tablets, %d seals; mean value difference (tablets minus seals) %+.2f; p = %.4f.' % (
        sum(lab), len(lab) - sum(lab), o, p))
    rec_('U1', o > 0 and p < 0.05)

    # U2
    say('## U2 tablet numerals stand at the edge')
    items = [(kind(r) == 'TAB', 0 if len(r['flat']) <= 3 else (1 if len(r['flat']) <= 5 else 2),
              1 if r['flat'][0] in NUMS or r['flat'][-1] in NUMS else 0) for r in objs if len(r['flat']) >= 2]
    o, p = strat_perm(items)
    say('- stratified difference (tablets minus seals) in numeral-at-edge %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('U2', o > 0 and p < 0.05)

    # U3
    say('## U3 the sign after a numeral comes from a smaller set on tablets')
    post = [Counter(y for ln in r['seq'] for x, y in zip(ln, ln[1:]) if x in NUMS and y not in NUMS) for r in objs]

    def st3(lb):
        a, b = Counter(), Counter()
        for c, l in zip(post, lb):
            (a if l else b).update(c)
        return T.entropy(b) - T.entropy(a)
    o, p = obj_perm(objs, lab, st3)
    say('- entropy of the sign after a numeral, seals minus tablets %+.2f bits; p = %.4f.' % (o, p))
    rec_('U3', o > 0 and p < 0.05)

    # U4
    say('## U4 incised tablets carry numerals more than moulded')
    tabs = [r for r in intact if r['type'] in ('TAB:I', 'TAB:B')]
    items = [(r['type'] == 'TAB:I', min(len(r['flat']), 5), 1 if any(g in NUMS for g in r['flat']) else 0) for r in tabs]
    o, p = strat_perm(items)
    a = [x for l, _, x in items if l]
    b = [x for l, _, x in items if not l]
    say('- incised with a numeral %d of %d, moulded %d of %d; stratified difference %+.1f points; p = %.4f.' % (
        sum(a), len(a), sum(b), len(b), 100 * o, p))
    rec_('U4', o > 0 and p < 0.05)

    # U5
    say('## U5 400 after the ending off the seals')
    items = []
    for r in intact:
        k = kind(r)
        if k not in ('SEAL', 'TAB', 'TAG', 'POT'):
            continue
        for ln in r['seq']:
            for x, y in zip(ln, ln[1:]):
                if x in END and y in POST:
                    items.append((k != 'SEAL', 0, 1 if y == '400' else 0))
    o, p = strat_perm(items)
    a = [x for l, _, x in items if l]
    b = [x for l, _, x in items if not l]
    say('- 400 among post-ending signs: off seals %d of %d, seals %d of %d; difference %+.1f points; p = %.4f.' % (
        sum(a), len(a), sum(b), len(b), 100 * o, p))
    rec_('U5', o > 0 and p < 0.05)

    # U6, U7
    for key, title in (('U6', '33-520 ends its text'), ('U7', 'a head stands before 33-520')):
        say('## %s %s' % (key, title))
        ok = True
        for lab_, L in (('A', A), ('B', B)):
            a = na = c = nc = 0
            for t in L:
                for i, g in enumerate(t):
                    if g != '520':
                        continue
                    is33 = i >= 1 and t[i - 1] == '33'
                    if key == 'U6':
                        out = i == len(t) - 1 or (i == len(t) - 2 and t[-1] in POST)
                    else:
                        j = i - 2 if is33 else i - 1
                        if j < 0:
                            continue
                        out = t[j] in head
                    if is33:
                        a += out
                        na += 1
                    else:
                        c += out
                        nc += 1
            p = hyper_ge(a, na - a, c, nc - c)
            good = p < 0.05 and a / max(1, na) > c / max(1, nc)
            ok = ok and good
            say('- %s: 33-520 %d of %d (%.0f%%), other 520 %d of %d (%.0f%%); p = %.4f.' % (
                lab_, a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p))
        rec_(key, ok)

    # U8
    say('## U8 names closing in 33-520 also take 740')
    ns = T.names(A) + T.names(B)
    v740 = {b for b, e in ns if e == '740'}
    s33 = {b[:-1] for b, e in ns if e == '520' and len(b) >= 2 and b[-1] == '33'}
    plain = {b for b, e in ns if e == '520' and b[-1] != '33'}
    a, na = sum(x in v740 for x in s33), len(s33)
    c, nc = sum(x in v740 for x in plain), len(plain)
    p = hyper_ge(a, na - a, c, nc - c)
    say('- stems before 33-520 also found with 740: %d of %d (%.0f%%); plain 520 bodies %d of %d (%.0f%%); p = %.4f.' % (
        a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p))
    rec_('U8', p < 0.05 and a / max(1, na) > c / max(1, nc))

    # U9
    say('## U9 33-520 off the seals')
    a = na = c = nc = 0
    for r in intact:
        k = kind(r)
        if k not in ('SEAL', 'TAB', 'TAG'):
            continue
        for ln in r['seq']:
            nm = name_of(ln)
            if nm and nm[1] == '520':
                is33 = nm[0][-1] == '33'
                if k == 'SEAL':
                    c += is33
                    nc += 1
                else:
                    a += is33
                    na += 1
    p = hyper_ge(a, na - a, c, nc - c)
    say('- lines ending 520 that end 33-520: tablets + sealings %d of %d (%.0f%%), seals %d of %d (%.0f%%); p = %.4f.' % (
        a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p))
    rec_('U9', p < 0.05 and a / max(1, na) > c / max(1, nc))

    # U10
    say('## U10 33-520 is not split by a line break')
    m77 = [r['seq'] for r in load(only_m77=True) if len(r['seq']) >= 2 and not any('?' in ln for ln in r['seq'])]
    ok = True
    for lab_, texts in (('as listed', m77), ('reversed', [t[::-1] for t in m77])):
        a, na, c, nc = m_break(texts, lambda t: {g for g in range(1, len(t)) if t[g - 1] == '33' and t[g] == '520'})
        p = fisher_less(a, na - a, c, nc - c)
        ok = ok and p < 0.05 and a / max(1, na) < c / nc
        say('- lines %s: 33 | 520 broken %d of %d, other gaps %d of %d (%.1f%%); p = %.4f.' % (
            lab_, a, na, c, nc, 100 * c / nc, p))
    rec_('U10', ok)

    # U11
    say('## U11 heads are steadier than attributes across space')
    sp = []
    for r in intact:
        if kind(r) != 'SEAL' or r['site'].strip() not in ('Mohenjo-daro', 'Harappa'):
            continue
        for ln in r['seq']:
            nm = name_of(ln)
            if nm and len(nm[0]) >= 2:
                sp.append((nm[0][0], nm[0][-1], r['site'].strip()))

    def d11(labs):
        f1 = Counter(f for (f, _, _), l in zip(sp, labs) if l == 'Mohenjo-daro')
        f2 = Counter(f for (f, _, _), l in zip(sp, labs) if l != 'Mohenjo-daro')
        h1 = Counter(h for (_, h, _), l in zip(sp, labs) if l == 'Mohenjo-daro')
        h2 = Counter(h for (_, h, _), l in zip(sp, labs) if l != 'Mohenjo-daro')
        return T.jsd(f1, f2) - T.jsd(h1, h2)
    labs = [s for _, _, s in sp]
    obs = d11(labs)
    ge = 0
    sh = labs[:]
    for _ in range(N):
        random.shuffle(sh)
        ge += d11(sh) >= obs
    p = (ge + 1) / (N + 1)
    say('- seal names: %d (Mohenjo-daro %d, Harappa %d); JSD first minus last %+.3f; p = %.4f.' % (
        len(sp), labs.count('Mohenjo-daro'), labs.count('Harappa'), obs, p))
    rec_('U11', obs > 0 and p < 0.05)

    # U12
    say('## U12 heads select their attributes')
    ok = True
    for lab_, L in (('A', A), ('B', B)):
        nn = [b for b, _ in T.names(L) if len(b) >= 2]
        X, Y = [b[0] for b in nn], [b[-1] for b in nn]
        obs = T.mi(X, Y)
        ge = 0
        yy = Y[:]
        for _ in range(N):
            random.shuffle(yy)
            ge += T.mi(X, yy) >= obs
        p = (ge + 1) / (N + 1)
        ok = ok and p < 0.05
        say('- %s: %d names; MI(first; last) %.3f bits; p = %.4f.' % (lab_, len(nn), obs, p))
    rec_('U12', ok)

    # U13
    say('## U13 slot 2 is steadier than slot 1 over time')
    per = []
    for r in intact:
        site = r['site'].strip()
        rc = recs[r['sealid']]
        g = None
        if site == 'Mohenjo-daro':
            pr = rc[9].strip()
            g = 'E' if pr.startswith(('Early', 'Interm')) else ('L' if pr.startswith('Late') else None)
        elif site == 'Harappa':
            f10 = rc[10].strip()
            if rc[9].strip() == '3' and f10 in ('B', 'C'):
                g = 'E' if f10 == 'B' else 'L'
            elif f10 in ('Stratum IV', 'Stratum V', 'Stratum VI', 'Stratum VII'):
                g = 'E'
            elif f10 in ('Stratum I', 'Stratum II', 'Stratum III'):
                g = 'L'
        if not g:
            continue
        for ln in r['seq']:
            nm = name_of(ln)
            if nm and len(nm[0]) >= 3:
                per.append((nm[0][0], nm[0][-2], site, g))

    def d13(labs):
        s1e = Counter(a for (a, _, _, _), l in zip(per, labs) if l == 'E')
        s1l = Counter(a for (a, _, _, _), l in zip(per, labs) if l == 'L')
        s2e = Counter(b for (_, b, _, _), l in zip(per, labs) if l == 'E')
        s2l = Counter(b for (_, b, _, _), l in zip(per, labs) if l == 'L')
        return T.jsd(s1e, s1l) - T.jsd(s2e, s2l)
    labs = [g for _, _, _, g in per]
    obs = d13(labs)
    bys = defaultdict(list)
    for i, (_, _, s, _) in enumerate(per):
        bys[s].append(i)
    ge = 0
    for _ in range(N):
        sh = labs[:]
        for ii in bys.values():
            v = [sh[i] for i in ii]
            random.shuffle(v)
            for i, w in zip(ii, v):
                sh[i] = w
        ge += d13(sh) >= obs
    p = (ge + 1) / (N + 1)
    say('- names of 3+ signs with a level: %d; JSD slot 1 minus slot 2 %+.3f; p = %.4f.' % (len(per), obs, p))
    rec_('U13', obs > 0 and p < 0.05)

    # U14
    say('## U14 human signs stand last')
    ok = True
    for lab_, L in (('A', A), ('B', B)):
        hl = hf = ol = of = 0
        for b, _ in T.names(L):
            if len(b) < 2:
                continue
            for g, w in ((b[0], 'f'), (b[-1], 'l')):
                if g not in cat:
                    continue
                if cat[g] == 'A':
                    hl += w == 'l'
                    hf += w == 'f'
                else:
                    ol += w == 'l'
                    of += w == 'f'
        p = hyper_ge(hl, hf, ol, of)
        ok = ok and p < 0.05 and hl / max(1, hl + hf) > ol / max(1, ol + of)
        say('- %s: human signs last %d of %d (%.0f%%), other categorised %d of %d (%.0f%%); p = %.4f.' % (
            lab_, hl, hl + hf, 100 * hl / max(1, hl + hf), ol, ol + of, 100 * ol / max(1, ol + of), p))
    rec_('U14', ok)

    # U15
    say('## U15 the ending is predictable from the head across transcriptions')
    byh = defaultdict(Counter)
    for b, e in T.names(A):
        byh[b[-1]][e] += 1
    rule = {h: c.most_common(1)[0][0] for h, c in byh.items() if sum(c.values()) >= 3}
    test = [(b[-1], e) for b, e in T.names(B) if b[-1] in rule]
    k = sum(rule[h] == e for h, e in test)
    base = max(Counter(e for _, e in test).values()) / len(test)
    p = sum(math.comb(len(test), i) * base ** i * (1 - base) ** (len(test) - i) for i in range(k, len(test) + 1))
    acc = k / len(test)
    say('- B names with a head seen 3+ times in A: %d; rule accuracy %.1f%%; majority baseline %.1f%%; p = %.2g.' % (
        len(test), 100 * acc, 100 * base, p))
    rec_('U15', acc >= 0.9 and p < 0.05)

    # U16, U17, U18
    say('## U16 headed names are longer')
    ok = True
    for lab_, L in (('A', A), ('B', B)):
        hd, nh = [], []
        for t in L:
            nm = name_of(t)
            if nm:
                (hd if headed(t) else nh).append(len(nm[0]))
        o, p = rank_perm(hd, nh)
        ok = ok and o > 0 and p < 0.05
        say('- %s: headed mean %.2f signs (%d), headless %.2f (%d); rank difference %+.1f; p = %.4f.' % (
            lab_, sum(hd) / len(hd), len(hd), sum(nh) / len(nh), len(nh), o, p))
    rec_('U16', ok)

    say('## U17 headed names use other heads')
    ok = True
    for lab_, L in (('A', A), ('B', B)):
        it = [(headed(t), name_of(t)[0][-1]) for t in L if name_of(t)]
        hs = [h for _, h in it]
        lb = [x for x, _ in it]

        def d17(lbl):
            return T.jsd(Counter(h for h, l in zip(hs, lbl) if l), Counter(h for h, l in zip(hs, lbl) if not l))
        o, p = obj_perm(it, lb, d17)
        ok = ok and p < 0.05
        say('- %s: JSD headed against headless heads %.3f; p = %.4f.' % (lab_, o, p))
    rec_('U17', ok)

    say('## U18 each opener selects its heads')
    ok = True
    for lab_, L in (('A', A), ('B', B)):
        it = [(t[0], name_of(t)[0][-1]) for t in L if name_of(t) and headed(t)]
        X, Y = [a for a, _ in it], [b for _, b in it]
        obs = T.mi(X, Y)
        ge = 0
        xx = X[:]
        for _ in range(N):
            random.shuffle(xx)
            ge += T.mi(xx, Y) >= obs
        p = (ge + 1) / (N + 1)
        ok = ok and p < 0.05
        say('- %s: %d headed names; MI(opener; head) %.3f bits; p = %.4f.' % (lab_, len(it), obs, p))
    rec_('U18', ok)

    # U19, U20
    for key, title, other, direction in (('U19', 'the heading on sealings', 'TAG', 'more'),
                                         ('U20', 'no heading on pots', 'POT', 'less')):
        say('## %s %s' % (key, title))
        a = na = c = nc = 0
        for r in intact:
            k = kind(r)
            if k not in ('SEAL', other):
                continue
            for ln in r['seq']:
                if len(ln) < 3:
                    continue
                h = headed(ln)
                if k == other:
                    a += h
                    na += 1
                else:
                    c += h
                    nc += 1
        if direction == 'more':
            p = hyper_ge(a, na - a, c, nc - c)
            good = p < 0.05 and a / max(1, na) > c / nc
        else:
            p = fisher_less(a, na - a, c, nc - c)
            good = p < 0.05 and a / max(1, na) < c / nc
        say('- %s lines with the heading %d of %d (%.1f%%), seals %d of %d (%.1f%%); p = %.4f.' % (
            other, a, na, 100 * a / max(1, na), c, nc, 100 * c / nc, p))
        rec_(key, good)

    # U21, U22
    seals = [r for r in intact if kind(r) == 'SEAL']
    mot = lambda r: ('' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip())
    uni = [r for r in seals if mot(r).startswith('Bull1')]
    oth = [r for r in seals if mot(r) and mot(r) not in ('-', 'None') and not mot(r).startswith('Bull1')]
    say('## U21 unicorn seals carry longer texts')
    o, p = rank_perm([len(r['flat']) for r in uni], [len(r['flat']) for r in oth])
    say('- unicorn %d seals mean %.2f signs; other animals %d mean %.2f; rank difference %+.1f; p = %.4f.' % (
        len(uni), sum(len(r['flat']) for r in uni) / len(uni), len(oth), sum(len(r['flat']) for r in oth) / len(oth), o, p))
    rec_('U21', o > 0 and p < 0.05)
    say('## U22 unicorn seals carry the heading')
    items = [(mot(r).startswith('Bull1'), min(len(r['flat']), 6), 1 if any(headed(ln) for ln in r['seq']) else 0)
             for r in uni + oth if len(r['flat']) >= 3]
    o, p = strat_perm(items)
    say('- stratified difference (unicorn minus other) %+.1f points; p = %.4f.' % (100 * o, p))
    rec_('U22', o > 0 and p < 0.05)

    # U23
    say('## U23 names are longer in later levels')
    ok = True
    for site in ('Mohenjo-daro', 'Harappa'):
        e, l_ = [], []
        for r in intact:
            if r['site'].strip() != site:
                continue
            rc = recs[r['sealid']]
            g = None
            if site == 'Mohenjo-daro':
                pr = rc[9].strip()
                g = 'E' if pr.startswith(('Early', 'Interm')) else ('L' if pr.startswith('Late') else None)
            else:
                f10 = rc[10].strip()
                if rc[9].strip() == '3' and f10 in ('B', 'C'):
                    g = 'E' if f10 == 'B' else 'L'
                elif f10 in ('Stratum IV', 'Stratum V', 'Stratum VI', 'Stratum VII'):
                    g = 'E'
                elif f10 in ('Stratum I', 'Stratum II', 'Stratum III'):
                    g = 'L'
            if not g:
                continue
            for ln in r['seq']:
                nm = name_of(ln)
                if nm:
                    (e if g == 'E' else l_).append(len(nm[0]))
        o, p = rank_perm(l_, e)
        ok = ok and o > 0 and p < 0.05
        say('- %s: later mean %.2f (%d), earlier %.2f (%d); rank difference %+.1f; p = %.4f.' % (
            site, sum(l_) / max(1, len(l_)), len(l_), sum(e) / max(1, len(e)), len(e), o, p))
    rec_('U23', ok)

    # U24
    say('## U24 cylinder seals omit the endings')
    items = []
    for r in intact:
        if r['type'] in ('SEAL:C', 'SEAL:CY', 'SEAL:S'):
            for ln in r['seq']:
                if len(ln) >= 2:
                    items.append((r['type'] != 'SEAL:S', min(len(ln), 5), 0 if name_of(ln) else 1))
    o, p = strat_perm(items)
    a = [x for l, _, x in items if l]
    say('- cylinder seal lines without an ending %d of %d; stratified difference (cylinder minus square) %+.1f points; '
        'p = %.4f.' % (sum(a), len(a), 100 * o, p))
    rec_('U24', o > 0 and p < 0.05)

    # U25
    say('## U25 the post-ending sign depends on the site')
    it = []
    for r in seals:
        s = r['site'].strip()
        s = s if s in ('Mohenjo-daro', 'Harappa') else 'other'
        for ln in r['seq']:
            for x, y in zip(ln, ln[1:]):
                if x in END and y in POST:
                    it.append((s, y))
    X, Y = [a for a, _ in it], [b for _, b in it]
    obs = T.mi(X, Y)
    ge = 0
    xx = X[:]
    for _ in range(N):
        random.shuffle(xx)
        ge += T.mi(xx, Y) >= obs
    p = (ge + 1) / (N + 1)
    tab = Counter(it)
    say('- %d post-ending tokens on seals; %s; MI %.4f bits; p = %.4f.' % (
        len(it), ', '.join('%s %s %d' % (s, y, n) for (s, y), n in sorted(tab.items())), obs, p))
    rec_('U25', p < 0.05)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test17.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
