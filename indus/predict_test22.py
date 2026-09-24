"""Test of the twenty-second registered prediction set (PREDICTIONS.md, Q1-Q15): classes of the content signs.

Usage: python predict_test22.py path/to/icit_full_records_indusscript_net.csv path/to/sk_indus_script-webfont.ttf
       path/to/linb
Writes results/predict_test22.md.
"""
import math
import os
import random
import sys
from collections import Counter, defaultdict
from itertools import combinations

import numpy as np

import icit_full
import predict_test13 as T
from gulf import IRAN_WEST, WEST
from numerals import NUMS
from predict_test11 import linb_lines
from predict_test14 import cat_of, classes

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
GRAMMAR = {'740', '520', '90', '400', '151', '817', '820', '861', '2'}
FORMULA = {'705', '706', '33'}
random.seed(42)


def say(s=''):
    OUT.append(s)
    print(s)


def cluster(lines, signs, k=8, seed=42, dims=20):
    ctx = sorted({g for t in lines for g in t} | {'^', '$'})
    ci = {g: i for i, g in enumerate(ctx)}
    si = {g: i for i, g in enumerate(signs)}
    L = np.zeros((len(signs), len(ctx)))
    R = np.zeros((len(signs), len(ctx)))
    for t in lines:
        s = ['^'] + list(t) + ['$']
        for i in range(1, len(s) - 1):
            if s[i] in si:
                L[si[s[i]], ci[s[i - 1]]] += 1
                R[si[s[i]], ci[s[i + 1]]] += 1

    def ppmi(M):
        tot = M.sum()
        rs, cs = M.sum(1, keepdims=True), M.sum(0, keepdims=True)
        with np.errstate(divide='ignore', invalid='ignore'):
            p = np.log(M * tot / (rs * cs))
        p[~np.isfinite(p)] = 0
        p = np.maximum(p, 0)
        return p / (np.linalg.norm(p, axis=1, keepdims=True) + 1e-12)
    X = np.hstack([ppmi(L), ppmi(R)])
    U, S, _ = np.linalg.svd(X, full_matrices=False)
    d = min(dims, len(signs) - 1)
    Z = U[:, :d] * S[:d]
    Z = Z / (np.linalg.norm(Z, axis=1, keepdims=True) + 1e-12)
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(50):
        C = Z[rng.choice(len(Z), k, replace=False)]
        for _ in range(200):
            lab = ((Z[:, None, :] - C[None]) ** 2).sum(2).argmin(1)
            newC = np.array([Z[lab == j].mean(0) if (lab == j).any() else C[j] for j in range(k)])
            if np.allclose(newC, C):
                break
            C = newC
        inert = ((Z - C[lab]) ** 2).sum()
        if best is None or inert < best[0]:
            best = (inert, lab.copy())
    return {g: int(best[1][i]) for g, i in si.items()}


def perm_labels(lab, signs):
    v = [lab[g] for g in signs]
    random.shuffle(v)
    return dict(zip(signs, v))


def main(path, font_path, linb):
    A, B = T.sample('A'), T.sample('B')
    cat = cat_of()
    head, _ = classes(A)
    tokA = Counter(g for t in A for g in t)
    tokB = Counter(g for t in B for g in t)
    content = sorted((g for g in tokA if tokA[g] >= 10 and g not in NUMS and g not in GRAMMAR and g not in FORMULA),
                     key=int)
    lab = cluster(A, content)
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    say('# Twenty-second registered predictions: classes of the content signs')
    say()
    say('- content signs clustered (A, 10+ tokens): %d.' % len(content))
    for c in range(8):
        mem = sorted((g for g in content if lab[g] == c), key=lambda g: -tokA[g])
        say('  - cluster %d (%d signs, %d tokens): %s' % (c, len(mem), sum(tokA[g] for g in mem), ', '.join(
            '%s%s' % (g, '(' + cat[g] + ')' if g in cat else '') for g in mem[:18])))
    say()

    # Q1
    say('## Q1 validation: numerals cluster together')
    nums = sorted(g for g in tokA if tokA[g] >= 10 and g in NUMS)
    lab1 = cluster(A, content + nums)
    allp = list(combinations(content + nums, 2))
    base = sum(lab1[a] == lab1[b] for a, b in allp) / len(allp)
    nump = list(combinations(nums, 2))
    rate = sum(lab1[a] == lab1[b] for a, b in nump) / len(nump)
    say('- numerals clustered: %d; same-cluster rate for numeral pairs %.2f, for all pairs %.2f; ratio %.1f; threshold 3.' % (
        len(nums), rate, base, rate / base))
    rec_('Q1', rate / base >= 3)

    # Q2
    say('## Q2 validation: Linear B sign kinds cluster together')
    ll = linb_lines(linb)
    kinds = {}
    for t in ll:
        for k_, s in t:
            kinds.setdefault(s, k_)
    lines_b = [[s for _, s in t] for t in ll]
    tl = Counter(s for t in lines_b for s in t)
    lb_signs = sorted(s for s in tl if tl[s] >= 10 and kinds[s] in ('syl', 'word'))
    labL = cluster(lines_b, lb_signs)
    pairs = [(a, b) for a, b in combinations(lb_signs, 2) if labL[a] == labL[b]]
    kk = [kinds[s] for s in lb_signs]
    km = dict(zip(lb_signs, kk))
    obs = sum(km[a] == km[b] for a, b in pairs) / len(pairs)
    ge = 0
    for _ in range(N):
        random.shuffle(kk)
        km2 = dict(zip(lb_signs, kk))
        ge += sum(km2[a] == km2[b] for a, b in pairs) / len(pairs) >= obs
    p = (ge + 1) / (N + 1)
    say('- Linear B signs: %d (%d syllabograms, %d word signs); same-kind share of same-cluster pairs %.2f; p = %.4f.' % (
        len(lb_signs), sum(kinds[s] == 'syl' for s in lb_signs), sum(kinds[s] == 'word' for s in lb_signs), obs, p))
    rec_('Q2', p < 0.05)

    # Q3
    say('## Q3 A clusters predict B contexts')
    vecB = T.contexts(B)
    sb = [g for g in content if tokB[g] >= 10 and g in vecB]
    cosm = {(a, b): T.cos(vecB[a], vecB[b]) for a, b in combinations(sb, 2)}

    def st3(l_):
        s_ = [v for (a, b), v in cosm.items() if l_[a] == l_[b]]
        d_ = [v for (a, b), v in cosm.items() if l_[a] != l_[b]]
        return sum(s_) / len(s_) - sum(d_) / len(d_)
    obs = st3(lab)
    ge = sum(st3(perm_labels(lab, sb)) >= obs for _ in range(N))
    p = (ge + 1) / (N + 1)
    say('- signs with 10+ tokens in B: %d; B-context cosine same cluster minus different %+.3f; p = %.4f.' % (len(sb), obs, p))
    rec_('Q3', obs > 0 and p < 0.05)

    # Q12
    say('## Q12 a clustering of B agrees with A')
    contentB = sorted((g for g in tokB if tokB[g] >= 10 and g not in NUMS and g not in GRAMMAR and g not in FORMULA),
                      key=int)
    labB = cluster(B, contentB)
    both = [g for g in contentB if g in lab]
    pr = list(combinations(both, 2))
    obs = sum(lab[a] == lab[b] and labB[a] == labB[b] for a, b in pr)
    ge = 0
    for _ in range(N):
        l2 = perm_labels(labB, both)
        ge += sum(lab[a] == lab[b] and l2[a] == l2[b] for a, b in pr) >= obs
    p = (ge + 1) / (N + 1)
    say('- signs clustered in both: %d; pairs together in both %d; p = %.4f.' % (len(both), obs, p))
    rec_('Q12', p < 0.05)

    # Q4, Q14, Q5
    namesB = T.names(B)
    toks = [(g, 'last' if i == len(b) - 1 else ('first' if i == 0 else 'inside'))
            for b, _ in namesB for i, g in enumerate(b) if g in lab]

    def mi_pos(l_):
        return T.mi([l_[g] for g, _ in toks], [w for _, w in toks])
    say('## Q4 clusters differ in position in B')
    obs = mi_pos(lab)
    ge = sum(mi_pos(perm_labels(lab, content)) >= obs for _ in range(N))
    p = (ge + 1) / (N + 1)
    say('- B name tokens in A clusters: %d; MI(cluster; position) %.3f bits; p = %.4f.' % (len(toks), obs, p))
    rec_('Q4', p < 0.05)
    say('## Q14 clusters have a dominant position')
    dom = 0
    for c in range(8):
        cc = Counter(w for g, w in toks if lab[g] == c)
        n_ = sum(cc.values())
        if n_:
            w, v = cc.most_common(1)[0]
            dom += v / n_ >= 0.6
            say('  - cluster %d: %s' % (c, ', '.join('%s %.0f%%' % (x, 100 * y / n_) for x, y in cc.most_common())))
    say('- clusters with 60%%+ of tokens in one position: %d of 8; threshold 4.' % dom)
    rec_('Q14', dom >= 4)
    say('## Q5 clusters differ in the ending')
    ends = [(b[-1], e) for b, e in namesB if b[-1] in lab]

    def mi_end(l_):
        return T.mi([l_[g] for g, _ in ends], [e for _, e in ends])
    obs = mi_end(lab)
    ge = sum(mi_end(perm_labels(lab, content)) >= obs for _ in range(N))
    p = (ge + 1) / (N + 1)
    say('- B names with a clustered last sign: %d; MI(cluster; ending) %.3f bits; p = %.4f.' % (len(ends), obs, p))
    rec_('Q5', p < 0.05)

    # Q13
    say('## Q13 coverage of B')
    known = set(NUMS) | GRAMMAR | FORMULA | set(lab)
    k_ = sum(tokB[g] for g in tokB if g in known)
    say('- B tokens covered: %d of %d (%.1f%%); threshold 70%%.' % (k_, sum(tokB.values()), 100 * k_ / sum(tokB.values())))
    rec_('Q13', k_ / sum(tokB.values()) >= 0.7)

    # Q6, Q7, Q15
    catd = [g for g in content if g in cat]
    say('## Q6 clusters and picture categories')

    def mi_cat(l_):
        return T.mi([l_[g] for g in catd], [cat[g] for g in catd])
    obs = mi_cat(lab)
    ge = sum(mi_cat(perm_labels(lab, catd)) >= obs for _ in range(N))
    p = (ge + 1) / (N + 1)
    say('- categorised content signs: %d; MI %.3f bits; p = %.4f.' % (len(catd), obs, p))
    rec_('Q6', p < 0.05)
    say('## Q7 human figures cluster together')
    hum = [g for g in catd if cat[g] == 'A']
    hp = list(combinations(hum, 2))

    def st7(l_):
        return sum(l_[a] == l_[b] for a, b in hp) / max(1, len(hp))
    obs = st7(lab)
    ge = sum(st7(perm_labels(lab, catd)) >= obs for _ in range(N))
    p = (ge + 1) / (N + 1)
    say('- human-figure signs clustered: %s; same-cluster share of their pairs %.2f; p = %.4f.' % (
        ', '.join('%s:%d' % (g, lab[g]) for g in hum), obs, p))
    rec_('Q7', p < 0.05)
    say('## Q15 heads are concentrated')
    hs = [g for g in head if g in lab]
    cc = Counter(lab[g] for g in hs)
    top = cc.most_common(1)[0]
    say('- head-class signs clustered: %d; largest share in one cluster %d (cluster %d, %.0f%%); threshold 50%%.' % (
        len(hs), top[1], top[0], 100 * top[1] / len(hs)))
    rec_('Q15', top[1] / len(hs) >= 0.5)

    # F-based: Q8, Q9, Q11
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = {r['sealid'] for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST}

    def obj_mi(units, name):
        labs_ = [u for u, _ in units]
        cl = [Counter(lab[g] for g in toks_ if g in lab) for _, toks_ in units]

        def mi_(l_):
            xs, ys = [], []
            for x, c in zip(l_, cl):
                for y, n_ in c.items():
                    xs += [x] * n_
                    ys += [y] * n_
            return T.mi(xs, ys)
        obs = mi_(labs_)
        ge = 0
        sh = labs_[:]
        for _ in range(N // 10):
            random.shuffle(sh)
            ge += mi_(sh) >= obs
        p = (ge + 1) / (N // 10 + 1)
        say('- %s: units %d; MI %.4f bits; p = %.4f (1,000 permutations: token lists per unit).' % (name, len(units), obs, p))
        return p
    say('## Q8 seals and tablets use different clusters')
    u = [(r['type'].split(':')[0], r['flat']) for r in rows if r['type'].startswith(('SEAL', 'TAB'))]
    rec_('Q8', obj_mi(u, 'seals and tablets') < 0.05)
    say('## Q9 Mohenjo-daro and Harappa seals use different clusters')
    u = [(r['site'].strip(), r['flat']) for r in rows if r['type'].startswith('SEAL')
         and r['site'].strip() in ('Mohenjo-daro', 'Harappa')]
    rec_('Q9', obj_mi(u, 'Mohenjo-daro and Harappa seals') < 0.05)
    say('## Q11 foreign texts use different clusters')
    u = [('west' if r['sealid'] in west else 'home', ln) for r in rows for ln in r['seq']]
    rec_('Q11', obj_mi(u, 'West Asian and home lines') < 0.05)

    # Q10
    say('## Q10 clusters differ in graphic complexity')
    comp = T.complexity(font_path, content)
    cs = [g for g in content if g in comp]

    def bvar(l_):
        m = sum(comp[g] for g in cs) / len(cs)
        by = defaultdict(list)
        for g in cs:
            by[l_[g]].append(comp[g])
        return sum(len(v) * (sum(v) / len(v) - m) ** 2 for v in by.values())
    obs = bvar(lab)
    ge = sum(bvar(perm_labels(lab, cs)) >= obs for _ in range(N))
    p = (ge + 1) / (N + 1)
    say('- signs with a glyph: %d; between-cluster variance of complexity %.0f; p = %.4f.' % (len(cs), obs, p))
    rec_('Q10', p < 0.05)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test22.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
