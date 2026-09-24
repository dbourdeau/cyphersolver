"""Test of the thirteenth registered prediction set (PREDICTIONS.md, H1-H10).

Samples: A = data/corpus.tsv, B = data/corpus_m77_added.tsv (lines of 2+ signs, no '?'); F = the fuller ICIT corpus.

Usage: python predict_test13.py path/to/icit_full_records_indusscript_net.csv path/to/sk_indus_script-webfont.ttf
Writes results/predict_test13.md.
"""
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations

import icit_full
from gulf import IRAN_WEST, WEST
from numerals import NUMS
from predict_test4 import name_of
from predict_test8 import bound_pairs
from signs import CRAB, EYE, FIG, FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
GRAM = {'740', '520', '817', '820', '861', '90', '400'} | set(NUMS)
random.seed(33)

COORD = {'Mohenjo-daro': (27.33, 68.14), 'Harappa': (30.63, 72.86), 'Dholavira': (23.89, 70.21),
         'Lothal': (22.52, 72.25), 'Kalibangan': (29.47, 74.13), 'Chanhu-daro': (26.17, 68.32),
         'Banawali': (29.60, 75.39), 'Rakhigarhi': (29.29, 76.11), 'Nausharo': (29.36, 67.62),
         'Allahdino': (24.85, 67.20), 'Surkotada': (23.62, 70.84), 'Lakhanjo-daro': (27.73, 68.83),
         'Farmana': (28.97, 76.30), 'Bala-kot': (25.47, 66.73)}


def say(s=''):
    OUT.append(s)
    print(s)


def verdict(ok):
    return 'holds' if ok else 'fails'


def sample(which):
    rows = load() if which == 'A' else load(only_m77=True)
    return [ln for r in rows for ln in r['seq'] if len(ln) >= 2 and '?' not in ln]


def names(lines):
    return [nm for nm in (name_of(ln) for ln in lines) if nm]


def quintiles(tok, signs):
    s = sorted(signs, key=lambda g: tok[g])
    return {g: min(4, 5 * i // len(s)) for i, g in enumerate(s)}


def ranks(v):
    o = sorted(range(len(v)), key=lambda i: v[i])
    r = [0.0] * len(v)
    i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]:
            j += 1
        for k in range(i, j + 1):
            r[o[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def spearman(a, b):
    ra, rb = ranks(a), ranks(b)
    ma, mb = sum(ra) / len(ra), sum(rb) / len(rb)
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb))
    return num / den if den else 0.0


def entropy(c):
    n = sum(c.values())
    return -sum(v / n * math.log2(v / n) for v in c.values() if v)


# ---------------------------------------------------------------- H1
def h1(lines):
    tok = Counter(g for t in lines for g in t)
    dbl = Counter(a for t in lines for a, b in zip(t, t[1:]) if a == b and a not in NUMS)
    D = {g for g, c in dbl.items() if c >= 2}
    S = [g for g in tok if tok[g] >= 20 and g not in NUMS]
    pre = Counter(b for t in lines for a, b in zip(t, t[1:]) if a in NUMS)
    rate = {g: pre[g] / tok[g] for g in S}
    q = quintiles(tok, S)
    lab = [g in D for g in S]
    if sum(lab) < 3:
        return None

    def stat(lb):
        a = [rate[g] for g, l in zip(S, lb) if l]
        b = [rate[g] for g, l in zip(S, lb) if not l]
        return sum(a) / len(a) - sum(b) / len(b)
    obs = stat(lab)
    idx = defaultdict(list)
    for i, g in enumerate(S):
        idx[q[g]].append(i)
    ge = 0
    for _ in range(N):
        sh = lab[:]
        for ii in idx.values():
            v = [sh[i] for i in ii]
            random.shuffle(v)
            for i, w in zip(ii, v):
                sh[i] = w
        ge += stat(sh) >= obs
    return obs, (ge + 1) / (N + 1), sorted((g for g in S if g in D), key=lambda g: -tok[g]), \
        sum(rate[g] for g in S if g in D) / sum(lab), sum(rate[g] for g in S if g not in D) / (len(S) - sum(lab))


# ---------------------------------------------------------------- H2
def h2(lines, bound):
    c = Counter((a, b) for t in lines for a, b in zip(t, t[1:]) if a != b)
    P = [p for p, v in c.items() if v >= 10]
    r = [c[(p[1], p[0])] / c[p] for p in P]
    lab = [p in bound for p in P]
    rk = ranks(r)

    def stat(lb):
        a = [x for x, l in zip(rk, lb) if l]
        b = [x for x, l in zip(rk, lb) if not l]
        return sum(a) / len(a) - sum(b) / len(b)
    obs = stat(lab)
    le = 0
    for _ in range(N):
        random.shuffle(lab)
        le += stat(lab) <= obs
    lab = [p in bound for p in P]
    return obs, (le + 1) / (N + 1), sum(lab), len(P), \
        sum(x for x, l in zip(r, lab) if l) / sum(lab), sum(x for x, l in zip(r, lab) if not l) / (len(P) - sum(lab))


# ---------------------------------------------------------------- H3
FAMILIES = {'fish': FISH, 'jar': {'740', '741', '742', '745'}, 'fig': FIG, 'crab': CRAB, 'eye': EYE}


def contexts(lines):
    L, R = defaultdict(Counter), defaultdict(Counter)
    for t in lines:
        s = ['^'] + t + ['$']
        for i in range(1, len(s) - 1):
            L[s[i]][s[i - 1]] += 1
            R[s[i]][s[i + 1]] += 1
    vec = {}
    for side, M in (('L', L), ('R', R)):
        tot = sum(sum(c.values()) for c in M.values())
        col = Counter()
        for c in M.values():
            col.update(c)
        for g, c in M.items():
            rs = sum(c.values())
            for k, v in c.items():
                p = math.log(v * tot / (rs * col[k]))
                if p > 0:
                    vec.setdefault(g, {})[(side, k)] = p
    return vec


def cos(a, b):
    if not a or not b:
        return 0.0
    num = sum(v * b.get(k, 0) for k, v in a.items())
    return num / math.sqrt(sum(v * v for v in a.values()) * sum(v * v for v in b.values()))


def h3(lines):
    tok = Counter(g for t in lines for g in t)
    vec = contexts(lines)
    S = [g for g in tok if tok[g] >= 10]
    q = quintiles(tok, S)
    byq = defaultdict(list)
    for g in S:
        byq[q[g]].append(g)
    fam = {}
    for f, ss in FAMILIES.items():
        for g in ss:
            fam[g] = f
    pairs = [(a, b) for f, ss in FAMILIES.items() for a, b in combinations(sorted(g for g in ss if g in q), 2)]
    if not pairs:
        return None
    obs = sum(cos(vec.get(a), vec.get(b)) for a, b in pairs) / len(pairs)
    ge = 0
    for _ in range(N):
        tot = 0
        for a, b in pairs:
            while True:
                c, d = random.choice(byq[q[a]]), random.choice(byq[q[b]])
                if c != d and not (c in fam and fam.get(c) == fam.get(d)):
                    break
            tot += cos(vec.get(c), vec.get(d))
        ge += tot / len(pairs) >= obs
    return obs, (ge + 1) / (N + 1), len(pairs)


# ---------------------------------------------------------------- H4
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(h))


def jsd(p, q):
    ks = set(p) | set(q)
    np_, nq = sum(p.values()), sum(q.values())
    d = 0.0
    for k in ks:
        a, b = p.get(k, 0) / np_, q.get(k, 0) / nq
        m = (a + b) / 2
        if a:
            d += 0.5 * a * math.log2(a / m)
        if b:
            d += 0.5 * b * math.log2(b / m)
    return d


def h4(home):
    by = defaultdict(list)
    for r in home:
        by[r['site'].strip()].append(r)
    sites = sorted(s for s, rs in by.items() if len(rs) >= 40 and s in COORD)
    res = {}
    for lab, keep in (('name signs', lambda g: g not in GRAM), ('grammar signs', lambda g: g in GRAM)):
        toks = {s: [g for r in by[s] for ln in r['seq'] for g in ln if keep(g)] for s in sites}
        m = min(len(v) for v in toks.values())
        pairs = list(combinations(range(len(sites)), 2))
        J = defaultdict(float)
        for _ in range(200):
            samp = {s: Counter(random.sample(toks[s], m)) for s in sites}
            for i, j in pairs:
                J[(i, j)] += jsd(samp[sites[i]], samp[sites[j]]) / 200
        dist = [hav(COORD[sites[i]], COORD[sites[j]]) for i, j in pairs]
        jv = [J[p] for p in pairs]
        rho = spearman(jv, dist)
        ge = 0
        for _ in range(N):
            perm = list(range(len(sites)))
            random.shuffle(perm)
            dp = [hav(COORD[sites[perm[i]]], COORD[sites[perm[j]]]) for i, j in pairs]
            ge += spearman(jv, dp) >= rho
        res[lab] = (rho, (ge + 1) / (N + 1), m)
    return sites, res


# ---------------------------------------------------------------- H5
def complexity(font_path, signs):
    from PIL import Image, ImageDraw, ImageFont
    cps = {}
    for ln in open(os.path.join(HERE, 'data', 'glyphs.tsv'), encoding='utf-8'):
        p = ln.rstrip('\n').split('\t')
        if len(p) == 2 and p[1] and p[0] != 'glyph':
            cps[p[0]] = ''.join(chr(int(x, 16)) for x in p[1].split())
    font = ImageFont.truetype(font_path, 120)
    out = {}
    for g in signs:
        if g not in cps:
            continue
        im = Image.new('L', (220, 220), 0)
        ImageDraw.Draw(im).text((30, 20), cps[g], font=font, fill=255)
        px = im.load()
        ink = [(x, y) for x in range(220) for y in range(220) if px[x, y] > 127]
        if len(ink) < 20:
            continue
        s = set(ink)
        per = sum(1 for x, y in ink if any((x + dx, y + dy) not in s for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))))
        out[g] = per * per / len(ink)
    return out


def h5(lines, comp):
    tok = Counter(g for t in lines for g in t)
    S = [g for g in comp if tok[g] >= 5]
    a, b = [comp[g] for g in S], [math.log(tok[g]) for g in S]
    rho = spearman(a, b)
    le = 0
    bb = b[:]
    for _ in range(N):
        random.shuffle(bb)
        le += spearman(a, bb) <= rho
    return rho, (le + 1) / (N + 1), len(S)


# ---------------------------------------------------------------- H6
def h6(objs):
    items = []
    for r in objs:
        k = 1 if r['type'].startswith(('TAB', 'TAG')) else (0 if r['type'].startswith('SEAL') else None)
        n = len(r['flat'])
        if k is None or n < 3:
            continue
        st = 0 if n <= 4 else (1 if n <= 6 else 2)
        items.append((k, st, sum(g in ('740', '520') for g in r['flat']) >= 2))

    def stat(lab):
        num = den = 0
        for s in range(3):
            a = [o for (l, (_, st, o)) in zip(lab, items) if st == s and l]
            b = [o for (l, (_, st, o)) in zip(lab, items) if st == s and not l]
            if a and b:
                num += len(a) * (sum(a) / len(a) - sum(b) / len(b))
                den += len(a)
        return num / den
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
    rates = [(s, sum(o for k, st, o in items if st == s and k), sum(1 for k, st, _ in items if st == s and k),
              sum(o for k, st, o in items if st == s and not k), sum(1 for k, st, _ in items if st == s and not k))
             for s in range(3)]
    return obs, (ge + 1) / (N + 1), rates


# ---------------------------------------------------------------- H7
def h7(lines):
    ns = set(names(lines))
    b = c = both = neither = 0
    for body, end in ns:
        if len(body) < 3:
            continue
        suf = (body[1:], end) in ns
        pre = any((body[:-1], e) in ns for e in ('740', '520'))
        b += suf and not pre
        c += pre and not suf
        both += suf and pre
        neither += not suf and not pre
    n = b + c
    p = sum(math.comb(n, k) for k in range(b, n + 1)) / 2 ** n if n else 1.0
    return b, c, both, neither, p


# ---------------------------------------------------------------- H8
def mi(xs, ys):
    n = len(xs)
    cx, cy, cxy = Counter(xs), Counter(ys), Counter(zip(xs, ys))
    return sum(v / n * math.log2(v * n / (cx[x] * cy[y])) for (x, y), v in cxy.items())


def h8(home):
    nm = []
    for r in home:
        for ln in r['seq']:
            x = name_of(ln)
            if x and len(x[0]) >= 2:
                nm.append((x[0][0], x[0][-1], r['site'].strip()))
    sc = Counter(s for _, _, s in nm)
    nm = [(f, l, s if sc[s] >= 20 else 'other') for f, l, s in nm]
    F, L, S = [x[0] for x in nm], [x[1] for x in nm], [x[2] for x in nm]
    obs = mi(F, S) - mi(L, S)
    ge = 0
    ss = S[:]
    for _ in range(N):
        random.shuffle(ss)
        ge += mi(F, ss) - mi(L, ss) >= obs
    return obs, (ge + 1) / (N + 1), len(nm), mi(F, S), mi(L, S)


# ---------------------------------------------------------------- H9
def cramer(a, b):
    n = len(a)
    ca, cb, cab = Counter(a), Counter(b), Counter(zip(a, b))
    chi = 0.0
    for x in ca:
        for y in cb:
            e = ca[x] * cb[y] / n
            chi += (cab[(x, y)] - e) ** 2 / e
    k = min(len(ca), len(cb)) - 1
    return math.sqrt(chi / (n * k)) if k > 0 else 0.0


def h9(home):
    txt = open(os.path.join(HERE, 'results', 'allographs.md'), encoding='utf-8').read()
    line = [ln for ln in txt.splitlines() if 'candidate variant pairs' in ln][0]
    vp = re.findall(r'(\d+)~(\d+)', line)
    site_of = lambda s: s if s in ('Mohenjo-daro', 'Harappa') else 'other'
    occ = defaultdict(list)
    for r in home:
        for ln in r['seq']:
            for g in ln:
                occ[g].append(site_of(r['site'].strip()))

    cnt = {g: Counter(v) for g, v in occ.items()}

    def v(a, b):
        ca, cb = cnt[a], cnt[b]
        na, nb = sum(ca.values()), sum(cb.values())
        n = na + nb
        chi = 0.0
        for s in set(ca) | set(cb):
            col = ca[s] + cb[s]
            for obs_, row in ((ca[s], na), (cb[s], nb)):
                e = row * col / n
                chi += (obs_ - e) ** 2 / e
        k = min(2, len(set(ca) | set(cb))) - 1
        return math.sqrt(chi / (n * k)) if k > 0 else 0.0
    pairs = [(a, b) for a, b in vp if len(occ[a]) >= 10 and len(occ[b]) >= 10]
    obs = sum(v(a, b) for a, b in pairs) / len(pairs)
    S = [g for g in occ if len(occ[g]) >= 10]
    tk = {g: len(occ[g]) for g in S}
    q = quintiles(tk, S)
    byq = defaultdict(list)
    for g in S:
        byq[q[g]].append(g)
    ge = 0
    for _ in range(N):
        tot = 0
        for a, b in pairs:
            while True:
                c, d = random.choice(byq[q[a]]), random.choice(byq[q[b]])
                if c != d:
                    break
            tot += v(c, d)
        ge += tot / len(pairs) >= obs
    return obs, (ge + 1) / (N + 1), pairs


# ---------------------------------------------------------------- H10
def h10(lines):
    ns = [b for b, _ in names(lines) if len(b) >= 2]
    d = lambda xs: entropy(Counter(x[0] for x in xs)) - entropy(Counter(x[-1] for x in xs))
    obs = d(ns)
    ge = 0
    for _ in range(N):
        sh = []
        for b in ns:
            b = list(b)
            random.shuffle(b)
            sh.append(b)
        ge += d(sh) >= obs
    return obs, (ge + 1) / (N + 1), len(ns), entropy(Counter(x[0] for x in ns)), entropy(Counter(x[-1] for x in ns))


def main(path, font_path):
    A, B = sample('A'), sample('B')
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = {r['sealid'] for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST}
    home = [r for r in rows if r['sealid'] not in west and recs[r['sealid']][2] not in ('Other',)]
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    say('# Thirteenth registered predictions: ten hypotheses')
    say()
    say('- samples: A %d lines, B %d lines; F %d intact home objects.' % (len(A), len(B), len(home)))
    say()
    summary = []

    say('## H1 doubling means plurality')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        r = h1(L)
        if r is None:
            say('- %s: fewer than 3 doubled signs with 20+ tokens; not testable.' % lab)
            ok = False
            continue
        o, p, D, ra, rb = r
        ok = ok and o > 0 and p < 0.05
        say('- %s: doubled signs %s; preceded by a numeral: doubled %.1f%%, others %.1f%%; difference %+.1f points, '
            'p = %.4f.' % (lab, ', '.join(D), 100 * ra, 100 * rb, 100 * o, p))
    say('- **H1 %s.**' % verdict(ok))
    summary.append(('H1', ok))
    say()

    say('## H2 compounds have a fixed order')
    bound = bound_pairs(path)
    ok = True
    for lab, L in (('A', A), ('B', B)):
        o, p, nb, npr, rb, ro = h2(L, bound)
        ok = ok and o < 0 and p < 0.05
        say('- %s: %d pairs with count 10+, %d bound; mean reversal ratio bound %.3f, others %.3f; rank difference '
            '%+.1f, p = %.4f.' % (lab, npr, nb, rb, ro, o, p))
    say('- **H2 %s.**' % verdict(ok))
    summary.append(('H2', ok))
    say()

    say('## H3 diacritics keep the word class')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        r = h3(L)
        o, p, n = r
        ok = ok and p < 0.05
        say('- %s: %d family pairs; mean context cosine %.3f; p = %.4f.' % (lab, n, o, p))
    say('- **H3 %s.**' % verdict(ok))
    summary.append(('H3', ok))
    say()

    say('## H4 name signs vary with distance, grammar does not')
    sites, res = h4(home)
    nr, npv, nm_ = res['name signs']
    gr, gp, gm_ = res['grammar signs']
    ok = nr > 0 and npv < 0.05 and gr < nr
    say('- sites (40+ intact texts, with coordinates): %s.' % ', '.join(sites))
    say('- name signs (rarefied to %d tokens): Mantel rho %.3f, p = %.4f; grammar signs (rarefied to %d): rho %.3f, '
        'p = %.4f.' % (nm_, nr, npv, gm_, gr, gp))
    say('- **H4 %s.**' % verdict(ok))
    summary.append(('H4', ok))
    say()

    say('## H5 frequent signs are simpler')
    tokall = Counter(g for t in A + B for g in t)
    comp = complexity(font_path, [g for g in tokall if tokall[g] >= 5])
    ok = True
    for lab, L in (('A', A), ('B', B)):
        rho, p, n = h5(L, comp)
        ok = ok and rho < 0 and p < 0.05
        say('- %s: %d signs; Spearman(complexity, log tokens) %.3f; p = %.4f.' % (lab, n, rho, p))
    say('- **H5 %s.**' % verdict(ok))
    summary.append(('H5', ok))
    say()

    say('## H6 tablets and sealings name two parties')
    o, p, rates = h6(intact)
    ok = o > 0 and p < 0.05
    for s, a, na, b, nb in rates:
        say('- length %s: tablets + sealings with 2+ endings %d of %d; seals %d of %d.' % (
            ('3-4', '5-6', '7+')[s], a, na, b, nb))
    say('- stratified difference %+.1f points, p = %.4f. **H6 %s.**' % (100 * o, p, verdict(ok)))
    summary.append(('H6', ok))
    say()

    say('## H7 names are built head-final from shorter names')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        b, c, both, nei, p = h7(L)
        ok = ok and b > c and p < 0.05
        say('- %s: minus first sign attested only %d, minus last sign only %d, both %d, neither %d; McNemar one-sided '
            'p = %.4f.' % (lab, b, c, both, nei, p))
    say('- **H7 %s.**' % verdict(ok))
    summary.append(('H7', ok))
    say()

    say('## H8 attributes are local, heads general')
    o, p, n, mf, ml = h8(home)
    ok = o > 0 and p < 0.05
    say('- %d names; MI(first sign, site) %.3f bits, MI(last sign, site) %.3f; difference %+.3f, permutation p = %.4f. '
        '**H8 %s.**' % (n, mf, ml, o, p, verdict(ok)))
    summary.append(('H8', ok))
    say()

    say('## H9 graphic variants are local habits')
    o, p, pairs = h9(home)
    ok = p < 0.05
    say('- variant pairs with 10+ tokens each: %d (%s); mean Cramer V %.3f; p = %.4f. **H9 %s.**' % (
        len(pairs), ', '.join('%s~%s' % x for x in pairs), o, p, verdict(ok)))
    summary.append(('H9', ok))
    say()

    say('## H10 heads come from a smaller inventory')
    ok = True
    for lab, L in (('A', A), ('B', B)):
        o, p, n, hf, hl = h10(L)
        ok = ok and o > 0 and p < 0.05
        say('- %s: %d names; entropy first sign %.2f bits, last sign %.2f; difference %+.2f, shuffle p = %.4f.' % (
            lab, n, hf, hl, o, p))
    say('- **H10 %s.**' % verdict(ok))
    summary.append(('H10', ok))
    say()

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(h for h, o in summary if o) or 'none',
                                   ', '.join(h for h, o in summary if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test13.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
