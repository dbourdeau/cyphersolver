"""Reproduce the Lévis identification test with Python's standard library."""
import csv
import hashlib
import json
import random
import unicodedata
from pathlib import Path

here = Path(__file__).resolve().parent
plan_data = (here / "plan.json").read_bytes()
assert hashlib.sha256(plan_data).hexdigest() == "4224185d794fa02a2d387292f4f39eacd03995e16e72962b3e301bad4c9b5893"
plan = json.loads(plan_data)
with (here.parent.parent / "key" / "levis_identification.tsv").open() as source:
    rows = list(csv.DictReader(source, delimiter="\t"))

def normalize(value):
    plain = value.lower().replace("œ", "oe").replace("æ", "ae")
    return "".join(c for c in unicodedata.normalize("NFD", plain) if c.isalnum())

def count(values, expected):
    return sum(bool(v) and v == normalize(e) for v,e in zip(values, expected))

assert [r["group"] for r in rows] == list(plan["anchors"])
models = list(zip(*plan["anchors"].values()))
values = []
for row in rows:
    complete = row["status_A"] == row["status_B"] == "clear"
    a, b = normalize(row["pass_A"]), normalize(row["pass_B"])
    value = a if complete and a and a == b else ""
    assert value == row["consensus_normalized"]
    assert [row[k] for k in ("B", "W", "I", "Vaudreuil_276")] == plan["anchors"][row["group"]]
    values.append(value)

observed = [count(values,m) for m in models]
rng = random.Random(17590132)
controls = []
for trial in range(1000):
    mixed = values.copy()
    rng.shuffle(mixed)
    controls.append([count(mixed,m) for m in models])
with (here / "shuffled_scores.tsv").open() as audit:
    archived = list(csv.reader(audit,delimiter="\t"))
assert [[int(x) for x in row[1:]] for row in archived[1:]] == controls
best = max(max(scores) for scores in controls)
ranking = sorted(observed, reverse=True)
passed = ranking[0] >= 12 and ranking[0] - ranking[1] >= 7 and ranking[0] > best
print(f"{plan['models']}: {observed}; strongest shuffle {best}; passed {passed}")
