"""Recompute the six-by-six comparison of already aligned witnesses. Read-only."""
import csv
import re
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROUGH = HERE.parent / "wainut" / "decryption_philip_1546_1553_x_blind.txt"
BLOCKS = ((1, 15), (16, 21), (22, 40), (41, 47), (48, 55), (56, 64))


def normalize(text):
    text = unicodedata.normalize("NFKD", text.lower()).translate(str.maketrans("vj", "ui"))
    return re.sub("[^a-z]", "", text).replace("sumagestad", "")


def distance(left, right):
    row = list(range(len(right) + 1))
    for i, first in enumerate(left, 1):
        following = [i]
        for j, second in enumerate(right, 1):
            following.append(min(row[j] + 1, following[-1] + 1, row[j - 1] + (first != second)))
        row = following
    return row[-1]


def main():
    lines = {}
    for number, content in re.findall(r"^B-(\d+) (.*)$", ROUGH.read_text(), re.MULTILINE):
        number = int(number)
        if number in lines:
            raise ValueError(f"Duplicate cipher line {number}")
        lines[number] = re.sub(r"\[[^\]]*\]", "", content)
    text = (HERE / "spanish_enclosure.txt").read_text().split("[37r]\n", 1)[1]
    # Each leaf heading interrupts a paragraph, with a blank line before the heading.
    text = re.sub(r"\n\s*\[(?:37v|38r)\]\s*\n", " ", text)
    paragraphs = [normalize(p) for p in re.split(r"\n\s*\n", text.strip())]
    if len(paragraphs) != len(BLOCKS):
        raise ValueError(f"Expected six paragraphs, found {len(paragraphs)}")
    with (HERE / "paragraph_correspondence.tsv").open() as source:
        expected = list(csv.reader(source, delimiter="\t"))
    table = [["prior_rough_lines", *[f"clear_para_{i}" for i in range(1, 7)]]]
    for index, (start, stop) in enumerate(BLOCKS):
        left = normalize("".join(lines[i] for i in range(start, stop + 1)))
        scores = [1 - distance(left, p) / max(len(left), len(p)) for p in paragraphs]
        if scores[index] <= max(score for j, score in enumerate(scores) if j != index):
            raise ValueError(f"Assigned paragraph is not the unique closest for B{start}–{stop}")
        table.append([f"{start}-{stop}", *[f"{s:.4f}" for s in scores]])
    if table != expected:
        raise ValueError("Recomputed values differ from paragraph_correspondence.tsv")
    print("All 36 similarities reproduced. The assigned paragraph ranks first in each of six rows.")
    print("Boundaries were chosen after inspection. This comparison credits no new cipher words.")


if __name__ == "__main__":
    main()
