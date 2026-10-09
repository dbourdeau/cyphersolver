"""Accuracy of dec.py output (dec_out/<page>.txt) against the hand reading (high/medium lines, tokens without '?'),
binned by the per-token margin."""
import sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dec
tag = sys.argv[1] if len(sys.argv) > 1 else ''
bins = [(-99, 1), (1, 2), (2, 3), (3, 4), (4, 6), (6, 99)]
acc = collections.defaultdict(lambda: [0, 0])
for pg in dec.PAGES:
    t = open('dec_out/%s%s.txt' % (pg, tag), encoding='utf8').read().splitlines()
    de = [x for l in t if l.startswith('dec:') for x in l.split()[1:]]
    mg = [float(x) for l in t if l.startswith('marg:') for x in l.split()[1:]]
    ct, rd, pairs = dec.page_pairs(pg)
    assert len(de) == len(ct), (pg, len(de), len(ct))
    for r, h, conf, bi, i in pairs:
        if conf not in ('high', 'medium') or '?' in h or h not in dec.KEY: continue
        k = de[i]; ok = k != '-' and dec.VAL[k] == dec.VAL[h]
        for a, b in bins:
            if a <= mg[i] < b: acc[(a, b)][0] += ok; acc[(a, b)][1] += 1
for (a, b), (o, n) in sorted(acc.items()):
    print('margin %3g-%-3g  %3d/%3d = %.0f%%' % (a, b, o, n, 100 * o / max(1, n)))
