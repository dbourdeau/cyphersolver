#!/usr/bin/env python3
"""eaglepass1917: strict word and letter counts (standard library only).
Run from the repository root:  python3 -I targets/eaglepass1917/count_words.py
A word is clean when key.tsv, applied to its cipher letters in transcription.txt (first readings), gives the word of
reading.md (accents folded) letter for letter. The extra cipher letter in "falsas" is charged to that word, so it is a
hole (docs/_replay.py charges it to the gap instead and counts 27 words). Also prints the counts under the doubtful
readings named in NOTES.md (cipher positions 1-based)."""
import os, re, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda f: os.path.join(HERE, f)

key = {}
for line in open(P('key.tsv'), encoding='utf-8'):
    f = line.rstrip('\n').split('\t')
    if line.startswith('#') or f[0] == 'cipher' or len(f) < 2: continue
    key[f[0]] = f[1]
cipher = ''
for line in open(P('transcription.txt'), encoding='utf-8'):
    if line.startswith('L'):
        cipher += re.sub(r'\[(\w)/\w\]', r'\1', line.split('\t')[1]).replace('/', '').replace(' ', '').strip()
text = open(P('reading.md'), encoding='utf-8').read().split('<!-- replay -->')[1].split('<!-- /replay -->')[0]
fold = lambda w: unicodedata.normalize('NFD', w).encode('ascii', 'ignore').decode().lower()
words = [fold(w).replace('[', '').replace(']', '') for w in re.findall(r"[^\W\d_\[\]]*(?:\[[^\]]+\][^\W\d_\[\]]*)+|[^\W\d_]+", text)]
EXTRA = {'falsas': 1}          # one extra cipher letter typed in this word (the N of MNX)

def count(alt=None):
    c = list(cipher)
    for pos, ch in (alt or {}).items(): c[pos - 1] = ch
    i = clean = letters = 0
    for w in words:
        n = len(w) + EXTRA.get(w, 0)
        span = ''.join(key.get(ch, '?') for ch in c[i:i + n]); i += n
        if span == w:
            clean += 1; letters += len(w)
    assert i == len(cipher) == 246, (i, len(cipher))
    return clean, letters

print(f'{len(words)} words, {len(cipher)} cipher letters')
for label, alt in (('readings in transcription.txt', None), ('position 121 = N', {121: 'N'}),
                   ('position 241 = P', {241: 'P'}),
                   ('fourth blind reading (7 F, 29 X, 129 F, 220 G)', {7: 'F', 29: 'X', 129: 'F', 220: 'G'})):
    w, l = count(alt)
    print(f'{label}: {w} of {len(words)} words clean ({100 * w / len(words):.1f}%), {l} of 246 letters in clean words ({100 * l / 246:.1f}%)')
