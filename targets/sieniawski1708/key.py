"""The Vienna -> Schenck letter cipher (1706): numbers 7-78 in blocks of three, alphabetical.

a = 7 8 9, b = 10 11 12, c = 13 14 15, ... z = 76 77 78  (alphabet a-i, k-u, w-z: 24 letters, no j, no v).
Found here by a monotone (alphabetical-block) key search on the runs, then fixed as the exact 3-per-letter rule.
"""
ALPH = 'abcdefghiklmnopqrstuwxyz'

def letter(n):
    n = int(n)
    if 7 <= n <= 78:
        return ALPH[(n - 7) // 3]
    return None

def table():
    return {ALPH[i]: [7 + 3 * i, 8 + 3 * i, 9 + 3 * i] for i in range(len(ALPH))}

if __name__ == '__main__':
    for k, v in table().items():
        print(k, v)
