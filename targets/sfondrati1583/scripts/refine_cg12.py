#!/usr/bin/env python3
"""Refined Factored Cg.12 (1582) SA solver on Cat. #2077 using es-golden-age-nospace (lm_ns)."""
import collections
import math
import pathlib
import random
import re
import sys
import time
import numpy as np

THEORIES = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(THEORIES))

from lm_goldenage1583 import load_spanish_lms, GoldenAge1583Lexicon

TRANS = THEORIES.parent / 'transcript_2077_v2.txt'

VMARKS = ['+', '.', '@', 'e', '|']
VOWELS = ['a', 'e', 'i', 'o', 'u']
CODA_CHARS = ["'", '^', ',', '*', ':', '~', '°']
CODA_REQ = {"'", '^', ','}

ONSETS_TOP = [
    'd', 's', 'r', 'n', 't', 'c', 'l', 'm', 'p', 'qu', 'b', 'g',
    'u', 'f', 'y', 'h', 'z', 'ch', 'll', 'pr', 'tr', 'cr', 'gr', 'br', 'j', 'x', ''
]

ES_PROBS = {
    'e': 0.138, 'a': 0.124, 'o': 0.089, 's': 0.079, 'n': 0.068,
    'r': 0.067, 'i': 0.063, 'l': 0.052, 'd': 0.050, 't': 0.045,
    'u': 0.044, 'c': 0.043, 'm': 0.032, 'p': 0.026, 'q': 0.019,
    'b': 0.016, 'y': 0.012, 'g': 0.011, 'f': 0.008, 'h': 0.009,
    'z': 0.005, 'x': 0.003,
}


def load_core_lines():
    lines = []
    for raw in TRANS.read_text(encoding='utf-8').splitlines():
        s = raw.strip()
        if not s or s.startswith('#'):
            continue
        lid, toks = s.split(':', 1)
        lines.append((lid.strip(), toks.strip().split()))
    return lines


def parse_cg12_token(tok, split_x1_x6=True, split_56=False, split_41=False):
    if '=' in tok:
        return ('NOM', tok, '', '')
    if re.match(r'^[A-Za-z]{2,6}[^0-9]*$', tok):
        return ('NOM', tok, '', '')

    i = len(tok)
    while i > 0 and tok[i - 1] in CODA_CHARS:
        i -= 1
    core, codas = tok[:i], tok[i:]

    if split_x1_x6 and core in ('91', '96', '61', '66', '46'):
        return ('SYL', core[0], '|' if core[1] == '1' else '@', codas)
    if split_56 and core == '56':
        return ('SYL', '5', '@', codas)
    if split_41 and core == '41':
        return ('SYL', '4', '|', codas)

    if len(core) >= 2 and core[-1] in VMARKS:
        base = core[:-1]
        if base.isdigit() or base == 'D':
            return ('SYL', base, core[-1], codas)

    if core in ('f', '{', 'Δ', '7', '8', '21', 'a', 'e', 'E', 'D', 'X', 'c'):
        return ('BARE', core, '', codas)
    if core.isdigit() and int(core) <= 35:
        return ('BARE', core, '', codas)

    return ('NOM', tok, '', '')


def solve_ns(lines, lm_ns, lex, split_56=False, split_41=False, n_restarts=14, steps=12000, seed=1583):
    parsed_lines = [[parse_cg12_token(t, split_x1_x6=True, split_56=split_56, split_41=split_41) for t in ws] for _, ws in lines]
    flat_parsed = [p for ln in parsed_lines for p in ln]

    syl_bases = sorted({p[1] for p in flat_parsed if p[0] == 'SYL'}, key=lambda x: (0, int(x)) if x.isdigit() else (1, x))
    bare_stems = sorted({p[1] for p in flat_parsed if p[0] == 'BARE'})

    uniq_tokens = []
    utok2id = {}
    # Store contiguous non-NOM segments as separate spans so [NOM] doesn't inject false bigrams,
    # OR score concatenated stream — we test concatenated stream AND compute exact span scores at end.
    stream_ids = []
    for p in flat_parsed:
        if p[0] != 'NOM':
            if p not in utok2id:
                utok2id[p] = len(uniq_tokens)
                uniq_tokens.append(p)
            stream_ids.append(utok2id[p])

    U = len(uniq_tokens)
    stream_arr = np.array(stream_ids, dtype=np.int64)

    b2i = {b: i for i, b in enumerate(syl_bases)}
    br2i = {b: i for i, b in enumerate(bare_stems)}
    v2i = {v: i for i, v in enumerate(VMARKS)}
    coda2i = {c: i for i, c in enumerate(CODA_CHARS)}

    u_meta = []
    for kind, stem, vm, codas in uniq_tokens:
        ctup = tuple(coda2i[c] for c in codas if c in coda2i)
        if kind == 'SYL':
            u_meta.append((0, b2i[stem], v2i[vm], ctup))
        else:
            u_meta.append((1, br2i[stem], -1, ctup))

    A_sz = len(lm_ns.alpha)
    c2id = {c: int(lm_ns.encode(c)[0]) for c in lm_ns.alpha}

    p_ref = np.full(A_sz, 1e-4, dtype=np.float64)
    for ch, pr in ES_PROBS.items():
        if ch in c2id:
            p_ref[c2id[ch]] = pr
    p_ref /= p_ref.sum()
    log_p_ref = np.log(p_ref)

    onset_ids = {o: [c2id[ch] for ch in o if ch in c2id] for o in ONSETS_TOP}
    vowel_ids = [c2id[v] for v in VOWELS]
    coda_pool_req = ['n', 's', 'r', 'l', 'd']
    coda_pool_opt = ['n', 's', 'r', 'l', 'd', '']
    coda_ids = {c: [c2id[ch] for ch in c] for c in coda_pool_opt}

    bare_cands_req = list('eaonrsiludtcmpqbyghfz') + ['qu', 'de', 'la', 'el', 'en', 'se', 'lo', 'su', 'es', 'no', 'si', 'ha']
    bare_cands_opt = bare_cands_req + ['']

    nB, nBr, nC = len(syl_bases), len(bare_stems), len(CODA_CHARS)
    base_cnt = collections.Counter(p[1] for p in flat_parsed if p[0] == 'SYL')
    bare_cnt = collections.Counter(p[1] for p in flat_parsed if p[0] == 'BARE')
    top14_b_idxs = [b2i[b] for b, _ in base_cnt.most_common(14)]
    req_bare_idxs = {br2i[b] for b in ('f', '7', '8', '{', 'Δ', '21', '19', '24') if b in br2i}
    req_coda_idxs = {coda2i[c] for c in CODA_REQ}

    MAX_W = 6

    def eval_factors(C_map, V_map, S_map, L_map):
        if len({C_map[i] for i in top14_b_idxs}) < 11:
            return -1e9, -99.0
        cc = collections.Counter(C_map[i] for i in top14_b_idxs)
        if cc.most_common(1)[0][1] > 2:
            return -1e9, -99.0

        lut = np.full((U, MAX_W), -1, dtype=np.int64)
        for u, (is_bare, sidx, vidx, ctup) in enumerate(u_meta):
            if is_bare == 0:
                ids = list(onset_ids[C_map[sidx]])
                ids.append(vowel_ids[V_map[vidx]])
            else:
                bval = L_map[sidx]
                ids = [c2id[ch] for ch in bval if ch in c2id]
            for ci in ctup:
                ids.extend(coda_ids[S_map[ci]])
            for k, cid in enumerate(ids[:MAX_W]):
                lut[u, k] = cid

        flat = lut[stream_arr].ravel()
        seq = flat[flat >= 0]
        dec_chars = len(seq)
        if dec_chars < 200:
            return -1e9, -99.0
        dec_cnt = np.bincount(seq, minlength=A_sz).astype(np.float64)
        p_dec = dec_cnt / dec_chars
        nz = p_dec > 0
        kl = float(np.sum(p_dec[nz] * (np.log(p_dec[nz]) - log_p_ref[nz])))

        tot_lp = float(lm_ns.score_idx(seq))
        # es-golden-age-nospace avg is ~ -1.8 to -2.1/ch; char_bonus=2.30 encourages keeping real letters/codas without inflating
        obj = tot_lp + 2.30 * dec_chars - 1.2 * dec_chars * kl
        return obj, tot_lp / dec_chars

    # Seed hint from Mode B_v2 discovery (half seeded, half cold blind random)
    seed_C = {'2': 'd', '4': 'b', '6': 'g', '9': 'c', '10': 'l', '11': 'm', '12': 'p', '13': 'r',
              '14': 't', '16': 'y', '17': 'l', '18': 'u', '19': 's', '20': 'qu', '22': 'm',
              '24': 'r', '26': 'ch', '27': 'd', '33': 'pr', '34': 'tr', '36': 'tr'}
    seed_V = {'+': 2, '.': 3, '@': 4, 'e': 1, '|': 0}  # i, o, u, e, a
    seed_S = {"'": 'n', '^': 'n', ',': 'r', '*': 's', ':': 's', '~': '', '°': ''}
    seed_L = {'f': 'e', '8': 'a', '7': 'e', '{': 's', 'Δ': 'a', '21': 'o', '5': 'i', '19': 's'}

    rng = random.Random(seed)
    best_obj = -1e18
    best_lpc = -99.0
    best_params = None

    b_order = sorted(range(nB), key=lambda i: -base_cnt[syl_bases[i]])
    br_order = sorted(range(nBr), key=lambda i: -bare_cnt[bare_stems[i]])

    t0 = time.time()
    for r in range(n_restarts):
        if r < 2:
            # Hot blind random initialization
            V_map = list(range(5))
            rng.shuffle(V_map)
            c_init = list(ONSETS_TOP[:16])
            rng.shuffle(c_init)
            C_map = [''] * nB
            for rank_idx, bi in enumerate(b_order):
                C_map[bi] = c_init[rank_idx] if rank_idx < len(c_init) else rng.choice(ONSETS_TOP[:20])
            S_map = [rng.choice(coda_pool_req) if i in req_coda_idxs else rng.choice(coda_pool_opt) for i in range(nC)]
            L_map = [rng.choice(bare_cands_req[:10]) if i in req_bare_idxs else rng.choice(bare_cands_opt[:12]) for i in range(nBr)]
        else:
            # Mode-B_v2 guided initialization with random perturbations
            V_map = [seed_V[v] for v in VMARKS]
            C_map = [seed_C.get(syl_bases[i], rng.choice(ONSETS_TOP[:16])) for i in range(nB)]
            if r > 2:
                for _ in range(4):
                    bi = rng.choice(b_order[:20])
                    C_map[bi] = rng.choice(ONSETS_TOP[:18])
            # Fix any top14 conflict
            used = collections.Counter()
            for bi in top14_b_idxs:
                while used[C_map[bi]] >= 2 or len({C_map[x] for x in top14_b_idxs}) < 11:
                    C_map[bi] = rng.choice(ONSETS_TOP[:18])
                    if len({C_map[x] for x in top14_b_idxs}) >= 11 and used[C_map[bi]] < 2:
                        break
                used[C_map[bi]] += 1
            S_map = [seed_S.get(CODA_CHARS[i], '') for i in range(nC)]
            L_map = [seed_L.get(bare_stems[i], rng.choice(bare_cands_req[:10])) for i in range(nBr)]

        cur_obj, cur_lpc = eval_factors(C_map, V_map, S_map, L_map)
        loc_best = (cur_obj, cur_lpc, (list(C_map), list(V_map), list(S_map), list(L_map)))
        T0 = 18.0 if r < 2 else 6.0

        for step in range(steps):
            T = T0 * ((0.12 / T0) ** (step / steps))
            mv = rng.random()
            if mv < 0.36:
                bi = rng.choice(b_order[:22]) if rng.random() < 0.78 else rng.randrange(nB)
                old = C_map[bi]
                C_map[bi] = rng.choice(ONSETS_TOP[:20] if base_cnt[syl_bases[bi]] >= 10 else ONSETS_TOP)
                if C_map[bi] == old:
                    continue
                new_obj, new_lpc = eval_factors(C_map, V_map, S_map, L_map)
                if new_obj >= cur_obj or rng.random() < math.exp((new_obj - cur_obj) / T):
                    cur_obj, cur_lpc = new_obj, new_lpc
                else:
                    C_map[bi] = old
            elif mv < 0.48:
                i, j = rng.sample(range(nB), 2)
                if C_map[i] == C_map[j]:
                    continue
                C_map[i], C_map[j] = C_map[j], C_map[i]
                new_obj, new_lpc = eval_factors(C_map, V_map, S_map, L_map)
                if new_obj >= cur_obj or rng.random() < math.exp((new_obj - cur_obj) / T):
                    cur_obj, cur_lpc = new_obj, new_lpc
                else:
                    C_map[i], C_map[j] = C_map[j], C_map[i]
            elif mv < 0.58:
                i, j = rng.sample(range(5), 2)
                V_map[i], V_map[j] = V_map[j], V_map[i]
                new_obj, new_lpc = eval_factors(C_map, V_map, S_map, L_map)
                if new_obj >= cur_obj or rng.random() < math.exp((new_obj - cur_obj) / T):
                    cur_obj, cur_lpc = new_obj, new_lpc
                else:
                    V_map[i], V_map[j] = V_map[j], V_map[i]
            elif mv < 0.80:
                ci = rng.randrange(nC)
                old = S_map[ci]
                pool = coda_pool_req if ci in req_coda_idxs else coda_pool_opt
                S_map[ci] = rng.choice(pool)
                if S_map[ci] == old:
                    continue
                new_obj, new_lpc = eval_factors(C_map, V_map, S_map, L_map)
                if new_obj >= cur_obj or rng.random() < math.exp((new_obj - cur_obj) / T):
                    cur_obj, cur_lpc = new_obj, new_lpc
                else:
                    S_map[ci] = old
            else:
                bi = rng.choice(br_order[:14]) if rng.random() < 0.80 else rng.randrange(nBr)
                old = L_map[bi]
                pool = bare_cands_req if bi in req_bare_idxs else bare_cands_opt
                L_map[bi] = rng.choice(pool)
                if L_map[bi] == old:
                    continue
                new_obj, new_lpc = eval_factors(C_map, V_map, S_map, L_map)
                if new_obj >= cur_obj or rng.random() < math.exp((new_obj - cur_obj) / T):
                    cur_obj, cur_lpc = new_obj, new_lpc
                else:
                    L_map[bi] = old

            if cur_obj > loc_best[0]:
                loc_best = (cur_obj, cur_lpc, (list(C_map), list(V_map), list(S_map), list(L_map)))

        if loc_best[0] > best_obj:
            best_obj = loc_best[0]
            best_lpc = loc_best[1]
            best_params = loc_best[2]
        print(f'  restart {r+1:2d}/{n_restarts}: loc_lpc={loc_best[1]:.4f}, best_lpc={best_lpc:.4f} ({time.time()-t0:.1f}s)')

    C_map, V_map, S_map, L_map = best_params
    res_V = {VMARKS[i]: VOWELS[V_map[i]] for i in range(5)}
    res_C = {syl_bases[i]: C_map[i] for i in range(nB)}
    res_S = {CODA_CHARS[i]: S_map[i] for i in range(nC)}
    res_L = {bare_stems[i]: L_map[i] for i in range(nBr)}

    # Decode & measure word-level lexicon quality
    rendered = []
    all_letters = []
    for (lid, _), pline in zip(lines, parsed_lines):
        out = []
        for kind, stem, vm, codas in pline:
            if kind == 'NOM':
                out.append(f' [{stem}] ')
            elif kind == 'SYL':
                cstr = ''.join(res_S.get(c, '') for c in codas)
                s = res_C[stem] + res_V[vm] + cstr
                out.append(s)
                all_letters.append(s)
            else:
                cstr = ''.join(res_S.get(c, '') for c in codas)
                s = res_L[stem] + cstr
                out.append(s)
                all_letters.append(s)
        rendered.append((lid, ''.join(out)))

    joined = ''.join(all_letters)
    norm = ''.join(ch for ch in joined.lower() if ch in lm_ns.alpha)
    words = lex.viterbi_segment(norm)
    wh, h3, c4, c5, _ = lex.evaluate_words(words)
    norm_ids = lm_ns.encode(norm)
    exact_lpc = float(lm_ns.score_idx(norm_ids)) / max(1, len(norm_ids))
    print(f'\nFINAL: exact_LM/ch={exact_lpc:.4f} | WordHit={wh:.3f} | Len3Hit={h3:.3f} | Cov4={c4:.3f} | Cov5={c5:.3f}')
    print('Vowel marks:', res_V)
    print('Coda marks :', res_S)
    print('Consonants :', res_C)
    print('Bare tokens:', res_L)
    print('\n--- Sample Decoded Lines ---')
    show_ids = [f'L{i:02d}' for i in range(1, 16)] + ['PS07', 'PS08', 'I19_P1_L01', 'I19_P1_L02', 'I19_P1_L03', 'I19_P1_L04', 'I19_P1_L05', 'I19_P2_SLOT', 'I26_P1_L01', 'I26_P1_L02']
    rmap = dict(rendered)
    for sid in show_ids:
        if sid in rmap:
            print(f'  {sid}: {rmap[sid]}')

    # Also save full decoded lines
    out_full = THEORIES / f'decoded_ns_56_{split_56}_41_{split_41}.txt'
    out_full.write_text('\n'.join(f'{lid}: {txt}' for lid, txt in rendered) + '\n', encoding='utf-8')
    return exact_lpc, res_C, res_V, res_S, res_L, rendered


if __name__ == '__main__':
    lm_ns, _ = load_spanish_lms()
    lex = GoldenAge1583Lexicon()
    lines = load_core_lines()
    print('=== RUN 1: split_56=False, split_41=False ===')
    solve_ns(lines, lm_ns, lex, split_56=False, split_41=False, n_restarts=8, steps=16000, seed=1583)
