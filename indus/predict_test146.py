"""Hundred-and-forty-sixth registered prediction set (PREDICTIONS.md, WS1-WS9): scribal workshops. Graphic variant
pairs (results/allographs.md) and CISI allograph features (cisi.py) against find spot, level, medium and object.
Writes results/predict_test146.md."""
import os
import random
import re
from collections import Counter, defaultdict
from itertools import combinations

import cisi
import predict_test13 as T
import rtools as R
from predict_test18 import level

random.seed(166)
N = 2000
GENERIC = ('DK-', 'HR-', 'VS-', 'DKG', '--', '')


def pairs_list():
    s = open(os.path.join(R.HERE, 'results', 'allographs.md'), encoding='utf-8').read()
    ln = [x for x in s.splitlines() if x.startswith('- candidate variant pairs')][0]
    return re.findall(r'(\d+)~(\d+) \(', ln)


def pooled(tokens, place, strat=lambda t: 0):
    """tokens: dicts with 'pair', 'var'. Sum over pairs of MI(var, place); permute var within (pair, strat)."""
    tk = [t for t in tokens if place(t) is not None]
    by = defaultdict(list)
    for i, t in enumerate(tk):
        by[t['pair']].append(i)

    def stat(v):
        return sum(T.mi([v[i] for i in ix], [place(tk[i]) for i in ix]) for ix in by.values() if len(ix) >= 2)
    v = [t['var'] for t in tk]
    obs = stat(v)
    grp = defaultdict(list)
    for i, t in enumerate(tk):
        grp[(t['pair'], strat(t))].append(i)
    ge = 0
    for _ in range(N):
        w = list(v)
        for ix in grp.values():
            x = [w[i] for i in ix]
            random.shuffle(x)
            for i, y in zip(ix, x):
                w[i] = y
        ge += stat(w) >= obs
    return obs, (ge + 1) / (N + 1), len(tk), len([1 for ix in by.values() if len(ix) >= 2])


def agree_perm(tokens, same, eligible):
    """Share of eligible token pairs (same pair id) with the same variant, among pairs where same() is true, minus
    among those where it is false (or against 0 if every pair is 'same'); permute var within pair."""
    by = defaultdict(list)
    for i, t in enumerate(tokens):
        by[t['pair']].append(i)
    prs = [(i, j, same(tokens[i], tokens[j])) for ix in by.values() for i, j in combinations(ix, 2) if eligible(tokens[i], tokens[j])]

    def stat(v):
        a = [v[i] == v[j] for i, j, s in prs if s]
        c = [v[i] == v[j] for i, j, s in prs if not s]
        return sum(a) / max(1, len(a)) - sum(c) / max(1, len(c)), len(a), len(c)
    v = [t['var'] for t in tokens]
    obs, na, nc = stat(v)
    ge = 0
    for _ in range(N):
        w = list(v)
        for ix in by.values():
            x = [w[i] for i in ix]
            random.shuffle(x)
            for i, y in zip(ix, x):
                w[i] = y
        ge += stat(w)[0] >= obs
    return obs, (ge + 1) / (N + 1), na, nc


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-forty-sixth registered predictions: scribal workshops', 'predict_test146')
    cnt = Counter(g for r in F for g in r['flat'])
    prs = [(a, b) for a, b in pairs_list() if cnt[a] >= 5 and cnt[b] >= 5]
    pid = {}
    for k, (a, b) in enumerate(prs):
        pid.setdefault(a, (k, 0))
        pid.setdefault(b, (k, 1))
    toks = []
    for r in F:
        rc = recs[r['sealid']]
        sub = rc[4].strip() if rc[4].strip() not in GENERIC else None
        f5 = rc[5].strip()
        for g in r['flat']:
            if g in pid:
                toks.append({'pair': pid[g][0], 'var': pid[g][1], 'obj': r['sealid'], 'site': rc[3], 'sub': sub,
                             'house': (sub, f5) if sub and re.search(r'[IVX]+$', f5) else None, 'lv': level(rc[3], rc),
                             'type': 'seal' if r['type'].startswith('SEAL') else ('tablet' if r['type'].startswith('TAB') else 'other'),
                             'text': tuple(pid.get(x, (x,))[0] if x in pid else x for x in r['flat'])})
    rd.say('- variant pairs with 5+ tokens a side in F: %d (%s); tokens %d.' % (len(prs), ', '.join('%s~%s' % p for p in prs), len(toks)))
    rd.say()

    def rep(key, title, res):
        o, p, n, k = res
        rd.rec(key, title, 'tokens %d in %d pairs; summed MI %.4f bits; p = %.4f' % (n, k, o, p), p < 0.05)
    md = [t for t in toks if t['site'] == 'Mohenjo-daro']
    rep('WS1', 'variants by Mohenjo-daro sub-area', pooled(md, lambda t: t['sub']))
    hp = [t for t in toks if t['site'] == 'Harappa']
    hsub = {r['sealid']: recs[r['sealid']][4].strip() for r in F}
    rep('WS2', 'variants by Harappa unit', pooled(hp, lambda t: hsub[t['obj']] if hsub[t['obj']] not in ('--', '') else None))
    mh = [t for t in md if t['house']]
    o, p, na, nc = agree_perm(mh, lambda a, b: a['house'] == b['house'], lambda a, b: a['sub'] == b['sub'] and a['obj'] != b['obj'])
    rd.rec('WS3', 'a house writes one variant', 'same-house token pairs %d, same sub-area other house %d; agreement difference %+.3f; p = %.4f' % (na, nc, o, p), o > 0 and p < 0.05)
    rep('WS4', 'variants by level', pooled(toks, lambda t: t['lv'], strat=lambda t: t['site']))
    rep('WS5', 'variants by medium', pooled(toks, lambda t: t['type']))
    o, p, na, nc = agree_perm(toks, lambda a, b: a['obj'] == b['obj'], lambda a, b: True)
    rd.rec('WS6', 'one object, one variant', 'same-object token pairs %d, other pairs %d; agreement difference %+.3f; p = %.4f' % (na, nc, o, p), o > 0 and p < 0.05)
    o, p, na, nc = agree_perm(toks, lambda a, b: a['text'] == b['text'], lambda a, b: a['obj'] != b['obj'])
    rd.rec('WS7', 'same text, same variant', 'token pairs on different objects with the same text %d, other %d; agreement difference %+.3f; p = %.4f' % (na, nc, o, p), o > 0 and p < 0.05)
    # CISI allograph features
    C = cisi.load()
    byno = {}
    for k, rec in recs.items():
        byno.setdefault(rec[1].strip(), rec)
    ct = []
    for side, ob in C.items():
        rec = byno.get(cisi.cisi_no(side))
        sub = rec[4].strip() if rec and rec[4].strip() not in GENERIC else None
        for ln, fl in zip(ob['seq'], ob['feat']):
            for g, f in zip(ln, fl):
                if f != '-' and g != 'P000':
                    ct.append({'pair': g, 'var': f, 'obj': cisi.cisi_no(side), 'sub': sub})
    c10 = Counter(t['pair'] for t in ct if t['sub'])
    ct8 = [t for t in ct if c10[t['pair']] >= 10 and len({x['var'] for x in ct if x['pair'] == t['pair']}) >= 2]
    rep('WS8', 'CISI allographs by sub-area', pooled(ct8, lambda t: t['sub']))
    ctv = [t for t in ct if len({x['var'] for x in ct if x['pair'] == t['pair']}) >= 2]
    o, p, na, nc = agree_perm(ctv, lambda a, b: a['obj'] == b['obj'], lambda a, b: True)
    rd.rec('WS9', 'CISI: one object, one allograph', 'same-object token pairs %d, other pairs %d; agreement difference %+.3f; p = %.4f' % (na, nc, o, p), o > 0 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
