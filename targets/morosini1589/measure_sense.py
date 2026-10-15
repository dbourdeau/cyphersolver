"""Sense measure for the F22b enclosures (R53, R54), with the Meister no. 40 records of morosini1588 as a control.

Input: the word-split public decryption bodies (decode_updates/decryptions/R<id>.txt, written by
../morosini1588/make_decryptions.py from the decoder output). A word counts as sense when its form occurs at least
twice in the it-cinquecento corpora (lang/corpora it-renaissance + it-nunziature, early normalisation: u/v, i/j
merged). Measured in letters: share of decoded letters that fall in attested words; '<nnn>' and '[?]' count as
unread. The word split is itself chosen by a language model, so a stretch of nonsense can still split into short
attested words: the figure is an upper bound, and the control shows what a fully read record of the same
correspondence scores.
usage: python measure_sense.py [R53 R54 ...]   (default: R53 R54 and the 34 Francia 22 Meister records)
"""
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, ROOT)
from lang import lm  # noqa: E402

V = collections.Counter()
for c in ('it-renaissance', 'it-nunziature'):
    V.update(lm.norm(open(os.path.join(ROOT, 'lang', 'corpora', c + '.txt'), encoding='utf-8').read(), 'early').split())
VOC = {w for w, n in V.items() if n >= 2}

MEISTER = [f'R{n}' for n in list(range(18, 23)) + list(range(27, 50)) + [51, 52, 55, 56, 57, 58]]


def measure(rec):
    path = os.path.join(ROOT, 'decode_updates', 'decryptions', rec + '.txt')
    ok = tot = 0
    for line in open(path, encoding='utf-8'):
        if line.startswith('[IMG'):
            continue
        for w in line.split():
            if w.startswith('<') or w == '[?]' or '[?]' in w:
                tot += max(1, len(re.sub(r'\[\?\]|<[^>]*>', '', w)))
                continue
            x = lm.norm(w, 'early').strip()
            if not x:
                continue
            tot += len(x)
            ok += len(x) if x in VOC else 0
    return ok, tot


def main():
    recs = sys.argv[1:] or ['R53', 'R54'] + MEISTER
    groups = collections.defaultdict(lambda: [0, 0])
    for r in recs:
        if not os.path.exists(os.path.join(ROOT, 'decode_updates', 'decryptions', r + '.txt')):
            print(r, 'no decryption file')
            continue
        ok, tot = measure(r)
        g = 'F22b' if r in ('R53', 'R54') else 'Meister no. 40 (control)'
        groups[g][0] += ok
        groups[g][1] += tot
        if g == 'F22b':
            print(f'{r}: {ok}/{tot} letters in attested words = {ok / tot:.3f}')
    for g, (ok, tot) in groups.items():
        print(f'{g}: {ok}/{tot} = {ok / tot:.3f}')


if __name__ == '__main__':
    main()
