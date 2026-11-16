"""shuffle.py: shuffled-key control for the gerlach1252 pp.124-137 blind decode.

Usage:  python3 -I shuffle.py REPO_ROOT [N] [SEED ...]
  REPO_ROOT  a cyphersolver checkout (for lang/, the shared language models)
  N          shuffles per seed (default 5000)
  SEED       seeds (default 20261112 7)

Reads BLIND_all.tsv and key_frozen.tsv beside this script (read only; FREEZE hash checked), never edits them.
Real decode: every sign label through the frozen key, as decode_once.py does; doubt marks '?' dropped;
'#', '[...]', '{clear}', '.', ';', ':', '=' and labels not in the key contribute no letter.
Check: the real letter string must equal the letters in decode_once.txt (same filter); the script stops otherwise.
Shuffle: the letter column of the key is permuted among the sign labels (key values permuted among signs),
the same token stream decoded again. Score: lang model de-1500s (German 1470-1610), letters only (spaces=False),
order 5, mean log-prob per letter (lm.per_char on lm.norm(text, 'early', spaces=False)).
Pass rule: fewer than 5 of N shuffles score >= the real decode, at every seed.
"""
import hashlib
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
repo = os.path.abspath(sys.argv[1])
N = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
SEEDS = [int(s) for s in sys.argv[3:]] or [20261112, 7]
sys.path.insert(0, repo)
from lang import lm  # noqa: E402

KEY = os.path.join(HERE, "key_frozen.tsv")
want = re.search(r"^sha256:\s*([0-9a-f]{64})", open(os.path.join(HERE, "FREEZE.txt"), encoding="utf-8").read(), re.M).group(1)
assert hashlib.sha256(open(KEY, "rb").read()).hexdigest() == want, "key hash mismatch"

labels, letters = [], []
for line in open(KEY, encoding="utf-8"):
    if not line.strip() or line.startswith("#"):
        continue
    f = line.rstrip("\n").split("\t")
    if f[0] == "letter":
        continue
    labels.append(f[1]); letters.append(f[0])
pos = {lab: i for i, lab in enumerate(labels)}

stream = []  # key-row index for every sign that decodes to a letter, in text order
rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "BLIND_all.tsv"), encoding="utf-8") if l.strip()][1:]
for r in rows:
    for t in re.findall(r"\{[^}]*\}|\[[^\]]*\]|\S+", r[2]):
        lab = t[:-1] if t.endswith("?") else t
        if lab in pos:
            stream.append(pos[lab])

def text(vals):
    return "".join(vals[i] for i in stream)

real = text(letters)
# cross-check against decode_once.txt
dec = []
for l in open(os.path.join(HERE, "decode_once.txt"), encoding="utf-8"):
    if l.startswith("  letters: "):
        s = l[len("  letters: "):].rstrip("\n")
        s = re.sub(r"\{[^}]*\}|<[^>]*>|\[[^\]]*\]", "", s)
        dec.append(re.sub(r"[^a-z]", "", s))
assert "".join(dec) == real, "real decode does not match decode_once.txt"

m = lm.load("de-1500s", spaces=False)
def score(s):
    return m.per_char(lm.norm(s, "early", spaces=False))

rs = score(real)
print(f"letters scored: {len(real)}; model de-1500s order {m.order} letters-only; real mean log-prob per letter {rs:.4f}")
print(f"real decode matches decode_once.txt letters: yes ({len(real)} letters)")
for seed in SEEDS:
    rng = random.Random(seed)
    sc = []
    for _ in range(N):
        v = letters[:]
        rng.shuffle(v)
        sc.append(score(text(v)))
    ge = sum(1 for x in sc if x >= rs)
    sc.sort()
    print(f"seed {seed}: {N} shuffles; >= real: {ge}; max {sc[-1]:.4f}; median {sc[N // 2]:.4f}; "
          f"min {sc[0]:.4f}; {'PASS' if ge < 5 else 'FAIL'} (pass = fewer than 5)")
