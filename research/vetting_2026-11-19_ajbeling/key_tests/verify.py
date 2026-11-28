"""Reproduce the fourteen reserved rows and historical/shuffled bigram scores."""

import argparse
import csv
import hashlib
import json
import math
import random
import re
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
CORPUS = HERE.parents[2] / "targets/edmondes1594/corpus/corpus_butler.txt"
CORPUS_HASH = "05f76766ad91be3852a8c9ea5f1ccd2ebb5b046cfa809d43fcd811f0abdd5449"


def table(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def normalize(text):
    return text.lower().replace("j", "i").replace("v", "u")


def corpus_counts(path):
    if hashlib.sha256(path.read_bytes()).hexdigest() != CORPUS_HASH:
        raise ValueError("Unexpected scoring corpus")
    counts = Counter()
    for paragraph in re.split(r"\n\s*\n", path.read_text()):
        letters = normalize(re.sub("[^a-z]", "", paragraph.lower()))
        counts.update(zip(letters, letters[1:]))
    return counts


def agreed_tiles(key):
    readings = []
    for reader in ("a", "b"):
        rows = [r for r in table(HERE / f"map_{reader}.tsv") if r["key"] == key]
        if len(rows) != 53:
            raise ValueError(f"Incomplete comparison for {reader}, key {key}")
        readings.append({r["shape"]: r["tile"] for r in rows
                         if r["confidence"].lower() == "high" and r["tile"].isdigit()})
    first, second = readings
    return {shape: tile for shape, tile in first.items() if second.get(shape) == tile}


def observations(key):
    tiles = agreed_tiles(key)
    lines = defaultdict(list)
    shapes = set()
    for row in table(HERE.parent / "transcription/consensus.tsv"):
        if row["line"] in {"U02", "L08", "U08"}:
            continue
        tile = tiles.get(row["agreed"])
        lines[row["line"]].append(tile)
        if tile is not None:
            shapes.add(row["agreed"])
    row_stats = {}
    pairs = []
    for line, seq in lines.items():
        neighbors = [(a, b) for a, b in zip(seq, seq[1:]) if a and b]
        pairs.extend(neighbors)
        row_stats[line] = dict(positions=len(seq), covered=sum(t is not None for t in seq),
                               pairs=len(neighbors))
    return shapes, pairs, row_stats


def verify(key, seed, counts, expected):
    values = {r["tile"]: (r["kind"], r["value"]) for r in table(HERE / "values.tsv")
              if r["key"] == key}
    shapes, pairs, rows = observations(key)
    denominator = sum(counts.values()) + 67.6

    def score(assignments):
        total_score = 0
        for a, b in pairs:
            left = normalize(assignments[values[a]])[-1]
            right = normalize(assignments[values[b]])[0]
            total_score += math.log((counts[left, right] + 0.1) / denominator)
        return total_score / len(pairs) if pairs else 0.

    actual = score({value: value[1] for value in values.values()})
    groups = {kind: sorted({s for k, s in values.values() if k == kind})
              for kind in ("letter", "word")}
    rng = random.Random(seed)
    controls = []
    for _ in range(1000):
        shuffled = {}
        for kind, original in groups.items():
            perm = original.copy()
            rng.shuffle(perm)
            shuffled.update({(kind, a): b for a, b in zip(original, perm)})
        controls.append(score(shuffled))
    covered = sum(row["covered"] for row in rows.values())
    total = sum(row["positions"] for row in rows.values())
    lines_with_pairs = sum(row["pairs"] > 0 for row in rows.values())
    eligible = (covered / total >= 0.30 and len(shapes) >= 8
                and len(pairs) >= 24 and lines_with_pairs >= 4)
    status = "underpowered"
    if eligible:
        status = "pass" if actual > max(controls) else "miss"
    result = dict(coverage=covered, total=total, distinct_shapes=len(shapes),
                  adjacent_pairs=len(pairs), lines_with_pairs=lines_with_pairs,
                  controls_equal_or_better=sum(s >= actual for s in controls),
                  shuffles_run=len(controls), status=status, row_stats=rows)
    for field, value in result.items():
        if expected[field] != value:
            raise ValueError(f"Key {key}: difference in {field}")
    for field, value in [("observed", actual), ("best_shuffle", max(controls))]:
        if not math.isclose(expected[field], value, abs_tol=1e-12, rel_tol=0):
            raise ValueError(f"Key {key}: difference in {field}")
    print(f"Key {key}: {covered}/{total} slots, {len(pairs)} adjacent pairs, "
          f"{result['controls_equal_or_better']}/1000 shuffles equal or better.")



def verify_chartley():
    source = HERE / "chartley"
    readers = []
    for filename in ("reader_a.tsv", "reader_b.tsv"):
        rows = table(source / filename)
        if {int(r["shape"]) for r in rows} != set(range(1, 54)) or len(rows) != 53:
            raise ValueError("Missing or duplicate Chartley comparison")
        readers.append({r["shape"].zfill(2): r["tile"].zfill(2) for r in rows
                        if r["confidence"].lower() == "high" and r["tile"].isdigit()})
    agreed = {s: t for s, t in readers[0].items() if readers[1].get(s) == t}
    values = {r["tile"]: r["value"] for r in table(source / "values_v2.tsv")}
    lines = defaultdict(list)
    for r in table(HERE.parent / "transcription/consensus.tsv"):
        if r["line"] not in {"U02", "L08", "U08"}:
            lines[r["line"]].append(agreed.get(r["agreed"]))
    occurrences = Counter(t for seq in lines.values() for t in seq if t)
    overlaps = sum(bool(a and b) for seq in lines.values() for a, b in zip(seq, seq[1:]))
    result = json.loads((source / "result.json").read_text())
    if (agreed != result["accepted_shape_to_tile"] or dict(occurrences) != result["tile_occurrences"]
            or any(t not in values for t in occurrences)
            or sum(map(len, lines.values())) != result["reserved_slots"]
            or sum(occurrences.values()) != result["covered"]
            or sum(any(seq) for seq in lines.values()) != result["rows_with_placements"]
            or overlaps != result["adjacent_pairs"]):
        raise ValueError("Chartley comparison differs from the saved result")
    if overlaps or result["controls_equal_or_better"] != result["controls_run"]:
        raise ValueError("The recorded empty-score control does not follow from the pairs")
    print(f"Chartley additions: {sum(occurrences.values())} placements, {overlaps} adjacent pairs.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=CORPUS)
    counts = corpus_counts(parser.parse_args().corpus)
    expected = json.loads((HERE / "results.json").read_text())
    for name, seed in [("96", 1960), ("97", 1970), ("97a", 1971)]:
        verify(name, seed, counts, expected[name])
    verify_chartley()
