"""Search a consistent unit->string map aligning a unit sequence to a plaintext (exploration tool).
python align.py units_file plaintext maxlen"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.setrecursionlimit(10000)
units = open(sys.argv[1]).read().split()
plain = sys.argv[2]
ML = int(sys.argv[3])
best = [0, None]
def rec(i, j, m, nulls):
    if i > best[0]:
        best[0] = i; best[1] = (dict(m), j)
    if i == len(units):
        return j == len(plain)
    u = units[i]
    if u in m:
        s = m[u]
        if plain.startswith(s, j):
            return rec(i + 1, j + len(s), m, nulls)
        return False
    for L in range(1, ML + 1):
        s = plain[j:j + L]
        if len(s) < L: break
        m[u] = s
        if rec(i + 1, j + L, m, nulls): return True
        del m[u]
    return False
ok = rec(0, 0, {}, 0)
print('complete' if ok else 'partial', best[0], 'of', len(units))
m, j = best[1]
print('plain pos', j, plain[j:j+30])
for k in sorted(m, key=lambda x: m[x]): print(k, m[k])
