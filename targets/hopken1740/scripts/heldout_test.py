"""Held-out test: decode the K lines of a page not used for the key and compare each group's key value with the
piece the word-level pairing gives it there. usage: python scripts/heldout_test.py key.tsv wordpairs_heldout.tsv
Control: the same key with its values shuffled among its groups, 500 times."""
import sys, random, unicodedata
def fold(s):
    s = unicodedata.normalize("NFD", s.lower()); return "".join(c for c in s if c.isalpha() or c.isdigit())
key = {}
for ln in open(sys.argv[1], encoding="utf-8"):
    if ln[0] == "#": continue
    f = ln.rstrip("\n").split("\t"); key[f[0]] = (f[1], f[4])
items = []
for ln in open(sys.argv[2], encoding="utf-8"):
    if ln[0] == "#": continue
    f = ln.rstrip("\n").split("\t")
    if len(f) < 6 or f[2] != "K": continue
    gs, ps = f[3].split(), f[5].split("|")
    if len(gs) != len(ps): continue
    items += [(g, fold(p)) for g, p in zip(gs, ps) if "?" not in g]
def score(k): return sum(1 for g, p in items if g in k and k[g] == p)
k = {g: v for g, (v, s) in key.items()}
kc = {g: v for g, (v, s) in key.items() if s == "confirmed"}
n = len(items); known = sum(1 for g, _ in items if g in k)
print(f"held-out groups {n}; in key {known} ({known/n:.0%}); exact match {score(k)} ({score(k)/n:.0%} of all, {score(k)/known:.0%} of known)")
print(f"confirmed values only: in key {sum(1 for g,_ in items if g in kc)}, match {score(kc)}")
random.seed(1); gs = list(k); sh = []
for _ in range(500):
    vs = [k[g] for g in gs]; random.shuffle(vs); sh.append(score(dict(zip(gs, vs))))
print(f"shuffled control: mean {sum(sh)/len(sh):.1f}, max {max(sh)}")
