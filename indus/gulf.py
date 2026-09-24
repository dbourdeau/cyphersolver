"""The West Asian Indus texts as a foreign-language control (fuller ICIT-derived corpus; see icit_full.py).

Indus-inscribed seals from the Gulf, Mesopotamia, Iran and Central Asia are thought to write other peoples' names
in Indus signs (Hunter 1932; Parpola 1994; Laursen 2010). If 740 and 520 are suffixes of the Indus language, those
texts should use them less, and their sign sequences should be less familiar, while the signs themselves are the
Indus ones.

G1  Share of texts ending in 740 / 520 (with or without 400 / 90 / 151 after), and opening with the heading
    formula: West Asian texts against home texts (Indus region), Fisher test.
G2  Familiarity: share of adjacent sign pairs in each West Asian text that occur anywhere in the home corpus, against
    home texts (each scored against the home corpus without itself and its copies), and against the West Asian
    texts with their signs shuffled.
G3  Share of West Asian sign tokens that are Indus signs in common use at home (5+ home tokens).

Usage: python gulf.py path/to/icit_full_records_indusscript_net.csv
Writes results/gulf.md.
"""
import math
import os
import random
import sys
from collections import Counter

import icit_full

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
WEST = {'Persian Gulf', 'Mesopotamia', 'Central Asia'}
IRAN_WEST = {'Susa', 'Luristan', 'Tepe Yahya'}


def say(s=''):
    OUT.append(s)
    print(s)


def fisher_two(a, b, c, d):
    n1, n2, k = a + b, c + d, a + c
    tot = n1 + n2

    def lc(n, r):
        return math.lgamma(n + 1) - math.lgamma(r + 1) - math.lgamma(n - r + 1)

    def p(x):
        return math.exp(lc(n1, x) + lc(n2, k - x) - lc(tot, k))
    obs = p(a)
    return min(1.0, sum(p(x) for x in range(max(0, k - n2), min(n1, k) + 1) if p(x) <= obs * (1 + 1e-9)))


def ends_ok(t):
    return t[-1] in ('740', '520') or (len(t) >= 2 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'))


def main(path):
    rng = random.Random(139)
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = [r for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST]
    home = [r for r in rows if r not in west and recs[r['sealid']][2] not in ('Other',)]
    say('# The West Asian Indus texts as a foreign-language control')
    say()
    say('- West Asian objects with intact text: %d (%s); home objects: %d.' % (
        len(west), ', '.join('%s %d' % kv for kv in Counter(r['site'] for r in west).most_common()), len(home)))
    say()
    wt = [ln for r in west for ln in r['seq'] if len(ln) >= 2]
    ht = [ln for r in home for ln in r['seq'] if len(ln) >= 2]
    a, b = sum(ends_ok(t) for t in wt), len(wt)
    c, d = sum(ends_ok(t) for t in ht), len(ht)
    say('## G1 Endings and heading')
    say()
    say('- lines of 2+ signs ending in 740 / 520: West Asian %d of %d (%.0f%%), home %d of %d (%.0f%%); Fisher p = %.3f.' % (
        a, b, 100 * a / max(b, 1), c, d, 100 * c / d, fisher_two(a, b - a, c, d - c)))
    hw = sum(1 for r in west if len(r['flat']) >= 3 and r['flat'][0] in ('817', '820', '861') and r['flat'][1] in ('2', '60', '1'))
    hh = sum(1 for r in home if len(r['flat']) >= 3 and r['flat'][0] in ('817', '820', '861') and r['flat'][1] in ('2', '60', '1'))
    say('- the heading formula: West Asian %d of %d objects, home %d of %d (%.1f%%).' % (hw, len(west), hh, len(home), 100 * hh / len(home)))
    say()
    say('## G2 Familiar sign pairs')
    say()
    pair_home = Counter()
    for t in ht:
        for p in set(zip(t, t[1:])):
            pair_home[p] += 1

    def fam(t, excl=None):
        ps = list(zip(t, t[1:]))
        if not ps:
            return None
        k = 0
        for p in ps:
            n = pair_home[p] - (excl[p] if excl else 0)
            k += n > 0
        return k / len(ps)
    fw = [x for x in (fam(t) for t in wt) if x is not None]
    copies = Counter(tuple(t) for t in ht)
    sample = rng.sample(ht, min(len(ht), 600))
    fh = []
    for t in sample:
        same = [u for u in ht if tuple(u) == tuple(t)]
        ex = Counter()
        for u in same:
            for p in set(zip(u, u[1:])):
                ex[p] += 1
        x = fam(t, ex)
        if x is not None:
            fh.append(x)
    fs = []
    for t in wt:
        u = list(t)
        rng.shuffle(u)
        x = fam(u)
        if x is not None:
            fs.append(x)
    say('- share of a text\'s adjacent pairs found in the home corpus: West Asian texts %.0f%% (%d texts); home texts, '
        'scored without themselves and their copies, %.0f%% (%d sampled); West Asian texts with shuffled signs %.0f%%.' % (
            100 * sum(fw) / len(fw), len(fw), 100 * sum(fh) / len(fh), len(fh), 100 * sum(fs) / len(fs)))
    say()
    say('## G3 The signs')
    say()
    tok_home = Counter(g for r in home for g in r['flat'])
    wtok = [g for r in west for g in r['flat']]
    say('- West Asian sign tokens: %d; of them Indus signs with 5+ home tokens: %d (%.0f%%). Commonest West Asian signs: %s.' % (
        len(wtok), sum(1 for g in wtok if tok_home[g] >= 5), 100 * sum(1 for g in wtok if tok_home[g] >= 5) / max(1, len(wtok)),
        ', '.join('%s x%d' % kv for kv in Counter(wtok).most_common(10))))
    say('- the West Asian texts: %s.' % '; '.join('%s %s: %s' % (r['site'], r['type'], ' '.join(r['flat'])) for r in west))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'gulf.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
