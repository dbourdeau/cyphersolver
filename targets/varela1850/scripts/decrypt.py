"""Mechanical decryption, catalogue 1500. Standard library only.

    python scripts/decrypt.py transcription_varela1850.txt key_frozen.tsv > decryption_varela1850.txt

Each group is replaced by its key value; a group with no value is written [n]. Lone single numbers (items N..) and
the sign PHI are not in the letter table and are written [n] / [PHI]. ' / ' (line break) is kept as ' / '.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')


def load_key(path):
    k = {}
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or line.startswith('value'):
            continue
        p = line.rstrip('\n').split('\t')
        if len(p) >= 2 and p[0].strip().isdigit():
            k[int(p[0])] = p[1]
    return k


def runs(path):
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        p = line.rstrip('\n').split('\t')
        yield p[0], p[1], p[2], (p[3] if len(p) > 3 else '')


def dec_run(rid, run, k):
    if rid.startswith('N') or rid.startswith('S'):
        return f'[{run}]'
    out = []
    for part in run.split(' / '):
        s = ''
        for g in part.split('.'):
            g = g.strip()
            if not g:
                continue
            s += k.get(int(g), f'[{g}]') if g.isdigit() else f'[{g}]'
        out.append(s)
    return ' / '.join(out)


if __name__ == '__main__':
    k = load_key(sys.argv[2])
    print('# Mechanical decryption of transcription_varela1850.txt with key_frozen.tsv (scripts/decrypt.py).')
    print('# id\tsheet.line\tcipher\tdecryption')
    for rid, where, run, ctx in runs(sys.argv[1]):
        print(f'{rid}\t{where}\t{run}\t{dec_run(rid, run, k)}')
