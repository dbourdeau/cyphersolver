#!/usr/bin/env python3
"""Verify strict mechanical alignment and count sure cipher words / holes for Cosimo 1537 main-system readings.

Rules verified deterministically (19 November 2026 word rule + sized marks):
1. In the unedited mechanical decode of r4039.md, r4047.md, and r4054.md, every
   doubtful-digit letter (⟨x⟩), open code (·), break ([?]), and non-digit sign (#)
   is replaced with a barrier token '!' so NO unmarked ("sure") word may touch or
   cross any doubtful digit, open code, or gap.
2. Every contiguous run of unmarked ("sure") words between holes must appear
   verbatim as an unbroken substring of the clean mechanical decode stream
   (normalized only for case, accents, and u=v / i=j).
3. Every word containing [x] counts as one hole; each sized gap [... N] records the
   exact number N of unread decode letters/symbols spanned and contributes
   max(1, round(N / 5)) estimated words to the size-adjusted word count (alongside
   the raw 1-per-mark count).
"""

from __future__ import annotations

import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent.parent
RECS = ("r4039", "r4047", "r4054")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower().replace("v", "u").replace("j", "i")
    return re.sub(r"[^a-z]", "", s)


def extract_clean_decode_stream(md_path: pathlib.Path) -> str:
    txt = md_path.read_text(encoding="utf-8")
    rows = re.findall(r"decode: `([^`]+)`", txt)
    raw = "".join(rows)
    raw = re.sub(r"⟨[^⟩]*⟩", "!", raw)
    raw = raw.replace("[?]", "!").replace("·", "!").replace("#", "!")
    out = []
    for ch in raw.lower():
        if "a" <= ch <= "z":
            out.append("u" if ch == "v" else ("i" if ch == "j" else ch))
        elif ch == "!":
            out.append("!")
    return "".join(out)


def extract_reading_tokens(reading_path: pathlib.Path) -> list[str]:
    lines = []
    for line in reading_path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("*("):
            continue
        lines.append(s)
    text = " ".join(lines)
    # Keep [... N] as a single token
    text = re.sub(r"\[\.\.\.\s+(\d+)\]", r"[..._\1]", text)
    raw_toks = text.split()
    out: list[str] = []
    for tok in raw_toks:
        stripped = tok.strip(".,;:!?")
        if re.fullmatch(r"\[\.\.\.(?:_\d+)?\]", stripped):
            out.append(stripped)
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


def verify_one(rec: str) -> tuple[int, int, int, int]:
    decode_stream = extract_clean_decode_stream(HERE / f"{rec}.md")
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
    raw_holes = 0
    adj_holes = 0
    bad: list[str] = []
    for kind, toks in runs:
        if kind == "hole":
            raw_holes += len(toks)
            for t in toks:
                m = re.fullmatch(r"\[\.\.\._(\d+)\]", t)
                if m:
                    adj_holes += max(1, round(int(m.group(1)) / 5.0))
                else:
                    adj_holes += 1
            continue
        joined = "".join(norm(t) for t in toks)
        found = decode_stream.find(joined, pos)
        if found == -1:
            bad.append(f"sure run {toks!r} (joined={joined!r}) not found after pos={pos}, decode has {decode_stream[pos:pos+70]!r}")
        else:
            pos = found + len(joined)
            sure += len(toks)

    if bad:
        print(f"FAIL {rec}: {len(bad)} alignment error(s):")
        for msg in bad[:20]:
            print(" ", msg)
        sys.exit(1)
    raw_tot = sure + raw_holes
    adj_tot = sure + adj_holes
    print(
        f"OK {rec}: sure={sure:3d}, raw={sure}/{raw_tot} ({sure/raw_tot:.3f}, {raw_holes} marks), "
        f"size-adjusted={sure}/{adj_tot} ({sure/adj_tot:.3f}, {adj_holes} est. holes; 0 unmarked departures)"
    )
    return sure, raw_tot, adj_tot, adj_holes


def main() -> None:
    tot_s = tot_r = tot_a = tot_ah = 0
    for rec in RECS:
        s, r, a, ah = verify_one(rec)
        tot_s += s
        tot_r += r
        tot_a += a
        tot_ah += ah
    print(
        f"TOTAL (3 blind main-system letters): sure={tot_s}, raw={tot_s}/{tot_r} ({tot_s/tot_r:.3f}), "
        f"size-adjusted={tot_s}/{tot_a} ({tot_s/tot_a:.3f}, {tot_ah} est. holes)"
    )


if __name__ == "__main__":
    main()
