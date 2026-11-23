"""Undo Verkehrsbuch Schieber I on the middle three digits."""
import argparse
import csv
from pathlib import Path

STRIPS = ("4709263581", "6273508194", "9083465271")
KEY = "376"


def transform(group, key=KEY, *, encode=False):
    """Preserve the outer digits and any '?' in a damaged group."""
    if len(group) != 5 or any(digit not in "0123456789?" for digit in group):
        raise ValueError(f"Expected a five-position group, got {group!r}")
    result = list(group)
    for position, (strip, setting) in enumerate(zip(STRIPS, key), start=1):
        digit = group[position]
        if digit == "?":
            continue
        offset = strip.index(setting)
        if encode:
            result[position] = strip[(int(digit) + offset) % 10]
        else:
            result[position] = str((strip.index(digit) - offset) % 10)
    return "".join(result)


def verify_reading():
    path = Path(__file__).with_name("reading.tsv")
    with path.open(encoding="utf-8-sig", newline="") as source:
        rows = list(csv.DictReader(source, delimiter="\t"))
    assert len(rows) == 43
    assert transform("51712", "718", encode=True) == "50532"
    for row in rows:
        group = row["tested_cipher"]
        code = transform(group)
        assert code == row["vb_number"], row
        assert transform(code, encode=True) == group, row
    return rows


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("groups", nargs="*")
    args = cli.parse_args()
    if args.groups:
        for group in args.groups:
            print(group, transform(group))
    else:
        for row in verify_reading():
            print(row["index"], row["tested_cipher"], row["vb_number"], row["reading"])
