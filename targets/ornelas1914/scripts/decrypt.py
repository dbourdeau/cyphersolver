"""Decrypt CMXV.35.3492.2-3 with the syllabary card as transcribed (key.tsv), unchanged, and count the cipher words.

Writes decryption_CMXV.35.3492.2-3.txt (the unedited output of the key, line by line against the transcription).
With --check it rebuilds the text in memory and compares it with the file instead of writing.
The word list below is the reading's division of the decrypted string into the telegram's words; the script checks
that the words, joined, give back exactly the decrypted string, so no letter is added or dropped by the division.
Usage: python3 -I scripts/decrypt.py [--check]
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TID = "CMXV.35.3492.2-3"

# (word as the key gives it, word as read, status) ; status: read | hole
WORDS = [
    ("se", "se", "read"), ("rumora", "rumora", "read"), ("por", "por", "read"), ("aqui", "aquí", "read"),
    ("y", "y", "read"), ("la", "la", "read"), ("prensa", "prensa", "read"), ("tambien", "también", "read"),
    ("lo", "lo", "read"), ("dice", "dice", "read"), ("que", "que", "read"),
    ("biene", "biene", "read"), ("a", "a", "read"), ("esta", "ésta", "read"), ("mi", "mi", "read"),
    ("general", "general", "read"), ("billa", "Billa", "read"),
    ("sirrase", "Sir{va}se", "hole"),
    ("informarme", "informarme", "read"), ("lo", "lo", "read"), ("que", "que", "read"),
    ("aya", "aya", "read"), ("de", "de", "read"), ("cierto", "cierto", "read"),
]


def key():
    k = {}
    for line in (HERE / "key.tsv").read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or line.startswith("group\t"):
            continue
        g, v = line.split("\t")[:2]
        k[g] = v
    assert len(k) == 100
    return k


def lines():
    out = []
    for line in (HERE / f"transcription_{TID}.txt").read_text(encoding="utf-8").splitlines():
        if line.startswith("L"):
            tag, groups = line.split(":", 1)
            out.append((tag, groups.split()))
    return out


def build():
    k = key()
    rows = ["# Decryption of CMXV.35.3492.2-3 with key.tsv (row digit, then column digit), unedited output of the key.",
            "# Written by scripts/decrypt.py. One line of the form per block: group=value, then the values run together.",
            ""]
    allv = []
    for tag, groups in lines():
        vals = [k[g] for g in groups]
        allv += vals
        rows.append(f"{tag}: " + " ".join(f"{g}={v}" for g, v in zip(groups, vals)))
        rows.append(f"{tag}> " + "".join(vals))
    rows += ["", "Whole text, run together: " + "".join(allv), "[clear on the form] Saludolo afecte."]
    return "\n".join(rows) + "\n", "".join(allv)


def main():
    text, run = build()
    assert "".join(w for w, _, _ in WORDS) == run, "word division does not give back the decrypted string"
    f = HERE / f"decryption_{TID}.txt"
    if "--check" in sys.argv:
        same = f.read_bytes() == text.encode("utf-8")
        print("decryption file matches the key's output:", same)
        if not same:
            sys.exit(1)
    else:
        with open(f, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("written", f.name)
    n = len(WORDS)
    r = sum(1 for _, _, s in WORDS if s == "read")
    print(f"groups {sum(len(g) for _, g in lines())}; cipher words {n}; read {r}; holes {n - r}; share {r / n:.3f}")
    print("holes:", [w for w, rd, s in WORDS if s == "hole"])
    print("reading:", " ".join(rd for _, rd, _ in WORDS))


if __name__ == "__main__":
    main()
