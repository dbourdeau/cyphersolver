"""Seventh pass, lead: the Harappa tablets as a genre of their own.

Incised (TAB:I) and moulded (TAB:B) tablets are small, often made in many copies, and date from mid
3B into 3C at Harappa (Kenoyer and Meadow 2010). Their texts end in 740 + 400 where seals end in
740 + 'man' (G2). What are they?

TB1 Copies: distinct texts, copies per text, texts made in 5+ copies; does one text keep one
    picture (as on the copper tablets) or change it?
TB2 Vocabulary: signs over-represented on tablets against square seals (log odds with a 0.5
    prior, 10+ tokens), and the signs found only on tablets.
TB3 Tablets and seals: how many tablet texts (less the 740 400 ending) are found whole inside a
    seal text, against the same test for tablet texts with their signs shuffled (a null for how
    often short sequences turn up in seals by chance).
TB4 Numerals on tablets: share of texts with a stroke numeral, values, what the numeral
    precedes, against seals.
TB5 Texts that are only a numeral and one sign (a quantity + a thing, as on tokens and tallies),
    by object type; and which stroke series stands before the pot 700.

Writes results/tablets.md.
"""
import math
import os
import random
from collections import Counter, defaultdict

from numerals import NUMS
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
random.seed(71)
TAB = ('TAB:I', 'TAB:B')


def say(s=''):
    OUT.append(s)
    print(s)


def core(t):
    t = list(t)
    if len(t) >= 2 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
        t = t[:-2]
    elif t and t[-1] in ('740', '520'):
        t = t[:-1]
    return t


def main():
    rows = [r for r in load(split=False) if r['flat']]
    tabs = [r for r in rows if r['type'] in TAB]
    seals = [r for r in rows if r['type'] == 'SEAL:S']
    say('# The Harappa tablets as a genre')
    say()
    say('## TB1 Copies')
    say()
    for t in TAB + ('SEAL:S',):
        rs = [r for r in rows if r['type'] == t]
        c = Counter(' '.join(r['flat']) for r in rs)
        say('- %s: %d objects, %d distinct texts (%.2f objects a text); texts in 5+ copies: %d, holding %d objects; '
            'Harappa %d%%.' % (t, len(rs), len(c), len(rs) / len(c), sum(1 for v in c.values() if v >= 5),
                               sum(v for v in c.values() if v >= 5), 100 * sum(1 for r in rs if r['site'] == 'Harappa') / len(rs)))
    mot = defaultdict(Counter)
    for r in tabs:
        mot[' '.join(r['flat'])][(r['motif'] or '-').split(':')[0]] += 1
    multi = {t: m for t, m in mot.items() if sum(m.values()) >= 3}
    one = sum(1 for m in multi.values() if len(m) == 1)
    say('- tablet texts in 3+ copies: %d; with one picture (or none) on every copy: %d; with two or more pictures: %d '
        '(%s).' % (len(multi), one, len(multi) - one, '; '.join('%s: %s' % (t, dict(m)) for t, m in multi.items() if len(m) > 1)[:900]))
    top = sorted(mot.items(), key=lambda x: -sum(x[1].values()))[:10]
    say('- the most copied tablet texts: %s.' % '; '.join('%s x%d %s' % (t, sum(m.values()), dict(m)) for t, m in top))
    say()
    say('## TB2 Vocabulary')
    say()
    ft = Counter(g for r in tabs for g in r['flat'])
    fs = Counter(g for r in seals for g in r['flat'])
    nt, ns = sum(ft.values()), sum(fs.values())
    lo = []
    for g in set(ft) | set(fs):
        if ft[g] + fs[g] >= 10:
            lo.append((math.log((ft[g] + .5) / nt) - math.log((fs[g] + .5) / ns), g))
    lo.sort()
    say('- tokens: tablets %d, square seals %d.' % (nt, ns))
    say('- most tablet-leaning signs (log odds, tablet/seal tokens): %s.' % ', '.join(
        '%s %.1f (%d/%d)' % (g, v, ft[g], fs[g]) for v, g in lo[::-1][:14]))
    say('- most seal-leaning signs: %s.' % ', '.join('%s %.1f (%d/%d)' % (g, v, ft[g], fs[g]) for v, g in lo[:14]))
    only = sorted((g for g in ft if fs[g] == 0 and ft[g] >= 5), key=lambda g: -ft[g])
    say('- signs with 5+ tablet tokens and none on square seals: %s.' % ', '.join('%s x%d' % (g, ft[g]) for g in only))
    say()
    say('## TB3 Tablet texts inside seal texts')
    say()
    sealtxt = [' ' + ' '.join(r['flat']) + ' ' for r in seals]
    dist = {tuple(core(r['flat'])) for r in tabs}
    dist = [t for t in dist if len(t) >= 2]

    def found(t):
        s = ' ' + ' '.join(t) + ' '
        return any(s in x for x in sealtxt)
    real = sum(1 for t in dist if found(t))
    sims = []
    for _ in range(100):
        k = 0
        for t in dist:
            u = list(t)
            random.shuffle(u)
            k += found(u)
        sims.append(k)
    sims.sort()
    say('- distinct tablet texts of 2+ signs before the ending: %d; found whole inside a square-seal text: %d (%.0f%%); '
        'with their signs shuffled: median %d (range %d-%d).' % (len(dist), real, 100 * real / len(dist), sims[50],
                                                                   sims[0], sims[-1]))
    ex = [t for t in dist if found(t) and len(t) >= 3][:10]
    say('- e.g. %s.' % '; '.join(' '.join(t) for t in ex))
    say()
    say('## TB4 Numerals')
    say()
    for lab, rs in (('tablets', tabs), ('square seals', seals)):
        n = len(rs)
        wn = [r for r in rs if any(g in NUMS for g in r['flat'])]
        vals = Counter(NUMS[g][0] for r in rs for g in r['flat'] if g in NUMS and g not in ('2', '32'))
        nxt = Counter()
        for r in rs:
            f = r['flat']
            for a, b in zip(f, f[1:]):
                if a in NUMS and a not in ('2', '32') and b not in NUMS:
                    nxt[b] += 1
        first = sum(1 for r in rs if r['flat'][0] in NUMS and r['flat'][0] not in ('2', '32'))
        say('- %s: %d of %d objects with a stroke numeral (%.0f%%); numeral first sign in %d (%.0f%%); values (pairs '
            'left out) %s; commonest sign after a numeral: %s.' % (
                lab, len(wn), n, 100 * len(wn) / n, first, 100 * first / n,
                ', '.join('%d x%d' % kv for kv in sorted(vals.items())),
                ', '.join('%s x%d' % kv for kv in nxt.most_common(8))))
    say()
    say('## TB5 Number + one sign as a whole text')
    say()
    for lab, rs in (('tablets', tabs), ('square seals', seals), ('bar seals', [r for r in rows if r['type'] == 'SEAL:R']),
                    ('pottery', [r for r in rows if r['type'].startswith('POT')])):
        c = Counter()
        for r in rs:
            f = r['flat']
            if len(f) == 2 and f[0] in NUMS and f[1] not in NUMS:
                c['%s(%s %d) %s' % (f[0], NUMS[f[0]][1], NUMS[f[0]][0], f[1])] += 1
        say('- %s: %d of %d objects (%.0f%%) carry only a numeral and one sign; %s.' % (
            lab, sum(c.values()), len(rs), 100 * sum(c.values()) / len(rs), ', '.join('%s x%d' % kv for kv in c.most_common(10))))
    pots = Counter()
    for r in rows:
        f = r['flat']
        for a, b in zip(f, f[1:]):
            if b == '700':
                pots[(r['type'].split(':')[0], NUMS[a][1] if a in NUMS else 'not a numeral')] += 1
    say('- what stands before the pot 700, by object: %s.' % ', '.join('%s %s x%d' % (t, k, v) for (t, k), v in pots.most_common(8)))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'tablets.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
