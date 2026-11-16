"""Ciphertext-only and crib attack on the note as a monoalphabetic substitution of Arabic letters, with controls.

    python crib_attack.py [--restarts N] [--iters N] [--controls N]

Hypothesis tested: each of the note's 26 distinct groups stands for one Arabic letter (no vowels, no word division),
and the clear Arabic words on the leaf are part of the same plaintext. The plaintext model is a letter trigram
(interpolated with bigram and unigram) trained on the first 85 percent of lang/corpora/ar-wikipedia-sample.txt.

With 26 free symbols and 119 letters an optimiser overfits any text, so the number that means something is not the
score but where it falls between two controls run through the same code:
  - real: 119-letter slices of held-out Arabic (the last 15 percent of the corpus), enciphered with a random key;
  - null: the note's own groups in shuffled order (same symbol frequencies, no sequence structure).
If the note's best score sits with the null, the substitution hypothesis is not supported, whatever the output looks like.
"""
import math, os, random, sys
from collections import Counter

import numpy as np

import analysis as A

HERE = os.path.dirname(os.path.abspath(__file__))
L = A.LETTERS
IDX = {c: i for i, c in enumerate(L)}


def arabic_text():
    t = open(os.path.join(A.ROOT, 'lang', 'corpora', 'ar-wikipedia-sample.txt'), encoding='utf-8').read()
    t = ''.join(A.FOLD.get(c, c) for c in t)
    return [IDX[c] for c in t if c in IDX]


def trigram_table(seq):
    n = len(L)
    u = np.ones(n) * 0.5; b = np.ones((n, n)) * 0.1; t = np.ones((n, n, n)) * 0.02
    s = np.array(seq)
    np.add.at(u, s, 1); np.add.at(b, (s[:-1], s[1:]), 1); np.add.at(t, (s[:-2], s[1:-1], s[2:]), 1)
    pu = u / u.sum(); pb = b / b.sum(axis=1, keepdims=True); pt = t / t.sum(axis=2, keepdims=True)
    P = 0.55 * pt + 0.30 * pb[None, :, :] + 0.15 * pu[None, None, :]
    return np.log(P), np.log(pu)


T3, U1 = trigram_table(arabic_text()[:int(len(arabic_text()) * 0.85)])


def seq_score(plain):
    """Log-probability of a letter-index array under the trigram model (first two letters by unigram)."""
    p = np.asarray(plain)
    return float(U1[p[0]] + U1[p[1]] + T3[p[:-2], p[1:-1], p[2:]].sum())


def anneal(cipher, nsym, rng, iters, fixed=None):
    """Find the injective symbol->letter key that maximises seq_score. `fixed` is an optional list of
    (position, letter) pairs forced into the plaintext (clear words); cipher positions index the symbols, and
    fixed letters are spliced in by `build`. Returns (best score, key)."""
    n = len(L)
    key = np.array(rng.sample(range(n), nsym))
    cipher = np.asarray(cipher)

    def plain_of(k):
        return build(k[cipher], fixed) if fixed else k[cipher]

    cur = seq_score(plain_of(key)); best = cur; bestkey = key.copy()
    T0, T1 = 3.0, 0.05
    for it in range(iters):
        temp = T0 * (T1 / T0) ** (it / iters)
        k2 = key.copy()
        if rng.random() < 0.7:
            a, b = rng.sample(range(nsym), 2); k2[a], k2[b] = k2[b], k2[a]
        else:
            a = rng.randrange(nsym); free = [x for x in range(n) if x not in set(key)]
            k2[a] = rng.choice(free)
        s = seq_score(plain_of(k2))
        if s >= cur or rng.random() < math.exp((s - cur) / temp):
            key, cur = k2, s
            if cur > best: best, bestkey = cur, key.copy()
    return best, bestkey


def build(letters_for_groups, fixed):
    """Splice clear-word letters into the plaintext: fixed is a list of (group_index, [letter indices]) meaning
    those letters stand before that group."""
    out = []; g = list(letters_for_groups); fi = 0
    ins = dict()
    for pos, ls in fixed: ins.setdefault(pos, []).extend(ls)
    for i, x in enumerate(g):
        if i in ins: out.extend(ins[i])
        out.append(int(x))
    if len(g) in ins: out.extend(ins[len(g)])
    return np.array(out)


def word(w):
    return [IDX[A.FOLD.get(c, c)] for c in w if A.FOLD.get(c, c) in IDX]


def clear_cribs(g):
    """Clear Arabic read as H or M confidence in clear_words.md, spliced before the group that follows it."""
    rows = [ln.split() for ln in open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8') if not ln.startswith('#')]
    start = [0]
    for r in rows: start.append(start[-1] + len(r))
    fixed = [(start[4] + 2, word('كما سبق التحرير')),           # row 5 after 62 38
             (start[10] + 3, word('كل')),                        # row 11 after 14 39 82
             (start[15], word('المذكورين أخبرنا بأنه لم يعطهم')),  # closing line 1, before 38 75 34 49
             (len(g), word('حصل') + word('حضورهم لنا فنعطي لكل'))]
    return fixed


def decode(key, syms, g):
    m = {s: L[k] for s, k in zip(syms, key)}
    return ''.join(m[v] for v in g), m


def main():
    restarts = int(sys.argv[sys.argv.index('--restarts') + 1]) if '--restarts' in sys.argv else 12
    iters = int(sys.argv[sys.argv.index('--iters') + 1]) if '--iters' in sys.argv else 20000
    ncontrol = int(sys.argv[sys.argv.index('--controls') + 1]) if '--controls' in sys.argv else 8
    rng = random.Random(7)
    g = A.groups(); n = len(g)
    syms = sorted(set(g)); sidx = {s: i for i, s in enumerate(syms)}
    cipher = [sidx[v] for v in g]
    held = arabic_text()[int(len(arabic_text()) * 0.85):]

    def best_of(c, ns, fixed=None):
        return max(anneal(c, ns, rng, iters, fixed)[0] for _ in range(restarts))

    # note, ciphertext only
    note_best = None
    for _ in range(restarts):
        s, k = anneal(cipher, len(syms), rng, iters)
        if note_best is None or s > note_best[0]: note_best = (s, k)
    per = lambda s, m: s / m
    print(f'note: {n} groups, {len(syms)} symbols; best score {note_best[0]:.1f} ({note_best[0] / n:.3f} per letter)')
    # null: shuffled note
    nulls = []
    for i in range(ncontrol):
        sh = cipher[:]; rng.shuffle(sh); nulls.append(best_of(sh, len(syms)))
    # real: held-out Arabic slices enciphered with random keys, 119 letters, reduced to their own symbol set
    reals = []
    for i in range(ncontrol):
        a = rng.randrange(0, len(held) - n); sl = held[a:a + n]
        keym = {}; perm = rng.sample(range(len(L)), len(L))
        cs = [perm[x] for x in sl]; ss = sorted(set(cs)); mp = {x: j for j, x in enumerate(ss)}
        reals.append(best_of([mp[x] for x in cs], len(ss)))
    print(f'null  (note shuffled, {ncontrol}): mean {np.mean(nulls):.1f}  range {min(nulls):.1f} to {max(nulls):.1f}')
    print(f'real  (held-out Arabic, {ncontrol}): mean {np.mean(reals):.1f}  range {min(reals):.1f} to {max(reals):.1f}')
    lo, hi = np.mean(nulls), np.mean(reals)
    print(f'note position between null and real: {(note_best[0] - lo) / (hi - lo):.2f} (0 = null, 1 = real)')
    plain, m = decode(note_best[1], syms, g)
    print('\nbest ciphertext-only decode (letters, no vowels):\n', plain)
    print('key:', {s: m[s] for s in sorted(m, key=lambda s: -Counter(g)[s])})

    # with the clear words spliced in
    fixed = clear_cribs(g)
    cb = None
    for _ in range(restarts):
        s, k = anneal(cipher, len(syms), rng, iters, fixed)
        if cb is None or s > cb[0]: cb = (s, k)
    plain2, m2 = decode(cb[1], syms, g)
    print(f'\nwith the clear words spliced in as known plaintext: best score {cb[0]:.1f}')
    print(plain2)
    print('key:', {s: m2[s] for s in sorted(m2, key=lambda s: -Counter(g)[s])})


if __name__ == '__main__':
    main()
