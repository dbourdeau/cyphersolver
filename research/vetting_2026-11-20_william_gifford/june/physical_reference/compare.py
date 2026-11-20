"""Secondary test against two physically specified English manuscript crops."""
import hashlib
import importlib.util
import json
from pathlib import Path
import random
import re

OUT = Path(__file__).resolve().parent
DATA = OUT.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    for line in (OUT / "FREEZE.txt").read_text().splitlines()[1:]:
        expected, path = line.split("  ", 1)
        assert sha(DATA / path) == expected, path
    spec = importlib.util.spec_from_file_location("registered", DATA / "score.py")
    original = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(original)
    reference_file = DATA / "clear/recovery_reading.txt"
    annotated = []
    for line in reference_file.read_text().splitlines():
        if not line.strip():
            continue
        label, body = line.split("\t", 1)
        assert re.fullmatch(r"128[rv]-\d+", label), label
        for literal in body.split():
            clean = "" if any(c in literal for c in "?[]") else original.word(literal)
            annotated.append((label, literal, clean))
    words = [entry[2] for entry in annotated]
    assert not (OUT / "result.json").exists()
    assert not (OUT / "controls.tsv").exists()
    assert (OUT / "RUN_FREEZE.txt").exists()
    for line in (OUT / "RUN_FREEZE.txt").read_text().splitlines()[1:]:
        expected, path = line.split("  ", 1)
        assert sha(DATA / path) == expected, path
    readings = [original.reader(DATA / f"reader_{r}/reading.tsv") for r in "ab"]
    agreed = original.agree(*readings)
    eligible = [item for item in agreed if not item["reason"]]
    count = sum(sum(c in original.LETTERS for c in item["stem"]) for item in eligible)
    result = dict(reference_sha256=sha(reference_file), consensus=agreed,
                  reference_words=len(words), legible_reference=sum(bool(w) for w in words),
                  eligible_groups=len(eligible), eligible_letters=count)
    if len(eligible) < 5 or count < 18 or result["legible_reference"] < 60:
        result["status"] = "insufficient inputs"
    else:
        index = original.reference_index(words)
        table = original.tsv(DATA / "alphabet.tsv")
        streams, scores = {}, {}
        for direction, source, target in (("row_to_top", "shift_row", "header"),
                                           ("top_to_row", "header", "shift_row")):
            rows = {r["marker"]: str.maketrans(r[source], r[target]) for r in table}
            streams[direction] = {e["group"]: e["stem"].translate(rows[e["marker"]])
                                  for e in eligible}
            scores[direction] = original.matches(streams[direction], words, index)
            for match in scores[direction]["matches"]:
                match["line"], match["literal"], _ = annotated[match["reference_word"] - 1]
        best = max(scores, key=lambda name: original.rank(scores[name]["matches"]))
        score = scores[best]["score"]
        generator = random.Random(15950615)
        controls = []
        for i in range(1000):
            shuffled = list(original.LETTERS)
            generator.shuffle(shuffled)
            remap = str.maketrans(original.LETTERS, "".join(shuffled))
            pair = []
            for sequence in streams.values():
                shifted = {group: value.translate(remap) for group, value in sequence.items()}
                pair.append(original.matches(shifted, words, index)["score"])
            controls.append((i + 1, *pair, max(pair)))
        maximum = max(row[-1] for row in controls)
        result.update(status="scored", directions=scores, best=best, score=score,
                      passed=score >= 12 and len(scores[best]["matches"]) >= 3 and score > maximum,
                      control_max=maximum, tied=sum(row[-1] == score for row in controls),
                      higher=sum(row[-1] > score for row in controls))
        with (OUT / "controls.tsv").open("x") as file:
            file.write("replicate\trow_to_top\ttop_to_row\tbest\n")
            for row in controls:
                file.write("\t".join(map(str, row)) + "\n")
    with (OUT / "result.json").open("x") as file:
        json.dump(result, file, indent=2)
        file.write("\n")
    print({k: v for k, v in result.items() if k not in ("directions", "consensus")})


if __name__ == "__main__":
    run()
