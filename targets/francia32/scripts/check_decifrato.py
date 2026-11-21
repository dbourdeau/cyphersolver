"""Compare the decode of two letters with the clerk's decipherment of the time on the same letter.

Usage, from the folder of this target: python3 scripts/check_decifrato.py
For R5621 (ff. 229v, 231r, 231v) against f. 230r, and for R5613 (f. 45v) against f. 46r, it prints
the letters of the decode, the letters of the decipherment, and the share of the decode's letters
that fall in matching blocks: with key no. 65, and with a wrong key. The wrong key gives the key's
pair values to its pairs in a fixed random order (seed 3). The label words of the transcription's
notes ("underlined:", "superscript:") do not count. check.md, section 1, gives the rule and the numbers.
It reads only files of this folder: the rows files in transcription/, the clerk's lines in
decifrato/, and the key of scripts/decode.py.

Credit: DECODE, the database of historical ciphers of the DECRYPT project, records R5613 and R5621
(https://de-crypt.org/decrypt-web/RecordsView/5613, https://de-crypt.org/decrypt-web/RecordsView/5621);
Archivio Apostolico Vaticano, Segreteria di Stato, Francia 32; M. Héder and B. Megyesi (2022),
"The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt,
https://doi.org/10.3384/ecp188397. No DECODE image is published.
"""
from __future__ import annotations

import difflib
import random
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
import decode as dk  # noqa: E402

TR = HERE.parent / "transcription"
DEC = HERE.parent / "decifrato"
CASES = [
    ("R5621 (229v, 231r, 231v) vs decifrato 230r",
     ["R5621_f229v_digits.txt", "R5621_f231r_digits.txt", "R5621_f231v_digits.txt"], "R5621_f230r.txt"),
    ("R5613 (045v) vs decifrato 046r", ["R5613_f045v_digits.txt"], "R5613_f046r.txt"),
]


def letters(t: str) -> str:
    """Letters only: no marks, no accents; u = v, i = j; a doubled letter counts once."""
    t = re.sub(r"«[^»]*»|<[^>]*>|\{[^}]*\}|\[[^\]]*\]", "", t)
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = re.sub(r"[^a-z]", "", t.replace("v", "u").replace("j", "i"))
    return re.sub(r"(.)\1+", r"\1", t)


LABEL = re.compile(r"\[(?:underlined|superscript):\s*")


def drop_labels(t: str) -> str:
    """Drop the label words of the transcription's notes: [underlined: x] -> [x], [superscript: m[a|o?]] -> m[a|o?]."""
    out, i = "", 0
    while m := LABEL.search(t, i):
        depth, j = 1, m.end()
        while depth and j < len(t):
            depth += {"[": 1, "]": -1}.get(t[j], 0)
            j += 1
        inner = t[m.end():j - 1]
        out += t[i:m.start()] + (inner if "[" in inner else "[" + inner + "]")
        i = j
    return out + t[i:]


def clear_letters(t: str) -> str:
    """The decipherment: no label words of the notes, the left reading of [a|b?], other brackets dropped."""
    t = re.sub(r"\[([^\]|]*)\|[^\]]*\]", r"\1", drop_labels(t))
    return letters(re.sub(r"\[[^\]]*\]", "", t))


def decode_letters(files: list[str]) -> str:
    out = ""
    for name in files:
        for line in (TR / name).read_text(encoding="utf-8").splitlines():
            if line.startswith("#") or not line.strip():
                continue
            toks = dk.lex(line.partition(" ")[2])
            if sum(1 for k, _ in toks if k == "d") >= 10:
                out += dk.decode(toks)
    return letters(out)


def decifrato_letters(name: str) -> str:
    rows = [ln for ln in (DEC / name).read_text(encoding="utf-8").splitlines() if re.match(r"^L\d+:", ln)]
    return clear_letters(" ".join(re.sub(r"^L\d+:\s*(\[[^\]]*\]\s*)?", "", ln) for ln in rows))


def matched(dec: str, a: str) -> int:
    sm = difflib.SequenceMatcher(None, dec, a, autojunk=False)
    return sum(x.size for x in sm.get_matching_blocks())


def main() -> None:
    right = dict(dk.PAIRS)
    ks = sorted(right)
    vs = [right[k] for k in ks]
    random.Random(3).shuffle(vs)
    wrong = dict(zip(ks, vs))
    for label, cipher, clerk in CASES:
        dec = decifrato_letters(clerk)
        dk.PAIRS.clear()
        dk.PAIRS.update(right)
        a = decode_letters(cipher)
        dk.PAIRS.clear()
        dk.PAIRS.update(wrong)
        w = decode_letters(cipher)
        dk.PAIRS.clear()
        dk.PAIRS.update(right)
        ma, mw = matched(dec, a), matched(dec, w)
        print(f"{label} | decifrato letters {len(dec)} | key: {ma} of {len(a)} decode letters "
              f"({ma / max(1, len(a)):.3f}) | wrong key: {mw} of {len(w)} ({mw / max(1, len(w)):.3f})")


if __name__ == "__main__":
    main()
