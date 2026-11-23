"""Reproduce the published June score from text only. No network or file writes."""
import csv
import hashlib
import importlib.util
import json
import random
from pathlib import Path

DATA = Path(__file__).resolve().parent / "june"
RUN = DATA / "physical_reference"


def check(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_freezes():
    first = json.loads((DATA / "FREEZE.json").read_text())["sha256"]
    for name in ("PLAN.md", "alphabet.tsv", "boxes.tsv"):
        hashes = [v for k, v in first.items() if k.endswith("/" + name)]
        check(hashes == [digest(DATA / name)], "first freeze: " + name)
    for name in (DATA / "SCORER_FREEZE.txt", RUN / "FREEZE.txt", RUN / "RUN_FREEZE.txt"):
        for line in name.read_text().splitlines()[1:]:
            expected, relative = line.split("  ", 1)
            if relative.endswith(".png"):
                continue  # The published freeze preserves the image hash only.
            check(digest(DATA / relative) == expected, "freeze mismatch: " + relative)
    first_result = json.loads((DATA / "status.json").read_text())
    check(first_result["status"] == "stopped_before_substitution", "first status")
    check(first_result["controls_run"] == first_result["substitutions_applied"] == 0,
          "first test performed a substitution or control")
    check((DATA / "clear/reading.txt").read_bytes() == b"", "first reference is nonempty")


def main():
    verify_freezes()
    spec = importlib.util.spec_from_file_location("original_score", DATA / "score.py")
    score = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(score)
    result = json.loads((RUN / "result.json").read_text())
    consensus = score.agree(score.reader(DATA / "reader_a/reading.tsv"),
                            score.reader(DATA / "reader_b/reading.tsv"))
    check(consensus == result["consensus"], "reader consensus")
    eligible = [row for row in consensus if not row["reason"]]
    counts = [len(eligible), sum(c in score.LETTERS for row in eligible for c in row["stem"])]
    check(counts == [result["eligible_groups"], result["eligible_letters"]], "eligibility")

    reference = DATA / "clear/recovery_reading.txt"
    check(digest(reference) == result["reference_sha256"], "reference digest")
    annotated = []
    for line in reference.read_text().splitlines():
        label, body = line.split("\t", 1)
        for token in body.split():
            clean = "" if any(mark in token for mark in "?[]") else score.word(token)
            annotated.append((label, token, clean))
    words = [entry[2] for entry in annotated]
    check((len(words), sum(bool(word) for word in words)) ==
          (result["reference_words"], result["legible_reference"]), "reference counts")
    index = score.reference_index(words)
    rows = score.tsv(DATA / "alphabet.tsv")
    directions = {}
    for name, source, target in (("row_to_top", "shift_row", "header"),
                                 ("top_to_row", "header", "shift_row")):
        table = {row["marker"]: str.maketrans(row[source], row[target]) for row in rows}
        stream = {row["group"]: row["stem"].translate(table[row["marker"]]) for row in eligible}
        outcome = score.matches(stream, words, index)
        for match in outcome["matches"]:
            match["line"], match["literal"], _ = annotated[match["reference_word"] - 1]
        check(outcome == result["directions"][name], "recorded direction: " + name)
        directions[name] = stream
    generator = random.Random(15950615)
    observed = []
    for n in range(1, 1001):
        shuffled = list(score.LETTERS)
        generator.shuffle(shuffled)
        table = str.maketrans(score.LETTERS, "".join(shuffled))
        pair = []
        for stream in directions.values():
            remapped = {group: value.translate(table) for group, value in stream.items()}
            pair.append(score.matches(remapped, words, index)["score"])
        observed.append([n, *pair, max(pair)])
    with (RUN / "controls.tsv").open() as source:
        reader = csv.reader(source, delimiter="\t")
        check(next(reader) == ["replicate", "row_to_top", "top_to_row", "best"], "control columns")
        recorded = [[int(cell) for cell in row] for row in reader]
    check(observed == recorded, "control scores")
    winner = max(result["directions"], key=lambda name: score.rank(result["directions"][name]["matches"]))
    winning = result["directions"][winner]
    maximum = max(row[-1] for row in observed)
    passed = winning["score"] >= 12 and len(winning["matches"]) >= 3 and winning["score"] > maximum
    check((winner, winning["score"], maximum, passed) ==
          (result["best"], result["score"], result["control_max"], result["passed"]), "test outcome")
    check((sum(r[-1] == winning["score"] for r in observed), sum(r[-1] > winning["score"] for r in observed)) ==
          (result["tied"], result["higher"]), "control ties and exceedances")

    whole = {g: v for g, v in directions["row_to_top"].items() if "?" not in v}
    check(whole == {"C": "OVER", "D": "KILL", "J": "WRITE", "L": "SPAW"}, "complete words")
    print("First plan stopped before substitution. Secondary test: 8/12 eligible groups, 33 agreed letters.")
    print("Directional scores 16 and 0. Reproduced all 1,000 controls; maximum 9.")
    print("Complete outputs C OVER, D KILL, J WRITE, L SPAW. Physical alignment is documented separately.")


if __name__ == "__main__":
    main()
