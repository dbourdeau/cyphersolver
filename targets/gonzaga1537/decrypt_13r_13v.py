#!/usr/bin/env python3
"""Mechanical, unedited decoder for Modena Estense Campori, Gonzaga Federico II, cc. 13r-13v (catalogue 2162).

Applies recovered entries from key_gonzaga1537.tsv directly to transcription_13r_13v.txt
with ZERO dictionary lookup, ZERO language model, ZERO stroke edits, and ZERO contextual fills.

Parsing rules (purely structural, key-table only):
  1. Every character of a cipher word must be covered by a recovered 1- or 2-char entry in
     key_gonzaga1537.tsv (characters i, p, c, d, t have no standalone entries).
  2. Doubled-letter digraphs zo=tt and zz=zz are kept atomic (not split into z+o / z+z).
  3. ib decodes as e word-finally and nn medially.
  4. When a word admits a unique full-coverage parse, that string is emitted verbatim; when
     more than one full-coverage parse exists (an i-digraph boundary ambiguity such as r+i4 vs ri+4
     or r+ig vs ri+g), all valid parses are emitted separated by '/'; when zero full-coverage
     parse exists (scribal slip or unmapped stroke), longest-match fallback emits [c] for each
     unmapped character.
"""
from __future__ import annotations

import csv
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
KEY_PATH = HERE / "key_gonzaga1537.tsv"
TRANS_PATH = HERE / "transcription_13r_13v.txt"
OUT_PATH = HERE / "decryption_13r_13v.txt"


def load_key(path: pathlib.Path) -> tuple[dict[str, str], dict[str, str]]:
    """Return (sign_map, nomenclator_map) from recovered rows of key_gonzaga1537.tsv."""
    signs: dict[str, str] = {}
    nom: dict[str, str] = {}
    with path.open(encoding="utf-8") as fh:
        rows = csv.DictReader((r for r in fh if not r.startswith("#")), delimiter="\t")
        for row in rows:
            if row["status"].strip() != "recovered":
                continue
            tok = row["token"].strip()
            val = row["value"].split(" / ")[0].strip()
            if row["kind"].strip() == "nomenclator":
                nom[tok] = val
            else:
                signs[tok] = val
    return signs, nom


def full_coverage_parses(word: str, signs: dict[str, str]) -> list[list[str]]:
    """All ways to tile word with recovered signs, keeping atomic zo/zz intact."""
    n = len(word)
    res: list[list[str]] = []

    def dfs(i: int, acc: list[str]) -> None:
        if i == n:
            res.append(acc)
            return
        # Keep zo and zz atomic when present
        if i + 2 <= n and word[i : i + 2] in ("zo", "zz") and word[i : i + 2] in signs:
            dfs(i + 2, acc + [word[i : i + 2]])
            return
        if i + 2 <= n and word[i : i + 2] in signs:
            dfs(i + 2, acc + [word[i : i + 2]])
        if word[i] in signs:
            dfs(i + 1, acc + [word[i]])

    dfs(0, [])
    return res


def render_parse(toks: list[str], signs: dict[str, str]) -> str:
    out = []
    for idx, t in enumerate(toks):
        if t == "ib":
            out.append("nn" if idx < len(toks) - 1 else "e")
        else:
            out.append(signs[t])
    return "".join(out)


def fallback_decode(word: str, signs: dict[str, str]) -> str:
    """Longest-match left-to-right fallback marking any uncovered char as [c]."""
    out = []
    i, n = 0, len(word)
    while i < n:
        if i + 2 <= n and word[i : i + 2] in signs:
            dg = word[i : i + 2]
            out.append("nn" if (dg == "ib" and i + 2 < n) else signs[dg])
            i += 2
        elif word[i] in signs:
            out.append(signs[word[i]])
            i += 1
        else:
            out.append(f"[{word[i]}]")
            i += 1
    return "".join(out)


def decode_token(tok: str, signs: dict[str, str], nom: dict[str, str]) -> tuple[str, str]:
    """Return (decoded_str, category) where category in {'nom', 'open', 'uniq', 'ambig', 'slip'}."""
    core = tok.strip(".,:;/")
    if not core:
        return tok, "punct"
    if core == "30":
        return nom.get("30", "[30]"), "nom"
    if core == "30&":
        return nom.get("30", "[30]") + "'" + signs.get("&", "[&]"), "nom"
    if core == "&4.27":
        return signs["&"] + signs["4"] + " [27]", "mixed"
    if re.fullmatch(r"\{L\d+\}", core):
        return core, "open"
    if (core.isdigit() and core != "4") or core in ("+", "e4,s.{ar}"):
        return f"[{core}]", "open"

    # Handle apostrophe / internal comma splits (e.g. ipux'&, 94', id4', ri,érri4)
    pieces = re.split(r"([',])", core)
    out_pieces = []
    cat = "uniq"
    for p in pieces:
        if p in ("'", ","):
            out_pieces.append(p)
            continue
        if not p:
            continue
        parses = full_coverage_parses(p, signs)
        if parses:
            plains = sorted({render_parse(ps, signs) for ps in parses})
            if len(plains) == 1:
                out_pieces.append(plains[0])
            else:
                out_pieces.append("|" + "/".join(plains) + "|")
                if cat != "slip":
                    cat = "ambig"
        else:
            out_pieces.append(fallback_decode(p, signs))
            cat = "slip"
    return "".join(out_pieces), cat


def main() -> None:
    signs, nom = load_key(KEY_PATH)
    out_lines = [
        "# Unedited mechanical decryption of Modena Estense Campori, Gonzaga Federico II, cc. 13r-13v (catalogue 2162).",
        "# Generated strictly by applying recovered entries of key_gonzaga1537.tsv to transcription_13r_13v.txt",
        "# via decrypt_13r_13v.py, with ZERO dictionary lookup, ZERO language model, and ZERO manual edits.",
        "# Notation: C = cipher line; K = mechanical key output (<<...>> = inline clear Italian; |a/b| = multiple",
        "#           valid full-coverage i-digraph parses; [c] = character with no full-coverage parse; [NN] / {L..} = open code).",
        "",
    ]

    counts = {"uniq": 0, "ambig": 0, "slip": 0, "nom": 0, "open": 0}
    for raw in TRANS_PATH.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(L\d{2})\s+(.*)$", raw)
        if not m:
            continue
        lbl, body = m.group(1), m.group(2)
        c_parts, k_parts = [], []
        for part in re.split(r"(<<.*?>>)", body):
            part = part.strip()
            if not part:
                continue
            if part.startswith("<<") and part.endswith(">>"):
                c_parts.append(part)
                k_parts.append(part)
            else:
                for tok in part.split():
                    if tok in (".", ":", "/", ","):
                        continue
                    c_parts.append(tok)
                    dec_s, cat = decode_token(tok, signs, nom)
                    k_parts.append(dec_s)
                    if cat == "mixed":
                        counts["uniq"] += 1
                        counts["open"] += 1
                    elif cat in counts:
                        counts[cat] += 1
        out_lines.append(f"{lbl} C  " + " ".join(c_parts))
        out_lines.append(f"{lbl} K  " + " ".join(k_parts))
        out_lines.append("")

    tot = sum(counts.values())
    word_tot = counts["uniq"] + counts["ambig"] + counts["slip"] + counts["nom"]
    out_lines.append(
        f"# Summary: {tot} non-clear tokens ({word_tot} letter/che words: "
        f"{counts['uniq']} unique exact parse, {counts['ambig']} boundary-ambiguous exact parse, "
        f"{counts['nom']} nomenclator 30=che, {counts['slip']} scribal/unmapped-stroke fallback; "
        f"{counts['open']} open numeric/underlined-L/abbreviated codes)."
    )
    OUT_PATH.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH}")
    print(out_lines[-1])


if __name__ == "__main__":
    main()
