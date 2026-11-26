"""Test word-bounded passages against three putative sign recurrences in fig. 69.

Usage: python check_passages.py quran.txt openiti-taysir.txt
Neither model is a recovered key. The strict model assumes a simple substitution.
"""
import argparse
from collections import Counter
from pathlib import Path
import re
import unicodedata
import xml.etree.ElementTree as ET
import zipfile

LETTERS = re.compile(r"[ء-غف-ي]+")
NORMALIZE = str.maketrans("أإآٱىؤئ", "اااايوي")


def words(text):
    text = re.sub(r"[\u064b-\u065f\u0670\u0640]", "", text)
    return LETTERS.findall(text.translate(NORMALIZE))


def tests(upper, lower):
    # Coordinates refer to the 1313-pixel title-page crop, in physical order.
    # Upper R1 (x1177) = lower L3 (x207): S with curled ends.
    # Upper R3 (x1060) = upper L2 (x168): capped hourglass.
    # Upper R9 (x713) = lower R1 (x1165): 9-shaped sign.
    if not (upper[0] == lower[-3] and upper[2] == upper[-2]
            and upper[8] == lower[0]):
        return None
    if len(set(upper[:7])) != 7 or len(set(lower[-5:])) != 5:
        return "recurrences only"
    # Distinguish readily dissimilar bases, leaving upper R2/R8 unresolved.
    bases = upper[:7] + upper[8] + lower[1] + lower[-5:-3] + lower[-2:]
    return "distinct bases" if len(set(bases)) == len(bases) else "line ends"


def passages(tokens):
    for begin in range(len(tokens)):
        letters = ""
        for end in range(begin, min(begin + 48, len(tokens))):
            letters += tokens[end]
            if len(letters) > 48:
                break
            if len(letters) >= 38:
                yield letters, " ".join(tokens[begin:end + 1])


def run(label, groups):
    counts = Counter()
    strict = set()
    examined = 0
    for reference, tokens in groups:
        for phrase, display in passages(tokens):
            examined += 1
            for split in range(max(17, len(phrase) - 26), min(26, len(phrase) - 17) + 1):
                upper, lower = phrase[:split], phrase[split:]
                for direction, a, b in (("RTL", upper, lower), ("LTR", upper[::-1], lower[::-1]),
                                        ("lower first RTL", lower, upper), ("lower first LTR", lower[::-1], upper[::-1])):
                    result = tests(a, b)
                    if result:
                        counts[direction, result] += 1
                        if result == "distinct bases":
                            # Distinct in the plate: upper L1 is a stepped upright, lower R3/R4
                            # are upstrokes. Neither resembles the upper R3 capped hourglass.
                            check = "passes holdout" if (a[-1] not in (a[0], a[6])
                                                       and a[2] not in (b[2], b[3])) else "fails holdout"
                            strict.add((direction, split, reference, check, display))
    print(label, examined, "word-bounded windows")
    for direction in ("RTL", "LTR", "lower first RTL", "lower first LTR"):
        print(direction, [counts[direction, k] for k in ("recurrences only", "line ends", "distinct bases")])
    for row in sorted(strict):
        print(" | ".join(map(str, row)))


def fihrist_entries(archive):
    tags = {"colophon", "provenance", "additions", "explicit", "incipit", "seal"}
    seen = set()
    with zipfile.ZipFile(archive) as bundle:
        for member in bundle.namelist():
            if not ("/collections/" in member and member.endswith(".xml")):
                continue
            document = ET.fromstring(bundle.read(member))
            for node in document.iter():
                if node.tag.rsplit("}", 1)[-1] not in tags:
                    continue
                passage = " ".join(node.itertext()).translate(str.maketrans("کی", "كي"))
                passage = re.sub(r"[\u064b-\u065f\u0670\u0640]", "", passage).translate(NORMALIZE)
                passage = "".join(" " if unicodedata.category(c).startswith("P") else c for c in passage)
                chunks = []
                # Break the passage when a word contains an unmodelled letter. Dropping
                # that letter alone would make a fictitious Arabic word from Persian.
                for token in passage.split():
                    if LETTERS.fullmatch(token):
                        chunks.append(token)
                    elif chunks:
                        chunks.append(None)
                chunks.append(None)
                start = 0
                for i, chunk in enumerate(chunks):
                    if chunk is None:
                        tokens = tuple(chunks[start:i])
                        start = i + 1
                        if sum(map(len, tokens)) >= 38 and tokens not in seen:
                            seen.add(tokens)
                            yield member.rsplit("/", 1)[-1], tokens


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("quran", type=Path)
    parser.add_argument("taysir", type=Path)
    parser.add_argument("--fihrist", type=Path)
    parser.add_argument("--openiti", type=Path, action="append", default=[],
                        help="Additional OpenITI text to search within paragraphs")
    args = parser.parse_args()
    verses = []
    for line in args.quran.read_text(encoding="utf-8-sig").splitlines():
        match = re.fullmatch(r"(\d+)\|(\d+)\|(.+)", line)
        if match:
            verses.append((f"{match[1]}:{match[2]}", words(match[3])))
    assert len(verses) == 6236
    assert tests("abcdefghijabcdefghcX", "ijabcdefgklamn") == "distinct bases"
    run("Quran (within single verses)", verses)
    chapters = {}
    for ref, tokens in verses:
        chapters.setdefault(ref.split(":")[0], []).extend(tokens)
    run("Quran (including passages across verse boundaries)", chapters.items())
    text = args.taysir.read_text(encoding="utf-8-sig").split("#META#Header#End#")[1]
    run("Taysir (within OpenITI paragraphs)", [(str(n), words(p)) for n, p in enumerate(re.split(r"\n#+", text))])
    run("Taysir (including passages across paragraph boundaries)", [("text", words(text))])
    # These are text strings available from the description, title page, and colophon.
    # Variants model explicitly identified names and titles, not an arbitrary name list.
    readings = [
        "كتاب التيسير في القراءات السبعة تأليف الشيخ الإمام الحافظ أبي عمرو عثمان بن سعيد بن عثمان المقرئ الداني",
        "كتاب التيسير في القراءات السبع تأليف الشيخ الإمام الحافظ أبي عمرو عثمان بن سعيد بن عثمان المقرئ الداني",
        "كتاب التيسير في القراءات السبع لأبي عمرو عثمان بن سعيد بن عثمان المقرئ الداني",
        "العبد المسرف الراجي عفو الله الكريم أبو سعيد بن حميد الشافعي المقرئ",
        "كتبه العبد المسرف الراجي عفو الله الكريم أبو سعيد بن حميد الشافعي المقري",
        "تم الكتاب المبارك بعون الله تعالى ومنه في الحادي والعشرين من شهر ربيع الآخر من شهور سنة خمس عشرة وست مائة",
    ]
    run("Manuscript-based title, author, signature and date variants", [(str(i), words(s)) for i, s in enumerate(readings)])
    if args.fihrist:
        run("Fihrist Arabic-script colophons, provenance, additions, explicit, incipit, seals", fihrist_entries(args.fihrist))
    for path in args.openiti:
        body = path.read_text(encoding="utf-8-sig").split("#META#Header#End#")[-1]
        run(path.name, ((str(i), words(re.sub(r"PageV\d+P\d+", " ", p)))
                        for i, p in enumerate(re.split(r"\n#+", body))))
