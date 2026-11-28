#!/usr/bin/env python3
"""Strictly zero-retuning out-of-sample test of frozen #2077 Cg.12 key on Cat. #2518 & transcript_2077_v2.txt."""
import argparse
import collections
import math
import pathlib
import random
import re
import sys

SCRIPTS_DIR = pathlib.Path(__file__).resolve().parent
TARGET_DIR = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from lm_goldenage1583 import load_spanish_lms, GoldenAge1583Lexicon
from refine_cg12 import CODA_CHARS, VMARKS

V2_PATH = TARGET_DIR / 'transcript_2077_v2.txt'
OOS_PATH = TARGET_DIR / 'transcript_2518.txt'

# Frozen #2077 Cg.12 (1582) Syllabary Key (incorporating v2 / #124 structural rules; ZERO tuning on #2518)
V_MAP = {'+': 'i', '.': 'o', '@': 'u', 'e': 'e', '|': 'a'}
S_MAP = {"'": 'n', '^': 's', ',': 'r', ':': 'l', '*': '*', '~': '', '°': ''}

C_MAP = {
    '1': 'b', '2': 'd', '3': 'f', '4': 'b', '5': 'p', '6': 'g', '9': 'c',
    '10': 'l', '11': 'n', '12': 'p', '13': 'r', '14': 't', '15': 'x', '16': 'c',
    '17': 'y', '18': 'u', '19': 's', '20': 'qu', '22': 'm', '23': 'bl', '24': 'br',
    '26': 'cr', '27': 'dr', '28': 'tu', '29': 'fr', '30': 'c', '31': 'gr',
    '32': 'pl', '33': 'pr', '34': 'tr', '35': 'y', '36': 'tr', '42': 'd',
    '60': 'auis', 'D': 'ch',
}

# Frozen EXACT_CORE (note 60=auis->60|=auisa/60|,=auisar/60e=auise; Di=cha; 5_m=im; 5.=jo; 7.=em; 8.=am)
EXACT_CORE = {
    '4e': 'he', '4.': 'ho', '41': 'ha', '46': 'hu',
    '56': 'ju', '61': 'ga', '66': 'gu', '91': 'ca', '96': 'cu',
    '5_m': 'im', '5.': 'jo', '7.': 'em', '8.': 'am',
    '24': 'di', '17': 'de', '17,': 'yr', '36': 'fu',
    'f': 'e', 'f.': 'e', '7': 'e', '8': 'a', '21': 'o', '21e': 'oe',
    '5': 'i', '6': 'en', '{': 'y', '{.': 'yo', '{e': 'ye', 'Δ': 'a',
    '19': 's', '14': 't', '15': 'x', '16': 'z', '18': 'u', '2': 'd',
    '4': 'v', '9': 'p', '26': 'a', 'E': 'no', 'X': 'la', 'a': 'a',
    'c': 's', 'e': 'd', 'Di': 'cha', '31': 'fa', '31:': 'fal',
    '60|': 'auisa', '60e': 'auise',
}

PROVED_SHORT_NOMS = {
    '56': 'ju', "56'": 'jun', '56^': 'jus',
    '23=': 'cosa', '23=^': 'cosas',
    'xe': 'manera',
    'quol': 'qual',
    '79': 'carta', '79^': 'cartas',
    '224': 'mi', '224^': 'mis',
    '12°': '',
}


def load_lines(path):
    lines = []
    for raw in path.read_text(encoding='utf-8').splitlines():
        s = raw.strip()
        if not s or s.startswith('#'):
            continue
        lid, rest = s.split(':', 1)
        ws = rest.strip().split()
        if ws:
            lines.append((lid.strip(), ws))
    return lines


def apply_gemination(syl, has_star):
    """Apply Carbon's * gemination (ll/rr/ss/ff/nn) on consonant onset of decoded syllable."""
    if not has_star or not syl:
        return syl
    if syl[0] in ('l', 'r', 's', 'f', 'n'):
        return syl[0] + syl
    return syl


def extract_parsed(lines):
    parsed = []
    for _, ws in lines:
        for tok in ws:
            # Keep literal numeral overbar tokens (~) as NOM/LITERAL unless syllabic base
            if '~' in tok:
                parsed.append(('NOM', tok, '', ''))
                continue
            if '=' in tok or (re.match(r'^[A-Za-z]{2,6}[^0-9]*$', tok) and tok != 'Di' and not tok.startswith('Di,')):
                if not (tok.startswith('D') and (tok == 'D' or (len(tok) >= 2 and tok[1] in VMARKS))):
                    parsed.append(('NOM', tok, '', ''))
                    continue
            # Check exact full-token overrides like 17, or 31: or Di, before splitting codas
            if tok in EXACT_CORE:
                parsed.append(('EXACT', tok, tok, ''))
                continue
            i = len(tok)
            while i > 0 and tok[i - 1] in CODA_CHARS:
                i -= 1
            core, codas = tok[:i], tok[i:]
            if core in EXACT_CORE:
                parsed.append(('EXACT', tok, core, codas))
            elif len(core) >= 2 and core[-1] in VMARKS and core[:-1] in C_MAP:
                parsed.append(('SYL', tok, core[:-1], (core[-1], codas)))
            else:
                parsed.append(('NOM', tok, '', ''))
    return parsed


def eval_text(text_raw, lm_ns, lex):
    norm = ''.join(ch for ch in text_raw.lower() if ch in lm_ns.alpha)
    if len(norm) < 20:
        return -10.0, 0.0, 0.0, 0.0, 0.0, 0
    ids = lm_ns.encode(norm)
    lpc = float(lm_ns.score_idx(ids)) / len(ids)
    words = lex.viterbi_segment(norm)
    wh, h3, c4, c5, _ = lex.evaluate_words(words)
    return lpc, wh, h3, c4, c5, len(norm)


def z_and_p(real_val, null_vals):
    n = len(null_vals)
    mu = sum(null_vals) / n
    var = sum((x - mu) ** 2 for x in null_vals) / max(1, n - 1)
    sd = math.sqrt(var) if var > 1e-12 else 0.0
    z = (real_val - mu) / sd if sd > 0.0 else 0.0
    ge = sum(1 for x in null_vals if x >= real_val)
    p = (ge + 1.0) / (n + 1.0)
    return mu, sd, z, p


def run_validation(label, parsed, lm_ns, lex, c_map, v_map, s_map, e_map, include_short_noms=True, n_null=200, seed=2518):
    rng = random.Random(seed)
    all_e = dict(e_map)

    def render(cm, vm, sm, em, shuffle_order=False):
        chunks = []
        for kind, raw, stem, extra in parsed:
            if kind == 'NOM':
                if include_short_noms and raw in PROVED_SHORT_NOMS:
                    chunks.append(PROVED_SHORT_NOMS[raw])
            elif kind == 'EXACT':
                has_star = '*' in extra
                cstr = ''.join(sm.get(c, '') for c in extra if c != '*')
                chunks.append(apply_gemination(em[stem], has_star) + cstr)
            elif kind == 'SYL':
                vmark, codas = extra
                has_star = '*' in codas
                cstr = ''.join(sm.get(c, '') for c in codas if c != '*')
                if stem == '60':
                    syl = cm[stem] + vm[vmark]
                else:
                    syl = cm[stem] + vm[vmark]
                chunks.append(apply_gemination(syl, has_star) + cstr)
        if shuffle_order:
            rng.shuffle(chunks)
        return ''.join(chunks)

    real_txt = render(c_map, v_map, s_map, all_e, shuffle_order=False)
    lpc, wh, h3, c4, c5, n_ch = eval_text(real_txt, lm_ns, lex)

    c_keys, c_vals = list(c_map.keys()), list(c_map.values())
    v_keys, v_vals = list(v_map.keys()), list(v_map.values())
    # Exclude '*' sentinel when shuffling coda letters, permute real coda consonants
    s_keys = [k for k in s_map.keys()]
    s_vals = [s_map[k] for k in s_keys]
    e_keys, e_vals = list(all_e.keys()), list(all_e.values())

    sk_lm, sk_c4, sk_c5 = [], [], []
    for _ in range(n_null):
        cv = list(c_vals); rng.shuffle(cv)
        vv = list(v_vals); rng.shuffle(vv)
        sv = list(s_vals); rng.shuffle(sv)
        ev = list(e_vals); rng.shuffle(ev)
        txt = render(dict(zip(c_keys, cv)), dict(zip(v_keys, vv)), dict(zip(s_keys, sv)), dict(zip(e_keys, ev)))
        nl, _, _, nc4, nc5, _ = eval_text(txt, lm_ns, lex)
        sk_lm.append(nl); sk_c4.append(nc4); sk_c5.append(nc5)

    ss_lm, ss_c4, ss_c5 = [], [], []
    for _ in range(n_null):
        txt = render(c_map, v_map, s_map, all_e, shuffle_order=True)
        nl, _, _, nc4, nc5, _ = eval_text(txt, lm_ns, lex)
        ss_lm.append(nl); ss_c4.append(nc4); ss_c5.append(nc5)

    mu_kl, sd_kl, z_kl, p_kl = z_and_p(lpc, sk_lm)
    mu_kc4, sd_kc4, z_kc4, p_kc4 = z_and_p(c4, sk_c4)
    mu_kc5, sd_kc5, z_kc5, p_kc5 = z_and_p(c5, sk_c5)
    mu_sl, sd_sl, z_sl, p_sl = z_and_p(lpc, ss_lm)
    mu_sc4, sd_sc4, z_sc4, p_sc4 = z_and_p(c4, ss_c4)
    mu_sc5, sd_sc5, z_sc5, p_sc5 = z_and_p(c5, ss_c5)

    # Pure dynamic verdict (zero dummy shortcuts!)
    passed = (
        z_kl >= 5.0 and z_sl >= 5.0
        and z_kc4 >= 5.0 and z_sc4 >= 5.0
        and p_kl <= 0.01 and p_sl <= 0.01
        and wh >= 0.85
    )
    verdict = 'PASS' if passed else 'FAIL'
    print(f'=== {label} ===')
    print(f'  Decoded chars={n_ch} | LM/ch={lpc:.4f} | WordHit={wh:.3f} | Len3Hit={h3:.3f} | Cov4={c4:.3f} | Cov5={c5:.3f}')
    print(f'  Shuf-Key (n={n_null}): LM={mu_kl:.4f}+/-{sd_kl:.4f} z={z_kl:+.2f} p={p_kl:.4f} | Cov4={mu_kc4:.3f}+/-{sd_kc4:.3f} z={z_kc4:+.2f} p={p_kc4:.4f} | Cov5={mu_kc5:.3f} z={z_kc5:+.2f}')
    print(f'  Shuf-Strm(n={n_null}): LM={mu_sl:.4f}+/-{sd_sl:.4f} z={z_sl:+.2f} p={p_sl:.4f} | Cov4={mu_sc4:.3f}+/-{sd_sc4:.3f} z={z_sc4:+.2f} p={p_sc4:.4f} | Cov5={mu_sc5:.3f} z={z_sc5:+.2f}')
    print(f'  VERDICT: {verdict}')
    return passed, real_txt


def decode_pretty(lines, bare17='de'):
    all_e = dict(EXACT_CORE)
    all_e['17'] = bare17
    out_lines = []
    nom_ctx = collections.defaultdict(list)
    n_tot = 0
    n_map = 0
    for lid, ws in lines:
        parts = []
        decs = []
        for tok in ws:
            n_tot += 1
            if '~' in tok:
                decs.append(('NOM', f'[{tok}]'))
                continue
            if tok in PROVED_SHORT_NOMS:
                n_map += 1
                decs.append(('SYL', PROVED_SHORT_NOMS[tok]))
                continue
            if '=' in tok or (re.match(r'^[A-Za-z]{2,6}[^0-9]*$', tok) and tok != 'Di' and not tok.startswith('Di,')):
                if not (tok.startswith('D') and (tok == 'D' or (len(tok) >= 2 and tok[1] in VMARKS))):
                    decs.append(('NOM', f'[{tok}]'))
                    continue
            if tok in all_e:
                n_map += 1
                decs.append(('SYL', all_e[tok]))
                continue
            i = len(tok)
            while i > 0 and tok[i - 1] in CODA_CHARS:
                i -= 1
            core, codas = tok[:i], tok[i:]
            has_star = '*' in codas
            cstr = ''.join(S_MAP.get(c, '') for c in codas if c != '*')
            if core in all_e:
                n_map += 1
                decs.append(('SYL', apply_gemination(all_e[core], has_star) + cstr))
            elif len(core) >= 2 and core[-1] in VMARKS and core[:-1] in C_MAP:
                n_map += 1
                syl = C_MAP[core[:-1]] + V_MAP[core[-1]]
                decs.append(('SYL', apply_gemination(syl, has_star) + cstr))
            else:
                decs.append(('NOM', f'[{tok}]'))
        for j, (k, d) in enumerate(decs):
            parts.append(f' {d} ' if k == 'NOM' else d)
            if k == 'NOM':
                l = ''.join(decs[m][1] for m in range(max(0, j - 5), j))
                r = ''.join(decs[m][1] for m in range(j + 1, min(len(decs), j + 6)))
                nom_ctx[ws[j]].append((lid, l, r))
        txt = re.sub(r' +', ' ', ''.join(parts)).strip()
        out_lines.append((lid, txt))
    return n_map, n_tot, out_lines, nom_ctx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dummy-all-e', action='store_true')
    ap.add_argument('--dummy-all-a', action='store_true')
    ap.add_argument('--target', choices=['2518', '2077_v2', 'both'], default='both')
    ap.add_argument('--n-null', type=int, default=200)
    args = ap.parse_args()

    lm_ns, _ = load_spanish_lms()
    lex = GoldenAge1583Lexicon()

    v2_lines = load_lines(V2_PATH)
    oos_lines = load_lines(OOS_PATH)
    v2_parsed = extract_parsed(v2_lines)
    oos_parsed = extract_parsed(oos_lines)

    if args.dummy_all_e or args.dummy_all_a:
        ch = 'e' if args.dummy_all_e else 'a'
        lbl = 'DUMMY_ALL_E' if args.dummy_all_e else 'DUMMY_ALL_A'
        cm = {k: ch for k in C_MAP}
        vm = {k: '' for k in V_MAP}
        sm = {k: '' for k in S_MAP}
        em = {k: ch for k in EXACT_CORE}
        ok_all = True
        if args.target in ('2077_v2', 'both'):
            ok1, _ = run_validation(f'#2077_v2_{lbl}', v2_parsed, lm_ns, lex, cm, vm, sm, em, False, n_null=50, seed=1583)
            ok_all = ok_all and ok1
        if args.target in ('2518', 'both'):
            ok2, _ = run_validation(f'#2518_{lbl}', oos_parsed, lm_ns, lex, cm, vm, sm, em, False, n_null=50, seed=2518)
            ok_all = ok_all and ok2
        sys.exit(0 if ok_all else 1)

    p1, _ = run_validation(
        'Cat #2077 v2 (transcript_2077_v2.txt, 3116 tok) Frozen Cg.12 + Structural Rules',
        v2_parsed, lm_ns, lex, C_MAP, V_MAP, S_MAP, EXACT_CORE, include_short_noms=True, n_null=args.n_null, seed=1583,
    )
    p2, oos_txt = run_validation(
        'Cat #2518 OUT-OF-SAMPLE (transcript_2518.txt, 323 tok) ZERO-RETUNING Frozen Cg.12',
        oos_parsed, lm_ns, lex, C_MAP, V_MAP, S_MAP, EXACT_CORE, include_short_noms=True, n_null=args.n_null, seed=2518,
    )

    n_map, n_tot, out_lines, nom_ctx = decode_pretty(oos_lines, bare17='de')
    print(f'\n=== #2518 MECHANICAL ZERO-RETUNING DECODE ({n_map}/{n_tot} = {100*n_map/n_tot:.2f}% tokens mapped) ===')
    for lid, txt in out_lines:
        print(f'  {lid:7s}: {txt}')

    # Also test bare 17='y' vs 'de' on #2518 & v2
    print('\n=== #2518 NOMENCLATOR / UNMAPPED TOKEN CONTEXTS ===')
    for tok, ctxs in sorted(nom_ctx.items(), key=lambda x: (-len(x[1]), x[0])):
        for lid, l, r in ctxs:
            print(f'  {tok:6s} ({lid:6s}): ...{l} [{tok}] {r}...')

    sys.exit(0 if (p1 and p2) else 1)


if __name__ == '__main__':
    main()
