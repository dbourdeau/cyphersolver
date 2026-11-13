"""Mechanical decryption: python scripts/decrypt.py transcription.txt key.tsv > decryption.txt
Each capital is replaced by its key value (letters not in the key stand for themselves); spaces and ' are kept."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
def load_key(p):
    k = {}
    for line in open(p, encoding='utf-8'):
        if line.startswith('#') or line.startswith('cipher') or not line.strip():
            continue
        c, v = line.rstrip('\n').split('\t')
        k[c] = v
    return k
def dec(s, k):
    return ''.join(k.get(ch, ch) for ch in s)
if __name__ == '__main__':
    key = load_key(sys.argv[2])
    import os
    print('# Mechanical decryption of', os.path.basename(sys.argv[1]), 'with', os.path.basename(sys.argv[2]))
    print('# id\tpage\tdecryption')
    for line in open(sys.argv[1], encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        rid, page, signs = line.rstrip('\n').split('\t')
        print(f'{rid}\t{page}\t{dec(signs, key)}')
