"""Gronsfeld-type decryption over the 27-letter Spanish alphabet (with Ñ): each letter of a cipher word is shifted
back by the key digits in turn (3,1,3,3,1,3,...), restarting at every word.
python scripts/decrypt.py transcription.txt [key digits, default 313] > decryption.txt"""
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')
A = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
def dec_word(w, key):
    out = []
    for i, ch in enumerate(w):
        up = ch.upper()
        if up not in A:
            out.append(ch); continue
        p = A[(A.index(up) - key[i % len(key)]) % 27]
        out.append(p)
    return ''.join(out)
def dec(s, key):
    return re.sub(r'[A-Za-zÑñ]+', lambda m: dec_word(m.group(0), key), s)
if __name__ == '__main__':
    key = [int(c) for c in (sys.argv[2] if len(sys.argv) > 2 else '313')]
    print('# Mechanical decryption of', os.path.basename(sys.argv[1]), 'with key', ''.join(map(str, key)))
    print('# id\tpage\tdecryption')
    for line in open(sys.argv[1], encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        rid, page, signs = line.rstrip('\n').split('\t')
        print(f'{rid}\t{page}\t{dec(signs, key)}')
