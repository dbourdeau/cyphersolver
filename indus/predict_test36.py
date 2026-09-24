"""Test of the thirty-sixth registered prediction set (PREDICTIONS.md, OS / OT): the core findings at the other sites
and over time at Mohenjo-daro. The tests are those of predict_test35, applied to other groups of objects.

Usage: python predict_test36.py path/to/icit_full_records_indusscript_net.csv path/to/sk_indus_script-webfont.ttf
Writes results/predict_test36.md. F read with lines reversed; A for direction.
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
from predict_test17 import rank_perm
from predict_test18 import level
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
AFF = ('231', '233', '235', '240')
random.seed(56)


def say(s=''):
    OUT.append(s)
    print(s)


def fl(a, na, c, nc, p):
    return '%d of %d (%.1f%%) against %d of %d (%.1f%%), p = %.4f' % (a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


def gt(a, na, c, nc):
    p = hyper_ge(a, na - a, c, nc - c)
    return p, p < 0.05 and a / max(1, na) > c / max(1, nc)


def lt(a, na, c, nc):
    p = fisher_less(a, na - a, c, nc - c)
    return p, p < 0.05 and a / max(1, na) < c / max(1, nc)


class G:
    """A group of objects with its lines and names."""
    def __init__(self, objs):
        self.objs = objs
        self.lines = [ln for r in objs for ln in r['seq'] if len(ln) >= 2]
        self.names = [name_of(ln) for ln in self.lines if name_of(ln)]


def make_tests(cat, comp, mot):
    kind = lambda g: NUMS[g][1]

    def t1(g):
        nm = [(b[0], b[-1], e) for b, e in g.names if len(b) >= 2]
        F, L, E = [x[0] for x in nm], [x[1] for x in nm], [x[2] for x in nm]
        obs = T.mi(L, E) - T.mi(F, E)
        ge = 0
        ee = E[:]
        for _ in range(N):
            random.shuffle(ee)
            ge += T.mi(L, ee) - T.mi(F, ee) >= obs
        p = (ge + 1) / (N + 1)
        return 'names %d; MI last minus first %+.3f; p = %.4f' % (len(nm), obs, p), obs > 0 and p < 0.05, len(nm)

    def t2(g):
        ns = [b for b, _ in g.names if len(b) >= 2]
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

    def t3(g):
        h = [e == '740' for b, e in g.names if cat.get(b[-1]) == 'A']
        o = [e == '740' for b, e in g.names if cat.get(b[-1]) != 'A']
        p, ok = gt(sum(h), len(h), sum(o), len(o))
        return 'human heads 740 %s' % fl(sum(h), len(h), sum(o), len(o), p), ok, len(h)

    def t16(g):
        byh = defaultdict(Counter)
        for b, e in g.names:
            byh[b[-1]][e] += 1
        hs = [c_ for c_ in byh.values() if sum(c_.values()) >= 5]
        fx = sum(1 for c_ in hs if max(c_.values()) / sum(c_.values()) >= 0.9)
        return 'heads with 5+ names %d; fixed %d' % (len(hs), fx), bool(hs) and fx / len(hs) >= 0.8, sum(sum(c_.values()) for c_ in hs)

    def t8(g):
        a = [i == len(b) - 1 for b, _ in g.names for i, x in enumerate(b) if x in AFF]
        o = [i == len(b) - 1 for b, _ in g.names for i, x in enumerate(b) if x == '220']
        p, ok = lt(sum(a), len(a), sum(o), len(o))
        return 'affixed fish last %s' % fl(sum(a), len(a), sum(o), len(o), p), ok, min(len(a), len(o))

    def t10(g):
        hi = [kind(x) == 'tiered' for t in g.lines for x in t if x in NUMS and 5 <= NUMS[x][0] <= 8]
        lo = [kind(x) == 'tiered' for t in g.lines for x in t if x in NUMS and 3 <= NUMS[x][0] <= 4]
        p, ok = gt(sum(hi), len(hi), sum(lo), len(lo))
        return 'tiered among 5-8 %s' % fl(sum(hi), len(hi), sum(lo), len(lo), p), ok, len(hi)

    def t11(g):
        a = [cat.get(y) in ('J', 'K') for t in g.lines for x, y in zip(t, t[1:]) if x in NUMS and y not in NUMS and kind(x) == 'long']
        o = [cat.get(y) in ('J', 'K') for t in g.lines for x, y in zip(t, t[1:]) if x in NUMS and y not in NUMS and kind(x) == 'short']
        p, ok = gt(sum(a), len(a), sum(o), len(o))
        return 'long before J / K %s' % fl(sum(a), len(a), sum(o), len(o), p), ok, len(a)

    def t12(g):
        prs = [(NUMS[x][0], y) for t in g.lines for x, y in zip(t, t[1:]) if x in NUMS and y not in NUMS]
        xs, ys = [a for a, _ in prs], [b for _, b in prs]
        obs = T.mi(xs, ys)
        ge = 0
        xx = xs[:]
        for _ in range(N):
            random.shuffle(xx)
            ge += T.mi(xx, ys) >= obs
        p = (ge + 1) / (N + 1)
        return 'pairs %d; MI %.3f; p = %.4f' % (len(prs), obs, p), p < 0.05, len(prs)

    def t20(g):
        a = [i == 0 for t in g.lines for i, x in enumerate(t) if x in NUMS and kind(x) == 'long']
        o = [i == 0 for t in g.lines for i, x in enumerate(t) if x in NUMS and kind(x) == 'short']
        p, ok = gt(sum(a), len(a), sum(o), len(o))
        return 'long opening the line %s' % fl(sum(a), len(a), sum(o), len(o), p), ok, len(a)

    def t18(g):
        tk = Counter(x for t in g.lines for x in t)
        S = [x for x in comp if tk[x] >= 5]
        a, b = [comp[x] for x in S], [math.log(tk[x]) for x in S]
        rho = T.spearman(a, b)
        le = 0
        bb = b[:]
        for _ in range(N):
            random.shuffle(bb)
            le += T.spearman(a, bb) <= rho
        p = (le + 1) / (N + 1)
        return 'signs %d; Spearman %.3f; p = %.4f' % (len(S), rho, p), rho < 0 and p < 0.05, len(S)

    def t9(g):
        a = [y in FISH for t in g.lines for x, y in zip(t, t[1:]) if x == '2']
        o = [y in FISH for t in g.lines for x, y in zip(t, t[1:]) if x == '3']
        p, ok = gt(sum(a), len(a), sum(o), len(o))
        return 'fish after the stroke pair %s' % fl(sum(a), len(a), sum(o), len(o), p), ok, len(o)

    def variants(texts):
        by = defaultdict(list)
        for t in texts:
            for i in range(len(t)):
                by[(len(t), i, t[:i], t[i + 1:])].append(t)
        return [(ts[x], ts[y], i) for (n_, i, _, _), ts in by.items() for x in range(len(ts)) for y in range(x + 1, len(ts))]

    def t13(g):
        tv = variants(sorted({tuple(r['flat']) for r in g.objs if r['type'].startswith('TAB') and len(r['flat']) >= 2}))
        sv = variants(sorted({name_of(ln)[0] for r in g.objs if r['type'].startswith('SEAL') for ln in r['seq'] if name_of(ln)}))
        f = lambda v: sum(a[i] in NUMS or b[i] in NUMS for a, b, i in v)
        a, c_ = f(tv), f(sv)
        p, ok = gt(a, len(tv), c_, len(sv))
        return 'tablet variants at a numeral %s' % fl(a, len(tv), c_, len(sv), p), ok, len(tv)

    def t14(g):
        ss = [r for r in g.objs if r['type'].startswith('SEAL') and mot(r) and mot(r) not in ('-', 'None')]
        u = [len(r['flat']) for r in ss if mot(r).startswith('Bull1')]
        o = [len(r['flat']) for r in ss if not mot(r).startswith('Bull1')]
        if not u or not o:
            return 'unicorn %d, other %d' % (len(u), len(o)), False, min(len(u), len(o))
        d, p = rank_perm(u, o)
        return 'unicorn %d, other %d; rank difference %+.1f; p = %.4f' % (len(u), len(o), d, p), d > 0 and p < 0.05, min(len(u), len(o))

    return {'1': t1, '2': t2, '3': t3, '16': t16, '8': t8, '10': t10, '11': t11, '12': t12, '20': t20, '18': t18,
            '9': t9, '13': t13, '14': t14}


def main(path, font_path):
    cat = cat_of()
    icit_full.LINES_REVERSED = True
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    west = lambda r: recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST or r['site'].strip() in ('Unknown', '')
    other = G([r for r in intact if r['site'].strip() not in ('Mohenjo-daro', 'Harappa') and not west(r)])
    two = G([r for r in intact if r['site'].strip() in ('Mohenjo-daro', 'Harappa')])
    md = [r for r in intact if r['site'].strip() == 'Mohenjo-daro']
    early = G([r for r in md if level('Mohenjo-daro', recs[r['sealid']]) == 'E'])
    late = G([r for r in md if level('Mohenjo-daro', recs[r['sealid']]) == 'L'])
    tok = Counter(g for t in two.lines + other.lines for g in t)
    comp = T.complexity(font_path, [g for g in tok if tok[g] >= 5])
    mot = lambda r: recs[r['sealid']][18].strip()
    tests = make_tests(cat, comp, mot)
    res = []

    def run(key, title, groups, tkey):
        say('## %s %s' % (key, title))
        ok = True
        for lab, g in groups:
            line, good, n = tests[tkey](g)
            if n < 20:
                say('- %s: %s; under 20 cases, not testable.' % (lab, line))
                ok = False
            else:
                say('- %s: %s.' % (lab, line))
                ok = ok and good
        say('- **%s %s.**' % (key, T.verdict(ok)))
        say()
        res.append((key, ok))

    say('# Thirty-sixth registered predictions: the core findings beyond the two cities and over time')
    say()
    say('- other sites: %d objects (%s); Mohenjo-daro earlier %d, later %d objects.' % (
        len(other.objs), ', '.join('%s %d' % kv for kv in Counter(r['site'].strip() for r in other.objs).most_common(8)),
        len(early.objs), len(late.objs)))
    say()
    O = [('other sites', other)]
    for key, title, tk in (('OS1', 'the last sign decides the ending', '1'), ('OS2', 'heads are a smaller inventory', '2'),
                           ('OS3', 'human heads take 740', '3'), ('OS16', 'the head fixes the ending', '16'),
                           ('OS8', 'affixed fish are attributes', '8'), ('OS10', 'the tiered form is for larger numbers', '10'),
                           ('OS11', 'long strokes count containers', '11'), ('OS12', 'the sign decides the number', '12'),
                           ('OS20', 'long numbers open the line', '20'), ('OS18', 'frequent signs are simpler', '18')):
        run(key, title, O, tk)

    say('## OS4 the two cities\' rule predicts the other sites')
    byh = defaultdict(Counter)
    for b, e in two.names:
        byh[b[-1]][e] += 1
    rule = {h: c_.most_common(1)[0][0] for h, c_ in byh.items() if sum(c_.values()) >= 3}
    test = [(b[-1], e) for b, e in other.names if b[-1] in rule]
    k = sum(rule[h] == e for h, e in test)
    base = max(Counter(e for _, e in test).values()) / len(test)
    p = sum(math.comb(len(test), i) * base ** i * (1 - base) ** (len(test) - i) for i in range(k, len(test) + 1))
    ok = len(test) >= 20 and k / len(test) >= 0.9 and p < 0.05
    say('- other-site names with a known head %d; accuracy %.1f%%; baseline %.1f%%; p = %.2g.' % (len(test), 100 * k / len(test), 100 * base, p))
    say('- **OS4 %s.**' % T.verdict(ok))
    say()
    res.append(('OS4', ok))

    for key, title, tk in (('OS9', 'the stroke pair goes with the fish', '9'), ('OS13', 'tablets vary in numbers', '13'),
                           ('OS14', 'unicorn seals carry longer texts', '14')):
        run(key, title, O, tk)
    say('## OS19 seals avoid left-to-right writing')
    rowsA = load()
    rs = [r for r in rowsA if r['site'] not in ('Mohenjo-daro', 'Harappa') and r['site'] not in (
        'Kish', 'Luristan', 'Susa', 'Tell Umma', 'Ur', "Qala'at al-Bahrain", "Ra's al-Junayz", 'Salut', 'Karzakan', 'Saar',
        'Hajar', 'Gonur Depe', 'Altyn Depe', 'Shortughai', 'Unknown', '')]
    s_ = [r['direction'] == 'L/R' for r in rs if r['type'].startswith('SEAL')]
    o = [r['direction'] == 'L/R' for r in rs if not r['type'].startswith('SEAL')]
    p, good = lt(sum(s_), len(s_), sum(o), len(o))
    ok = good and min(len(s_), len(o)) >= 20
    say('- other sites: left-to-right, seals %s.' % fl(sum(s_), len(s_), sum(o), len(o), p))
    say('- **OS19 %s.**' % T.verdict(ok))
    say()
    res.append(('OS19', ok))

    TT = [('Mohenjo-daro earlier', early), ('Mohenjo-daro later', late)]
    for key, title, tk in (('OT1', 'the last sign decides the ending', '1'), ('OT3', 'human heads take 740', '3'),
                           ('OT16', 'the head fixes the ending', '16'), ('OT11', 'long strokes count containers', '11'),
                           ('OT12', 'the sign decides the number', '12')):
        run(key, title, TT, tk)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test36.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
