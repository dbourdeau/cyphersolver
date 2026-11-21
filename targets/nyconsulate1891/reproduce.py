#!/usr/bin/env python3
"""Standalone verifier and mechanical decoder for Imperial Russian cipher key No. 375 (catalogue 756).

Usage:
    python3 targets/nyconsulate1891/reproduce.py           # verify all files, counts, and holdout test
    python3 targets/nyconsulate1891/reproduce.py --write   # regenerate *_decode.txt from key375.tsv + *_digits.txt
"""
from __future__ import annotations
import hashlib
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = ["3902", "4945", "5078", "5015", "519", "4166"]
EXPECTED = {
    "3902": (316, 417, 135),
    "4945": (40, 60, 24),
    "5078": (257, 268, 252),
    "5015": (118, 128, 114),
    "519":  (192, 242, 82),
    "4166": (57, 134, 34),
}


def load_key(path: Path) -> dict[tuple[int, str], tuple[str, str]]:
    table: dict[tuple[int, str], tuple[str, str]] = {}
    by_rank_pair: dict[int, set[str]] = {1: set(), 2: set()}
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.split("\t")
        rk, code, pair, grade = int(parts[0]), parts[1], parts[2], parts[3]
        assert rk in (1, 2) and len(code) == 3 and code.isdigit(), f"Bad code: {line}"
        assert len(pair) == 2, f"Bad bigram: {line}"
        assert (rk, code) not in table, f"Duplicate code {(rk, code)}"
        assert pair not in by_rank_pair[rk], f"Duplicate bigram {pair} in rank {rk}"
        table[(rk, code)] = (pair, grade)
        by_rank_pair[rk].add(pair)
    return table


def load_digits(doc_id: str, frame_hashes: dict[int, str]) -> tuple[list[tuple[str, list[str]]], str]:
    path = HERE / f"{doc_id}_digits.txt"
    rows: list[tuple[str, list[str]]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            m = re.search(r"frame\s+(\d+):.*sha256_tiff=([0-9a-f]{64})", line)
            if m:
                fr, digest = int(m.group(1)), m.group(2)
                assert frame_hashes.get(fr) == digest, f"Hash mismatch for frame {fr} in {path.name}"
            continue
        lid, rest = line.split(None, 1)
        groups = rest.split()
        for g in groups:
            assert len(g) == 2 and all(ch.isdigit() or ch == "?" for ch in g), f"Bad group {g} in {lid}"
        rows.append((lid, groups))
    stream = "".join(g for _, gs in rows for g in gs)
    return rows, stream


def decode_triples(stream: str, key: dict[tuple[int, str], tuple[str, str]]) -> tuple[list[tuple[int, int, str, str, str]], str]:
    n = len(stream) // 3
    tail = stream[3 * n :]
    out: list[tuple[int, int, str, str, str]] = []
    for i in range(n):
        rk = 1 if (i % 2 == 0) else 2
        code = stream[3 * i : 3 * i + 3]
        if "?" in code or (rk, code) not in key:
            pair, grade = "??", ""
        else:
            pair, grade = key[(rk, code)]
        out.append((i + 1, rk, code, pair, grade))
    return out, tail


def grid_stream(triples: list[tuple[int, int, str, str, str]], width: int = 24) -> str:
    chars: list[str] = []
    for start in range(0, len(triples), width):
        blk = triples[start : start + width]
        chars.extend(t[3][0] for t in blk)
        chars.extend(t[3][1] for t in blk)
    return "".join(chars)


def format_decode_file(doc_id: str, triples: list[tuple[int, int, str, str, str]], tail: str) -> str:
    n = len(triples)
    full = sum(1 for t in triples if t[3] != "??")
    direct_k = sum(1 for t in triples if t[4] == "K")
    lines = [
        f"# Unedited mechanical decryption of No. {doc_id} under key375.tsv",
        f"# Whole triples decoded: {full}/{n} ({100.0 * full / n:.2f}%), direct K triples: {direct_k}",
        f"# Convention: '-' is the encrypted word-space symbol; '?' marks an unkeyed or overwritten position; nothing is supplied from clear text.",
    ]
    if tail:
        lines.append(f"# Trailing ungrouped digit(s) after {n} triples: {tail}")
    lines.append("")

    for start in range(0, n, 24):
        blk = triples[start : start + 24]
        end = start + len(blk)
        lines.append(f"{start + 1}-{end}")
        lines.append("C " + " ".join(t[2] for t in blk))
        lines.append("U " + " ".join(f" {t[3][0]} " for t in blk))
        lines.append("L " + " ".join(f" {t[3][1]} " for t in blk))
    lines.append("")
    lines.append("# Horizontal row-pair character stream (unedited):")
    raw_text = grid_stream(triples, 24)
    for start in range(0, len(raw_text), 48):
        lines.append(raw_text[start : start + 48])
    return "\n".join(lines) + "\n"


def verify_4166_holdout(stream_4166: str) -> None:
    frozen = load_key(HERE / "frozen_471_key.tsv")
    direct_only = {k: v for k, v in frozen.items() if v[1] == "K"}
    assert len(frozen) == 471 and len(direct_only) == 285

    target_phrase = "на-письменном-вашем-заявлении"
    triples_full, _ = decode_triples(stream_4166, frozen)
    triples_k, _ = decode_triples(stream_4166, direct_only)
    s_full = grid_stream(triples_full, 24)
    s_k = grid_stream(triples_k, 24)

    # Position 199 (1-based) = index 198 (0-based)
    win_full = s_full[198 : 198 + len(target_phrase)]
    win_k = s_k[198 : 198 + len(target_phrase)]
    known_full = sum(1 for c in win_full if c != "?")
    hits_full = sum(1 for c, t in zip(win_full, target_phrase) if c != "?" and c == t)
    known_k = sum(1 for c in win_k if c != "?")
    hits_k = sum(1 for c, t in zip(win_k, target_phrase) if c != "?" and c == t)
    assert (hits_full, known_full) == (15, 15), (hits_full, known_full, win_full)
    assert (hits_k, known_k) == (9, 9), (hits_k, known_k, win_k)

    # Pre-registered rank-preserving permutation test (9,999 shuffles across all offsets of the 268-cell grid)
    rng = random.Random(20261119)
    r1_codes = [c for (r, c) in frozen if r == 1]
    r1_vals = [frozen[(1, c)] for c in r1_codes]
    r2_codes = [c for (r, c) in frozen if r == 2]
    r2_vals = [frozen[(2, c)] for c in r2_codes]
    # Note: shuffling code addresses across 000..999 within each rank preserves marginal hit rates
    all_codes = [f"{i:03d}" for i in range(1000)]
    max_ge = 0
    best_perm = -999
    n_cells = len(s_full)
    max_off = n_cells - len(target_phrase) + 1
    for _ in range(9999):
        shuf1 = rng.sample(all_codes, len(r1_vals))
        shuf2 = rng.sample(all_codes, len(r2_vals))
        pk = {(1, c): v for c, v in zip(shuf1, r1_vals)}
        pk.update({(2, c): v for c, v in zip(shuf2, r2_vals)})
        pt, _ = decode_triples(stream_4166, pk)
        ps = grid_stream(pt, 24)
        best_here = -999
        for off in range(max_off):
            sc = 0
            for j, tch in enumerate(target_phrase):
                ch = ps[off + j]
                if ch != "?":
                    sc += 1 if ch == tch else -1
            if sc > best_here:
                best_here = sc
        if best_here > best_perm:
            best_perm = best_here
        if best_here >= 15:
            max_ge += 1
    assert max_ge == 0, f"Unexpected permutation hit: {max_ge}"
    print(f"Holdout check on No. 4166 ('{target_phrase}' at cell 199): K+A {hits_full}/{known_full}, direct-K {hits_k}/{known_k}; 0/9999 random within-rank keys reached 15 (max={best_perm}).")


def main() -> None:
    write_mode = "--write" in sys.argv[1:]
    img_meta = json.loads((HERE / "source-images.json").read_text(encoding="utf-8"))
    frame_hashes = {int(it["frame"]): it["sha256_original_tiff"] for it in img_meta["images"]}

    key = load_key(HERE / "key375.tsv")
    r1 = sum(1 for r, _ in key if r == 1)
    r2 = sum(1 for r, _ in key if r == 2)
    k_cnt = sum(1 for _, (_, g) in key.items() if g == "K")
    a_cnt = sum(1 for _, (_, g) in key.items() if g == "A")
    assert (len(key), r1, r2, k_cnt, a_cnt) == (472, 240, 232, 285, 187), (len(key), r1, r2, k_cnt, a_cnt)
    print(f"Loaded key375.tsv: {len(key)} entries ({r1} Rank 1 + {r2} Rank 2; {k_cnt} K + {a_cnt} A), strict within-rank bijectivity OK.")

    tot_full = tot_n = tot_k = 0
    streams: dict[str, str] = {}
    for doc_id in DOCS:
        _, stream = load_digits(doc_id, frame_hashes)
        streams[doc_id] = stream
        triples, tail = decode_triples(stream, key)
        n = len(triples)
        full = sum(1 for t in triples if t[3] != "??")
        dk = sum(1 for t in triples if t[4] == "K")
        assert (full, n, dk) == EXPECTED[doc_id], f"Mismatch on {doc_id}: got {(full, n, dk)}, expected {EXPECTED[doc_id]}"
        tot_full += full
        tot_n += n
        tot_k += dk

        rendered = format_decode_file(doc_id, triples, tail)
        dec_path = HERE / f"{doc_id}_decode.txt"
        if write_mode:
            dec_path.write_text(rendered, encoding="utf-8")
        else:
            existing = dec_path.read_text(encoding="utf-8")
            assert existing == rendered, f"Out-of-date {dec_path.name}; run with --write"
        print(f"  No. {doc_id:<4s}: {full:3d}/{n:<3d} ({100.0 * full / n:6.2f}%), direct K = {dk:3d}")

    assert (tot_full, tot_n, tot_k) == (980, 1249, 641)
    print(f"Total across 6 dispatches: {tot_full}/{tot_n} ({100.0 * tot_full / tot_n:.2f}%), direct K = {tot_k}.")
    verify_4166_holdout(streams["4166"])
    print("ALL CHECKS PASSED.")


if __name__ == "__main__":
    main()
