"""Test of the thirty-fifth registered prediction set (PREDICTIONS.md, SR1-SR20): the core findings, city by city.

Usage: python predict_test35.py path/to/icit_full_records_indusscript_net.csv path/to/sk_indus_script-webfont.ttf
Writes results/predict_test35.md. F read with lines reversed; A for direction.
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
from predict_test15 import binom_ge
from predict_test16 import m_break
from predict_test17 import headed, rank_perm
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
CITIES = ('Mohenjo-daro', 'Harappa')
AFF = ('231', '233', '235', '240')
random.seed(55)


def say(s=''):
    OUT.append(s)
    print(s)


def fisher_gt(a, na, c, nc):
    return hyper_ge(a, na - a, c, nc - c)


def fline(a, na, c, nc, p):
    return '%d of %d (%.1f%%) against %d of %d (%.1f%%), p = %.4f' % (a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


def main(path, font_path):
    cat = cat_of()
    head, _ = classes(T.sample('A'))
    icit_full.LINES_REVERSED = True
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    city = {c: [r for r in intact if r['site'].strip() == c] for c in CITIES}
    lines = {c: [ln for r in city[c] for ln in r['seq'] if len(ln) >= 2] for c in CITIES}
    names = {c: [name_of(ln) for ln in lines[c] if name_of(ln)] for c in CITIES}
    kind = lambda g: NUMS[g][1]
    res = []

    def run(key, title, fn):
        say('## %s %s' % (key, title))
        ok = True
        for c in CITIES:
            line, good, n = fn(c)
            if n < 20:
                say('- %s: %s; under 20 cases, not testable.' % (c, line))
                ok = False
            else:
                say('- %s: %s.' % (c, line))
                ok = ok and good
        say('- **%s %s.**' % (key, T.verdict(ok)))
        say()
        res.append((key, ok))

    def sr1(c):
        nm = [(b[0], b[-1], e) for b, e in names[c] if len(b) >= 2]
        F, L, E = [x[0] for x in nm], [x[1] for x in nm], [x[2] for x in nm]
        obs = T.mi(L, E) - T.mi(F, E)
        ge = 0
        ee = E[:]
        for _ in range(N):
            random.shuffle(ee)
            ge += T.mi(L, ee) - T.mi(F, ee) >= obs
        p = (ge + 1) / (N + 1)
        return 'names %d; MI last minus first %+.3f; p = %.4f' % (len(nm), obs, p), obs > 0 and p < 0.05, len(nm)
    run('SR1', 'the last sign decides the ending', sr1)

    def sr2(c):
        ns = [b for b, _ in names[c] if len(b) >= 2]
        d = lambda xs: T.entropy(Counter(x[0] for x in xs)) - T.entropy(Counter(x[-1] for x in xs))
        obs = d(ns)
        ge = 0
        for _ in range(N):
            sh = []
            for b in ns:
                b = list(b)
                random.shuffle(b)
                sh.append(b)
            ge += d(sh) >= obs
        p = (ge + 1) / (N + 1)
        return 'names %d; entropy first minus last %+.2f; p = %.4f' % (len(ns), obs, p), obs > 0 and p < 0.05, len(ns)
    run('SR2', 'heads are a smaller inventory', sr2)

    def sr3(c):
        h = [e == '740' for b, e in names[c] if cat.get(b[-1]) == 'A']
        o = [e == '740' for b, e in names[c] if cat.get(b[-1]) != 'A']
        p = fisher_gt(sum(h), len(h), sum(o), len(o))
        return 'human heads 740 %s' % fline(sum(h), len(h), sum(o), len(o), p), p < 0.05 and sum(h) / max(1, len(h)) > sum(o) / len(o), len(h)
    run('SR3', 'human heads take 740', sr3)

    say('## SR4 the head rule carries from city to city')
    ok = True
    for a_, b_ in (CITIES, CITIES[::-1]):
        byh = defaultdict(Counter)
        for b, e in names[a_]:
            byh[b[-1]][e] += 1
        rule = {h: c_.most_common(1)[0][0] for h, c_ in byh.items() if sum(c_.values()) >= 3}
        test = [(b[-1], e) for b, e in names[b_] if b[-1] in rule]
        k = sum(rule[h] == e for h, e in test)
        base = max(Counter(e for _, e in test).values()) / len(test)
        p = sum(math.comb(len(test), i) * base ** i * (1 - base) ** (len(test) - i) for i in range(k, len(test) + 1))
        good = len(test) >= 20 and k / len(test) >= 0.9 and p < 0.05
        ok = ok and good
        say('- learned at %s, tested at %s: %d names; accuracy %.1f%%; baseline %.1f%%; p = %.2g.' % (
            a_, b_, len(test), 100 * k / len(test), 100 * base, p))
    say('- **SR4 %s.**' % T.verdict(ok))
    say()
    res.append(('SR4', ok))

    def sr7(c):
        ns = set(names[c])
        b10 = b01 = 0
        for body, end in ns:
            if len(body) < 3:
                continue
            suf = (body[1:], end) in ns
            pre = any((body[:-1], e) in ns for e in ('740', '520'))
            b10 += suf and not pre
            b01 += pre and not suf
        p = binom_ge(b10, b10 + b01)
        return 'minus first attested only %d, minus last only %d; p = %.4f' % (b10, b01, p), b10 > b01 and p < 0.05, b10 + b01
    run('SR7', 'names grow at the front', sr7)

    def sr8(c):
        a = [i == len(b) - 1 for b, _ in names[c] for i, g in enumerate(b) if g in AFF]
        o = [i == len(b) - 1 for b, _ in names[c] for i, g in enumerate(b) if g == '220']
        p = fisher_less(sum(a), len(a) - sum(a), sum(o), len(o) - sum(o))
        return 'affixed fish last %s' % fline(sum(a), len(a), sum(o), len(o), p), p < 0.05 and sum(a) / max(1, len(a)) < sum(o) / max(1, len(o)), min(len(a), len(o))
    run('SR8', 'affixed fish are attributes', sr8)

    def sr16(c):
        byh = defaultdict(Counter)
        for b, e in names[c]:
            byh[b[-1]][e] += 1
        hs = [c_ for c_ in byh.values() if sum(c_.values()) >= 5]
        fx = sum(1 for c_ in hs if max(c_.values()) / sum(c_.values()) >= 0.9)
        return 'heads with 5+ names %d; fixed %d (%.0f%%)' % (len(hs), fx, 100 * fx / max(1, len(hs))), hs and fx / len(hs) >= 0.8, sum(sum(c_.values()) for c_ in hs)
    run('SR16', 'the head fixes the ending', sr16)

    def sr17(c):
        k7 = [cat[b[-1]] in 'AHIK' for b, e in names[c] if e == '740' and b[-1] in cat and cat[b[-1]] != 'Q' and b[-1] not in FISH]
        k5 = [cat[b[-1]] in 'AHIK' for b, e in names[c] if e == '520' and b[-1] in cat and cat[b[-1]] != 'Q' and b[-1] not in FISH]
        p = fisher_gt(sum(k7), len(k7), sum(k5), len(k5))
        return '740 heads people and tools %s' % fline(sum(k7), len(k7), sum(k5), len(k5), p), p < 0.05 and sum(k7) / max(1, len(k7)) > sum(k5) / max(1, len(k5)), len(k5)
    run('SR17', '740 is the class of people and trades', sr17)

    def sr15(c):
        hd, un = defaultdict(Counter), defaultdict(Counter)
        for ln in lines[c]:
            x = name_of(ln)
            if x:
                (hd if headed(ln) else un)[x[0][-1]][x[1]] += 1
        hs = [h for h in hd if sum(hd[h].values()) >= 5 and sum(un[h].values()) >= 5]
        ag = sum(1 for h in hs if hd[h].most_common(1)[0][0] == un[h].most_common(1)[0][0])
        n_ = sum(sum(hd[h].values()) + sum(un[h].values()) for h in hs)
        return 'heads %d; same majority %d' % (len(hs), ag), hs and ag / len(hs) >= 0.8, n_
    run('SR15', 'the heading does not change the ending', sr15)

    # units kept whole
    def pmi_pairs(ls):
        single = [ln for ln in ls]
        uni = Counter(g for t in single for g in t)
        bi = Counter((a, b) for t in single for a, b in zip(t, t[1:]))
        N1, N2 = sum(uni.values()), sum(bi.values())
        pm = {p_: math.log((c_ / N2) / ((uni[p_[0]] / N1) * (uni[p_[1]] / N1))) for p_, c_ in bi.items() if c_ >= 10}
        return set(sorted(pm, key=lambda p_: -pm[p_])[:30])
    single = {c: [r['seq'][0] for r in city[c] if len(r['seq']) == 1 and len(r['seq'][0]) >= 2] for c in CITIES}
    multi = {c: [r['seq'] for r in city[c] if len(r['seq']) >= 2] for c in CITIES}

    def sr5(c):
        other = CITIES[1] if c == CITIES[0] else CITIES[0]
        bp = pmi_pairs(single[other])
        a, na, cc, nc = m_break(multi[c], lambda t: {g for g in range(1, len(t)) if (t[g - 1], t[g]) in bp})
        p = fisher_less(a, na - a, cc, nc - cc)
        return 'bound gaps broken %s' % fline(a, na, cc, nc, p), p < 0.05 and a / max(1, na) < cc / max(1, nc), na
    run('SR5', "the other city's bound pairs are not split", sr5)

    def sr6(c):
        a, na, cc, nc = m_break(multi[c], lambda t: {g for g in range(1, len(t)) if t[g - 1] in NUMS and t[g] not in NUMS})
        p = fisher_less(a, na - a, cc, nc - cc)
        return 'numeral | sign broken %s' % fline(a, na, cc, nc, p), p < 0.05 and a / max(1, na) < cc / max(1, nc), na
    run('SR6', 'a numeral and its sign are not split', sr6)

    # numbers
    def sr9(c):
        a = [y in FISH for t in lines[c] for x, y in zip(t, t[1:]) if x == '2']
        o = [y in FISH for t in lines[c] for x, y in zip(t, t[1:]) if x == '3']
        p = fisher_gt(sum(a), len(a), sum(o), len(o))
        return 'fish after the stroke pair %s' % fline(sum(a), len(a), sum(o), len(o), p), p < 0.05 and sum(a) / max(1, len(a)) > sum(o) / max(1, len(o)), len(o)
    run('SR9', 'the stroke pair goes with the fish', sr9)

    def sr10(c):
        hi = [kind(g) == 'tiered' for t in lines[c] for g in t if g in NUMS and 5 <= NUMS[g][0] <= 8]
        lo = [kind(g) == 'tiered' for t in lines[c] for g in t if g in NUMS and 3 <= NUMS[g][0] <= 4]
        p = fisher_gt(sum(hi), len(hi), sum(lo), len(lo))
        return 'tiered among 5-8 %s' % fline(sum(hi), len(hi), sum(lo), len(lo), p), p < 0.05 and sum(hi) / max(1, len(hi)) > sum(lo) / max(1, len(lo)), len(hi)
    run('SR10', 'the tiered form is for larger numbers', sr10)

    def sr11(c):
        a = [cat.get(y) in ('J', 'K') for t in lines[c] for x, y in zip(t, t[1:]) if x in NUMS and y not in NUMS and kind(x) == 'long']
        o = [cat.get(y) in ('J', 'K') for t in lines[c] for x, y in zip(t, t[1:]) if x in NUMS and y not in NUMS and kind(x) == 'short']
        p = fisher_gt(sum(a), len(a), sum(o), len(o))
        return 'long before J / K %s' % fline(sum(a), len(a), sum(o), len(o), p), p < 0.05 and sum(a) / max(1, len(a)) > sum(o) / max(1, len(o)), len(a)
    run('SR11', 'long strokes count containers', sr11)

    def sr12(c):
        prs = [(NUMS[x][0], y) for t in lines[c] for x, y in zip(t, t[1:]) if x in NUMS and y not in NUMS]
        xs, ys = [a for a, _ in prs], [b for _, b in prs]
        obs = T.mi(xs, ys)
        ge = 0
        xx = xs[:]
        for _ in range(N):
            random.shuffle(xx)
            ge += T.mi(xx, ys) >= obs
        p = (ge + 1) / (N + 1)
        return 'pairs %d; MI %.3f; p = %.4f' % (len(prs), obs, p), p < 0.05, len(prs)
    run('SR12', 'the sign decides the number', sr12)

    def sr20(c):
        a = [i == 0 for t in lines[c] for i, g in enumerate(t) if g in NUMS and kind(g) == 'long']
        o = [i == 0 for t in lines[c] for i, g in enumerate(t) if g in NUMS and kind(g) == 'short']
        p = fisher_gt(sum(a), len(a), sum(o), len(o))
        return 'long opening the line %s' % fline(sum(a), len(a), sum(o), len(o), p), p < 0.05 and sum(a) / max(1, len(a)) > sum(o) / max(1, len(o)), len(a)
    run('SR20', 'long numbers open the line', sr20)

    def variants(texts):
        by = defaultdict(list)
        for t in texts:
            for i in range(len(t)):
                by[(len(t), i, t[:i], t[i + 1:])].append(t)
        out = []
        for (n_, i, _, _), ts in by.items():
            for x in range(len(ts)):
                for y in range(x + 1, len(ts)):
                    out.append((ts[x], ts[y], i))
        return out

    def sr13(c):
        tv = variants(sorted({tuple(r['flat']) for r in city[c] if r['type'].startswith('TAB') and len(r['flat']) >= 2}))
        sv = variants(sorted({name_of(ln)[0] for r in city[c] if r['type'].startswith('SEAL') for ln in r['seq'] if name_of(ln)}))
        f = lambda v: sum(a[i] in NUMS or b[i] in NUMS for a, b, i in v)
        a, c_ = f(tv), f(sv)
        p = fisher_gt(a, len(tv), c_, len(sv))
        return 'tablet variants at a numeral %s' % fline(a, len(tv), c_, len(sv), p), p < 0.05 and a / max(1, len(tv)) > c_ / max(1, len(sv)), len(tv)
    run('SR13', 'tablets vary in numbers, seals in words', sr13)

    mot = lambda r: ('' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip())

    def sr14(c):
        ss = [r for r in city[c] if r['type'].startswith('SEAL') and mot(r) and mot(r) not in ('-', 'None')]
        u = [len(r['flat']) for r in ss if mot(r).startswith('Bull1')]
        o = [len(r['flat']) for r in ss if not mot(r).startswith('Bull1')]
        d, p = rank_perm(u, o)
        return 'unicorn %d, other %d; rank difference %+.1f; p = %.4f' % (len(u), len(o), d, p), d > 0 and p < 0.05, len(o)
    run('SR14', 'unicorn seals carry longer texts', sr14)

    tokall = Counter(g for c in CITIES for t in lines[c] for g in t)
    comp = T.complexity(font_path, [g for g in tokall if tokall[g] >= 5])

    def sr18(c):
        tk = Counter(g for t in lines[c] for g in t)
        S = [g for g in comp if tk[g] >= 5]
        a, b = [comp[g] for g in S], [math.log(tk[g]) for g in S]
        rho = T.spearman(a, b)
        le = 0
        bb = b[:]
        for _ in range(N):
            random.shuffle(bb)
            le += T.spearman(a, bb) <= rho
        p = (le + 1) / (N + 1)
        return 'signs %d; Spearman %.3f; p = %.4f' % (len(S), rho, p), rho < 0 and p < 0.05, len(S)
    run('SR18', 'frequent signs are simpler', sr18)

    rowsA = load()

    def sr19(c):
        rs = [r for r in rowsA if r['site'] == c]
        s_ = [r['direction'] == 'L/R' for r in rs if r['type'].startswith('SEAL')]
        o = [r['direction'] == 'L/R' for r in rs if not r['type'].startswith('SEAL')]
        p = fisher_less(sum(s_), len(s_) - sum(s_), sum(o), len(o) - sum(o))
        return 'left-to-right, seals %s' % fline(sum(s_), len(s_), sum(o), len(o), p), p < 0.05 and sum(s_) / max(1, len(s_)) < sum(o) / max(1, len(o)), min(len(s_), len(o))
    run('SR19', 'seals avoid left-to-right writing', sr19)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test35.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
