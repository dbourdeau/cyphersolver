"""Mechanical decode of the Holbeck transcriptions with the frozen key (frozen/cle/key-FROZEN.json).

Each sign takes the FIRST value of its set; digits between #...# are sums in clear and are kept; a sign
not in the key is printed in capitals. This is not a reading: it was made after the one pre-registered
measure (frozen/MESURE-p3-passe1.json) and is kept so the next reader can see what the key gives.

  python3 decode_first.py frozen/transcription/p3-TEST-passe1.txt
"""
import sys, json, re, pathlib

HERE = pathlib.Path(__file__).resolve().parent
key = json.loads((HERE / 'frozen' / 'cle' / 'key-FROZEN.json').read_text(encoding='utf-8'))

def dec_word(w):
    if w.startswith('#') or w.endswith('#') or w == '[?]':
        return w
    return ''.join(key[c][0] if c in key else c.upper() for c in w)

for line in open(sys.argv[1], encoding='utf-8'):
    parts = re.split(r'(#.*?#)', line.rstrip('\n'))
    out = []
    for p in parts:
        out.append(p if p.startswith('#') else ' '.join(dec_word(w) for w in p.split()))
    print(' '.join(x for x in out if x))
