"""Rebuild the decryption of every cipher line from transcription_1719.txt + key_frozen.tsv and check the
reading against it. Fails (exit 1) on any unmarked departure.

reading_1719_*.md holds lines `lid: reading`. Clear text there is in {braces} and is ignored. Every
departure from the mechanical decryption must sit inside [square brackets]; outside brackets the
reading's letters must equal the decryption's letters exactly (u=v, j=i, case, spaces, accents and
punctuation ignored). A group the key does not cover, and a token piece that cannot be parsed, stand in
the rebuilt decryption as a placeholder that only a [bracket] can absorb: such a group can be neither
read silently nor left out silently. A reading line with a character outside the Latin script fails too.
Prints words read (no bracket) / words in cipher passages, in all and per part.
usage: python check_marks.py [key.tsv]
"""
import glob
import os
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from decrypt import load_key, lines, values  # noqa: E402

key = load_key(sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, 'key_frozen.tsv'))
tr = dict(lines(os.path.join(D, 'transcription_1719.txt')))
PARTS = [('2 Oct, ff. 4r-5r (key built from this gloss)', ('4r', '4v', '5r')),
         ('2 Oct, ff. 5v-6v (held out)', ('5v', '6r', '6v')),
         ('27 Oct, ff. 12r-13v (no gloss)', ('12r', '12v', '13r', '13v'))]


def letters(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if 'a' <= c <= 'z')
    return s.replace('u', 'v').replace('j', 'i')


def dec(body):
    body = re.sub(r'\{[^}]*\}', ' ', body)
    out = []
    for tok in body.split():
        for v in values(tok, key):
            out.append('#' if v.startswith('[') else letters(v))
    return ''.join(out)


bad = 0
count = {}
for fn in sorted(glob.glob(os.path.join(D, 'reading_1719_*.md'))):
    for ln in open(fn, encoding='utf-8'):
        m = re.match(r'\s*(\d+[rv]\.L\d+):\s*(.*)', ln)
        if not m:
            continue
        lid, rd = m.groups()
        if any(ord(c) > 0x24f and unicodedata.category(c).startswith('L') for c in rd):
            print(f'NON-LATIN LETTER in {lid}: {rd.strip()}')
            bad += 1
        if lid not in tr:
            print('NO TRANSCRIPTION LINE', lid)
            bad += 1
            continue
        rd = re.sub(r'\{[^}]*\}', ' ', rd)
        parts = re.split(r'(\[[^\]]*\])', rd)
        rx = ''.join('.*?' if p.startswith('[') else re.escape(letters(p)) for p in parts)
        d = dec(tr[lid])
        if not re.fullmatch(rx, d):
            print(f'UNMARKED DEPARTURE {lid}: decryption "{d}" (# = uncovered or unparsable group) '
                  f'reading "{rd.strip()}"')
            bad += 1
        c = count.setdefault(lid.split('.')[0], [0, 0])
        for w in re.findall(r'\S+', re.sub(r'\[[^\]]*\]', ' [] ', rd)):
            if re.search(r'[A-Za-z\[]', w):
                c[0] += 1
                c[1] += '[' not in w
words = sum(v[0] for v in count.values())
read = sum(v[1] for v in count.values())
for name, pages in PARTS:
    w = sum(count.get(p, [0, 0])[0] for p in pages)
    r = sum(count.get(p, [0, 0])[1] for p in pages)
    print(f'{name}: {w} words, {r} read without a mark ({r / max(w, 1):.0%})')
print(f'all cipher-passage words: {words}, read without a mark: {read} ({read / max(words, 1):.0%})')
print('FAIL' if bad else 'OK: every departure is marked')
sys.exit(1 if bad else 0)
