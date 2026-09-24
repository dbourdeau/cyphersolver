"""Test of the nineteenth registered prediction set (PREDICTIONS.md, X1-X25).

Usage: python predict_test19.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test19.md.
"""
import math
import os
import random
import sys
from collections import Counter, defaultdict

import numpy as np

import icit_full
import predict_test13 as T
from numerals import NUMS
from predict_test4 import name_of
from predict_test14 import cat_of, classes, hyper_ge
from predict_test15 import strat_perm
from predict_test17 import headed
from predict_test18 import level, lstrat, n700
from signs import FISH

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
END = ('740', '520')
POST = ('90', '400', '151')
random.seed(39)


def say(s=''):
    OUT.append(s)
    print(s)


def cosd(a, b):
    num = sum(v * b.get(k, 0) for k, v in a.items())
    den = math.sqrt(sum(v * v for v in a.values()) * sum(v * v for v in b.values()))
    return num / den if den else 0.0


def numeral_like(lines, g):
    tok = Counter(x for t in lines for x in t)
    if tok[g] < 5:
        return None
    R = defaultdict(Counter)
    for t in lines:
        for x, y in zip(t, t[1:] + ['$']):
            R[x][y] += 1
    core = [n for n in NUMS if tok[n] >= 20 and n != g]
    vc = Counter()
    for n in core:
        vc.update(R[n])
    S = [x for x in tok if tok[x] >= 5]
    q = T.quintiles(tok, S)
    pool = [x for x in S if x not in NUMS and x != g and q[x] == q[g]]
    obs = cosd(R[g], vc)
    k = sum(1 for x in pool if cosd(R[x], vc) >= obs)
    return obs, (k + 1) / (len(pool) + 1), len(pool)


def fline(lab, a, na, c, nc, p):
    return '%s %d of %d (%.1f%%) against %d of %d (%.1f%%), p = %.4f' % (
        lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


def main(path):
    A, B = T.sample('A'), T.sample('B')
    AB = A + B
    NM = T.names(AB)
    cat = cat_of()
    head, attr = classes(A)
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    kind = lambda r: r['type'].split(':')[0]
    tabs = [r for r in intact if kind(r) == 'TAB']
    seals = [r for r in intact if kind(r) == 'SEAL']
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    say('# Nineteenth registered predictions: published readings and the formulas')
    say()

    # X1
    say('## X1 700 takes long-stroke numerals')
    c = Counter(NUMS[x][1] for r in tabs for ln in r['seq'] for x, y in zip(ln, ln[1:]) if y == '700' and x in NUMS)
    n = sum(c.values())
    say('- numerals before 700 on tablets: %s; long %.0f%%; threshold 90%%.' % (dict(c), 100 * c['long'] / n))
    rec_('X1', c['long'] / n >= 0.9)

    # X2-X6
    for key, g, who in (('X2', '706', "Fairservis 'hundred'"), ('X3', '32', "against Parpola 'space'"),
                        ('X4', '840', "Fairservis '8' against Parpola 'rings'"), ('X5', '13', "against Parpola 'hearth'"),
                        ('X6', '55', "numeral 12 against Fairservis 'rain'")):
        say('## %s is %s numeral-like (%s)' % (key, g, who))
        ok = True
        for lab, L in (('A', A), ('B', B)):
            r = numeral_like(L, g)
            if r is None:
                say('- %s: under 5 tokens; not testable.' % lab)
                ok = False
                continue
            o, p, npool = r
            ok = ok and p < 0.05
            say('- %s: cosine with the numerals %.3f; rank p among %d matched non-numerals = %.4f.' % (lab, o, npool, p))
        rec_(key, ok)

    # X7
    say('## X7 400 after person names')
    c740, c520 = Counter(), Counter()
    for t in AB:
        for x, y in zip(t, t[1:]):
            if x == '740' and y in POST:
                c740[y] += 1
            elif x == '520' and y in POST:
                c520[y] += 1
    a, na, cc, nc = c740['400'], sum(c740.values()), c520['400'], sum(c520.values())
    p = hyper_ge(a, na - a, cc, nc - cc)
    say('- %s.' % fline('400 among post-ending signs after 740', a, na, cc, nc, p))
    rec_('X7', p < 0.05 and a / max(1, na) > cc / max(1, nc))

    # X8-X10
    hum = [e for b, e in NM if cat.get(b[-1]) == 'A']
    say('## X8 human heads do not take 520')
    say('- human-headed names taking 520: %d of %d (%.1f%%); threshold under 2%%.' % (
        hum.count('520'), len(hum), 100 * hum.count('520') / len(hum)))
    rec_('X8', hum.count('520') / len(hum) < 0.02)
    fish = [e for b, e in NM if b[-1] in FISH]
    say('## X9 fish heads take 520')
    say('- fish-headed names taking 520: %d of %d (%.1f%%); threshold 90%%.' % (
        fish.count('520'), len(fish), 100 * fish.count('520') / len(fish)))
    rec_('X9', fish.count('520') / len(fish) >= 0.9)
    say('## X10 the ending is fixed by the head')
    byh = defaultdict(Counter)
    for b, e in NM:
        byh[b[-1]][e] += 1
    hs = [(h, c) for h, c in byh.items() if sum(c.values()) >= 5]
    fixed = [h for h, c in hs if max(c.values()) / sum(c.values()) >= 0.9]
    mixed = sorted(((h, dict(c)) for h, c in hs if h not in fixed), key=lambda x: -sum(x[1].values()))
    say('- heads with 5+ names: %d; with one ending in 90%%+ of names: %d (%.0f%%); threshold 80%%. Mixed: %s.' % (
        len(hs), len(fixed), 100 * len(fixed) / len(hs), '; '.join('%s %s' % x for x in mixed[:10])))
    rec_('X10', len(fixed) / len(hs) >= 0.8)

    # X11
    say('## X11 740 is followed by what is possessed')
    k = n = 0
    for t in AB:
        for i, g in enumerate(t):
            if g == '740':
                n += 1
                k += i < len(t) - 1 and t[i + 1] not in POST
    say('- 740 followed by further name material: %d of %d (%.1f%%); threshold 20%%.' % (k, n, 100 * k / n))
    rec_('X11', k / n >= 0.2)

    # X12
    say("## X12 '740 + 90' lines carry the heading")
    items = []
    for t in AB:
        if len(t) >= 3 and t[-2] == '740' and t[-1] == '90':
            items.append((True, lstrat(len(t)), 1 if headed(t) else 0))
        elif len(t) >= 2 and t[-1] == '740':
            items.append((False, lstrat(len(t)), 1 if headed(t) else 0))
    o, p = strat_perm(items)
    say('- 740 + 90 lines %d; stratified difference in headed share %+.1f points; p = %.4f.' % (
        sum(l for l, _, _ in items), 100 * o, p))
    rec_('X12', o > 0 and p < 0.05)

    # X13
    say("## X13 '861 2' as 'in the town'")
    h861 = [t[1] for t in AB if len(t) >= 3 and t[0] == '861' and t[1] in ('2', '60', '1')]
    h817 = [t[1] for t in AB if len(t) >= 3 and t[0] == '817' and t[1] in ('2', '60', '1')]
    a, na, cc, nc = h861.count('2'), len(h861), h817.count('2'), len(h817)
    p = hyper_ge(a, na - a, cc, nc - cc)
    say('- %s.' % fline('2 after the opener 861', a, na, cc, nc, p))
    rec_('X13', p < 0.05 and a / na > cc / nc)

    # X14
    say('## X14 705 and 706 alternate')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        tok = Counter(g for t in L for g in t)
        vec = T.contexts(L)
        S = [g for g in tok if tok[g] >= 10]
        q = T.quintiles(tok, S)
        byq = defaultdict(list)
        for g in S:
            byq[q[g]].append(g)
        if '705' not in q or '706' not in q:
            say('- %s: 705 or 706 under 10 tokens (705 %d, 706 %d); not testable.' % (lab, tok['705'], tok['706']))
            ok = False
            continue
        obs = T.cos(vec.get('705'), vec.get('706'))
        ge = 0
        for _ in range(N):
            while True:
                c1, c2 = random.choice(byq[q['705']]), random.choice(byq[q['706']])
                if c1 != c2 and {c1, c2} != {'705', '706'}:
                    break
            ge += T.cos(vec.get(c1), vec.get(c2)) >= obs
        p = (ge + 1) / (N + 1)
        ok = ok and p < 0.05
        say('- %s: cosine 705 / 706 %.3f; p = %.4f.' % (lab, obs, p))
    rec_('X14', ok)

    # X15
    say('## X15 a name stands before the closing formula')
    bodies = {b for b, _ in NM}
    a = na = cc = nc = 0
    for t in AB:
        nm = name_of(t)
        if not nm or nm[1] != '520':
            continue
        b = nm[0]
        if len(b) >= 3 and b[-1] == '33' and b[-2] in ('705', '706'):
            na += 1
            a += b[:-2] in bodies
        elif len(b) >= 2 and b[-1] != '33':
            nc += 1
            cc += b[:-1] in bodies
    p = hyper_ge(a, na - a, cc, nc - cc)
    say('- %s.' % fline('text before the formula an attested name body', a, na, cc, nc, p))
    rec_('X15', p < 0.05 and a / max(1, na) > cc / max(1, nc))

    # X16
    say('## X16 tiered numerals before fish')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        tf = tn = sf = sn = 0
        for t in L:
            for x, y in zip(t, t[1:]):
                if x in NUMS and NUMS[x][1] == 'tiered':
                    tf += y in FISH
                    tn += 1
                elif x in NUMS and NUMS[x][1] == 'short':
                    sf += y in FISH
                    sn += 1
        p = hyper_ge(tf, tn - tf, sf, sn - sf)
        ok = ok and p < 0.05 and tf / max(1, tn) > sf / max(1, sn)
        say('- %s: %s.' % (lab, fline('tiered numerals before a fish', tf, tn, sf, sn, p)))
    rec_('X16', ok)

    # X17
    say('## X17 Mohenjo-daro tablets count another unit')
    c = Counter(y for r in tabs if r['site'].strip() == 'Mohenjo-daro' for ln in r['seq']
                for x, y in zip(ln, ln[1:]) if x in NUMS and y not in NUMS)
    top, k = c.most_common(1)[0]
    say('- Mohenjo-daro tablets, sign after a numeral (%d tokens): %s.' % (
        sum(c.values()), ', '.join('%s %.0f%%' % (g, 100 * v / sum(c.values())) for g, v in c.most_common(6))))
    rec_('X17', top != '700' and k / sum(c.values()) >= 0.3)

    # X18
    say('## X18 same-value count tokens lie together')
    val = {'32': 2, '33': 3, '34': 4}
    it = []
    for r in tabs:
        if r['site'].strip() != 'Harappa' or r['depth'] is None or not n700(r):
            continue
        vs = [x for ln in r['seq'] for x, y in zip(ln, ln[1:]) if y == '700' and x in val]
        if vs:
            it.append((val[vs[0]], r['depth']))
    v = np.array([a for a, _ in it])
    d = np.array([b for _, b in it], dtype=float)
    iu = np.triu_indices(len(it), 1)
    dd = np.abs(d[iu[0]] - d[iu[1]])

    def st18(vv):
        same = vv[iu[0]] == vv[iu[1]]
        return np.median(dd[~same]) - np.median(dd[same])
    obs = st18(v)
    ge = 0
    vv = v.copy()
    for _ in range(N):
        np.random.shuffle(vv)
        ge += st18(vv) >= obs
    p = (ge + 1) / (N + 1)
    say('- count tokens with a depth: %d; median depth difference, different minus same value %+.2f; p = %.4f.' % (
        len(it), obs, p))
    rec_('X18', obs > 0 and p < 0.05)

    # X19
    say('## X19 longer count tokens name someone')
    sb = {name_of(ln)[0] for r in seals for ln in r['seq'] if name_of(ln)}
    pre = []
    for r in tabs:
        if not n700(r) or len(r['flat']) <= 2:
            continue
        f = r['flat']
        i = next(i for i in range(len(f) - 1) if f[i] in NUMS and f[i + 1] == '700')
        if i >= 1:
            pre.append(tuple(f[:i]))
    obs = sum(x in sb for x in pre)
    ge = 0
    for _ in range(N):
        k = 0
        for x in pre:
            s = list(x)
            random.shuffle(s)
            k += tuple(s) in sb
        ge += k >= obs
    p = (ge + 1) / (N + 1)
    say('- prefixes before the count: %d (%s); equal to a seal name body: %d; p = %.4f.' % (
        len(pre), ', '.join('%s x%d' % ('-'.join(k_), v_) for k_, v_ in Counter(pre).most_common(5)), obs, p))
    rec_('X19', p < 0.05)

    # X20
    say('## X20 the human head 100 is known everywhere')
    tok, sites = Counter(), defaultdict(set)
    for r in seals:
        for g in set(r['flat']):
            tok[g] += 1
            sites[g].add(r['site'].strip())
    S = [g for g in head | {'100'} if tok[g] >= 5]
    q = T.quintiles(tok, S)
    pool = [g for g in S if g != '100' and q[g] == q['100']]
    k = sum(1 for g in pool if len(sites[g]) >= len(sites['100']))
    p = (k + 1) / (len(pool) + 1)
    say('- 100 on %d seals at %d sites; matched heads: %s; p = %.4f.' % (
        tok['100'], len(sites['100']), ', '.join('%s %d/%d' % (g, tok[g], len(sites[g])) for g in pool), p))
    rec_('X20', p < 0.05)

    # X21
    say('## X21 numbered fish are star names (520)')
    items = [(any(g in NUMS for g in b[:-1]), min(len(b), 4), 1 if e == '520' else 0) for b, e in NM
             if b[-1] in FISH and len(b) >= 2]
    o, p = strat_perm(items)
    say('- fish-headed names with a numeral %d of %d; stratified difference in 520 share %+.1f points; p = %.4f.' % (
        sum(l for l, _, _ in items), len(items), 100 * o, p))
    rec_('X21', o > 0 and p < 0.05)

    # X22
    say('## X22 90 is a seal sign')
    def post(objs):
        c = Counter(y for r in objs for ln in r['seq'] for x, y in zip(ln, ln[1:]) if x in END and y in POST)
        return c['90'], sum(c.values())
    a, na = post(seals)
    cc, nc = post(tabs)
    p = hyper_ge(a, na - a, cc, nc - cc)
    say('- %s.' % fline('90 among post-ending signs on seals', a, na, cc, nc, p))
    rec_('X22', p < 0.05 and a / max(1, na) > cc / max(1, nc))

    # X23
    say('## X23 moulded and incised tokens count differently')
    it = []
    for r in tabs:
        if r['type'] in ('TAB:B', 'TAB:I') and n700(r):
            vs = [x for ln in r['seq'] for x, y in zip(ln, ln[1:]) if y == '700' and x in val]
            if vs:
                it.append((r['type'], val[vs[0]]))
    X_, Y_ = [a for a, _ in it], [b for _, b in it]
    obs = T.mi(X_, Y_)
    ge = 0
    xx = X_[:]
    for _ in range(N):
        random.shuffle(xx)
        ge += T.mi(xx, Y_) >= obs
    p = (ge + 1) / (N + 1)
    say('- %s; MI %.4f; p = %.4f.' % (', '.join('%s %d x%d' % (a, b, n_) for (a, b), n_ in sorted(Counter(it).items())),
                                      obs, p))
    rec_('X23', p < 0.05)

    # X24
    say('## X24 the closing formula is a Mohenjo-daro habit')
    a = na = cc = nc = 0
    for r in seals:
        for ln in r['seq']:
            nm = name_of(ln)
            if not nm:
                continue
            b = nm[0]
            f = nm[1] == '520' and len(b) >= 2 and b[-1] == '33' and b[-2] in ('705', '706')
            md = r['site'].strip() == 'Mohenjo-daro'
            if f:
                a += md
                na += 1
            else:
                cc += md
                nc += 1
    p = hyper_ge(a, na - a, cc, nc - cc)
    say('- %s.' % fline('formula lines from Mohenjo-daro', a, na, cc, nc, p))
    rec_('X24', p < 0.05 and a / max(1, na) > cc / nc)

    # X25
    say('## X25 fish-named persons carry the heading')
    items = []
    for t in AB:
        nm = name_of(t)
        if nm and nm[0][-1] in FISH and len(t) >= 3:
            items.append((nm[1] == '740', lstrat(len(t)), 1 if headed(t) else 0))
    o, p = strat_perm(items)
    say('- fish-headed lines ending 740: %d of %d; stratified difference in headed share %+.1f points; p = %.4f.' % (
        sum(l for l, _, _ in items), len(items), 100 * o, p))
    rec_('X25', o > 0 and p < 0.05)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test19.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
