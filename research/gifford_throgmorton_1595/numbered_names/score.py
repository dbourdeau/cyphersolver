"""Score only the registered numeral/gloss comparison. Do not decode unglossed names."""
from collections import defaultdict
from pathlib import Path
import csv
import hashlib
import json
import random
import re
import unicodedata

HERE = Path(__file__).resolve().parent
REGIONS = {"19r_middle", "37r_lower", "37v_middle"}


def clean(value):
    letters = unicodedata.normalize("NFKD", value).casefold()
    return "".join(c for c in letters if c.isalpha())


def rows(name):
    with (HERE / name).open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source, delimiter="\t"))


def parse_readers(filename):
    sure = defaultdict(list)
    rejected = []
    for row in rows(filename):
        region = Path(row["region"].strip()).stem
        num = row["numeral"].strip()
        gloss = row["gloss"].strip()
        line = row["line"].strip()
        if (region not in REGIONS or not re.fullmatch(r"[0-9]{2,3}", num)
                or row["certainty"].strip().lower() != "sure"
                or not clean(gloss) or any(c in gloss for c in "?[]")
                or not line.isdecimal()):
            rejected.append(row)
            continue
        sure[(region, num)].append((int(line), clean(gloss), gloss))
    return sure, rejected


def main():
    lock = (HERE / "FREEZE.txt").read_text().splitlines()[1:]
    for row in lock:
        value, path = row.split("  ", 1)
        assert hashlib.sha256((HERE / path).read_bytes()).hexdigest() == value
    assert not (HERE / "result.json").exists()
    fixed = rows("aliases.tsv")
    labels = {r["number"]: set(map(clean, r["normalized_aliases"].split("|"))) for r in fixed}
    a, rejected_a = parse_readers("reader_a.tsv")
    b, rejected_b = parse_readers("reader_b.tsv")
    paired = []
    unmatched = []
    for item in sorted(set(a) | set(b)):
        region, number = item
        aa, bb = a.get(item, []), b.get(item, [])
        for line, name, diplomatic in aa:
            partners = [(other, word) for other, word, _ in bb if other == line and word == name]
            # A difference of one in counting a clipped line is allowed only when
            # both report exactly one occurrence of this number in the entire region.
            if (not partners and len(aa) == len(bb) == 1
                    and abs(bb[0][0] - line) == 1 and bb[0][1] == name):
                partners = [(bb[0][0], bb[0][1])]
            if len(partners) == 1:
                paired.append(dict(region=region, line_a=line, line_b=partners[0][0],
                                   number=number, gloss=diplomatic, normalized=name))
            else:
                unmatched.append(dict(region=region, number=number, line_a=line, gloss=diplomatic))
    by_number = defaultdict(set)
    for item in paired:
        if item["number"] in labels:
            by_number[item["number"]].add(item["normalized"])
    # One score per distinct number. Conflicting testimonies can never score.
    nums = list(labels)
    def count(assignments):
        return sum(len(words) == 1 and words <= labels[assignments[n]]
                   for n, words in by_number.items())
    correct = count({n:n for n in nums})
    contradictions = sorted(n for n, words in by_number.items() if not words <= labels[n] or len(words) != 1)
    controls = []
    status = "unscorable"
    if by_number:
        rng = random.Random(15950519)
        for i in range(1000):
            order = nums[:]
            rng.shuffle(order)
            controls.append(count(dict(zip(nums, order))))
        status = "pass" if correct >= 3 and not contradictions and correct > max(controls) else "miss"
    result = dict(status=status, correct=correct, matched_numbers=dict((n,sorted(x)) for n,x in by_number.items()),
                  contradictions=contradictions, paired=paired, no_partner_from_a=unmatched,
                  uncertain_or_unusable_a=rejected_a, uncertain_or_unusable_b=rejected_b,
                  controls=len(controls), maximum=max(controls,default=None),
                  ties=controls.count(correct), higher=sum(c>correct for c in controls))
    (HERE/"result.json").write_text(json.dumps(result,indent=2)+"\n")
    if controls:
        (HERE/"controls.tsv").write_text("replicate\tcorrect\n"+"".join(f"{i}\t{x}\n" for i,x in enumerate(controls,1)))
    print({k:v for k,v in result.items() if k not in {"uncertain_or_unusable_a","uncertain_or_unusable_b","no_partner_from_a","paired"}})


if __name__ == "__main__":
    main()
