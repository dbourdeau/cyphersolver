"""Read-only verification of the two March 1553 opening rows and all 1,000 controls."""
import argparse
import csv
import difflib
import hashlib
import json
import random
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

here = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--targets", type=Path, default=here.parents[2])
parser.add_argument("--enclosure", type=Path, default=here.parent / "spanish_enclosure.txt")
args = parser.parse_args()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(value):
    value = unicodedata.normalize("NFKD", value.lower()).translate(str.maketrans("vj", "ui"))
    return re.sub("[^a-z]", "", value)


def labels(path):
    return [row.split("|") for row in path.read_text().splitlines()]


def consensus(left, right):
    # Each reader's uncertain observations get a distinct, noncolliding identity.
    a = [s if not s.startswith("?") else ("A", i) for i, s in enumerate(left)]
    b = [s if not s.startswith("?") else ("B", i) for i, s in enumerate(right)]
    output = []
    for kind, a1, a2, b1, b2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        output.extend(a[a1:a2] if kind == "equal" else ["?"] * max(a2 - a1, b2 - b1))
    return output


def prefix_score(text, reference):
    # Prefix edit distance: the DP pattern is the short emitted string. Myers'
    # bit-vector recurrence gives the global edit distance at every reference prefix.
    masks = defaultdict(int)
    for i, char in enumerate(text):
        masks[char] |= 1 << i
    positive, negative, distance = -1, 0, len(text)
    end = 1 << (len(text) - 1)
    best = (-1, 0)
    for j, char in enumerate(reference, 1):
        mask = masks[char]
        xv = mask | negative
        xh = (((mask & positive) + positive) ^ positive) | mask
        ph = negative | ~(xh | positive)
        mh = positive & xh
        distance += bool(ph & end) - bool(mh & end)
        ph = (ph << 1) | 1
        mh <<= 1
        positive = mh | ~(xv | ph)
        negative = ph & xv
        best = max(best, (1 - distance / max(j, len(text)), j))
    return best


validation = args.targets / "figueroa1534/validation"
inputs = {p.name: p for p in (validation / "K4.tsv", validation / "LABELS-FORMES.md",
                               here / "PLAN_modena_shapes.md", here / "A.txt", here / "B.txt")}
for name in ("modena_shapes.sha256", "readers.sha256"):
    for line in (here / name).read_text().splitlines():
        digest, path = line.split(maxsplit=1)
        assert sha(inputs[Path(path).name]) == digest, path
enclosure = args.enclosure
assert sha(enclosure) == "9336d173241cbefe7092084c544681c05440cf98ecf3a1219200d9b4f019bc05"
reference = normalize(enclosure.read_text().split("[37r]\n", 1)[1].split("\n\n", 1)[0])
saved = json.loads((here / "result.json").read_text())
record = []
counts = []
left, right = labels(here / "A.txt"), labels(here / "B.txt")
assert len(left) == len(right) == 2
for a, b in zip(left, right):
    row = consensus(a,b)
    counts.append((len(row) - row.count("?"), len(row)))
    record.extend(row)
assert counts == [(6, 10), (14, 22)]
assert record == saved["consensus"]
options = defaultdict(set)
with (validation / "K4.tsv").open() as handle:
    for row in csv.DictReader((s for s in handle if not s.startswith("#")), delimiter="\t"):
        options[row["label"]].update(row["valeur"].split("|"))
key = {}
for label, possible in options.items():
    emission = "?"
    if len(possible) == 1:
        value = next(iter(possible))
        emission = "" if value == "NUL" else normalize(value) or "?"
    key[label] = emission


def decode(mapping):
    return "".join(mapping.get(label, "?") for label in record)


literal = decode(key)
assert literal == saved["mechanical"]
observed, length = prefix_score(literal, reference)
assert (observed, length) == (saved["similarity"], saved["prefix_length"])
rng = random.Random(15530314)
with (here / "control.tsv").open() as f:
    controls = list(csv.DictReader(f, delimiter="\t"))
assert len(controls) == 1000
computed = []
for i,row in enumerate(controls, 1):
    labels_shuffled = list(key.values())
    rng.shuffle(labels_shuffled)
    value, _ = prefix_score(decode(dict(zip(key, labels_shuffled))), reference)
    assert int(row["permutation"]) == i and value == float(row["score"])
    computed.append(value)
assert saved["control_max"] == max(computed)
assert saved["control_at_least_actual"] == sum(v >= observed for v in computed)
assert saved["passes"] is False and observed < .75
print(f"6/10 and 14/22 signs agree. Similarity {observed:.6f} at prefix {length}; "
      f"all 1,000 controls match (maximum {max(computed):.6f}). Registered result: miss.")
