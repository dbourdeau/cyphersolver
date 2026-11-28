#!/usr/bin/env python3
"""1580s Spanish cifra-general solver (1-char, 2-char CV, nulls, nomenclators) & strict dynamic validator."""
import collections
import math
import pathlib
import random
import statistics
import sys
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lm_goldenage1583 import load_spanish_lms, GoldenAge1583Lexicon, clm

ES_ALPHA = list('eaosnrildtcumpqbgyfhzx')
ES_PROBS = {
    'e': 0.138, 'a': 0.124, 'o': 0.089, 's': 0.079, 'n': 0.068,
    'r': 0.067, 'i': 0.063, 'l': 0.052, 'd': 0.050, 't': 0.045,
    'u': 0.044, 'c': 0.043, 'm': 0.032, 'p': 0.026, 'q': 0.019,
    'b': 0.016, 'y': 0.012, 'g': 0.011, 'f': 0.008, 'h': 0.009,
    'z': 0.005, 'x': 0.003,
}
ES_BIGRAMS = [
    'de', 'en', 'es', 'el', 'la', 'lo', 'le', 'se', 'no', 'su', 'un', 'al', 'os',
    'as', 'ar', 'er', 'or', 'an', 'in', 'on', 'ra', 're', 'ri', 'ro', 'ta', 'te',
    'to', 'ca', 'co', 'da', 'do', 'ma', 'me', 'mi', 'na', 'pa', 'pe', 'po', 'qu',
]


def sukhotin_stream(tokens):
    alpha = sorted(set(tokens))
    idx = {t: i for i, t in enumerate(alpha)}
    k = len(alpha)
    adj = [[0] * k for _ in range(k)]
    rsum = [0] * k
    for a, b in zip(tokens, tokens[1:]):
        if a != b:
            ia, ib = idx[a], idx[b]
            adj[ia][ib] += 1
            adj[ib][ia] += 1
            rsum[ia] += 1
            rsum[ib] += 1
    vowels = set()
    rem = set(range(k))
    sc = list(rsum)
    while rem:
        b = max(rem, key=lambda i: sc[i])
        if sc[b] <= 0:
            break
        vowels.add(b)
        rem.remove(b)
        for j in rem:
            sc[j] -= 2 * adj[b][j]
    vset = {alpha[i] for i in vowels}
    same = sum(1 for a, b in zip(tokens, tokens[1:]) if (a in vset) == (b in vset))
    diff = sum(1 for a, b in zip(tokens, tokens[1:]) if (a in vset) != (b in vset))
    return vset, set(alpha) - vset, diff / max(1, same + diff)


def profile_cipher(tokens, label='1583 Cipher'):
    n = len(tokens)
    ug = collections.Counter(tokens)
    ic = sum(v * (v - 1) for v in ug.values()) / max(1, n * (n - 1))
    ent = -sum((v / n) * math.log2(v / n) for v in ug.values())
    bg = collections.Counter(zip(tokens, tokens[1:]))
    tg = collections.Counter(zip(tokens, tokens[1:], tokens[2:]))
    vset, _, alt = sukhotin_stream(tokens)
    print(f'=== PROFILE: {label} ===')
    print(f'Tokens N={n}, |V|={len(ug)}, IC={ic:.5f}, H={ent:.3f} bits, Sukhotin alt={alt:.3f}')
    print('Top 25 tokens:', ug.most_common(25))
    print('Top 12 bigrams:', [(f'{a}+{b}', c) for (a, b), c in bg.most_common(12)])
    print('Top 10 trigrams:', [(f'{a}+{b}+{c}', cnt) for (a, b, c), cnt in tg.most_common(10) if cnt >= 2])
    return {'n': n, 'vocab': len(ug), 'ic': ic, 'vset': vset, 'ug': ug}


def solve_cifra_general(
    tokens,
    lm_ns,
    fixed=None,
    null_toks=None,
    allow_nulls=False,
    allow_2char_for=None,
    n_restarts=24,
    steps=25000,
    min_distinct=16,
    max_null_frac=0.08,
    kl_weight=1.1,
    seed=1583,
):
    """Unspaced SA + greedy 1-opt & swap polish for 1580s Spanish homophonic/syllabic ciphers."""
    rng = random.Random(seed)
    fixed = dict(fixed or {})
    for nt in (null_toks or ()):
        fixed[nt] = ''
    allow_2char_set = set(allow_2char_for or ())

    all_toks = sorted(set(tokens))
    tok_counts = collections.Counter(tokens)
    tot_toks = len(tokens)
    V = len(all_toks)
    t2i = {t: i for i, t in enumerate(all_toks)}
    cnt_vec = np.array([tok_counts[t] for t in all_toks], dtype=np.float64)
    free_idxs = [i for i, t in enumerate(all_toks) if t not in fixed]
    free_sorted = sorted(free_idxs, key=lambda i: -cnt_vec[i])

    tok_arr = np.array([t2i[t] for t in tokens], dtype=np.int64)
    A_sz = len(lm_ns.alpha)
    c2i = {c: int(lm_ns.encode(c)[0]) for c in lm_ns.alpha}

    p_ref = np.full(A_sz, 1e-4, dtype=np.float64)
    for ch, pr in ES_PROBS.items():
        if ch in c2i:
            p_ref[c2i[ch]] = pr
    p_ref /= p_ref.sum()
    log_p_ref = np.log(p_ref)

    vset, _, _ = sukhotin_stream(tokens)
    vowels_top = ['e', 'a', 'o', 'i', 'u']
    v_w = [0.30, 0.28, 0.19, 0.14, 0.09]
    cons_top = ['s', 'n', 'r', 'l', 'd', 't', 'c', 'm', 'p', 'q', 'b', 'y', 'g', 'f', 'h', 'z', 'x']
    c_w = [0.13, 0.11, 0.11, 0.09, 0.09, 0.08, 0.08, 0.06, 0.05, 0.04, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.01]

    cands_1 = list(ES_ALPHA) + ([''] if allow_nulls else [])
    cands_2 = list(ES_ALPHA) + list(ES_BIGRAMS) + ([''] if allow_nulls else [])

    def str_to_ids(s):
        return [c2i[ch] for ch in s if ch in c2i]

    def eval_map(val_map, enc_ids):
        distinct_1 = {val_map[i] for i in range(V) if len(val_map[i]) == 1}
        if len(distinct_1) < min(min_distinct, V - (1 if allow_nulls else 0)):
            return -1e9, 0.0
        null_cnt = sum(cnt_vec[i] for i in range(V) if val_map[i] == '')
        if null_cnt / tot_toks > max_null_frac:
            return -1e9, 0.0

        if max((len(x) for x in enc_ids), default=0) <= 2:
            lut2 = np.full((V, 2), -1, dtype=np.int64)
            for idx, ids in enumerate(enc_ids):
                if len(ids) >= 1:
                    lut2[idx, 0] = ids[0]
                if len(ids) >= 2:
                    lut2[idx, 1] = ids[1]
            flat = lut2[tok_arr].ravel()
            seq = flat[flat >= 0]
        else:
            flat = [cid for ti in tok_arr for cid in enc_ids[ti]]
            seq = np.array(flat, dtype=np.int64)

        dec_chars = len(seq)
        if dec_chars < 10:
            return -1e9, 0.0

        dec_cnt = np.bincount(seq, minlength=A_sz).astype(np.float64)
        p_dec = dec_cnt / dec_chars
        nz = p_dec > 0
        kl = float(np.sum(p_dec[nz] * (np.log(p_dec[nz]) - log_p_ref[nz])))

        tot_lp = float(lm_ns.score_idx(seq))
        obj = tot_lp + 1.95 * dec_chars - kl_weight * dec_chars * kl
        return obj, tot_lp / dec_chars

    best_global_obj = -1e18
    best_global_map = None
    best_global_lpc = -99.0
    top_solutions = []

    for _ in range(n_restarts):
        val_map = [''] * V
        enc_ids = [[] for _ in range(V)]
        for t, fv in fixed.items():
            if t in t2i:
                nfv = clm.norm(fv, 'early', spaces=False)
                idx = t2i[t]
                val_map[idx] = nfv
                enc_ids[idx] = str_to_ids(nfv)

        used = {v for v in val_map if len(v) == 1}
        for rank, i in enumerate(free_sorted):
            tok = all_toks[i]
            if tok in allow_2char_set and rng.random() < 0.4:
                ch = rng.choice(ES_BIGRAMS)
            elif tok in vset:
                ch = rng.choices(vowels_top, weights=v_w, k=1)[0]
            elif rank < len(ES_ALPHA) and len(used) < min_distinct:
                rem = [c for c in ES_ALPHA[:18] if c not in used]
                ch = rng.choice(rem) if rem else rng.choices(cons_top, weights=c_w, k=1)[0]
            else:
                ch = rng.choices(cons_top, weights=c_w, k=1)[0]
            used.add(ch)
            val_map[i] = ch
            enc_ids[i] = str_to_ids(ch)

        cur_obj, cur_lpc = eval_map(val_map, enc_ids)
        best_obj, best_map, best_lpc = cur_obj, list(val_map), cur_lpc

        t_start, t_end = 12.0, 0.25
        for st in range(steps):
            frac = st / max(1, steps - 1)
            temp = t_start * ((t_end / t_start) ** frac)
            if len(free_idxs) >= 2 and rng.random() < 0.35:
                i1, i2 = rng.sample(free_idxs, 2)
                v1, v2 = val_map[i1], val_map[i2]
                if v1 == v2:
                    continue
                if len(v1) > 1 and all_toks[i2] not in allow_2char_set:
                    continue
                if len(v2) > 1 and all_toks[i1] not in allow_2char_set:
                    continue
                old1, old2 = enc_ids[i1], enc_ids[i2]
                val_map[i1], val_map[i2] = v2, v1
                enc_ids[i1], enc_ids[i2] = old2, old1
                no, nl = eval_map(val_map, enc_ids)
                d = no - cur_obj
                if d >= 0 or (d > -40 and rng.random() < math.exp(d / temp)):
                    cur_obj, cur_lpc = no, nl
                    if no > best_obj:
                        best_obj, best_map, best_lpc = no, list(val_map), nl
                else:
                    val_map[i1], val_map[i2] = v1, v2
                    enc_ids[i1], enc_ids[i2] = old1, old2
            else:
                i1 = rng.choice(free_idxs)
                v1 = val_map[i1]
                pool = cands_2 if all_toks[i1] in allow_2char_set else cands_1
                v2 = rng.choice(pool)
                if v2 == v1:
                    continue
                old1 = enc_ids[i1]
                val_map[i1] = v2
                enc_ids[i1] = str_to_ids(v2)
                no, nl = eval_map(val_map, enc_ids)
                d = no - cur_obj
                if d >= 0 or (d > -40 and rng.random() < math.exp(d / temp)):
                    cur_obj, cur_lpc = no, nl
                    if no > best_obj:
                        best_obj, best_map, best_lpc = no, list(val_map), nl
                else:
                    val_map[i1] = v1
                    enc_ids[i1] = old1

        val_map = list(best_map)
        enc_ids = [str_to_ids(v) for v in val_map]
        cur_obj, cur_lpc = eval_map(val_map, enc_ids)
        improved = True
        while improved:
            improved = False
            for i in free_sorted:
                orig = val_map[i]
                orig_e = enc_ids[i]
                best_loc_obj, best_loc_v, best_loc_lpc = cur_obj, orig, cur_lpc
                pool = cands_2 if all_toks[i] in allow_2char_set else cands_1
                for cand in pool:
                    if cand == orig:
                        continue
                    val_map[i] = cand
                    enc_ids[i] = str_to_ids(cand)
                    no, nl = eval_map(val_map, enc_ids)
                    if no > best_loc_obj + 1e-6:
                        best_loc_obj, best_loc_v, best_loc_lpc = no, cand, nl
                if best_loc_v != orig:
                    val_map[i] = best_loc_v
                    enc_ids[i] = str_to_ids(best_loc_v)
                    cur_obj, cur_lpc = best_loc_obj, best_loc_lpc
                    improved = True
                else:
                    val_map[i] = orig
                    enc_ids[i] = orig_e

        kmap = {all_toks[i]: val_map[i] for i in range(V)}
        top_solutions.append((cur_obj, cur_lpc, kmap))
        if cur_obj > best_global_obj:
            best_global_obj = cur_obj
            best_global_map = kmap
            best_global_lpc = cur_lpc

    top_solutions.sort(key=lambda x: -x[0])
    return best_global_obj, best_global_map, best_global_lpc, top_solutions[:5]


def eval_nospace_key(tokens, key_map, lm_ns, lex):
    pt = ''.join(key_map.get(t, '') for t in tokens)
    seq = lm_ns.encode(pt)
    if len(seq) == 0:
        return -99.0, 0.0, 0.0, 0.0, 0.0, pt, []
    lpc = float(lm_ns.score_idx(seq)) / len(seq)
    seg_words = lex.viterbi_segment(pt)
    wh, h3, c4, c5, _ = lex.evaluate_words(seg_words)
    return lpc, wh, h3, c4, c5, pt, seg_words


def z_stats(real_v, null_vals):
    mu = statistics.mean(null_vals)
    sd = statistics.pstdev(null_vals) if len(null_vals) > 1 else 0.0
    z = (real_v - mu) / sd if sd > 1e-9 else 0.0
    ge = sum(1 for v in null_vals if v >= real_v)
    p = (ge + 1) / (len(null_vals) + 1)
    return mu, sd, z, ge, p


def run_dynamic_validation(
    tokens,
    key_map,
    lm_ns,
    lex,
    n_shuf_key=200,
    n_shuf_stream=200,
    seed=1583,
    min_z_lm=5.0,
    min_z_cov4=5.0,
    max_p=0.01,
    strict_exit=True,
    label='#2077',
):
    """Dynamic PASS/FAIL validator with zero hardcoded verdict strings + negative-control check."""
    rng = random.Random(seed)
    real_lpc, real_wh, real_h3, real_c4, real_c5, pt, seg = eval_nospace_key(tokens, key_map, lm_ns, lex)
    print(f'=== DYNAMIC VALIDATION ({label}) ===')
    print(f'Real decode: len={len(pt)} chars, seg_words={len(seg)} | LM/ch={real_lpc:.4f} | '
          f'WordHit={real_wh:.3f} | Len3Hit={real_h3:.3f} | Cov4={real_c4:.3f} | Cov5={real_c5:.3f}')

    obs_toks = sorted(set(tokens))
    real_vals = [key_map.get(t, '') for t in obs_toks]

    sk_lpc, sk_wh, sk_h3, sk_c4, sk_c5 = [], [], [], [], []
    for _ in range(n_shuf_key):
        perm = list(real_vals)
        rng.shuffle(perm)
        km = dict(zip(obs_toks, perm))
        lpc, wh, h3, c4, c5, _, _ = eval_nospace_key(tokens, km, lm_ns, lex)
        sk_lpc.append(lpc); sk_wh.append(wh); sk_h3.append(h3); sk_c4.append(c4); sk_c5.append(c5)

    ss_lpc, ss_wh, ss_h3, ss_c4, ss_c5 = [], [], [], [], []
    for _ in range(n_shuf_stream):
        shuf_t = list(tokens)
        rng.shuffle(shuf_t)
        lpc, wh, h3, c4, c5, _, _ = eval_nospace_key(shuf_t, key_map, lm_ns, lex)
        ss_lpc.append(lpc); ss_wh.append(wh); ss_h3.append(h3); ss_c4.append(c4); ss_c5.append(c5)

    metrics = {}
    for name, rv, nv in [
        (f'Shuf-Key (n={n_shuf_key}) LM/ch', real_lpc, sk_lpc),
        (f'Shuf-Key (n={n_shuf_key}) WordHit', real_wh, sk_wh),
        (f'Shuf-Key (n={n_shuf_key}) Len3Hit', real_h3, sk_h3),
        (f'Shuf-Key (n={n_shuf_key}) Cov4', real_c4, sk_c4),
        (f'Shuf-Key (n={n_shuf_key}) Cov5', real_c5, sk_c5),
        (f'Shuf-Strm (n={n_shuf_stream}) LM/ch', real_lpc, ss_lpc),
        (f'Shuf-Strm (n={n_shuf_stream}) WordHit', real_wh, ss_wh),
        (f'Shuf-Strm (n={n_shuf_stream}) Len3Hit', real_h3, ss_h3),
        (f'Shuf-Strm (n={n_shuf_stream}) Cov4', real_c4, ss_c4),
        (f'Shuf-Strm (n={n_shuf_stream}) Cov5', real_c5, ss_c5),
    ]:
        mu, sd, z, ge, p = z_stats(rv, nv)
        metrics[name] = (rv, mu, sd, z, ge, p)
        print(f'  {name:28s}: real={rv:7.4f} vs null={mu:7.4f}±{sd:6.4f} | z={z:+6.2f} | >=real={ge}/{len(nv)} (p={p:.4f})')

    sk_lm_z, sk_lm_p = metrics[f'Shuf-Key (n={n_shuf_key}) LM/ch'][3], metrics[f'Shuf-Key (n={n_shuf_key}) LM/ch'][5]
    ss_lm_z, ss_lm_p = metrics[f'Shuf-Strm (n={n_shuf_stream}) LM/ch'][3], metrics[f'Shuf-Strm (n={n_shuf_stream}) LM/ch'][5]
    sk_c4_z = metrics[f'Shuf-Key (n={n_shuf_key}) Cov4'][3]
    ss_c4_z = metrics[f'Shuf-Strm (n={n_shuf_stream}) Cov4'][3]

    dummy_key = {t: 'e' for t in obs_toks}
    d_lpc, _, _, d_c4, _, _, _ = eval_nospace_key(tokens, dummy_key, lm_ns, lex)
    d_sk_z = z_stats(d_lpc, sk_lpc)[2]
    d_c4_z = z_stats(d_c4, sk_c4)[2]
    neg_failed = not (d_sk_z >= min_z_lm and d_c4_z >= min_z_cov4)
    print(f'  Negative Control (all-"e"): LM/ch={d_lpc:.4f} (z_key={d_sk_z:+.2f}), Cov4={d_c4:.3f} (z_key={d_c4_z:+.2f}) -> '
          f'{"EXPECTED_FAIL" if neg_failed else "UNEXPECTED_PASS"}')

    passed = (
        sk_lm_p <= max_p and ss_lm_p <= max_p and
        sk_lm_z >= min_z_lm and ss_lm_z >= min_z_lm and
        sk_c4_z >= min_z_cov4 and ss_c4_z >= min_z_cov4 and
        neg_failed
    )
    verdict = 'PASS' if passed else 'FAIL'
    print(f'DYNAMIC VERDICT ({label}): {verdict} '
          f'(z_lm_key={sk_lm_z:+.2f}, z_lm_strm={ss_lm_z:+.2f}, z_cov4_key={sk_c4_z:+.2f}, '
          f'p_key={sk_lm_p:.4f}, p_strm={ss_lm_p:.4f}, neg_failed={neg_failed})')
    if strict_exit and not passed:
        sys.exit(1)
    return passed, metrics
