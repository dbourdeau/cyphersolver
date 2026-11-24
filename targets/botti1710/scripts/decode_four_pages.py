#!/usr/bin/env python3
"""Reproducible mechanical decoder for the four newly shown dotted pages of targets/botti1710:
R8666 T003, R8674 T001, R8677 T001, and R8710 T004.

Uses strictly the ciphertext-only letter values from key-and-read/key.tsv (including 17 -> r),
showing all 14 clerk-derived word/letter values and all open codes as middle dot (·),
matching the convention of the other 143 decoded pages of targets/botti1710.
"""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
FOUR_PAGES = [
    ("R8666", "T003"),
    ("R8674", "T001"),
    ("R8677", "T001"),
    ("R8710", "T004"),
]


def load_ciphertext_key(key_path: pathlib.Path) -> dict[str, str]:
    ct_key: dict[str, str] = {}
    for ln in key_path.read_text(encoding="utf-8").splitlines():
        if not ln.strip() or ln.startswith("#") or ln.startswith("code\t"):
            continue
        parts = ln.split("\t")
        code, val, src = parts[0], parts[1], parts[2]
        if src == "from ciphertext":
            ct_key[code] = val
        elif code == "17":
            ct_key[code] = "r"
    return ct_key


def decode_dots_row(raw_body: str, ct_key: dict[str, str]) -> tuple[str, tuple[int, int, int, int]]:
    groups: list[str] = []
    cur: list[str] = []
    depth = 0
    for ch in raw_body.strip():
        if ch in "[⟦":
            depth += 1
            cur.append(ch)
        elif ch in "]⟧":
            depth = max(0, depth - 1)
            cur.append(ch)
        elif ch.isspace() and depth == 0:
            if cur:
                groups.append("".join(cur))
                cur = []
        else:
            cur.append(ch)
    if cur:
        groups.append("".join(cur))

    out_groups: list[str] = []
    n_tok = n_shown = n_open = n_notcode = 0

    def repl_br(m: re.Match[str]) -> str:
        inner = m.group(1)
        if "|" in inner and inner.endswith("?"):
            left = inner[:-1].split("|")[0].strip()
            if re.match(r"^[0-9au.]+$", left):
                return left
        elif inner.endswith("?") and re.match(r"^[0-9au.]+$", inner[:-1]):
            return inner[:-1]
        return "§?§"

    for g in groups:
        if (g.startswith("[") and g.endswith("]")) or (g.startswith("⟦") and g.endswith("⟧")):
            inner = g[1:-1]
            left_parts = None
            if "|" in inner and inner.endswith("?"):
                left = inner[:-1].split("|")[0].strip()
                parts = [p for p in left.split(".") if p]
                if parts and all(re.match(r"^[0-9au]+$", p) for p in parts):
                    left_parts = parts
            elif inner.endswith("?") and re.match(r"^[0-9au.]+$", inner[:-1]):
                parts = [p for p in inner[:-1].split(".") if p]
                if parts:
                    left_parts = parts
            if left_parts is not None:
                res = []
                for p in left_parts:
                    n_tok += 1
                    if p in ct_key:
                        n_shown += 1
                        res.append(ct_key[p])
                    else:
                        n_open += 1
                        res.append("·")
                out_groups.append("".join(res))
                continue
            n_notcode += 1
            out_groups.append("?")
            continue

        g2 = re.sub(r"\[([^\]]*)\]", repl_br, g)
        g2 = re.sub(r"⟦([^⟧]*)⟧", repl_br, g2)
        sub_out = []
        for seg in g2.split("."):
            if not seg:
                continue
            if "§?§" in seg:
                for p in re.split(r"(§\?§)", seg):
                    if not p:
                        continue
                    if p == "§?§":
                        n_notcode += 1
                        sub_out.append("?")
                    elif re.match(r"^[0-9au]+$", p):
                        n_tok += 1
                        if p in ct_key:
                            n_shown += 1
                            sub_out.append(ct_key[p])
                        else:
                            n_open += 1
                            sub_out.append("·")
                    else:
                        n_notcode += 1
                        sub_out.append("?")
            elif re.match(r"^[0-9au]+$", seg):
                n_tok += 1
                if seg in ct_key:
                    n_shown += 1
                    sub_out.append(ct_key[seg])
                else:
                    n_open += 1
                    sub_out.append("·")
            else:
                n_notcode += 1
                sub_out.append("?")
        if sub_out:
            out_groups.append("".join(sub_out))

    return " ".join(out_groups), (n_tok, n_shown, n_open, n_notcode)


def decode_page(rec: str, pg: str, ct_key: dict[str, str]) -> tuple[list[str], tuple[int, int, int, int]]:
    path = ROOT / "transcription" / f"{rec}_{pg}_digits.txt"
    lines_out: list[str] = []
    t_tok = t_sh = t_op = t_nc = 0
    for ln in path.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^C\d+ ", ln):
            continue
        lbl, body = ln.split(" ", 1)
        dec, (a, b, c, d) = decode_dots_row(body, ct_key)
        t_tok += a
        t_sh += b
        t_op += c
        t_nc += d
        lines_out.append(f"- {rec}, {pg}, {lbl}: `{dec}`")
    return lines_out, (t_tok, t_sh, t_op, t_nc)


if __name__ == "__main__":
    key = load_ciphertext_key(ROOT / "key-and-read" / "key.tsv")
    for rec, pg in FOUR_PAGES:
        rows, (t_tok, t_sh, t_op, t_nc) = decode_page(rec, pg, key)
        print(f"### {rec} {pg} ({len(rows)} rows: {t_tok} tokens, {t_sh} shown, {t_op} open, {t_nc} not codes)")
        for r in rows:
            print(r)
        print()
