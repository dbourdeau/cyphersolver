#!/usr/bin/env python3
"""Leak-free synthetic Golden-Age Spanish control (held-out mendoza1589 f14_clear.txt)
encrypted into Philip II cifra-general style + dynamic PASS/FAIL & --dummy-all-e exit check."""
import argparse
import pathlib
import random
import re
import sys

THEORIES = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(THEORIES))

from lm_goldenage1583 import REPO, load_spanish_lms, GoldenAge1583Lexicon, clm
from solver_philip1583 import (
    profile_cipher,
    solve_cifra_general,
    run_dynamic_validation,
    z_stats,
)

MENDOZA_CLEAR = REPO / 'targets' / 'mendoza1589' / 'f14_clear.txt'


def load_heldout_mendoza():
    lines = []
    for ln in MENDOZA_CLEAR.read_text(encoding='utf-8').splitlines()[8:25]:
        # Strip inline annotations (nem+), {francia}, [tam], <...> cleanly
        s = re.sub(r'\([^)]*\)', '', ln)
        s = re.sub(r'\{[^}]*\}', '', s)
        s = re.sub(r'<[^>]*>', '', s)
        s = s.replace('[', '').replace(']', '')
        lines.append(s)
    return clm.norm(' '.join(lines), scheme='early', spaces=False)


def encrypt_philip_style(pt, seed=1583):
    """Encrypt held-out 1589 prose with homophones + 3% nulls (simulating Philip II cifra general)."""
    rng = random.Random(seed)
    # 44 synthetic cipher labels (numbers + 2/3-char tags)
    labels = [f'{i:02d}' for i in range(10, 52)] + ['nul1', 'nul2']
    rng.shuffle(labels)
    hom_spec = [
        ('e', 5), ('a', 5), ('o', 4), ('s', 3), ('n', 3), ('r', 3), ('i', 3),
        ('l', 2), ('d', 2), ('t', 2), ('c', 2), ('u', 2), ('m', 1), ('p', 1),
        ('q', 1), ('b', 1), ('y', 1), ('g', 1), ('f', 0), ('h', 0), ('z', 0),
    ]
    # Allocate 42 letter signs + 2 nulls
    enc = {}
    gt = {}
    pos = 0
    for ch, cnt in hom_spec:
        if cnt == 0:
            enc[ch] = [labels[pos - 1]]  # fallback for rare if needed
            continue
        enc[ch] = labels[pos:pos + cnt]
        for lb in enc[ch]:
            gt[lb] = ch
        pos += cnt
    # Assign 3 rare singletons f,h,z properly by trimming 1 from e,a,o -> exact 42
    enc = {}
    gt = {}
    hom_exact = [
        ('e', 4), ('a', 4), ('o', 3), ('s', 3), ('n', 3), ('r', 3), ('i', 3),
        ('l', 2), ('d', 2), ('t', 2), ('c', 2), ('u', 2), ('m', 1), ('p', 1),
        ('q', 1), ('b', 1), ('y', 1), ('g', 1), ('f', 1), ('h', 1), ('z', 1),
    ]
    # Sum = 42
    pos = 0
    for ch, cnt in hom_exact:
        enc[ch] = labels[pos:pos + cnt]
        for lb in enc[ch]:
            gt[lb] = ch
        pos += cnt
    nulls = labels[42:44]
    for nl in nulls:
        gt[nl] = ''

    ct = []
    for ch in pt:
        if rng.random() < 0.03:
            ct.append(rng.choice(nulls))
        ct.append(rng.choice(enc.get(ch, enc['s'])))
    return ct, gt, nulls


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dummy-all-e', action='store_true')
    args = ap.parse_args()

    lm_ns, _ = load_spanish_lms()
    lex = GoldenAge1583Lexicon()
    pt = load_heldout_mendoza()
    ct, gt, nulls = encrypt_philip_style(pt, seed=1583)

    if args.dummy_all_e:
        dummy = {t: 'e' for t in set(ct)}
        run_dynamic_validation(ct, dummy, lm_ns, lex, n_shuf_key=50, n_shuf_stream=50, strict_exit=True, label='Synth1583_DummyAllE')
        return

    profile_cipher(ct, label='Synthetic 1589 Held-Out Philip II Prose (mendoza1589 f14)')
    obj, kmap, lpc, _ = solve_cifra_general(
        ct, lm_ns, fixed=None, allow_nulls=True, allow_2char_for=None,
        n_restarts=16, steps=22000, min_distinct=18, max_null_frac=0.06, kl_weight=1.1, seed=1583
    )
    dec_pt = ''.join(kmap.get(t, '') for t in ct)
    # Strip nulls from ground truth comparison by comparing decoded vs true pt via char rate & Levenshtein/exact
    print(f'0-Crib Blind SA: LM/ch={lpc:.4f} | true_len={len(pt)} vs dec_len={len(dec_pt)}')
    print('True sample:   ', pt[:130])
    print('Decoded sample:', dec_pt[:130])

    # Equal-restart blind SA null controls (6 streams)
    rng = random.Random(1583)
    null_sa_lpc = []
    for k in range(6):
        st = list(ct)
        rng.shuffle(st)
        _, _, lpck, _ = solve_cifra_general(
            st, lm_ns, fixed=None, allow_nulls=True, allow_2char_for=None,
            n_restarts=16, steps=22000, min_distinct=18, max_null_frac=0.06, kl_weight=1.1, seed=2100 + k
        )
        null_sa_lpc.append(lpck)
    mu, sd, z, ge, p = z_stats(lpc, null_sa_lpc)
    print(f'Equal-Restart 0-Crib Blind SA (n=6): real={lpc:.4f} vs null={mu:.4f}±{sd:.4f} | z={z:+.2f} | >=real={ge}/6 (p={p:.4f})')

    run_dynamic_validation(ct, kmap, lm_ns, lex, n_shuf_key=200, n_shuf_stream=200, strict_exit=True, label='Synth1583_Blind')


if __name__ == '__main__':
    main()
