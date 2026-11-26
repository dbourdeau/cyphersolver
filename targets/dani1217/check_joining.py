"""Test the 21+22 sign transcription against positional Arabic letter forms."""
from collections import Counter
from pathlib import Path
import re
import sys

TOP = "ABCDEFGbJk???mnoPqHCI"
BOTTOM = "JvLldfgTiU???sdyzdwAhT"
NON_FORWARD = set("اآأإٱدذرزوؤةء")
LETTERS = re.compile(r"[ء-غف-يٱ]+")


def forms(word):
    for i, letter in enumerate(word):
        left = i > 0 and word[i-1] not in NON_FORWARD and letter != "ء"
        right = i+1 < len(word) and letter not in NON_FORWARD and word[i+1] != "ء"
        yield (letter, left, right)


def search(body, pattern):
    tokens = LETTERS.findall(re.sub(r"[\u064b-\u065f\u0670\u0640]", "", body))
    seq = [form for word in tokens for form in forms(word)]
    visible = [i for i, c in enumerate(pattern) if c != "?"]
    pairs = [(pattern.index(pattern[i]), i) for i in visible if pattern.index(pattern[i]) != i]
    total = max(0, len(seq)-len(pattern)+1)
    repeats = strict = 0
    for start in range(total):
        if any(seq[start+a] != seq[start+b] for a,b in pairs):
            continue
        repeats += 1
        if len({seq[start+i] for i in visible}) == len(set(pattern)-{"?"}):
            strict += 1
    return Counter(windows=total, repeated=repeats, bijective=strict)


if __name__ == "__main__":
    assert list(forms("باب")) == [("ب",False,True),("ا",True,False),("ب",False,False)]
    assert search("باب باب", "ABCABC")["bijective"] == 1
    for name in sys.argv[1:]:
        raw = Path(name).read_text(encoding="utf-8-sig").split("#META#Header#End#")[-1]
        if re.search(r"(?m)^1\|1\|", raw):
            groups = {}
            for chapter, line in re.findall(r"(?m)^(\d+)\|\d+\|(.+)$", raw):
                groups.setdefault(chapter, []).append(line)
            texts = [" ".join(group) for group in groups.values()]
        else:
            texts = re.split(r"\n#+", re.sub(r"PageV\d+P\d+|ms\d+", " ", raw))
        for first, second in [(TOP,BOTTOM), (BOTTOM,TOP)]:
            for direction in [1,-1]:
                pattern = first[::direction] + second[::direction]
                counts = Counter()
                for passage in texts:
                    counts.update(search(passage, pattern))
                print(Path(name).name, "upper" if first == TOP else "lower", direction, dict(counts))
