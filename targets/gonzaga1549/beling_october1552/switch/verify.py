"""Reproduce the registered two-title comparison, retaining alternatives as holes."""
import csv
import hashlib
import random
import unicodedata
from collections import defaultdict
from pathlib import Path

here = Path(__file__).resolve().parent
table_file = here.parents[2] / "figueroa1534/validation/K4.tsv"

assert hashlib.sha256(table_file.read_bytes()).hexdigest() == "a456e5bba6ee788371827d73ffa263ae034c98615bfb1f91dfdac3de90632ed6"

def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower().strip()) if not unicodedata.combining(c)).removeprefix("el ")

groups = defaultdict(set)
for line in table_file.read_text().splitlines():
    row = line.split("\t")
    if len(row) != 3:
        continue
    label, value, source = row
    if label.startswith("{") and label.endswith("}") and label[1:-1].isalpha():
        forms = groups[label[1:-1]]
        forms.update(fold(v) for v in value.split("|"))
codes = {k: next(iter(v)) for k, v in groups.items() if len(v) == 1
         and next(iter(v)).replace(" ", "").isalpha() and v != {"nul"}}
observed = defaultdict(list)
with (here / "readers.tsv").open() as stream:
    for row in csv.DictReader(stream, delimiter="\t"):
        observed[int(row["position"])].append(row["primary"] if row["certain"] == "yes" else None)
labels = [x[0] if len(x) == 2 and x[0] == x[1] else None for _, x in sorted(observed.items())]
target = ["duque", "principe"]
def score(key):
    return sum(key.get(label) == title for label,title in zip(labels, target))

rng = random.Random(1552100632)
keys = sorted(codes)
scores = []
for _ in range(1000):
    values = [codes[k] for k in keys]
    rng.shuffle(values)
    scores.append(score(dict(zip(keys,values))))
real = score(codes)
assert (here / "control_scores.txt").read_text() == "\n".join(map(str,scores))+"\n"
report = [
    f"Historical entries: {len(codes)} ; literal readings: {labels}",
    f"Primary (uncertain) readings would give: {codes.get('saa')} {codes.get('lim')}",
    f"Observed: {real} / 2; tied: {scores.count(real)} ; higher: {sum(i > real for i in scores)} ; maximum: {max(scores)}",
]
assert "\n".join(report)+"\n" == (here / "result.txt").read_text()
print("\n".join(report))
