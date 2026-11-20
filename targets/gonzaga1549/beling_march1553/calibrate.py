"""Fit and test the frozen March 1553 calibration. Standard library only."""
import argparse
import csv
import hashlib
import json
import random
import re
import unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
WAINUT = HERE.parent / "wainut"
KEY = WAINUT / "key.tsv"
NAMES = WAINUT / "scripts/blind_name_map.json"
TOKENS = WAINUT / "transcription_philip_1546_1553_x_blind.txt"
REFERENCE = HERE / "spanish_enclosure.txt"
PARAGRAPHS = ((1, 15), (16, 21), (22, 40), (41, 47), (48, 55), (56, 64))
HOLE = "?"
PLAN_HASH = "3ba51eaf7cf89a840392e1e4def72d366d45b1c75e05be45168f3c2fabff2e9b"


def norm(text):
    folded = unicodedata.normalize("NFKD", text.lower()).translate(str.maketrans("vj", "ui"))
    return re.sub("[^a-z]", "", folded)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_table(path, header, rows):
    with path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.writer(output, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def source_data():
    assert sha(HERE / "PLAN.md") == PLAN_HASH
    names = json.loads(NAMES.read_text())
    key = {}
    for line in KEY.read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            label, value = line.split("\t")[:2]
            key[label] = HOLE if "[" in value else norm(value)
    all_lines = dict((int(n), s.split()) for n, s in re.findall(r"^B-(\d+) (.*)$", TOKENS.read_text(), re.M))
    assert sorted(all_lines) == list(range(1, 65))
    baseline, groups, paragraphs = {}, set(), []
    for start, end in PARAGRAPHS:
        sequence = []
        for number in range(start, end + 1):
            for token in all_lines[number]:
                label = token.rstrip("?").strip("{}")
                if "{" in token:
                    groups.add(label)
                mapped = names.get(label, label)
                baseline[label] = "" if mapped.endswith("_") else key.get(mapped, key.get(label, HOLE))
                sequence.append(label)
        paragraphs.append(sequence)
    body = REFERENCE.read_text().split("[37r]\n")[1].replace("[37v]", "").replace("[38r]", "")
    chunks = [s.strip() for s in re.split(r"\n\s*\n", body) if s.strip()]
    assert len(chunks) == 8
    plain = list(map(norm, [chunks[0], chunks[1], chunks[2] + chunks[3], chunks[4] + chunks[5], chunks[6], chunks[7]]))
    candidates = sorted({v for v in key.values() if 1 <= len(v) <= 3 and v != HOLE} | set(norm("abcdefghijklmnopqrstuvwxyz")))
    return baseline, groups, paragraphs, plain, candidates


class Distance:
    """Myers' global bit-vector Levenshtein distance for a fixed Spanish target."""
    def __init__(self, reference):
        self.length = len(reference)
        self.high_bit = 1 << (self.length - 1)
        self.masks = {}
        for i, char in enumerate(reference):
            self.masks[char] = self.masks.get(char, 0) | (1 << i)

    def __call__(self, sequence):
        positive = -1
        negative = 0
        score = self.length
        for char in sequence:
            matches = self.masks.get(char, 0)
            xv = matches | negative
            xh = (((matches & positive) + positive) ^ positive) | matches
            ph = negative | ~(xh | positive)
            mh = positive & xh
            score += bool(ph & self.high_bit) - bool(mh & self.high_bit)
            ph = (ph << 1) | 1
            mh <<= 1
            positive = mh | ~(xv | ph)
            negative = ph & xv
        return score


def decoded(table, sequence):
    return "".join(table[label] for label in sequence)


def distances(table, paragraphs, metrics):
    return [metric(decoded(table, seq)) for seq, metric in zip(paragraphs, metrics)]


def train():
    base, groups, paragraphs, plain, candidates = source_data()
    training = paragraphs[:3]
    metrics = list(map(Distance, plain[:3]))
    counts = Counter(label for paragraph in training for label in paragraph)
    order = sorted((label for label, n in counts.items()
                    if n >= 5 and sum(label in p for p in training) >= 2
                    and label not in groups | {"#", "", "?"} and 0 < len(base[label]) <= 3),
                   key=lambda label: (-counts[label], label))
    fitted = dict(base)
    scores = distances(fitted, training, metrics)
    journal = []
    for sweep in range(1, 4):
        changes = 0
        for label in order:
            old = fitted[label]
            choices = []
            for candidate in sorted(set(candidates) | {base[label]}):
                if candidate == old:
                    continue
                fitted[label] = candidate
                trial = distances(fitted, training, metrics)
                gains = [a - b for a, b in zip(scores, trial)]
                if min(gains) >= 0 and sum(g > 0 for g in gains) >= 2 and sum(gains) >= 3:
                    choices.append((-sum(gains), candidate != base[label], candidate, trial))
            fitted[label] = old
            if choices:
                _, _, new, trial = min(choices)
                journal.append((sweep, label, counts[label], old, new, *scores, *trial))
                fitted[label] = new
                scores = trial
                changes += 1
        if not changes:
            break
    write_table(HERE / "training_changes.tsv", ("sweep","label","count","before","after","old_1","old_2","old_3","new_1","new_2","new_3"), journal)
    write_table(HERE / "assignments.tsv", ("label", "training_n", "eligible", "baseline", "fitted"),
                [(label, counts[label], int(label in order), base[label], fitted[label]) for label in sorted(base)])
    print("eligible", len(order), "final changes", sum(base[s] != fitted[s] for s in base), "training distances", scores, flush=True)


def test():
    base, _, paragraphs, plain, _ = source_data()
    with (HERE / "assignments.tsv").open() as file:
        assignments = list(csv.DictReader(file, delimiter="\t"))
    fitted = {row["label"]: row["fitted"] for row in assignments}
    assert {row["label"]: row["baseline"] for row in assignments} == base
    order = [row["label"] for row in assignments if row["eligible"] == "1"]
    count = {row["label"]: int(row["training_n"]) for row in assignments}
    metrics = list(map(Distance, plain))
    b = distances(base, paragraphs, metrics)
    f = distances(fitted, paragraphs, metrics)
    rows = []
    for i, (reference, seq) in enumerate(zip(plain, paragraphs)):
        reduced = reference.replace("sumagestad", "")
        extra = Distance(reduced)
        bd = extra(decoded(base, seq).replace("sumagestad", ""))
        fd = extra(decoded(fitted, seq).replace("sumagestad", ""))
        rows.append((i + 1, "fit" if i < 3 else "holdout", len(seq), len(reference), b[i], f[i],
                     (b[i]-f[i])/len(reference), len(reduced), bd, fd))
    write_table(HERE / "paragraphs.tsv", ("paragraph","split","tokens","spanish_letters","base_edits","fit_edits","CER_gain","no_formula_letters","no_formula_base_edits","no_formula_fit_edits"), rows)
    total_chars = sum(len(p) for p in plain[3:])
    fitted_edits = sum(f[3:])
    baseline_edits = sum(b[3:])
    labels = sorted(label for label in fitted if fitted[label] not in {"", HOLE})
    values = [fitted[label] for label in labels]
    strata = [[label for label in order if lo <= count[label] < hi] for lo, hi in ((5, 10),(10,20),(20,10**9))]
    key_rng, correction_rng = random.Random(15530314), random.Random(15530315)
    control_rows = []
    for i in range(1000):
        perm = values[:]
        key_rng.shuffle(perm)
        shuffled = dict(fitted)
        shuffled.update(zip(labels, perm))
        shuffled_edits = sum(distances(shuffled, paragraphs[3:], metrics[3:]))
        permuted_fit = dict(base)
        for stratum in strata:
            destinations = stratum[:]
            correction_rng.shuffle(destinations)
            for label, destination in zip(stratum, destinations):
                if fitted[label] != base[label]:
                    permuted_fit[destination] = fitted[label]
        permuted_edits = sum(distances(permuted_fit, paragraphs[3:], metrics[3:]))
        control_rows.append((i + 1, shuffled_edits, permuted_edits))
    write_table(HERE / "controls.tsv", ("shuffle","full_key_edits","redistributed_corrections_edits"), control_rows)
    gain = (baseline_edits - fitted_edits) / total_chars
    key_wins = sum(row[1] <= fitted_edits for row in control_rows)
    correction_wins = sum(row[2] <= fitted_edits for row in control_rows)
    passed = (gain >= .025 and sum(x > y for x,y in zip(b[3:],f[3:])) >= 2
              and all((y-x)/len(p) <= .02 for x,y,p in zip(b[3:],f[3:],plain[3:])) and key_wins == 0 and correction_wins <= 9)
    summary = {"holdout_letters":total_chars, "base_edits":baseline_edits, "fitted_edits":fitted_edits,
               "baseline_CER":baseline_edits/total_chars,"fitted_CER":fitted_edits/total_chars,
               "CER_gain":gain, "best_shuffled_key_edits":min(x[1] for x in control_rows),
               "best_shuffled_corrections_edits":min(x[2] for x in control_rows),"key_ties_or_wins":key_wins,
               "correction_ties_or_wins":correction_wins,"pass":passed}
    (HERE / "result.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary), flush=True)


def validate_distance():
    def slow(a, b):
        row = list(range(len(b) + 1))
        for i, x in enumerate(a, 1):
            new = [i]
            for j, y in enumerate(b, 1):
                new.append(min(row[j]+1, new[-1]+1, row[j-1]+(x!=y)))
            row = new
        return row[-1]
    rng = random.Random(522)
    for length in [1, 2, 11, 63, 64, 65, 128, 273]:
        a = "".join(rng.choices("abcdefghij", k=length))
        for k in [0, 1, length, length + 9]:
            b = "".join(rng.choices("abcdefghij?", k=k))
            assert Distance(a)(b) == slow(a,b)
    print("32 bit-vector distance checks passed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["validate", "fit", "test"])
    action = parser.parse_args().action
    if action == "validate":
        validate_distance()
    elif action == "fit":
        write_table(HERE / "inputs.tsv", ("sha256", "path_from_project"),
                    [(sha(p), p.relative_to(PROJECT)) for p in (KEY, NAMES, TOKENS, REFERENCE)])
        train()
    else:
        test()
