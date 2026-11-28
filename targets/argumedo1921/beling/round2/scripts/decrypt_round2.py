"""Round 2 (DCXXI.4.425.2): decode the settled Argumedo runs with Narvaez's table (unchanged) and run control C2 of the round-2 PLAN.md (seed 20261126).
Usage (from targets/argumedo1921/beling/round2/): python3 -I scripts/decrypt_round2.py KEY.tsv SANTANDER_OCR.txt
KEY.tsv = ../../key.tsv (SHA-256 69ce383f...); SANTANDER_OCR.txt = public-domain
Archivo Santander XIV OCR (model text for C2). Writes decryption.tsv and prints C2."""
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

# C1 is not rerun in round 2 (PLAN.md of round 2): it passed in round 1 (87 of 89 letters).

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
codes = list(key.keys()); vals = list(key.values()); rnd = random.Random(20261126); beat = 0; best = -99
for _ in range(1000):
    v = vals[:]; rnd.shuffle(v); s = score(all_decode(dict(zip(codes, v)))); best = max(best, s); beat += (s >= real)
print(f'C2: frozen table {real:.3f} per letter; best of 1,000 permutations {best:.3f}; permutations at or above: {beat}; '
      f'{"PASS" if beat == 0 else "FAIL"}')
