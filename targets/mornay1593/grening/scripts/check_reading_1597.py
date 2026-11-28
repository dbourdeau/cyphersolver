#!/usr/bin/env python3
"""Check the Duplessis Jan 1597 reading against the repo's transcription (standard library only).

Run from targets/mornay1593/grening/:  python3 -I scripts/check_reading_1597.py
Reads ../duplessis1597.txt (unchanged) and key_duplessis1597.tsv, writes duplessis1597_decryption.txt.
For each passage it splits the groups into figures 1-10, prints the letters each figure can stand for (the
unedited output of the key), and tests whether the proposed reading encodes to exactly the printed figures.
A reading may end in one extra e: where the words have an odd number of letters the clerk filled the last
pair with e (figure 1), so the last group is 11.
"""
import os, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANSCRIPTION = os.path.join(os.path.dirname(HERE), "duplessis1597.txt")
KEY = os.path.join(HERE, "key_duplessis1597.tsv")
OUT = os.path.join(HERE, "duplessis1597_decryption.txt")

READINGS = {  # letters only; ? = figure not read; + = the filling e at the end
    "C1": "dupart??contrai",
    "C2": "unprisonnierdequalite+",
    "C3": "poursignaluneeguilletebleueaupourpointoualamandille+",
    "C4": "vosgensdepoitoudient",
    "C5": "????????",
    "C6": "courbejoliere+",
    "C7": "ruinesursamaison",
    "C8": "monbarot",
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
    out = []
    for g in groups:
        i = 0
        while i < len(g):
            if g[i:i + 2] == "10": out.append(10); i += 2
            else: out.append(int(g[i])); i += 1
    return out

def main():
    enc = load_key(); enc["+"] = enc["e"]
    buckets = {}
    for l, f in sorted(enc.items()):
        if l != "+": buckets.setdefault(f, []).append(l)
    lines, exact, figs_exact, total = [], 0, 0, 0
    for row in open(TRANSCRIPTION, encoding="utf-8"):
        if not row.startswith(("C", "W")): continue
        parts = [p.strip() for p in row.split("|")]
        pid, before, figs, after = parts[0], parts[1], parts[2], parts[3]
        if pid.startswith("W"):
            lines += ["%s | %s | %s | %s" % (pid, before, figs, after),
                      "   not tried here: the letter to his wife uses other figures (40, 80, 132, printed letters)", ""]
            continue
        toks = split(figs.split()); total += len(toks)
        reading = READINGS[pid]
        want = [enc.get(c) for c in reading]
        if len(want) != len(toks): verdict = "LENGTH MISMATCH"
        else:
            diff = sum(1 for w, t in zip(want, toks) if w is not None and w != t)
            unread = sum(1 for w in want if w is None)
            if diff == 0 and unread == 0:
                verdict = "exact"; exact += 1; figs_exact += len(toks)
            else:
                verdict = "%d figure(s) differ, %d not read" % (diff, unread)
        lines += ["%s | %s | %s | %s" % (pid, before, figs, after),
                  "   figures : " + " ".join(str(t) for t in toks),
                  "   key     : " + " ".join("".join(buckets[t]) for t in toks),
                  "   reading : " + reading + "   [" + verdict + "]", ""]
    lines.append("exact passages: %d of 8 (C1-C8), %d of %d figures" % (exact, figs_exact, total))
    open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))

if __name__ == "__main__":
    sys.exit(main())
