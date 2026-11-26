"""Look for exact continuous matches allowing unknown signs at the damaged ends."""

import argparse
from itertools import product
from pathlib import Path
import re

from check_readings import ROWS


def expression(signs):
    seen = set()
    parts = []
    for sign in signs:
        if sign == "?":
            parts.append(".")
        elif sign in seen:
            parts.append(f"(?P={sign})")
        else:
            parts.append(f"(?P<{sign}>.)")
            seen.add(sign)
    return re.compile("(?=(" + "".join(parts) + "))")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", type=Path, help="UTF-8 plain text")
    parser.add_argument("--max-gap", type=int, default=3, choices=range(4))
    args = parser.parse_args()
    text = args.text.read_text(encoding="utf8").lower()
    text = text.replace("æ", "ae").replace("œ", "oe").replace("v", "u").replace("j", "i")
    text = re.sub("[^a-z]", "", text)
    print(len(text), "normalized letters")
    for gap1, gap2 in product(range(args.max_gap + 1), repeat=2):
        lines = (ROWS[0] + "?" * gap1, ROWS[1] + "?" * gap2, ROWS[2])
        for steps in product((1, -1), repeat=3):
            signs = "".join(row[::step] for row, step in zip(lines, steps))
            for hit in expression(signs).finditer(text):
                print(gap1, gap2, steps, hit.start(), hit[1])


if __name__ == "__main__":
    main()
