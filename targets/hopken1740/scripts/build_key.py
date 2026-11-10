"""Build the code list (group -> plaintext piece) from the interlinear pairs by hard-EM segmentation.

Each cipher run is paired with the French written over it. The French is reduced to letters (accents and
apostrophes dropped), and every group must account for a contiguous piece of it. Starting from a flat prior,
we alternate (1) best segmentation of each run under the current counts and (2) recounting, until stable.

usage: python build_key.py pairs.tsv key.tsv [use-letters, default K] [seeds.tsv]
Seeds enter as one pseudo-count each, in every round, so the pairs can overrule them.
"""
import sys, math, unicodedata, collections, re

MAXLEN = 9


def norm(s):
    s = re.sub(r"\[[^\]]*\]", "", s)
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if "a" <= c <= "z")


def load(path, uses):
    runs = []
    for ln in open(path, encoding="utf-8"):
        if ln.startswith("#") or not ln.strip():
            continue
        img, run, use, groups, gloss = ln.rstrip("\n").split("\t")
        if use in uses:
            runs.append((img + run, [g.rstrip("?") for g in groups.split()], norm(gloss)))
    return runs


def prior(s):
    if s == "":
        return 0.01
    return 0.45 ** len(s) / 26 ** len(s) * 26 * 3


def align(groups, text, counts, tot, alpha=0.5):
    n, m = len(groups), len(text)
    NEG = -1e18
    best = [[NEG] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]
    best[0][0] = 0.0
    for i in range(n):
        g = groups[i]
        c, t = counts[g], tot[g]
        for j in range(m + 1):
            if best[i][j] == NEG:
                continue
            for L in range(0, min(MAXLEN, m - j) + 1):
                s = text[j:j + L]
                p = (c.get(s, 0) + alpha * prior(s)) / (t + alpha)
                v = best[i][j] + math.log(p)
                if v > best[i + 1][j + L]:
                    best[i + 1][j + L] = v
                    back[i + 1][j + L] = j
    if best[n][m] == NEG:
        return None
    segs, j = [], m
    for i in range(n, 0, -1):
        pj = back[i][j]
        segs.append(text[pj:j])
        j = pj
    return segs[::-1]


def load_seeds(path):
    seeds = {}
    for ln in open(path, encoding="utf-8"):
        if ln.startswith("#") or not ln.strip():
            continue
        g, v = ln.split()
        seeds[g] = v
    return seeds


def seeded(seeds, w=1.0):
    counts = collections.defaultdict(dict)
    tot = collections.Counter()
    for g, v in seeds.items():
        counts[g][v] = w
        tot[g] += w
    return counts, tot


def em(runs, iters=30, seeds=None):
    counts, tot = seeded(seeds or {})
    prev = None
    for it in range(iters):
        segs = {rid: align(g, t, counts, tot) for rid, g, t in runs}
        counts, tot = seeded(seeds or {})
        for rid, g, t in runs:
            for grp, s in zip(g, segs[rid] or []):
                counts[grp][s] = counts[grp].get(s, 0) + 1
                tot[grp] += 1
        if segs == prev:
            break
        prev = segs
    return counts, tot, segs


if __name__ == "__main__":
    runs = load(sys.argv[1], set(sys.argv[3]) if len(sys.argv) > 3 else {"K"})
    seeds = load_seeds(sys.argv[4]) if len(sys.argv) > 4 else {}
    counts, tot, segs = em(runs, seeds=seeds)
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write("# group\tvalue\tseen\tagree\tother readings (from the pairs, hard-EM segmentation)\n")
        for g in sorted(counts):
            items = sorted(counts[g].items(), key=lambda kv: -kv[1])
            items = [(s_, n - (1 if seeds.get(g) == s_ else 0)) for s_, n in items]
            items = sorted([it for it in items if it[1] > 0], key=lambda kv: -kv[1])
            if not items:
                continue
            v, k = items[0]
            tot[g] -= 1 if g in seeds else 0
            f.write(f"{g}\t{v or '[null]'}\t{tot[g]}\t{k}\t{' '.join(f'{s or chr(216)}:{n}' for s, n in items[1:])}\n")
    for rid, g, t in runs:
        print(rid, " ".join(f"{a}={b}" for a, b in zip(g, segs[rid] or ["?"] * len(g))))
