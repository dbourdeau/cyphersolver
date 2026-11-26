#!/usr/bin/env python3
"""Verify strict mechanical alignment and count sure cipher words / holes for Botti 1710 readings.

Rules verified deterministically:
1. Every unmarked ("sure") word in readings/<rec>_reading.md appears verbatim in
   exact sequential order in the unedited mechanical decode of <rec>.md (normalized
   only for case, accents, and u=v / i=j).
2. Every contiguous run of unmarked ("sure") words between holes appears as a
   single unbroken substring of the unedited mechanical decode (spaces removed).
3. Every word containing [...] or [x], and every standalone [...] gap, counts as
   one hole in the word count.
"""

from __future__ import annotations

import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent.parent
RECS = ("r8718", "r8673", "r8668", "r8661", "r8660", "r8664", "r8665")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower().replace("v", "u").replace("j", "i")
    return re.sub(r"[^a-z]", "", s)


def extract_decode_stream(md_path: pathlib.Path) -> str:
    txt = md_path.read_text(encoding="utf-8")
    rows = re.findall(r"- R\d+, T\d+, ≈?C\d+: `([^`]+)`", txt)
    raw = "".join(rows).replace("·", " ").replace("?", " ")
    return norm(raw)


def extract_reading_tokens(reading_path: pathlib.Path) -> list[str]:
    lines = []
    for line in reading_path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        lines.append(s)
    text = " ".join(lines)
    raw_toks = text.split()
    out: list[str] = []
    for tok in raw_toks:
        if tok.strip(".,;:!?") == "[...]":
            out.append("[...]")
            continue
        if "'" in tok and not tok.startswith("["):
            parts = tok.split("'")
            for i, p in enumerate(parts):
                if not p:
                    continue
                out.append(p + "'" if i < len(parts) - 1 else p)
        else:
            out.append(tok)
    return out


def verify_one(rec: str) -> tuple[int, int, int, float]:
    decode_stream = extract_decode_stream(HERE / f"{rec}.md")
    tokens = extract_reading_tokens(HERE / "readings" / f"{rec}_reading.md")
    runs: list[tuple[str, list[str]]] = []
    cur: list[str] = []
    for tok in tokens:
        if "[" in tok or "]" in tok or "…" in tok or "?" in tok:
            if cur:
                runs.append(("sure", cur))
                cur = []
            runs.append(("hole", [tok]))
        else:
            if norm(tok):
                cur.append(tok)
    if cur:
        runs.append(("sure", cur))

    pos = 0
    sure = 0
    holes = 0
    bad: list[str] = []
    for kind, toks in runs:
        if kind == "hole":
            holes += len(toks)
            continue
        joined = "".join(norm(t) for t in toks)
        found = decode_stream.find(joined, pos)
        if found == -1:
            bad.append(f"sure run {toks!r} (joined={joined!r}) not found after pos={pos}, decode has {decode_stream[pos:pos+60]!r}")
        else:
            pos = found + len(joined)
            sure += len(toks)

    if bad:
        print(f"FAIL {rec}: {len(bad)} alignment error(s):")
        for msg in bad[:20]:
            print(" ", msg)
        sys.exit(1)
    total = sure + holes
    share = sure / total if total else 0.0
    print(f"OK {rec}: cipher_words={total:3d}, sure={sure:3d}, holes={holes:2d}, read_share={share:.3f} (0 unmarked departures)")
    return total, sure, holes, share


def main() -> None:
    tot_w = tot_s = tot_h = 0
    for rec in RECS:
        w, s, h, _ = verify_one(rec)
        tot_w += w
        tot_s += s
        tot_h += h
    print(f"TOTAL ({len(RECS)} pure-blind letters): cipher_words={tot_w}, sure={tot_s}, holes={tot_h}, read_share={tot_s/tot_w:.3f}")


if __name__ == "__main__":
    main()
