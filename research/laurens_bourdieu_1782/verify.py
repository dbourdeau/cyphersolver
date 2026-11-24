"""Check the frozen readings, the positions in each comparison and the held-out register."""
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
    positions = [int(row["august_10_position"]) for row in parallels]
    assert positions == [3, 6, 7, 8, 9, 10, 11]
    for position, row in zip(positions, parallels):
        page, _, code = left[position - 1]
        assert page == 2 and code == row["august_10_number"]
        digits = re.findall(r"\b\d+\b", row["august_10_fragment"])
        assert digits == (["56", "19"] if position in (10, 11) else [code])
        assert row["august_7_fragment"].strip()
        expected_source = ("Richard Oswald", "2495") if position == 3 else ("Benjamin Franklin", "2497")
        assert (row["august_7_addressee"], row["august_7_leaf"]) == expected_source

    supplied = [row["august_10_number"] for row in parallels if row["comparison"] == "marked quotation"]
    assert supplied == ["68", "36", "54", "23"]
    assert parallels[-2]["august_7_fragment"] == parallels[-1]["august_7_fragment"]
    print("August 10: both readers agree on all 13 designations (12 distinct). Only 19 repeats.")
    print("Inside the marked quotation: 68, 36, 54, 23, in that order. Four positions.")
    print("The verifier checks numeric agreement and placement. The proposed senses depend on the manuscripts.")

    franklin_positions = [i for i, (_, _, code) in enumerate(left, start=1) if code == "19"]
    assert franklin_positions == [3, 11]
    for path in ("oswald_reading_a.txt", "oswald_reading_b.txt"):
        witness = (HERE / path).read_text(encoding="utf-8")
        assert "Franklin has been abundantly polite & kind" in witness
        assert "the 19" in witness and "has been abundtly polite" in witness
    print("The two 19s are positions 3 and 11. With positions 6–9, six positions are discussed as identified.")

    subprocess.run([sys.executable, "-I", "-B", str(HERE / "full_text/collate.py")],
                   check=True)

    later = HERE / "august_28"
    digests = {
        "PLAN.md": "8a03a6886f1a1796f6e66d287dc4e89baf3b637a10ec2554d9a2babafd40dd49",
        "reader_a.txt": "24df1d4eb6eccaf63aaae3c06822cebb5c3a0dd19df934b2a0213dba617db086",
        "reader_b.txt": "c9bb5fa6752c0362a95fbf9f00ca3756c22a41b3e329f44210280793582a7584",
    }
    for name, digest in digests.items():
        assert hashlib.sha256((later / name).read_bytes()).hexdigest() == digest, name
    for name, given_name in (("reader_a.txt", "Jones"), ("reader_b.txt", "James")):
        witness = (later / name).read_text(encoding="utf-8")
        start = witness.index("Wise Men may draw Conclusions")
        passage = witness[start:witness.index("\n\n", start)]
        assert re.findall(r"\b[0-9]+\b", passage) == ["45", "19", "68"]
        assert "i have lately heard from 19. seemingly a studied silence respecting the\nconcerns of 68." in passage.lower()
        assert given_name + " Bourdieu" in witness and "London" in witness
    print("August 28: the two readings agree on 45, 19 and 68 and the recurrence passage; the given name differs.")

    held = HERE / "heldout"
    digest = (held / "PLAN.sha256").read_text(encoding="utf-8").splitlines()[1].split()[0]
    assert hashlib.sha256((held / "PLAN.md").read_bytes()).hexdigest() == digest
    register = read("heldout/leaf_register.tsv")
    result = json.loads((held / "result.json").read_text(encoding="utf-8"))
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
