"""Mechanical decryption for fuerstenberg1659. Standard library only.

    python scripts/decrypt.py transcription_fuerstenberg1659.txt key_frozen.tsv > decryption_fuerstenberg1659.txt

The key file gives, per cipher letter, the plain letter at odd and at even places of a run; the place count
restarts at each run (column 2 of the transcription). A sign not in the key prints as '#'. A '?' after a sign
(an uncertain reading, SIGN_CONVENTIONS.md) is not a sign: it does not advance the place count and is copied after
the plain letter, so the doubt shows in the decryption.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

def load_key(path):
    k = {}
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or line.startswith('cipher'):
            continue
        c, o, e = line.rstrip('\n').split('\t')
        k[c] = (o, e)
    return k

def runs(path):
    out = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or '\t' not in line:
            continue
        lab, run, ct = line.rstrip('\n').split('\t')
        out.append((lab, run, ct))
    return out

def decrypt(trans, keyp):
    k = load_key(keyp)
    lines = []
    pos = {}
    for lab, run, ct in runs(trans):
        i = pos.get(run, 0)
        pt = ''
        for ch in ct:
            if ch == '?':
                pt += '?'
                continue
            pt += k[ch][i % 2] if ch in k else '#'
            i += 1
        pos[run] = i
        lines.append((lab, run, ct, pt))
    return lines

if __name__ == '__main__':
    print('# Mechanical decryption of transcription_fuerstenberg1659.txt with key_frozen.tsv (scripts/decrypt.py)')
    print('# label\trun\tcipher\tplain')
    for row in decrypt(sys.argv[1], sys.argv[2]):
        print('\t'.join(row))
