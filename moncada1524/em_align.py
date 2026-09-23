"""EM crib alignment of the Moncada 1524 cipher runs (ct.txt) against the CODOIN XXIV decipherment.

Each sign emits one letter, two letters (a syllable or a doubled letter), or nothing (null); a plaintext
letter may also be skipped by the encipherer. '....' in a plaintext marks the printed gap: any number of
signs there emit unknown letters at a flat cost. EM re-estimates P(letters | sign) and prints the key
and each run's alignment.
"""
import math, re, sys
from collections import defaultdict

def load(path='ct.txt'):
    runs = []
    for line in open(path, encoding='utf-8'):
        if not line.startswith('RUN'):
            continue
        _, toks, plain = [x.strip() for x in line.split('|')]
        rid = line.split('|')[0].split()[1]
        runs.append((rid, toks.split(), plain))
    return runs

def norm(p):
    p = p.lower().replace('ñ', 'n~')
    out = []
    i = 0
    while i < len(p):
        if p.startswith('n~', i):
            out.append('ñ'); i += 2
        elif p.startswith('....', i):
            out.append('*'); i += 4
        elif p[i].isalpha():
            out.append({'j': 'i', 'v': 'u'}.get(p[i], p[i])); i += 1
        else:
            i += 1
    return out

SKIP, NULL, GAPTOK, TWO = math.log(0.02), math.log(0.03), math.log(0.2), math.log(0.05)

def align(toks, plain, emit):
    """Viterbi over (token index, plain index). Returns cost and list of (token, letters)."""
    n, m = len(toks), len(plain)
    NEG = -1e18
    best = [[NEG] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]
    best[0][0] = 0.0
    def lp(t, s):
        return math.log(emit[t].get(s, 1e-4))
    for i in range(n + 1):
        for j in range(m + 1):
            v = best[i][j]
            if v == NEG:
                continue
            # skip a plaintext letter
            if j < m and plain[j] != '*':
                c = v + SKIP
                if c > best[i][j + 1]:
                    best[i][j + 1], back[i][j + 1] = c, (i, j, None, '')
            if j < m and plain[j] == '*':
                # leave the gap
                if v > best[i][j + 1]:
                    best[i][j + 1], back[i][j + 1] = v, (i, j, None, '')
                if i < n:  # a sign inside the gap
                    c = v + GAPTOK
                    if c > best[i + 1][j]:
                        best[i + 1][j], back[i + 1][j] = c, (i, j, toks[i], '?')
                continue
            if i < n:
                t = toks[i]
                c = v + NULL + lp(t, '')
                if c > best[i + 1][j]:
                    best[i + 1][j], back[i + 1][j] = c, (i, j, t, '')
                if j < m:
                    c = v + lp(t, plain[j])
                    if c > best[i + 1][j + 1]:
                        best[i + 1][j + 1], back[i + 1][j + 1] = c, (i, j, t, plain[j])
                if j + 1 < m and plain[j + 1] != '*':
                    s = plain[j] + plain[j + 1]
                    c = v + TWO + lp(t, s)
                    if c > best[i + 1][j + 2]:
                        best[i + 1][j + 2], back[i + 1][j + 2] = c, (i, j, t, s)
    path = []
    i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, t, s = back[i][j]
        if t is not None:
            path.append((t, s))
        else:
            path.append((None, plain[pj] if plain[pj] != '*' else ''))
        i, j = pi, pj
    return best[n][m], path[::-1]

def main():
    runs = [r for r in load() if r[2] != '?']
    signs = sorted({t for _, toks, _ in runs for t in toks})
    letters = sorted({c for _, _, p in runs for c in norm(p) if c != '*'})
    emit = {t: {c: 1.0 / len(letters) for c in letters} for t in signs}
    for it in range(12):
        counts = defaultdict(lambda: defaultdict(float))
        total = 0
        for rid, toks, p in runs:
            cost, path = align(toks, norm(p), emit)
            total += cost
            for t, s in path:
                if t is not None and s != '?':
                    counts[t][s] += 1
        for t in signs:
            tot = sum(counts[t].values()) + 0.5
            emit[t] = {s: (c + 0.01) / tot for s, c in counts[t].items()}
            emit[t].setdefault('', 0.01 / tot)
        print(f'iter {it} logp {total:.1f}', file=sys.stderr)
    print('KEY (sign: letters x count)')
    for t in signs:
        items = sorted(counts[t].items(), key=lambda x: -x[1])
        print(f'  {t:4s}', ', '.join(f"{s or '∅'}x{int(c)}" for s, c in items))
    print()
    for rid, toks, p in runs:
        _, path = align(toks, norm(p), emit)
        print(f'RUN {rid}:', ' '.join(f"{t}={s or '∅'}" if t else f"[-{s}]" for t, s in path))
    best = {t: max(counts[t].items(), key=lambda x: x[1])[0] if counts[t] else '?' for t in signs}
    print()
    for rid, toks, p in load():
        if p == '?' or '....' in p:
            print(f'DECODE {rid}:', ' '.join(f"{t}={best.get(t, '?') or '∅'}" for t in toks))

if __name__ == '__main__':
    main()
