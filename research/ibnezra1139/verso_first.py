"""Use attested verso phrases to predict the two recto words."""
from collections import defaultdict
import sys
from zipfile import ZipFile

from crib_check import R11, R12, V5
from joint_words import extend, token

positions = (0, 2, 3, 4, 5, 6, 7, 9)
signs = [V5[i] for i in positions]
if "--last-is-eight" in sys.argv[2:]:
    positions = (*positions[:-1], 10)
phrases = defaultdict(set)
stems, modifiers = set(), set()
with ZipFile(sys.argv[1]) as archive:
    for name in archive.namelist():
        if not name.endswith("_transcription.txt") or "/9097/" in name:
            continue
        words = [token(w) for w in archive.read(name).decode("utf-8-sig").split()]
        for w in words:
            for prefix in ("אל", "ואל"):
                if w.startswith(prefix) and len(w) == len(prefix) + 5:
                    stems.add(w[len(prefix):])
        modifiers.update(a for a,b in zip(words, words[1:]) if len(a)==4 and b=="כמא")
        for p in zip(words, words[1:], words[2:]):
            lengths = tuple(map(len,p))
            if lengths not in ((5,2,4),(4,2,5)):
                continue
            direction = 1 if lengths == (5,2,4) else -1
            oriented = "".join(p)[::direction]
            retained = "".join(oriented[i] for i in positions)
            key = extend({}, signs, retained)
            if key is not None:
                phrases[p,direction,retained].add(name.split("/")[-2])

for (phrase,direction,retained), docs in sorted(phrases.items()):
    key = extend({}, signs, retained)
    front_keys = [(w,extend(key,R11[::direction],w)) for w in stems]
    front_keys = [(w,k) for w,k in front_keys if k is not None]
    results = [(w,x) for w,k in front_keys for x in modifiers
               if extend(k,R12[::direction],x) is not None]
    print(phrase, sorted(docs), "article-compatible stems", len(front_keys),
          "complete matches",results)
