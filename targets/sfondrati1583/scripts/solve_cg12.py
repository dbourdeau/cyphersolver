#!/usr/bin/env python3
"""Factored Cg.12 (1582) SA solver v2 on Cat. #2077 (fixes char_bonus & enforces consonant diversity)."""
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

from lm_goldenage1583 import load_spanish_lms, GoldenAge1583Lexicon, clm

TRANS = THEORIES.parent / 'transcript_2077_v2.txt'

VMARKS = ['+', '.', '@', 'e', '|']
VOWELS = ['a', 'e', 'i', 'o', 'u']
CODA_CHARS = ["'", '^', '*', ':', ',', '~', '°']
# Primary codas can never all collapse to null; keep ',', '~', '°' optionally droppable
CODA_REQUIRED = ["'", '^']

ONSETS_TOP = ['d', 's', 'r', 'n', 't', 'c', 'l', 'm', 'p', 'qu', 'b', 'g', 'u', 'f', 'y', 'h', 'z', 'ch', 'll', 'pr', 'tr', 'cr', 'gr', 'br']

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


def parse_cg12_token(tok, split_x1_x6=True, split_41=False):
    if '=' in tok:
        return ('NOM', tok, '', '')
    if re.match(r'^[A-Za-z]{2,6}[^0-9]*$', tok):
        return ('NOM', tok, '', '')

    i = len(tok)
    while i > 0 and tok[i - 1] in CODA_CHARS:
        i -= 1
    core, codas = tok[:i], tok[i:]

    if split_x1_x6 and core in ('21', '31', '61', '91', '56', '66', '96'):
        return ('SYL', core[0], '|' if core[1] == '1' else '@', codas)
    if split_41 and core == '41':
        return ('SYL', '4', '|', codas)

    if len(core) >= 2 and core[-1] in VMARKS:
        base = core[:-1]
        if base.isdigit() or base == 'D':
            return ('SYL', base, core[-1], codas)

    if core in ('f', '{', 'Δ', '7', '8', 'a', 'e', 'E', 'D', 'X', 'c'):
        return ('BARE', core, '', codas)
    if core.isdigit() and int(core) <= 35:
        return ('BARE', core, '', codas)

    return ('NOM', tok, '', '')


def solve_factored_cg12(lines, lm_sp, split_41=False, seed_caesar=False, n_restarts=24, steps=25000, seed=1583):
    parsed_lines = [[parse_cg12_token(t, split_x1_x6=True, split_41=split_41) for t in ws] for _, ws in lines]
    flat_parsed = [p for ln in parsed_lines for p in ln]

    syl_bases = sorted({p[1] for p in flat_parsed if p[0] == 'SYL'}, key=lambda x: (0, int(x)) if x.isdigit() else (1, x))
    bare_stems = sorted({p[1] for p in flat_parsed if p[0] == 'BARE'})

    uniq_tokens = []
    utok2id = {}
    stream_ids = []
    last_was_space = True
    for p in flat_parsed:
        if p[0] == 'NOM':
            if not last_was_space:
                stream_ids.append(-1)
                last_was_space = True
        else:
            if p not in utok2id:
                utok2id[p] = len(uniq_tokens)
                uniq_tokens.append(p)
            stream_ids.append(utok2id[p])
            last_was_space = False

    U = len(uniq_tokens)
    SPACE_TOK = U
    stream_arr = np.array([SPACE_TOK if x == -1 else x for x in stream_ids], dtype=np.int64)

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

    A_sz = len(lm_sp.alpha)
    space_cid = int(lm_sp.encode(' ')[0])
    c2id = {c: int(lm_sp.encode(c)[0]) for c in lm_sp.alpha if c != ' '}

    p_ref = np.full(A_sz, 1e-4, dtype=np.float64)
    for ch, pr in ES_PROBS.items():
        if ch in c2id:
            p_ref[c2id[ch]] = pr
    p_ref[space_cid] = 1e-9
    p_ref /= p_ref.sum()
    log_p_ref = np.log(p_ref)

    onset_ids = {o: [c2id[ch] for ch in o if ch in c2id] for o in ONSETS_TOP}
    vowel_ids = [c2id[v] for v in VOWELS]
    coda_pool_req = ['n', 's', 'r', 'l', 'd']
    coda_pool_opt = ['n', 's', 'r', 'l', 'd', '']
    coda_ids = {c: [c2id[ch] for ch in c] for c in coda_pool_opt}
    bare_cands_req = list('eaonrsiludtcmpqbyghfz') + ['qu']
    bare_cands_opt = bare_cands_req + ['']

    nB, nBr, nC = len(syl_bases), len(bare_stems), len(CODA_CHARS)
    base_cnt = collections.Counter(p[1] for p in flat_parsed if p[0] == 'SYL')
    bare_cnt = collections.Counter(p[1] for p in flat_parsed if p[0] == 'BARE')
    top14_b_idxs = [b2i[b] for b, _ in base_cnt.most_common(14)]
    req_bare_idxs = {br2i[b] for b in ('f', '7', '8', '{', 'Δ') if b in br2i}
    req_coda_idxs = {coda2i[c] for c in CODA_REQUIRED}

    print(f'Factored v2 (split_41={split_41}, seed_caesar={seed_caesar}): U={U}, nB={nB}, nBr={nBr}, top14={[syl_bases[i] for i in top14_b_idxs]}')

    MAX_W = 6

    def eval_factors(C_map, V_map, S_map, L_map):
        # Top 14 consonant bases must map to at least 11 distinct Spanish consonants (prevents collapsing onto r/s/n/m)
        if len({C_map[i] for i in top14_b_idxs}) < 11:
            return -1e9, 0.0
        # No single consonant may be used by >2 of the top 14 bases
        cc = collections.Counter(C_map[i] for i in top14_b_idxs)
        if cc.most_common(1)[0][1] > 2:
            return -1e9, 0.0

        lut = np.full((U + 1, MAX_W), -1, dtype=np.int64)
        lut[SPACE_TOK, 0] = space_cid
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
        if len(seq) < 50:
            return -1e9, 0.0
        non_space = seq[seq != space_cid]
        dec_chars = len(non_space)
        dec_cnt = np.bincount(non_space, minlength=A_sz).astype(np.float64)
        p_dec = dec_cnt / max(1, dec_chars)
        nz = p_dec > 0
        kl = float(np.sum(p_dec[nz] * (np.log(p_dec[nz]) - log_p_ref[nz])))

        tot_lp = float(lm_sp.score_idx(seq))
        # Use char_bonus = 2.60 so valid codas/bare vowels are never deleted to dodge LM cost
        obj = tot_lp + 2.60 * dec_chars - 1.1 * dec_chars * kl
        return obj, tot_lp / len(seq)

    rng = random.Random(seed)
    best_obj = -1e18
    best_params = None
    best_lpc = -99.0

    b_order = sorted(range(nB), key=lambda i: -base_cnt[syl_bases[i]])
    br_order = sorted(range(nBr), key=lambda i: -bare_cnt[bare_stems[i]])

    for r in range(n_restarts):
        V_map = list(range(5))
        rng.shuffle(V_map)
        c_init = list(ONSETS_TOP[:16])
        rng.shuffle(c_init)
        C_map = [''] * nB
        for rank_idx, bi in enumerate(b_order):
            C_map[bi] = c_init[rank_idx] if rank_idx < len(c_init) else rng.choice(ONSETS_TOP)
        S_map = [rng.choice(coda_pool_req if i in req_coda_idxs else coda_pool_opt) for i in range(nC)]
        L_map = [rng.choice(bare_cands_req if i in req_bare_idxs else list('eaonrsiludtcmp')) for i in range(nBr)]
        if seed_caesar:
            if 'f' in br2i:
                L_map[br2i['f']] = 'e'

        cur_obj, cur_lpc = eval_factors(C_map, V_map, S_map, L_map)
        loc_best = (cur_obj, cur_lpc, list(C_map), list(V_map), list(S_map), list(L_map))

        t0_temp, t1_temp = 14.0, 0.25
        for st in range(steps):
            frac = st / max(1, steps - 1)
            temp = t0_temp * ((t1_temp / t0_temp) ** frac)
            mv = rng.random()
            if mv < 0.14:
                i1, i2 = rng.sample(range(5), 2)
                V_map[i1], V_map[i2] = V_map[i2], V_map[i1]
                no, nl = eval_factors(C_map, V_map, S_map, L_map)
                d = no - cur_obj
                if d >= 0 or (d > -40 and rng.random() < math.exp(d / temp)):
                    cur_obj, cur_lpc = no, nl
                    if no > loc_best[0]:
                        loc_best = (no, nl, list(C_map), list(V_map), list(S_map), list(L_map))
                else:
                    V_map[i1], V_map[i2] = V_map[i2], V_map[i1]
            elif mv < 0.64:
                if rng.random() < 0.45 and nB >= 2:
                    i1, i2 = rng.sample(range(nB), 2)
                    if C_map[i1] == C_map[i2]:
                        continue
                    C_map[i1], C_map[i2] = C_map[i2], C_map[i1]
                    no, nl = eval_factors(C_map, V_map, S_map, L_map)
                    d = no - cur_obj
                    if d >= 0 or (d > -40 and rng.random() < math.exp(d / temp)):
                        cur_obj, cur_lpc = no, nl
                        if no > loc_best[0]:
                            loc_best = (no, nl, list(C_map), list(V_map), list(S_map), list(L_map))
                    else:
                        C_map[i1], C_map[i2] = C_map[i2], C_map[i1]
                else:
                    i1 = rng.choice(range(nB))
                    old = C_map[i1]
                    cand = rng.choice(ONSETS_TOP)
                    if cand == old:
                        continue
                    C_map[i1] = cand
                    no, nl = eval_factors(C_map, V_map, S_map, L_map)
                    d = no - cur_obj
                    if d >= 0 or (d > -40 and rng.random() < math.exp(d / temp)):
                        cur_obj, cur_lpc = no, nl
                        if no > loc_best[0]:
                            loc_best = (no, nl, list(C_map), list(V_map), list(S_map), list(L_map))
                    else:
                        C_map[i1] = old
            elif mv < 0.84:
                i1 = rng.choice(range(nBr))
                if seed_caesar and bare_stems[i1] == 'f':
                    continue
                old = L_map[i1]
                cand = rng.choice(bare_cands_req if i1 in req_bare_idxs else bare_cands_opt)
                if cand == old:
                    continue
                L_map[i1] = cand
                no, nl = eval_factors(C_map, V_map, S_map, L_map)
                d = no - cur_obj
                if d >= 0 or (d > -40 and rng.random() < math.exp(d / temp)):
                    cur_obj, cur_lpc = no, nl
                    if no > loc_best[0]:
                        loc_best = (no, nl, list(C_map), list(V_map), list(S_map), list(L_map))
                else:
                    L_map[i1] = old
            else:
                i1 = rng.choice(range(nC))
                old = S_map[i1]
                cand = rng.choice(coda_pool_req if i1 in req_coda_idxs else coda_pool_opt)
                if cand == old:
                    continue
                S_map[i1] = cand
                no, nl = eval_factors(C_map, V_map, S_map, L_map)
                d = no - cur_obj
                if d >= 0 or (d > -40 and rng.random() < math.exp(d / temp)):
                    cur_obj, cur_lpc = no, nl
                    if no > loc_best[0]:
                        loc_best = (no, nl, list(C_map), list(V_map), list(S_map), list(L_map))
                else:
                    S_map[i1] = old

        # Greedy coordinate polish
        cur_obj, cur_lpc, C_map, V_map, S_map, L_map = loc_best
        improved = True
        while improved:
            improved = False
            for i1 in range(5):
                for i2 in range(i1 + 1, 5):
                    V_map[i1], V_map[i2] = V_map[i2], V_map[i1]
                    no, nl = eval_factors(C_map, V_map, S_map, L_map)
                    if no > cur_obj + 1e-6:
                        cur_obj, cur_lpc = no, nl
                        improved = True
                    else:
                        V_map[i1], V_map[i2] = V_map[i2], V_map[i1]
            for i1 in b_order:
                orig = C_map[i1]
                best_c, best_o, best_l = orig, cur_obj, cur_lpc
                for cand in ONSETS_TOP:
                    if cand == orig:
                        continue
                    C_map[i1] = cand
                    no, nl = eval_factors(C_map, V_map, S_map, L_map)
                    if no > best_o + 1e-6:
                        best_c, best_o, best_l = cand, no, nl
                C_map[i1] = best_c
                if best_c != orig:
                    cur_obj, cur_lpc = best_o, best_l
                    improved = True
            for i1 in br_order:
                if seed_caesar and bare_stems[i1] == 'f':
                    continue
                orig = L_map[i1]
                best_v, best_o, best_l = orig, cur_obj, cur_lpc
                pool = bare_cands_req if i1 in req_bare_idxs else bare_cands_opt
                for cand in pool:
                    if cand == orig:
                        continue
                    L_map[i1] = cand
                    no, nl = eval_factors(C_map, V_map, S_map, L_map)
                    if no > best_o + 1e-6:
                        best_v, best_o, best_l = cand, no, nl
                L_map[i1] = best_v
                if best_v != orig:
                    cur_obj, cur_lpc = best_o, best_l
                    improved = True
            for i1 in range(nC):
                orig = S_map[i1]
                best_s, best_o, best_l = orig, cur_obj, cur_lpc
                pool = coda_pool_req if i1 in req_coda_idxs else coda_pool_opt
                for cand in pool:
                    if cand == orig:
                        continue
                    S_map[i1] = cand
                    no, nl = eval_factors(C_map, V_map, S_map, L_map)
                    if no > best_o + 1e-6:
                        best_s, best_o, best_l = cand, no, nl
                S_map[i1] = best_s
                if best_s != orig:
                    cur_obj, cur_lpc = best_o, best_l
                    improved = True

        params = {
            'V': {VMARKS[i]: VOWELS[V_map[i]] for i in range(5)},
            'C': {syl_bases[i]: C_map[i] for i in range(nB)},
            'S': {CODA_CHARS[i]: S_map[i] for i in range(nC)},
            'L': {bare_stems[i]: L_map[i] for i in range(nBr)},
        }
        if cur_obj > best_obj:
            best_obj, best_lpc, best_params = cur_obj, cur_lpc, params

    return best_obj, best_lpc, best_params, parsed_lines


def render_lines(parsed_lines, params):
    out_lines = []
    V, C, S, L = params['V'], params['C'], params['S'], params['L']
    for lid, pln in parsed_lines:
        parts = []
        for kind, stem, vm, codas in pln:
            if kind == 'NOM':
                parts.append(f' [{stem}] ')
            elif kind == 'SYL':
                c_str = ''.join(S.get(c, '') for c in codas)
                parts.append(C[stem] + V[vm] + c_str)
            else:
                c_str = ''.join(S.get(c, '') for c in codas)
                parts.append(L[stem] + c_str)
        out_lines.append((lid, ''.join(parts).strip()))
    return out_lines


def main():
    t0 = time.time()
    _, lm_sp = load_spanish_lms()
    lines = load_core_lines()

    for label, split_41, seed_caesar in [
        ('Mode B_v2: soft f=e (split_41=False)', False, True),
        ('Mode C_v2: soft f=e (split_41=True)', True, True),
    ]:
        print('=' * 76)
        print(label)
        print('=' * 76)
        obj, lpc, params, parsed = solve_factored_cg12(
            lines, lm_sp, split_41=split_41, seed_caesar=seed_caesar,
            n_restarts=16, steps=25000, seed=1585 if not split_41 else 1586,
        )
        tagged = [(lines[i][0], parsed[i]) for i in range(len(lines))]
        rendered = render_lines(tagged, params)
        print(f'obj={obj:.2f} | LM/ch={lpc:.4f}')
        print('Vowel marks:', params['V'])
        print('Coda marks :', params['S'])
        print('Consonants :', params['C'])
        print('Bare tokens:', params['L'])
        print('\n--- Sample Decoded Lines (Item 6 L01-L15 & Item 19/26 Inline Cribs) ---')
        for lid, txt in rendered[:15] + rendered[-10:]:
            print(f'  {lid}: {txt}')
    print(f'\nTotal elapsed: {time.time()-t0:.1f}s')


if __name__ == '__main__':
    main()
