"""Measure the reading of BnF fr. 3022 no. 6 from n6_signs.tsv.

Checks that the tokens of n6_signs.tsv (status r/i/n/u) reproduce, in order, the sign stream of Lasry's decryption
file for ff. 16v-17v (sections 16, 17a, 17b, 17va, 17vb; '_' and <plaintext> dropped), then counts cipher tokens
read (r = Lasry's key as it stands, i/n = value inferred here on 18/22 Sept 2026) against all tokens (x = signs seen on the image but
missing from Lasry's list, counted as unread). Also counts nomenclator groups ([xxx], titles excluded) and
prints the edited reading.

    PYTHONUTF8=1 python vasto1527/n6_measure.py [--text]
"""
import os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SECTIONS = ['16', '17a', '17b', '17va', '17vb']


def lasry_stream():
    t = open(os.path.join(HERE, 'prior', 'BnF_fr3022_f16_decryption.txt'), encoding='utf8').read()
    parts = re.split(r'^# (\S+)\.jpg\s*$', t, flags=re.M)
    toks = []
    for i in range(1, len(parts), 2):
        if parts[i] in SECTIONS:
            toks += [x for x in parts[i + 1].split() if x not in ('_', '<plaintext>')]
    return toks


def rows():
    for line in open(os.path.join(HERE, 'n6_signs.tsv'), encoding='utf8'):
        if not line.strip() or line.startswith('#'):
            continue
        f = line.rstrip('\n').split('\t')
        loc, toks, reading, status = f[:4]
        yield loc, toks.split(), reading, status, (f[4] if len(f) > 4 else '')


def main():
    ref = lasry_stream()
    got = []
    n = Counter()
    code = Counter()
    text = []
    for loc, toks, reading, status, note in rows():
        assert status in 'rinuxw' and len(status) == 1, (loc, status)
        if status not in 'xw':
            got += toks
        n[status] += len(toks)
        for t in toks:
            if t.startswith('[') and not t.startswith('[title'):
                code['read' if status in 'rinw' else 'open'] += 1
        text.append(reading if status in 'rinw' else '<' + reading + '>')
    if got != ref:
        for k, (a, b) in enumerate(zip(got, ref)):
            if a != b:
                sys.exit(f'token mismatch at {k}: reading file {got[k:k+8]} vs Lasry {ref[k:k+8]}')
        sys.exit(f'length mismatch: reading file {len(got)} vs Lasry {len(ref)}')
    total = sum(n.values())
    read = n['r'] + n['i'] + n['n'] + n['w']
    print(f'no. 6 cipher tokens: {total} (Lasry list {len(ref)} + {n["x"] + n["w"]} seen only on the image)')
    print(f'  read with Lasry key as it stands (r):        {n["r"]}')
    print(f'  read, value inferred 18 Sept 2026 (i):       {n["i"]}')
    print(f'  read, value inferred 22 Sept 2026 (n, w):    {n["n"] + n["w"]}')
    print(f'  not read (u + x):                            {n["u"] + n["x"]}')
    print(f'  Lasry key alone:            {n["r"]}/{total} = {n["r"] / total:.4f}')
    print(f'  with the 18 Sept readings:  {n["r"] + n["i"]}/{total} = {(n["r"] + n["i"]) / total:.4f}')
    print(f'  fraction read now:          {read}/{total} = {read / total:.4f}')
    print(f'  nomenclator group tokens (titles excluded): read {code["read"]}, open {code["open"]}')
    if '--text' in sys.argv:
        print()
        print(' '.join(text))


if __name__ == '__main__':
    main()
