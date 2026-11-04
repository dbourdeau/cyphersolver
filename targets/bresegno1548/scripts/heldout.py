"""Held-out test: decrypt lines lo..hi with a frozen key and compare with the clear text of the same passage.

    python heldout.py <transcription> <key_frozen.tsv> <lo> <hi> "<first clear words of the passage>"

Score: share of clear letters matched in order (difflib), and share in matched runs of 4+.
Baseline: 200 tables with the values shuffled among the key rows (seed 1548).
"""
import difflib
import pathlib
import random
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decrypt

ROOT = decrypt.ROOT


def clear_from(start):
    s = ' '.join(l.split('\t', 1)[1] for l in open(ROOT / 'clear_c22r.txt', encoding='utf-8') if l.startswith('P'))
    s = s[s.index(start):].lower().replace('ñ', 'n').replace('ç', 'z')
    s = s.replace('v. ex.', '').replace('mag.', '')
    return re.sub(r'[^a-z]', '', s)


def letters(tr, key, lo, hi):
    out = []
    for ln, s, _ in decrypt.signs(tr):
        if lo <= ln <= hi:
            v = decrypt.value(s, key)
            if not v.startswith('['):
                out.append(re.sub(r'[^a-z]', '', v))
    return ''.join(out)


def score(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    blocks = sm.get_matching_blocks()
    m = sum(x.size for x in blocks)
    m4 = sum(x.size for x in blocks if x.size >= 4)
    return m / len(b), m4 / len(b)


def main():
    tr, kp, lo, hi, start = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    key = decrypt.load_key(kp)
    clear = clear_from(start)
    a, r4 = score(letters(tr, key, lo, hi), clear)
    print(f'frozen key: in order {a:.3f}, runs of 4+ {r4:.3f}  ({len(clear)} clear letters)')
    rnd = random.Random(1548)
    best = [0, 0]
    for _ in range(200):
        base, bare, code, st = key
        k2 = []
        for d in (base, bare, code):
            vals = list(d.values())
            rnd.shuffle(vals)
            k2.append(dict(zip(d.keys(), vals)))
        k2.append(st)
        s = score(letters(tr, tuple(k2), lo, hi), clear)
        best = [max(best[0], s[0]), max(best[1], s[1])]
    print(f'200 shuffled tables, max: in order {best[0]:.3f}, runs of 4+ {best[1]:.3f}')


if __name__ == '__main__':
    main()
