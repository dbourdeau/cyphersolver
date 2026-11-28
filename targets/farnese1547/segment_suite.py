#!/usr/bin/env python3
"""Comprehensive segmentation & structural analysis suite for Farnese 1547 (c. 78r).

Supports:
1. Run extraction from clean/diplomatic transcription files.
2. Fixed 2-digit phase & odd/even offset analysis vs shuffled controls.
3. Null-split segment length parity analysis (testing every candidate null digit 0-9).
4. Exhaustive 3^10 = 59,049 prefix-free partition search (mapping {0..9} -> {1, 2, 3}),
   calibrated against length-matched shuffled controls (IC ratio, type compression,
   zero-remainder line/run binomial p-value, bigram MI, repeated multi-token n-grams).
5. Non-prefix-free unsupervised segmentation: BPE compression (real vs shuffle vs Italian)
   and unigram EM (MAXL=2,3) + branching-entropy unit discovery.
6. 2-class vowel/consonant alternation partition & diplomatic mark distribution.
"""

from __future__ import annotations
import argparse
import collections
import itertools
import json
import math
import pathlib
import random
import re
from typing import Dict, List, Tuple


def load_clean_lines(path: pathlib.Path) -> List[Tuple[str, str]]:
    """Return list of (line_id, text) from c78_clean.txt or similar."""
    lines = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"^(L\d+)\s*[:|]?\s*(.*)$", s)
        if m:
            lines.append((m.group(1), m.group(2).strip()))
        else:
            lines.append((f"L{len(lines)+1:02d}", s))
    return lines


def extract_digit_runs_from_lines(lines: List[Tuple[str, str]]) -> Tuple[List[Tuple[str, str]], List[str]]:
    """Return (line_runs, contiguous_runs).
    line_runs: list of (line_id, digits_only_or_segments) per line where cleartext breaks a run.
    contiguous_runs: runs split ONLY at cleartext interpolations (joining across line breaks),
    and per_line_runs: runs split at BOTH line breaks and cleartext interpolations.
    """
    per_line_runs: List[Tuple[str, str]] = []
    stream_tokens: List[str] = []
    for lid, text in lines:
        # Remove bracketed notes if any, split on non-digit runs (cleartext words)
        # Keep only pure digit chunks; spaces within a digit run are collapsed
        # Wait: if cleartext word appears (letters), split run there.
        parts = re.split(r"[A-Za-zÀ-ÿ]+[^0-9]*", text)
        for idx, p in enumerate(parts):
            d = re.sub(r"[^0-9]", "", p)
            if d:
                tag = lid if len(parts) == 1 else f"{lid}.{idx+1}"
                per_line_runs.append((tag, d))
                stream_tokens.append(d)
            if idx < len(parts) - 1:
                stream_tokens.append("|")
        stream_tokens.append("\n")

    # Contiguous runs: join across '\n', split only at '|'
    joined = "".join(stream_tokens)
    contiguous_runs = [re.sub(r"[^0-9]", "", chunk) for chunk in joined.split("|")]
    contiguous_runs = [c for c in contiguous_runs if c]
    return per_line_runs, contiguous_runs


def index_of_coincidence(items: List[str]) -> float:
    n = len(items)
    if n < 2:
        return 0.0
    c = collections.Counter(items)
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


def entropy(items: List[str]) -> float:
    n = len(items)
    if n == 0:
        return 0.0
    c = collections.Counter(items)
    return -sum((v / n) * math.log2(v / n) for v in c.values())


def mutual_information_bigrams(items: List[str]) -> float:
    if len(items) < 2:
        return 0.0
    bg = collections.Counter(zip(items, items[1:]))
    tot = sum(bg.values())
    c1 = collections.Counter(a for a, _ in bg for _ in range(bg[(a, _)])) if False else None
    p1 = collections.Counter()
    p2 = collections.Counter()
    for (a, b), v in bg.items():
        p1[a] += v
        p2[b] += v
    mi = 0.0
    for (a, b), v in bg.items():
        pab = v / tot
        pa = p1[a] / tot
        pb = p2[b] / tot
        mi += pab * math.log2(pab / (pa * pb))
    return mi


def digit_profile(runs: List[str]) -> None:
    flat = "".join(runs)
    n = len(flat)
    c = collections.Counter(flat)
    print(f"=== DIGIT PROFILE ({len(runs)} contiguous runs, {n} total digits) ===")
    print("Frequencies:")
    for d in "0123456789":
        print(f"  {d}: {c[d]:4d} ({100*c[d]/n:5.2f}%)")
    print(f"Digit IC: {index_of_coincidence(list(flat)):.5f} (uniform=0.10000)")
    print(f"Digit H : {entropy(list(flat)):.4f} bits (uniform=3.3219)")

    bg = collections.Counter()
    for r in runs:
        for a, b in zip(r, r[1:]):
            bg[a + b] += 1
    print("\nDigit Bigram Matrix (row=first, col=second):")
    print("    " + "".join(f"{d:>5}" for d in "0123456789"))
    for a in "0123456789":
        print(f" {a}  " + "".join(f"{bg[a+b]:>5}" for b in "0123456789"))


def fixed_pair_analysis(per_line_runs: List[Tuple[str, str]], runs: List[str], n_shuf: int = 500) -> None:
    print("\n=== FIXED 2-DIGIT PAIR & PHASE ANALYSIS ===")
    even_lines = sum(1 for _, r in per_line_runs if len(r) % 2 == 0)
    odd_lines = len(per_line_runs) - even_lines
    print(f"Per-line/chunk lengths: {even_lines} even, {odd_lines} odd (total {len(per_line_runs)})")
    for tag, r in per_line_runs:
        if len(r) % 2 == 1:
            print(f"  ODD chunk {tag}: len={len(r)}")

    # Even vs odd offset distribution on contiguous runs
    even_pos = collections.Counter()
    odd_pos = collections.Counter()
    pairs_p0, pairs_p1 = [], []
    for r in runs:
        for i, ch in enumerate(r):
            if i % 2 == 0:
                even_pos[ch] += 1
            else:
                odd_pos[ch] += 1
        for i in range(0, len(r) - 1, 2):
            pairs_p0.append(r[i : i + 2])
        for i in range(1, len(r) - 1, 2):
            pairs_p1.append(r[i : i + 2])

    def chi2_even_odd(ep, op):
        tot_e = sum(ep.values())
        tot_o = sum(op.values())
        tot = tot_e + tot_o
        chi2 = 0.0
        for d in "0123456789":
            obs_e, obs_o = ep[d], op[d]
            row = obs_e + obs_o
            if row == 0:
                continue
            exp_e = row * tot_e / tot
            exp_o = row * tot_o / tot
            chi2 += (obs_e - exp_e) ** 2 / exp_e + (obs_o - exp_o) ** 2 / exp_o
        return chi2

    real_chi2 = chi2_even_odd(even_pos, odd_pos)
    ic_p0 = index_of_coincidence(pairs_p0)
    ic_p1 = index_of_coincidence(pairs_p1)

    rnd = random.Random(42)
    sh_chi2, sh_ic = [], []
    for _ in range(n_shuf):
        ep, op = collections.Counter(), collections.Counter()
        sp = []
        for r in runs:
            lst = list(r)
            rnd.shuffle(lst)
            sr = "".join(lst)
            for i, ch in enumerate(sr):
                if i % 2 == 0:
                    ep[ch] += 1
                else:
                    op[ch] += 1
            for i in range(0, len(sr) - 1, 2):
                sp.append(sr[i : i + 2])
        sh_chi2.append(chi2_even_odd(ep, op))
        sh_ic.append(index_of_coincidence(sp))

    mu_c, sd_c = sum(sh_chi2) / n_shuf, (sum((x - sum(sh_chi2) / n_shuf) ** 2 for x in sh_chi2) / n_shuf) ** 0.5
    mu_i, sd_i = sum(sh_ic) / n_shuf, (sum((x - sum(sh_ic) / n_shuf) ** 2 for x in sh_ic) / n_shuf) ** 0.5
    print(f"Even vs Odd offset chi2: real={real_chi2:.2f}, shuf={mu_c:.2f}+-{sd_c:.2f}, z={(real_chi2-mu_c)/(sd_c+1e-9):+.2f}")
    print(f"Pair IC (phase 0): real={ic_p0:.5f} ({len(set(pairs_p0))} types), shuf={mu_i:.5f}+-{sd_i:.5f}, z={(ic_p0-mu_i)/(sd_i+1e-9):+.2f}")
    print(f"Pair IC (phase 1): real={ic_p1:.5f} ({len(set(pairs_p1))} types)")
    print("Digit ratio even/odd:")
    for d in "0123456789":
        e, o = even_pos[d], odd_pos[d]
        print(f"  {d}: even={e:3d} odd={o:3d} ratio={e/(o+1e-9):.2f}")

    # Test null-split parity for each candidate null digit
    print("\nNull-split segment parity test (for each candidate single-digit null):")
    for nd in "0123456789":
        segs = []
        for r in runs:
            for s in r.split(nd):
                if s:
                    segs.append(s)
        ev = sum(1 for s in segs if len(s) % 2 == 0)
        od = len(segs) - ev
        # Phase chi2 inside even segments
        ep, op = collections.Counter(), collections.Counter()
        ep_pairs = []
        for s in segs:
            if len(s) >= 2:
                for i, ch in enumerate(s):
                    (ep if i % 2 == 0 else op)[ch] += 1
                for i in range(0, len(s) - 1, 2):
                    ep_pairs.append(s[i : i + 2])
        c2 = chi2_even_odd(ep, op) if ep and op else 0.0
        z_par = (ev - od) / math.sqrt(max(1, len(segs)))
        print(f"  null={nd}: {len(segs):3d} segs, even={ev:3d} odd={od:3d} (z_parity={z_par:+.2f}), phase_chi2={c2:6.2f}, pair_IC={index_of_coincidence(ep_pairs):.5f}")


def parse_prefix_partition(runs: List[str], lengths: Tuple[int, ...]) -> Tuple[List[str], int, int]:
    """Parse runs greedily using lengths[int(d)].
    Returns (tokens, zero_rem_runs, total_rem_digits).
    """
    toks = []
    zero_rem = 0
    rem_digits = 0
    for r in runs:
        i = 0
        n = len(r)
        while i < n:
            L = lengths[ord(r[i]) - 48]
            if i + L <= n:
                toks.append(r[i : i + L])
                i += L
            else:
                rem_digits += n - i
                break
        if i == n:
            zero_rem += 1
    return toks, zero_rem, rem_digits


def prefix_partition_search(per_line_runs: List[Tuple[str, str]], runs: List[str], top_k: int = 25) -> None:
    print("\n=== EXHAUSTIVE PREFIX-FREE PARTITION SEARCH (3^10 = 59,049 models) ===")
    line_strs = [r for _, r in per_line_runs]
    n_lines = len(line_strs)
    # Precompute shuffled streams (fixed seed) for fast calibration of top candidates
    rnd = random.Random(12345)
    shuf_streams = []
    for _ in range(20):
        s_runs = []
        for r in runs:
            lst = list(r)
            rnd.shuffle(lst)
            s_runs.append("".join(lst))
        shuf_streams.append(s_runs)

    # Also precompute shuffled line strings
    shuf_lines = []
    for _ in range(20):
        sl = []
        for r in line_strs:
            lst = list(r)
            rnd.shuffle(lst)
            sl.append("".join(lst))
        shuf_lines.append(sl)

    # First pass over all 59,049 partitions: compute line zero-remainders + contiguous token IC & types
    # Skip trivial all-1-digit (mean_len < 1.15) unless interesting, actually record everything and filter in ranking.
    candidates = []
    for lengths in itertools.product((1, 2, 3), repeat=10):
        n1 = lengths.count(1)
        n2 = lengths.count(2)
        n3 = lengths.count(3)
        if n1 == 10:
            continue
        # Parse contiguous runs for IC / compression
        toks, zr_runs, rem_runs = parse_prefix_partition(runs, lengths)
        if len(toks) < 50:
            continue
        # Parse per-line runs for zero-remainder check
        _, zr_lines, rem_lines = parse_prefix_partition(line_strs, lengths)

        # Quick score: IC * len(toks) or compare against expected random IC?
        # Wait: expected IC for a 1-2-3 partition depends strongly on digit frequencies and lengths!
        # We can compute theoretical baseline IC under independent digit draws!
        # Let p[d] be empirical digit probability in `runs`.
        # Expected probability of token w = d1..dk is P(w) = p[d1]*...*p[dk] (normalized over reachable tokens).
        # Let's compute exact independence IC analytically in O(1) using digit frequencies!
        candidates.append((zr_lines, -rem_lines, zr_runs, -rem_runs, lengths, toks))

    # Compute exact digit probabilities for analytical independence baseline
    flat = "".join(runs)
    ntot = len(flat)
    dfreq = [flat.count(str(d)) / ntot for d in range(10)]

    scored = []
    for zr_lines, neg_rem_lines, zr_runs, neg_rem_runs, lengths, toks in candidates:
        ntok = len(toks)
        ic_real = index_of_coincidence(toks)
        # Analytical baseline IC under iid digits with same lead-length distribution:
        # Actually, lead digit d appears with prob ~ dfreq[d] / mean_len? Wait: under iid draws,
        # the stationary probability of starting a token with d is dfreq[d] / sum_x dfreq[x] (approx)!
        # More accurately, sum_{w} P_iid(w)^2: let Z = sum_{d} dfreq[d] * 1? No, in iid sequence,
        # every digit has equal chance to be at a token start if lengths didn't bias it, wait:
        # Better: check BOTH analytical ratio AND shuffle exact z-score for top 1000!
        # Fast proxy for iid IC: sum over valid tokens w of (dfreq[w[0]] * prod_{j>0} dfreq[w[j]])^2
        # Wait: exact stationary prob of lead d in iid renewal process is dfreq[d] * (1? No, E[L] * pi(d) != dfreq[d] when L(d) differs!).
        # Actually, empirical lead distribution is sum_w count(w)/ntok; under iid trailing digits,
        # P(d1 d2 .. dk) = P_lead(d1) * prod_{j>=2} dfreq[dj].
        c_tok = collections.Counter(toks)
        lead_cnt = [0] * 10
        for w, cnt in c_tok.items():
            lead_cnt[ord(w[0]) - 48] += cnt
        ic_iid = 0.0
        for d in range(10):
            pl = lead_cnt[d] / ntok
            if pl == 0:
                continue
            L = lengths[d]
            if L == 1:
                ic_iid += pl * pl
            elif L == 2:
                ic_iid += (pl * pl) * sum(p * p for p in dfreq)
            else:
                s2 = sum(p * p for p in dfreq)
                ic_iid += (pl * pl) * s2 * s2
        ic_ratio = ic_real / max(ic_iid, 1e-9)
        h_real = entropy(toks)
        # Expected bits/digit under iid tokens vs real
        mean_len = sum(len(t) for t in toks) / ntok
        bpd_real = h_real / mean_len

        # Combined preliminary rank: high line zero-remainder AND high IC ratio AND low bpd
        # Also track pure IC ratio separately so we don't miss wrapping-line ciphers!
        scored.append((ic_ratio, zr_lines, -rem_lines, bpd_real, len(c_tok), ntok, lengths))

    # Top 150 by ic_ratio and top 150 by zr_lines (with mean_len >= 1.4)
    by_ic = sorted(scored, key=lambda x: x[0], reverse=True)[:150]
    by_zr = sorted([x for x in scored if x[6].count(1) <= 7], key=lambda x: (x[1], x[2], x[0]), reverse=True)[:150]
    pool_lengths = {x[6] for x in by_ic} | {x[6] for x in by_zr}
    # Always include pure 2-digit (2,)*10 and pure 3-digit (3,)*10
    pool_lengths.add((2,) * 10)
    pool_lengths.add((3,) * 10)

    print(f"Evaluated {len(candidates)} partitions; running 20x shuffled controls on top {len(pool_lengths)} candidates...")

    calibrated = []
    for lengths in pool_lengths:
        toks, zr_runs, rem_runs = parse_prefix_partition(runs, lengths)
        _, zr_lines, rem_lines = parse_prefix_partition(line_strs, lengths)
        ic_real = index_of_coincidence(toks)
        mi_real = mutual_information_bigrams(toks)
        ntypes_real = len(set(toks))
        ntok_real = len(toks)

        # Count repeated 3-grams and 4-grams of tokens
        bg_toks = collections.Counter(zip(toks, toks[1:]))
        tg_toks = collections.Counter(zip(toks, toks[1:], toks[2:]))
        rep3_real = sum(v - 1 for v in tg_toks.values() if v >= 2)

        sh_ics, sh_mis, sh_types, sh_zr, sh_rep3 = [], [], [], [], []
        for s_runs, s_lines in zip(shuf_streams, shuf_lines):
            stoks, _, _ = parse_prefix_partition(s_runs, lengths)
            _, szr, _ = parse_prefix_partition(s_lines, lengths)
            sh_ics.append(index_of_coincidence(stoks))
            sh_mis.append(mutual_information_bigrams(stoks))
            sh_types.append(len(set(stoks)))
            sh_zr.append(szr)
            stg = collections.Counter(zip(stoks, stoks[1:], stoks[2:]))
            sh_rep3.append(sum(v - 1 for v in stg.values() if v >= 2))

        def zscore(val, arr):
            m = sum(arr) / len(arr)
            sd = (sum((x - m) ** 2 for x in arr) / len(arr)) ** 0.5
            return (val - m) / (sd + 1e-9), m

        z_ic, mu_ic = zscore(ic_real, sh_ics)
        z_mi, mu_mi = zscore(mi_real, sh_mis)
        z_ty, mu_ty = zscore(ntypes_real, sh_types)  # negative = fewer types than shuffle (good!)
        z_zr, mu_zr = zscore(zr_lines, sh_zr)
        z_r3, mu_r3 = zscore(rep3_real, sh_rep3)

        calibrated.append({
            "lengths": lengths,
            "1s": "".join(str(d) for d, l in enumerate(lengths) if l == 1),
            "2s": "".join(str(d) for d, l in enumerate(lengths) if l == 2),
            "3s": "".join(str(d) for d, l in enumerate(lengths) if l == 3),
            "ntok": ntok_real,
            "ntypes": ntypes_real,
            "mu_types": mu_ty,
            "zr_lines": zr_lines,
            "n_lines": n_lines,
            "rem_lines": rem_lines,
            "z_zr": z_zr,
            "ic": ic_real,
            "ic_ratio": ic_real / (mu_ic + 1e-9),
            "z_ic": z_ic,
            "mi_diff": mi_real - mu_mi,
            "z_mi": z_mi,
            "rep3": rep3_real,
            "mu_rep3": mu_r3,
            "z_rep3": z_r3,
            "z_types": z_ty,
            "score": z_ic + z_zr + 0.5 * z_r3 - 0.5 * z_ty,
        })

    calibrated.sort(key=lambda d: d["ic_ratio"], reverse=True)
    print(f"\nTop {top_k} by IC_real / IC_shuffled:")
    print("  1s         2s         3s         | tok  typ(shuf) | zr/ln (z_zr) | IC_rat (z_ic) | rep3(shuf) | MI_diff")
    for r in calibrated[:top_k]:
        print(
            f"  {r['1s']:10s} {r['2s']:10s} {r['3s']:10s} | "
            f"{r['ntok']:4d} {r['ntypes']:3d}({r['mu_types']:5.1f}) | "
            f"{r['zr_lines']:2d}/{r['n_lines']:2d} ({r['z_zr']:+5.1f}) | "
            f"{r['ic_ratio']:6.3f} ({r['z_ic']:+5.1f}) | "
            f"{r['rep3']:3d}({r['mu_rep3']:5.1f}) | {r['mi_diff']:+.4f}"
        )

    calibrated.sort(key=lambda d: (d["zr_lines"], -d["rem_lines"], d["ic_ratio"]), reverse=True)
    print(f"\nTop {top_k} by zero-remainder line parses (1s <= 7):")
    print("  1s         2s         3s         | tok  typ(shuf) | zr/ln (rem)  | IC_rat (z_ic) | rep3(shuf) | MI_diff")
    cnt = 0
    for r in calibrated:
        if len(r["1s"]) > 7:
            continue
        print(
            f"  {r['1s']:10s} {r['2s']:10s} {r['3s']:10s} | "
            f"{r['ntok']:4d} {r['ntypes']:3d}({r['mu_types']:5.1f}) | "
            f"{r['zr_lines']:2d}/{r['n_lines']:2d} ({r['rem_lines']:3d})  | "
            f"{r['ic_ratio']:6.3f} ({r['z_ic']:+5.1f}) | "
            f"{r['rep3']:3d}({r['mu_rep3']:5.1f}) | {r['mi_diff']:+.4f}"
        )
        cnt += 1
        if cnt >= top_k:
            break


def repeated_ngrams_report(runs: List[str]) -> None:
    print("\n=== LONG REPEATED DIGIT SUBSTRINGS & BRANCHING ENTROPY ===")
    rnd = random.Random(99)
    shuf_runs = []
    for r in runs:
        lst = list(r)
        rnd.shuffle(lst)
        shuf_runs.append("".join(lst))

    for k in range(3, 13):
        c_real = collections.Counter()
        c_shuf = collections.Counter()
        for r in runs:
            for i in range(len(r) - k + 1):
                c_real[r[i : i + k]] += 1
        for r in shuf_runs:
            for i in range(len(r) - k + 1):
                c_shuf[r[i : i + k]] += 1
        rep_r = sum(v - 1 for v in c_real.values() if v >= 2)
        rep_s = sum(v - 1 for v in c_shuf.values() if v >= 2)
        types_r = sum(1 for v in c_real.values() if v >= 2)
        types_s = sum(1 for v in c_shuf.values() if v >= 2)
        print(f"  k={k:2d}: real={types_r:4d} repeated types ({rep_r:4d} excess occ) | shuf={types_s:4d} ({rep_s:4d} excess)")

    print("\nTop repeated 5-10 digit substrings with left/right branching entropy:")
    def H(c):
        n = sum(c.values())
        return -sum((v / n) * math.log2(v / n) for v in c.values()) if n else 0.0

    rows = []
    for k in (4, 5, 6, 7, 8, 9):
        c = collections.Counter()
        for r in runs:
            for i in range(len(r) - k + 1):
                c[r[i : i + k]] += 1
        min_v = 8 if k == 4 else 5 if k == 5 else 3 if k == 6 else 2
        for g, v in c.items():
            if v < min_v:
                continue
            L, R = collections.Counter(), collections.Counter()
            for r in runs:
                i = r.find(g)
                while i >= 0:
                    if i > 0:
                        L[r[i - 1]] += 1
                    if i + k < len(r):
                        R[r[i + k]] += 1
                    i = r.find(g, i + 1)
            rows.append((min(H(L), H(R)), k, v, g, H(L), H(R)))
    rows.sort(key=lambda x: (x[1], x[2], x[0]), reverse=True)
    for m, k, v, g, hl, hr in rows[:45]:
        print(f"  len={k} {g:10s} n={v:3d}  H_L={hl:.2f} H_R={hr:.2f}")


def bpe_analysis(runs: List[str], merges: int = 120) -> None:
    print(f"\n=== GREEDY BPE COMPRESSION (merges={merges}) ===")
    def run_bpe(seq):
        toks = list(seq)
        vocab = []
        for _ in range(merges):
            pairs = collections.Counter(zip(toks, toks[1:]))
            if not pairs:
                break
            (a, b), n = pairs.most_common(1)[0]
            if n < 3:
                break
            new = a + b
            out, i = [], 0
            while i < len(toks):
                if i + 1 < len(toks) and toks[i] == a and toks[i + 1] == b:
                    out.append(new)
                    i += 2
                else:
                    out.append(toks[i])
                    i += 1
            toks = out
            vocab.append((new, n))
        c = collections.Counter(toks)
        nt = len(toks)
        H = -sum((v / nt) * math.log2(v / nt) for v in c.values())
        dl = nt * H + sum(len(t) * math.log2(10) for t in c if len(t) > 1)
        return toks, vocab, dl, H

    real_seq = list("|".join(runs))
    # Don't merge across '|'
    def run_bpe_runs(rlist):
        toks = []
        for idx, r in enumerate(rlist):
            if idx > 0:
                toks.append("|")
            toks.extend(list(r))
        vocab = []
        for _ in range(merges):
            pairs = collections.Counter((a, b) for a, b in zip(toks, toks[1:]) if a != "|" and b != "|")
            if not pairs:
                break
            (a, b), n = pairs.most_common(1)[0]
            if n < 3:
                break
            new = a + b
            out, i = [], 0
            while i < len(toks):
                if i + 1 < len(toks) and toks[i] == a and toks[i + 1] == b:
                    out.append(new)
                    i += 2
                else:
                    out.append(toks[i])
                    i += 1
            toks = out
            vocab.append((new, n))
        clean_toks = [t for t in toks if t != "|"]
        c = collections.Counter(clean_toks)
        nt = len(clean_toks)
        H = -sum((v / nt) * math.log2(v / nt) for v in c.values())
        dl = nt * H + sum(len(t) * math.log2(10) for t in c if len(t) > 1)
        return clean_toks, vocab, dl, H

    rtoks, rvoc, rdl, rH = run_bpe_runs(runs)
    rnd = random.Random(19)
    sh_runs = []
    for r in runs:
        lst = list(r)
        rnd.shuffle(lst)
        sh_runs.append("".join(lst))
    stoks, svoc, sdl, sH = run_bpe_runs(sh_runs)
    base_toks = [d for r in runs for d in r]
    base_dl = len(base_toks) * entropy(base_toks)

    print(f"Real   : {len(base_toks)} digits -> {len(rtoks)} tokens, {len(rvoc)} merges, H={rH:.3f}, DL={rdl:.0f} (gain {100*(base_dl-rdl)/base_dl:.1f}%)")
    print(f"Shuffle: {len(base_toks)} digits -> {len(stoks)} tokens, {len(svoc)} merges, H={sH:.3f}, DL={sdl:.0f} (gain {100*(base_dl-sdl)/base_dl:.1f}%)")
    print("First 30 BPE merges (real):", ", ".join(f"{u}({n})" for u, n in rvoc[:30]))
    lens = collections.Counter(len(t) for t in rtoks)
    print("BPE token length distribution:", {k: f"{100*v/len(rtoks):.1f}%" for k, v in sorted(lens.items())})
    top_toks = collections.Counter(rtoks).most_common(30)
    print("Top 30 BPE tokens:", ", ".join(f"{t}:{c}" for t, c in top_toks))


def vowel_consonant_partition(runs: List[str]) -> None:
    print("\n=== 2-CLASS DIGIT ALTERNATION PARTITION (SUKHOTIN/VATICAN5) ===")
    bg = collections.Counter()
    for r in runs:
        for a, b in zip(r, r[1:]):
            bg[a + b] += 1
    tot = sum(bg.values())
    res = []
    for mask in range(1, 512):
        V = {"0"} | {str(d) for d in range(1, 10) if (mask >> (d - 1)) & 1}
        alt = sum(c for p, c in bg.items() if (p[0] in V) != (p[1] in V))
        res.append((alt / tot, "".join(sorted(V))))
    res.sort(reverse=True)
    for r, A in res[:8]:
        B = "".join(d for d in "0123456789" if d not in A)
        print(f"  alt={r:.4f}  A={A:10s}  B={B}")


def unigram_em_segmentation(runs: List[str], maxl: int = 3, alpha: float = 0.05, prune: float = 2.0, iters: int = 60) -> None:
    print(f"\n=== UNIGRAM EM SEGMENTATION (MAXL={maxl}, ALPHA={alpha}, PRUNE={prune}) ===")
    def digamma(x):
        r = 0.0
        while x < 6:
            r -= 1.0 / x
            x += 1
        return r + math.log(x) - 1 / (2 * x) - 1 / (12 * x * x) + 1 / (120 * x**4) - 1 / (252 * x**6)

    def fwd_bwd(s, p):
        n = len(s)
        a = [0.0] * (n + 1)
        a[0] = 1.0
        for i in range(1, n + 1):
            v = 0.0
            for L in range(1, maxl + 1):
                if i - L >= 0:
                    pu = p.get(s[i - L : i])
                    if pu:
                        v += a[i - L] * pu
            a[i] = v
        b = [0.0] * (n + 1)
        b[n] = 1.0
        for i in range(n - 1, -1, -1):
            v = 0.0
            for L in range(1, maxl + 1):
                if i + L <= n:
                    pu = p.get(s[i : i + L])
                    if pu:
                        v += pu * b[i + L]
            b[i] = v
        return a, b

    ndig = sum(len(s) for s in runs)
    cnt = collections.Counter()
    for s in runs:
        for i in range(len(s)):
            for L in range(1, maxl + 1):
                if i + L <= len(s):
                    cnt[s[i : i + L]] += 1.0 / L
    tot = sum(cnt.values())
    p = {u: c / tot for u, c in cnt.items()}
    for it in range(iters):
        exp = collections.Counter()
        ll = 0.0
        for s in runs:
            a, b = fwd_bwd(s, p)
            Z = a[len(s)]
            if Z <= 0:
                continue
            ll += math.log(Z)
            for i in range(len(s)):
                for L in range(1, maxl + 1):
                    if i + L <= len(s):
                        u = s[i : i + L]
                        pu = p.get(u)
                        if pu:
                            exp[u] += a[i] * pu * b[i + L] / Z
        keep = {u: c for u, c in exp.items() if c >= prune or len(u) == 1}
        K = len(keep)
        T = sum(keep.values())
        denom = digamma(T + alpha * K)
        p = {u: math.exp(digamma(c + alpha) - denom) for u, c in keep.items()}
        if it in (0, 29, iters - 1):
            print(f"  iter {it:2d}: loglik={ll:9.1f} types={K:4d} bpd={-ll/math.log(2)/ndig:.3f}")

    # Viterbi decode
    all_toks = []
    for s in runs:
        n = len(s)
        best = [-1e300] * (n + 1)
        back = [0] * (n + 1)
        best[0] = 0.0
        for i in range(1, n + 1):
            for L in range(1, maxl + 1):
                if i - L >= 0:
                    pu = p.get(s[i - L : i])
                    if pu and best[i - L] + math.log(pu) > best[i]:
                        best[i] = best[i - L] + math.log(pu)
                        back[i] = L
        out = []
        i = n
        while i > 0:
            out.append(s[i - back[i] : i])
            i -= back[i]
        all_toks.extend(out[::-1])

    uc = collections.Counter(all_toks)
    print(f"Viterbi: {len(all_toks)} tokens, {len(uc)} types, mean_len={ndig/len(all_toks):.2f}")
    print("Length breakdown:", dict(collections.Counter(len(u) for u in all_toks)))
    print("Top 50 EM units:", ", ".join(f"{u}:{c}" for u, c in uc.most_common(50)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clean_file", type=pathlib.Path)
    args = ap.parse_args()

    lines = load_clean_lines(args.clean_file)
    per_line_runs, contiguous_runs = extract_digit_runs_from_lines(lines)
    digit_profile(contiguous_runs)
    fixed_pair_analysis(per_line_runs, contiguous_runs)
    repeated_ngrams_report(contiguous_runs)
    vowel_consonant_partition(contiguous_runs)
    bpe_analysis(contiguous_runs)
    unigram_em_segmentation(contiguous_runs, maxl=2)
    unigram_em_segmentation(contiguous_runs, maxl=3)
    prefix_partition_search(per_line_runs, contiguous_runs)


if __name__ == "__main__":
    main()
