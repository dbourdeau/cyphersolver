#!/usr/bin/env python3
"""Reproducible mechanical decoder for targets/francia346b (DECODE R5634, R5638, R5639).

Uses strictly key.tsv (frequency-weighted dynamic programming over the 59 1-digit and 2-digit
codes in key.tsv; zero external language model and zero manual post-editing) to produce the
unedited row-by-row decode of all six transcription pages.
"""
from __future__ import annotations

import math
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
RECORDS = [
    ("R5634", [("f. 190r", "R5634_f190r_digits.txt"), ("f. 190v", "R5634_f190v_digits.txt")]),
    ("R5638", [("f. 218r", "R5638_f218r_digits.txt"), ("f. 218v", "R5638_f218v_digits.txt")]),
    ("R5639", [("f. 220r", "R5639_f220r_digits.txt"), ("f. 220v", "R5639_f220v_digits.txt")]),
]


def load_key(path: pathlib.Path) -> tuple[dict[str, tuple[str, str, int, str]], int]:
    kmap: dict[str, tuple[str, str, int, str]] = {}
    tot = 0
    for ln in path.read_text(encoding="utf-8").splitlines():
        if not ln.strip() or ln.startswith("#") or ln.startswith("code\t"):
            continue
        code, kind, val, _src, cnt, grade, _note = ln.split("\t")
        c = int(cnt)
        tot += c
        kmap[code] = (kind, val, c, grade)
    return kmap, tot


def row_to_segments(raw_body: str) -> list[str]:
    parts = re.split(r"\[(?:unresolved[^\]]*|gap:[^\]]*)\]", raw_body.strip())
    segs: list[str] = []
    for p in parts:
        p = re.sub(r"\[([0-9]+)\|[^\]]*\?\]", r"\1", p)
        p = re.sub(r"\[([0-9]+)\?\]", r"\1", p)
        p = re.sub(r"[^0-9]", "", p)
        if p:
            segs.append(p)
    return segs


def dp_decode_segment(
    seg: str,
    kmap: dict[str, tuple[str, str, int, str]],
    tot_cnt: int,
) -> tuple[str, int, int]:
    n = len(seg)
    dp: list[tuple[float, int, str | None]] = [(-1e18, -1, None)] * (n + 1)
    dp[0] = (0.0, -1, None)
    for i in range(n):
        if dp[i][0] < -1e17:
            continue
        if i + 2 <= n and seg[i : i + 2] in kmap:
            code = seg[i : i + 2]
            sc = dp[i][0] + math.log(kmap[code][2] / tot_cnt)
            if sc > dp[i + 2][0]:
                dp[i + 2] = (sc, i, code)
        if seg[i : i + 1] in kmap:
            code = seg[i : i + 1]
            sc = dp[i][0] + math.log(kmap[code][2] / tot_cnt)
            if sc > dp[i + 1][0]:
                dp[i + 1] = (sc, i, code)
        else:
            sc = dp[i][0] - 12.0
            if sc > dp[i + 1][0]:
                dp[i + 1] = (sc, i, "?")
    codes: list[str] = []
    cur = n
    while cur > 0:
        _, prev, code = dp[cur]
        assert code is not None
        codes.append(code)
        cur = prev
    codes.reverse()
    letters: list[str] = []
    n_null = 0
    for c in codes:
        if c == "?":
            letters.append("?")
        else:
            kind, val, _, _ = kmap[c]
            if kind == "null":
                n_null += 1
            else:
                letters.append(val)
    return "".join(letters), len(codes), n_null


def decode_record(
    rec_id: str,
    pages: list[tuple[str, str]],
    kmap: dict[str, tuple[str, str, int, str]],
    tot_cnt: int,
) -> dict[str, object]:
    page_blocks = []
    tot_digits = tot_codes = tot_nulls = tot_letters = tot_gaps = 0
    for folio, fname in pages:
        rows = []
        raw_text = (ROOT / "transcription" / fname).read_text(encoding="utf-8")
        for ln in raw_text.splitlines():
            if not re.match(r"^C\d+ ", ln):
                continue
            lbl, body = ln.split(" ", 1)
            gaps = len(re.findall(r"\[(?:unresolved[^\]]*|gap:[^\]]*)\]", body))
            tot_gaps += gaps
            segs = row_to_segments(body)
            dec_parts = []
            for s in segs:
                tot_digits += len(s)
                dstr, nc, nn = dp_decode_segment(s, kmap, tot_cnt)
                tot_codes += nc
                tot_nulls += nn
                tot_letters += len(dstr)
                dec_parts.append(dstr)
            rows.append((lbl, " [...] ".join(dec_parts)))
        page_blocks.append((folio, fname, rows))
    return {
        "record": rec_id,
        "pages": page_blocks,
        "digits": tot_digits,
        "codes": tot_codes,
        "nulls": tot_nulls,
        "letters": tot_letters,
        "gaps": tot_gaps,
    }


if __name__ == "__main__":
    kmap, tot_cnt = load_key(ROOT / "key.tsv")
    for rec_id, pages in RECORDS:
        res = decode_record(rec_id, pages, kmap, tot_cnt)
        print(
            f"=== {rec_id}: {res['digits']} digits -> {res['codes']} code units "
            f"({res['letters']} letters, {res['nulls']} nulls, {res['gaps']} gaps) ==="
        )
        for folio, _fn, rows in res["pages"]:
            print(f"  [{folio}] {len(rows)} rows")
            for lbl, dec in rows[:3]:
                print(f"    - {rec_id}, {folio}, {lbl}: `{dec}`")
