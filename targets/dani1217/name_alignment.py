"""Check all placements of the reported scribe's name with a single substitution."""
from itertools import combinations, product
from pathlib import Path

rows = [line.split() for line in Path(__file__).with_name("signs.txt").read_text().splitlines()
        if line and not line.startswith("#")]
for full in (False, True):
    trials = []
    for step, gap, start_name, ibn, father in product(
            (1, -1), range(4), ("ابو", "ابي"), ("بن", "ابن"), ("حميد", "حامد")):
        # Add possible lost signs only at the documented break in the second line.
        second = rows[1][:10] + ["?"] * gap + rows[1][10:]
        signs = rows[0][::step] + second[::step]
        name = start_name + "سعيد" + ibn + father + ("الشافعيالمقري" if full else "")
        for offset in range(len(signs) - len(name) + 1):
            pairs = [(s, c) for s, c in zip(signs[offset:], name) if s != "?"]
            if len(pairs) * 4 < len(name) * 3:
                continue
            conflicts = sum((s == t) != (c == d) for (s,c),(t,d) in combinations(pairs, 2))
            trials.append((conflicts, -len(pairs), name, step, gap, offset+1))
    print("full" if full else "short", "placements", len(trials),
          "exact", sum(r[0]==0 for r in trials), "best", min(trials))
