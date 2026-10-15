"""Inventory DECODE's marked-digit transcription of R1893."""

from collections import Counter
from pathlib import Path
import re


source = (Path(__file__).parent / ".." / "vanreede1787" / "decode" / "DOC_R1893_D3608_3608.txt").read_text(
    encoding="utf-8", errors="replace"
)
source = re.sub(r"(\d)\s+\^", r"\1^", source)

groups = []
for line in source.splitlines():
    if line.startswith("#") or line.startswith("<"):
        continue
    for raw in re.split(r"\.\s+", line):
        digits = re.findall(r"(\d)(?:\^([~v=¨+]))?", raw)
        if len(digits) not in (1, 2, 3):
            continue
        number = "".join(digit for digit, _ in digits)
        marks = "".join(mark or "." for _, mark in digits)
        groups.append((number, marks, raw.strip()))

print("tokens", len(groups), "distinct", len(set((n, m) for n, m, _ in groups)))
print("mark patterns")
for pattern, count in Counter(m for _, m, _ in groups).most_common():
    print(pattern, count)
print("first 80")
for number, marks, _ in groups[:80]:
    print(f"{number}:{marks}", end=" ")
print()

print("canonical markers")
for marker, count in Counter(next((mark for mark in marks if mark != "."), "") for _, marks, _ in groups).most_common():
    print(marker or "none", count)
