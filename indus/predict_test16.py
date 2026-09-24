"""Test of the sixteenth registered prediction set (PREDICTIONS.md, P1-P25).

Usage: python predict_test16.py path/to/icit_full_records_indusscript_net.csv path/to/sk_indus_script-webfont.ttf
       path/to/linb
Writes results/predict_test16.md.
"""
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

import icit_full
import predict_test13 as T
from gulf import IRAN_WEST, WEST
from numerals import NUMS
from predict_test4 import name_of
from predict_test7 import fisher_less
from predict_test8 import bound_pairs
from predict_test11 import freedom, linb_lines
from predict_test14 import cat_of, classes, hyper_ge
from predict_test15 import binom_ge, strat_perm
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
OPEN = ('817', '820', '861')
END = ('740', '520')
POST = ('90', '400', '151')
random.seed(36)


def say(s=''):
    OUT.append(s)
    print(s)


def set_test(C, pool, tok, score):
    """Mean score of C against random sets matched on token-count quintiles (drawn from pool)."""
    C = [g for g in C if g in pool]
    q = T.quintiles(tok, pool)
    byq = defaultdict(list)
    for g in pool:
        byq[q[g]].append(g)
    obs = score(C)
    ge = 0
    for _ in range(N):
        R = [random.choice(byq[q[g]]) for g in C]
        ge += score(R) >= obs
    return obs, (ge + 1) / (N + 1), len(C)


def enrich(S, a, b):
    A_, B_ = sum(a.values()), sum(b.values())
    x = sum(a[g] for g in S) + 0.5
    y = sum(b[g] for g in S) + 0.5
    return math.log((x / A_) / (y / B_))


def once_rec(lines):
    cnt = Counter(T.names(lines))
    once, rec = Counter(), Counter()
    for (body, end), c in cnt.items():
        for g in body:
            (once if c == 1 else rec)[g] += c
    return cnt, once, rec


def split_texts(lines_rows):
    return [r['seq'] for r in lines_rows]


def m_break(texts, gapfn):
    """Break rate at gaps selected by gapfn(t) (a set of gap indices) against other gaps. texts: lists of lines."""
    a = b = c = d = 0
    for lines in texts:
        t, brk = [], set()
        for ln in lines:
            if t:
                brk.add(len(t))
            t.extend(ln)
        sel = gapfn(t)
        for g in range(1, len(t)):
            isb = g in brk
            if g in sel:
                a += isb
                b += not isb
            else:
                c += isb
                d += not isb
    return a, a + b, c, c + d


def main(path, font_path, linb):
    A, B = T.sample('A'), T.sample('B')
    cat = cat_of()
    head, attr = classes(A)
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = {r['sealid'] for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST}
    home = [r for r in rows if r['sealid'] not in west and recs[r['sealid']][2] not in ('Other',)]
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    bp = bound_pairs(path)
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    say('# Sixteenth registered predictions: twenty-five hypotheses on the leads')
    say()

    # candidate set C
    frA0 = freedom([t for t in A if not name_of(t)])
    sc = {g: v for g, v in frA0.items() if g not in T.GRAM}
    cut = sorted(sc.values())[3 * len(sc) // 4]
    C = sorted((g for g, v in sc.items() if v >= cut), key=int)
    say('- candidate set C (top quartile of freedom in A lines without a name; %d signs): %s.' % (len(C), ', '.join(C)))
    say()

    # P1
    say('## P1 rare-name enrichment agrees between A and B')
    _, oa, ra = once_rec(A)
    _, ob, rb = once_rec(B)
    S = [g for g in set(oa) | set(ra) if oa[g] + ra[g] >= 5 and ob[g] + rb[g] >= 5 and g not in T.GRAM]
    ea = [enrich([g], oa, ra) for g in S]
    eb = [enrich([g], ob, rb) for g in S]
    rho = T.spearman(ea, eb)
    ge = 0
    ee = eb[:]
    for _ in range(N):
        random.shuffle(ee)
        ge += T.spearman(ea, ee) >= rho
    p = (ge + 1) / (N + 1)
    say('- %d signs; Spearman %.3f; p = %.4f.' % (len(S), rho, p))
    rec_('P1', rho > 0 and p < 0.05)

    # P2
    say('## P2 C is enriched in B once-only names')
    tokB = Counter(g for t in B for g in t)
    poolB = [g for g in tokB if tokB[g] >= 5 and g not in T.GRAM]
    o, p, n = set_test(C, poolB, tokB, lambda S_: enrich(S_, ob, rb))
    say('- C signs in B: %d; log enrichment %.3f; p = %.4f.' % (n, o, p))
    rec_('P2', o > 0 and p < 0.05)

    # P3
    say('## P3 C is enriched in West Asian texts')
    wl = Counter(g for r in rows if r['sealid'] in west for ln in r['seq'] for g in ln)
    hl = Counter(g for r in home for ln in r['seq'] for g in ln)
    poolF = [g for g in hl if hl[g] >= 5 and g not in T.GRAM]
    o, p, n = set_test(C, poolF, hl, lambda S_: enrich(S_, wl, hl))
    say('- C signs in F: %d; log enrichment West Asian against home %.3f; p = %.4f.' % (n, o, p))
    rec_('P3', o > 0 and p < 0.05)

    # P4
    say('## P4 C signs are position-free')
    pos = defaultdict(Counter)
    for body, _ in T.names(B):
        for i, g in enumerate(body):
            pos[g]['f' if i == 0 else ('l' if i == len(body) - 1 else 'm')] += 1
    ent = {g: T.entropy(c) for g, c in pos.items() if sum(c.values()) >= 5}
    poolP = [g for g in ent if g not in T.GRAM]
    o, p, n = set_test(C, poolP, tokB, lambda S_: sum(ent[g] for g in S_) / len(S_))
    say('- C signs scored: %d; mean positional entropy %.3f bits; p = %.4f.' % (n, o, p))
    rec_('P4', p < 0.05)

    # P5, P22, P23
    for key, title, outcome, strata, flip in (
            ('P5', 'once-only names repeat a sign', lambda b: 1 if any(b[i] == b[j] and b[i] not in NUMS for i in range(len(b))
                                                                      for j in range(i + 2, len(b))) else 0,
             lambda n: None if n < 3 else min(n, 5), False),
            ('P22', 'once-only names avoid bound pairs', lambda b: 1 if any((x, y) in bp for x, y in zip(b, b[1:])) else 0,
             lambda n: None if n < 2 else min(n, 4), True),
            ('P23', 'once-only names lack a head-class ending sign', lambda b: 1 if b[-1] in head else 0,
             lambda n: min(n, 4), True)):
        say('## %s %s' % (key, title))
        ok = True
        for lab, L in (('A', A), ('B', B)):
            cnt = Counter(T.names(L))
            items = []
            for (body, end), c in cnt.items():
                st = strata(len(body))
                if st is None:
                    continue
                once = c == 1
                items.append(((not once) if flip else once, st, outcome(body)))
            o, p = strat_perm(items)
            ok = ok and o > 0 and p < 0.05
            a = [x for l, _, x in items if l]
            b_ = [x for l, _, x in items if not l]
            say('- %s: %s %d of %d, %s %d of %d; stratified difference %+.1f points, p = %.4f.' % (
                lab, 'recurring' if flip else 'once-only', sum(a), len(a), 'once-only' if flip else 'recurring',
                sum(b_), len(b_), 100 * o, p))
        rec_(key, ok)

    # P24
    say('## P24 C signs are simpler')
    tokA = Counter(g for t in A for g in t)
    comp = T.complexity(font_path, [g for g in tokA if tokA[g] >= 5])
    poolC = [g for g in comp if g not in T.GRAM]
    o, p, n = set_test(C, poolC, tokA, lambda S_: -sum(comp[g] for g in S_) / len(S_))
    say('- C signs with a glyph: %d; mean complexity %.1f; p (simpler than matched sets) = %.4f.' % (n, -o, p))
    rec_('P24', p < 0.05)

    # P25
    say('## P25 control: the rare-word effect in Linear B')
    ll = linb_lines(linb)
    frL = freedom([[s for _, s in t] for t in ll])
    words = []
    for ln in open(os.path.join(linb, 'corpus_damos_lines.txt'), encoding='utf-8'):
        parts = ln.rstrip('\n').split('\t')
        if len(parts) < 3:
            continue
        for tok in parts[2].split():
            if re.match(r'^[a-z0-9*]+(-[a-z0-9*]+)+$', tok) and re.search(r'[a-z]', tok):
                words.append(tuple(tok.split('-')))
    wc = Counter(words)
    items = []
    for w, c in wc.items():
        v = [frL[s] for s in w if s in frL]
        if v:
            items.append((c == 1, min(len(w), 4), sum(v) / len(v)))
    o, p = strat_perm(items)
    say('- Linear B word types: %d once-only, %d recurring; mean syllabogram freedom difference (once minus recurring) '
        '%+.3f; p = %.4f. (If this holds, the Indus rare-name effect is not evidence of sound spelling.)' % (
            sum(l for l, _, _ in items), sum(not l for l, _, _ in items), o, p))
    rec_('P25', o > 0 and p < 0.05)

    # P6
    say('## P6 numerals before 520 are long-stroke')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        a = na = c = nc = 0
        for t in L:
            for x, y in zip(t, t[1:]):
                if x in NUMS:
                    lg = NUMS[x][1] == 'long'
                    if y == '520':
                        a += lg
                        na += 1
                    else:
                        c += lg
                        nc += 1
        p = hyper_ge(a, na - a, c, nc - c)
        ok = ok and p < 0.05 and a / max(1, na) > c / nc
        say('- %s: long-stroke numerals before 520 %d of %d (%.0f%%), before other signs %d of %d (%.0f%%); p = %.4f.' % (
            lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / nc, p))
    rec_('P6', ok)

    # P7
    say('## P7 520 lines on tablets and sealings')
    items = []
    for r in intact:
        k = 1 if r['type'].startswith(('TAB', 'TAG')) else (0 if r['type'].startswith('SEAL') else None)
        if k is None:
            continue
        for ln in r['seq']:
            nm = name_of(ln)
            if nm:
                items.append((k == 1, min(len(ln), 5), 1 if nm[1] == '520' else 0))
    o, p = strat_perm(items)
    a = [x for l, _, x in items if l]
    b_ = [x for l, _, x in items if not l]
    say('- tablets + sealings ending 520: %d of %d; seals %d of %d; stratified difference %+.1f points, p = %.4f.' % (
        sum(a), len(a), sum(b_), len(b_), 100 * o, p))
    rec_('P7', o > 0 and p < 0.05)

    # P8
    say('## P8 520 is followed by name material more than 740')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        cnt = {e: [0, 0] for e in END}
        for t in L:
            for i, g in enumerate(t):
                if g in END:
                    cnt[g][1] += 1
                    cnt[g][0] += i < len(t) - 1 and t[i + 1] not in POST
        a, na = cnt['520']
        c, nc = cnt['740']
        p = hyper_ge(a, na - a, c, nc - c)
        ok = ok and p < 0.05 and a / na > c / nc
        say('- %s: 520 followed by name material %d of %d (%.0f%%), 740 %d of %d (%.0f%%); p = %.4f.' % (
            lab, a, na, 100 * a / na, c, nc, 100 * c / nc, p))
    rec_('P8', ok)

    # P9
    say('## P9 520 names carry numerals away from the ending')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        items = []
        for body, end in T.names(L):
            if len(body) < 2:
                continue
            items.append((end == '520', min(len(body), 4), 1 if any(g in NUMS for g in body[:-1]) else 0))
        o, p = strat_perm(items)
        ok = ok and o > 0 and p < 0.05
        say('- %s: stratified difference (520 minus 740 names) %+.1f points, p = %.4f.' % (lab, 100 * o, p))
    rec_('P9', ok)

    # P10
    say('## P10 human heads are not counted')
    hw = hn = ow = on = 0
    for t in A + B:
        for x, y in zip(t, t[1:]):
            if y in head or cat.get(y) == 'A':
                if cat.get(y) == 'A':
                    hw += x in NUMS
                    hn += x not in NUMS
                elif y in head:
                    ow += x in NUMS
                    on += x not in NUMS
    p = fisher_less(hw, hn, ow, on)
    say('- pooled: human signs preceded by a numeral %d of %d (%.1f%%), other head-class signs %d of %d (%.1f%%); '
        'p = %.4f.' % (hw, hw + hn, 100 * hw / max(1, hw + hn), ow, ow + on, 100 * ow / (ow + on), p))
    rec_('P10', p < 0.05 and hw / max(1, hw + hn) < ow / (ow + on))

    # P11, P12
    def variants(texts):
        by = defaultdict(list)
        for t in texts:
            for i in range(len(t)):
                by[(len(t), i, t[:i], t[i + 1:])].append(t)
        out = []
        for (n, i, _, _), ts in by.items():
            for x in range(len(ts)):
                for y in range(x + 1, len(ts)):
                    out.append((ts[x], ts[y], i))
        return out
    tabs = sorted({tuple(r['flat']) for r in intact if r['site'].strip() == 'Harappa' and r['type'].startswith('TAB')
                   and len(r['flat']) >= 2})
    tv = variants(tabs)
    num_at = lambda a, b, i: a[i] in NUMS or b[i] in NUMS
    obs = sum(num_at(a, b, i) for a, b, i in tv)
    ge = 0
    for _ in range(N):
        k = 0
        for a, b, i in tv:
            j = random.randrange(len(a))
            k += num_at(a, b, j)
        ge += k >= obs
    p = (ge + 1) / (N + 1)
    say('## P11 tablet variants differ at a numeral')
    say('- Harappa tablet texts: %d distinct; one-position variant pairs %d; differing at a numeral %d (%.0f%%); p = %.4f.'
        % (len(tabs), len(tv), obs, 100 * obs / max(1, len(tv)), p))
    rec_('P11', p < 0.05)
    sb = sorted({nm[0] for r in intact if r['type'].startswith('SEAL') for ln in r['seq'] for nm in [name_of(ln)] if nm})
    sv = variants(sb)
    k2 = sum(num_at(a, b, i) for a, b, i in sv)
    p = fisher_less(k2, len(sv) - k2, obs, len(tv) - obs)
    say('## P12 seal name variants differ at a numeral less often')
    say('- seal name variant pairs %d; differing at a numeral %d (%.0f%%) against tablets %.0f%%; p = %.4f.' % (
        len(sv), k2, 100 * k2 / max(1, len(sv)), 100 * obs / max(1, len(tv)), p))
    rec_('P12', p < 0.05 and k2 / max(1, len(sv)) < obs / max(1, len(tv)))

    # P13
    say('## P13 heads steadier than attributes at Harappa')
    per = []
    for r in intact:
        if r['site'].strip() != 'Harappa':
            continue
        rc = recs[r['sealid']]
        f10 = rc[10].strip()
        if rc[9].strip() == '3' and f10 in ('B', 'C'):
            g = 'E' if f10 == 'B' else 'L'
        elif f10 in ('Stratum IV', 'Stratum V', 'Stratum VI', 'Stratum VII'):
            g = 'E'
        elif f10 in ('Stratum I', 'Stratum II', 'Stratum III'):
            g = 'L'
        else:
            continue
        for ln in r['seq']:
            nm = name_of(ln)
            if nm and len(nm[0]) >= 2:
                per.append((nm[0][0], nm[0][-1], g))

    def d13(labs):
        fe = Counter(f for (f, _, _), l in zip(per, labs) if l == 'E')
        fl = Counter(f for (f, _, _), l in zip(per, labs) if l == 'L')
        le = Counter(h for (_, h, _), l in zip(per, labs) if l == 'E')
        ll_ = Counter(h for (_, h, _), l in zip(per, labs) if l == 'L')
        return T.jsd(fe, fl) - T.jsd(le, ll_)
    labs = [l for _, _, l in per]
    obs = d13(labs)
    ge = 0
    sh = labs[:]
    for _ in range(N):
        random.shuffle(sh)
        ge += d13(sh) >= obs
    p = (ge + 1) / (N + 1)
    say('- Harappa names with a level: %d (earlier %d, later %d); JSD first minus last %+.3f; p = %.4f.' % (
        len(per), labs.count('E'), labs.count('L'), obs, p))
    rec_('P13', obs > 0 and p < 0.05)

    # P14
    say('## P14 two attribute slots')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        b3 = [b for b, _ in T.names(L) if len(b) == 3]

        def mi_slots(pairs):
            xs = [p_[0] for p_ in pairs] + [p_[1] for p_ in pairs]
            ys = [1] * len(pairs) + [2] * len(pairs)
            return T.mi(xs, ys)
        pr = [(b[0], b[1]) for b in b3]
        obs = mi_slots(pr)
        ge = 0
        for _ in range(N):
            ge += mi_slots([(x, y) if random.random() < 0.5 else (y, x) for x, y in pr]) >= obs
        p = (ge + 1) / (N + 1)
        ok = ok and p < 0.05
        say('- %s: %d three-sign names; MI(sign; slot) %.3f bits; p = %.4f.' % (lab, len(b3), obs, p))
    rec_('P14', ok)

    # P15
    say('## P15 numerals stand before other attributes')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        first = later = 0
        for b, _ in T.names(L):
            if len(b) < 3:
                continue
            att = b[:-1]
            nums = [i for i, g in enumerate(att) if g in NUMS]
            others = [i for i, g in enumerate(att) if g not in NUMS and g not in T.GRAM]
            if len(nums) != 1 or not others:
                continue
            if nums[0] < min(others):
                first += 1
            else:
                later += 1
        p = binom_ge(first, first + later)
        ok = ok and first > later and p < 0.05
        say('- %s: numeral first %d, not first %d; sign test p = %.4f.' % (lab, first, later, p))
    rec_('P15', ok)

    # P21
    say('## P21 attributes are freer than heads')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        fr = freedom(L)
        tk = Counter(g for t in L for g in t)
        S_ = [g for g in (head | attr) if g in fr and g not in T.GRAM]
        labl = [g in attr for g in S_]
        if sum(labl) < 2 or len(S_) - sum(labl) < 2:
            say('- %s: too few scored signs.' % lab)
            ok = False
            continue
        q = T.quintiles(tk, S_)

        def st(lb):
            a = [fr[g] for g, l in zip(S_, lb) if l]
            b_ = [fr[g] for g, l in zip(S_, lb) if not l]
            return sum(a) / len(a) - sum(b_) / len(b_)
        obs = st(labl)
        grp = defaultdict(list)
        for i, g in enumerate(S_):
            grp[q[g]].append(i)
        ge = 0
        for _ in range(N):
            sh = labl[:]
            for ii in grp.values():
                v = [sh[i] for i in ii]
                random.shuffle(v)
                for i, w in zip(ii, v):
                    sh[i] = w
            ge += st(sh) >= obs
        p = (ge + 1) / (N + 1)
        ok = ok and obs > 0 and p < 0.05
        say('- %s: %d attributes, %d heads scored; freedom difference %+.3f; p = %.4f.' % (
            lab, sum(labl), len(S_) - sum(labl), obs, p))
    rec_('P21', ok)

    # P16-P20 on M
    m77 = [r['seq'] for r in load(only_m77=True) if len(r['seq']) >= 2 and not any('?' in ln for ln in r['seq'])]

    def gaps_pairs(pred):
        return lambda t: {g for g in range(1, len(t)) if pred(t[g - 1], t[g])}

    def name_gaps(t):
        off = 2 if len(t) >= 3 and t[0] in OPEN and t[1] in ('2', '60', '1') else 0
        e = None
        for i in range(len(t) - 1, -1, -1):
            if t[i] in END:
                e = i
                break
        if e is None or e - off < 2:
            return None
        before_head = {e - 1}
        inner = set(range(off + 1, e - 1))
        return before_head, inner

    tests = [('P16', 'numeral + fish kept together', gaps_pairs(lambda x, y: x in NUMS and y in FISH), 'less'),
             ('P17', 'ending + post-ending sign kept together', gaps_pairs(lambda x, y: x in END and y in POST), 'less'),
             ('P18', 'head + ending kept together', gaps_pairs(lambda x, y: y in END), 'less'),
             ('P20', 'heading is a separate word', lambda t: {2} if len(t) >= 3 and t[0] in OPEN and
              t[1] in ('2', '60', '1') else set(), 'more')]
    for key, title, fn, direction in tests:
        say('## %s %s' % (key, title))
        ok = True
        for lab, texts in (('as listed', m77), ('reversed', [t[::-1] for t in m77])):
            a, na, c, nc = m_break(texts, fn)
            if direction == 'less':
                p = fisher_less(a, na - a, c, nc - c)
                good = p < 0.05 and a / max(1, na) < c / nc
            else:
                p = hyper_ge(a, na - a, c, nc - c)
                good = p < 0.05 and a / max(1, na) > c / nc
            ok = ok and good
            say('- lines %s: selected gaps broken %d of %d (%.1f%%), other gaps %d of %d (%.1f%%); p = %.4f.' % (
                lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / nc, p))
        rec_(key, ok)

    say('## P19 attribute and head are separate words')
    ok = True
    for lab, texts in (('as listed', m77), ('reversed', [t[::-1] for t in m77])):
        a = na = c = nc = 0
        for lines in texts:
            t, brk = [], set()
            for ln in lines:
                if t:
                    brk.add(len(t))
                t.extend(ln)
            ng = name_gaps(t)
            if not ng:
                continue
            bh, inner = ng
            for g in bh:
                a += g in brk
                na += 1
            for g in inner:
                c += g in brk
                nc += 1
        p = hyper_ge(a, na - a, c, nc - c)
        good = p < 0.05 and a / max(1, na) > c / max(1, nc)
        ok = ok and good
        say('- lines %s: gap before the head broken %d of %d (%.1f%%), other name-internal gaps %d of %d (%.1f%%); '
            'p = %.4f.' % (lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p))
    rec_('P19', ok)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test16.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
