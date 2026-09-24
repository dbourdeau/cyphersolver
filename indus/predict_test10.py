"""Test of the tenth registered prediction set (PREDICTIONS.md, Hypothesis AA): is the sign that one name adds to
another a free (sound) sign, standing at the end of the word?

AA1  freedom of the added sign against the other signs of the longer name (paired permutation).
AA2  the added sign is the name's last sign, against each pair's 1 / length (exact Poisson-binomial tail).

Usage: python predict_test10.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test10.md.
"""
import math
import os
import random
import sys
from collections import Counter, defaultdict

import icit_full
from gulf import IRAN_WEST, WEST
from numerals import NUMS
from predict_test4 import name_of

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N_PERM = 10000
random.seed(30)


def say(s=''):
    OUT.append(s)
    print(s)


def freedom(path):
    """As predict_test8 Y2: residual of log(distinct left/right neighbours) on log(tokens), home lines, 5+ tokens."""
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = {r['sealid'] for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST}
    hl = [ln for r in rows if r['sealid'] not in west and recs[r['sealid']][2] not in ('Other',)
          for ln in r['seq'] if len(ln) >= 2]
    tok = Counter(g for t in hl for g in t)
    nb = defaultdict(set)
    for t in hl:
        for a, b in zip(t, t[1:]):
            nb[a].add(('R', b))
            nb[b].add(('L', a))
    sg = [g for g in tok if tok[g] >= 5]
    xs = [math.log(tok[g]) for g in sg]
    ys = [math.log(max(1, len(nb[g]))) for g in sg]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return {g: y - (my + slope * (x - mx)) for g, x, y in zip(sg, xs, ys)}


def main(path):
    free = freedom(path)
    names = set()
    for r in icit_full.objects(path):
        if not r['flat'] or '?' in r['flat']:
            continue
        if any(ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw']):
            continue
        nm = name_of(r['flat'])
        if nm:
            names.add(nm)
    pairs = []
    for body, end in names:
        if len(body) < 2:
            continue
        hits = defaultdict(list)
        for i in range(len(body)):
            s = body[:i] + body[i + 1:]
            if (s, end) in names:
                hits[s].append(i)
        for s, pos in hits.items():
            if len(pos) == 1:
                pairs.append((body, end, pos[0]))
    say('# Tenth registered predictions: optional signs, freedom and position')
    say()
    say('- distinct names: %d; insertion pairs (unambiguous position): %d.' % (len(names), len(pairs)))
    added = Counter(b[i] for b, _, i in pairs)
    say('- commonest added signs: %s.' % ', '.join('%s x%d (freedom %s)' % (g, c, '%+.2f' % free[g] if g in free else '-')
                                                  for g, c in added.most_common(15)))
    say()

    # AA1
    usable = []
    for b, e, i in pairs:
        ok = lambda g: g in free and g not in NUMS
        if not ok(b[i]):
            continue
        others = [free[g] for j, g in enumerate(b) if j != i and ok(g)]
        if others:
            usable.append((free[b[i]], others))
    obs = sum(a - sum(o) / len(o) for a, o in usable) / len(usable)
    ge = 0
    for _ in range(N_PERM):
        tot = 0
        for a, o in usable:
            allv = [a] + o
            k = random.randrange(len(allv))
            rest = allv[:k] + allv[k + 1:]
            tot += allv[k] - sum(rest) / len(rest)
        if tot / len(usable) >= obs:
            ge += 1
    p1 = (ge + 1) / (N_PERM + 1)
    say('## AA1 the optional sign is free')
    say()
    say('- pairs with a scored added sign and another scored sign: %d. Mean freedom, added sign minus the rest of the '
        'name: %+.3f; paired permutation p = %.4f. **AA1 %s.**' % (len(usable), obs, p1,
                                                                   'holds' if obs > 0 and p1 < 0.05 else 'fails'))
    say('- mean freedom of added signs %+.3f; of the other signs of the same names %+.3f.' % (
        sum(a for a, _ in usable) / len(usable), sum(sum(o) / len(o) for _, o in usable) / len(usable)))
    say()

    # AA2
    k = sum(1 for b, _, i in pairs if i == len(b) - 1)
    ps = [1 / len(b) for b, _, _ in pairs]
    dist = [1.0]
    for p in ps:
        nd = [0.0] * (len(dist) + 1)
        for j, v in enumerate(dist):
            nd[j] += v * (1 - p)
            nd[j + 1] += v * p
        dist = nd
    p2 = sum(dist[k:])
    pos = Counter('first' if i == 0 else ('last' if i == len(b) - 1 else 'inside') for b, _, i in pairs)
    say('## AA2 it stands at the end of the word')
    say()
    say('- added sign last: %d of %d (%.0f%%); expected from position alone %.1f (%.0f%%); first %d, inside %d; exact '
        'p = %.4f. **AA2 %s.**' % (k, len(pairs), 100 * k / len(pairs), sum(ps), 100 * sum(ps) / len(pairs),
                                   pos['first'], pos['inside'], p2, 'holds' if p2 < 0.05 else 'fails'))
    say()
    say('**Hypothesis AA %s.**' % ('holds' if obs > 0 and p1 < 0.05 and p2 < 0.05 else 'fails'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test10.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
