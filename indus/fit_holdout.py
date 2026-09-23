"""Fitted keys on unseen texts: does a key fitted in one language carry over to new inscriptions?

A key fitted to the corpus reads about 93% of it in any language (bench.py B5b): fitting alone proves
nothing. The test that could discriminate is generalisation. For each language:

H1  Fit a syllabic key on the training texts (the ICIT-derived lines of 3+ signs): the 250 commonest
    signs each get one value from a syllable inventory (consonant class x vowel class, a bare vowel
    or a bare consonant; bench.skelv classes), by hill-climbing the vowel-aware reading score, credited on consonants covered by words of 3+
    consonants (vowels earn nothing: with every sign a syllable, nearly any vowel pattern finds a word).
H2  Read the held-out texts (the M77-only lines of 3+ signs, minus any that repeat a training text
    exactly) with the fitted key, against 100 shuffles of the fitted key (values permuted among
    signs of similar frequency). A key that has found something true about the language keeps an
    edge on new texts; a key that has only memorised the training texts falls back to its shuffles.
H3  Control for memorising: the same fit on sign-shuffled training lines (the signs of each line in
    random order), read on the held-out texts the same way.
H4  Power: a synthetic language (real Dravidian words written with a random syllabic sign key of the
    corpus's size), split into training and held-out halves, fitted and tested the same way.

Usage: python fit_holdout.py <mw.txt> <dedr forms.csv> <sux_gloss.tsv> <scout folder> [steps]
Writes results/fit_holdout.md.
"""
import os
import random
import sys
from collections import Counter, defaultdict

import bench
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
CONS = sorted(set(bench.CLASS.values()))
VALUES = [c.upper() + v for c in CONS for v in 'aiu'] + list('aiu') + [c.upper() for c in CONS]


def say(s=''):
    OUT.append(s)
    print(s)


def runs_raw(t, key):
    out, cur = [], ''
    for g in t:
        v = key.get(g)
        if v is None:
            if cur:
                out.append(cur)
            cur = ''
        else:
            cur += v
    if cur:
        out.append(cur)
    return out


def norm(s):
    import re
    return re.sub(r'(.)\1+', r'\1', s)


def coverage_c(s, words, ends, maxlen=14):
    """Best parse of a vowel-aware skeleton into lexicon words (+ one ending consonant); credit = the
    consonants covered by words of 3+ consonants (vowels give no credit: with every sign a syllable,
    nearly any vowel pattern finds some word)."""
    n = len(s)
    best = [-1] * (n + 1)
    best[0] = 0
    for i in range(n):
        if best[i] < 0:
            continue
        for L in range(1, min(maxlen, n - i) + 1):
            w = s[i:i + L]
            if w in words or (L > 1 and w[:-1] in words and w[-1] in ends):
                k = sum(1 for ch in w if ch.isupper())
                v = best[i] + (k if k >= 3 else 0)
                if v > best[i + L]:
                    best[i + L] = v
    return max(best[n], 0)


def score_text(t, key, lex, ends):
    c = n = 0
    for s in runs_raw(t, key):
        s = norm(s)
        n += sum(1 for ch in s if ch.isupper())
        c += coverage_c(s, lex, ends)
    return c, n


def score(texts, key, lex, ends):
    c = n = 0
    for t in texts:
        a, b = score_text(t, key, lex, ends)
        c += a
        n += b
    return c / n if n else 0.0


def fit(texts, lex, ends, rng, steps, nsigns=250):
    freq = Counter(g for t in texts for g in t)
    signs = [g for g, _ in freq.most_common(nsigns)]
    key = {g: rng.choice(VALUES) for g in signs}
    idx = defaultdict(set)
    for i, t in enumerate(texts):
        for g in t:
            idx[g].add(i)
    per = [score_text(t, key, lex, ends) for t in texts]
    for _ in range(steps):
        g = rng.choice(signs)
        old = key[g]
        key[g] = rng.choice(VALUES)
        new = {i: score_text(texts[i], key, lex, ends) for i in idx[g]}
        if sum(new[i][0] - per[i][0] for i in new) >= 0:
            for i in new:
                per[i] = new[i]
        else:
            key[g] = old
    return key, sum(c for c, _ in per) / max(1, sum(n for _, n in per))


def shuffled_keys(key, freq, rng, n=100, band=10):
    signs = sorted(key, key=lambda g: -freq[g])
    bands = [signs[i:i + band] for i in range(0, len(signs), band)]
    for _ in range(n):
        k2 = {}
        for b in bands:
            vals = [key[g] for g in b]
            rng.shuffle(vals)
            k2.update(zip(b, vals))
        yield k2


def test(label, train, held, lex, ends, rng, steps):
    key, tr = fit(train, lex, ends, rng, steps)
    freq = Counter(g for t in train + held for g in t)
    real = score(held, key, lex, ends)
    sims = sorted(score(held, k2, lex, ends) for k2 in shuffled_keys(key, freq, rng))
    ge = sum(1 for s in sims if s >= real)
    say('| %s | %.1f%% | %.1f%% | %.1f%% (%.1f-%.1f) | %d of 100 |' % (
        label, 100 * tr, 100 * real, 100 * sims[50], 100 * sims[0], 100 * sims[-1], ge))
    return real, sims[50], ge


def main(mw, dedr, sux, scout, steps='6000'):
    steps = int(steps)
    rng = random.Random(113)
    _, _, raw = bench.lexicons(mw, dedr, sux)
    raw.update({L: v for L, v in bench.extra_raw(scout).items() if v})
    lexv = {L: {bench.skelv(w) for w in ws if bench.skelv(w)} for L, ws in raw.items()}
    train = [ln for r in load() for ln in r['seq'] if len(ln) >= 3]
    tset = {tuple(t) for t in train}
    held = []
    for r in load(only_m77=True):
        for ln in r['seq']:
            ln = [g for g in ln if g != '?']
            if len(ln) >= 3 and tuple(ln) not in tset:
                held.append(ln)
    say('# Fitted keys on unseen texts')
    say()
    say('- training: %d ICIT-derived lines of 3+ signs; held out: %d M77-only lines of 3+ signs that do not repeat a '
        'training line. Key: the 250 commonest training signs, %d possible values (consonant class x vowel class, bare '
        'vowels, bare consonants), %d hill-climbing steps on the vowel-aware score.' % (
            len(train), len(held), len(VALUES), steps))
    say()
    say('## H1-H2 Fitted in each language, read on the held-out texts')
    say()
    say('| language | training score | held-out score | held-out, shuffles of the fitted key median (range) | '
        'shuffles as good |')
    say('|---|---|---|---|---|')
    res = {}
    for L in ('dra', 'sa', 'sux', 'mu', 'ta', 'bu'):
        res[L] = test(bench.LANGNAME[L], train, held, lexv[L], bench.ENDINGS_V[L], rng, steps)
    say()
    say('## H3 The same fit on sign-shuffled training lines (memorising control)')
    say()
    say('| language | training score | held-out score | shuffles median (range) | shuffles as good |')
    say('|---|---|---|---|---|')
    strain = []
    for t in train:
        u = list(t)
        rng.shuffle(u)
        strain.append(u)
    for L in ('dra', 'sa'):
        test(bench.LANGNAME[L] + ', shuffled training', strain, held, lexv[L], bench.ENDINGS_V[L], rng, steps)
    say()
    say('## H4 Power: a synthetic language with a planted key')
    say()
    words = [w for w in raw['dra'] if 2 <= len(bench.skelv(w)) <= 6]
    freq = Counter(g for t in train for g in t)
    signs = [g for g, _ in freq.most_common(250)]
    sylls = Counter()
    for w in words[:20000]:
        s = bench.skelv(w)
        i = 0
        while i < len(s):
            if s[i].isupper() and i + 1 < len(s) and s[i + 1] in 'aiu':
                sylls[s[i:i + 2]] += 1
                i += 2
            else:
                sylls[s[i]] += 1
                i += 1
    inv = [x for x, _ in sylls.most_common(len(signs))]
    truth = {}
    for j, g in enumerate(signs):
        truth[g] = inv[j % len(inv)]
    by = defaultdict(list)
    for g, v in truth.items():
        by[v].append(g)

    def encode(w):
        s = bench.skelv(w)
        out, i = [], 0
        while i < len(s):
            if s[i].isupper() and i + 1 < len(s) and s[i + 1] in 'aiu' and s[i:i + 2] in by:
                out.append(rng.choice(by[s[i:i + 2]]))
                i += 2
            elif s[i] in by:
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
    half = len(train)
    say('| setting | training score | held-out score | shuffles median (range) | shuffles as good |')
    say('|---|---|---|---|---|')
    test('synthetic Dravidian, planted key', syn[:half], syn[half:], lexv['dra'], bench.ENDINGS_V['dra'], rng, steps)
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'fit_holdout.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:6])
