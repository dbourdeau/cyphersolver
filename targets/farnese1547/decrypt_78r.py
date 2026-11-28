#!/usr/bin/env python3
"""Mechanical, unedited decoder for ASF Mediceo del Principato 384, c. 78r (catalogue 2339).

Applies strictly witness-attested codes from key_mdp384_witness.tsv (derived exclusively from
c. 76r/79r, c. 77r, and c. 147r/148r — zero c. 78r-only entries) to transcription_78r.txt
and writes decryption_78r.txt.
"""
from __future__ import annotations
import csv
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
KEY_PATH = HERE / "key_mdp384_witness.tsv"
TRANS_PATH = HERE / "transcription_78r.txt"
OUT_PATH = HERE / "decryption_78r.txt"

# Witness-attested two-digit nomenclator/special codes whose first digit is 6, 8, or 9
# when marked with an overbar, circumflex hat, or single dot on the lead digit.
BARRED_2D = {"22̄", "61̄", "68̄", "53̄", "55̄", "58̄", "70̄", "71̄", "85̄"}


def load_witness_key(path: pathlib.Path) -> dict[str, str]:
    key = {}
    with path.open(encoding="utf-8") as fh:
        rows = csv.DictReader((r for r in fh if not r.startswith("#")), delimiter="\t")
        for row in rows:
            code = row["code"].strip()
            val = row["value"].split(" / ")[0].strip()
            key[code] = val
    return key


def tokenize_run(run: str) -> list[tuple[str, str]]:
    """Parse a continuous cipher run from transcription_78r.txt into (base, formatted) tokens.

    Prefix rule (witness-established on c. 76r, c. 77r, c. 147r):
      - Unmarked 6, 8, 9 are 1-digit vowels (e, o, a).
      - A 6, 8, or 9 marked with an overbar/hat/single-lead-dot (not followed by a dotted digit,
        as in L21 8^0^ delimiter) or followed by a barred/hatted digit forms a 2-digit code.
      - Digits in {0, 1, 2, 3, 4, 5, 7} initiate 2-digit codes.
    """
    # Parse into (digit, mark) pairs where mark in {'', '^', '̄', '̂'}
    units = []
    i = 0
    s = re.sub(r"\s+", "", run)
    while i < len(s):
        ch = s[i]
        if ch.isdigit():
            mark = ""
            if i + 1 < len(s) and s[i + 1] in ("^", "\u0304", "\u0302"):
                mark = s[i + 1]
                i += 1
            units.append((ch, mark))
        i += 1

    toks = []
    i = 0
    n = len(units)
    while i < n:
        d1, m1 = units[i]
        if d1 in "689":
            # Two-digit override for barred/hatted/lead-dotted nomenclators (6^7, 8^9, 9^3, 6̄8̄, 8̄5̄, 6̄1̄, 84̂, 8^7, 9^2)
            # Exclude L21 8^ followed by dotted 0^ (where 8^ is a 1-digit dotted delimiter before 0^7 11)
            next_is_hat = (i + 1 < n and units[i + 1][1] == "\u0302")
            lead_marked_2d = (
                m1 in ("\u0304", "\u0302")
                or (m1 == "^" and i + 1 < n and units[i + 1][1] == "")
            )
            if i + 1 < n and (next_is_hat or lead_marked_2d):
                d2, m2 = units[i + 1]
                fmt = f"{d1}{m1}{d2}{m2}"
                # Collapse double-barred 6̄8̄ -> 68̄ for key lookup
                if m1 == "\u0304" and m2 == "\u0304":
                    fmt = f"{d1}{d2}\u0304"
                toks.append((d1 + d2, fmt))
                i += 2
                continue
            toks.append((d1, f"{d1}{m1}"))
            i += 1
        elif i + 1 < n:
            d2, m2 = units[i + 1]
            fmt = f"{d1}{m1}{d2}{m2}"
            if m1 == "\u0304" and m2 == "\u0304":
                fmt = f"{d1}{d2}\u0304"
            toks.append((d1 + d2, fmt))
            i += 2
        else:
            toks.append((d1, f"{d1}{m1}"))
            i += 1
    return toks


def lookup(base: str, fmt: str, key: dict[str, str]) -> str | None:
    if fmt in key:
        return key[fmt]
    # Handle trailing-dot drift on 1x/2x function words (e.g. 13^ -> 1^3, 18^ -> 1^8, 1^0^ -> 1^0)
    if "^" in fmt and len(base) == 2:
        norm_dot = f"{base[0]}^{base[1]}"
        if norm_dot in key:
            return key[norm_dot]
    # Do not fall back from marked nomenclators/hapax codes to plain letter values
    if "\u0304" in fmt or "\u0302" in fmt:
        return None
    if len(base) == 2 and base[0] in "689":
        return None
    if fmt in ("1^9", "2^2", "4^3", "7^6^", "7^6", "4^7"):
        return None
    # Unmarked or routine i-dotted 2-digit letters (e.g. 0^3 -> 03, 2^1 -> 21)
    if base in key:
        return key[base]
    return None


def main():
    key = load_witness_key(KEY_PATH)
    lines_out = [
        "# Unedited mechanical decryption of ASF Mediceo del Principato 384, c. 78r (catalogue 2339).",
        "# Generated strictly by applying key_mdp384_witness.tsv (witness-attested on c. 76r/79r, c. 77r, c. 147r/148r ONLY)",
        "# to transcription_78r.txt via decrypt_78r.py, with ZERO edits, ZERO target-only homophones, and ZERO contextual fills.",
        "# Notation: T = segmented cipher tokens; K = unedited witness-key output ([code] = no witness value; <<...>> = inline clear Italian).",
        "",
    ]
    total = mapped = 0
    for raw in TRANS_PATH.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(L\d{2})\s+(.*)$", raw)
        if not m:
            continue
        lbl, body = m.group(1), m.group(2)
        parts = re.split(r"(<<.*?>>)", body)
        t_parts, k_parts = [], []
        for p in parts:
            if not p.strip():
                continue
            if p.startswith("<<") and p.endswith(">>"):
                t_parts.append(p)
                k_parts.append(f" {p} ")
            else:
                for base, fmt in tokenize_run(p):
                    total += 1
                    t_parts.append(fmt)
                    val = lookup(base, fmt, key)
                    if val is not None:
                        mapped += 1
                        if val == "NULL":
                            k_parts.append(f" [{fmt}:NULL] ")
                        elif len(val) > 1 or val[0].isupper():
                            k_parts.append(f" {val} ")
                        else:
                            k_parts.append(val)
                    else:
                        k_parts.append(f"[{fmt}]")
        lines_out.append(f"{lbl} T  " + " ".join(t_parts))
        lines_out.append(f"{lbl} K  " + re.sub(r" +", " ", "".join(k_parts)).strip())
        lines_out.append("")

    lines_out.append(f"# Witness-key token coverage: {mapped}/{total} ({100*mapped/total:.1f}%)")
    OUT_PATH.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({mapped}/{total} tokens = {100*mapped/total:.1f}% mapped by witness key alone)")


if __name__ == "__main__":
    main()
