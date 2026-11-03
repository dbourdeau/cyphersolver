#!/usr/bin/env python3
"""Decrypt the transcription of cc. 15-16 with key.tsv. Standard library only.

    python scripts/decrypt.py            print the line table
    python scripts/decrypt.py --check    compare with decryption_c15_16.txt

A sign followed by _8 or _9 is a null. {X} = code word. [clear text] is copied. No repairs.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = ['transcription_c15r.txt', 'transcription_c15v.txt', 'transcription_c16r.txt']
HEAD = '# Line-by-line output of scripts/decrypt.py with key.tsv on the transcription. No repairs. Null signs removed. {X} = code word. [clear text].'
DOUBLES = ('cc', 'tt', 'ss', 'rr', 'll')


def key():
    k, codes = {}, {}
    for l in (ROOT / 'key.tsv').read_text(encoding='utf8').splitlines():
        if l.startswith('#') or not l.strip():
            continue
        f = l.split('\t')
        if ' ' in f[0]:
            codes[f[0]] = f[1] if f[1] in DOUBLES else '{' + f[0].replace(' ', '').upper() + '}'
        else:
            k[f[0]] = f[1]
    return k, codes


def groups(part, codes):
    o = []
    for x in part.split():
        if x in ('_8', '_9'):
            if o:
                o.pop()
        else:
            o.append(x)
    s = ' ' + ' '.join(o) + ' '
    s = s.replace(' e r ', ' ER ')
    for nm, v in codes.items():
        s = s.replace(' ' + nm + ' ', ' <' + v + '> ')
    return s.split()


def lines():
    k, codes = key()
    out = []
    for f in FILES:
        for ln in (ROOT / f).read_text(encoding='utf8').splitlines():
            if ln.startswith('#') or ' ' not in ln.strip():
                continue
            lab, t = ln.rstrip().split(' ', 1)
            o = lab + ' '
            for p in re.split(r'(\[[^\]]*\])', t):
                if p.startswith('['):
                    o += ' ' + p + ' '
                    continue
                for x in groups(p, codes):
                    o += x[1:-1] if x.startswith('<') else k.get(x, '?')
            out.append(o.rstrip())
    return out


if __name__ == '__main__':
    d = lines()
    if '--check' in sys.argv:
        old = [l.rstrip() for l in (ROOT / 'decryption_c15_16.txt').read_text(encoding='utf8').splitlines() if not l.startswith('#')]
        bad = sum(a != b for a, b in zip(d, old)) + abs(len(d) - len(old))
        print(f'{len(d)} lines, {bad} differences')
        sys.exit(1 if bad else 0)
    print(HEAD)
    print('\n'.join(d))
