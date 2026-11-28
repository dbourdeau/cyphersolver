#!/usr/bin/env python3
"""Programmatic word-by-word sense and hole audit for ASF MdP 384, c. 78r (catalogue 2339).

Computes:
  1. Official Cyphersolver cipher-words-only read_share (matching research/reading_audit/v10_relabel.py
     and v2_score.py with clear_markup=⟨⟩).
  2. Orthographic cipher-word count (contractions like d'una counted as 1 word, clear spans excluded).
  3. Breakdown of every hole in reading_78r.md by category:
       - unresolved_code: bare code numbers [76], [47], [84], [65], [61], [18], [55], [87], [80], [22], [1547], [...]
       - contextual_hypothesis: [?word] proposals unattested in sibling witnesses
       - target_homophone: words whose sole departure from key_mdp384_witness.tsv is a recurring c. 78r
         homophone or ligature documented in key_78r_extensions.tsv (20=i, 55=p, 36=pe, 08=l, 00=o, 57=d, 30=s)
       - scribal_or_disputed: words with a scribal/enciphering/transcription slip or disputed L15-L17 reading
  4. Exact verdict under Cyphersolver's 95% cipher-word read bar (>= 0.95 -> "read", < 0.95 -> "read in part").
"""
from __future__ import annotations
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
READING_PATH = HERE / "reading_78r.md"
DECRYPTION_PATH = HERE / "decryption_78r.txt"


def extract_reading_section(text: str) -> str:
    m = re.search(r"^## Reading[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        raise ValueError("No ## Reading section found")
    return m.group(1)


def strip_clear(text: str) -> str:
    return re.sub(r"⟨[^⟩]*⟩", " ", text)


def v2_holes_equivalent(body: str) -> tuple[int, int, float]:
    """Replicate Cyphersolver research/reading_audit/v2_score.holes + v10_relabel word counting."""
    t = strip_clear(body)

    def rep(m: re.Match) -> str:
        inner = m.group(1)
        if re.fullmatch(r"[\s\d.?…*+-]*", inner) or len(inner.strip()) <= 2:
            return "[?]"
        if "?" in inner or inner == inner.lower():
            n = max(1, len(re.findall(r"[^\W\d_]+", inner)))
            return " ".join(["[?]"] * n)
        return m.group(0)

    t = re.sub(r"\[([^\]\n]*)\]", rep, t)
    # Collapse any word containing one or more [?] into a single [?] hole
    t = re.sub(r"(?:\w*\[\?\]\w*)+", "[?]", t)
    holes = t.count("[?]")
    words = len(re.findall(r"[^\W\d_]+", t.replace("[?]", " ")))
    share = round(1 - holes / (words + holes), 3) if (words + holes) else 0.0
    return words, holes, share


def audit_orthographic(body: str) -> dict:
    cipher_only = strip_clear(body)
    raw_tokens = cipher_only.split()
    sure = []
    holes = []
    seen = {}

    for tok in raw_tokens:
        clean = tok.strip(".,;:!()\"'«»“”")
        if not clean:
            continue
        if "[" not in clean and "]" not in clean:
            sure.append(clean)
            continue

        seen[clean] = seen.get(clean, 0) + 1
        occ = seen[clean]

        # Classify hole
        if re.fullmatch(r"\[(?:\d+|\.\.\.)\]", clean):
            cat = "unresolved_code"
        elif clean.startswith("[?"):
            cat = "contextual_hypothesis"
        else:
            # Words whose ONLY departure from key_mdp384_witness.tsv is a recurring c. 78r-only
            # homophone or ligature in key_78r_extensions.tsv (20=i, 55=p, 36=pe, 08=l, 00=o, 57=d, 30=s).
            is_hom = False
            if clean == "[di]":
                is_hom = (occ == 2)  # occ 1: L01 71=NULL; occ 2: L04 20=i; occ 3: L11 52=g; occ 4: L25 01 70=ri; occ 5: L26 del
            elif clean == "[per]":
                is_hom = (occ in (1, 2))  # occ 1: L17 36=pe; occ 2: L24 36=pe; occ 3: L26 a+36=pe
            elif clean == "[protonotario]":
                is_hom = (occ == 1)  # occ 1: L09 20=i; occ 2: L18 47=f & 6=e
            elif clean in ("[procinto]", "[ringratia]", "[collegarsi]", "[in]",
                           "n'[andrà]", "[saprà]", "[oferischi]", "[sopratutto]", "[egli]",
                           "[ragionamento]", "[estensione]", "[il]"):
                is_hom = True
            cat = "target_homophone" if is_hom else "scribal_or_disputed"
        holes.append((clean, cat))

    counts_by_cat = {}
    for _, cat in holes:
        counts_by_cat[cat] = counts_by_cat.get(cat, 0) + 1

    total = len(sure) + len(holes)
    strict_share = len(sure) / total if total else 0.0
    with_hom = (len(sure) + counts_by_cat.get("target_homophone", 0)) / total if total else 0.0

    return {
        "total_ortho": total,
        "sure_ortho": len(sure),
        "holes_ortho": len(holes),
        "strict_ortho_share": strict_share,
        "with_hom_ortho_share": with_hom,
        "counts_by_cat": counts_by_cat,
        "hole_list": holes,
    }


def main():
    text = READING_PATH.read_text(encoding="utf-8")
    body = extract_reading_section(text)
    v2_words, v2_holes, v2_share = v2_holes_equivalent(body)
    v2_total = v2_words + v2_holes

    ortho = audit_orthographic(body)
    n_hom = ortho["counts_by_cat"].get("target_homophone", 0)
    v2_with_hom_share = (v2_words + n_hom) / v2_total if v2_total else 0.0

    # Parse witness token coverage from decryption_78r.txt
    dec_text = DECRYPTION_PATH.read_text(encoding="utf-8")
    m_cov = re.search(r"Witness-key token coverage:\s*(\d+)/(\d+)\s*\(([\d.]+)%\)", dec_text)
    tok_cov = f"{m_cov.group(1)}/{m_cov.group(2)} ({m_cov.group(3)}%)" if m_cov else "n/a"

    print("=== Word-Sense Audit: ASF MdP 384, c. 78r (Catalogue 2339) ===")
    print(f"Witness-key cipher token coverage (decryption_78r.txt): {tok_cov}")
    print()
    print("1. Official Cyphersolver word-token count (v2_score / v10_relabel, clear_markup=⟨⟩):")
    print(f"   Sure cipher words : {v2_words}")
    print(f"   Holes             : {v2_holes}")
    print(f"   Total cipher words: {v2_total}")
    print(f"   Strict read_share : {v2_share:.3f} ({100*v2_words/v2_total:.1f}%)")
    print(f"   Verdict (>=0.95)  : {'read (complete)' if v2_share >= 0.95 else 'read in part (partial)'}")
    print()
    print("2. Orthographic cipher-word count (apostrophe contractions = 1 word, clear excluded):")
    print(f"   Sure cipher words : {ortho['sure_ortho']}")
    print(f"   Holes             : {ortho['holes_ortho']}")
    print(f"   Total cipher words: {ortho['total_ortho']}")
    print(f"   Strict share      : {ortho['strict_ortho_share']:.3f} ({100*ortho['strict_ortho_share']:.1f}%)")
    print()
    print("3. Hole breakdown by category (orthographic words):")
    for cat in ("unresolved_code", "contextual_hypothesis", "target_homophone", "scribal_or_disputed"):
        print(f"   - {cat:22s}: {ortho['counts_by_cat'].get(cat, 0)}")
    print()
    print("4. Sensitivity (if recurring c. 78r-only homophones in key_78r_extensions.tsv were counted):")
    print(f"   v2_score token share  : {v2_with_hom_share:.3f} ({v2_words + n_hom}/{v2_total} = {100*v2_with_hom_share:.1f}%)")
    print(f"   Orthographic share    : {ortho['with_hom_ortho_share']:.3f} ({ortho['sure_ortho'] + n_hom}/{ortho['total_ortho']} = {100*ortho['with_hom_ortho_share']:.1f}%)")
    print(f"   Still under 95% bar?  : {'YES -> read in part' if v2_with_hom_share < 0.95 else 'NO'}")
    print()
    print("Detailed hole list:")
    for idx, (tok, cat) in enumerate(ortho["hole_list"], 1):
        print(f"  {idx:2d}. {tok:22s} [{cat}]")


if __name__ == "__main__":
    main()
