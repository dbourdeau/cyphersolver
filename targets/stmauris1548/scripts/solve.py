"""Homophonic solver: each sign -> one value (letter, or consonant+vowel pair if --pairs), simulated annealing on
French 4-grams. Usage: python solve.py <transcription> [--pairs] [--fix fixed.tsv] [--restarts N] [--iters N] [--seed S]
Writes best key to stdout."""
import sys, re, math, random, numpy as np, os, collections, argparse
ap = argparse.ArgumentParser(); ap.add_argument("tr"); ap.add_argument("--pairs", action="store_true")
ap.add_argument("--fix"); ap.add_argument("--restarts", type=int, default=6); ap.add_argument("--iters", type=int, default=60000)
ap.add_argument("--seed", type=int, default=1); ap.add_argument("--map", default="A"); ap.add_argument("--nulls", default=""); ap.add_argument("--lam", type=float, default=1.0)
g = ap.parse_args(); random.seed(g.seed); np.random.seed(g.seed)
H = os.path.dirname(os.path.abspath(__file__)); q = np.load(os.path.join(H, "..", "model", "quad.npy"))
AL = "abcdefghilmnopqrstuxyz"; LI = {c: i for i, c in enumerate(AL)}
sys.path.insert(0, H); from compare import load, BMAP
rows = load(g.tr, BMAP if g.map == "B" else None)
toks = [t for k in rows for t in rows[k] if t not in g.nulls.split(",")]
syms = sorted(set(toks)); S = {s: i for i, s in enumerate(syms)}; ct = np.array([S[t] for t in toks])
freq = collections.Counter(toks)
vals = list(AL)
if g.pairs: vals += [c+v for c in "bcdfglmnpqrstu" for v in "aeiou"]
VI = [[LI[ch] for ch in v] for v in vals]
fixed = {}
if g.fix:
    for line in open(g.fix, encoding="utf-8"):
        if line.strip() and not line.startswith("#"):
            s, v = line.split()[:2]
            if s in S: fixed[S[s]] = vals.index(v)
def decode(m):
    out = []
    for c in ct: out.extend(VI[m[c]])
    return np.array(out)
REF = None
def score(m):
    d = decode(m); base = q[d[:-3], d[1:-2], d[2:-1], d[3:]].sum()
    obs = np.bincount(d, minlength=len(AL)) / len(d) + 1e-4
    kl = (obs * np.log10(obs / REF)).sum()
    return base - g.lam * len(d) * kl
best = None
uni = [0.176,0.008,0.033,0.034,0.176,0.011,0.009,0.007,0.074,0.053,0.029,0.075,0.056,0.029,0.016,0.065,0.087,0.072,0.082,0.005,0.006,0.001]
REF = np.array(uni) / sum(uni)
for r in range(g.restarts):
    m = [random.choices(range(len(AL)), weights=uni)[0] for _ in syms]
    for k, v in fixed.items(): m[k] = v
    cur = score(m); T0 = 3.0
    free = [i for i in range(len(syms)) if i not in fixed]
    for it in range(g.iters):
        T = T0 * (1 - it/g.iters) + 0.05
        i = random.choice(free); old = m[i]
        m[i] = random.randrange(len(vals)) if (g.pairs and random.random() < 0.3) else random.randrange(len(AL))
        new = score(m)
        if new >= cur or random.random() < math.exp((new-cur)/T): cur = new
        else: m[i] = old
    d_=decode(m); print("   ", "".join(AL[i] for i in d_[:120]), file=sys.stderr); print(f"restart {r}: score {cur:.1f} per-letter {cur/len(decode(m)):.3f}", file=sys.stderr)
    if best is None or cur > best[0]: best = (cur, list(m))
cur, m = best
print(f"# best score {cur:.1f}, per 4-gram {cur/len(decode(m)):.3f}")
for s in sorted(syms, key=lambda s: -freq[s]): print(f"{s}\t{vals[m[S[s]]]}\t{freq[s]}")
txt = "".join(vals[m[S[t]]] for t in toks)
print("#TEXT", txt[:1500])
