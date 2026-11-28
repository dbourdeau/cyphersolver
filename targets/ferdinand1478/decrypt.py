#!/usr/bin/env python3
"""Mechanical, unedited decoder for Zaragoza AHPZ C_CRAR/000001/0024 (catalogue 2854,
King Ferdinand II of Aragon -> King John II of Aragon, Seville, 9 June 1478).

Applies key_ferdinand1478.tsv strictly to transcript_2854.txt with ZERO language model,
ZERO dictionary lookup, ZERO per-word overrides, and ZERO scribal-slip corrections.
Writes decryption_2854.txt.
"""
from __future__ import annotations

import csv
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
KEY_PATH = HERE / "key_ferdinand1478.tsv"
TRANS_PATH = HERE / "transcript_2854.txt"
OUT_PATH = HERE / "decryption_2854.txt"


def load_key(path: pathlib.Path) -> dict[str, str]:
    km: dict[str, str] = {}
    with path.open(encoding="utf-8") as fh:
        rows = csv.DictReader((r for r in fh if not r.startswith("#")), delimiter="\t")
        for row in rows:
            tok = row["token"].strip()
            val = row["value"].strip()
            km[tok] = "" if val in ("?", "NULL") else val
    return km


def main() -> None:
    key = load_key(KEY_PATH)
    out = [
        "# Unedited mechanical decryption of Zaragoza AHPZ C_CRAR/000001/0024 (catalogue 2854).",
        "# Generated strictly by applying key_ferdinand1478.tsv to transcript_2854.txt via decrypt.py",
        "# with ZERO dictionary lookup, ZERO language model, and ZERO scribal-slip corrections.",
        "# Notation: C = canonical cipher line; K = unedited continuous mechanical plaintext ([oo] unmapped).",
        "",
    ]
    tot_toks = mapped = 0
    for raw in TRANS_PATH.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        lbl, folio, body = s.split("\t", 2)
        toks = body.split()
        pieces = []
        for t in toks:
            tot_toks += 1
            v = key.get(t, "")
            if v:
                mapped += 1
                pieces.append(v)
            else:
                pieces.append(f"[{t}]")
        out.append(f"{lbl} ({folio}) C  " + " ".join(toks))
        out.append(f"{lbl} ({folio}) K  " + "".join(pieces))
        out.append("")
    out.append(f"# Mechanical token coverage: {mapped}/{tot_toks} ({100*mapped/max(1,tot_toks):.2f}%)")
    OUT_PATH.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH.name}: {mapped}/{tot_toks} tokens ({100*mapped/max(1,tot_toks):.2f}%)")


if __name__ == "__main__":
    main()
