"""AFTER THE PLAN. Rebuild the one-letter-per-group key of CMXV.33.3233.1 (Terrazas to Avila, 11 May 1914) from the
stretches whose period text has as many letters as groups, then decode the other stretches and the two Villa
telegrams CMXV.33.3231.1-2 and 2-2 (same office, May 1914; no period decipherment).
Usage: python3 -I scripts/after_plan_terrazas_key.py
"""
import re, unicodedata
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


def rows(name):
    for line in (HERE / "heldout" / name).read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#") and not line.startswith("stretch\t"):
            yield line.split("\t")


def letters(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-zñ]", "", s)


groups = {r[0]: r[2].split() for r in rows("Ha_3233_groups.tsv")}
period = {r[0]: r[1] for r in rows("Ha_3233_period_decipherment.tsv")}
key = defaultdict(set)
used = []
for s, g in groups.items():
    p = letters(period[s])
    if len(p) == len(g):
        used.append(s)
        for a, b in zip(g, p):
            key[a].add(b)
print("stretches used for the key (letters = groups):", " ".join(used))
conf = {g: v for g, v in key.items() if len(v) > 1}
print("groups:", len(key), " conflicting:", conf or "none")
inv = defaultdict(list)
for g, v in sorted(key.items()):
    inv["/".join(sorted(v))].append(g)
print("letter -> groups:", "; ".join(f"{k}={','.join(v)}" for k, v in sorted(inv.items())))
K = {g: "/".join(sorted(v)) for g, v in key.items()}
for s, g in groups.items():
    if s not in used:
        print(f"{s}: {''.join(K.get(x, '[' + x + ']') for x in g)}   | period: {period[s]}")
VILLA = {
    "CMXV.33.3231.1-2 (Villa, Torreón 13 [May] 1914, typed)": "66 51 67 22 65 13 55 82 67 29 16 62 82",
    "CMXV.33.3231.2-2 (Villa draft, 16 May 1914, pencil)": "66 51 67 22 15 63 85 22 17 29 96 11 25 24 85",
}
for k, v in VILLA.items():
    print(f"{k}: {''.join(K.get(x, '[' + x + ']') for x in v.split())}")

# The values above fit one rule (found by looking at them, after the plan): with a = 1 ... z = 26 (26 letters),
# a group g <= 26 stands for the letter (g - 17) mod 26 and a group g >= 27 for (g - 15) mod 26 (0 read as z).
def rule(g):
    g = int(g)
    n = (g - 17) % 26 if g <= 26 else (g - 15) % 26
    return "abcdefghijklmnopqrstuvwxyz"[(n or 26) - 1]


bad = [(g, v) for g, v in K.items() if rule(g) != v]
print("groups the rule gets wrong among the 30 attested:", bad or "none")
for s, g in groups.items():
    if s not in used:
        print(f"rule, {s}: {''.join(rule(x) for x in g)}   | period: {period[s]}")
for k, v in VILLA.items():
    print(f"rule, {k}: {''.join(rule(x) for x in v.split())}")
