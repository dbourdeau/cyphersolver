"""Decode a sign-level transcription of BL Add MS 72438 f. 107 (DECODE R8728) with the lower alphabet of
f. 106 (DECODE R8727), plus the homophones the sheet does not list (see f107_reading.txt).

Line 6 of the letter is transcribed here sign by sign from the DECODE image (9 Oct 2026); words are separated
as in the manuscript. ':' stands for both m and n on the key, the u sign for u and v; MN and UV give the reading chosen in order.
Usage: python f107_decode.py            prints the decoded line
       python f107_decode.py --reveal   writes ../../docs/reveal/rupert.json
"""
import json, os, sys

KEY = {  # f. 106 lower alphabet
    '∧': 'a', 'Ꝛ': 'b', '–': 'c', '=': 'd', '≡': 'e', '+': 'f', '↓': 'g', '↑': 'h', 'o': 'i', '†': 'k',
    'ɭ': 'l', ':': 'm/n', 'ı': 'o', 'ǂ': 'p', 'X': 'r', 'ʂ': 's', 'Ⱥ': 't', 'ŧ̥': 'u/v', 'ıı': 'y',
}
# where a sign is used for a letter the key gives to another sign (writer's homophone or slip)
OVERRIDE = {('X', 'expect'): 'x'}

LINE6 = [  # f. 107 line 6, gloss above it: "I hoped for some comfortable lynes but tis in vaine to expect"
    ['o'], ['↑', 'ı', 'ǂ', '≡', '='], ['+', 'ı', 'X'], ['ʂ', 'ı', ':', '≡'],
    ['–', 'ı', ':', '+', 'ı', 'X', 'Ⱥ', '∧', 'Ꝛ', '≡', 'ɭ'], ['ɭ', 'ıı', ':', '≡', 'ʂ'],
    ['Ꝛ', 'ŧ̥', 'Ⱥ'], ['Ⱥ', 'o', 'ʂ'], ['o', ':'], ['ŧ̥', '∧', 'o', ':', '≡'], ['Ⱥ', 'ı'],
    ['≡', 'X', 'ǂ', '≡', '–', 'Ⱥ'],
]
WORDS = ['i', 'hoped', 'for', 'some', 'comfortabel', 'lynes', 'but', 'tis', 'in', 'vaine', 'to', 'expect']
MN = ['m', 'm', 'n', 'n', 'n']  # some, comfortabel, lynes, in, vaine
UV = ['u', 'v']  # but, vaine


def decode():
    out, mn, uv = [], iter(MN), iter(UV)
    for signs, word in zip(LINE6, WORDS):
        toks = []
        for s in signs:
            p = KEY[s]
            cls = ''
            if p == 'm/n':
                p = next(mn)
            elif p == 'u/v':
                p = next(uv)
            if (s, word) in OVERRIDE:
                p, cls = OVERRIDE[(s, word)], 'unc'
            toks.append({'g': s, 'p': p, 'cls': cls})
        got = ''.join(t['p'] for t in toks)
        assert got == word, (got, word)
        out.append(toks)
    return out


if __name__ == '__main__':
    words = decode()
    print(' '.join(''.join(t['p'] for t in w) for w in words))
    if '--reveal' in sys.argv:
        toks = []
        for i, w in enumerate(words):
            if i:
                toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
            toks.extend(w)
        here = os.path.dirname(os.path.abspath(__file__))
        dst = os.path.join(here, '..', '..', 'docs', 'reveal', 'rupert.json')
        json.dump({
            'slug': 'rupert',
            'anchor': 'f107',
            'title': 'Line 6 of f. 107, sign by sign',
            'caption': 'BL Add MS 72438 f. 107, line 6, transcribed sign by sign from the DECODE image (R8728) and '
                       'decoded with the lower alphabet of the key sheet f. 106 (R8727). The contemporary gloss over '
                       'the line reads the same words.',
            'unit': 'sign',
            'key_note': 'The colon stands for both m and n on the key; the reading here picks one by the word. '
                        'In "expect" the writer used the r sign for x (marked uncertain).',
            'tokens': toks,
        }, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('wrote', os.path.normpath(dst), len([t for t in toks if t['cls'] != 'plain']), 'signs')
