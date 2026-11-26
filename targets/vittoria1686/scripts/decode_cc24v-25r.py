#!/usr/bin/env python3
"""Decrypt the letter of 18 Sept 1691 (cc. 24v-25r) with kennedy_2026/key_kennedy.tsv. Standard library only.

    python scripts/decode_cc24v-25r.py            print the decryption
    python scripts/decode_cc24v-25r.py --write    write decryption_cc24v-25r.txt
    python scripts/decode_cc24v-25r.py --check    compare with decryption_cc24v-25r.txt

The key file is applied sign by sign with nothing edited: u/v printed u, a raised ending in parentheses,
an abbreviation point kept, a code group in the key printed as [value], a group not in the key as [number].
[clear text] is copied. The '=' of a word carried over a line end is kept.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEY = ROOT / 'kennedy_2026' / 'key_kennedy.tsv'
SRC = ROOT / 'transcription_cc24v-25r.txt'
OUT = ROOT / 'decryption_cc24v-25r.txt'
HEAD = ['# Catalogue 1570 (vittoria1686) - Letter 5 (cc. 24v-25r, 18 September 1691) literal decryption of transcription_cc24v-25r.txt.',
        '# kennedy_2026/key_kennedy.tsv applied group by group by scripts/decode_cc24v-25r.py, nothing edited: u/v rendered u, raised endings in parentheses,',
        '# code groups of the key as [value], code groups not in the key as [number]. This is not the reading (reading_cc24v-25r.md).']


def key():
    t = {}
    for l in KEY.read_text(encoding='utf-8').splitlines():
        if l.startswith('#') or not l.strip():
            continue
        code, plain = l.split('\t')[:2]
        code = code.strip('.')                       # '.5.' is the dot-marked 5 = b
        plain = plain.split('/')[0]                   # 'u/v' -> 'u'
        t[code] = f'[{plain}]' if len(plain) > 1 else plain
    return t


def group(g, t):
    m = re.fullmatch(r'(\d+)(\.)?(?:\^([a-z]+))?', g)
    if not m:
        raise SystemExit(f'cannot read group {g!r}')
    n, dot, sup = m.groups()
    v = t.get(n, f'[{n}]')
    return v + ('.' if dot else '') + (f'({sup})' if sup else '')


def lines():
    t = key()
    out = []
    for ln in SRC.read_text(encoding='utf-8').splitlines():
        if ln.startswith('#') or not ln.strip():
            continue
        lab, body = ln.split(' ', 1)
        r = []
        for part in re.split(r'(\[[^\]]*\])', body):
            if part.startswith('['):
                r.append(part)
                continue
            for w in part.split('/'):
                gs = w.split()
                if not gs:
                    continue
                word = ''.join('=' if g == '=' else group(g, t) for g in gs)
                r.append(word)
        out.append(lab + ' ' + ' '.join(r))
    return out


if __name__ == '__main__':
    d = lines()
    if '--check' in sys.argv:
        old = [l for l in OUT.read_text(encoding='utf-8').splitlines() if l.strip() and not l.startswith('#')]
        bad = sum(a != b for a, b in zip(d, old)) + abs(len(d) - len(old))
        print(f'{len(d)} lines, {bad} differences')
        sys.exit(1 if bad else 0)
    text = '\n'.join(HEAD + d) + '\n'
    if '--write' in sys.argv:
        OUT.write_text(text, encoding='utf-8', newline='\n')
        print(f'wrote {OUT.name}: {len(d)} lines')
    else:
        sys.stdout.reconfigure(encoding='utf-8')
        print(text, end='')
