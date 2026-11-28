"""Mechanical decode of a Meyerfeldt transcription with key.tsv.

Usage: python3 decode.py transcription/143535_block1.txt [transcription/143535_block2.txt ...]
Each transcription line is "Ln: CODE CODE ..."; {..} items (figures written in the line) are copied as they are.
Ambiguous values are printed as (a|b). Not a reading: see reading.md.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent


def load_key():
    key = {}
    for line in (HERE / 'key.tsv').read_text(encoding='utf-8').splitlines():
        if not line or line.startswith('# ') or line.startswith('code\t'):
            continue
        code, value = line.split('\t')[:2]
        key[code] = value if '|' not in value else '(' + value + ')'
    return key


def main(paths):
    key = load_key()
    for p in paths:
        print('#', p)
        for line in pathlib.Path(p).read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('# '):
                continue
            label, codes = line.split(':', 1)
            out = ''.join(c if c.startswith('{') else key[c] for c in codes.split())
            print(f'{label}: {out}')


if __name__ == '__main__':
    main(sys.argv[1:])
