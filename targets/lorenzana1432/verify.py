"""Reproduce the readings, compare the December check with key permutations."""
import argparse
import csv
import random
from pathlib import Path

BASE = Path(__file__).resolve().parent

def rows(name):
    with (BASE / name).open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))

def decode(signs, key):
    return "".join(" " if s == " " else key.get(s, "?") for s in signs)

def distance(left, right):
    previous = list(range(len(right) + 1))
    for index, a in enumerate(left, 1):
        current = [index]
        for j, b in enumerate(right, 1):
            current.append(min(current[-1] + 1, previous[j] + 1,
                               previous[j - 1] + int(a != b)))
        previous = current
    return previous[-1]

def check_score(check, key):
    errors = 0
    for row in check:
        output = decode(row["signs"], key).split()
        gloss = row["gloss"].replace("v", "u").split()
        errors += sum(distance(a, b) for a, b in zip(output, gloss, strict=True))
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--controls", action="store_true")
    args = parser.parse_args()
    dec = {r["sign"]: r["value"] for r in rows("december-key.tsv")}
    additions = {r["sign"]: r["value"] for r in rows("april-key.tsv")}
    if dec.keys() & additions.keys():
        raise SystemExit("An April addition overwrites a December value")
    extended = {**dec, **additions}
    april = rows("april.tsv")
    report = []
    for row in april:
        signs = row["signs"]
        if set(signs) - (extended.keys() | {" ", "?"}):
            raise SystemExit(f"Unregistered sign on line {row['line']}")
        report.append(row["line"] + "\t" + decode(signs, extended))
    literal = "\n".join(report) + "\n"
    if literal != (BASE / "literal.tsv").read_text():
        raise SystemExit("Literal reading differs from the saved transcription or key")
    print(literal, end="")
    check = rows("december-check.tsv")
    for row in check:
        print("December", row["line"], decode(row["signs"], dec), sep="\t")
    if args.controls:
        rng = random.Random(1432)
        baseline = []
        values = list(dec.values())
        trials = 1000
        for _ in range(trials):
            rng.shuffle(values)
            baseline.append(check_score(check, dict(zip(dec, values, strict=True))))
        target = check_score(check, dec)
        denominator = sum(len(r["gloss"].replace(" ", "")) for r in check)
        print(f"December word-aligned edits {target}/{denominator}. Best shuffled {min(baseline)}. "
              f"Shuffles as good {sum(x <= target for x in baseline)}/{trials}.")
    signs = "".join(r["signs"].replace(" ", "") for r in april)
    print(f"April {len(signs)} sign positions, {sum(s in dec for s in signs)} under December key, "
          f"{len(set(signs))} distinct sign labels.")

if __name__ == "__main__":
    main()
