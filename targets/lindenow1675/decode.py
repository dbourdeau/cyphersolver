#!/usr/bin/env python3
"""Decode the Lindenow letters of the Biermann copybook with key.tsv, line by line.

    python decode.py            write texts/<date>_lindenow_decryption.txt for every transcription
    python decode.py --check    the same in memory; exit 1 if a decryption file on disk differs
    python decode.py --counts   groups, groups with a value and distinct groups per letter

The key is the one rebuilt on the letter of 22 February 1675 and is applied unchanged to the other three.
A group with no value in key.tsv is printed [n]. Nothing is corrected or guessed here: the transcription is
decoded as it stands. Standard library only.
"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
TEXTS = HERE / 'texts'


def load_key():
    key = {}
    for line in (HERE / 'key.tsv').read_text(encoding='utf-8').splitlines()[1:]:
        f = line.split('\t')
        if len(f) >= 3 and f[2]:
            key[f[1]] = f[2]
    return key


def pieces(line):
    """Split a transcription line into ('clear', text) and ('group', token) pieces."""
    out, i = [], 0
    while i < len(line):
        if line[i] == '{':
            j = line.index('}', i)
            out.append(('clear', line[i + 1:j]))
            i = j + 1
        elif line[i].isspace():
            i += 1
        else:
            j = i
            while j < len(line) and not line[j].isspace() and line[j] != '{':
                j += 1
            out.append(('group', line[i:j]))
            i = j
    return out


def decode(path, key):
    head = [f'# Decryption of texts/{path.name}, line by line, under key.tsv (the key of 22 February 1675, unchanged).',
            '# lower case = letter sign, letter number or syllable; Capitalised or longer = word code; [n] = group with no value; |cl| = clear text.',
            '']
    body, n, total, read, seen = [], 0, 0, 0, set()
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        n += 1
        top, bottom = [], []
        for kind, x in pieces(line):
            if kind == 'clear':
                top.append('{cl}')
                bottom.append('|' + x + '|')
            else:
                total += 1
                seen.add(x)
                v = key.get(x)
                read += v is not None
                top.append(x)
                bottom.append(v if v is not None else '[' + x + ']')
        body += [f'{n:02d} ' + ' '.join(top), '   ' + ' '.join(bottom)]
    return '\n'.join(head + body) + '\n', (total, read, len(seen))


def main():
    key = load_key()
    bad = 0
    for path in sorted(TEXTS.glob('*_lindenow_transcription.txt')):
        text, (total, read, distinct) = decode(path, key)
        out = TEXTS / path.name.replace('_transcription', '_decryption')
        if '--counts' in sys.argv:
            print(f'{path.name[:10]}  groups {total:3d}  with a value {read:3d}  distinct {distinct:3d}')
        elif '--check' in sys.argv:
            same = out.is_file() and out.read_text(encoding='utf-8') == text
            print(f'{out.name}: ' + ('same' if same else 'DIFFERENT'))
            bad += not same
        else:
            out.write_text(text, encoding='utf-8')
            print(f'wrote {out.name}: {read} of {total} groups have a value')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
