"""Rebuild the consensus from both sign readers' positions. No images required."""

import csv
from pathlib import Path


DIRECTORY = Path(__file__).resolve().parent


def read_table(name):
    with (DIRECTORY / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def read_pass(name):
    lines = {}
    for row in read_table(name):
        positions = lines.setdefault(row["line"], {})
        x = int(row["x"])
        if x in positions:
            raise ValueError(f"Duplicate position in {name}, row {row['line']}, x={x}")
        label = row["symbol"].strip()
        if label.isdigit():
            label = label.zfill(2)
        positions[x] = "05" if label == "15" else label
    return lines


def nearest(x, positions):
    distance = min(abs(y - x) for y in positions)
    nearest_positions = [y for y in positions if abs(y - x) == distance]
    if len(nearest_positions) == 1 and distance <= 14:
        return nearest_positions[0]
    return None


def compare_line(first, second):
    slots = []
    paired = set()
    for x, a in first.items():
        y = nearest(x, second)
        if y is None or nearest(y, first) != x:
            slots.append((x, x, "", a, "", "?"))
            continue
        paired.add(y)
        b = second[y]
        agreed = a if a == b and a and "?" not in a else "?"
        slots.append(((x + y) / 2, x, y, a, b, agreed))
    for y, b in second.items():
        if y not in paired:
            slots.append((y, "", y, "", b, "?"))
    return sorted(slots, key=lambda slot: slot[0])


def main():
    first = read_pass("pass_a.tsv")
    second = read_pass("pass_b.tsv")
    lines = [f"U{i:02}" for i in range(1, 9)] + [f"L{i:02}" for i in range(1, 10)]
    if set(first) != set(lines) or set(second) != set(lines):
        raise ValueError("A reading has missing or unexpected rows")
    rebuilt = [(line, *map(str, slot)) for line in lines
               for slot in compare_line(first[line], second[line])]
    fields = ("line", "center", "x_a", "x_b", "a", "b", "agreed")
    recorded = [tuple(row[field] for field in fields) for row in read_table("consensus.tsv")]
    if rebuilt != recorded:
        raise ValueError("The two passes do not reproduce the recorded consensus")
    labels = [row[-1] for row in rebuilt if row[-1] != "?"]
    print(f"{len(rebuilt)} slots, {len(labels)} agreed positions, {len(set(labels))} agreed labels.")


if __name__ == "__main__":
    main()
