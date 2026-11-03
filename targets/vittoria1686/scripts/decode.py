#!/usr/bin/env python3
"""Decrypt the number groups of the Vittoria Gonzaga letters with key.tsv. Standard library only.

    python scripts/decode.py            print the line table
    python scripts/decode.py --check    compare with decryption_numbers.txt

Groups are split where the writer leaves a space (/). [clear text] is copied. No repairs.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HEAD = '# Number groups decrypted with key.tsv, no repairs. [che], [?per] = code groups; [109], [182] = code groups not identified; ? = group not in the key. Compare reading_numbers.md.'


def table():
    t, c = {}, {}
    for l in (ROOT / 'key.tsv').read_text(encoding='utf8').splitlines():
        if l.startswith('#') or not l.strip():
            continue
        f = l.split('\t')
        if f[1].startswith('['):
            c[int(f[0])] = f[1]
        else:
            t[int(f[0])] = f[1].split(',')[0].strip()
    return t, c


def lines():
    t, c = table()
    out = []
    for ln in (ROOT / 'transcription_numbers.txt').read_text(encoding='utf8').splitlines():
        if ln.startswith('#') or not ln.strip():
            continue
        lab, b = ln.rstrip().split(' ', 1)
        r = []
        for p in re.split(r'(\[[^\]]*\])', b):
            if p.startswith('['):
                r.append(p)
                continue
            for g in p.split('/'):
                w = ''
                for x in g.split():
                    d = x.endswith('~')
                    n = int(x.rstrip('~'))
                    v = c.get(n, t.get(n, '?'))
                    w += v * 2 if d else v
                if w:
                    r.append(w)
        out.append(lab + '  ' + ' '.join(r))
    return out


if __name__ == '__main__':
    d = lines()
    if '--check' in sys.argv:
        old = [l.rstrip() for l in (ROOT / 'decryption_numbers.txt').read_text(encoding='utf8').splitlines() if not l.startswith('#')]
        bad = sum(a != b for a, b in zip(d, old)) + abs(len(d) - len(old))
        print(f'{len(d)} lines, {bad} differences')
        sys.exit(1 if bad else 0)
    print(HEAD)
    print('\n'.join(d))
