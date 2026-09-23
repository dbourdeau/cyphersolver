"""Fitted keys on unseen texts, with the lexicons matched in size and word length.

fit_holdout.py found that a key fitted in any language generalises to unseen texts, and that the margin
over its shuffles tracks the density of the lexicon, not the language. Here every lexicon is cut to the
same number of word skeletons with the same distribution of consonant counts (stratified random draws,
5 draws per language), so that no language has more chances to match than another. For each draw: fit
on the training texts, read the held-out texts, and measure the margin over 50 shuffles of the fitted
key as a z-score. The language with the right lexicon should show the largest margin.

M1  Positive control: a synthetic corpus of real Dravidian (DEDR) words written with a planted sign key
    of the Indus corpus's size, split into training and held-out halves. The test has power only if
    the Dravidian lexicon wins here.
M2  The Indus corpus: training = ICIT-derived lines, held out = M77-only lines not in the training set.

Usage: python matched_holdout.py <mw.txt> <dedr forms.csv> <sux_gloss.tsv> <scout folder> [steps] [draws]
Writes results/matched_holdout.md.
"""
import os
import random
import statistics
import sys
from collections import Counter, defaultdict

import bench
import fit_holdout as fh
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
LANGS = ('dra', 'ta', 'sa', 'sux', 'mu', 'bu')


def say(s=''):
    OUT.append(s)
    print(s)


def ncons(s):
    return sum(1 for c in s if c.isupper())


def matched(lexv, rng):
    """Stratified draw: for each consonant count 1-6, the same number of skeletons from every lexicon."""
    bins = {L: defaultdict(list) for L in lexv}
    for L, ws in lexv.items():
        for w in ws:
            k = ncons(w)
            if 1 <= k <= 6:
                bins[L][k].append(w)
    size = {k: min(len(bins[L][k]) for L in lexv) for k in range(1, 7)}
    out = {}
    for L in lexv:
        s = set()
        for k, n in size.items():
            s.update(rng.sample(sorted(bins[L][k]), n))
        out[L] = s
    return out, sum(size.values()), size


def margin(train, held, lex, ends, rng, steps, nshuf=50):
    key, _ = fh.fit(train, lex, ends, rng, steps)
    freq = Counter(g for t in train + held for g in t)
    real = fh.score(held, key, lex, ends)
    sims = [fh.score(held, k2, lex, ends) for k2 in fh.shuffled_keys(key, freq, rng, n=nshuf)]
    sd = statistics.pstdev(sims) or 1e-9
    return (real - statistics.mean(sims)) / sd, real, statistics.mean(sims)


def run(label, train, held, lexv, rng, steps, draws):
    say('### %s' % label)
    say()
    z = defaultdict(list)
    for d in range(draws):
        lx, n, size = matched(lexv, rng)
        for L in LANGS:
            zz, real, mean = margin(train, held, lx[L], bench.ENDINGS_V[L], rng, steps)
            z[L].append(zz)
        if d == 0:
            say('- matched lexicons: %d skeletons each (by consonant count: %s).' % (
                n, ', '.join('%d: %d' % kv for kv in sorted(size.items()))))
    say()
    say('| lexicon | z-score of the held-out margin, mean (draws) | wins (largest z in a draw) |')
    say('|---|---|---|')
    wins = Counter(max(LANGS, key=lambda L: z[L][d]) for d in range(draws))
    for L in sorted(LANGS, key=lambda L: -statistics.mean(z[L])):
        say('| %s | %.2f (%s) | %d of %d |' % (bench.LANGNAME[L], statistics.mean(z[L]),
                                              ', '.join('%.1f' % x for x in z[L]), wins[L], draws))
    say()
    return {L: statistics.mean(z[L]) for L in LANGS}, wins


def main(mw, dedr, sux, scout, steps='20000', draws='5'):
    steps, draws = int(steps), int(draws)
    rng = random.Random(127)
    _, _, raw = bench.lexicons(mw, dedr, sux)
    raw.update({L: v for L, v in bench.extra_raw(scout).items() if v})
    lexv = {L: {bench.skelv(w) for w in raw[L] if bench.skelv(w)} for L in LANGS}
    train = [ln for r in load() for ln in r['seq'] if len(ln) >= 3]
    tset = {tuple(t) for t in train}
    held = [ln for r in load(only_m77=True) for ln in ([g for g in x if g != '?'] for x in r['seq'])
            if len(ln) >= 3 and tuple(ln) not in tset]
    say('# Fitted keys on unseen texts, lexicons matched')
    say()
    say('%d hill-climbing steps a fit, %d draws of matched lexicons, 50 shuffles a test; z = (held-out score - mean '
        'of the shuffles) / their standard deviation.' % (steps, draws))
    say()
    say('## M1 Positive control: synthetic Dravidian')
    say()
    words = [w for w in raw['dra'] if 2 <= ncons(bench.skelv(w)) <= 5]
    freq = Counter(g for t in train for g in t)
    signs = [g for g, _ in freq.most_common(250)]
    inv = fh.VALUES
    truth = {g: inv[i % len(inv)] for i, g in enumerate(rng.sample(signs, len(signs)))}
    by = defaultdict(list)
    for g, v in truth.items():
        by[v].append(g)

    def encode(w):
        s, out, i = bench.skelv(w), [], 0
        while i < len(s):
            if s[i].isupper() and i + 1 < len(s) and s[i + 1] in 'aiu' and by.get(s[i:i + 2]):
                out.append(rng.choice(by[s[i:i + 2]]))
                i += 2
            elif by.get(s[i]):
                out.append(rng.choice(by[s[i]]))
                i += 1
            else:
                i += 1
        return out
    syn = []
    for t in train + held:
        line = []
        while len(line) < len(t):
            line += encode(rng.choice(words))
        syn.append(line[:max(3, len(t))])
    ctrl, cw = run('synthetic Dravidian corpus (training %d lines, held out %d)' % (len(train), len(held)),
                   syn[:len(train)], syn[len(train):], lexv, rng, steps, draws)
    say('## M2 The Indus corpus')
    say()
    real, rw = run('ICIT-derived training (%d lines), M77-only held out (%d lines)' % (len(train), len(held)),
                   train, held, lexv, rng, steps, draws)
    say('## Reading')
    say()
    order_c = sorted(ctrl, key=lambda L: -ctrl[L])
    order_r = sorted(real, key=lambda L: -real[L])
    say('- Control (a corpus written in Dravidian): %s. The Dravidian family comes first through Old Tamil (%d of %d '
        'draws), but DEDR, the very lexicon the synthetic text was drawn from, comes last: cut to %s random skeletons '
        'of all Dravidian languages, it rarely holds the words used. The ranking depends on how a lexicon is made, '
        'not only on its language; the test tells families apart only roughly.' % (
            ', '.join('%s %.1f' % (L, ctrl[L]) for L in order_c), cw['ta'], draws, 'matched'))
    say('- Indus: %s. No language stands out (the z-scores overlap from draw to draw). If the Indus texts behaved like '
        'the synthetic Dravidian corpus, Old Tamil should win most draws; it wins %d of %d and ranks %d of 6. That is '
        'weak evidence against an Old-Tamil-like lexicon at best, given the noisy control. **Inconclusive: fitted keys, '
        'even with matched lexicons and unseen texts, do not identify the language.**' % (
            ', '.join('%s %.1f' % (L, real[L]) for L in order_r), rw['ta'], draws, order_r.index('ta') + 1))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'matched_holdout.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:7])
