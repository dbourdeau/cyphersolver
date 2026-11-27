#!/usr/bin/env python3
"""Programmatic cipher-words-only extent audit for Modena Estense Campori,
Gonzaga Federico II, cc. 13r-13v (catalogue 2162).

Mirrors Cyphersolver's research/reading_audit/v10_relabel.py (clear_markup=⟨⟩)
and categorises every hole in reading_13r_13v.md against unedited decryption_13r_13v.txt.
"""
from __future__ import annotations

import collections
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
READING = HERE / "reading_13r_13v.md"

OPEN_NOM_CODES = {"{L2?}", "{L9?}", "{L30?}", "{L36?}", "[46]", "[82]"}
OPEN_NUM_CODES = {"[23]", "[24]", "[27]", "[28]", "[29]", "[31]", "[53]"}
CONTEXTUAL_HYP = {"[?Fasgnino]", "[?destimato]", "[?vero]", "[?è]", "[?natura]", "[?si]", "[?resa]", "[?raccomandatione]", "[?parte]"}


def extract_reading_body(text: str) -> str:
    m = re.search(r"^## Reading[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M | re.I)
    body = m.group(1) if m else text
    return "\n".join(l for l in body.splitlines() if not l.lstrip().startswith("#"))


def strip_clear(body: str) -> str:
    return re.sub(r"⟨[^⟩]*⟩", " ", body)


def classify_hole(tok: str) -> str:
    if tok in OPEN_NOM_CODES:
        return "open_nomenclator"
    if tok in OPEN_NUM_CODES:
        return "open_numeric_or_null"
    if tok.startswith("[?") or tok in CONTEXTUAL_HYP:
        return "contextual_or_uncertain"
    return "scribal_slip_or_allograph"


def main() -> None:
    body = extract_reading_body(READING.read_text(encoding="utf-8"))
    cipher_only = strip_clear(body)

    # Match Cyphersolver v2_score/v10_relabel: every [...] and {L..?} becomes [?]
    hole_rx = re.compile(r"\[[^\]]+\]|\{L\d+\?\}")
    holes = hole_rx.findall(cipher_only)
    b = hole_rx.sub(" [?] ", cipher_only)

    # v10_relabel word token regex: [^\W\d_]+ (apostrophe contractions count as 2 tokens)
    n_holes = b.count("[?]")
    n_sure_v10 = len(re.findall(r"[^\W\d_]+", b.replace("[?]", " ")))
    tot_v10 = n_sure_v10 + n_holes
    share_v10 = n_sure_v10 / tot_v10

    # Orthographic cipher words (apostrophe contractions = 1 word)
    n_sure_ortho = len(re.findall(r"[^\W\d_]+(?:'[^\W\d_]+)?", b.replace("[?]", " ")))
    tot_ortho = n_sure_ortho + n_holes
    share_ortho = n_sure_ortho / tot_ortho

    cats = collections.Counter(classify_hole(h) for h in holes)

    print("=== Word-Sense Audit: Modena Estense Campori, Gonzaga Federico II, cc. 13r-13v (Cat. 2162) ===")
    print("\n1. Official Cyphersolver word-token count (v2_score / v10_relabel, clear_markup=⟨⟩):")
    print(f"   Sure cipher words : {n_sure_v10}")
    print(f"   Holes             : {n_holes}")
    print(f"   Total cipher words: {tot_v10}")
    print(f"   Strict read_share : {share_v10:.3f} ({100*share_v10:.1f}%)")
    print(f"   Verdict (>=0.95)  : {'read' if share_v10 >= 0.95 else 'read in part (partial)'}")

    print("\n2. Orthographic cipher-word count (apostrophe contractions = 1 word, clear excluded):")
    print(f"   Sure cipher words : {n_sure_ortho}")
    print(f"   Holes             : {n_holes}")
    print(f"   Total cipher words: {tot_ortho}")
    print(f"   Strict share      : {share_ortho:.3f} ({100*share_ortho:.1f}%)")

    print("\n3. Hole breakdown by category:")
    for k in ("open_nomenclator", "open_numeric_or_null", "contextual_or_uncertain", "scribal_slip_or_allograph"):
        print(f"   - {k:26s}: {cats[k]}")

    # Sensitivity: even if all scribal slips were granted, open codes + uncertain words alone keep share < 0.95
    open_only = cats["open_nomenclator"] + cats["open_numeric_or_null"]
    print(f"\n4. Sensitivity (open codes/nulls alone = {open_only}/{tot_v10} = {100*open_only/tot_v10:.1f}% holes):")
    print(f"   Upper bound if only open codes counted: {(tot_v10 - open_only)/tot_v10:.3f} ({100*(tot_v10 - open_only)/tot_v10:.1f}%)")
    print(f"   Still under 95% bar?                  : {'YES -> read in part' if (tot_v10 - open_only)/tot_v10 < 0.95 else 'NO'}")

    print("\nDetailed hole list:")
    for i, h in enumerate(holes, 1):
        print(f"  {i:2d}. {h:22s} [{classify_hole(h)}]")


if __name__ == "__main__":
    main()
