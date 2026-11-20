"""Compare the two frozen full-letter transcriptions and reproduce the joint text."""
import argparse
import csv
from dataclasses import dataclass
from difflib import SequenceMatcher
import hashlib
import io
from pathlib import Path
import re
import string

HERE = Path(__file__).resolve().parent
DIGESTS = {
    "reader_one/reading.tsv": "fc07d6be4f686ae15877cc9c526e705960d7d5df1a22d42435503e94fc80682b",
    "reader_one/NOTES.md": "81b0ae2c65001ec8677a194a07cfbf968b2c028b6a9515a3e72d92778629587c",
    "reader_two/reading.tsv": "8af5350609d770b114c066e9079984a71cfb2ba64b1ec46270a29cb14a9ddf29",
    "reader_two/NOTES.md": "0e7b443429a8f36c1546a9665dcfe869ce9a2adf6e747ed7782328f860c1f2bc",
}
LABELS = {
    "19": "Benjamin Franklin",
    "68": "James Bourdieu",
    "36": "American independence",
    "54": "Lord S. (Lord Shelburne)",
    "23": "French interests, exact wording unknown",
}
# Reader-two physical line numbers. Folio 1 includes the salutation and dateline.
CODE_LINES = {
    (1, 11): ["29"], (2, 11): ["21"], (2, 12): ["19"],
    (2, 14): ["55", "57", "68", "36"], (2, 15): ["54"],
    (2, 16): ["23"], (2, 19): ["56", "19"], (2, 20): ["67"], (2, 21): ["20"],
}
# Each bracketed passage is one editorial unit, even with nested uncertainty.
CHUNKS = re.compile(r"\[(?:[^\[\]]|\[(?:[^\[\]]|\[[^\[\]]*\])*\])*\]|⟨[^⟩]*⟩|[^\s\[⟨]+")
EDGE = (string.punctuation + "“”’‘—–").replace("&", "")
CODE = re.compile(r"(?<!\w)(\d+)(?!\w)")


@dataclass
class Unit:
    raw: str
    key: str
    display: str


def read_rows(label):
    # One uses literal unescaped quotation marks. Two uses TSV quoting.
    quote = csv.QUOTE_NONE if label == "one" else csv.QUOTE_MINIMAL
    path = HERE / f"reader_{label}/reading.tsv"
    with path.open(encoding="utf8", newline="") as f:
        rows = csv.DictReader(f, delimiter="\t", quoting=quote)
        return {(int(r["page"]), int(r["line"])): r["text"] for r in rows}


def units(text):
    result = []
    last_end = 0
    for match in CHUNKS.finditer(text):
        gap = " " if match.start() != last_end else ""
        last_end = match.end()
        raw = match.group()
        if raw.startswith("⟨") or raw.startswith("[inserted:"):
            inner = raw[1:-1] if raw.startswith("⟨") else raw[len("[inserted:"):-1].strip()
            key = "insert " + inner.rstrip(",.").casefold()
            display = "⟨" + inner + "⟩"
        elif raw.startswith("["):
            key = "mark " + raw.casefold()
            display = raw
        else:
            key = raw.strip(EDGE).casefold()
            display = raw
        if key:
            result.append(Unit(raw, key, display))
        elif result:
            # A bare quote/dash belongs to the printed line but has no word vote.
            result[-1].display += gap + raw
            result[-1].raw += gap + raw
    return result


def render_line(first, second, page, joint_line, line_a, line_b, apparatus):
    # Treat the marginal annotation's outer wrapper as a location, not a word.
    if (page, line_a) == (1, 35):
        prefix = "[interline at right, keyed ×: "
        assert first.startswith(prefix) and first.endswith("]")
        first = first[len(prefix):-1]
    a, b = units(first), units(second)
    compare = SequenceMatcher(None, [x.key for x in a], [x.key for x in b], autojunk=False)
    pieces = []
    for kind, i, j, k, m in compare.get_opcodes():
        if kind == "equal":
            pieces.extend(x.display for x in a[i:j])
            continue
        left = " ".join(x.raw for x in a[i:j])
        right = " ".join(x.raw for x in b[k:m])
        locus = f"T{len(apparatus)+1:03}"
        apparatus.append((locus, page, joint_line, line_a or "—", line_b or "—",
                          left or "∅", right or "∅"))
        # Preserve ordinary numerals at their line of occurrence despite uncertainty.
        visible = ""
        if (left, right) == ("[1782?]", "1782"):
            visible = " · 1782?"
        elif (left, right) == ("[¼?]", "½"):
            visible = " · ¼? / ½"
        elif left.startswith("[del:") and right.startswith("[cancelled:"):
            visible = " · includes cancelled ink"
        elif left.startswith("[") and left.endswith("?]") and left[1:-2].casefold() == right.casefold():
            visible = " · " + right + "?"
        elif (left, right) == ("[overwritten: sufficient]", "Sufficient"):
            visible = " · sufficient, overwriting disputed"
        elif (page, line_a) == (1, 1):
            visible = " · marginal mark"
        pieces.append("⟦" + locus + visible + "⟧")
    return " ".join(pieces)


def collate():
    for name, expected in DIGESTS.items():
        assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == expected, name
    one, two = read_rows("one"), read_rows("two")
    assert [sum(p == page for p, _ in one) for page in (1, 2, 3)] == [39, 35, 29]
    assert [sum(p == page for p, _ in two) for page in (1, 2, 3)] == [38, 35, 29]
    lines = ["# Henry Laurens to James Bourdieu, 10 August 1782", "",
             "Joint English reading of the three manuscript pages. A number in square "
             "brackets is followed by its documentary identification or a question mark. "
             "Double brackets mark uncertain transcription. The number beginning with T "
             "locates both readings in the apparatus. Angle brackets mark agreed insertions. "
             "The frozen passes preserve each reader’s punctuation and layout. "
             "[Variant apparatus](variants.tsv) · [Collation method](METHOD.md)", ""]
    apparatus, counted, seen_b = [], [], set()
    for (page, a_line), first in one.items():
        if a_line == 1:
            if page > 1:
                lines.append("")
            lines.extend([f"## Page {page}", ""])
        b_line = a_line if page != 1 else a_line - 1
        # Only reader one included the upper-right foliation.
        second = two[page, b_line] if b_line else ""
        if b_line:
            seen_b.add((page, b_line))
        joint = render_line(first, second, page, a_line, a_line, b_line, apparatus)
        where = (page, b_line)
        if where in CODE_LINES:
            expected = CODE_LINES[where]
            assert CODE.findall(first) == CODE.findall(second) == expected, where
            assert CODE.findall(joint) == expected, where

            def label(match):
                code = match.group()
                counted.append(code)
                return "[" + code + " · " + LABELS.get(code, "?") + "]"

            joint = CODE.sub(label, joint)
        if (page, a_line) == (1, 35):
            joint = "*Interlinear note*  " + joint
        # Nonbreaking spaces align line labels and leave the prose selectable.
        lines.append(f"**{a_line:02}.**  {joint}<br>")
    assert seen_b == set(two)
    assert counted == "29 21 19 55 57 68 36 54 23 56 19 67 20".split()
    assert sum(c in LABELS for c in counted) == 6
    lines.extend(["", "AI agents did this work; no person has checked it.", ""])
    out = io.StringIO()
    writer = csv.writer(out, delimiter="\t", lineterminator="\n")
    writer.writerow(["locus", "page", "joint_line", "reader_one_line",
                     "reader_two_line", "reader_one_variant", "reader_two_variant"])
    writer.writerows(apparatus)
    return {"joint.md": "\n".join(lines), "variants.tsv": out.getvalue()}, len(apparatus)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="replace the two derived files")
    args = parser.parse_args()
    outputs, count = collate()
    for name, text in outputs.items():
        path = HERE / name
        if args.write:
            path.write_bytes(text.encode("utf8"))
        elif path.read_bytes() != text.encode("utf8"):
            raise ValueError(f"Published collation differs from frozen passes: {name}")
    print(f"Full text: 3 pages, 103 / 102 witness lines, 103 joint lines, {count} variant loci.")
    print("All 13 code positions retained in place; six identified and seven open.")


if __name__ == "__main__":
    main()
