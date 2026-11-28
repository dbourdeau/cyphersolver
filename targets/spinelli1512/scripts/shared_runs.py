# Longest common runs of cipher signs between letter A and letter B (ciphertext only; no values used).
import sys, difflib
d = {}
for l in open(sys.argv[1]):
    a, b = l.rstrip('\n').split('\t'); d.setdefault(a[0], []).extend([t.rstrip('?') for t in b.split() if t != '{clear}'] + ['|'])
A, B = d['A'], d['B']; seen = []
for n in range(12, 4, -1):
    gA = {tuple(A[i:i+n]): i for i in range(len(A)-n+1) if '|' not in A[i:i+n]}
    for j in range(len(B)-n+1):
        t = tuple(B[j:j+n])
        if t in gA and not any(set(range(j, j+n)) & s for s in seen):
            seen.append(set(range(j, j+n))); print(n, 'A@', gA[t], 'B@', j, ' '.join(t))
