"""Compare possible base-shape repetitions with every letter offset in a text.

Input is either a Tanzil chapter|verse|text file or an OpenITI text. Coordinates
refer to sign-positions.png. The six optional equalities deliberately ignore
detached marks. A high score is a prompt for inspection, not a decipherment.
"""
import argparse
from collections import Counter
from pathlib import Path
import re

from check_passages import words


def lines(path):
    body = path.read_text(encoding="utf-8-sig")
    if re.search(r"(?m)^1\|1\|", body):
        chapters = {}
        for chapter, verse, text in re.findall(r"(?m)^(\d+)\|(\d+)\|(.+)$", body):
            chapters.setdefault(chapter, []).extend(words(text))
        return [(k, "".join(v)) for k, v in chapters.items()]
    body = body.split("#META#Header#End#")[-1]
    body = re.sub(r"PageV\d+P\d+|ms\d+", " ", body)
    return [(path.stem, "".join(words(body)))]


def optional(u, b):
    return (u[1] == u[7], b[2] == b[3], b[4] == b[-5],
            b[7] == b[-1], u[-3] == b[-2], u[-5] == u[-7] == u[8])


def find(text, upper_length, lower_length, lower_first):
    # Search physical right-to-left order. Reversing the source tests left-to-right.
    off_u, off_b = (lower_length, 0) if lower_first else (0, upper_length)
    for start in range(len(text) - upper_length - lower_length + 1):
        u, b = start + off_u, start + off_b
        if (text[u] != text[b + lower_length - 3]
                or text[u + 2] != text[u + upper_length - 2]
                or text[u + 8] != text[b]):
            continue
        upper = text[u:u + upper_length]
        lower = text[b:b + lower_length]
        yield start, upper, lower, optional(upper, lower)


def scan(path):
    scores = Counter()
    best, hits = -1, []
    for ref, original in lines(path):
        for reverse in (False, True):
            text = original[::-1] if reverse else original
            for lower_first in (False, True):
                for nu in range(19, 24):
                    for nb in range(20, 25):
                        for pos, u, b, mask in find(text, nu, nb, lower_first):
                            score = sum(mask)
                            scores[score] += 1
                            if score > best:
                                best, hits = score, []
                            if score == best and len(hits) < 10:
                                hits.append((ref, reverse, lower_first, nu, nb, pos, u, b, mask))
    print(path.name, sorted(scores.items()))
    for hit in hits:
        print(*hit)


if __name__ == "__main__":
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("texts", type=Path, nargs="+")
    # Construct a text from the proposed base-shape classes and recover it at
    # an internal offset under each line ordering.
    u, b = "ABCDEFG BJxyzwwJrJqHCA".replace(" ", ""), "JkllMnpIqrstuvwMxAHI"
    assert all(optional(u, b))
    for lower_first in (False, True):
        sample = "xx" + (b + u if lower_first else u + b) + "zz"
        assert any(pos == 2 and all(mask) for pos, _, _, mask in find(sample, len(u), len(b), lower_first))
    for path in args.parse_args().texts:
        scan(path)
