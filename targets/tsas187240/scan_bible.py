"""Search an OSHB 2.2 release ZIP without crossing chapter boundaries."""

import argparse
from collections import Counter
from itertools import accumulate
from pathlib import PurePosixPath
import re
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from test_alphabet import B1, B2, FOLD


def chapters(archive):
    for path in sorted(archive.namelist()):
        if PurePosixPath(path).parent.as_posix() != "OSHB-v.2.2" or not path.endswith(".xml"):
            continue
        root = ET.fromstring(archive.read(path))
        for chapter in root.findall(".//{*}chapter"):
            words = []
            for verse in chapter.findall("{*}verse"):
                for node in verse.findall("{*}w"):
                    word = re.sub("[^א-ת]", "", "".join(node.itertext()))
                    if word:
                        words.append((word, verse.attrib["osisID"]))
            if words:
                yield words


def repeated_positions(signs):
    seen = {}
    pairs = []
    for pos, sign in enumerate(signs):
        if sign in seen:
            pairs.append((seen[sign], pos))
        seen[sign] = pos
    return pairs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive")
    parser.add_argument("--show", action="store_true", help="print three-boundary matches")
    parser.add_argument("--merge", type=int, nargs="+", choices=(5, 13), default=[],
                        help="tentatively classify these loop shapes with G03")
    parser.add_argument("--single-wave", action="store_true",
                        help="treat the adjacent G21 labels in B2 as one sign")
    parser.add_argument("--wide-gaps", action="store_true",
                        help="require word breaks at the two wide spaces shared by B1 and C1")
    parser.add_argument("--turn", action="store_true",
                        help="read the second row in the opposite direction from the first")
    parser.add_argument("--gap-shift", type=int, choices=range(-2, 3), default=0,
                        help="displace both wide-gap positions for a sensitivity check")
    args = parser.parse_args()
    if args.gap_shift and not args.wide_gaps:
        parser.error("--gap-shift requires --wide-gaps")
    totals = Counter()
    shapes = []
    second = tuple(sign for i, sign in enumerate(B2)
                   if not (args.single_wave and i and B2[i-1] == sign))
    for direction in (1, -1):
        for first in (B1, B1[1:]):
            left = first[::direction]
            right = second[::-direction] if args.turn else second[::direction]
            signs = [3 if sign in args.merge else sign for sign in left + right]
            shapes.append((len(left), direction, repeated_positions(signs)))
    with ZipFile(args.archive) as archive:
        for entries in chapters(archive):
            totals["chapters"] += 1
            words, refs = zip(*entries)
            original = "".join(words)
            text = original.translate(FOLD)
            boundaries = set(accumulate(map(len, words), initial=0))
            starts = dict(zip(sorted(boundaries), refs))
            totals["words"] += len(words)
            totals["letters"] += len(text)
            for middle, direction, pairs in shapes:
                length = middle + len(second)
                for start in range(len(text) - length + 1):
                    end = start + length
                    totals["placements"] += 1
                    if any(text[start+i] != text[start+j] for i, j in pairs):
                        continue
                    if args.wide_gaps:
                        gaps = (3 + args.gap_shift, 11 + args.gap_shift)
                        if direction == 1:
                            gaps = tuple(middle-gap for gap in gaps)
                        if any(start+gap not in boundaries for gap in gaps):
                            continue
                    totals["matches"] += 1
                    if start in boundaries and end in boundaries:
                        totals["outer boundaries"] += 1
                        if start + middle in boundaries:
                            totals["all boundaries"] += 1
                            if args.show:
                                print(starts[start], start, direction, original[start:start+middle],
                                      original[start+middle:end])
    for label, count in totals.items():
        print(label, count)


if __name__ == "__main__":
    main()
