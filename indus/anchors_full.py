"""Sign and picture on the seals of the fuller ICIT-derived corpus (icit_full.py; field 18 = the animal or scene,
field 19 = the object before the animal: the 'standard' of the unicorn seals, a trough, none).

S1  Sign against animal, seals only, unit = a distinct text: for each sign in 3+ distinct seal texts and each animal
    other than the unicorn, texts with both against the animal's share of seal texts (binomial), Bonferroni.
S2  Sign against the object before the animal (standard / trough / none), the same way: is any sign tied to the
    cult standard or to the trough rather than to the animal?

Usage: python anchors_full.py path/to/icit_full_records_indusscript_net.csv
Writes results/anchors_full.md.
"""
import math
import os
import sys
from collections import Counter, defaultdict

import icit_full

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def binom_upper(k, n, p):
    if k <= 0:
        return 1.0
    return min(1.0, sum(math.exp(math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
                                 + i * math.log(p) + (n - i) * math.log(1 - p)) for i in range(k, n + 1)))


def test(units, label):
    freq = Counter(m for _, m in units)
    N = len(units)
    by = defaultdict(Counter)
    for t, m in units:
        for g in set(t):
            by[g][m] += 1
    tests = [(g, m) for g, c in by.items() if sum(c.values()) >= 3 for m in c if m not in ('Bull1', '-', 'None', '')]
    alpha = 0.05 / max(1, len(tests))
    hits = []
    for g, m in tests:
        n, k = sum(by[g].values()), by[g][m]
        p = binom_upper(k, n, freq[m] / N)
        if k >= 3 and p < alpha:
            hits.append((p, g, m, k, n))
    hits.sort()
    say('- %s: %d distinct seal texts; %s. Sign x category pairs tested: %d (alpha %.1e); significant: %s.' % (
        label, N, ', '.join('%s %d' % kv for kv in freq.most_common(10)), len(tests), alpha,
        '; '.join('%s with %s in %d of %d texts (%.1f%% of texts), p %.1g' % (g, m, k, n, 100 * freq[m] / N, p)
                  for p, g, m, k, n in hits[:15]) or 'none'))


def main(path):
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    seals = [r for r in icit_full.objects(path, intact_only=True) if r['type'].startswith('SEAL') and r['flat']]
    say('# Sign and picture on the seals of the fuller corpus')
    say()
    u_an, u_fs = {}, {}
    for r in seals:
        t = tuple(r['flat'])
        an = recs[r['sealid']][18].split(':')[0].strip()
        fs = recs[r['sealid']][19].strip()
        u_an.setdefault((t, an), 1)
        u_fs.setdefault((t, fs), 1)
    test(list(u_an), 'S1 animal')
    test(list(u_fs), 'S2 object before the animal')
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'anchors_full.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
