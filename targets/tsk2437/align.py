"""How much does the new transcription differ from the first attempt? Needleman-Wunsch per line on the sign streams
(dividers dropped) with a class-compatibility table (first-attempt merged classes -> new classes)."""
import os
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
DIV = {'-', '.', '|'}
COMPAT = {
    'J': {'J', 'Jd', 'I'}, 'L': {'L', 'J'}, 'U': {'U', 'u', 'Uc'}, 'N': {'N', 'C'}, 'B': {'B', 'R', 'r'}, 'C': {'R', 'r', 'C', 'B', 'U'},
    'P': {'P', 'U'}, 'Z': {'Z', 'M', 'S', 'X', 'Y'}, 'H': {'K', 'G', 'W', 'X', 'A', 'H', 'Y', 'M', 'I'}, 'S': {'S', 'b', 'd', 'Z'},
    'V': {'V', 'Ds', 'D', 'wd', 'o'}, 'O': {'O'}, 'c': {'c', 'o', 'wd', 'E', 'u', 'Uc', 'd', 'V'}, 'b': {'b', 'd', 'bb', 'b^', 'S'},
}


def read(p):
    return [[t for t in l.split(':', 1)[1].split() if t not in DIV] for l in open(os.path.join(HERE, p), encoding='utf-8') if l.startswith('L')]


old, new = read('transcription_first_attempt.txt'), read('transcription.txt')
tot = collections.Counter()
for a, b in zip(old, new):
    n, m = len(a), len(b)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = -i
    for j in range(1, m + 1):
        S[0][j] = -j

    def sc(x, y):
        if x == '?' or y == '?':
            return 0
        return 1 if y in COMPAT.get(x, {x}) else -1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i - 1][j - 1] + sc(a[i - 1], b[j - 1]), S[i - 1][j] - 1, S[i][j - 1] - 1)
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and S[i][j] == S[i - 1][j - 1] + sc(a[i - 1], b[j - 1]):
            s = sc(a[i - 1], b[j - 1])
            tot['compatible' if s == 1 else ('unknown (?)' if s == 0 else 'different class')] += 1
            i -= 1
            j -= 1
        elif i > 0 and S[i][j] == S[i - 1][j] - 1:
            tot['first-attempt sign with no counterpart'] += 1
            i -= 1
        else:
            tot['new sign (not in first attempt)'] += 1
            j -= 1
print(sum(len(x) for x in old), 'first-attempt signs;', sum(len(x) for x in new), 'new signs')
for k, v in tot.items():
    print('%-42s %d' % (k, v))
