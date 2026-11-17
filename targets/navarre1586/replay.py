"""Adapter for docs/_replay.py: key_321.json applied to ct_333.txt, against texts/f333_reading.md.

The decode rule is targets/segur/decode.py's (letters; syllable blocks of five from 63, sixteen rows; names).
The clear text of the leaf is passed through as anchor text and is not counted. The cipher runs on without word
division, so words are counted over the reading.
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
DIVIDED = False
SOURCES = {'key': 'key_321.json', 'transcription': 'ct_333.txt', 'reading': 'texts/f333_reading.md'}
POLYPHONY = {}
BLOCK0, NBLK, VOW = 63, 16, 'aeiou'
LABEL = 'f333'


def mechanical():
    key = json.load(open(os.path.join(HERE, 'key_321.json'), encoding='utf8'))
    L = {int(k): v for k, v in key['letters'].items()}
    B = {int(k): v for k, v in key['blocks'].items()}
    N = {k: v.strip('[]') for k, v in key.get('names', {}).items() if v.startswith('[')}

    def dec(t):
        n = int(t)
        if n in L:
            return L[n]
        if BLOCK0 <= n < BLOCK0 + 5 * NBLK:
            c = B.get(BLOCK0 + 5 * ((n - BLOCK0) // 5))
            return c + VOW[(n - BLOCK0) % 5] if c else None
        return N.get(t)
    word = []
    for line in open(os.path.join(HERE, 'ct_333.txt'), encoding='utf8'):
        if line.startswith('#'):
            continue
        for part in re.split(r'(\[[^\]]*\])', line.strip()):
            if part.startswith('['):
                word.append((None, part[1:-1].replace('...', ' ')))
            else:
                for t in part.split():
                    if t.isdigit():
                        word.append((t, dec(t)))
    return [(LABEL, [word])]


def reading():
    txt = open(os.path.join(HERE, 'texts', 'f333_reading.md'), encoding='utf8').read().split('## Reading', 1)[1]
    txt = txt.replace('⟨', ' ').replace('⟩', ' ').replace('…', ' ')
    txt = re.sub(r'\[\s*\]', ' # ', txt)                      # "[…]" after the ellipsis is stripped
    txt = re.sub(r'\[162 = ([^\]]*)\]', r'\1', txt)           # the one name code the key gives
    txt = re.sub(r'\[\d+\]', ' # ', txt)                      # name codes with no value
    return {LABEL: txt}
