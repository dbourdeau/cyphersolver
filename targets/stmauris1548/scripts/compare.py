"""Align pass A and pass B (B names mapped to A names), report disagreements and agreement rate."""
import re, sys, difflib, collections
BMAP = {"N31": "N1", "N9": "N1", "N11": "N2", "N12": "N3", "N7": "N4", "N17": "N5", "N10": "N6", "N3o": "N7o",
        "N15": "N8", "N5": "N9", "N1": "N10", "N2": "N11", "N24": "Le", "N21": "fs", "N26": "fs", "n": "y", "y": "q",
        "N13": "vto", "N25": "y"}
def load(fn, mp=None):
    rows = {}
    for line in open(fn, encoding="utf-8"):
        m = re.match(r"^(\d[rv]) (L\d\d):\s*(.*)$", line.strip())
        if not m: continue
        body = re.sub(r'"[^"]*"', "", m.group(3)).split()
        toks = []
        for t in body:
            t = t.rstrip("?")
            if t in (".", "/", "(", "") : continue
            toks.append(mp.get(t, t) if mp else t)
        rows[(m.group(1), m.group(2))] = toks
    return rows
if __name__ == "__main__":
    A = load("transcription_l2_passA.txt"); B = load("transcription_l2_passB.txt", BMAP)
    tot = same = 0; dis = []
    for k in A:
        a, b = A[k], B.get(k, [])
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            n = max(i2-i1, j2-j1); tot += n
            if op == "equal": same += n
            else: dis.append((k, i1, " ".join(a[i1:i2]), " ".join(b[j1:j2])))
    print(f"aligned positions {tot}, same {same}, rate {same/tot:.3f}, disagreements {len(dis)}")
    for d in dis: print(*d, sep=" | ")
    c = collections.Counter(t for r in A.values() for t in r); print(len(c), "distinct in A"); print(c.most_common())
