"""Project re-check of Harumi-Matsuba's decipherment (issue #370), written here from the description in the issue,
not from the contributor's decrypt.py.

5 x 6 table, one digit pair per letter; pairs written row by row into an N x N square (N/2 pairs to a row),
sent column by column. Nr 451: N = 40, columns first/second digit, rows read right to left.
Nr 523: N = 24, columns second/first digit, rows read left to right.

    python targets/krassin1921/verify.py          # prints both decryptions
    python targets/krassin1921/verify.py --write  # also writes decryption_451.txt and decryption_523.txt
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TABLE = {'6': 'евьэкщ', '7': 'афязнр', '8': 'быглчю', '9': 'ж?шидо', '0': '?тпхум'}
EXTRA = {'06': 'с', '10': '.', '33': ',', '00': ''}


def value(p):
    if p in EXTRA:
        return EXTRA[p]
    a, b = p
    if a in TABLE and b in '012345' and TABLE[a][int(b)] != '?':
        return TABLE[a][int(b)]
    return '[%s]' % p


def digits(name):
    with open(os.path.join(HERE, name), encoding='utf-8') as f:
        return ''.join(c for line in f if not line.startswith('#') for c in line if c.isdigit())


def decrypt(name, n, mirrored):
    s = digits(name)
    s += '?' * (n * n - len(s))
    cols = [s[i * n:(i + 1) * n] for i in range(n)]
    out = []
    for r in range(n):
        if mirrored:
            out += [cols[2 * j + 1][r] + cols[2 * j][r] for j in range(n // 2)]
        else:
            out += [cols[2 * j][r] + cols[2 * j + 1][r] for j in range(n // 2)][::-1]
    while out and out[-1] in ('00', '?0'):
        out.pop()
    return ''.join(value(p) for p in out)


if __name__ == '__main__':
    for num, n, mir in (('451', 40, False), ('523', 24, True)):
        text = decrypt('ciphertext_%s.txt' % num, n, mir)
        print('Nr', num)
        print(text)
        if '--write' in sys.argv:
            with open(os.path.join(HERE, 'decryption_%s.txt' % num), 'w', encoding='utf-8') as f:
                f.write(text + '\n')
