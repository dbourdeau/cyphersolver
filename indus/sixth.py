"""Sixth pass: the ending grid (Kober) and the opening formula.

G1  The ending grid. Each line is split into stem + ending, the ending being the final run from
    {740, 520} followed by up to one of {400, 90, 151}, or nothing. Stems (their last sign) against
    endings; mutual information between the stem's last sign and the ending, against a permutation
    of endings among lines. Which last signs prefer 520, which 740, which no ending.
G2  The second slot (400 / 90 / 151 after 740): does its choice go with site, object type or
    the stem, beyond chance?
O1  The opening formula [817 | 820 | 861] + [2 | 60 | 1] + ...: does the choice of opener go
    with the name sign after it, the site, the object type or the field animal, beyond chance?

Writes results/sixth.md.
"""
import math
import os
import random
from collections import Counter, defaultdict

from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
random.seed(31)
FIRST = {'740', '520'}
SECOND = {'400', '90', '151'}
OPENERS = {'817', '820', '861'}
NAMEMARK = FISH | {'803', '806', '798', '794'}


def say(s=''):
    OUT.append(s)
    print(s)


def mi(pairs):
    n = len(pairs)
    a = Counter(x for x, _ in pairs)
    b = Counter(y for _, y in pairs)
    ab = Counter(pairs)
    return sum(c / n * math.log2(c * n / (a[x] * b[y])) for (x, y), c in ab.items())


def mi_test(pairs, n=1000):
    obs = mi(pairs)
    xs = [x for x, _ in pairs]
    ys = [y for _, y in pairs]
    ge = 0
    for _ in range(n):
        random.shuffle(ys)
        ge += mi(list(zip(xs, ys))) >= obs
    return obs, ge / n


def split(ln):
    k = len(ln)
    end = []
    if k >= 2 and ln[-1] in SECOND and ln[-2] in FIRST:
        end = ln[-2:]
    elif ln[-1] in FIRST:
        end = ln[-1:]
    stem = ln[:len(ln) - len(end)]
    return stem, ' '.join(end) if end else '(none)'


def g1(rows):
    say('## G1 The ending grid')
    say()
    pairs, full = [], []
    for r in rows:
        for ln in r['seq']:
            if len(ln) < 2:
                continue
            stem, end = split(ln)
            if stem:
                pairs.append((stem[-1], end))
                full.append((r, stem, end))
    ends = Counter(e for _, e in pairs)
    say('- lines of 2+ signs: %d; endings: %s.' % (len(pairs), ', '.join('%s x%d' % kv for kv in ends.most_common())))
    # restrict to stems' last signs with 10+ lines for the MI test
    last = Counter(s for s, _ in pairs)
    sub = [(s, 'none' if e == '(none)' else ('520' if e.startswith('520') else '740')) for s, e in pairs if last[s] >= 10]
    obs, p = mi_test(sub)
    say('- mutual information between the stem\'s last sign and the ending type (none / 740 / 520), '
        'last signs with 10+ lines (%d lines): %.3f bits; permutations as large: %.3f.' % (len(sub), obs, p))
    grid = defaultdict(Counter)
    for s, e in sub:
        grid[s][e] += 1
    prefs = []
    for s, c in grid.items():
        n = sum(c.values())
        prefs.append((c['520'] / n, c['740'] / n, c['none'] / n, n, s))
    say()
    say('| stem ends in | lines | 740 | 520 | none |')
    say('|---|---|---|---|---|')
    for f520, f740, fn, n, s in sorted(prefs, key=lambda x: -x[0])[:10]:
        say('| %s | %d | %.0f%% | %.0f%% | %.0f%% |' % (s, n, 100 * f740, 100 * f520, 100 * fn))
    say('| ... | | | | |')
    for f520, f740, fn, n, s in sorted(prefs, key=lambda x: -x[1])[:8]:
        say('| %s | %d | %.0f%% | %.0f%% | %.0f%% |' % (s, n, 100 * f740, 100 * f520, 100 * fn))
    fish520 = sum(1 for s, e in sub if s in FISH and e == '520')
    fish = sum(1 for s, e in sub if s in FISH)
    oth520 = sum(1 for s, e in sub if s not in FISH and e == '520')
    say()
    say('- stems ending in a fish sign take 520 in %d of %d lines (%.0f%%); other stems %d of %d (%.0f%%).' % (
        fish520, fish, 100 * fish520 / fish, oth520, len(sub) - fish, 100 * oth520 / (len(sub) - fish)))
    say()
    return full


def g2(full):
    say('## G2 The second slot after 740')
    say()
    ev = [(r, stem, e.split()[1]) for r, stem, e in full if e.startswith('740 ')]
    say('- lines ending 740 + second sign: %d (%s).' % (len(ev), ', '.join(
        '%s x%d' % kv for kv in Counter(x for _, _, x in ev).most_common())))
    for lab, f in (('site', lambda r, s: r['site']), ('object type', lambda r, s: r['type'].split(':')[0] + ':' + r['type'].split(':')[-1]),
                   ('stem\'s last sign', lambda r, s: s[-1])):
        obs, p = mi_test([(f(r, s), x) for r, s, x in ev])
        say('- with %s: %.3f bits, permutations as large %.3f.' % (lab, obs, p))
    by = defaultdict(Counter)
    for r, s, x in ev:
        by[r['site']][x] += 1
    say('- by site: ' + '; '.join('%s %s' % (k, dict(v)) for k, v in by.items() if sum(v.values()) >= 5))
    by = defaultdict(Counter)
    for r, s, x in ev:
        by[r['type']][x] += 1
    say('- by object type: ' + '; '.join('%s %s' % (k, dict(v)) for k, v in by.items() if sum(v.values()) >= 5))
    say()


def o1(rows):
    say('## O1 The opening formula')
    say()
    ev = []
    for r in rows:
        s = r['flat']
        if len(s) >= 3 and s[0] in OPENERS and s[1] in ('2', '60', '1'):
            ev.append((r, s[0], s[1], s[2]))
    say('- texts opening [817/820/861] + [2/60/1]: %d; openers %s; second element %s.' % (
        len(ev), dict(Counter(o for _, o, _, _ in ev)), dict(Counter(p for _, _, p, _ in ev))))
    say('- opener by second element: %s.' % dict(Counter((o, p) for _, o, p, _ in ev)))
    tests = [('the sign after the formula', lambda r, t: t),
             ('whether that sign is a name sign', lambda r, t: t in NAMEMARK),
             ('site', lambda r, t: r['site']),
             ('object type', lambda r, t: r['type']),
             ('field animal (seals with a motif)', lambda r, t: r['motif'] or None)]
    for lab, f in tests:
        pr = [(o, f(r, t)) for r, o, _, t in ev if f(r, t) is not None]
        obs, p = mi_test(pr)
        say('- opener against %s (%d texts): %.3f bits, permutations as large %.3f.' % (lab, len(pr), obs, p))
    by = defaultdict(Counter)
    for r, o, _, t in ev:
        by[o][t] += 1
    for o, c in sorted(by.items()):
        say('  - %s + pair is followed by: %s' % (o, ', '.join('%s x%d' % kv for kv in c.most_common(6))))
    say()


def main():
    rows = [r for r in load() if r['flat']]
    say('# Sixth pass: the ending grid and the opening formula')
    say()
    full = g1(rows)
    g2(full)
    o1(rows)
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'sixth.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
