"""Replay the earlier c. 76r alphabet on the c. 78r digit stream."""

import csv
import re
from pathlib import Path

TARGET = Path(__file__).resolve().parents[1]
EARLIER_KEY = TARGET / "key_76r.tsv"

# Ordinary letter values supported by the adjacent cipher/plaintext pairs.
# c. 77r: costui and offerendo. c. 147r/148r: fussino.
SIBLING_LETTERS = {"45": "t", "31": "f", "02": "u"}


def decode(line, alphabet):
    runs = re.split(r"<CLEAR:.*?>|⟨.*?⟩", line)
    decoded = []
    for run in runs:
        digits = re.sub(r"[^0-9]", "", run)
        if not digits:
            continue
        tokens = re.findall(r"[689]|[0123457][0-9]?", digits)
        decoded.append("".join(alphabet.get(token, "·") for token in tokens))
    return " | ".join(decoded)


def main():
    with EARLIER_KEY.open(encoding="utf-8") as source:
        rows = csv.DictReader((r for r in source if not r.startswith("#")), delimiter="\t")
        earlier = {row["code"]: row["values"].split(" / ")[0] for row in rows}

    source = (TARGET / "transcription_78r.txt").read_text(encoding="utf-8")
    for title, key in [("Earlier key alone", earlier),
                       ("Earlier key plus three sibling letters", {**earlier, **SIBLING_LETTERS})]:
        print(title)
        for line in source.splitlines():
            m = re.match(r"^(L\d{2})[:\s]+(.*)$", line.strip())
            if m:
                print(m.group(1), decode(m.group(2), key))
        print()


if __name__ == "__main__":
    main()
