"""Decrypt the message of 4 June 1940 (frames 0863-0867) with the keys of the day.

  python solver/decrypt.py transcription.txt

Double columnar transposition, irregular grids. Encipherment: plaintext written in rows under K1 (19 columns),
read off column by column in the order of the key numbers; the result written in rows under K2 (22 columns) and read
off the same way. Decryption undoes K2, then K1. The first five-letter group of each part is the indicator group
and is removed first. Each part is enciphered on its own.
"""
import sys

K1 = [9, 14, 17, 1, 12, 6, 18, 3, 16, 10, 4, 8, 19, 13, 7, 2, 11, 15, 5]
K2 = [19, 22, 9, 17, 1, 12, 7, 16, 21, 13, 10, 20, 4, 18, 2, 15, 6, 3, 8, 11, 5, 14]

def order(key):
    """Column indices in reading order (key number 1 first; ties left to right)."""
    return sorted(range(len(key)), key=lambda i: (key[i], i))

def undo(ct, key):
    o = order(key); n, k = len(ct), len(key)
    rows = -(-n // k); full = n % k or k
    pt = [None] * n; p = 0
    for c in o:
        for r in range(rows if c < full else rows - 1):
            pt[r * k + c] = ct[p]; p += 1
    return ''.join(pt)

def encipher(pt, key):
    o = order(key); n, k = len(pt), len(key)
    return ''.join(pt[r * k + c] for c in o for r in range(-(-n // k)) if r * k + c < n)

def parts(path):
    for line in open(path, encoding='utf-8'):
        if line.startswith('P'):
            head, groups = line.split('|')
            yield head.split()[0], ''.join(groups.split())

if __name__ == '__main__':
    for name, ct in parts(sys.argv[1] if len(sys.argv) > 1 else 'transcription.txt'):
        body = ct[5:]
        pt = undo(undo(body, K2), K1)
        assert encipher(encipher(pt, K1), K2) == body
        print(name, pt.upper())
