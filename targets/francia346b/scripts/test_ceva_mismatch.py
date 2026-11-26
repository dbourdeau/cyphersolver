#!/usr/bin/env python3
"""Reproducible test proving that the published Ceva key (targets/francia346) does NOT fit
DECODE R5634, R5638, or R5639, with R5635 as a positive control and 100 digit-shuffled controls.

Uses only Python stdlib plus files already in this repository:
  - lang/lexicons/it.json.gz (Italian lexicon for character 4-gram and >=4-letter word scoring)
  - targets/francia346/key-and-key-free-read/key.tsv (published Ceva key)
  - targets/francia346/transcription/R5635_f205r_digits.txt (Ceva positive control)
  - targets/francia346b/key.tsv and transcription/ (R5634, R5638, R5639)

Why digit-shuffle nulls (holding each key fixed):
  Ceva's published key assigns 3-4 homophones to every Italian vowel plus 14 Italian syllables,
  so random digits decoded under Ceva still appear vowel-rich compared to uniform letter
  permutations. Shuffling the ciphertext digits inside each segment while holding each key
  fixed preserves exact key-output unigram statistics and tests real cipher structure cleanly.
"""
from __future__ import annotations

import collections
import gzip
import json
import math
import pathlib
import random
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
TARGET = HERE.parent
REPO = TARGET.parent.parent
sys.path.insert(0, str(HERE))
import decode as dec_mod


def load_italian_lm_and_words(lex_path: pathlib.Path):
    with gzip.open(lex_path, "rt", encoding="utf-8") as f:
        lex = json.load(f)
    c1: collections.Counter[str] = collections.Counter()
    c2: collections.Counter[str] = collections.Counter()
    c3: collections.Counter[str] = collections.Counter()
    c4: collections.Counter[str] = collections.Counter()
    words5: set[str] = set()
    tot1 = 0
    for word, freq in lex.items():
        w = re.sub(r"[^a-z]", "", word.lower())
        if len(w) < 2:
            continue
        wt = int(freq)
        if len(w) >= 5 and wt >= 20:
            words5.add(w)
        for i, ch in enumerate(w):
            c1[ch] += wt
            tot1 += wt
            if i >= 1:
                c2[w[i - 1 : i + 1]] += wt
            if i >= 2:
                c3[w[i - 2 : i + 1]] += wt
            if i >= 3:
                c4[w[i - 3 : i + 1]] += wt
    return (c1, c2, c3, c4, tot1), words5


def score_italian(text: str, lm) -> float:
    c1, c2, c3, c4, tot1 = lm
    s = re.sub(r"[^a-z]", "", text.lower())
    if len(s) < 4:
        return -10.0
    tot = 0.0
    n = 0
    for i in range(3, len(s)):
        p1 = (c1[s[i]] + 0.5) / (tot1 + 13.0)
        p2 = (c2[s[i - 1 : i + 1]] + 0.2) / (c1[s[i - 1]] + 5.2) if c1[s[i - 1]] else p1
        p3 = (c3[s[i - 2 : i + 1]] + 0.1) / (c2[s[i - 2 : i]] + 2.6) if c2[s[i - 2 : i]] else p2
        p4 = (c4[s[i - 3 : i + 1]] + 0.05) / (c3[s[i - 3 : i]] + 1.3) if c3[s[i - 3 : i]] else p3
        tot += math.log(0.55 * p4 + 0.25 * p3 + 0.15 * p2 + 0.05 * p1)
        n += 1
    return tot / n


def word5_coverage(text: str, words5: set[str]) -> float:
    s = re.sub(r"[^a-z]", "", text.lower())
    n = len(s)
    if n < 5:
        return 0.0
    cov = [False] * n
    for L in range(5, 13):
        for i in range(0, n - L + 1):
            if s[i : i + L] in words5:
                for j in range(i, i + L):
                    cov[j] = True
    return sum(cov) / n


def load_ceva_key(path: pathlib.Path) -> dict[str, str]:
    ceva: dict[str, str] = {}
    for ln in path.read_text(encoding="utf-8").splitlines():
        if not ln.strip() or ln.startswith("#") or ln.startswith("code\t"):
            continue
        parts = ln.split("\t")
        code, kind, val = parts[0], parts[1], parts[2]
        if kind in ("word space", "null"):
            ceva[code] = ""
        elif kind in ("letter", "syllable") and val != "-":
            ceva[code] = val
    return ceva


def decode_ceva(segs: list[str], ceva: dict[str, str]) -> str:
    out = []
    for seg in segs:
        i = 0
        n = len(seg)
        while i < n:
            if seg[i] == "6":
                i += 1
                continue
            if i + 2 <= n:
                pair = seg[i : i + 2]
                if pair in ceva:
                    out.append(ceva[pair])
                i += 2
            else:
                i += 1
    return "".join(out)


def read_all_segments(paths: list[pathlib.Path]) -> list[str]:
    segs: list[str] = []
    for p in paths:
        for ln in p.read_text(encoding="utf-8").splitlines():
            if not re.match(r"^C\d+ ", ln):
                continue
            _, body = ln.split(" ", 1)
            segs.extend(dec_mod.row_to_segments(body))
    return segs


def shuffle_segments(segs: list[str], rng: random.Random) -> list[str]:
    out = []
    for s in segs:
        chars = list(s)
        rng.shuffle(chars)
        out.append("".join(chars))
    return out


def main() -> None:
    lm, words5 = load_italian_lm_and_words(REPO / "lang" / "lexicons" / "it.json.gz")
    ceva = load_ceva_key(REPO / "targets" / "francia346" / "key-and-key-free-read" / "key.tsv")
    alt_key, alt_tot = dec_mod.load_key(TARGET / "key.tsv")

    datasets = [
        ("R5635 (Ceva control)", [REPO / "targets" / "francia346" / "transcription" / "R5635_f205r_digits.txt"]),
        ("R5634", [TARGET / "transcription" / "R5634_f190r_digits.txt", TARGET / "transcription" / "R5634_f190v_digits.txt"]),
        ("R5638", [TARGET / "transcription" / "R5638_f218r_digits.txt", TARGET / "transcription" / "R5638_f218v_digits.txt"]),
        ("R5639", [TARGET / "transcription" / "R5639_f220r_digits.txt", TARGET / "transcription" / "R5639_f220v_digits.txt"]),
    ]

    rng = random.Random(346)
    n_null = 100

    print("| Record | Digits | Ceva LM4 vs digit-shuffle null (Z) | Ceva >=5-ltr word cov | Alt-key LM4 vs digit-shuffle null (Z) | Alt >=5-ltr word cov |")
    print("| --- | ---: | ---: | ---: | ---: | ---: |")
    for label, paths in datasets:
        segs = read_all_segments(paths)
        ndig = sum(len(s) for s in segs)

        c_txt = decode_ceva(segs, ceva)
        c_sc = score_italian(c_txt, lm)
        c_cov = word5_coverage(c_txt, words5)

        a_txt = "".join(dec_mod.dp_decode_segment(s, alt_key, alt_tot)[0] for s in segs)
        a_sc = score_italian(a_txt, lm)
        a_cov = word5_coverage(a_txt, words5)

        c_nulls, a_nulls = [], []
        for _ in range(n_null):
            sh = shuffle_segments(segs, rng)
            c_nulls.append(score_italian(decode_ceva(sh, ceva), lm))
            a_nulls.append(score_italian("".join(dec_mod.dp_decode_segment(s, alt_key, alt_tot)[0] for s in sh), lm))

        c_mu = sum(c_nulls) / n_null
        c_sd = math.sqrt(sum((x - c_mu) ** 2 for x in c_nulls) / n_null)
        c_z = (c_sc - c_mu) / max(c_sd, 1e-9)

        a_mu = sum(a_nulls) / n_null
        a_sd = math.sqrt(sum((x - a_mu) ** 2 for x in a_nulls) / n_null)
        a_z = (a_sc - a_mu) / max(a_sd, 1e-9)

        print(
            f"| {label} | {ndig} | {c_sc:.3f} vs {c_mu:.3f} +/- {c_sd:.3f} (Z={c_z:+.1f}) | {100*c_cov:.1f}% | "
            f"{a_sc:.3f} vs {a_mu:.3f} +/- {a_sd:.3f} (Z={a_z:+.1f}) | {100*a_cov:.1f}% |"
        )


if __name__ == "__main__":
    main()
