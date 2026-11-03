#!/usr/bin/env python3
"""Rerun each key in this folder over its transcription and compare with the decryption files. Standard library only.
Consistency only: it shows that the files agree, not that the signs are right.

    python scripts/check_decryption.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def keymap(name):
    k = {}
    for l in (ROOT / name).read_text(encoding='utf8').splitlines()[1:]:
        p = l.split('\t')
        k[p[0]] = p[1 if name == 'key_1576.tsv' else 2].replace('u/v', 'u')  # 1576: sign, plain; 1559: sign, shape, plain
    return k


def lines(name):
    return [l for l in (ROOT / name).read_text(encoding='utf8').splitlines() if l.strip() and not l.startswith('#')]


if (ROOT / 'key_1576.tsv').exists():
    K = keymap('key_1576.tsv')
    bad = n = 0
    dec = lines('decryption_cc76-77_1576-04-14.txt')
    for i, l in enumerate(lines('transcription_cc76-77_1576-04-14.txt')):
        lab, s = l.split()
        assert dec[2 * i].split() == [lab, s], lab
        want = dec[2 * i + 1].strip()
        got = ''.join(c if c in '{}' else '.' if K.get(c) == 'null' else '?' if c == '#' else K[c] for c in s)
        n += 1
        if got != want:
            bad += 1
            print('differs', lab)
    print(f'cc. 76-77: {n} lines, {bad} differences')

if (ROOT / 'key_1559.tsv').exists():
    K = keymap('key_1559.tsv')
    bad = n = 0
    dec = lines('decryption_cc50r_1559-05-28.txt')
    for i, l in enumerate(lines('transcription_cc50r_1559-05-28.txt')):
        lab, *s = l.split()
        want = dec[3 * i + 1].split(': ', 1)[1]
        got = ''.join(K.get(c, '?') for c in s)
        n += 1
        if got != want:
            bad += 1
            print('differs', lab)
    print(f'c. 50r: {n} lines, {bad} differences')
