"""Three-hundred-and-thirty-third registered prediction set (PREDICTIONS.md, ST1-ST4): decipherment loop 158, the
combined referent pool (set 332: tablets, seals, tags; alpha 0.0025) with site-stratified base rates. A unit's expected
share of picture m is the mean, over its objects, of m's share among the pictured objects of the object's own site
(binomial with that mean); the FDR comes from 100 shuffles of the pictures within each site. If picture shares differ
between sites, a phrase common at one site no longer passes for a referent. Validation: the stratified figures replace
the current ones if lower. Writes results/predict_test333.md."""
import random
from collections import Counter, defaultdict

from scipy.stats import binom

import rtools as R
import referents as X
from damaged import segments
from predict_test200 import SKIP
from predict_test237 import merged
from predict_test304 import coverage, fam
from predict_test325 import FAM, SIGN
from progress import data

TABS = ('TAB:C', 'TAB:I', 'TAB:B')
SEALS = ('SEAL:S', 'SEAL:R', 'SEAL', 'SEAL:C', 'SEAL:CY', 'TAG')
ALPHA = 0.0025


def site_objects(F, recs):
    clean, frag = [], []
    for r in F:
        rec = recs.get(r['sealid'])
        if not rec or not any(rec[20].startswith(t) for t in TABS + SEALS):
            continue
        m = rec[18].split(':')[0]
        if m in SKIP or not r['flat']:
            continue
        clean.append((tuple(r['flat']), m, rec[3]))
    by = defaultdict(list)
    for s in segments(drop_copies=False):
        if any(s['type'].startswith(t) for t in TABS + SEALS) and s['motif'] not in SKIP:
            by[(s['sealid'], s['motif'], s['site'])].append(s['signs'])
    for (sid, m, site), runs in by.items():
        frag.append((tuple(x for i, run in enumerate(runs) for x in (('|',) if i else ()) + run), m, site))
    allo = clean + frag
    mg = merged([(t, m) for t, m, s in allo])
    both = [(t, m, s) for (t, m), (_, _, s) in zip(mg, allo)]
    return clean, both


def units(clean, both):
    sites = Counter(s for t, m, s in both)
    sm = defaultdict(Counter)
    for t, m, s in both:
        sm[s][m] += 1
    rate = lambda m, s: sm[s][m] / sites[s]
    u = {'texts': {}}
    g = defaultdict(list)
    for t, m, s in clean:
        g[t].append((m, s))
    for t, ms in g.items():
        if len(ms) >= 2:
            m, v = Counter(x for x, s in ms).most_common(1)[0]
            p = sum(rate(m, s) for x, s in ms) / len(ms)
            if binom.sf(v - 1, len(ms), p) < ALPHA:
                u['texts'][t] = m
    for isf in (False, True):
        for n in (FAM if isf else SIGN):
            occ, texts = defaultdict(list), defaultdict(set)
            for t, m, s in both:
                tt = fam(t) if isf else t
                for gram in X.grams_of(tt, n):
                    if '|' in gram:
                        continue
                    occ[gram].append((m, s))
                    texts[gram].add(t)
            q = {}
            for gram, ms in occ.items():
                if len(ms) < 2 or len(texts[gram]) < 2:
                    continue
                m, v = Counter(x for x, s in ms).most_common(1)[0]
                p = sum(rate(m, s) for x, s in ms) / len(ms)
                if binom.sf(v - 1, len(ms), p) < ALPHA:
                    q[gram] = m
            u[('Fmade' if isf else 'made', n)] = q
    return u


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-thirty-third registered predictions: decipherment loop 158, site-stratified base rates for the referent pool', 'predict_test333')
    DL, tr, te = data()
    clean, both = site_objects(F, recs)
    P = {'made': ([(t, m) for t, m, s in clean], [(t, m) for t, m, s in both])}
    u = units(clean, both)
    real = X.count(u)
    nb = {k: {g: m for g, m in v.items() if m != 'Bull1'} for k, v in u.items()}
    rnd = random.Random(333)
    tot = 0
    for _ in range(100):
        bys = defaultdict(list)
        for i, (t, m, s) in enumerate(both):
            bys[s].append(i)
        pics = [m for t, m, s in both]
        for s, idx in bys.items():
            vals = [pics[i] for i in idx]
            rnd.shuffle(vals)
            for i, v in zip(idx, vals):
                pics[i] = v
        sb = [(t, p, s) for (t, m, s), p in zip(both, pics)]
        cl = defaultdict(list)
        for t, m, s in clean:
            cl[s].append(m)
        for s in cl:
            rnd.shuffle(cl[s])
        it = {s: iter(v) for s, v in cl.items()}
        sc = [(t, next(it[s]), s) for t, m, s in clean]
        tot += X.count(units(sc, sb))
    fdr = tot / 100 / max(1, real)
    c, cnb = coverage(DL, P, u), coverage(DL, P, nb)
    rd.say('- %d objects in %d sites; %d units, FDR %.1f%%; coverage %.2f%% (without Bull1 units %.2f%%); current 23.77%% / 7.85%%.' % (len(both), len({s for t, m, s in both}), real, 100 * fdr, 100 * c, 100 * cnb))
    rd.say()
    rd.rec('ST1', 'site-stratified FDR <= 10%', '%.1f%%' % (100 * fdr), fdr <= 0.10)
    rd.rec('ST2', 'stratified coverage at least 23.77%', '%.2f%%' % (100 * c), c >= 0.2377)
    rd.rec('ST3', 'stratified coverage without Bull1 units at least 7.85%', '%.2f%%' % (100 * cnb), cnb >= 0.0785)
    rd.rec('ST4', 'progress rule: none (validation; lower stratified figures replace the current ones)', 'ST2 %s, ST3 %s' % (c >= 0.2377, cnb >= 0.0785), False)
    rd.finish()


if __name__ == '__main__':
    main()
