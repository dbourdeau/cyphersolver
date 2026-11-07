"""Decrypt the seven Soviet courier letters (NARA M336 roll 75) and check them.

Single columnar transposition, no nulls. The plaintext is written in rows under the key;
the columns are read top to bottom in the order of the key numbers; long columns (when the
last row is short) are the leftmost ones.

    python decrypt.py            # decrypt ciphertext_corrected.txt, compare with plaintext.txt
    python decrypt.py --typed    # also count where the typed copy (transcription.txt) differs
"""
import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEYS = {
    "27001": [5, 1, 15, 16, 8, 4, 7, 17, 12, 18, 13, 2, 19, 14, 9, 6, 3, 10, 11],
    "27003": [1, 3, 10, 24, 6, 11, 12, 4, 2, 16, 5, 7, 14, 13, 8, 20, 15, 22, 17, 25, 23, 18, 19, 21, 9],
}
LETTERS = re.compile(r"[A-ZÄÖÜ?]")


def sections(path):
    out, cur = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"## (r75-\S+)", line)
        if m:
            cur = m.group(1)
            out[cur] = {"text": []}
            continue
        if cur is None or line.startswith("#"):
            continue
        m = re.match(r"Indicator (\d+), (\d+) letters", line)
        if m:
            out[cur]["ind"], out[cur]["count"] = m.group(1), int(m.group(2))
            continue
        out[cur]["text"].append(line)
    return out


def order(n_letters, key):
    """Plaintext positions in the order the ciphertext reads them."""
    n = len(key)
    rows = -(-n_letters // n)
    full = n_letters % n or n
    seq = []
    for col in sorted(range(n), key=lambda c: key[c]):
        height = rows if col < full else rows - 1
        seq += [r * n + col for r in range(height)]
    return seq


def decrypt(ct, key):
    pt = [None] * len(ct)
    for c, p in zip(ct, order(len(ct), key)):
        pt[p] = c
    return "".join(pt)


def main():
    ctx = sections(HERE / "ciphertext_corrected.txt")
    ptx = sections(HERE / "plaintext.txt")
    typed = sections(HERE / "transcription.txt") if "--typed" in sys.argv else {}
    ok = True
    for doc, s in ctx.items():
        key = KEYS[s["ind"]]
        ct = LETTERS.findall(" ".join(s["text"]))
        want = "".join(LETTERS.findall(" ".join(ptx[doc]["text"])))
        got = decrypt(ct, key)
        diff = sum(1 for a, b in zip(got, want) if a != b and "?" not in (a, b))
        lost = got.count("?")
        status = "OK" if diff == 0 and len(ct) == s["count"] == len(want) else "MISMATCH"
        ok &= status == "OK"
        line = f"{doc:12} {s['ind']} {len(key):2} columns  {len(ct):4} letters  {status}  lost/illegible {lost}"
        if typed:
            tl = re.sub(r"\[\?\]", "?", " ".join(typed[doc]["text"]))
            tl = LETTERS.findall(tl)
            line += f"  typed copy: {len(tl)} letters"
        print(line)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
