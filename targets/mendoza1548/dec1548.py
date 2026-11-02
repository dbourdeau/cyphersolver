"""Decode the cipher of MSS/20212/29/1 (mendoza1548) with the key rebuilt from sign-syllable pairs.

Usage: python3 dec1548.py [transcription/d1_transcription.md] [key_pairs_gloss.txt key_pairs_crib.txt]

The key is the most common syllable of each sign over the pairs (a second value with two or more places and at
least a third of the first's count prints as a/b), plus a few values from
Bucuré 2025 for signs not in the pairs. Code groups print in brackets, nulls print nothing, dots are dropped,
a sign without a value prints as [sign]. ꝺ followed by a dot is *que* or *da* (the two are not
separable on the scan).
"""
import sys, re, collections, pathlib, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
# Values from Bucuré 2025 (Estudios Románicos 34, key table p. 52) and from the sign families, for signs the pairs
# do not cover or cover once.
BASE = {
    'ʃ': 'e', 'ω': 'e', 'aꝶ': 'o', '─o': 'l', 'mo': 's', 'ꝺ': 's', 'Xo': 'de', '8̈': 'ci', 'M': 'pu',
    'ꝶ': 'se', 'ÿ': 'si', '8ꝶ': 'cu', '∠': 'll', 'd': 'r', 'n': 'a', '6': 'a', 'ꝺ̇': 'ta',
    'X': 'se', 'V̇': 'ta', 'V': 'pa/po', '⊥': 'tra', '⊥̇': 'tra', '4': 'tre', 'ɑ': 'ra',
    'ꝓ°': 'po/ho', 'g': 'r', '∇o': 'to', 'ꝶ4': 'me', 'β': 'y', 'ÿo': 'vo', 'ɔo': 'no', 'I': 'i',
}
CODE = {'dide': '[Su Majestad]', 'mta': '[Su Santidad]', 'nego:': '[franceses]', 'ritib': '[Vuestra Señoría]'}
NULLS = {'–', 'ö', 'o̤', 'n̤', 'ɑꝶ̤', 'd̤', 'δ̣'}
FIXED = {'de': 'lo', 'no': 'r'}  # glyphs shaped like clear words; their values from the alignment (NOTES.md)

def load_key(*paths):
    d = collections.defaultdict(collections.Counter)
    for p in paths:
        for ln in unicodedata.normalize('NFC', open(p, encoding='utf-8').read()).splitlines():
            if ln.startswith('#') or '\t' not in ln:
                continue
            for item in ln.rstrip('\n').split('\t')[1].split():
                if '=' in item:
                    s, v = item.split('=', 1)
                    v = v.rstrip('?')
                    if v and v != '?':
                        d[s][v] += 1
    key = {}
    for s, c in d.items():
        if s == 'V':
            continue
        (v1, n1), *rest = c.most_common(2)
        # a second value prints only with two or more places and at least a third of the first value's count
        key[s] = f'{v1}/{rest[0][0]}' if rest and rest[0][1] >= 2 and rest[0][1] * 3 >= n1 else v1
    for s, v in BASE.items():
        key.setdefault(s, v)
    key.update(FIXED)
    return key

def lines(path):
    text = unicodedata.normalize('NFC', open(path, encoding='utf-8').read())
    block = re.search(r'```\n(.*?)```', text, re.S).group(1)
    for ln in block.splitlines():
        if '\t' in ln:
            yield ln.split('\t')

def decode(signs, key):
    out, toks = [], signs.split()
    for j, t in enumerate(toks):
        if t == '.':
            continue
        if t == 'ꝺ' and j + 1 < len(toks) and toks[j + 1] == '.':
            out.append('que/da')
        elif t in CODE:
            out.append(CODE[t])
        elif t in NULLS:
            continue
        elif t in key:
            if key[t] != '–':
                out.append(key[t])
        else:
            out.append(f'[{t}]')
    return ' '.join(out)

if __name__ == '__main__':
    tr = sys.argv[1] if len(sys.argv) > 1 else HERE / 'transcription/d1_transcription.md'
    pairs = sys.argv[2:] or [HERE / 'key_pairs_gloss.txt', HERE / 'key_pairs_crib.txt']
    key = load_key(*pairs)
    for lab, gloss, signs in lines(tr):
        print(f'{lab}   {gloss}\n      {decode(signs, key)}')
