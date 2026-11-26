"""Repeated n-grams, repeated dash groups and top bigrams of transcription.txt (quick statistics only)."""
import os
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
D = {'-', '.', '|'}
lines = [l.split(':', 1)[1].split() for l in open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8') if l.startswith('L')]
sg = [[t for t in ln if t not in D and t != '?'] for ln in lines]
for n in (4, 3):
    c = collections.Counter()
    for ln in sg:
        for i in range(len(ln) - n + 1):
            c[tuple(ln[i:i + n])] += 1
    print(n, [(' '.join(k), v) for k, v in c.items() if v > 1])
grp = collections.Counter()
for ln in lines:
    g = []
    for t in ln + ['-']:
        if t in D:
            if g:
                grp[' '.join(g)] += 1
            g = []
        else:
            g.append(t)
print('repeated dash groups', [(k, v) for k, v in grp.items() if v > 1])
b = collections.Counter()
for ln in sg:
    for a, c in zip(ln, ln[1:]):
        b[(a, c)] += 1
print(b.most_common(12))
