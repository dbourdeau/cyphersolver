"""Decryption of the Wellington letter runs with Narvaez's key 313 (rule only; see NOTES.md for the citation).
Alphabet of 27 letters A-N, Ñ, O-Z; cipher = plain + 3, +1, +3, repeating; so plain = cipher - 3, -1, -3, ...
The cycle starts with 3 at the first letter of each run and continues across line breaks ("/").
"?" (an unsure or unreadable sign) holds its place: it advances the cycle and is output as "?".
python scripts/decrypt.py transcription_DCXXI.6.588.1.txt > decryption_DCXXI.6.588.1.txt"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
A = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
KEY = [3, 1, 3]
def dec(run, key=KEY):
    out, j = [], 0
    for ch in run:
        if ch in A:
            out.append(A[(A.index(ch) - key[j % len(key)]) % 27]); j += 1
        elif ch == '?':
            out.append('?'); j += 1
        else:
            out.append(ch)
    return ''.join(out)
def runs(path):
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        rid, para, before, signs = line.rstrip('\n').split('\t')
        yield rid, para, before, signs
if __name__ == '__main__':
    print('# Mechanical decryption of', os.path.basename(sys.argv[1]), 'with key 313 (cycle restarts at each run)')
    print('# id\tfolio.paragraph\tdecryption')
    for rid, para, before, signs in runs(sys.argv[1]):
        print(f'{rid}\t{para}\t{dec(signs)}')
