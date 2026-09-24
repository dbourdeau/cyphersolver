"""Hundred-and-eighty-second registered prediction set (PREDICTIONS.md, SE1-SE8): decipherment loop 7, are substitutions
semantic? Substitution pairs against Fairservis's depicted categories; categories inferred for unidentified signs from
their substitution partners. Writes results/predict_test182.md."""
import csv
import os
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from noun_class import HUMAN
from predict_test179 import M
from progress import data
from signs import FISH, load

random.seed(222)
KEEP = {'A', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Q'}


def categories():
    cat = {}
    for r in csv.DictReader((l for l in open(os.path.join(R.HERE, 'keys', 'fairservis1992_raw.tsv'), encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        if r['confidence'] in ('sure', 'likely') and r['icit']:
            c = r['fcode'][:1]
            c = 'C' if c == 'D' else c
            if c in KEEP:
                cat.setdefault(r['icit'].split('|')[0], c)
    for g in FISH:
        cat[g] = 'Q'
    for g in HUMAN:
        cat[g] = 'A'
    return cat


def pairs_pos(bodies, ok):
    byl = defaultdict(list)
    for b in bodies:
        byl[len(b)].append(b)
    out = Counter()
    for L, bs in byl.items():
        for i in range(L):
            grp = defaultdict(set)
            for b in bs:
                grp[b[:i] + b[i + 1:]].add(b[i])
            for vs in grp.values():
                vs = sorted(v for v in vs if ok(v))
                for x in range(len(vs)):
                    for y in range(x + 1, len(vs)):
                        out[(vs[x], vs[y], i == L - 1)] += 1
    return out


def same_share(pp, cat, head_only=False, drop=None):
    num = den = 0
    for (a, b, h), w in pp.items():
        if head_only and not h:
            continue
        if a in cat and b in cat and not (drop and (cat[a] == drop or cat[b] == drop)):
            den += w
            num += w * (cat[a] == cat[b])
    return num / den if den else 0.0, den


def perm_test(pp, cat, n=1000, **kw):
    obs, den = same_share(pp, cat, **kw)
    keys = sorted(cat)
    vals = [cat[k] for k in keys]
    ge = 0
    mean = 0.0
    for _ in range(n):
        random.shuffle(vals)
        v, _ = same_share(pp, dict(zip(keys, vals)), **kw)
        mean += v / n
        ge += v >= obs
    return obs, mean, den, (ge + 1) / (n + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-eighty-second registered predictions: decipherment loop 7, are substitutions semantic?', 'predict_test182')
    cat = categories()
    lexf = lambda g: g not in R.NUMS and g not in M
    bodies = lambda lines: sorted({b for b, e in T.names(lines) if b})
    Bl = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    pa, pb = pairs_pos(bodies(A), lexf), pairs_pos(bodies(Bl), lexf)
    pp = pa + pb
    rd.say('- identified signs %d (%s).' % (len(cat), dict(Counter(cat.values()))))
    rd.say()
    o, m, d, p = perm_test(pp, cat)
    rd.rec('SE1', 'substitutes share a category', 'same-category %.3f against %.3f shuffled (weight %d); p = %.4f' % (o, m, d, p), p < 0.05)
    o, m, d, p = perm_test(pp, cat, drop='Q')
    rd.rec('SE2', 'without the fish series', 'same-category %.3f against %.3f (weight %d); p = %.4f' % (o, m, d, p), p < 0.05)
    o, m, d, p = perm_test(pb, cat)
    rd.rec('SE3', 'on B alone', 'same-category %.3f against %.3f (weight %d); p = %.4f' % (o, m, d, p), p < 0.05)
    hw = sum(w for (a, b, h), w in pp.items() if (cat.get(a) == 'A') != (cat.get(b) == 'A') and a in cat and b in cat) + \
        sum(w for (a, b, h), w in pp.items() if cat.get(a) == 'A' and cat.get(b) == 'A')
    ha = sum(w for (a, b, h), w in pp.items() if cat.get(a) == 'A' and cat.get(b) == 'A')
    rd.thr('SE4', 'persons substitute persons', 'pair weight with a human figure whose partner is a human figure', ha, hw, 0.3)
    o, _ = same_share(pp, cat)
    rd.rec('SE5', 'same-category pairs are common', 'same-category share %.3f; threshold 0.40' % o, o >= 0.4)
    part = defaultdict(Counter)
    for (a, b, h), w in pp.items():
        if b in cat:
            part[a][cat[b]] += w
        if a in cat:
            part[b][cat[a]] += w

    def loo(cm):
        ok = n = 0
        for g in cm:
            c = part[g]
            if sum(c.values()) >= 3:
                n += 1
                ok += c.most_common(1)[0][0] == cm[g]
        return ok / max(1, n), n
    obs, n = loo(cat)
    keys = sorted(cat)
    vals = [cat[k] for k in keys]
    sims = []
    for _ in range(1000):
        random.shuffle(vals)
        sm = dict(zip(keys, vals))
        pt = defaultdict(Counter)
        for (a, b, h), w in pp.items():
            if b in sm:
                pt[a][sm[b]] += w
            if a in sm:
                pt[b][sm[a]] += w
        ok = nn = 0
        for g in sm:
            c = pt[g]
            if sum(c.values()) >= 3:
                nn += 1
                ok += c.most_common(1)[0][0] == sm[g]
        sims.append(ok / max(1, nn))
    q95 = sorted(sims)[949]
    se6 = obs >= 0.5 and obs > q95
    rd.rec('SE6', 'partners predict the category', 'leave-one-out %.2f over %d signs; shuffled 95th percentile %.2f' % (obs, n, q95), se6)
    DL, tr, te = data()
    tot = sum(len(t) for t in DL)
    tok = Counter(g for t in DL for g in t)
    inferred = {}
    if se6:
        for g, c in part.items():
            if g not in cat and g not in R.NUMS and sum(c.values()) >= 3:
                k, v = c.most_common(1)[0]
                if v / sum(c.values()) >= 0.6:
                    inferred[g] = k
    gain = sum(tok[g] for g, k in inferred.items() if k in ('A', 'H', 'I', 'E', 'Q')) / tot
    rd.rec('SE7', 'inferred categories raise M+', 'inferred %d signs (%s); M+ gain %.1f points (classes A, H, I, E, Q only)' % (
        len(inferred), ', '.join('%s:%s' % kv for kv in sorted(inferred.items())[:20]), 100 * gain), gain >= 0.02)
    o, m, d, p = perm_test(pp, cat, head_only=True)
    rd.rec('SE8', 'head-slot substitutes share a category', 'same-category %.3f against %.3f (weight %d); p = %.4f' % (o, m, d, p), p < 0.05)
    with open(os.path.join(R.HERE, 'results', 'inferred_categories.tsv'), 'w', encoding='utf-8') as f:
        f.write('# set 182: categories inferred from substitution partners (3+ identified partner weight, 60%+ majority)\nsign\tcategory\n')
        for g, k in sorted(inferred.items()):
            f.write('%s\t%s\n' % (g, k))
    rd.finish()


if __name__ == '__main__':
    main()
