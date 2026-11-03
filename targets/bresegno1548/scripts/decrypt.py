"""Decrypt a c. 15r transcription with key.tsv. Standard library only.

    python decrypt.py <transcription.txt> [key.tsv]   -> prints 'Lnn<TAB>value value ...' (one value per sign)

key.tsv rows: kind<TAB>sign<TAB>value<TAB>status
  base   sign with a superscript vowel digit: value = consonant + vowel (2 a, 3 e, 4 i, 5 o, 6 u)
  bare   sign standing alone
  code   whole sign group; value in [brackets] for a code word, '-' for a null
A sign with two digits (e.g. L^62) is decoded on its last digit and flagged '!'. Unknown signs print as [?sign].
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VOW = {'2': 'a', '3': 'e', '4': 'i', '5': 'o', '6': 'u'}


def load_key(path=ROOT / 'key.tsv'):
    base, bare, code, status = {}, {}, {}, {}
    for line in open(path, encoding='utf-8'):
        if not line.strip() or line.startswith('#'):
            continue
        kind, sign, val, st = (line.rstrip('\n').split('\t') + [''])[:4]
        if kind == 'rule':
            continue  # context rules are applied in line_values
        {'base': base, 'bare': bare, 'code': code}[kind][sign] = val
        status[(kind, sign)] = st
    return base, bare, code, status


def norm(t):
    """Sign name without reader's doubt marks. Returns (name, doubtful) or None for struck/empty."""
    if t.startswith('~') and t.endswith('~'):
        return None
    doubt = '?' in t
    t = t.replace('?', '')
    t = re.sub(r'^\.', '', t)
    t = re.sub(r'\.(?=\^|$)', '', t)
    if t in ('', ';', ','):
        return None
    return t, doubt


def value(sign, key):
    base, bare, code, _ = key
    if sign in code:
        return code[sign]
    m = re.match(r'^(.+?)\^(\d+)$', sign)
    if m:
        b, digits = m.group(1), m.group(2)
        if b in base and digits[-1] in VOW:
            v = base[b] + VOW[digits[-1]]
            return v + ('!' if len(digits) > 1 else '')
        return f'[?{sign}]'
    if sign in bare:
        return bare[sign]
    return f'[?{sign}]'


def line_values(items, key):
    """Values for one line's signs, with the two context rules of key.tsv (kind 'rule'):
    bare a before an s- or ms-sign is p (pr, pl)."""
    out = []
    for i, (s, d) in enumerate(items):
        nxt = items[i + 1][0] if i + 1 < len(items) else ''
        nb = re.sub(r'\^\d+$', '', nxt)
        if s == 'a' and nb in ('s', 'ms'):
            v = 'p'
        else:
            v = value(s, key)
        out.append(v)
    return out


def signs(path):
    for line in open(path, encoding='utf-8'):
        m = re.match(r'^L(\d\d)\t(.*)$', line.rstrip('\n'))
        if not m:
            continue
        for t in m.group(2).split():
            n = norm(t)
            if n:
                yield int(m.group(1)), n[0], n[1]


def main():
    tr = sys.argv[1]
    key = load_key(sys.argv[2]) if len(sys.argv) > 2 else load_key()
    cur, out = None, []
    for ln, s, d in signs(tr):
        if ln != cur:
            if out:
                print(f'L{cur:02d}\t' + ' '.join(out))
            cur, out = ln, []
        out.append(value(s, key) + ('?' if d else ''))
    if out:
        print(f'L{cur:02d}\t' + ' '.join(out))


if __name__ == '__main__':
    main()
