"""Test of the sixth registered prediction set (PREDICTIONS.md, Hypothesis W): sealings and seal names.

W1  sealings whose name is on a seal: share with a same-name seal at the sealing's site, against sites shuffled among
    those sealings.
W2  sealing names match a seal name more often than seal names match another seal, within length strata; object type
    permuted within strata (the match indicator, 'name on at least one other seal', is fixed per object).

Usage: python predict_test6.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test6.md.
"""
import os
import random
import sys
from collections import Counter, defaultdict

import icit_full
from predict_test4 import name_of, stratum

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N_PERM = 10000
random.seed(26)


def say(s=''):
    OUT.append(s)
    print(s)


def units(path):
    out = []
    for r in icit_full.objects(path):
        kind = 'seal' if r['type'].startswith('SEAL') else ('sealing' if r['type'].startswith('TAG') else None)
        if not kind or not r['flat']:
            continue
        if any(ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw']):
            continue
        nm = name_of(r['flat'])
        if nm:
            out.append({'id': r['sealid'], 'kind': kind, 'name': nm, 'site': r['site'].strip(), 'type': r['type']})
    return out


def main(path):
    us = units(path)
    seals = [u for u in us if u['kind'] == 'seal']
    tags = [u for u in us if u['kind'] == 'sealing']
    seal_sites = defaultdict(Counter)
    for s in seals:
        seal_sites[s['name']][s['site']] += 1
    say('# Sixth registered predictions: sealings and seal names')
    say()
    say('- intact seals with a name and an ending: %d; intact sealings: %d (%s).' % (
        len(seals), len(tags), ', '.join('%s %d' % kv for kv in Counter(t['site'] for t in tags).most_common(8))))
    say()

    # W1
    m = [t for t in tags if t['name'] in seal_sites]
    obs = sum(seal_sites[t['name']][t['site']] > 0 for t in m) / len(m)
    sites = [t['site'] for t in m]
    null = []
    for _ in range(N_PERM):
        sh = sites[:]
        random.shuffle(sh)
        null.append(sum(seal_sites[t['name']][s] > 0 for t, s in zip(m, sh)) / len(m))
    hi = (sum(1 for x in null if x >= obs) + 1) / (N_PERM + 1)
    lo = (sum(1 for x in null if x <= obs) + 1) / (N_PERM + 1)
    say('## W1 home')
    say()
    say('- sealings whose name is on a seal: %d of %d.' % (len(m), len(tags)))
    for t in m:
        say('  - %s %s+%s (%s): seals at %s' % (t['site'], '-'.join(t['name'][0]), t['name'][1], t['type'],
                                             ', '.join('%s %d' % kv for kv in seal_sites[t['name']].most_common())))
    say('- with a same-name seal at the same site: %.0f%% (%d of %d); sites shuffled: %.0f%%; p (home) = %.4f, '
        'p (away) = %.4f. **W1 %s.**' % (100 * obs, round(obs * len(m)), len(m), 100 * sum(null) / N_PERM, hi, lo,
                                         'holds' if hi < 0.05 else ('fails, the other way (away)' if lo < 0.05 else 'fails')))
    say()

    # W2
    names = Counter(s['name'] for s in seals)
    for u in us:
        u['match'] = names[u['name']] - (1 if u['kind'] == 'seal' else 0) > 0
        u['st'] = stratum(len(u['name'][0]))

    def stat(kinds):
        diffs = []
        for st in range(1, 5):
            idx = [i for i, u in enumerate(us) if u['st'] == st]
            a = [us[i]['match'] for i in idx if kinds[i] == 'sealing']
            b = [us[i]['match'] for i in idx if kinds[i] == 'seal']
            if a and b:
                diffs.append((len(a), sum(a) / len(a) - sum(b) / len(b)))
        return sum(n * d for n, d in diffs) / sum(n for n, _ in diffs)
    kinds = [u['kind'] for u in us]
    obs2 = stat(kinds)
    strata = defaultdict(list)
    for i, u in enumerate(us):
        strata[u['st']].append(i)
    ge = 0
    for _ in range(N_PERM):
        k = kinds[:]
        for idx in strata.values():
            vals = [k[i] for i in idx]
            random.shuffle(vals)
            for i, v in zip(idx, vals):
                k[i] = v
        if stat(k) >= obs2:
            ge += 1
    p2 = (ge + 1) / (N_PERM + 1)
    say('## W2 common names')
    say()
    say('| signs before the ending | sealings | matching a seal | seals | matching another seal |')
    say('|---|---|---|---|---|')
    for st in range(1, 5):
        a = [u for u in us if u['st'] == st and u['kind'] == 'sealing']
        b = [u for u in us if u['st'] == st and u['kind'] == 'seal']
        f = lambda xs: '%d (%.0f%%)' % (sum(x['match'] for x in xs), 100 * sum(x['match'] for x in xs) / len(xs)) if xs else '-'
        say('| %s | %d | %s | %d | %s |' % ('4+' if st == 4 else st, len(a), f(a), len(b), f(b)))
    say()
    say('Difference weighted by sealings per stratum: %+.1f points; permutation p = %.4f. **W2 %s.**' % (
        100 * obs2, p2, 'holds' if obs2 > 0 and p2 < 0.05 else 'fails'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test6.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
