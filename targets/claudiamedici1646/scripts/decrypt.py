"""Decrypt a transcription of catalogue 2354 (Claudia de' Medici to Piccolomini) with key_frozen.tsv.
Standard library only.

    python decrypt.py <transcription.txt> [key.tsv]   -> prints 'Lnn: decryption' per line

Transcription rules (SIGN_CONVENTIONS.md): tokens separated by spaces, ' | ' = gap in the cipher (printed as a
space), '<...>' = plain script copied through, '|f' = pen flourish (dropped), '=' = line-end hyphen (kept),
'a/b' = doubtful shape (first one used), '?' = illegible sign (printed '?'), 'X?' = a sign whose shape is only
near the key's X (printed as X's value in round brackets, e.g. '(z)'; the reading must mark it {?z}).
Code groups print as [Name].
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_key(path):
    key = {}
    for line in open(path, encoding='utf-8'):
        if not line.strip() or line.startswith('#') or line.startswith('token\t'):
            continue
        tok, val = line.rstrip('\n').split('\t')[:2]
        key[tok] = val
    return key


def decrypt_line(body, key):
    out = []
    for part in re.split(r'(<[^>]*>)', body):
        if part.startswith('<'):
            out.append(part)
            continue
        words = []
        for grp in part.split('|'):
            vals = []
            for t in grp.split():
                if t == 'f':          # remainder of '|f'
                    continue
                if t == '=':
                    vals.append('=')
                    continue
                if t == '.':
                    continue
                if t == '?':
                    vals.append('?')
                    continue
                t = t.split('/')[0]
                if len(t) > 1 and t.endswith('?') and t[:-1] in key:
                    vals.append('(' + key[t[:-1]] + ')')
                    continue
                if t not in key:
                    vals.append('[?' + t + ']')
                    continue
                vals.append(key[t])
            if vals:
                words.append(''.join(vals))
        if words:
            out.append(' '.join(words))
    return ' '.join(o.strip() for o in out if o.strip())


def decrypt_file(tpath, kpath):
    key = load_key(kpath)
    lines = []
    for line in open(tpath, encoding='utf-8'):
        m = re.match(r'(L\d+):\s*(.*)$', line.rstrip('\n'))
        if m:
            lines.append(f'{m.group(1)}: {decrypt_line(m.group(2), key)}')
    return lines


if __name__ == '__main__':
    t = sys.argv[1]
    k = sys.argv[2] if len(sys.argv) > 2 else str(ROOT / 'key_frozen.tsv')
    print('\n'.join(decrypt_file(t, k)))
