#!/usr/bin/env python3
"""Programmatic cipher-words-only extent audit for Cat. #2077 (reading_2077.md) and
out-of-sample Cat. #2518 (reading_2518.md) — Terranova -> Sfondrati, Aug-Oct 1583.

Mirrors Cyphersolver's research/reading_audit/v10_relabel.py (clear_markup=⟨⟩) and
categorises every explicit hole across both readings.
"""
from __future__ import annotations

import collections
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent


def extract_reading_body(text: str) -> str:
    m = re.search(r"^## Reading[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M | re.I)
    body = m.group(1) if m else text
    return "\n".join(l for l in body.splitlines() if not l.lstrip().startswith("#"))


def audit_file(path: pathlib.Path, label: str) -> tuple[int, int, collections.Counter]:
    body = extract_reading_body(path.read_text(encoding="utf-8"))
    cipher_only = re.sub(r"⟨[^⟩]*⟩", " ", body)
    tok_rx = re.compile(r"\{[^}]+\}|\[[^\]]+\]|[^\s.,;:!—]+")
    words_raw = tok_rx.findall(cipher_only)
    holes = []
    sure = 0
    for w in words_raw:
        if "{" in w and "?" in w:
            if "stain" in w:
                cat = "water_stain_lacuna"
            elif "~" in w:
                cat = "literal_numeral_overbar"
            else:
                cat = "open_nomenclator"
            holes.append((w, cat))
        elif "[" in w and "]" in w:
            cat = "uncertain_local_span" if "[?" in w else "homophone_or_scribal_repair"
            holes.append((w, cat))
        elif re.search(r"[^\W\d_]", w):
            sure += 1

    tot = sure + len(holes)
    share = sure / max(1, tot)
    cats = collections.Counter(c for _, c in holes)
    print(f"=== {label} ({path.name}, clear_markup=⟨⟩) ===")
    print(f"  Sure cipher words (verbatim key) : {sure}")
    print(f"  Explicit holes                   : {len(holes)}")
    for k in ("open_nomenclator", "literal_numeral_overbar", "water_stain_lacuna", "uncertain_local_span", "homophone_or_scribal_repair"):
        if cats[k]:
            print(f"    - {k:28s}: {cats[k]}")
    print(f"  Total cipher words               : {tot}")
    print(f"  Strict v10 read_share            : {share:.3f} ({100*share:.1f}%) -> {'read' if share >= 0.95 else 'read in part'}")
    print()
    return sure, len(holes), cats


def main() -> None:
    s1, h1, _ = audit_file(HERE / "reading_2077.md", "Cat. #2077 (BYU Vault MSS 771, Aug-Sep 1583)")
    s2, h2, _ = audit_file(HERE / "reading_2518.md", "Cat. #2518 (BYU Vault MSS 518, 5 Oct 1583)")
    tot = s1 + h1 + s2 + h2
    print(f"=== COMBINED (#2077 + #2518): {s1+s2}/{tot} = {(s1+s2)/max(1,tot):.3f} ({h1+h2} holes) ===")


if __name__ == "__main__":
    main()
