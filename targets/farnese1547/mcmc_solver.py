"""mcmc_solver.py -- Simulated Annealing homophonic & prefix-code solver with shuffled null controls.

Supports:
1. Tokenized homophonic substitution (from prefix-free 1+2-digit or fixed 2-digit segmentation).
   Tokens can map to single letters (a..z, early Italian), common cipher digraphs/words (che, et, non, per, con), or NULL ('').
2. Built-in 10-20 shuffled token-stream null controls to compute true z-scores (Bianco 1466 gold standard).
"""
import collections
import math
import pathlib
import random
import sys
import time
import numpy as np

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from lm_harness import load_it_lms, LexiconScorer, score_with_null_controls

ALPHA_EARLY = 'abcdefghilmnopqrstuz'  # 20 letters (j->i, v->u, no k/w/x/y)
EXPECT = {
    'a': .117, 'b': .009, 'c': .045, 'd': .037, 'e': .118, 'f': .010, 'g': .016, 'h': .015,
    'i': .113, 'l': .065, 'm': .025, 'n': .069, 'o': .098, 'p': .031, 'q': .005, 'r': .064,
    's': .050, 't': .056, 'u': .051, 'z': .005,
}
COMMON_MULTI = ['che', 'et', 'non', 'per', 'con', '']  # optional frequent codes/null


def kl_penalty(counts, mu=0.5):
    n = sum(counts.values())
    if n == 0 or mu == 0:
        return 0.0
    kl = 0.0
    for l, c in counts.items():
        if c:
            kl += (c / n) * math.log((c / n) / EXPECT.get(l, 1e-3))
    return -mu * n * kl


def score_decoded_fast(plain, lm_ns, mu=0.5, null_pen=2.5, n_nulls=0):
    if len(plain) < 6:
        return -1e9
    sc = lm_ns.score(plain)
    counts = collections.Counter(plain)
    sc += kl_penalty(counts, mu)
    sc -= null_pen * n_nulls
    return sc


def sa_solve_tokens(toks, lm_ns, iters=25000, seed=1, mu=0.6, allow_multi=True, fixed=None,
                    one_digit_vowels=None, T0=6.0, T1=0.15):
    """Anneal a mapping token -> plaintext string over segmented token list toks."""
    rng = random.Random(seed)
    fixed = dict(fixed or {})
    freq = collections.Counter(toks)
    vocab = sorted(freq.keys(), key=lambda t: (-freq[t], t))
    if not vocab:
        return {}, '', -1e9

    # Candidate outputs weighted realistically
    letters_pool = list(ALPHA_EARLY) + list('aeioaeiounrstlc')
    multi_pool = list(COMMON_MULTI) if allow_multi else []

    # Initialize mapping
    mapping = {}
    vowels_rem = list('aeiou')
    rng.shuffle(vowels_rem)
    for t in vocab:
        if t in fixed:
            mapping[t] = fixed[t]
        elif one_digit_vowels and t in one_digit_vowels:
            mapping[t] = vowels_rem.pop() if vowels_rem else rng.choice('aeiou')
        elif len(t) == 1:
            mapping[t] = rng.choice('aeioulnrstm')
        else:
            mapping[t] = rng.choice(letters_pool)

    def _eval(mp):
        parts = [mp[t] for t in toks]
        n_nulls = sum(1 for p in parts if p == '')
        plain = ''.join(parts)
        return score_decoded_fast(plain, lm_ns, mu=mu, null_pen=3.5, n_nulls=n_nulls), plain

    cur_sc, cur_plain = _eval(mapping)
    best_sc, best_mp, best_plain = cur_sc, dict(mapping), cur_plain

    free_syms = [t for t in vocab if t not in fixed]
    weights = [math.sqrt(freq[t]) for t in free_syms]

    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / max(1, iters))
        r = rng.random()
        if r < 0.35 and len(free_syms) >= 2:
            # Swap two tokens' values
            a, b = rng.choices(free_syms, weights, k=2)
            if a == b or mapping[a] == mapping[b]:
                continue
            old_a, old_b = mapping[a], mapping[b]
            mapping[a], mapping[b] = old_b, old_a
            nsc, nplain = _eval(mapping)
            delta = nsc - cur_sc
            if delta > 0 or rng.random() < math.exp(delta / T):
                cur_sc, cur_plain = nsc, nplain
                if cur_sc > best_sc:
                    best_sc, best_mp, best_plain = cur_sc, dict(mapping), cur_plain
            else:
                mapping[a], mapping[b] = old_a, old_b
        else:
            a = rng.choices(free_syms, weights, k=1)[0]
            old_a = mapping[a]
            if one_digit_vowels and a in one_digit_vowels:
                nv = rng.choice('aeiou')
            elif allow_multi and len(a) == 2 and rng.random() < 0.15:
                nv = rng.choice(multi_pool)
            else:
                nv = rng.choice(letters_pool)
            if nv == old_a:
                continue
            mapping[a] = nv
            nsc, nplain = _eval(mapping)
            delta = nsc - cur_sc
            if delta > 0 or rng.random() < math.exp(delta / T):
                cur_sc, cur_plain = nsc, nplain
                if cur_sc > best_sc:
                    best_sc, best_mp, best_plain = cur_sc, dict(mapping), cur_plain
            else:
                mapping[a] = old_a

    return best_mp, best_plain, best_sc


def run_with_null_controls(toks, lm_ns, lex, iters=20000, restarts=3, n_controls=10,
                           allow_multi=True, fixed=None, one_digit_vowels=None):
    """Run SA (best of `restarts`) on real toks, and 1 run each on `n_controls` shuffled token streams."""
    best_real = None
    for s in range(1, restarts + 1):
        mp, plain, sc = sa_solve_tokens(
            toks, lm_ns, iters=iters, seed=s * 101, allow_multi=allow_multi,
            fixed=fixed, one_digit_vowels=one_digit_vowels,
        )
        per_ch = lm_ns.per_char(plain) if len(plain) > 10 else -9.9
        if best_real is None or sc > best_real['score']:
            best_real = {'score': sc, 'per_ch': per_ch, 'plain': plain, 'map': mp}

    _, cov4, cov5 = lex.segment(best_real['plain'])
    best_real['cov4'] = cov4
    best_real['cov5'] = cov5

    rng = random.Random(1547)
    ctrl_scores = []
    ctrl_per_ch = []
    ctrl_cov5 = []
    for c in range(n_controls):
        shuf = list(toks)
        rng.shuffle(shuf)
        _, cplain, csc = sa_solve_tokens(
            shuf, lm_ns, iters=iters, seed=1000 + c, allow_multi=allow_multi,
            fixed=fixed, one_digit_vowels=one_digit_vowels,
        )
        _, _, ccov5 = lex.segment(cplain)
        ctrl_scores.append(csc)
        ctrl_per_ch.append(lm_ns.per_char(cplain) if len(cplain) > 10 else -9.9)
        ctrl_cov5.append(ccov5)

    def _z(val, arr):
        m = sum(arr) / len(arr)
        sd = math.sqrt(sum((x - m) ** 2 for x in arr) / max(1, len(arr) - 1)) or 1e-9
        return m, sd, (val - m) / sd

    sc_m, sc_sd, sc_z = _z(best_real['score'], ctrl_scores)
    pc_m, pc_sd, pc_z = _z(best_real['per_ch'], ctrl_per_ch)
    c5_m, c5_sd, c5_z = _z(best_real['cov5'], ctrl_cov5)
    return {
        'real': best_real,
        'score_z': sc_z, 'score_ctrl': (sc_m, sc_sd),
        'per_ch_z': pc_z, 'per_ch_ctrl': (pc_m, pc_sd),
        'cov5_z': c5_z, 'cov5_ctrl': (c5_m, c5_sd),
    }


if __name__ == '__main__':
    print('mcmc_solver module ready.')
