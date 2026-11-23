"""Compare the previously fixed alphabet to preselected groups in a separate letter."""
import csv
from hashlib import sha256
import json
from pathlib import Path
import random
import re

D = Path(__file__).resolve().parent
ROOT = D.parents[2]


def table(name):
    with (D / name).open(newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def verify(name):
    for line in (D / name).read_text().splitlines()[1:]:
        digest, location = line.split("  ", 1)
        assert sha256((ROOT / location).read_bytes()).hexdigest() == digest, location


def fold(text):
    return text.upper().replace("J", "I").replace("U", "V")


def run():
    verify("FREEZE.txt")
    verify("RUN_FREEZE.txt")
    assert not (D / "result.json").exists()
    assert not (D / "controls.tsv").exists()
    identifiers = "ABCDEFGHIJ"
    inputs = [table(n) for n in ("may_reader_a.tsv", "may_reader_b.tsv", "may_gloss.tsv")]
    assert all([r["group"] for r in records] == list(identifiers) for records in inputs)
    key = table("../nov20_william_transfer/alphabet.tsv")
    rows = {r["marker"]: str.maketrans(r["shift_row"], r["header"]) for r in key}
    alphabet = key[0]["header"]
    records = []
    for a, b, clear in zip(*inputs):
        left, right = (fold(row["reading"].strip()) for row in (a, b))
        gloss = clear["gloss"].strip()
        issue = []
        if left != right or not re.fullmatch(r"[A-Z]+[2468]", left):
            issue.append("incomplete or disagreeing stem, or selector missing")
        if any(c not in alphabet for c in left[:-1]):
            issue.append("unread or non-alphabetic stem")
        normal = re.sub(r"[^A-Z]", "", fold(gloss))
        if not normal or re.search(r"[?\[\]\d\s]", gloss):
            issue.append("missing or doubtful single-word gloss")
        output = "" if issue else left[:-1].translate(rows[left[-1]])
        records.append(dict(group=a["group"], a=a["reading"], b=b["reading"], gloss=gloss,
                            gloss_normal=normal, reasons=issue, output=output,
                            exact=bool(output) and output == normal))
    eligible = [r for r in records if not r["reasons"]]
    good = [r for r in eligible if r["exact"]]
    result = dict(eligible=len(eligible), whole_matches=len(good),
                  matched_letters=sum(len(r["output"]) for r in good), groups=records)
    if not eligible:
        result["status"] = "unscorable"
    else:
        rng = random.Random(15950510)
        controls = []
        for _ in range(1000):
            letters = list(alphabet)
            rng.shuffle(letters)
            perm = str.maketrans(alphabet, "".join(letters))
            controls.append(sum(r["output"].translate(perm) == r["gloss_normal"]
                                for r in eligible))
        result.update(control_max=max(controls), ties=controls.count(len(good)),
                      greater=sum(n > len(good) for n in controls))
        passed = len(good) >= 3 and result["matched_letters"] >= 12 and len(good) > max(controls)
        result["status"] = "pass" if passed else "miss"
        with (D / "controls.tsv").open("x") as file:
            file.write("replicate\texact_words\n")
            for i, n in enumerate(controls, start=1):
                file.write(f"{i}\t{n}\n")
    with (D / "result.json").open("x") as file:
        json.dump(result, file, indent=2)
        file.write("\n")
    print({k: v for k, v in result.items() if k != "groups"})


if __name__ == "__main__":
    run()
