"""Held-out test of the frozen key: python heldout_test.py key.tsv heldout.tsv
For each run, the best monotone alignment of the decoded groups against the letters of the interlinear French is found;
a group counts as 'decoded' when its key value matches the gloss letters exactly at its place in that alignment.
u and v are treated as one letter (the code does not separate them). Control: the same key with its values shuffled
among its groups (500 shuffles)."""
import sys, random, statistics
sys.path.insert(0, __file__.rsplit("\\", 1)[0].rsplit("/", 1)[0])
from build_key import load, norm

def readkey(p):
    k = {}
    for ln in open(p, encoding="utf-8"):
        if ln.startswith("#") or not ln.strip(): continue
        f = ln.rstrip("\n").split("\t"); k[f[0]] = "" if f[1] == "[null]" else f[1]
    return k

def uv(s): return s.replace("v", "u")

def score(groups, text, key, MAX=12):
    text = uv(text); n, m = len(groups), len(text)
    best = [[-1] * (m + 1) for _ in range(n + 1)]; best[0][0] = 0
    for i, g in enumerate(groups):
        v = uv(key[g]) if g in key else None
        for j in range(m + 1):
            b = best[i][j]
            if b < 0: continue
            if v is not None and text.startswith(v, j) and best[i + 1][j + len(v)] < b + 1:
                best[i + 1][j + len(v)] = b + 1
            for L in range(0, min(MAX, m - j) + 1):
                if best[i + 1][j + L] < b: best[i + 1][j + L] = b
    return max(best[n][m], 0)

key = readkey(sys.argv[1]); runs = load(sys.argv[2], {"H"})
tot = sum(len(g) for _, g, _ in runs); known = sum(1 for _, g, _ in runs for x in g if x in key)
hit = sum(score(g, t, key) for _, g, t in runs)
random.seed(1); vals = list(key.values()); sh = []
for _ in range(500):
    random.shuffle(vals); k2 = dict(zip(key.keys(), vals))
    sh.append(sum(score(g, t, k2) for _, g, t in runs))
print(f"held-out groups {tot}; in frozen key {known} ({known/tot:.0%}); decoded to the gloss {hit} ({hit/tot:.0%} of all, {hit/known:.0%} of known)")
print(f"shuffled key: mean {statistics.mean(sh):.1f}, max {max(sh)} of {tot}")
for rid, g, t in runs:
    print(rid, " ".join(key.get(x, "[" + x + "]") for x in g), "|", t)
