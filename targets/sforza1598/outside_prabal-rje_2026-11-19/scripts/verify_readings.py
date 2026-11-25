#!/usr/bin/env python3
"""Verify strict mechanical alignment and count sure cipher words / holes for Sforza 1598 blind readings.

Rules verified deterministically:
1. In the unedited mechanical decode (key/<REC>_p*_decode.txt), every unknown sign
   (?), unread sign ([?]), and null (·) is treated as a barrier '!' so NO unmarked
   ("sure") word may cross an unknown or unread sign.
2. Every contiguous run of unmarked ("sure") words between holes must appear
   verbatim as an unbroken substring of the mechanical decode stream (normalized
   only for case, accents, and u=v / i=j).
3. Every word containing [...] or [x], and every standalone [...] gap, counts as
   one hole in the word count.
"""

from __future__ import annotations

import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent.parent
RECS = {
    "r5521": ["key/R5521_p1_decode.txt", "key/R5521_p2_decode.txt", "key/R5521_p3_decode.txt"],
    "r5523": ["key/R5523_p1_decode.txt"],
    "r5524": ["key/R5524_p1_decode.txt"],
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower().replace("v", "u").replace("j", "i")
    return re.sub(r"[^a-z]", "", s)


def extract_decode_stream(files: list[str]) -> str:
    parts = []
    for rel in files:
        txt = (HERE / rel).read_text(encoding="utf-8")
        for line in txt.splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            toks = line.split()[1:]
            for tok in toks:
                if tok in ("[?]", "?", "·"):
                    parts.append("!")
                else:
                    parts.append(norm(tok))
    return "".join(parts)


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


def verify_one(rec: str, files: list[str]) -> tuple[int, int, int, float]:
    decode_stream = extract_decode_stream(files)
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
        found = decode_stream.find(joined, pos, pos + 300)
        if found == -1:
            bad.append(f"sure run {toks!r} (joined={joined!r}) not found near pos={pos}, decode has {decode_stream[pos:pos+80]!r}")
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
    print(f"OK {rec}: cipher_words={total:3d}, sure={sure:3d}, holes={holes:3d}, read_share={share:.3f} (0 unmarked departures)")
    return total, sure, holes, share


def main() -> None:
    tot_w = tot_s = tot_h = 0
    for rec, files in RECS.items():
        w, s, h, _ = verify_one(rec, files)
        tot_w += w
        tot_s += s
        tot_h += h
    print(f"TOTAL (3 blind Sforza 1598 letters): cipher_words={tot_w}, sure={tot_s}, holes={tot_h}, read_share={tot_s/tot_w:.3f}")


if __name__ == "__main__":
    main()
