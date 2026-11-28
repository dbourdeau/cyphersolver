#!/usr/bin/env python3
"""Check the Lomenie 1595 reading against the repo's transcription (standard library only).

Run from targets/mornay1593/grening/:  python3 -I scripts/check_reading.py
Reads ../lomenie1595.txt (unchanged) and key_lomenie1595.tsv, writes lomenie1595_decryption.txt.
For each passage it splits the groups into figures 1-10, prints the letters each figure can stand
for (the unedited output of the key), and tests whether the proposed reading encodes to exactly
the printed figures.
"""
import os, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANSCRIPTION = os.path.join(os.path.dirname(HERE), "lomenie1595.txt")
KEY = os.path.join(HERE, "key_lomenie1595.tsv")
OUT = os.path.join(HERE, "lomenie1595_decryption.txt")

READINGS = {  # letters only; ? = figure not read
    "L1": "provincedebretaigne", "L2": "decamor", "L3": "lesdespesches", "L4": "decamor",
    "L5": "devennes", "L6": "villedeseuretedebretaigne", "L7": "lanecessite",
    "L8": "duroy", "L9": "dedicts", "L10": "lassambleedesaumur", "L11": "bearn",
    "L12": "lamesse", "L13": "deboisdauphin", "L14": "lemarquisdebelisle",
    "L15": "????querelles",
}

def load_key():
    enc = {}
    for line in open(KEY, encoding="utf-8"):
        if line.startswith("#") or line.startswith("letter") or not line.strip():
            continue
        letters, fig = line.split("\t")[:2]
        for l in letters.split("/"):
            enc[l] = int(fig)
    return enc

def split(groups):
    """Figures 1-10 written together: '10' is one figure wherever it occurs; anything else is one digit."""
    out = []
    for g in groups:
        i = 0
        while i < len(g):
            if g[i:i + 2] == "10":
                out.append(10); i += 2
            else:
                out.append(int(g[i])); i += 1
    return out

def main():
    enc = load_key()
    buckets = {}
    for l, f in sorted(enc.items()):
        buckets.setdefault(f, []).append(l)
    lines, exact, letters = [], 0, 0
    for row in open(TRANSCRIPTION, encoding="utf-8"):
        if not row.startswith("L"):
            continue
        pid, before, figs, after = [p.strip() for p in row.split("|")]
        toks = split(figs.split())
        reading = READINGS[pid]
        want = [enc.get(c) for c in reading]
        if len(want) == len(toks):
            diff = [i for i, (w, t) in enumerate(zip(want, toks)) if w is not None and w != t]
            unread = sum(1 for w in want if w is None)
        else:
            diff, unread = None, 0
        if diff == [] and unread == 0:
            verdict = "exact"
            if pid == "L8":
                verdict = "exact only with y = 8, a value seen nowhere else"
            else:
                exact += 1; letters += len(toks)
        elif diff is None:
            verdict = "LENGTH MISMATCH"
        else:
            verdict = "%d figure(s) differ, %d not read" % (len(diff), unread)
        lines += [
            "%s | %s | %s | %s" % (pid, before, figs, after),
            "   figures : " + " ".join(str(t) for t in toks),
            "   key     : " + " ".join("".join(buckets.get(t, ["?"])) for t in toks),
            "   reading : " + reading + "   [" + verdict + "]",
            "",
        ]
    lines.append("exact passages, not counting L8: %d of 15, %d letters" % (exact, letters))
    open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0

if __name__ == "__main__":
    sys.exit(main())
