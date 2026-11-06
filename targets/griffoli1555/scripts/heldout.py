"""Held-out test for target 2346 (Griffoli), letter level, with a shuffled-key baseline. Standard library only.

    python scripts/heldout.py [n_shuffles]

Decrypts block c (443 c. 318r, lines c01-c04 of transcription_k316.txt) with key_frozen.tsv and compares its letters
with the contemporary decipherment of the same passage on c. 317r (gloss_c317_heldout.txt, expanded line) by longest
common subsequence. Code units are spelled out (et, che, non, si, quanto, V.Ecc.); odd digit groups and units not in
the key are dropped. Baseline: the same score for keys whose values are shuffled among the frozen key's units
(fixed seed). The gloss sign between "ordinato" and "solo" is scored both as "et" (as first graded) and as "che".
The word-level figure in NOTES.md (22 of 24 words, spelling apart) was graded by hand; this script gives a
mechanical letter-level check of the same test.
"""
import pathlib
import random
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import decrypt  # noqa: E402


def letters(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower().replace('v', 'u')
    s = re.sub(r'\[[^\]]*\]', '', s)
    return re.sub(r'[^a-z]', '', s)


def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j] + 1 if x == y else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]


def block_c():
    out = []
    for line in open(ROOT / 'transcription_k316.txt', encoding='utf-8'):
        if line.startswith('c'):
            out.append(line.rstrip('\n').split('\t')[1].strip())
    return out


def decode(lines, key):
    return letters(''.join(decrypt.decrypt_line(d, key) for d in lines))


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    key = decrypt.load_key(ROOT / 'key_frozen.tsv')
    lines = block_c()
    units = [s for d in lines for k, s in decrypt.units(d) if k == 'u']
    odd = [s for d in lines for k, s in decrypt.units(d) if k == '?']
    missing = sorted({u for u in units if u not in key})
    gloss = [l.split('\t', 1)[1] for l in open(ROOT / 'gloss_c317_heldout.txt', encoding='utf-8')
             if l.startswith('expanded\t')][0]
    plain = decode(lines, key)
    print(f'block c: {len(units)} two-digit units, {len(odd)} odd group(s) {odd}; units not in the frozen key: {missing or "none"}')
    print(f'decryption letters: {len(plain)}')
    rng = random.Random(2346)
    vals = list(key.values())
    shuffled = []
    for _ in range(n):
        rng.shuffle(vals)
        k2 = dict(zip(key.keys(), vals))
        shuffled.append(decode(lines, k2))
    for reading in ('et', 'che'):
        g = letters(re.sub(r'\{et\|che\}', reading, gloss))
        real = lcs(plain, g)
        sc = [lcs(p, g) / len(g) for p in shuffled]
        print(f'gloss sign read "{reading}": gloss letters {len(g)}; frozen key matches {real} ({100 * real / len(g):.1f}%); '
              f'{n} shuffled keys: mean {100 * sum(sc) / n:.1f}%, max {100 * max(sc):.1f}%')


if __name__ == '__main__':
    main()
