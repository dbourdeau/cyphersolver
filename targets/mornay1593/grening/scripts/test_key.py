#!/usr/bin/env python3
"""Two tests of the Lomenie 1595 key (standard library only). Not pre-registered: both were written after the
reading existed. They are mechanical, so anyone can re-run them.

    python3 -I scripts/test_key.py <path to mmoiresetcorre06morn_djvu.txt> [--anneal [--shape]]

Language model: letter trigrams (22-letter alphabet, j = i, v = u, no k or w) from the vol. 6 OCR text, with the
king's letter CVI, Lomenie's letter CVII and the table of contents cut out, so no word of the reading or of the
cribs' source is in the model.

A key gives each figure 1-10 a set of letters. The score of a key on a passage is the best log-probability over
all the letterings the key allows (Viterbi), summed over passages and divided by the number of figures.

Test 1, held-out passages. The twelve letters the two cribs fix (d e c a m o r, b t i g n) keep their values in
every key. The pattern key fills the other ten letters by the folded-alphabet rule. A null key gives each of those
ten letters a figure at random (redrawn if figure 5, which the cribs leave empty, gets no letter). All keys are scored on the passages the cribs do not touch (L3, L5, the first
sixteen figures of L6, L7-L14, and the tail of L15). The question: does the rule do better than chance on text it
was not built on?

Test 2 (--anneal), no cribs. Twelve annealing runs start from random keys (every figure 1-4 letters; with --shape,
2-3 letters, the shape of the pattern key) and climb on all fifteen passages. The question: does a search that knows nothing of the cribs arrive at the same key, and does
anything score better than it?
"""
import math, os, random, re, sys, unicodedata
from multiprocessing import Pool

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANSCRIPTION = os.path.join(os.path.dirname(HERE), "lomenie1595.txt")
ALPHA = "abcdefghilmnopqrstuxyz"
IDX = {c: i for i, c in enumerate(ALPHA)}
N = len(ALPHA)
PATTERN = dict(a=2, b=4, c=6, d=8, e=10, f=1, g=3, h=5, i=7, l=9, m=1, n=2, o=10, p=8, q=6, r=4, s=2,
               t=9, u=7, x=5, y=3, z=1)
CRIB_LETTERS = "decamorbtign"
LO, HI = (2, 3) if "--shape" in sys.argv else (1, 4)   # letters allowed per figure in the annealing runs
HELD_OUT = {"L3": None, "L5": None, "L6": 16, "L7": None, "L8": None, "L9": None, "L10": None, "L11": None,
            "L12": None, "L13": None, "L14": None, "L15": -9}   # None = whole passage; n = first n; -n = last n


def norm(text):
    text = "".join(c for c in unicodedata.normalize("NFD", text.lower()) if unicodedata.category(c) != "Mn")
    return text.replace("j", "i").replace("v", "u")


def build_lm(path):
    lines = open(path, encoding="utf-8", errors="ignore").read().splitlines()
    start = next(i for i, l in enumerate(lines) if re.match(r"\s*CVII\.\s", l))
    end = next(i for i, l in enumerate(lines) if i > start and re.match(r"\s*CVIII\.\s", l))
    cvi = max(i for i, l in enumerate(lines[:start]) if "LETTRE" in l and "ROY" in l)
    toc = next((i for i, l in enumerate(lines) if i > end and l.strip().startswith("TABLE")), int(len(lines) * 0.94))
    kept = lines[:cvi] + lines[end:toc]
    c1, c2, c3 = [1.0] * N, {}, {}
    for word in re.findall(r"[a-z]+", norm(" ".join(kept))):
        w = [IDX[ch] for ch in word if ch in IDX]
        for i, a in enumerate(w):
            c1[a] += 1
            if i >= 1: c2[(w[i - 1], a)] = c2.get((w[i - 1], a), 0) + 1
            if i >= 2: c3[(w[i - 2], w[i - 1], a)] = c3.get((w[i - 2], w[i - 1], a), 0) + 1
    t1 = sum(c1)
    ctx1 = [sum(c2.get((a, b), 0) for b in range(N)) for a in range(N)]
    ctx2 = {}
    for (a, b, c), n in c3.items(): ctx2[(a, b)] = ctx2.get((a, b), 0) + n
    p1 = [c / t1 for c in c1]
    lp = [[[0.0] * N for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            for c in range(N):
                q2 = c2.get((b, c), 0) / ctx1[b] if ctx1[b] else 0.0
                q3 = c3.get((a, b, c), 0) / ctx2[(a, b)] if ctx2.get((a, b)) else 0.0
                lp[a][b][c] = math.log(0.6 * q3 + 0.3 * q2 + 0.1 * p1[c])
    lp2 = [[math.log(0.8 * (c2.get((a, b), 0) / ctx1[a] if ctx1[a] else 0.0) + 0.2 * p1[b]) for b in range(N)]
           for a in range(N)]
    return [math.log(p) for p in p1], lp2, lp, len(kept)


def split(groups):
    out = []
    for g in groups:
        i = 0
        while i < len(g):
            if g[i:i + 2] == "10": out.append(10); i += 2
            else: out.append(int(g[i])); i += 1
    return out


def passages():
    out = {}
    for row in open(TRANSCRIPTION, encoding="utf-8"):
        if row.startswith("L"):
            pid, _, figs, _ = [p.strip() for p in row.split("|")]
            toks = split(figs.split())
            if pid == "L15": toks = toks[-9:]          # 100 76 is not read; the 0 has no value in any key
            out[pid] = toks
    return out


def viterbi(toks, buckets, lm):
    lp1, lp2, lp3 = lm
    first = buckets[toks[0]]
    if len(toks) == 1: return max(lp1[a] for a in first)
    cur = {}
    for a in first:
        for b in buckets[toks[1]]:
            cur[(a, b)] = lp1[a] + lp2[a][b]
    for t in toks[2:]:
        nxt = {}
        for (a, b), s in cur.items():
            row = lp3[a][b]
            for c in buckets[t]:
                v = s + row[c]
                if v > nxt.get((b, c), -1e99): nxt[(b, c)] = v
        cur = nxt
    return max(cur.values())


def score(key, texts, lm):
    buckets = {f: [] for f in range(1, 11)}
    for letter, fig in key.items(): buckets[fig].append(IDX[letter])
    if any(not buckets[t] for toks in texts for t in toks): return -99.0
    return sum(viterbi(toks, buckets, lm) for toks in texts) / sum(len(t) for t in texts)


def test1(lm, n=2000, seed=1):
    ps = passages()
    texts = []
    for pid, cut in HELD_OUT.items():
        t = ps[pid]
        texts.append(t if cut is None else t[:cut] if cut > 0 else t[cut:])
    real = score(PATTERN, texts, lm)
    rng = random.Random(seed)
    free = [c for c in ALPHA if c not in CRIB_LETTERS]
    nulls = []
    while len(nulls) < n:
        k = {c: PATTERN[c] for c in CRIB_LETTERS}
        for c in free: k[c] = rng.randint(1, 10)
        if 5 not in k.values(): continue               # 5 is the one figure the cribs leave without a letter
        nulls.append(score(k, texts, lm))
    mean = sum(nulls) / n
    sd = (sum((x - mean) ** 2 for x in nulls) / n) ** 0.5
    print("Test 1: held-out passages, %d figures; crib letters fixed, the other ten by rule or at random" %
          sum(len(t) for t in texts))
    print("  pattern key      %.3f per figure" % real)
    print("  %d random keys %.3f mean, %.3f sd, best %.3f" % (n, mean, sd, max(nulls)))
    print("  pattern key beats %d of %d; z = %.1f" % (sum(real > x for x in nulls), n, (real - mean) / sd))


def anneal_run(args):
    seed, lm, texts, steps = args
    rng = random.Random(seed)
    letters = list(ALPHA)
    while True:
        key = {c: rng.randint(1, 10) for c in letters}
        if all(LO <= sum(v == f for v in key.values()) <= HI for f in range(1, 11)): break
    cur = best = score(key, texts, lm); best_key = dict(key)
    for step in range(steps):
        temp = 0.08 * (1 - step / steps) + 0.002
        new = dict(key)
        if rng.random() < 0.5:
            a, b = rng.sample(letters, 2); new[a], new[b] = new[b], new[a]
        else:
            new[rng.choice(letters)] = rng.randint(1, 10)
        if new == key or not all(LO <= sum(v == f for v in new.values()) <= HI for f in range(1, 11)): continue
        s = score(new, texts, lm)
        if s >= cur or rng.random() < math.exp((s - cur) / temp):
            key, cur = new, s
            if s > best: best, best_key = s, dict(new)
    return seed, best, best_key


def test2(lm, runs=12, steps=6000):
    texts = list(passages().values())
    real = score(PATTERN, texts, lm)
    attested = [c for c in ALPHA if c not in "fxyz"]
    print("Test 2: annealing from random keys on all passages, no cribs (%d runs, %d steps, %d-%d letters per figure)" % (runs, steps, LO, HI))
    print("  pattern key %.3f per figure" % real)
    with Pool(min(runs, os.cpu_count() or 2)) as pool:
        res = pool.map(anneal_run, [(s, lm, texts, steps) for s in range(1, runs + 1)])
    for seed, best, key in sorted(res, key=lambda r: -r[1]):
        same = sum(key[c] == PATTERN[c] for c in attested)
        print("  run %2d  %.3f  agrees with the pattern key on %2d of %d attested letters" %
              (seed, best, same, len(attested)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    lp1, lp2, lp3, kept = build_lm(sys.argv[1])
    print("model: letter trigrams from %d lines of vol. 6 (CVI, CVII and the table of contents left out)" % kept)
    test1((lp1, lp2, lp3))
    if "--anneal" in sys.argv: test2((lp1, lp2, lp3))
