"""Test of the fifteenth registered prediction set (PREDICTIONS.md, N1-N10).

Usage: python predict_test15.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test15.md.
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
from predict_test8 import bound_pairs
from predict_test11 import freedom
from predict_test14 import cat_of, classes, hyper_ge

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
OPEN = ('817', '820', '861')
END = ('740', '520')
random.seed(35)


def say(s=''):
    OUT.append(s)
    print(s)


def binom_ge(k, n):
    return sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n if n else 1.0


def strat_perm(items):
    """items: (label bool, stratum, outcome number). Weighted (by label-true count) difference of means, label
    permuted within strata."""
    def stat(lab):
        num = den = 0
        for s in set(st for _, st, _ in items):
            a = [o for l, (_, st, o) in zip(lab, items) if st == s and l]
            b = [o for l, (_, st, o) in zip(lab, items) if st == s and not l]
            if a and b:
                num += len(a) * (sum(a) / len(a) - sum(b) / len(b))
                den += len(a)
        return num / den if den else 0.0
    lab = [l for l, _, _ in items]
    obs = stat(lab)
    idx = defaultdict(list)
    for i, (_, s, _) in enumerate(items):
        idx[s].append(i)
    ge = 0
    for _ in range(N):
        sh = lab[:]
        for ii in idx.values():
            v = [sh[i] for i in ii]
            random.shuffle(v)
            for i, w in zip(ii, v):
                sh[i] = w
        ge += stat(sh) >= obs
    return obs, (ge + 1) / (N + 1)


def main(path):
    A, B = T.sample('A'), T.sample('B')
    cat = cat_of()
    head, _ = classes(A)
    head -= set(END)
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = {r['sealid'] for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST}
    home = [r for r in rows if r['sealid'] not in west and recs[r['sealid']][2] not in ('Other',)]
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    res = []
    say('# Fifteenth registered predictions: morphology and sound signs')
    say()
    say('- samples: A %d lines, B %d lines. Head class: %s.' % (len(A), len(B), ', '.join(sorted(head, key=int))))
    say()

    # N1, N2
    for key, sign in (('N1', '740'), ('N2', '520')):
        say('## %s %s is a bound suffix' % (key, sign))
        ok = True
        for lab, L in (('A', A), ('B', B)):
            tok = Counter(g for t in L for g in t)
            pre = Counter(b for t in L for a, b in zip(t, t[1:]) if a in NUMS)
            r_s = pre[sign] / tok[sign]
            r_h = sum(pre[g] for g in head) / sum(tok[g] for g in head)
            ok = ok and r_s < r_h / 3
            say('- %s: %s preceded by a numeral %d of %d (%.1f%%); head-class signs %d of %d (%.1f%%); one third of that '
                '%.1f%%.' % (lab, sign, pre[sign], tok[sign], 100 * r_s, sum(pre[g] for g in head),
                             sum(tok[g] for g in head), 100 * r_h, 100 * r_h / 3))
        say('- **%s %s.**' % (key, T.verdict(ok)))
        say()
        res.append((key, ok))

    # N3
    say('## N3 741 is an oblique form')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        ns = set(T.names(L))
        b10 = b01 = n = k741 = k_rand = 0
        for t in L:
            nm = name_of(t)
            if not nm:
                continue
            body, end = nm
            pos = [i for i, g in enumerate(body) if g == '741' and i < len(body) - 1]
            if not pos:
                continue
            i = pos[0]
            others = [j for j in range(len(body) - 1) if j != i]
            if not others:
                continue
            j = random.choice(others)
            a = (body[i + 1:], end) in ns
            b = (body[j + 1:], end) in ns
            n += 1
            k741 += a
            k_rand += b
            b10 += a and not b
            b01 += b and not a
        p = binom_ge(b10, b10 + b01)
        ok = ok and b10 > b01 and p < 0.05
        say('- %s: %d texts with a non-final 741; tail after 741 attested %d, tail after a random other position %d; '
            'discordant %d / %d; sign test p = %.4f.' % (lab, n, k741, k_rand, b10, b01, p))
    say('- **N3 %s.**' % T.verdict(ok))
    say()
    res.append(('N3', ok))

    # N4
    say('## N4 rare names are spelled by sound')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        fr = freedom(L)
        cnt = Counter(T.names(L))
        items = []
        for (body, end), c in cnt.items():
            v = [fr[g] for g in body if g in fr and g not in T.GRAM]
            if v:
                items.append((c == 1, min(len(body), 4), sum(v) / len(v)))
        o, p = strat_perm(items)
        ok = ok and o > 0 and p < 0.05
        say('- %s: %d once-only names, %d recurring; mean freedom difference (once minus recurring, length-stratified) '
            '%+.3f; p = %.4f.' % (lab, sum(l for l, _, _ in items), sum(not l for l, _, _ in items), o, p))
    say('- **N4 %s.**' % T.verdict(ok))
    say()
    res.append(('N4', ok))

    # N5
    say('## N5 bound pairs are word sign + sound complement')
    bp = bound_pairs(path)
    ok = True
    for lab, L in (('A', A), ('B', B)):
        fr = freedom(L)
        sc = [(fr[a], fr[b]) for a, b in bp if a in fr and b in fr]
        k = sum(1 for x, y in sc if y > x)
        p = binom_ge(k, len(sc))
        ok = ok and p < 0.05
        say('- %s: pairs scored %d; second sign freer in %d; sign test p = %.4f.' % (lab, len(sc), k, p))
    say('- **N5 %s.**' % T.verdict(ok))
    say()
    res.append(('N5', ok))

    # N6
    say('## N6 tablets carry seal names')
    bodies = set()
    for r in intact:
        if r['type'].startswith('SEAL'):
            for ln in r['seq']:
                nm = name_of(ln)
                if nm:
                    bodies.add(nm[0])
    tabs = sorted({tuple(r['flat']) for r in intact if r['type'].startswith('TAB') and len(r['flat']) >= 2})
    obs = sum(t in bodies for t in tabs)
    ge = 0
    for _ in range(N):
        k = 0
        for t in tabs:
            s = list(t)
            random.shuffle(s)
            k += tuple(s) in bodies
        ge += k >= obs
    p = (ge + 1) / (N + 1)
    ok = p < 0.05
    say('- distinct tablet texts: %d; equal to a seal name body: %d (%s); p (shuffled order) = %.4f. **N6 %s.**' % (
        len(tabs), obs, ', '.join('-'.join(t) for t in tabs if t in bodies)[:600], p, T.verdict(ok)))
    say()
    res.append(('N6', ok))

    # N7
    say('## N7 titles belong to persons')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        items = []
        for t in L:
            nm = name_of(t)
            if not nm or len(t) < 4:
                continue
            hd = t[0] in OPEN and t[1] in ('2', '60', '1')
            items.append((hd, 0 if len(t) <= 5 else (1 if len(t) <= 7 else 2), 1 if nm[1] == '740' else 0))
        o, p = strat_perm(items)
        ok = ok and o > 0 and p < 0.05
        a = [x for h, _, x in items if h]
        b = [x for h, _, x in items if not h]
        say('- %s: headed lines ending 740 %d of %d (%.0f%%), headless %d of %d (%.0f%%); stratified difference %+.1f '
            'points, p = %.4f.' % (lab, sum(a), len(a), 100 * sum(a) / max(1, len(a)), sum(b), len(b),
                                   100 * sum(b) / max(1, len(b)), 100 * o, p))
    say('- **N7 %s.**' % T.verdict(ok))
    say()
    res.append(('N7', ok))

    # N8
    say('## N8 one set of sound signs')
    wl = Counter(g for r in rows if r['sealid'] in west for ln in r['seq'] for g in ln)
    hl = Counter(g for r in home for ln in r['seq'] for g in ln)
    cnt = Counter(T.names(A))
    hap, rec = Counter(), Counter()
    for (body, end), c in cnt.items():
        for g in body:
            (hap if c == 1 else rec)[g] += c
    W, H, P, R = (sum(x.values()) for x in (wl, hl, hap, rec))
    S = [g for g in set(wl) | set(hl) if wl[g] + hl[g] >= 5 and hap[g] + rec[g] >= 5 and g not in T.GRAM]
    e1 = [math.log(((wl[g] + 0.5) / W) / ((hl[g] + 0.5) / H)) for g in S]
    e2 = [math.log(((hap[g] + 0.5) / P) / ((rec[g] + 0.5) / R)) for g in S]
    rho = T.spearman(e1, e2)
    ge = 0
    ee = e2[:]
    for _ in range(N):
        random.shuffle(ee)
        ge += T.spearman(e1, ee) >= rho
    p = (ge + 1) / (N + 1)
    ok = rho > 0 and p < 0.05
    say('- signs: %d (West Asian tokens %d); Spearman of the two enrichments %.3f; p = %.4f. **N8 %s.**' % (
        len(S), W, rho, p, T.verdict(ok)))
    say()
    res.append(('N8', ok))

    # N9
    say('## N9 400 after the ending marks plural')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        items = []
        for t in L:
            nm = name_of(t)
            if not nm:
                continue
            w400 = len(t) >= 3 and t[-1] == '400' and t[-2] in END
            items.append((w400, nm[1], 1 if any(g in NUMS for g in nm[0]) else 0))
        o, p = strat_perm(items)
        ok = ok and o > 0 and p < 0.05
        a = [x for w, _, x in items if w]
        b = [x for w, _, x in items if not w]
        say('- %s: names with 400 containing a numeral %d of %d (%.0f%%), without 400 %d of %d (%.0f%%); '
            'ending-stratified difference %+.1f points, p = %.4f.' % (lab, sum(a), len(a), 100 * sum(a) / max(1, len(a)),
                                                                     sum(b), len(b), 100 * sum(b) / len(b), 100 * o, p))
    say('- **N9 %s.**' % T.verdict(ok))
    say()
    res.append(('N9', ok))

    # N10
    say('## N10 no second man after a human head')
    hw = hn = ow = on = 0
    for t in A + B:
        nm = name_of(t)
        if not nm or nm[1] != '740':
            continue
        w90 = len(t) >= 3 and t[-1] == '90' and t[-2] == '740'
        if cat.get(nm[0][-1]) == 'A':
            hw += w90
            hn += not w90
        else:
            ow += w90
            on += not w90
    p = fisher_less(hw, hn, ow, on)
    ok = p < 0.05 and hw / max(1, hw + hn) < ow / (ow + on)
    say('- pooled A + B: human-headed 740 names followed by 90: %d of %d (%.1f%%); other 740 names %d of %d (%.1f%%); '
        'Fisher one-sided p = %.4f. **N10 %s.**' % (hw, hw + hn, 100 * hw / max(1, hw + hn), ow, ow + on,
                                                   100 * ow / (ow + on), p, T.verdict(ok)))
    say()
    res.append(('N10', ok))

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test15.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
