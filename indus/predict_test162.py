"""Hundred-and-sixty-second registered prediction set (PREDICTIONS.md, MX1-MX10): the office + name reading, further
checks. Writes results/predict_test162.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test140 import GENERIC, pair_perm
from predict_test144 import strat_diff
from predict_test157 import kind, profile
from predict_test161 import CITIES, motif, shared_openers, zmi
from predict_test18 import level
from signs import load

random.seed(182)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-sixty-second registered predictions: the office + name reading, further checks', 'predict_test162')
    SO = shared_openers(F, recs)
    seals = [r for r in F if r['type'].startswith('SEAL')]
    n3 = lambda r: [(b, e) for b, e in R.names_in(r) if b and len(b) >= 3]
    bym = defaultdict(list)
    for r in seals:
        m = motif(recs, r)
        if m and m != 'None':
            for b, e in n3(r):
                bym['unicorn' if m.startswith('Bull1') else m].append(b[0])
    rare = {m: v for m, v in bym.items() if m != 'unicorn' and len(v) >= 10}
    top = lambda v: Counter(v).most_common(1)[0][1] / len(v)
    mr = sum(top(v) for v in rare.values()) / max(1, len(rare))
    k = min(len(v) for v in rare.values()) if rare else 0
    win = sum(mr > top(random.sample(bym['unicorn'], k)) for _ in range(1000)) if rare else 0
    rd.thr('MX1', 'rare motifs concentrate openers', 'draws where rare motifs (%s; mean top share %.2f) beat the unicorn at size %d' % (
        ', '.join('%s %d' % (m, len(v)) for m, v in rare.items()), mr, k), win, 1000, 0.95)
    rows = [r for r in load(only_m77=True) if r['site'] in CITIES]
    cat = {'opener': {c: Counter() for c in CITIES}, 'core': {c: Counter() for c in CITIES}}
    for r in rows:
        for b, e in {x for x in R.names_in(r) if x[0] and len(x[0]) >= 3}:
            cat['opener'][r['site']][b[0]] += 1
            cat['core'][r['site']][(b[1:], e)] += 1
    po, pc = profile(cat['opener']), profile(cat['core'])
    rd.rec('MX2', 'B: openers title-like', '%s; %.2f, %.2f, %.2f -> %s' % (po['n'], po['ratio'], po['shared'], po['one'], kind(po)), kind(po) == 'title-like')
    rd.rec('MX3', 'B: cores person-like', '%s; %.2f, %.2f, %.2f -> %s' % (pc['n'], pc['ratio'], pc['shared'], pc['one'], kind(pc)), kind(pc) == 'person-like')
    mt = [b[0] for r in F if recs[r['sealid']][3] == 'Harappa' and r['type'] in ('TAB:B', 'TAB:I') for b, e in n3(r)]
    rd.thr('MX4', 'tablet openers are the shared ones', 'openers of 3+-sign names on Harappa moulded tablets', sum(o in SO for o in mt), len(mt), 0.5)
    ne = [(b, e) for r in seals for b, e in n3(r)]
    zh, _ = zmi([b[-1] for b, e in ne], [e for b, e in ne])
    zo, _ = zmi([b[0] for b, e in ne], [e for b, e in ne])
    rd.rec('MX5', 'the head sets the ending', 'names %d; head z %.2f, opener z %.2f' % (len(ne), zh, zo), zh > zo)
    size = lambda r: float(recs[r['sealid']][31]) if recs[r['sealid']][31].replace('.', '', 1).isdigit() and float(recs[r['sealid']][31]) > 0 else None
    a = [size(r) for r in seals if n3(r) and size(r) and any(b[0] in SO for b, e in n3(r))]
    c = [size(r) for r in seals if n3(r) and size(r) and not any(b[0] in SO for b, e in n3(r))]
    rd.rank('MX6', 'office seals are larger', 'seal size (mm), shared-opener against other-opener seals', a, c)
    om = {c_: defaultdict(Counter) for c_ in CITIES}
    for r in seals:
        c_ = recs[r['sealid']][3]
        m = motif(recs, r)
        if c_ in CITIES and m:
            for b, e in n3(r):
                if b[0] in SO:
                    om[c_][b[0]][m] += 1
    both = [o for o in SO if om[CITIES[0]][o] and om[CITIES[1]][o]]
    same = sum(om[CITIES[0]][o].most_common(1)[0][0] == om[CITIES[1]][o].most_common(1)[0][0] for o in both)
    rd.thr('MX7', 'one office, one emblem in both cities', 'shared openers with the same commonest motif in both cities', same, len(both), 0.6)
    tags = [b[0] in SO for r in F if r['type'].startswith('TAG') for b, e in n3(r)]
    sl = [b[0] in SO for r in seals for b, e in n3(r)]
    rd.gtl('MX8', 'sealings carry the office', 'shared opener, tag names', tags, sl)
    items = [(b[0], recs[r['sealid']][4].strip()) for r in seals if recs[r['sealid']][3] == 'Mohenjo-daro' and recs[r['sealid']][4].strip() not in GENERIC
             for b, e in n3(r) if b[0] in SO]
    o, ex, p, n = pair_perm(items)
    rd.rec('MX9', 'one office, one quarter', 'pairs %d; same sub-area %.3f against %.3f; p = %.4f' % (n, o, ex, p), o > ex and p < 0.05)
    it = []
    for r in seals:
        c_ = recs[r['sealid']][3]
        l_ = level(c_, recs[r['sealid']]) if c_ in CITIES else None
        if l_:
            for b, e in n3(r):
                it.append((c_, l_, b[0] in SO))
    d, p = strat_diff(it)
    rd.rec('MX10', 'the office share changes over time', 'names %d; late minus early %+.3f; p = %.4f (two-sided)' % (len(it), d, p), p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
