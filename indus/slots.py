"""Sign classes from the slots they fill (the step before Ventris's grid).

Each sign with >= 15 occurrences gets a context profile: counts of its left neighbours and
right neighbours (line start '<' and end '>' included), PPMI-weighted. Signs are clustered
by cosine similarity of these profiles (average-linkage agglomerative clustering, cut at a
fixed number of classes). The classes are checked against groups known independently of
context: the numerals (by shape), the fish series (by shape), and the ending and opening
classes (by position). Stability: the clustering is repeated on 50 bootstrap resamples of
the lines and each pair of signs gets the share of runs in which it is clustered together.

Writes results/slots.md.
"""
import os
import random
from collections import Counter, defaultdict

import numpy as np
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import pdist

from signs import FISH, NUMERAL, load

HERE = os.path.dirname(os.path.abspath(__file__))
random.seed(5)
OUT = []
K = 24          # number of classes


def say(s=''):
    OUT.append(s)
    print(s)


def profiles(lines, signs):
    idx = {s: i for i, s in enumerate(signs)}
    feats = {}
    rows = defaultdict(Counter)
    for ln in lines:
        s = ['<'] + ln + ['>']
        for i in range(1, len(s) - 1):
            g = s[i]
            if g in idx:
                rows[g]['L:' + s[i - 1]] += 1
                rows[g]['R:' + s[i + 1]] += 1
    for c in rows.values():
        for f in c:
            feats.setdefault(f, len(feats))
    M = np.zeros((len(signs), len(feats)))
    for g, c in rows.items():
        for f, v in c.items():
            M[idx[g], feats[f]] = v
    tot = M.sum()
    pr = M.sum(1, keepdims=True) / tot
    pc = M.sum(0, keepdims=True) / tot
    with np.errstate(divide='ignore', invalid='ignore'):
        pmi = np.log((M / tot) / (pr @ pc))
    pmi[~np.isfinite(pmi)] = 0
    return np.maximum(pmi, 0)


def cluster(lines, signs):
    P = profiles(lines, signs)
    D = pdist(P, 'cosine')
    D = np.nan_to_num(D, nan=1.0)
    Z = linkage(D, 'average')
    return fcluster(Z, K, 'maxclust')


def main():
    rows = [r for r in load() if r['flat']]
    lines = [ln for r in rows for ln in r['seq']]
    tot = Counter(g for ln in lines for g in ln)
    signs = sorted([g for g, c in tot.items() if c >= 15], key=lambda g: -tot[g])
    lab = cluster(lines, signs)
    # bootstrap co-assignment
    co = np.zeros((len(signs), len(signs)))
    B = 50
    for _ in range(B):
        bl = [random.choice(lines) for _ in lines]
        lb = cluster(bl, signs)
        co += (lb[:, None] == lb[None, :])
    co /= B
    groups = defaultdict(list)
    for s, l in zip(signs, lab):
        groups[l].append(s)
    fin = Counter(ln[-1] for ln in lines if len(ln) > 1)
    ini = Counter(ln[0] for ln in lines if len(ln) > 1)
    say('# Sign classes from context (slots)')
    say()
    say('%d signs with 15 or more occurrences; %d classes; stability = mean share of 50 bootstrap '
        'runs in which the members of a class are clustered together.' % (len(signs), K))
    say()
    say('| class | members (count) | stability | final share | initial share | numerals | fish series |')
    say('|---|---|---|---|---|---|---|')
    idx = {s: i for i, s in enumerate(signs)}
    for l, mem in sorted(groups.items(), key=lambda x: -sum(tot[g] for g in x[1])):
        ii = [idx[g] for g in mem]
        stab = np.mean([co[a, b] for a in ii for b in ii if a < b]) if len(ii) > 1 else float('nan')
        n = sum(tot[g] for g in mem)
        say('| %d | %s | %s | %.0f%% | %.0f%% | %d | %d |' % (
            l, ' '.join('%s(%d)' % (g, tot[g]) for g in mem), '-' if len(ii) == 1 else '%.2f' % stab,
            100 * sum(fin[g] for g in mem) / n, 100 * sum(ini[g] for g in mem) / n,
            sum(g in NUMERAL for g in mem), sum(g in FISH for g in mem)))
    say()
    # checks against independent groups
    def purity(group, name):
        g = [s for s in signs if s in group]
        labs = Counter(lab[idx[s]] for s in g)
        top, n = labs.most_common(1)[0]
        pairs = [(a, b) for i, a in enumerate(g) for b in g[i + 1:]]
        same = sum(lab[idx[a]] == lab[idx[b]] for a, b in pairs)
        # chance: pairs of random signs landing in the same class
        sizes = Counter(lab)
        chance = sum(v * (v - 1) for v in sizes.values()) / (len(signs) * (len(signs) - 1))
        say('- %s (%d signs by shape): %d of %d pairs share a class (%.0f%%; two random signs share a '
            'class %.0f%% of the time); largest class holds %d.' % (
                name, len(g), same, len(pairs), 100 * same / max(1, len(pairs)), 100 * chance, n))
    say('## Checks against classes known from shape or position')
    say()
    purity({s for s in NUMERAL if s in ('31', '32', '33', '34', '35', '36')}, 'long-stroke numerals')
    purity({s for s in NUMERAL if s in ('1', '2', '3', '4', '5')}, 'short-stroke numerals')
    purity(FISH, 'fish series')
    ends = {g for g in signs if fin[g] / tot[g] >= 0.5}
    purity(ends, 'signs ending a line half the time or more')
    starts = {g for g in signs if ini[g] / tot[g] >= 0.5}
    purity(starts, 'signs beginning a line half the time or more')
    say()
    say('## Most stable pairs (clustered together in >= 90% of bootstrap runs), by class')
    say()
    stable = defaultdict(list)
    for i, a in enumerate(signs):
        for j in range(i + 1, len(signs)):
            if co[i, j] >= 0.9:
                stable[lab[i]].append('%s~%s' % (a, signs[j]))
    for l, ps in sorted(stable.items()):
        say('- class %d: %s' % (l, ', '.join(ps[:30])))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'slots.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
