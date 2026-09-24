"""Test of the fourth registered prediction set (PREDICTIONS.md, Hypothesis T): are 520 names shared names (gods,
titles) and 740 names personal names?

T1  recurrence of a name on another seal, 520 against 740, stratified by name length; permutation of the ending
    labels within strata.
T2  among names on 2+ seals, spread over 2+ sites, 520 against 740, same stratification; and each class against a
    null in which site labels are shuffled among the seals.

Usage: python predict_test4.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test4.md.
"""
import os
import random
import sys
from collections import Counter, defaultdict

import icit_full

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
OPEN = ('817', '820', '861')
N_PERM = 10000
random.seed(24)


def say(s=''):
    OUT.append(s)
    print(s)


def name_of(t):
    t = [g for g in t if g != '?']
    if len(t) >= 3 and t[0] in OPEN and t[1] in ('2', '60', '1'):
        t = t[2:]
    if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
        t = t[:-1]
    if len(t) >= 2 and t[-1] in ('740', '520'):
        return tuple(t[:-1]), t[-1]
    return None


def stratum(n):
    return min(n, 4)


def main(path):
    seals = []
    for r in icit_full.objects(path):
        if not r['type'].startswith('SEAL') or not r['flat']:
            continue
        if any(ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw']):
            continue
        nm = name_of(r['flat'])
        if nm:
            seals.append({'name': nm[0], 'end': nm[1], 'site': r['site'].strip()})
    by = defaultdict(list)
    for s in seals:
        by[(s['name'], s['end'])].append(s)
    for s in seals:
        s['rec'] = len(by[(s['name'], s['end'])]) > 1
        s['st'] = stratum(len(s['name']))

    say('# Fourth registered predictions: are 520 names shared names and 740 names personal names?')
    say()
    say('- intact seals with a name and an ending: %d (740: %d, 520: %d); sites: %s.' % (
        len(seals), sum(s['end'] == '740' for s in seals), sum(s['end'] == '520' for s in seals),
        ', '.join('%s %d' % kv for kv in Counter(s['site'] for s in seals).most_common(6))))
    say()

    # T1
    def t1_stat(labels):
        diffs = []
        for st in range(1, 5):
            idx = [i for i, s in enumerate(seals) if s['st'] == st]
            a = [seals[i]['rec'] for i in idx if labels[i] == '520']
            b = [seals[i]['rec'] for i in idx if labels[i] == '740']
            if a and b:
                diffs.append((len(idx), sum(a) / len(a) - sum(b) / len(b)))
        return sum(n * d for n, d in diffs) / sum(n for n, _ in diffs)
    labels = [s['end'] for s in seals]
    obs = t1_stat(labels)
    strata = defaultdict(list)
    for i, s in enumerate(seals):
        strata[s['st']].append(i)
    ge = 0
    for _ in range(N_PERM):
        lab = labels[:]
        for idx in strata.values():
            vals = [lab[i] for i in idx]
            random.shuffle(vals)
            for i, v in zip(idx, vals):
                lab[i] = v
        if t1_stat(lab) >= obs:
            ge += 1
    p1 = (ge + 1) / (N_PERM + 1)
    say('## T1 recurrence')
    say()
    say('| signs before the ending | 520 seals | 520 recurring | 740 seals | 740 recurring |')
    say('|---|---|---|---|---|')
    for st in range(1, 5):
        a = [s for s in seals if s['st'] == st and s['end'] == '520']
        b = [s for s in seals if s['st'] == st and s['end'] == '740']
        say('| %s | %d | %s | %d | %s |' % ('4+' if st == 4 else st, len(a),
            '%d (%.0f%%)' % (sum(x['rec'] for x in a), 100 * sum(x['rec'] for x in a) / len(a)) if a else '-', len(b),
            '%d (%.0f%%)' % (sum(x['rec'] for x in b), 100 * sum(x['rec'] for x in b) / len(b)) if b else '-'))
    say()
    say('Pooled difference (520 minus 740, weighted by stratum size): %+.1f points; permutation p = %.4f. **T1 %s.**'
        % (100 * obs, p1, 'holds' if obs > 0 and p1 < 0.05 else 'fails'))
    say()

    # T2
    groups = [(k, v) for k, v in by.items() if len(v) >= 2]

    def spread(gs):
        return [len({s['site'] for s in v}) >= 2 for _, v in gs]

    def t2_stat(ends):
        diffs = []
        for st in range(1, 5):
            gi = [i for i, (k, _) in enumerate(groups) if stratum(len(k[0])) == st]
            sp = spread([groups[i] for i in gi])
            a = [x for i, x in zip(gi, sp) if ends[i] == '520']
            b = [x for i, x in zip(gi, sp) if ends[i] == '740']
            if a and b:
                diffs.append((len(gi), sum(a) / len(a) - sum(b) / len(b)))
        return sum(n * d for n, d in diffs) / sum(n for n, _ in diffs) if diffs else float('nan')
    ends = [k[1] for k, _ in groups]
    obs2 = t2_stat(ends)
    gstrata = defaultdict(list)
    for i, (k, _) in enumerate(groups):
        gstrata[stratum(len(k[0]))].append(i)
    ge = 0
    for _ in range(N_PERM):
        e = ends[:]
        for idx in gstrata.values():
            vals = [e[i] for i in idx]
            random.shuffle(vals)
            for i, v in zip(idx, vals):
                e[i] = v
        if t2_stat(e) >= obs2:
            ge += 1
    p2 = (ge + 1) / (N_PERM + 1)

    # site-shuffled null per class
    sites = [s['site'] for s in seals]
    pos = {id(s): i for i, s in enumerate(seals)}
    null = {'520': [], '740': []}
    for _ in range(2000):
        sh = sites[:]
        random.shuffle(sh)
        for end in null:
            gs = [v for k, v in groups if k[1] == end]
            null[end].append(sum(len({sh[pos[id(s)]] for s in v}) >= 2 for v in gs) / len(gs))
    say('## T2 spread over sites')
    say()
    say('| ending | names on 2+ seals | at 2+ sites | site-shuffled expectation | p (observed or more) |')
    say('|---|---|---|---|---|')
    pc = {}
    for end in ('520', '740'):
        gs = [v for k, v in groups if k[1] == end]
        o = sum(len({s['site'] for s in v}) >= 2 for v in gs) / len(gs)
        pc[end] = (sum(1 for x in null[end] if x >= o) + 1) / 2001
        say('| %s | %d | %d (%.0f%%) | %.0f%% | %.4f |' % (end, len(gs), round(o * len(gs)), 100 * o,
                                                         100 * sum(null[end]) / len(null[end]), pc[end]))
    say()
    ok2 = obs2 > 0 and p2 < 0.05 and pc['520'] < 0.05 and pc['740'] >= 0.05
    say('Pooled difference (520 minus 740): %+.1f points; permutation p = %.4f. **T2 %s.**' % (
        100 * obs2, p2, 'holds' if ok2 else 'fails'))
    say()
    say('Commonest recurring names: ' + '; '.join('%s+%s on %d seals at %s' % (
        '-'.join(k[0]), k[1], len(v), ', '.join('%s %d' % kv for kv in Counter(s['site'] for s in v).most_common(3)))
        for k, v in sorted(groups, key=lambda kv: -len(kv[1]))[:12]) + '.')
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test4.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
