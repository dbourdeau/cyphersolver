"""Own decoder for the claimed rule c = p - (2*(k mod 13)+1) mod 26 (A=0). Run: python3 -I decode.py
Reads cipher.txt, key.txt, plaintext.txt next to this script; stdlib only."""
import re, hashlib, random, os, sys
D = os.path.dirname(os.path.abspath(__file__))
def L(name):
    s = open(os.path.join(D, name), encoding='utf-8').read()
    return [ord(ch) - 65 for ch in re.sub(r'[^A-Z]', '', s.upper())]
c, k, p = L('cipher.txt'), L('key.txt'), L('plaintext.txt')
S = lambda v: ''.join(chr(65 + x) for x in v)
print('lengths', len(c), len(k), len(p), 'sha256(cipher letters)', hashlib.sha256(S(c).encode()).hexdigest())
n = 499
shift = lambda i: 2 * (k[i] % 13) + 1
# Decipher: p = c + shift
dec = [(c[i] + shift(i)) % 26 for i in range(n)]
enc = [(p[i] - shift(i)) % 26 for i in range(n)]
miss = [i for i in range(n) if enc[i] != c[i]]
print('plaintext letters reproduced by rule:', n - len(miss), 'of', n)
print('misses (1-based):', [i + 1 for i in miss])
for i in miss:
    ok = any((p[i] - 2 * kk - 1) % 26 == c[i] for kk in range(13))
    print(' ', i + 1, 'cipher', chr(65 + c[i]), 'rule gives', chr(65 + enc[i]), 'plain', chr(65 + p[i]), 'key', chr(65 + k[i]),
          'deciphered', chr(65 + dec[i]), '| some key letter could give it' if ok else '| no key letter can give it (parity)')
# odd shift positions: (p - c) mod 26 odd
odd = sum(((p[i] - c[i]) % 26) % 2 == 1 for i in range(n))
print('positions with odd (plain - cipher):', odd, 'of', n)
# spelling variants: pretenses / dispatches
var = {68: 'S', 456: 'I'}  # pretenSes (C->S), dIspatches (E->I); 0-based 68 and 456
p2 = p[:]; 
for i, ch in var.items(): p2[i] = ord(ch) - 65
enc2 = [(p2[i] - shift(i)) % 26 for i in range(n)]
print('with American spellings at 69 and 457:', sum(enc2[i] == c[i] for i in range(n)), 'of', n)
# controls
print('plaintext shifted one place:', sum((p[i + 1] - shift(i)) % 26 == c[i] for i in range(n - 1)), 'of 498')
print('key shifted one place:', sum((p[i] - (2 * (k[i + 1] % 13) + 1)) % 26 == c[i] for i in range(n - 1)), 'of 498')
random.seed(20261112)
best = 0; bo = 0; tot = []
for _ in range(2000):
    sh = c[:]; random.shuffle(sh)
    m = sum(enc[i] == sh[i] for i in range(n)); best = max(best, m)
    o = sum(((p[i] - sh[i]) % 26) % 2 == 1 for i in range(n)); bo = max(bo, o)
print('2000 shuffles of the ciphertext: max exact matches', best, ', max odd-shift positions', bo)
# parity alternation signal
alt = sum((c[i] - c[i + 1]) % 2 == 1 for i in range(n - 1)); print('adjacent cipher letters of opposite parity:', alt, 'of 498')
print(S(dec)[:140].lower())
