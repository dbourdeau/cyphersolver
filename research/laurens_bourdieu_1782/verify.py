"""Compare the two original number readings and locate the four quoted designations."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
import subprocess
import sys
import re

HERE = Path(__file__).resolve().parent


def read(name):
    with (HERE / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def locations(rows, line_column):
    return [(int(row["page"]), int(row[line_column]), row["digits"]) for row in rows
            if row["classification"] == "isolated designation"]


def main():
    one = read("reader_one.tsv")
    two = read("reader_two.tsv")
    left = locations(one, "approx_prose_line")
    right = locations(two, "approx_line")
    if left != right:
        raise ValueError(f"Readers differ: {left!r} versus {right!r}")
    assert len(one) == len(two) == 17
    assert len(left) == 13
    counts = Counter(code for _, _, code in left)
    assert len(counts) == 12 and {k:v for k,v in counts.items() if v>1} == {"19":2}
    assert [item["digits"] for item in one if item["classification"]!="isolated designation"] == ["3","8","1/?","1000"]
    assert [item["digits"] for item in two if item["classification"]!="isolated designation"] == ["3","8","1/4","1000"]

    parallels = read("parallel.tsv")
    supplied = []
    for index, row in enumerate(parallels, 1):
        code = row["august_10_number"]
        assert int(row["sequence"]) == index
        assert re.findall(r"\b\d+\b", row["august_10_fragment"]) == [code]
        assert row["august_7_fragment"].strip()
        supplied.append(code)
    # Positions 6–9 follow “55 or 57”, in the quotation on page 2.
    assert [code for page,_,code in left[5:9] if page==2] == supplied == ["68","36","54","23"]
    print("August 10: both readers agree on all 13 designations (12 distinct). Only 19 repeats.")
    print("Inside the marked quotation: 68, 36, 54, 23, in that order. Four positions.")
    print("The verifier checks numeric agreement and placement. The proposed senses depend on the manuscripts.")

    franklin_positions = [i for i, (_, _, code) in enumerate(left, start=1) if code == "19"]
    assert franklin_positions == [3, 11]
    for path in ("oswald_reading_a.txt", "oswald_reading_b.txt"):
        witness = (HERE / path).read_text()
        assert "Franklin has been abundantly polite & kind" in witness
        assert "the 19" in witness and "has been abundtly polite" in witness
    print("The two 19s are positions 3 and 11. With positions 6–9, six positions are discussed as identified.")

    subprocess.run([sys.executable, "-I", "-B", str(HERE / "full_text/collate.py")],
                   check=True)

    held = HERE / "heldout"
    digest = (held / "PLAN.sha256").read_text().splitlines()[1].split()[0]
    assert hashlib.sha256((held / "PLAN.md").read_bytes()).hexdigest() == digest
    register = read("heldout/leaf_register.tsv")
    result = json.loads((held / "result.json").read_text())
    packets = {r["packet"] for r in register}
    eligible = [r for r in register if r["eligible_region"] != "none"]
    assert len(packets) == result["packets"] == 6
    assert len(register) == len({r["leaf"] for r in register}) == result["listed_images_checked"] == 21
    assert len(eligible) == result["images_with_eligible_text"] == 9
    assert {r["packet"] for r in eligible} == packets
    assert all(int(r["potential_codes_in_target"]) == 0 for r in eligible)
    assert result["predicted_designator_occurrences"] == {code:0 for code in supplied}
    assert result["scorable_assignments"] == result["shuffles_run"] == 0
    assert result["other_personal_designations"] == [{"number":44,"leaf":2994,"identity":None}]
    print("Held out: six packets, 21 images, nine with eligible text. Zero recurrences of the four codes; no shuffle run.")


if __name__ == "__main__":
    main()
