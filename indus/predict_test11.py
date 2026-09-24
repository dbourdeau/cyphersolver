"""Test of the eleventh registered prediction set (PREDICTIONS.md): replications of X2 and Y2 and a Linear B control.

RB   M77-added multi-line texts: bound-pair gaps against other gaps as line breaks (Fisher), lines as listed and reversed.
RF1  freedom from home seals against freedom from home tablets (Spearman, permutation).
RF2  West Asian tokens against length-matched home draws, freedom computed from the M77-added texts only.
RC   Linear B (DAMOS): freedom of syllabograms against word signs (rank test, permutation).

Usage: python predict_test11.py path/to/icit_full_records_indusscript_net.csv path/to/linb
Writes results/predict_test11.md.
"""
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

import icit_full
from gulf import IRAN_WEST, WEST
from predict_test7 import fisher_less
from predict_test8 import bound_pairs
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N_PERM = 10000
LEAVE = {'740', '520', '817', '820', '861'}
random.seed(31)


def say(s=''):
    OUT.append(s)
    print(s)


def freedom(lines, min_tok=5):
    tok = Counter(g for t in lines for g in t)
    nb = defaultdict(set)
    for t in lines:
        for a, b in zip(t, t[1:]):
            nb[a].add(('R', b))
            nb[b].add(('L', a))
    sg = [g for g in tok if tok[g] >= min_tok]
    xs = [math.log(tok[g]) for g in sg]
    ys = [math.log(max(1, len(nb[g]))) for g in sg]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return {g: y - (my + slope * (x - mx)) for g, x, y in zip(sg, xs, ys)}


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
    return num / math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb))


def split_test(texts, bound):
    a = b = c = d = 0
    for lines in texts:
        t, brk = [], set()
        for ln in lines:
            if t:
                brk.add(len(t))
            t.extend(ln)
        for g in range(1, len(t)):
            inb, isb = (t[g - 1], t[g]) in bound, g in brk
            if inb:
                a += isb
                b += not isb
            else:
                c += isb
                d += not isb
    return a, a + b, c, c + d, fisher_less(a, b, c, d)


def linb_lines(d):
    out = []
    for ln in open(os.path.join(d, 'corpus_damos_lines.txt'), encoding='utf-8'):
        parts = ln.rstrip('\n').split('\t')
        if len(parts) < 3:
            continue
        cur = []
        for tok in parts[2].split():
            if tok.isdigit():
                cur.append(('N', 'N'))
            elif re.match(r'^[a-z0-9*]+(-[a-z0-9*]+)*$', tok) and re.search(r'[a-z]', tok) or \
                    re.match(r'^\*\d+(-[a-z0-9*]+)+$', tok):
                cur.extend(('syl', s) for s in tok.split('-'))
            elif re.match(r'^[A-Z*][A-Za-z0-9*+/]*$', tok):
                cur.append(('word', tok))
            else:
                if len(cur) >= 2:
                    out.append(cur)
                cur = []
        if len(cur) >= 2:
            out.append(cur)
    return out


def main(path, linb):
    say('# Eleventh registered predictions: replications and a Linear B control')
    say()
    bound = bound_pairs(path)

    # RB
    m77 = [r['seq'] for r in load(only_m77=True) if len(r['seq']) >= 2 and not any('?' in ln for ln in r['seq'])]
    say('## RB bound pairs on the M77 texts')
    say()
    ok = True
    for lab, texts in (('lines as listed', m77), ('lines reversed', [t[::-1] for t in m77])):
        a, na, c, nc, p = split_test(texts, bound)
        ok = ok and p < 0.05 and a / max(1, na) < c / nc
        say('- %s: %d multi-line texts; bound-pair gaps broken %d of %d (%.1f%%), other gaps %d of %d (%.1f%%); '
            'Fisher one-sided p = %.4f.' % (lab, len(texts), a, na, 100 * a / max(1, na), c, nc, 100 * c / nc, p))
    say('- **RB %s.**' % ('holds' if ok else 'fails'))
    say()

    # RF1
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = {r['sealid'] for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST}
    home = [r for r in rows if r['sealid'] not in west and recs[r['sealid']][2] not in ('Other',)]
    lines_of = lambda rs: [ln for r in rs for ln in r['seq'] if len(ln) >= 2]
    fs = freedom(lines_of([r for r in home if r['type'].startswith('SEAL')]))
    ft = freedom(lines_of([r for r in home if r['type'].startswith('TAB')]))
    common = sorted(set(fs) & set(ft))
    rho = spearman([fs[g] for g in common], [ft[g] for g in common])
    ge = 0
    vt = [ft[g] for g in common]
    for _ in range(N_PERM):
        random.shuffle(vt)
        if spearman([fs[g] for g in common], vt) >= rho:
            ge += 1
    p = (ge + 1) / (N_PERM + 1)
    say('## RF1 freedom from seals against freedom from tablets')
    say()
    say('- signs with 5+ tokens in both: %d; Spearman rho = %.3f; permutation p = %.4f. **RF1 %s.**' % (
        len(common), rho, p, 'holds' if rho > 0 and p < 0.05 else 'fails'))
    say()

    # RF2
    fm = freedom([ln for r in load(only_m77=True) for ln in r['seq'] if len(ln) >= 2 and '?' not in ln])
    wl = [ln for r in rows if r['sealid'] in west for ln in r['seq'] if len(ln) >= 2]
    hl = lines_of(home)
    bylen = defaultdict(list)
    for ln in hl:
        bylen[len(ln)].append(ln)

    def draw(n):
        while n not in bylen:
            n -= 1
        return random.choice(bylen[n])

    def fmean(lines):
        v = [fm[g] for t in lines for g in t if g in fm and g not in LEAVE]
        return sum(v) / len(v), len(v)
    obs, nw = fmean(wl)
    null = [fmean([draw(len(t)) for t in wl])[0] for _ in range(N_PERM)]
    p2 = (sum(1 for x in null if x >= obs) + 1) / (N_PERM + 1)
    say('## RF2 West Asian texts, freedom from the M77 texts only')
    say()
    say('- signs scored from M77: %d; West Asian tokens scored: %d. Mean freedom West Asian %+.3f, home draws %+.3f '
        '(5-95%%: %+.3f to %+.3f); p = %.4f. **RF2 %s.**' % (len(fm), nw, obs, sum(null) / N_PERM,
                                                          sorted(null)[N_PERM // 20], sorted(null)[-N_PERM // 20], p2,
                                                          'holds' if p2 < 0.05 else 'fails'))
    say()

    # RC
    ll = linb_lines(linb)
    fl = freedom([[s for _, s in t] for t in ll])
    kind = {}
    for t in ll:
        for k, s in t:
            kind.setdefault(s, k)
    syl = [fl[s] for s in fl if kind[s] == 'syl']
    wrd = [fl[s] for s in fl if kind[s] == 'word']

    def mean_rank_diff(a, b):
        r = ranks(a + b)
        return sum(r[:len(a)]) / len(a) - sum(r[len(a):]) / len(b)
    obs3 = mean_rank_diff(syl, wrd)
    allv = syl + wrd
    ge = 0
    for _ in range(N_PERM):
        random.shuffle(allv)
        if mean_rank_diff(allv[:len(syl)], allv[len(syl):]) >= obs3:
            ge += 1
    p3 = (ge + 1) / (N_PERM + 1)
    auc = sum(1 for x in syl for y in wrd if x > y) / (len(syl) * len(wrd))
    say('## RC Linear B control')
    say()
    say('- Linear B lines (dividers removed): %d; sign types with 5+ tokens: %d syllabograms, %d word signs '
        '(numerals as N left out of the comparison).' % (len(ll), len(syl), len(wrd)))
    say('- mean freedom syllabograms %+.3f, word signs %+.3f; AUC %.2f; permutation p = %.4f. **RC %s.**' % (
        sum(syl) / len(syl), sum(wrd) / len(wrd), auc, p3, 'holds' if p3 < 0.05 and auc > 0.5 else 'fails'))
    top = sorted(fl, key=lambda s: -fl[s])
    say('- freest 15: %s.' % ', '.join('%s (%s)' % (s, kind[s][0]) for s in top[:15]))
    say('- least free 15: %s.' % ', '.join('%s (%s)' % (s, kind[s][0]) for s in top[-15:]))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test11.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
