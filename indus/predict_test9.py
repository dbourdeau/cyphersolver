"""Test of the ninth registered prediction set (PREDICTIONS.md, Hypothesis Z): do Harappa tablets with the same text
lie in the same level? Also the power check for the fifth set (seal names).

Z1  same-text pairs sharing a level (HARP 3B / 3C; Vats Strata I-VI), against levels shuffled within the scheme.
Z2  same-text pairs' median depth difference, against depths shuffled.
The same statistics for Harappa seals with the same name, for comparison.

Usage: python predict_test9.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test9.md.
"""
import os
import random
import statistics
import sys
from collections import Counter, defaultdict
from itertools import combinations

import icit_full
from predict_test4 import name_of

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N_PERM = 10000
random.seed(29)


def say(s=''):
    OUT.append(s)
    print(s)


def level(rec):
    f = rec[10].strip()
    if rec[9].strip() == '3' and f in ('B', 'C'):
        return ('HARP', f)
    if f.startswith('Stratum '):
        return ('Vats', f)
    return None


def items(path, kind):
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    out = []
    for r in icit_full.objects(path):
        if r['site'].strip() != 'Harappa' or not r['type'].startswith(kind) or not r['flat'] or '?' in r['flat']:
            continue
        if any(ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw']):
            continue
        if kind == 'TAB':
            key = tuple(r['flat'])
        else:
            key = name_of(r['flat'])
            if not key:
                continue
        out.append({'key': key, 'level': level(recs[r['sealid']]), 'depth': r['depth']})
    return out


def pairs(xs):
    by = defaultdict(list)
    for i, x in enumerate(xs):
        by[x['key']].append(i)
    return [p for v in by.values() if len(v) >= 2 for p in combinations(v, 2)]


def level_test(xs):
    xs = [x for x in xs if x['level']]
    pr = [(i, j) for i, j in pairs(xs) if xs[i]['level'][0] == xs[j]['level'][0]]
    if not pr:
        return None
    lab = [x['level'] for x in xs]
    obs = sum(lab[i] == lab[j] for i, j in pr) / len(pr)
    sch = defaultdict(list)
    for i, x in enumerate(xs):
        sch[x['level'][0]].append(i)
    null = []
    for _ in range(N_PERM):
        sh = lab[:]
        for idx in sch.values():
            v = [sh[i] for i in idx]
            random.shuffle(v)
            for i, w in zip(idx, v):
                sh[i] = w
        null.append(sum(sh[i] == sh[j] for i, j in pr) / len(pr))
    p = (sum(1 for x in null if x >= obs) + 1) / (N_PERM + 1)
    return len(xs), Counter(x['level'] for x in xs), len(pr), len({xs[i]['key'] for i, _ in pr}), obs, \
        sum(null) / N_PERM, p


def depth_test(xs):
    xs = [x for x in xs if x['depth'] is not None]
    pr = pairs(xs)
    if not pr:
        return None
    d = [x['depth'] for x in xs]
    obs = statistics.median(abs(d[i] - d[j]) for i, j in pr)
    null = []
    for _ in range(N_PERM):
        sh = d[:]
        random.shuffle(sh)
        null.append(statistics.median(abs(sh[i] - sh[j]) for i, j in pr))
    p = (sum(1 for x in null if x <= obs) + 1) / (N_PERM + 1)
    return len(xs), len(pr), len({xs[i]['key'] for i, _ in pr}), obs, sum(null) / N_PERM, p


def main(path):
    say('# Ninth registered predictions: do Harappa tablets with the same text lie in the same level?')
    say()
    res = {}
    for kind, lab in (('TAB', 'tablets (same full text)'), ('SEAL', 'seals (same name), comparison')):
        xs = items(path, kind)
        say('## Harappa %s' % lab)
        say()
        say('- intact objects: %d.' % len(xs))
        lt = level_test(xs)
        if lt:
            n, lv, npr, nk, obs, nul, p = lt
            say('- level: %d objects with a level (%s); same-text pairs within a scheme: %d from %d texts; same level '
                '%.0f%%, shuffled %.0f%%; p = %.4f.' % (n, ', '.join('%s %s %d' % (a, b, c) for (a, b), c in
                                                              sorted(lv.items())), npr, nk, 100 * obs, 100 * nul, p))
        dt = depth_test(xs)
        if dt:
            n, npr, nk, obs, nul, p2 = dt
            say('- depth: %d objects with a depth; same-text pairs: %d from %d texts; median difference %.1f, '
                'shuffled %.1f; p = %.4f.' % (n, npr, nk, obs, nul, p2))
        res[kind] = (lt, dt)
        say()
    lt, dt = res['TAB']
    z1 = lt and lt[-1] < 0.05
    z2 = dt and dt[-1] < 0.05
    say('**Z1 %s. Z2 %s. Hypothesis Z %s.**' % ('holds' if z1 else 'fails', 'holds' if z2 else 'fails',
                                                'holds' if z1 and z2 else 'fails'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test9.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
