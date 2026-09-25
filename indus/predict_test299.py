"""Two-hundred-and-ninety-ninth registered prediction set (PREDICTIONS.md, XS1-XS3): decipherment loop 124, referents
across sites. Moulded tablets (TAB:B, clean texts and fragment runs) of Harappa and of Mohenjo-daro: units (set 294's
kinds and criterion) learned on one city's tablets predict the pictures of the other city's (both directions; copies of
a text excluded). Correct predictions against 200 shuffles of the pictures within the learning city.
Writes results/predict_test299.md."""
import random
from collections import Counter, defaultdict

import rtools as R
import referents as X
from damaged import segments
from predict_test200 import SKIP
from predict_test237 import merged
from predict_test294 import K, S, grams


def city_objects(F, recs, city):
    out = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and rec[20].startswith('TAB:B') and rec[3] == city:
            m = rec[18].split(':')[0]
            if m not in SKIP and r['flat']:
                out.append((tuple(r['flat']), m))
    by = defaultdict(list)
    for s in segments(drop_copies=False):
        if s['type'].startswith('TAB:B') and s['site'] == city and s['motif'] not in SKIP:
            by[(s['sealid'], s['motif'])].append(s['signs'])
    out += [(tuple(x for i, run in enumerate(runs) for x in (('|',) if i else ()) + run), m) for (sid, m), runs in by.items()]
    return out


def predict(learn, test):
    occ = defaultdict(list)
    for t, m in learn:
        for g in grams(t):
            occ[g].append((t, m))
    hits = n = 0
    for t, m in test:
        v = Counter()
        for g in grams(t):
            rest = [(u, x) for u, x in occ.get(g, []) if u != t]
            if len(rest) < K or len({u for u, x in rest}) < 2:
                continue
            lab = X.ok([x for u, x in rest], K, S)
            if lab:
                v[lab] += 1
        if v:
            n += 1
            hits += sorted(v.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] == m
    return hits, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-ninety-ninth registered predictions: decipherment loop 124, referents across sites', 'predict_test299')
    H = merged(city_objects(F, recs, 'Harappa'))
    M = merged(city_objects(F, recs, 'Mohenjo-daro'))
    rnd = random.Random(299)
    res = {}
    for lab, learn, test in (('Harappa -> Mohenjo-daro', H, M), ('Mohenjo-daro -> Harappa', M, H)):
        h, n = predict(learn, test)
        null = []
        for _ in range(200):
            pics = [m for t, m in learn]
            rnd.shuffle(pics)
            null.append(predict(list(zip([t for t, m in learn], pics)), test)[0])
        med = sorted(null)[100]
        p = (1 + sum(x >= h for x in null)) / 201
        res[lab] = (h, n, med, p)
        rd.say('- %s: %d correct of %d predicted (learning %d objects, test %d); shuffles median %d; p = %.3f.' % (lab, h, n, len(learn), len(test), med, p))
    rd.say()
    a, b = res['Harappa -> Mohenjo-daro'], res['Mohenjo-daro -> Harappa']
    rd.rec('XS1', 'Harappa -> Mohenjo-daro above the shuffles (p < 0.05)', '%d vs median %d, p = %.3f' % (a[0], a[2], a[3]), a[3] < 0.05)
    rd.rec('XS2', 'Mohenjo-daro -> Harappa above the shuffles (p < 0.05)', '%d vs median %d, p = %.3f' % (b[0], b[2], b[3]), b[3] < 0.05)
    rd.rec('XS3', 'progress rule: XS1 and XS2 (referents travel between cities; tier 3 cross-site line)', 'XS1 %s, XS2 %s' % (a[3] < 0.05, b[3] < 0.05), a[3] < 0.05 and b[3] < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
