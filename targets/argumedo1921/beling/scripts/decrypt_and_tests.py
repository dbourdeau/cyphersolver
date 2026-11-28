"""Decode the settled Argumedo runs with Narvaez's table (unchanged) and run controls C1 and C2 of PLAN.md.
Usage (from targets/argumedo1921/beling/): python3 -I scripts/decrypt_and_tests.py KEY.tsv SANTANDER_OCR.txt
KEY.tsv = ../key.tsv (SHA-256 69ce383f...); SANTANDER_OCR.txt = public-domain
Archivo Santander XIV OCR (model text for C2). Writes decryption.tsv and prints C1 and C2."""
import sys, re, random, math, unicodedata
from pathlib import Path

key = {}
for line in Path(sys.argv[1]).read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or line.startswith('code'): continue
    c, p = line.split('\t'); key[c] = p

def dec_pairs(s, k=key):
    s = re.sub(r'\[([^\]|]*)\|[^\]]*\]', lambda m: m.group(1), s)   # first alternative of an open doubt
    s = s.replace('|', '')
    out = []
    for tok in re.split(r'([.\s])', s):
        if tok == '.': out.append(' '); continue
        for grp in tok.split('-'):
            if not grp: continue
            if len(grp) % 2: out.append('?'); continue
            for i in range(0, len(grp), 2):
                out.append(k.get(grp[i:i+2], '?'))
    return ''.join(out)

rows = []
for line in Path('transcription.txt').read_text(encoding='utf-8').splitlines():
    if not line.startswith('DCXXI'): continue
    f = line.split('\t'); rows.append(f)
with open('decryption.tsv', 'w', newline='\n', encoding='utf-8') as fh:
    fh.write('doc\timage\trun\tpairs\tdecode\n')
    for f in rows:
        fh.write(f'{f[0]}\t{f[1]}\t{f[2]}\t{f[3]}\t{dec_pairs(f[3])}\n')

# C1: Narvaez's printed runs (2019 pp. 359-363) and his printed clear. Note (27 Nov 2026, after the cold check):
# the book prints the Benitez run as ...-10-05-L7(sic)-01-23 (p. 360) and its clear as "Benit-L7(sic)-ez"; this
# script was run with 17 there, as the image of the letter has it. Scored as printed (L7 a miss), C1 is 86 of 89
# (0.966), still above the 0.95 pass mark.
C1 = [('03-15-34-08-37-05-34-23', 'GRALDIAZ'), ('13-18-01-35-08-12', 'PUEBLO'),
      ('03-15-34-08-19-05-36-01-10-17-01-35-01-10-05-17-01-23', 'GRALVICENTEBENITEZ'),
      ('36-34-16-17-18-08-12', 'CASTULO'), ('06-18-34-10-17-37-01-34-15-34-10-34', 'JUANTDEARANA'),
      ('37-12-10-09-34-17-01-12', 'DONMATEO'), ('13-01-08-05-03-15-10', 'PELIGRO'),
      ('37-12-10-13-37-10-36-04-12', 'DONPANCHO'), ('16-12-36-05-12-16', 'SOCIOS'),
      ('34-15-03-18-09-01-37-12', 'ARGUMEDO')]
n = ok = 0
for c, p in C1:
    d = dec_pairs(c)
    for a, b in zip(d, p): n += 1; ok += (a == b)
    if d != p: print('C1 differs:', c, d, 'printed', p)
print(f'C1: {ok} of {n} letters agree ({ok/n:.3f}); pass mark 0.95: {"PASS" if ok/n >= 0.95 else "FAIL"}')

# C2: trigram score of all new runs against 1,000 permutations of the code values
def norm(t):
    t = t.upper().replace('Ñ', '\x00')
    t = unicodedata.normalize('NFD', t); t = ''.join(ch for ch in t if not unicodedata.combining(ch))
    return t.replace('\x00', 'Ñ')
model = norm(Path(sys.argv[2]).read_text(encoding='utf-8', errors='replace'))
words = re.findall(r'[A-ZÑ]+', model); text = ' '.join(words)
A = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ '
from collections import Counter
tri = Counter(text[i:i+3] for i in range(len(text)-2)); bi = Counter(text[i:i+2] for i in range(len(text)-1))
V = len(A)
def score(s):
    s = ' ' + s + ' '; tot = 0; n = 0
    for i in range(len(s)-2):
        t = s[i:i+3]; tot += math.log((tri[t] + 0.1) / (bi[t[:2]] + 0.1 * V)); n += 1
    return tot / max(n, 1)
def all_decode(k):
    return ' '.join(dec_pairs(f[3], k).replace('?', '') for f in rows)
real = score(all_decode(key))
codes = list(key.keys()); vals = list(key.values()); rnd = random.Random(20261125); beat = 0; best = -99
for _ in range(1000):
    v = vals[:]; rnd.shuffle(v); s = score(all_decode(dict(zip(codes, v)))); best = max(best, s); beat += (s >= real)
print(f'C2: frozen table {real:.3f} per letter; best of 1,000 permutations {best:.3f}; permutations at or above: {beat}; '
      f'{"PASS" if beat == 0 else "FAIL"}')
