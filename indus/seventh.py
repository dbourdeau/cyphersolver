"""Seventh pass: the fish-name ending and the ritual scenes, time depth, and a slot grammar.

R1  Is the 520 ending a mark of divine names? If the fish names are gods (Parpola), texts ending in
    520 should be commoner on objects with a ritual picture (anthropomorphic figure, scene,
    tree/pipal, composite animal, 'Cros(s)') than on seals with a plain animal. Fisher-style
    permutation test on the share, stems ending in a fish sign handled separately.
T1  Time depth. Kenoyer and Meadow (2010) date at Harappa: square animal seals late 3A-3C, bar seals
    3C only, incised and moulded tablets mid-3B to 3C. Do the ending choices (740 / 520 / none;
    740 + 400 / 90) differ between square seals and the late bar seals, beyond chance? Harappa
    only, then all sites.
P1  A slot grammar as a predictor. For each complete text, hide one sign at a time and predict it
    from (a) the unigram frequency, (b) a bigram model with the left neighbour, (c) a model with
    both neighbours, (d) (c) plus the slot: an opener slot at position 0-1, the ending slot,
    and for the ending the stem's last sign (the G1 grid). Leave-one-text-out counts, top-1 and
    top-5 accuracy. How much does the known structure add to plain n-grams? (Restoring damaged
    texts would need damage marks; corpus.tsv flags every text complete.)

Writes results/seventh.md.
"""
import math
import os
import random
from collections import Counter, defaultdict

from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
random.seed(47)
RITUAL = ('Anth', 'Scene', 'Phyt', 'Pipal', 'Comp', 'CompBull', 'T-A-T', 'T-M-T', 'Cros', 'Crs')
OPENERS = {'817', '820', '861'}


def say(s=''):
    OUT.append(s)
    print(s)


def ending(ln):
    if len(ln) >= 2 and ln[-1] in ('400', '90', '151') and ln[-2] in ('740', '520'):
        return ln[-2]
    return ln[-1] if ln[-1] in ('740', '520') else 'none'


def perm_share(a, b, n=5000):
    """p that the difference in share (a vs b, lists of 0/1) is as large under relabelling."""
    obs = abs(sum(a) / len(a) - sum(b) / len(b))
    pool = a + b
    ge = 0
    for _ in range(n):
        random.shuffle(pool)
        x, y = pool[:len(a)], pool[len(a):]
        ge += abs(sum(x) / len(x) - sum(y) / len(y)) >= obs - 1e-12
    return ge / n


def r1(rows):
    say('## R1 The 520 ending and the ritual pictures')
    say()
    grp = defaultdict(list)
    for r in rows:
        m = r['motif']
        if not m:
            continue
        kind = 'ritual' if m.split(':')[0] in RITUAL else ('unicorn' if m.startswith('Bull1') else 'other animal')
        last = r['seq'][-1]
        if len(last) < 2:
            continue
        grp[kind].append((r, ending(last), last))
    say('| picture | objects | ends 520 | ends 740 | no ending | a fish sign anywhere |')
    say('|---|---|---|---|---|---|')
    for k in ('ritual', 'unicorn', 'other animal'):
        v = grp[k]
        n = len(v)
        say('| %s | %d | %d (%.1f%%) | %d (%.0f%%) | %d (%.0f%%) | %d (%.0f%%) |' % (
            k, n, *sum(([c, 100 * c / n] for c in (
                sum(1 for _, e, _ in v if e == '520'), sum(1 for _, e, _ in v if e == '740'),
                sum(1 for _, e, _ in v if e == 'none'),
                sum(1 for r, _, _ in v if any(g in FISH for g in r['flat'])))), [])))
    rit = [e == '520' for _, e, _ in grp['ritual']]
    ani = [e == '520' for k in ('unicorn', 'other animal') for _, e, _ in grp[k]]
    say()
    say('- 520 ending, ritual pictures against animal seals: p = %.3f (permutation, two-sided).' % perm_share(rit, ani))
    rf = [r for r, _, _ in grp['ritual'] if any(g in FISH for g in r['flat'])]
    af = [r for k in ('unicorn', 'other animal') for r, _, _ in grp[k] if any(g in FISH for g in r['flat'])]
    say('- a fish sign anywhere, ritual against animal: p = %.3f.' % perm_share(
        [any(g in FISH for g in r['flat']) for r, _, _ in grp['ritual']],
        [any(g in FISH for g in r['flat']) for k in ('unicorn', 'other animal') for r, _, _ in grp[k]]))
    say('- the ritual objects that do carry a fish sign or 520: ' + '; '.join(
        '%s %s %s: %s' % (r['cisi'] or r['sealid'], r['type'], r['motif'], ' '.join(r['flat']))
        for r, e, _ in grp['ritual'] if e == '520' or any(g in FISH for g in r['flat'])))
    by = defaultdict(Counter)
    for k in grp:
        for r, e, _ in grp[k]:
            by[r['motif'].split(':')[0]][e] += 1
    say('- ending by picture (10+ objects): ' + '; '.join(
        '%s %d: 520 %.0f%%, 740 %.0f%%' % (m, sum(c.values()), 100 * c['520'] / sum(c.values()),
                                          100 * c['740'] / sum(c.values()))
        for m, c in sorted(by.items(), key=lambda x: -sum(x[1].values())) if sum(c.values()) >= 10))
    say()


def r1b(rows):
    """Fish-final names: which pictures do they go with?"""
    say('### Texts whose name ends in a fish sign + 520, by picture')
    say()
    c, tot = Counter(), Counter()
    for r in rows:
        if not r['motif']:
            continue
        m = r['motif'].split(':')[0]
        tot[m] += 1
        for ln in r['seq']:
            for a, b in zip(ln, ln[1:]):
                if a in FISH and b == '520':
                    c[m] += 1
                    break
    base = sum(c.values()) / sum(tot.values())
    say('- overall %d of %d pictured objects (%.1f%%); by picture: %s.' % (
        sum(c.values()), sum(tot.values()), 100 * base,
        ', '.join('%s %d/%d' % (m, c[m], tot[m]) for m in sorted(tot, key=lambda x: -tot[x]) if tot[m] >= 10)))
    nr = sum(tot[m] for m in RITUAL)
    kr = sum(c[m] for m in RITUAL)
    pz = sum(math.comb(nr, k) * base ** k * (1 - base) ** (nr - k) for k in range(kr + 1))
    say('- on the ritual pictures (%s): %d of %d; binomial chance of %d or fewer at the overall rate: %.4f.' % (
        ', '.join(RITUAL), kr, nr, kr, pz))
    say()


def t1(rows):
    say('## T1 Time depth: square seals (3A-3C) against the late bar seals (3C)')
    say()
    for lab, keep in (('Harappa', lambda r: r['site'] == 'Harappa'), ('all sites', lambda r: True)):
        g = {}
        for t in ('SEAL:S', 'SEAL:R', 'TAB:I', 'TAB:B'):
            es = [ending(r['seq'][-1]) for r in rows if r['type'] == t and keep(r) and len(r['seq'][-1]) >= 2]
            if es:
                g[t] = es
        say('**%s**' % lab)
        say()
        say('| object (period) | texts | 740 | 520 | none | mean length |')
        say('|---|---|---|---|---|---|')
        per = {'SEAL:S': 'square seal, 3A-3C', 'SEAL:R': 'bar seal, 3C', 'TAB:I': 'incised tablet, 3B-3C',
               'TAB:B': 'moulded tablet, 3B-3C'}
        for t, es in g.items():
            n = len(es)
            ln = [len(r['flat']) for r in rows if r['type'] == t and keep(r) and len(r['seq'][-1]) >= 2]
            say('| %s | %d | %.0f%% | %.1f%% | %.0f%% | %.2f |' % (
                per[t], n, 100 * es.count('740') / n, 100 * es.count('520') / n, 100 * es.count('none') / n,
                sum(ln) / len(ln)))
        if 'SEAL:S' in g and 'SEAL:R' in g:
            for e in ('740', '520', 'none'):
                p = perm_share([x == e for x in g['SEAL:S']], [x == e for x in g['SEAL:R']])
                say('- %s: square %.1f%% vs bar %.1f%%, p = %.3f.' % (
                    e, 100 * g['SEAL:S'].count(e) / len(g['SEAL:S']), 100 * g['SEAL:R'].count(e) / len(g['SEAL:R']), p))
        say()
    # the fish-final names: do they persist into 3C?
    for t in ('SEAL:S', 'SEAL:R'):
        rs = [r for r in rows if r['type'] == t]
        f = sum(1 for r in rs if any(g in FISH for g in r['flat']))
        f520 = sum(1 for r in rs if any(a in FISH and b == '520' for ln in r['seq'] for a, b in zip(ln, ln[1:])))
        say('- %s: a fish sign on %d of %d (%.0f%%); fish + 520 on %d (%.1f%%).' % (
            t, f, len(rs), 100 * f / len(rs), f520, 100 * f520 / len(rs)))
    say()


class Model:
    def __init__(self, texts):
        self.uni, self.big, self.rbig, self.tri = Counter(), defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)
        self.slot0, self.end = Counter(), defaultdict(Counter)
        for t in texts:
            self.add(t, 1)

    def add(self, t, w):
        s = ['<s>'] + t + ['</s>']
        for i in range(1, len(s) - 1):
            self.uni[s[i]] += w
            self.big[s[i - 1]][s[i]] += w
            self.rbig[s[i + 1]][s[i]] += w
            self.tri[(s[i - 1], s[i + 1])][s[i]] += w
        if len(t) >= 2:
            self.end[t[-2]][t[-1]] += w

    def rank(self, t, i, mode):
        V = len(self.uni)
        N = sum(self.uni.values())
        s = ['<s>'] + t + ['</s>']
        L, R = s[i], s[i + 2]
        scores = {}
        for g, c in self.uni.items():
            if c <= 0:
                continue
            pu = (c + 0.1) / (N + 0.1 * V)
            if mode == 'unigram':
                sc = math.log(pu)
            else:
                bl = self.big[L]
                pl = (bl[g] + 2 * pu) / (sum(bl.values()) + 2)
                sc = math.log(pl)
                if mode in ('both', 'slot'):
                    br = self.rbig[R]
                    pr = (br[g] + 2 * pu) / (sum(br.values()) + 2)
                    sc += math.log(pr) - math.log(pu)
                    tr = self.tri[(L, R)]
                    if tr:
                        sc = 0.5 * sc + 0.5 * math.log((tr[g] + 1 * math.exp(sc)) / (sum(tr.values()) + 1))
                if mode == 'slot' and R == '</s>' and i >= 1:
                    e = self.end[s[i]]
                    if e:
                        sc += 0.5 * math.log((e[g] + 1 * pu) / (sum(e.values()) + 1) / pu)
            scores[g] = sc
        order = sorted(scores, key=lambda g: -scores[g])
        return order.index(t[i]) if t[i] in scores else 10 ** 6


def p1(rows):
    say('## P1 A slot grammar as a predictor of a hidden sign')
    say()
    texts = [r['seq'][0] for r in rows if r['complete'] == 'Y' and len(r['seq']) == 1 and len(r['seq'][0]) >= 3]
    random.shuffle(texts)
    texts = texts[:1200]
    m = Model(texts)
    res = defaultdict(lambda: [0, 0, 0])
    respos = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    for t in texts:
        m.add(t, -1)
        for i in range(len(t)):
            pos = 'first' if i == 0 else ('last' if i == len(t) - 1 else 'middle')
            for mode in ('unigram', 'left', 'both', 'slot'):
                k = m.rank(t, i, mode)
                res[mode][0] += k == 0
                res[mode][1] += k < 5
                res[mode][2] += 1
                respos[mode][pos][0] += k == 0
                respos[mode][pos][1] += 1
        m.add(t, 1)
    say('Leave-one-text-out on %d complete one-line texts of 3+ signs; every sign hidden in turn.' % len(texts))
    say()
    say('| model | top-1 | top-5 | first sign top-1 | middle top-1 | last sign top-1 |')
    say('|---|---|---|---|---|---|')
    names = {'unigram': 'commonest sign', 'left': 'left neighbour', 'both': 'both neighbours',
             'slot': 'both neighbours + ending grid'}
    for mode in ('unigram', 'left', 'both', 'slot'):
        a, b, n = res[mode]
        say('| %s | %.1f%% | %.1f%% | %s |' % (names[mode], 100 * a / n, 100 * b / n, ' | '.join(
            '%.1f%%' % (100 * respos[mode][p][0] / respos[mode][p][1]) for p in ('first', 'middle', 'last'))))
    say()


def main():
    rows = [r for r in load() if r['flat']]
    say('# Seventh pass: ritual pictures, time depth, a slot grammar')
    say()
    r1(rows)
    r1b(rows)
    t1(rows)
    p1(rows)
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'seventh.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
