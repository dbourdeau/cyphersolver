"""Locate whole-word cribs with the repeat and spacing constraints of B1."""

from itertools import accumulate

from test_alphabet import B1, FOLD


def windows(words, first=B1, reverse_words=False, gaps=True):
    words = words.translate(FOLD).split()
    if reverse_words:
        words.reverse()
    limits = set(accumulate(map(len, words), initial=0))
    text = ''.join(words)
    for row in (first, first[1:]):
        for d in (1, -1):
            signs = row[::d]
            for start in sorted(limits):
                end = start + len(row)
                if end not in limits:
                    continue
                cuts = (start+3, start+11) if d == -1 else (end-3, end-11)
                if gaps and not all(i in limits for i in cuts):
                    continue
                pairs = list(zip(signs, text[start:end], strict=True))
                key = dict(pairs)
                if all(key[s] == c for s, c in pairs):
                    yield start, d, text[start:end], key
