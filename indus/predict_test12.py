"""Test of the twelfth registered prediction set (PREDICTIONS.md): the candidate sound-sign shortlist.

SL1  share of West Asian tokens that are shortlist signs, against length-matched home draws.
SL2  substitution pairs of names swapping two shortlist signs share a site more often than other substitution pairs
     (labels permuted within strata of the rarer name's object count).
SL3  the same for object type.

Usage: python predict_test12.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test12.md.
"""
import os
import random
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations

import icit_full
from gulf import IRAN_WEST, WEST
from numerals import NUMS
from predict_test4 import name_of

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N_PERM = 10000
LEAVE = {'740', '520', '817', '820', '861'}
random.seed(32)


def say(s=''):
    OUT.append(s)
    print(s)


def shortlist():
    out = []
    for ln in open(os.path.join(HERE, 'results', 'sound_shortlist.md'), encoding='utf-8'):
        m = re.match(r'^\| (\d+) \| (\d+) \|', ln)
        if m:
            out.append(m.group(2))
    return set(out)


def otype(t):
    for k in ('SEAL', 'TAB', 'TAG'):
        if t.startswith(k):
            return k
    return 'other'


def perm_test(pairs, key):
    """pairs: (is_candidate, stratum, outcome). Difference in outcome rate, candidate minus other; within-stratum
    permutation of the candidate label."""
    def diff(lab):
        a = [o for l, (_, _, o) in zip(lab, pairs) if l]
        b = [o for l, (_, _, o) in zip(lab, pairs) if not l]
        return sum(a) / len(a) - sum(b) / len(b)
    lab = [c for c, _, _ in pairs]
    obs = diff(lab)
    st = defaultdict(list)
    for i, (_, s, _) in enumerate(pairs):
        st[s].append(i)
    ge = 0
    for _ in range(N_PERM):
        sh = lab[:]
        for idx in st.values():
            v = [sh[i] for i in idx]
            random.shuffle(v)
            for i, w in zip(idx, v):
                sh[i] = w
        if diff(sh) >= obs:
            ge += 1
    return obs, (ge + 1) / (N_PERM + 1)


def main(path):
    sl = shortlist()
    say('# Twelfth registered predictions: testing the candidate sound-sign shortlist')
    say()
    say('- shortlist: %d signs.' % len(sl))
    say()

    # SL1
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = {r['sealid'] for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST}
    home = [r for r in rows if r['sealid'] not in west and recs[r['sealid']][2] not in ('Other',)]
    wl = [ln for r in rows if r['sealid'] in west for ln in r['seq'] if len(ln) >= 2]
    hl = [ln for r in home for ln in r['seq'] if len(ln) >= 2]
    bylen = defaultdict(list)
    for ln in hl:
        bylen[len(ln)].append(ln)

    def draw(n):
        while n not in bylen:
            n -= 1
        return random.choice(bylen[n])

    def share(lines):
        v = [g in sl for t in lines for g in t if g not in LEAVE and g not in NUMS]
        return sum(v) / len(v), sum(v), len(v)
    obs, k, n = share(wl)
    null = [share([draw(len(t)) for t in wl])[0] for _ in range(N_PERM)]
    p1 = (sum(1 for x in null if x >= obs) + 1) / (N_PERM + 1)
    say('## SL1 foreign names')
    say()
    say('- West Asian tokens that are shortlist signs: %d of %d (%.0f%%); length-matched home draws %.0f%% (5-95%%: '
        '%.0f-%.0f%%); p = %.4f. **SL1 %s.**' % (k, n, 100 * obs, 100 * sum(null) / N_PERM,
                                                 100 * sorted(null)[N_PERM // 20], 100 * sorted(null)[-N_PERM // 20],
                                                 p1, 'holds' if p1 < 0.05 else 'fails'))
    say('- West Asian shortlist tokens: %s.' % ', '.join('%s x%d' % kv for kv in Counter(
        g for t in wl for g in t if g in sl).most_common()))
    say()

    # names with their sites and object types
    sites, types, count = defaultdict(set), defaultdict(set), Counter()
    for r in icit_full.objects(path):
        if not r['flat'] or '?' in r['flat']:
            continue
        if any(ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw']):
            continue
        nm = name_of(r['flat'])
        if nm:
            sites[nm].add(r['site'].strip())
            types[nm].add(otype(r['type']))
            count[nm] += 1
    buckets = defaultdict(list)
    for body, end in count:
        for i in range(len(body)):
            buckets[(end, body[:i], body[i + 1:])].append((body, end))
    pairs = []
    for (end, pre, post), ns in buckets.items():
        i = len(pre)
        for a, b in combinations(ns, 2):
            cand = a[0][i] in sl and b[0][i] in sl
            st = min(3, count[a], count[b])
            pairs.append((cand, st, bool(sites[a] & sites[b]), bool(types[a] & types[b]), a[0][i], b[0][i]))
    nc = sum(1 for p in pairs if p[0])
    say('## SL2 / SL3 substitution pairs')
    say()
    say('- distinct names: %d; substitution pairs: %d, of which candidate pairs (both swapped signs on the list): %d.' % (
        len(count), len(pairs), nc))
    for lab, j in (('SL2 share a site', 2), ('SL3 share an object type', 3)):
        o, p = perm_test([(q[0], q[1], q[j]) for q in pairs], j)
        rc = sum(q[j] for q in pairs if q[0]) / nc
        ro = sum(q[j] for q in pairs if not q[0]) / (len(pairs) - nc)
        say('- %s: candidate pairs %.0f%%, other pairs %.0f%%; difference %+.1f points, stratified permutation p = %.4f. '
            '**%s %s.**' % (lab, 100 * rc, 100 * ro, 100 * o, p, lab.split()[0], 'holds' if o > 0 and p < 0.05 else 'fails'))
    say('- commonest candidate swaps: %s.' % ', '.join('%s/%s x%d' % (a, b, c) for (a, b), c in Counter(
        tuple(sorted((q[4], q[5]))) for q in pairs if q[0]).most_common(12)))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test12.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
