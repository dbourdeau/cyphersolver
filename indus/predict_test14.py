"""Test of the fourteenth registered prediction set (PREDICTIONS.md, K1-K15).

Usage: python predict_test14.py path/to/icit_full_records_indusscript_net.csv path/to/sk_indus_script-webfont.ttf
Writes results/predict_test14.md.
"""
import csv
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
from predict_test11 import freedom
from signs import FISH

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
random.seed(34)
T.COORD.update({'Rupar': (30.97, 76.52), 'Desalpur': (23.73, 69.46), 'Gola Dhoro (Bagasra)': (22.95, 70.63),
                'Bhirrana': (29.56, 75.53), 'Kot Diji': (27.35, 68.71), 'Shortughai': (37.35, 69.50)})


def say(s=''):
    OUT.append(s)
    print(s)


def hyper_ge(a, b, c, d):
    """One-sided Fisher: P(first cell >= a) for the 2x2 table [[a, b], [c, d]]."""
    n1, n2, k = a + b, c + d, a + c
    tot = n1 + n2

    def h(x):
        return math.exp(math.lgamma(n1 + 1) - math.lgamma(x + 1) - math.lgamma(n1 - x + 1) + math.lgamma(n2 + 1)
                        - math.lgamma(k - x + 1) - math.lgamma(n2 - k + x + 1) - math.lgamma(tot + 1)
                        + math.lgamma(k + 1) + math.lgamma(tot - k + 1))
    return sum(h(x) for x in range(a, min(n1, k) + 1))


def cat_of():
    out = {}
    for r in csv.DictReader(open(os.path.join(HERE, 'results', 'sign_list.tsv'), encoding='utf-8'), delimiter='\t'):
        f = r['fairservis'].strip()
        if f and '-' in f:
            out[r['sign']] = f.split('-')[0].strip()
    return out


def fisher_line(lab, a, na, c, nc, p):
    return '%s %d of %d (%.0f%%) against %d of %d (%.0f%%), p = %.4f' % (
        lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


def classes(lines):
    pos = defaultdict(Counter)
    for b, _ in T.names(lines):
        if len(b) < 2:
            continue
        for i, g in enumerate(b):
            pos[g]['first' if i == 0 else ('last' if i == len(b) - 1 else 'mid')] += 1
    head = {g for g, c in pos.items() if sum(c.values()) >= 10 and c['last'] / sum(c.values()) >= 0.6}
    attr = {g for g, c in pos.items() if sum(c.values()) >= 10 and c['first'] / sum(c.values()) >= 0.6}
    return head, attr


def main(path, font_path):
    A, B = T.sample('A'), T.sample('B')
    cat = cat_of()
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = {r['sealid'] for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST}
    home = [r for r in rows if r['sealid'] not in west and recs[r['sealid']][2] not in ('Other',)]
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    head, attr = classes(A)
    say('# Fourteenth registered predictions: fifteen hypotheses')
    say()
    say('- Fairservis categories known for %d signs. Head class (from A): %s. Attribute class: %s.' % (
        len(cat), ', '.join(sorted(head, key=int)), ', '.join(sorted(attr, key=int))))
    say()
    res = []

    def both(key, fn):
        ok = True
        for lab, L in (('A', A), ('B', B)):
            line, good = fn(L)
            ok = ok and good
            say('- %s: %s.' % (lab, line))
        say('- **%s %s.**' % (key, T.verdict(ok)))
        say()
        res.append((key, ok))

    # K1
    say('## K1 human heads take 740')

    def k1(L):
        ns = [(b, e) for b, e in T.names(L)]
        hum = [e for b, e in ns if cat.get(b[-1]) == 'A']
        oth = [e for b, e in ns if cat.get(b[-1]) != 'A']
        a, c = sum(e == '740' for e in hum), sum(e == '740' for e in oth)
        p = hyper_ge(a, len(hum) - a, c, len(oth) - c)
        return fisher_line('human heads take 740', a, len(hum), c, len(oth), p) + ' (heads: %s)' % ', '.join(
            '%s x%d' % kv for kv in Counter(b[-1] for b, _ in ns if cat.get(b[-1]) == 'A').most_common()), \
            p < 0.05 and a / max(1, len(hum)) > c / len(oth)
    both('K1', k1)

    # K2
    say('## K2 natural heads take 520')
    NAT, ART = set('CDEFN'), set('AGHIJKLM')

    def k2(L):
        ns = T.names(L)
        nat = [e for b, e in ns if cat.get(b[-1]) in NAT]
        art = [e for b, e in ns if cat.get(b[-1]) in ART]
        a, c = sum(e == '520' for e in nat), sum(e == '520' for e in art)
        p = hyper_ge(a, len(nat) - a, c, len(art) - c)
        return fisher_line('natural heads take 520', a, len(nat), c, len(art), p), \
            p < 0.05 and a / max(1, len(nat)) > c / max(1, len(art))
    both('K2', k2)

    # K3
    say('## K3 tools and weapons stand as heads')
    TOOL = set('HIK')

    def k3(L):
        tl = tf = ol = of = 0
        for b, _ in T.names(L):
            if len(b) < 2:
                continue
            for g, where in ((b[0], 'f'), (b[-1], 'l')):
                if g not in cat:
                    continue
                if cat[g] in TOOL:
                    tl += where == 'l'
                    tf += where == 'f'
                else:
                    ol += where == 'l'
                    of += where == 'f'
        p = hyper_ge(tl, tf, ol, of)
        return fisher_line('tool tokens last (of last + first)', tl, tl + tf, ol, ol + of, p), \
            p < 0.05 and tl / max(1, tl + tf) > ol / max(1, ol + of)
    both('K3', k3)

    # K4
    say('## K4 attributes agree with the class')

    def cmi(xs, ys, zs):
        byz = defaultdict(list)
        for x, y, z in zip(xs, ys, zs):
            byz[z].append((x, y))
        n = len(xs)
        return sum(len(v) / n * T.mi([a for a, _ in v], [b for _, b in v]) for v in byz.values() if len(v) > 1)

    def k4(L):
        ns = [(b, e) for b, e in T.names(L) if len(b) >= 2]
        X, Y, Z = [b[0] for b, _ in ns], [e for _, e in ns], [b[-1] for b, _ in ns]
        obs = cmi(X, Y, Z)
        grp = defaultdict(list)
        for i, z in enumerate(Z):
            grp[z].append(i)
        ge = 0
        for _ in range(N):
            y = Y[:]
            for ii in grp.values():
                v = [y[i] for i in ii]
                random.shuffle(v)
                for i, w in zip(ii, v):
                    y[i] = w
            ge += cmi(X, y, Z) >= obs
        p = (ge + 1) / (N + 1)
        return '%d names; CMI(first; ending | last) %.4f bits; p = %.4f' % (len(ns), obs, p), p < 0.05
    both('K4', k4)

    # K5
    say('## K5 foreign names have no native title')
    wl = [ln for r in rows if r['sealid'] in west for ln in r['seq'] if len(ln) >= 2]
    hl = [ln for r in home for ln in r['seq'] if len(ln) >= 2]
    bylen = defaultdict(list)
    for ln in hl:
        bylen[len(ln)].append(ln)

    def draw(n):
        while n not in bylen:
            n -= 1
        return random.choice(bylen[n])

    def last_head(t):
        t = [g for g in t if g not in ('740', '520', '90', '400', '151')]
        return bool(t) and t[-1] in head
    obs = sum(map(last_head, wl)) / len(wl)
    null = [sum(last_head(draw(len(t))) for t in wl) / len(wl) for _ in range(N)]
    p = (sum(1 for x in null if x <= obs) + 1) / (N + 1)
    ok = p < 0.05
    say('- West Asian lines ending (before any ending sign) in a head-class sign: %.0f%% (%d lines); home draws %.0f%%; '
        'p = %.4f. **K5 %s.**' % (100 * obs, len(wl), 100 * sum(null) / N, p, T.verdict(ok)))
    say()
    res.append(('K5', ok))

    # K6
    say('## K6 a genitive on possessions')
    items = []
    for r in intact:
        k = 1 if r['type'].startswith('POT') else (0 if r['type'].startswith('SEAL') else None)
        if k is None:
            continue
        for ln in r['seq']:
            idx = [i for i, g in enumerate(ln) if g in ('740', '520')]
            if not idx or len(ln) < 2:
                continue
            st = 0 if len(ln) <= 3 else (1 if len(ln) <= 5 else 2)
            items.append((k, st, idx[-1] < len(ln) - 1))

    def stat(lab):
        num = den = 0
        for s in range(3):
            a = [o for l, (_, st, o) in zip(lab, items) if st == s and l]
            b = [o for l, (_, st, o) in zip(lab, items) if st == s and not l]
            if a and b:
                num += len(a) * (sum(a) / len(a) - sum(b) / len(b))
                den += len(a)
        return num / den if den else 0.0
    lab = [k for k, _, _ in items]
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
    p = (ge + 1) / (N + 1)
    ok = obs > 0 and p < 0.05
    pots = [o for k, _, o in items if k == 1]
    seals_ = [o for k, _, o in items if k == 0]
    say('- lines with an ending followed by another sign: pots %d of %d, seals %d of %d; stratified difference %+.1f '
        'points, p = %.4f. **K6 %s.**' % (sum(pots), len(pots), sum(seals_), len(seals_), 100 * obs, p, T.verdict(ok)))
    say()
    res.append(('K6', ok))

    # K7
    say('## K7 titles are known everywhere')
    seals = [r for r in home if r['type'].startswith('SEAL')]
    tok, sites = Counter(), defaultdict(set)
    for r in seals:
        for g in set(r['flat']):
            tok[g] += 1
            sites[g].add(r['site'].strip())
    S = [g for g in (head | attr) if tok[g] >= 5]
    q = T.quintiles(tok, S)
    lab = [g in head for g in S]
    ns = [len(sites[g]) for g in S]

    def st7(lb):
        a = [x for x, l in zip(ns, lb) if l]
        b = [x for x, l in zip(ns, lb) if not l]
        return sum(a) / len(a) - sum(b) / len(b)
    obs = st7(lab)
    grp = defaultdict(list)
    for i, g in enumerate(S):
        grp[q[g]].append(i)
    ge = 0
    for _ in range(N):
        sh = lab[:]
        for ii in grp.values():
            v = [sh[i] for i in ii]
            random.shuffle(v)
            for i, w in zip(ii, v):
                sh[i] = w
        ge += st7(sh) >= obs
    p = (ge + 1) / (N + 1)
    ok = obs > 0 and p < 0.05
    say('- signs on 5+ seals: %d heads, %d attributes; mean number of sites heads %.1f, attributes %.1f; difference %+.2f, '
        'p = %.4f. **K7 %s.**' % (sum(lab), len(S) - sum(lab), sum(x for x, l in zip(ns, lab) if l) / max(1, sum(lab)),
                                  sum(x for x, l in zip(ns, lab) if not l) / max(1, len(S) - sum(lab)), obs, p,
                                  T.verdict(ok)))
    say()
    res.append(('K7', ok))

    # K8
    say('## K8 titles last, attributes change')
    per = []
    for r in seals:
        if r['site'].strip() != 'Mohenjo-daro':
            continue
        pr = recs[r['sealid']][9].strip()
        lab_ = 'E' if pr.startswith(('Early', 'Interm')) else ('L' if pr.startswith('Late') else None)
        if not lab_:
            continue
        for ln in r['seq']:
            x = name_of(ln)
            if x and len(x[0]) >= 2:
                per.append((x[0][0], x[0][-1], lab_))

    def d8(labs):
        fe = Counter(f for (f, _, _), l in zip(per, labs) if l == 'E')
        fl = Counter(f for (f, _, _), l in zip(per, labs) if l == 'L')
        le = Counter(h for (_, h, _), l in zip(per, labs) if l == 'E')
        ll = Counter(h for (_, h, _), l in zip(per, labs) if l == 'L')
        return T.jsd(fe, fl) - T.jsd(le, ll), T.jsd(fe, fl), T.jsd(le, ll)
    labs = [l for _, _, l in per]
    obs, jf, jl = d8(labs)
    ge = 0
    sh = labs[:]
    for _ in range(N):
        random.shuffle(sh)
        ge += d8(sh)[0] >= obs
    p = (ge + 1) / (N + 1)
    ok = obs > 0 and p < 0.05
    say('- %d Mohenjo-daro seal names with a period (Early+Intermediate %d, Late %d); JSD first signs %.3f, last signs '
        '%.3f; difference %+.3f, p = %.4f. **K8 %s.**' % (len(per), labs.count('E'), labs.count('L'), jf, jl, obs, p,
                                                          T.verdict(ok)))
    say()
    res.append(('K8', ok))

    # K9
    say('## K9 grammar signs vary with distance, more sites')
    by = defaultdict(list)
    for r in home:
        by[r['site'].strip()].append(r)
    sites9 = sorted(s for s, rs in by.items() if len(rs) >= 20 and s in T.COORD)
    toks = {s: [g for r in by[s] for ln in r['seq'] for g in ln if g in T.GRAM] for s in sites9}
    m = min(len(v) for v in toks.values())
    pairs = [(i, j) for i in range(len(sites9)) for j in range(i + 1, len(sites9))]
    J = defaultdict(float)
    for _ in range(200):
        samp = {s: Counter(random.sample(toks[s], m)) for s in sites9}
        for i, j in pairs:
            J[(i, j)] += T.jsd(samp[sites9[i]], samp[sites9[j]]) / 200
    jv = [J[pp] for pp in pairs]
    rho = T.spearman(jv, [T.hav(T.COORD[sites9[i]], T.COORD[sites9[j]]) for i, j in pairs])
    ge = 0
    for _ in range(N):
        pm = list(range(len(sites9)))
        random.shuffle(pm)
        ge += T.spearman(jv, [T.hav(T.COORD[sites9[pm[i]]], T.COORD[sites9[pm[j]]]) for i, j in pairs]) >= rho
    p = (ge + 1) / (N + 1)
    ok = rho > 0 and p < 0.05
    say('- sites (20+ intact texts): %s; grammar tokens rarefied to %d; Mantel rho %.3f, p = %.4f. **K9 %s.**' % (
        ', '.join(sites9), m, rho, p, T.verdict(ok)))
    say()
    res.append(('K9', ok))

    # K10
    say('## K10 doubling marks plurality, fuller corpus')
    F = [ln for r in intact for ln in r['seq'] if len(ln) >= 2]
    T.N = N
    r10 = T.h1(F)
    o, p, D, ra, rb = r10
    ok = o > 0 and p < 0.05
    say('- F: doubled signs %s; preceded by a numeral: doubled %.1f%%, others %.1f%%; difference %+.1f points, p = %.4f. '
        '**K10 %s.**' % (', '.join(D), 100 * ra, 100 * rb, 100 * o, p, T.verdict(ok)))
    say()
    res.append(('K10', ok))

    # K11, K12
    tokall = Counter(g for t in A + B for g in t)
    comp = T.complexity(font_path, [g for g in tokall if tokall[g] >= 5])
    say('## K11 heads are drawn more elaborately')

    def k11(L):
        ns = [b for b, _ in T.names(L) if len(b) >= 2 and all(g in comp for g in b)]
        d = lambda xs: sum(comp[x[-1]] for x in xs) / len(xs) - sum(comp[x[0]] for x in xs) / len(xs)
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
        return '%d names; mean complexity last minus first %+.1f; shuffle p = %.4f' % (len(ns), obs, p), \
            obs > 0 and p < 0.05
    both('K11', k11)

    say('## K12 free signs are simpler')

    def k12(L):
        fr = freedom(L)
        tk = Counter(g for t in L for g in t)
        S = [g for g in fr if g in comp]
        xs = [math.log(tk[g]) for g in S]
        ys = [comp[g] for g in S]
        mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
        sl = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
        cres = [y - (my + sl * (x - mx)) for x, y in zip(xs, ys)]
        f = [fr[g] for g in S]
        rho = T.spearman(f, cres)
        le = 0
        cc = cres[:]
        for _ in range(N):
            random.shuffle(cc)
            le += T.spearman(f, cc) <= rho
        p = (le + 1) / (N + 1)
        return '%d signs; Spearman(freedom, complexity residual) %.3f; p = %.4f' % (len(S), rho, p), rho < 0 and p < 0.05
    both('K12', k12)

    # K13
    say('## K13 fish names are sky names')

    def k13(L):
        ns = [b for b, _ in T.names(L) if len(b) >= 2]
        fish = lambda g: g in FISH or cat.get(g) == 'Q'
        fh = [b for b in ns if fish(b[-1])]
        oh = [b for b in ns if not fish(b[-1])]
        sky = lambda b: any(cat.get(g) == 'F' for g in b[:-1])
        a, c = sum(map(sky, fh)), sum(map(sky, oh))
        p = hyper_ge(a, len(fh) - a, c, len(oh) - c)
        return fisher_line('fish-headed names with a sky sign', a, len(fh), c, len(oh), p), \
            p < 0.05 and a / max(1, len(fh)) > c / len(oh)
    both('K13', k13)

    # K14
    say('## K14 places are local')
    grp_site = lambda s: s if s in ('Mohenjo-daro', 'Harappa') else 'other'
    pres = defaultdict(set)
    for i, r in enumerate(seals):
        for g in set(r['flat']):
            pres[g].add(i)
    sg = [grp_site(r['site'].strip()) for r in seals]

    def V(g):
        a = [sg[i] for i in pres[g]]
        return T.cramer(sg, [1 if i in pres[g] else 0 for i in range(len(seals))])
    S = [g for g in pres if len(pres[g]) >= 10]
    q = T.quintiles({g: len(pres[g]) for g in S}, S)
    place = [g for g in S if cat.get(g) in ('G', 'N') and g != '861']
    Vs = {g: V(g) for g in S}
    lab = [g in place for g in S]

    def st14(lb):
        a = [Vs[g] for g, l in zip(S, lb) if l]
        b = [Vs[g] for g, l in zip(S, lb) if not l]
        return sum(a) / len(a) - sum(b) / len(b)
    obs = st14(lab)
    grp = defaultdict(list)
    for i, g in enumerate(S):
        grp[q[g]].append(i)
    ge = 0
    for _ in range(N):
        sh = lab[:]
        for ii in grp.values():
            v = [sh[i] for i in ii]
            random.shuffle(v)
            for i, w in zip(ii, v):
                sh[i] = w
        ge += st14(sh) >= obs
    p = (ge + 1) / (N + 1)
    ok = obs > 0 and p < 0.05
    say('- place signs on 10+ seals: %s; mean V %.3f against %.3f for the rest; p = %.4f. **K14 %s.**' % (
        ', '.join(place), sum(Vs[g] for g in place) / max(1, len(place)),
        sum(Vs[g] for g in S if g not in place) / (len(S) - len(place)), p, T.verdict(ok)))
    say()
    res.append(('K14', ok))

    # K15
    say('## K15 the sign after the ending is a person')

    def k15(L):
        w90 = [t[-2] for t in L if len(t) >= 3 and t[-1] == '90' and t[-2] in ('740', '520')]
        oth = [t[-2] for t in L if len(t) >= 3 and t[-1] != '90' and t[-2] in ('740', '520')] + \
              [t[-1] for t in L if t[-1] in ('740', '520')]
        a, c = w90.count('740'), oth.count('740')
        p = hyper_ge(a, len(w90) - a, c, len(oth) - c)
        return fisher_line('ending before 90 is 740', a, len(w90), c, len(oth), p), \
            p < 0.05 and a / max(1, len(w90)) > c / len(oth)
    both('K15', k15)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none', ', '.join(k for k, o in res if not o)))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test14.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
