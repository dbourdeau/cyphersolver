#!/usr/bin/env python3
"""Mechanical, unedited decoder for Pierfilippo Pandolfini -> Lorenzo de' Medici
(ASFi MAP XXXVIII doc. 418 = Cat. 2574; ASFi MAP LIII doc. 13 = Cat. 2559).

Applies key_pandolfini1482.tsv directly to transcript_2574.txt and transcript_2559.txt
with ZERO language model, ZERO dictionary lookup, and ZERO manual edits, writing
decryption_2574.txt and decryption_2559.txt.

Notation in output lines:
  T = raw token stream
  K = strictly unedited mechanical key output:
      - monophonic signs emit their single letter;
      - polyphonic signs listed in key_pandolfini1482.tsv emit explicit choice pairs loaded directly from the TSV;
      - confirmed Grade-1 nulls (b_bar, h_bar, div, alp, x, wavy) and Grade-2 Mx are omitted (counted separately from letters);
      - provisional Rx, tf_lig, open nomenclators, and embedded Latin cover words emit [Rx], [tf_lig], [oo], [B], [invT], [H_cr], {LAT:...}, [?token].
"""
from __future__ import annotations

import csv
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
KEY_PATH = HERE / "key_pandolfini1482.tsv"

OPEN_NOM = {
    "B": "[B]",
    "invT": "[invT]",
    "H_cr": "[H_cr]",
    "M": "[?M]",
    "inf": "[?inf]",
}


def load_key(path: pathlib.Path) -> dict[str, tuple[str, str, str]]:
    """Return {token: (kind, value_m1, value_poly)} for single-token rows."""
    out = {}
    with path.open(encoding="utf-8") as fh:
        rows = csv.DictReader((r for r in fh if not r.startswith("#")), delimiter="\t")
        for row in rows:
            tok = row["token"].strip()
            if " " in tok:
                continue
            out[tok] = (row["kind"].strip(), row["value_m1"].strip(), row["value_poly"].strip())
    return out


def format_poly(val_poly: str) -> str:
    parts = [p.strip() for p in val_poly.split("/") if p.strip()]
    return "(" + "/".join(parts) + ")"


def decode_tokens(toks: list[str], key: dict[str, tuple[str, str, str]]) -> tuple[str, int, int, int, int]:
    """Return (decoded_str, letters_emitted, nulls_dropped, lat_mapped, total_count)."""
    out = []
    i = 0
    n = len(toks)
    letters = nulls = lat_mapped = 0
    while i < n:
        if i + 1 < n and toks[i] == "o" and toks[i + 1] == "o":
            out.append(" [oo] ")
            i += 2
            continue
        if i + 1 < n and toks[i] == "V" and toks[i + 1] == "t":
            out.append(" {LAT:ut} ")
            lat_mapped += 2
            i += 2
            continue
        if i + 1 < n and toks[i] == "V" and toks[i + 1] == "3":
            out.append(" {LAT:vz.} ")
            lat_mapped += 2
            i += 2
            continue

        t = toks[i]
        if t.startswith("LAT_"):
            out.append(f" {{{t}}} ")
            if t not in ("LAT_grandis", "LAT_grandes", "LAT_ocusa"):
                lat_mapped += 1
        elif t in OPEN_NOM:
            out.append(f" {OPEN_NOM[t]} ")
        elif t in key:
            kind, val_m1, val_poly = key[t]
            if t == "tf_lig":
                out.append(" [tf_lig] ")
            elif t == "Rx":
                out.append(" [Rx] ")
            elif kind == "polyphonic" and "/" in val_poly:
                out.append(format_poly(val_poly))
                letters += 1
            elif kind == "null" or val_poly == "NULL":
                nulls += 1  # null omitted
            elif t == "V":
                out.append(val_poly.split("/")[0].strip())
                letters += 1
            elif t == "H":
                out.append(val_poly)
                letters += 1
            elif t == "D":
                out.append(format_poly(val_poly))
                letters += 1
            elif val_m1 not in ("NULL", "?"):
                out.append(val_m1)
                letters += 1
            else:
                out.append(f" [{t}] ")
        else:
            out.append(f" [{t}] ")
        i += 1
    return re.sub(r" +", " ", "".join(out)).strip(), letters, nulls, lat_mapped, n


def process_file(in_name: str, out_name: str, title: str, key: dict[str, tuple[str, str, str]]) -> None:
    src = HERE / in_name
    dst = HERE / out_name
    lines_out = [
        f"# Unedited mechanical decryption of {title}",
        f"# Generated strictly by applying key_pandolfini1482.tsv to {in_name} via decrypt.py",
        "# ZERO language model, ZERO dictionary lookup, ZERO manual edits.",
        "# Notation: T = cipher tokens; K = unedited key output ((x/y) = audited polyphonic sign; [Rx]/[tf_lig] = provisional open signs; <<...>> = inline clear).",
        "",
    ]
    tot_letters = tot_nulls = tot_lat = tot_toks = 0
    for raw in src.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(L\d{2})\t(.*)$", raw)
        if not m:
            continue
        lbl, body = m.group(1), m.group(2)
        t_parts, k_parts = [], []
        for seg in re.split(r"(<<.*?>>)", body):
            seg = seg.strip()
            if not seg:
                continue
            if seg.startswith("<<") and seg.endswith(">>"):
                t_parts.append(seg)
                k_parts.append(f" {seg} ")
            else:
                toks = seg.split()
                t_parts.extend(toks)
                k_str, let_c, nul_c, lat_c, nt = decode_tokens(toks, key)
                tot_letters += let_c
                tot_nulls += nul_c
                tot_lat += lat_c
                tot_toks += nt
                k_parts.append(k_str)
        lines_out.append(f"{lbl} T  " + " ".join(t_parts))
        lines_out.append(f"{lbl} K  " + re.sub(r" +", " ", "".join(k_parts)).strip())
        lines_out.append("")
    tot_mapped = tot_letters + tot_nulls + tot_lat
    tot_open = tot_toks - tot_mapped
    lines_out.append(
        f"# Letters emitted: {tot_letters}/{tot_toks} ({100*tot_letters/max(1,tot_toks):.1f}%) | "
        f"cipher nulls omitted: {tot_nulls} | Latin null tokens: {tot_lat} | open/provisional tokens: {tot_open} | "
        f"total mapped (letters + nulls + Latin nulls): {tot_mapped}/{tot_toks} ({100*tot_mapped/max(1,tot_toks):.1f}%)"
    )
    dst.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
    print(
        f"Wrote {dst.name}: letters={tot_letters}/{tot_toks} ({100*tot_letters/max(1,tot_toks):.1f}%), "
        f"nulls={tot_nulls}, lat_nulls={tot_lat}, open={tot_open}, total_mapped={tot_mapped}/{tot_toks} ({100*tot_mapped/max(1,tot_toks):.1f}%)"
    )


def main() -> None:
    key = load_key(KEY_PATH)
    process_file(
        "transcript_2574.txt",
        "decryption_2574.txt",
        "ASFi MAP XXXVIII doc. 418 (Cat. 2574, Pierfilippo Pandolfini -> Lorenzo de' Medici, 27 Mar 1483)",
        key,
    )
    process_file(
        "transcript_2559.txt",
        "decryption_2559.txt",
        "ASFi MAP LIII doc. 13 (Cat. 2559, Pierfilippo Pandolfini -> Lorenzo de' Medici, Apr 1483)",
        key,
    )


if __name__ == "__main__":
    main()
