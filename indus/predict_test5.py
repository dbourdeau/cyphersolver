"""Test of the fifth registered prediction set (PREDICTIONS.md, Hypothesis V): do seals with the same name come from
the same level of a site?

V1  same-site pairs of same-name seals: share in the same excavators' period against periods shuffled within site.
V2  Mohenjo-daro same-name pairs: median depth difference against depths shuffled within the site.

Usage: python predict_test5.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test5.md.
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
random.seed(25)


def say(s=''):
    OUT.append(s)
    print(s)


def period(site, rec):
    if site == 'Mohenjo-daro':
        p = rec[9].strip()
        for k in ('Early', 'Interm', 'Late'):
            if p.startswith(k):
                return k
    if site == 'Harappa' and rec[9].strip() == '3':
        return {'B': 'B', 'B?': 'B', 'C': 'C'}.get(rec[10].strip())
    return None


def seals_of(path):
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    out = []
    for r in icit_full.objects(path):
        if not r['type'].startswith('SEAL') or not r['flat']:
            continue
        if any(ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw']):
            continue
        nm = name_of(r['flat'])
        if nm:
            site = r['site'].strip()
            out.append({'id': r['sealid'], 'name': nm, 'site': site, 'period': period(site, recs[r['sealid']]),
                        'depth': r['depth']})
    return out


def pairs(items):
    by = defaultdict(list)
    for i, s in enumerate(items):
        by[(s['site'], s['name'])].append(i)
    return [p for v in by.values() if len(v) >= 2 for p in combinations(v, 2)]


def main(path):
    seals = seals_of(path)
    say('# Fifth registered predictions: do seals with the same name come from the same level?')
    say()

    # V1
    ps = [s for s in seals if s['period']]
    pr = pairs(ps)
    lab = [s['period'] for s in ps]
    obs = sum(lab[i] == lab[j] for i, j in pr) / len(pr)
    bysite = defaultdict(list)
    for i, s in enumerate(ps):
        bysite[s['site']].append(i)
    null = []
    for _ in range(N_PERM):
        sh = lab[:]
        for idx in bysite.values():
            vals = [sh[i] for i in idx]
            random.shuffle(vals)
            for i, v in zip(idx, vals):
                sh[i] = v
        null.append(sum(sh[i] == sh[j] for i, j in pr) / len(pr))
    p1 = (sum(1 for x in null if x >= obs) + 1) / (N_PERM + 1)
    say('## V1 period')
    say()
    say('- seals with a name and a known period: %d (%s); same-name same-site pairs: %d, from %d names.' % (
        len(ps), ', '.join('%s %s %d' % (k[0], k[1], v) for k, v in sorted(Counter((s['site'], s['period']) for s in ps).items())),
        len(pr), len({ps[i]['name'] for i, _ in pr} )))
    for i, j in pr:
        say('  - %s+%s: %s %s (%s) / %s (%s)' % ('-'.join(ps[i]['name'][0]), ps[i]['name'][1], ps[i]['site'],
                                               ps[i]['period'], ps[i]['id'], ps[j]['period'], ps[j]['id']))
    say('- same period: %.0f%% of pairs (%d of %d); shuffled within site: %.0f%% (5-95%%: %.0f-%.0f%%); p = %.4f. **V1 %s.**'
        % (100 * obs, round(obs * len(pr)), len(pr), 100 * statistics.mean(null),
           100 * sorted(null)[N_PERM // 20], 100 * sorted(null)[-N_PERM // 20], p1, 'holds' if p1 < 0.05 else 'fails'))
    say()

    # V2
    md = [s for s in seals if s['site'] == 'Mohenjo-daro' and s['depth'] is not None]
    pr2 = pairs(md)
    dep = [s['depth'] for s in md]
    obs2 = statistics.median(abs(dep[i] - dep[j]) for i, j in pr2)
    null2 = []
    for _ in range(N_PERM):
        sh = dep[:]
        random.shuffle(sh)
        null2.append(statistics.median(abs(sh[i] - sh[j]) for i, j in pr2))
    p2 = (sum(1 for x in null2 if x <= obs2) + 1) / (N_PERM + 1)
    say('## V2 depth at Mohenjo-daro')
    say()
    say('- seals with a name and a depth: %d (depth range %.1f to %.1f ft, median %.1f); same-name pairs: %d.' % (
        len(md), min(dep), max(dep), statistics.median(dep), len(pr2)))
    say('- median depth difference of same-name pairs: %.1f ft; shuffled: %.1f ft (5-95%%: %.1f-%.1f); p = %.4f. '
        '**V2 %s.**' % (obs2, statistics.mean(null2), sorted(null2)[N_PERM // 20], sorted(null2)[-N_PERM // 20], p2,
                        'holds' if p2 < 0.05 else 'fails'))
    say()
    say('**Hypothesis V %s.**' % ('holds' if p1 < 0.05 and p2 < 0.05 else 'fails'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test5.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
