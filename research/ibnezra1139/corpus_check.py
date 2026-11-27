"""Find attested three-word phrases with the verso's exact equality pattern."""

import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from zipfile import ZipFile

from crib_check import pattern

FINALS = str.maketrans("ךםןףץ", "כמנפצ")


def normalize(word):
    return "".join(c for c in unicodedata.normalize("NFD", word)
                   if "א" <= c <= "ת").translate(FINALS)


def scan(path):
    variants = {}
    for tail in ("GG", "GH"):
        groups = ("ABCDE", "AC", "AF" + tail)
        for order, tokens in (
            ("rtl", groups),
            ("reverse-within", [g[::-1] for g in groups]),
            ("ltr", [g[::-1] for g in reversed(groups)]),
            ("reverse-groups", list(reversed(groups))),
        ):
            signature = tuple(map(len, tokens)), pattern("".join(tokens))
            variants[signature] = order, tail

    hits = defaultdict(lambda: defaultdict(set))
    free_hits = defaultdict(lambda: defaultdict(set))
    files = windows = 0
    with ZipFile(path) as corpus:
        print("PGP archive", corpus.comment.decode())
        for name in corpus.namelist():
            if not name.endswith("_transcription.txt") or "/9097/" in name:
                continue
            files += 1
            doc = Path(name).parent.name
            raw = corpus.read(name).decode("utf-8-sig")
            # Retain an empty token for headings, unknowns and editorial gaps.
            words = [normalize(w) if not any(c in w for c in "[].…") else ""
                     for w in raw.split()]
            # Allow any word divisions, keeping text direction uniform.
            # Equalities at indices 0,5,7 and 2,6 prune the test.
            for i, word in enumerate(words):
                if not word or len(word) > 11:
                    continue
                s = word
                end = i + 1
                while len(s) < 11 and end < len(words) and words[end]:
                    s += words[end]
                    end += 1
                if len(s) != 11:
                    continue
                for direction, t in (("rtl", s), ("ltr", s[::-1])):
                    if t[0] != t[5] or t[0] != t[7] or t[2] != t[6]:
                        continue
                    if pattern(t) not in ("ABCDEACAFGG", "ABCDEACAFGH"):
                        continue
                    # Full direction applies on the recto too. Use the
                    # five-letter crib trained there to predict indices 3,4.
                    # With the verso kept in photograph RTL coordinates,
                    # these indices are 400 and 40, in that order.
                    expected = "מת" if direction == "rtl" else "תמ"
                    if t[3:5] == expected:
                        free_hits[direction][" ".join(words[i:end])].add(doc)
            for i in range(len(words) - 2):
                phrase = tuple(words[i:i+3])
                lengths = tuple(map(len, phrase))
                if lengths not in ((5, 2, 4), (4, 2, 5)):
                    continue
                windows += 1
                label = variants.get((lengths, pattern("".join(phrase))))
                if label:
                    hits[label][phrase].add(doc)
    print("Transcription files:", files, "length-matched windows:", windows)
    for label in variants.values():
        print(label, len(hits[label]), "distinct phrases")
        for phrase, docs in sorted(hits[label].items()):
            print(" ", " ".join(phrase), ",".join(sorted(docs)))
    for direction in ("rtl", "ltr"):
        print(direction, "unrestricted word divisions plus first recto crib:",
              len(free_hits[direction]))
        for phrase, docs in sorted(free_hits[direction].items()):
            print(" ", phrase, ",".join(sorted(docs)))


if __name__ == "__main__":
    scan(sys.argv[1])
