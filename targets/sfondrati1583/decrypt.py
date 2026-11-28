#!/usr/bin/env python3
"""Mechanical, unedited decoder for Cat. #2077 (BYU Vault MSS 771) and out-of-sample
Cat. #2518 (BYU Vault MSS 518 f. 3 item 2) — Terranova -> Sfondrati, Aug-Oct 1583.

Applies key.tsv (k-sfondrati1583-cg12) strictly to transcript_2077_v2.txt and
transcript_2518.txt with ZERO language model, ZERO dictionary lookup, ZERO per-word
overrides, and ZERO scribal-slip corrections. Writes decryption_2077.txt and decryption_2518.txt.
"""
from __future__ import annotations

import csv
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
KEY_PATH = HERE / "key.tsv"


def load_key_tables(path: pathlib.Path) -> tuple[dict[str, str], dict[str, str], dict[str, str], dict[str, str], dict[str, str]]:
    v_map: dict[str, str] = {}
    s_map: dict[str, str] = {}
    c_map: dict[str, str] = {}
    exact_map: dict[str, str] = {}
    short_nom: dict[str, str] = {}
    with path.open(encoding="utf-8") as fh:
        rows = csv.DictReader((r for r in fh if not r.startswith("#")), delimiter="\t")
        for row in rows:
            sec = row["section"].strip()
            tok = row["token"].strip()
            val = row["value"].strip()
            if sec == "VOWEL_MARK":
                v_map[tok] = val
            elif sec == "CODA_MARK":
                s_map[tok] = val
            elif sec == "BASE_CONSONANT":
                c_map[tok] = val
            elif sec == "EXACT_CORE":
                exact_map[tok] = val
            elif sec == "SHORT_NOM":
                short_nom[tok] = val
    return v_map, s_map, c_map, exact_map, short_nom


def apply_gemination(syl: str, has_star: bool, star_val: str) -> str:
    if not has_star or not syl:
        return syl
    if star_val == "*":
        if syl[0] in ("l", "r", "s", "f", "n"):
            return syl[0] + syl
        return syl
    return syl + star_val


def decode_token(
    tok: str,
    v_map: dict[str, str],
    s_map: dict[str, str],
    c_map: dict[str, str],
    exact_map: dict[str, str],
    short_nom: dict[str, str],
) -> tuple[bool, str]:
    if "~" in tok:
        return False, f"[{tok}]"
    if tok in short_nom:
        return True, short_nom[tok]
    if tok in exact_map:
        return True, exact_map[tok]
    if "=" in tok or (re.match(r"^[A-Za-z]{2,6}[^0-9]*$", tok) and tok != "Di" and not tok.startswith("Di,")):
        if not (tok.startswith("D") and (tok == "D" or (len(tok) >= 2 and tok[1] in v_map))):
            return False, f"[{tok}]"
    coda_chars = set(s_map.keys())
    i = len(tok)
    while i > 0 and tok[i - 1] in coda_chars:
        i -= 1
    core, codas = tok[:i], tok[i:]
    has_star = "*" in codas
    star_val = s_map.get("*", "*")
    cstr = "".join(s_map.get(c, "") for c in codas if c != "*")
    if core in exact_map:
        return True, apply_gemination(exact_map[core], has_star, star_val) + cstr
    if len(core) >= 2 and core[-1] in v_map and core[:-1] in c_map:
        syl = c_map[core[:-1]] + v_map[core[-1]]
        return True, apply_gemination(syl, has_star, star_val) + cstr
    return False, f"[{tok}]"


def decode_file(in_path: pathlib.Path, out_path: pathlib.Path, title: str, tables) -> None:
    v_map, s_map, c_map, exact_map, short_nom = tables
    out = [
        f"# Unedited mechanical decryption of {title}.",
        f"# Generated strictly by applying key.tsv to {in_path.name} via decrypt.py",
        "# with ZERO dictionary lookup, ZERO language model, and ZERO scribal-slip corrections.",
        "# Notation: C = canonical factored cipher line; K = unedited mechanical plaintext ([tok] = unglossed nomenclator or literal numeral).",
        "",
    ]
    tot = mapped = 0
    for raw in in_path.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if not s:
            continue
        if s.startswith("#"):
            if s.startswith("# ITEM") or s.startswith("# Page"):
                out.append(s)
            continue
        lid, body = s.split(":", 1)
        toks = body.strip().split()
        pieces = []
        for t in toks:
            tot += 1
            ok, val = decode_token(t, v_map, s_map, c_map, exact_map, short_nom)
            if ok:
                mapped += 1
                pieces.append(val)
            else:
                pieces.append(f" {val} ")
        txt = re.sub(r" +", " ", "".join(pieces)).strip()
        out.append(f"{lid.strip()} C  " + " ".join(toks))
        out.append(f"{lid.strip()} K  " + txt)
        out.append("")
    out.append(f"# Mechanical token coverage: {mapped}/{tot} ({100*mapped/max(1,tot):.2f}%)")
    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {out_path.name}: {mapped}/{tot} tokens ({100*mapped/max(1,tot):.2f}%)")


def main() -> None:
    tables = load_key_tables(KEY_PATH)
    decode_file(HERE / "transcript_2077_v2.txt", HERE / "decryption_2077.txt", "Cat. #2077 (BYU Vault MSS 771, Aug-Sep 1583)", tables)
    decode_file(HERE / "transcript_2518.txt", HERE / "decryption_2518.txt", "Cat. #2518 (BYU Vault MSS 518 f. 3 item 2, 5 Oct 1583)", tables)


if __name__ == "__main__":
    main()
