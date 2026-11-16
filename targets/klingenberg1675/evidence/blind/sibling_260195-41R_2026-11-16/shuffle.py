"""shuffle.py: shuffled-key control for the klingenberg1675 260195-41R blind decode (copy of the 134R script, this line only changed).

Usage:  python3 -I shuffle.py REPO_ROOT [N] [SEED ...]
  REPO_ROOT  a cyphersolver checkout (for lang/, the shared language models)
  N          shuffles per seed (default 5000)
  SEED       seeds (default 20261112 7)

Reads BLIND.tsv beside this script and the frozen key in ../_key_frozen (read only; hashes checked by importing
../decode_once.py's EXPECT, parse(), SIGN and load(), the code that made decode_once.txt). Edits nothing.
Real decode: every token as decode_once.py decodes it (number -> table_M3, else words_v4; letter sign -> SIGN);
holes, struck groups, drawn signs and marks contribute nothing. The valued units are concatenated.
Check: the real unit stream must equal the valued units in decode_once.txt; the script stops otherwise.
Shuffle: key values permuted among signs, within each class: the values of the number codes (table_M3 and
words_v4 merged, table first, as dec1 reads them) are permuted among the number codes, and the SIGN letter values
among the letter signs. The same token stream is decoded again. Score: lang model de-1640s (German 1600-1670),
letters only (spaces=False), order 5, mean log-prob per letter (lm.per_char on lm.norm(text, 'early', spaces=False)).
Pass rule: fewer than 5 of N shuffles score >= the real decode, at every seed.
"""
import hashlib
import importlib.util
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
repo = os.path.abspath(sys.argv[1])
N = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
SEEDS = [int(s) for s in sys.argv[3:]] or [20261112, 7]
sys.path.insert(0, repo)
from lang import lm  # noqa: E402

spec = importlib.util.spec_from_file_location("dec", os.path.join(HERE, "..", "decode_once.py"))
dec = importlib.util.module_from_spec(spec); spec.loader.exec_module(dec)
KEY = os.path.join(HERE, "..", "_key_frozen")
for f, h in dec.EXPECT.items():
    assert hashlib.sha256(open(os.path.join(KEY, f), "rb").read()).hexdigest() == h, f"hash mismatch {f}"
bl = os.path.join(HERE, "BLIND.tsv")
assert hashlib.sha256(open(bl, "rb").read()).hexdigest() == open(os.path.join(HERE, "FREEZE_blind.txt")).read().split()[0]

table = dec.load(os.path.join(KEY, "maps_table_M3.json")); words = dec.load(os.path.join(KEY, "maps_words_v4.json"))
num = dict(words); num.update(table)              # table first, as dec1 reads them
ncodes = sorted(num); nvals = [num[c] for c in ncodes]; npos = {c: i for i, c in enumerate(ncodes)}
lsigns = sorted(dec.SIGN); lvals = [dec.SIGN[s] for s in lsigns]; lpos = {s: i for i, s in enumerate(lsigns)}

stream = []   # ('N', i) or ('L', i) for every valued token, in text order
rows = [l.rstrip("\n").split("\t") for l in open(bl, encoding="utf-8") if l.strip() and not l.startswith("#")][1:]
for img, ln, toks, cw in rows:
    for kind, raw in dec.parse(toks):
        if kind != "T":
            continue
        t = raw[:-1] if raw.endswith("~") else raw
        core = t.replace('"', "")
        if "?" in core:
            continue
        if core.isdigit():
            if core in npos:
                stream.append(("N", npos[core]))
        elif core in lpos:
            stream.append(("L", lpos[core]))

def units(nv, lv):
    return [nv[i] if k == "N" else lv[i] for k, i in stream]

real_units = units(nvals, lvals)
# cross-check against decode_once.txt: its valued units (not holes, marks or struck) in order
got = []
for l in open(os.path.join(HERE, "decode_once.txt"), encoding="utf-8").read().splitlines()[1:]:
    d = l.split("\t")[3]
    for kind, raw in dec.parse(d):
        if kind == "T" and not raw.startswith("<") and not raw.startswith("["):
            got.append(raw)
assert " ".join(got).split() == " ".join(real_units).split(), "real decode does not match decode_once.txt"

m = lm.load("de-1640s", spaces=False)
def score(us):
    return m.per_char(lm.norm("".join(us), "early", spaces=False))

rs = score(real_units)
nl = len(lm.norm("".join(real_units), "early", spaces=False))
print(f"valued tokens: {len(stream)}; letters scored: {nl}; model de-1640s order {m.order} letters-only; "
      f"real mean log-prob per letter {rs:.4f}")
print(f"real decode matches decode_once.txt valued units: yes; number codes permuted {len(ncodes)}, letter signs {len(lsigns)}")
for seed in SEEDS:
    rng = random.Random(seed)
    sc = []
    for _ in range(N):
        a = nvals[:]; b = lvals[:]
        rng.shuffle(a); rng.shuffle(b)
        sc.append(score(units(a, b)))
    ge = sum(1 for x in sc if x >= rs)
    sc.sort()
    print(f"seed {seed}: {N} shuffles; >= real: {ge}; max {sc[-1]:.4f}; median {sc[N // 2]:.4f}; "
          f"min {sc[0]:.4f}; {'PASS' if ge < 5 else 'FAIL'} (pass = fewer than 5)")
