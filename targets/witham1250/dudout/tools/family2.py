# LCS (subsequence) of Witham vs each sibling, vs shuffled-Witham null (n=5000). stdlib only.
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus import TARGETS, SIBLINGS, CONTROLS
random.seed(20261111)
def lcs(a, b):
    p = [0]*(len(b)+1)
    for x in a:
        c = [0]
        for j, y in enumerate(b):
            c.append(p[j]+1 if x == y else max(p[j+1], c[j]))
        p = c
    return p[-1]
def lcs_str(a, b):
    n, m = len(a), len(b); T = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            T[i+1][j+1] = T[i][j]+1 if a[i] == b[j] else max(T[i][j+1], T[i+1][j])
    out = []; i, j = n, m
    while i and j:
        if a[i-1] == b[j-1]: out.append(a[i-1]); i -= 1; j -= 1
        elif T[i-1][j] >= T[i][j-1]: i -= 1
        else: j -= 1
    return "".join(reversed(out))
N = 5000
def main():
  for t in ["witham_BL", "witham_new"]:
    s = TARGETS[t]; print(t, s)
    for k, (v, src) in SIBLINGS.items():
        if len(v) < 9: continue
        obs = lcs(s, v); l = list(s); ge = 0
        for _ in range(N):
            random.shuffle(l); ge += lcs("".join(l), v) >= obs
        print("  %-14s LCS %2d %-14s p=%.4f" % (k, obs, lcs_str(s, v), (ge+1)/(N+1)))

if __name__ == "__main__":
    main()
