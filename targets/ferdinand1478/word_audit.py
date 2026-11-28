#!/usr/bin/env python3
"""Programmatic cipher-words-only extent audit for Zaragoza AHPZ C_CRAR/000001/0024
(catalogue 2854, King Ferdinand II of Aragon -> King John II of Aragon, Seville, 9 June 1478).

Mirrors Cyphersolver's research/reading_audit/v10_relabel.py (clear_markup=⟨⟩) and
categorises every explicit hole in reading_2854.md.
"""
from __future__ import annotations

import collections
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
READING = HERE / "reading_2854.md"


def extract_reading_body(text: str) -> str:
    m = re.search(r"^## Reading[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M | re.I)
    body = m.group(1) if m else text
    return "\n".join(l for l in body.splitlines() if not l.lstrip().startswith("#"))


def main() -> None:
    body = extract_reading_body(READING.read_text(encoding="utf-8"))
    cipher_only = re.sub(r"⟨[^⟩]*⟩", " ", body)

    tok_rx = re.compile(r"[^\s.,;:!—]+")
    words_raw = tok_rx.findall(cipher_only)
    holes = []
    sure = 0
    for w in words_raw:
        if "{" in w and "?" in w:
            holes.append((w, "open_nomenclator"))
        elif "[" in w and "]" in w:
            cat = "uncertain_corrupt_span" if "[?" in w else "scribal_slip_or_polyvalence"
            holes.append((w, cat))
        elif re.search(r"[^\W\d_]", w):
            sure += 1

    tot = sure + len(holes)
    share = sure / max(1, tot)
    cats = collections.Counter(c for _, c in holes)

    print("=== Word-Sense Audit: AHPZ C_CRAR/000001/0024 (Cat. 2854, clear_markup=⟨⟩) ===")
    print(f"  Sure cipher words (verbatim key)    : {sure}")
    print(f"  Explicit holes                      : {len(holes)}")
    print(f"    - open_nomenclator ({{oo?}})        : {cats['open_nomenclator']}")
    print(f"    - uncertain_corrupt_span ([?...]) : {cats['uncertain_corrupt_span']}")
    print(f"    - slip_polyvalence_or_singleton   : {cats['scribal_slip_or_polyvalence']}")
    print(f"  Total cipher words                  : {tot}")
    print(f"  Strict v10 read_share (19 Nov rule) : {share:.3f} ({100*share:.1f}%) -> {'read' if share >= 0.95 else 'read in part (conservative)'}")


if __name__ == "__main__":
    main()
