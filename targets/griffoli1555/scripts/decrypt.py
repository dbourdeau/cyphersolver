"""Mechanical decryption of a Griffoli transcription. Standard library only.

    python scripts/decrypt.py <transcription.txt> [key.tsv]

Transcription lines: label<TAB>digits. Each line is split on the digit 0 (null/separator);
every segment of even length is read as two-digit units; a segment of odd length is printed
as [?segment] (a misread, a stray digit or an unknown sign). Units missing from the key print as [nn].
Output: label<TAB>mechanical text (units joined, codes in their key form).
"""
import pathlib
import sys

sys.stdout.reconfigure(encoding='utf-8', newline='\n')
ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_key(path):
    k = {}
    for line in open(path, encoding='utf-8'):
        if not line.strip() or line.startswith('#'):
            continue
        u, v = line.rstrip('\n').split('\t')[:2]
        k[u] = v
    return k


def units(digits):
    out = []
    for seg in digits.split('0'):
        if not seg:
            continue
        if len(seg) % 2:
            out.append(('?', seg))
        else:
            out += [('u', seg[i:i + 2]) for i in range(0, len(seg), 2)]
    return out


def decrypt_line(digits, key):
    res = []
    for kind, s in units(digits):
        if kind == '?':
            res.append(f'[?{s}]')
        else:
            v = key.get(s)
            res.append(v if v is not None else f'[{s}]')
            if v is not None and len(v) > 1:  # code word: keep it visible as one piece
                res[-1] = '<' + v + '>'
    return ''.join(res)


def main():
    tr = sys.argv[1]
    key = load_key(sys.argv[2] if len(sys.argv) > 2 else ROOT / 'key.tsv')
    for line in open(tr, encoding='utf-8'):
        if not line.strip() or line.startswith('#'):
            continue
        lab, d = line.rstrip('\n').split('\t')[:2]
        print(f'{lab}\t{decrypt_line(d.strip(), key)}')


if __name__ == '__main__':
    main()
