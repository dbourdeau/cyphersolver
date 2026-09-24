"""Test of the twentieth registered prediction set (PREDICTIONS.md, Z1-Z10).

Usage: python predict_test20.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test20.md.
"""
import os
import random
import sys
from collections import Counter, defaultdict

import numpy as np

import icit_full
import predict_test13 as T
from numerals import NUMS
from predict_test4 import name_of
from predict_test7 import fisher_less
from predict_test14 import cat_of, hyper_ge
from predict_test15 import strat_perm
from predict_test18 import lstrat, n700
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
random.seed(40)


def say(s=''):
    OUT.append(s)
    print(s)


def fline(lab, a, na, c, nc, p):
    return '%s %d of %d (%.1f%%) against %d of %d (%.1f%%), p = %.4f' % (
        lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


def main(path):
    A, B = T.sample('A'), T.sample('B')
    cat = cat_of()
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    tabs = [r for r in intact if r['type'].startswith('TAB')]
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    say('# Twentieth registered predictions: ten hypotheses')
    say()

    # Z1
    say('## Z1 numbered fish take 520, in each transcription')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        items = [(any(g in NUMS for g in b[:-1]), min(len(b), 4), 1 if e == '520' else 0) for b, e in T.names(L)
                 if b[-1] in FISH and len(b) >= 2]
        o, p = strat_perm(items)
        ok = ok and o > 0 and p < 0.05
        a = [x for l, _, x in items if l]
        b_ = [x for l, _, x in items if not l]
        say('- %s: with a numeral %d of %d take 520, without %d of %d; stratified difference %+.1f points; p = %.4f.' % (
            lab, sum(a), len(a), sum(b_), len(b_), 100 * o, p))
    rec_('Z1', ok)

    # Z2
    say('## Z2 705 and 706 share frames')
    tok = Counter(g for t in A for g in t)
    fr = defaultdict(set)
    for t in A:
        s = ['^'] + t + ['$']
        for i in range(1, len(s) - 1):
            fr[s[i]].add((s[i - 1], s[i + 1]))
    S = [g for g in tok if tok[g] >= 5]
    q = T.quintiles(tok, S)
    byq = defaultdict(list)
    for g in S:
        byq[q[g]].append(g)
    obs = len(fr['705'] & fr['706'])
    ge = 0
    for _ in range(N):
        while True:
            a, b = random.choice(byq[q['705']]), random.choice(byq[q['706']])
            if a != b and {a, b} != {'705', '706'}:
                break
        ge += len(fr[a] & fr[b]) >= obs
    p = (ge + 1) / (N + 1)
    say('- 705 (%d tokens) and 706 (%d) share %d frames (%s); p = %.4f.' % (
        tok['705'], tok['706'], obs, ', '.join('%s_%s' % f for f in sorted(fr['705'] & fr['706'])[:8]), p))
    rec_('Z2', p < 0.05)

    # Z3
    say('## Z3 740 heads are persons and their tools')
    PT = set('AHIK')
    a = na = c = nc = 0
    for b, e in T.names(A + B):
        k = cat.get(b[-1])
        if not k:
            continue
        if e == '740':
            a += k in PT
            na += 1
        else:
            c += k in PT
            nc += 1
    p = hyper_ge(a, na - a, c, nc - c)
    say('- %s.' % fline('categorised 740 heads that are humans, weapons, implements or measures', a, na, c, nc, p))
    rec_('Z3', p < 0.05 and a / na > c / max(1, nc))

    # Z4
    say('## Z4 moulded count tokens lie together')
    it = [(r['type'], tuple(r['flat']), r['depth']) for r in tabs if r['site'].strip() == 'Harappa' and n700(r)
          and r['depth'] is not None and r['type'] in ('TAB:B', 'TAB:I')]
    pairs = [(i, j) for i in range(len(it)) for j in range(i + 1, len(it)) if it[i][1] == it[j][1]]
    d = np.array([abs(it[i][2] - it[j][2]) for i, j in pairs])
    types = [x[0] for x in it]

    def st(tp):
        m = np.array([tp[i] == 'TAB:B' and tp[j] == 'TAB:B' for i, j in pairs])
        n_ = np.array([tp[i] == 'TAB:I' and tp[j] == 'TAB:I' for i, j in pairs])
        if not m.any() or not n_.any():
            return 0.0
        return np.median(d[n_]) - np.median(d[m])
    obs = st(types)
    ge = 0
    tp = types[:]
    for _ in range(N):
        random.shuffle(tp)
        ge += st(tp) >= obs
    p = (ge + 1) / (N + 1)
    say('- Harappa count tokens with a depth: %d (moulded %d, incised %d); same-text pairs %d; median difference '
        'incised minus moulded %+.2f ft; p = %.4f.' % (len(it), types.count('TAB:B'), types.count('TAB:I'), len(pairs),
                                                      obs, p))
    rec_('Z4', obs > 0 and p < 0.05)

    # Z5-Z7
    m77 = [r['seq'] for r in load(only_m77=True) if len(r['seq']) >= 2 and not any('?' in ln for ln in r['seq'])]
    for key, sign in (('Z5', '90'), ('Z6', '400'), ('Z7', '740')):
        say('## %s %s never starts a line' % (key, sign))
        ok = True
        for lab, texts in (('as listed', m77), ('reversed', [t[::-1] for t in m77])):
            a = na = c = nc = 0
            for lines in texts:
                for k, ln in enumerate(lines):
                    for i, g in enumerate(ln):
                        init = k > 0 and i == 0
                        if g == sign:
                            a += init
                            na += 1
                        else:
                            c += init
                            nc += 1
            p = fisher_less(a, na - a, c, nc - c)
            ok = ok and p < 0.05 and a / max(1, na) < c / nc
            say('- lines %s: %s.' % (lab, fline('%s tokens starting a non-first line' % sign, a, na, c, nc, p)))
        rec_(key, ok)

    # Z8
    say('## Z8 the value mix replicates across excavations')
    val = {'32': 2, '33': 3, '34': 4}
    ok = True
    for lab, keep in (('HARP', lambda rc: rc[9].strip() == '3'), ('Vats', lambda rc: rc[10].strip().startswith('Stratum'))):
        it = []
        for r in tabs:
            if r['type'] not in ('TAB:B', 'TAB:I') or not n700(r) or not keep(recs[r['sealid']]):
                continue
            vs = [x for ln in r['seq'] for x, y in zip(ln, ln[1:]) if y == '700' and x in val]
            if vs:
                it.append((r['type'], val[vs[0]]))
        X, Y = [a for a, _ in it], [b for _, b in it]
        if len(set(X)) < 2:
            say('- %s: one tablet type only (%s); not testable.' % (lab, dict(Counter(it))))
            ok = False
            continue
        obs = T.mi(X, Y)
        ge = 0
        xx = X[:]
        for _ in range(N):
            random.shuffle(xx)
            ge += T.mi(xx, Y) >= obs
        p = (ge + 1) / (N + 1)
        ok = ok and p < 0.05
        say('- %s: %s; MI %.4f; p = %.4f.' % (lab, ', '.join('%s %d x%d' % (a, b, n_) for (a, b), n_ in
                                                             sorted(Counter(it).items())), obs, p))
    rec_('Z8', ok)

    # Z9
    say('## Z9 names on tablets are incised')
    items = [(r['type'] == 'TAB:I', lstrat(len(r['flat'])), 1 if any(g in ('740', '520') for g in r['flat']) else 0)
             for r in tabs if r['type'] in ('TAB:B', 'TAB:I')]
    o, p = strat_perm(items)
    say('- incised with an ending %d of %d, moulded %d of %d; stratified difference %+.1f points; p = %.4f.' % (
        sum(x for l, _, x in items if l), sum(l for l, _, _ in items), sum(x for l, _, x in items if not l),
        sum(not l for l, _, _ in items), 100 * o, p))
    rec_('Z9', o > 0 and p < 0.05)

    # Z10
    say('## Z10 the head fixes the ending on seals')
    byh = defaultdict(Counter)
    for r in intact:
        if not r['type'].startswith('SEAL'):
            continue
        for ln in r['seq']:
            nm = name_of(ln)
            if nm:
                byh[nm[0][-1]][nm[1]] += 1
                break
    hs = [(h, c) for h, c in byh.items() if sum(c.values()) >= 5]
    fixed = [h for h, c in hs if max(c.values()) / sum(c.values()) >= 0.9]
    say('- heads with 5+ seal names: %d; fixed: %d (%.0f%%); mixed: %s.' % (
        len(hs), len(fixed), 100 * len(fixed) / len(hs),
        '; '.join('%s %s' % (h, dict(c)) for h, c in sorted(hs, key=lambda x: -sum(x[1].values())) if h not in fixed)))
    rec_('Z10', len(fixed) / len(hs) >= 0.8)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test20.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
