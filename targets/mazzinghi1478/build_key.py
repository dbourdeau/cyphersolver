"""Fit the sign -> letter key on the glossed sibling MAP LXXII 170 (t170.tsv) by hard-EM alignment.

    python build_key.py            fit on all glossed cipher words (conf h/m), write key.tsv
    python build_key.py --holdout  fit on 4/5 of the words, decode the held-out fifth and score it against its glosses

Each cipher token emits one plaintext letter, two letters (a sign for a double letter such as {ss} = ll), or nothing
(a null); a gloss letter may also stand unmatched (an abbreviation in the gloss). The first pass counts only words whose
token count equals their letter count; later passes realign every word with the current table by dynamic programming.
"""
import collections, csv, math, random, sys

HERE = __file__.rsplit('\\', 1)[0] if '\\' in __file__ else '.'


def letters(g):
    g = g.lower().replace('j', 'i').replace('v', 'u').replace('y', 'i')
    return [c for c in g if c.isalpha()]


def merge(toks):
    """'2 +' and '2 #' are one sign for l; '#' after {sg} or m is h (glyphs.md, recheck 6 Nov)."""
    out, i = [], 0
    while i < len(toks):
        if toks[i] == '2' and i + 1 < len(toks) and toks[i + 1] in ('+', '#'):
            out.append('{l}'); i += 2
        elif toks[i] == '#' and out and out[-1] in ('{sg}', 'm'):
            out.append('{ch}'); i += 1  # the double cross after c or g is h (recheck, 6 Nov)
        else:
            out.append(toks[i]); i += 1
    return out


def load(path, confs=('h', 'm')):
    out = []
    for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'):
        if r['kind'] != 'C' or not r['gloss'] or r['conf'] not in confs or '?' in r['gloss']:
            continue
        out.append((r['line'], r['pos'], merge(r['cipher'].split()), letters(r['gloss'])))
    return out


def align(toks, lets, P):
    """Best monotone alignment; returns list of (token, emitted letters)."""
    INF = float('inf')
    n, m = len(toks), len(lets)
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] == INF:
                continue
            if j < m:  # gloss letter with no sign (abbreviation)
                c = D[i][j] + 4.0
                if c < D[i][j + 1]: D[i][j + 1], B[i][j + 1] = c, (i, j, None, '')
            if i < n:
                t = toks[i]
                for k, cost0 in ((0, 3.0), (1, 0.0), (2, 1.5)):
                    if j + k > m: continue
                    e = ''.join(lets[j:j + k])
                    c = D[i][j] + cost0 - math.log(P[t].get(e, 0) + 1e-3)
                    if c < D[i + 1][j + k]: D[i + 1][j + k], B[i + 1][j + k] = c, (i, j, t, e)
    path, i, j = [], n, m
    while (i, j) != (0, 0):
        pi, pj, t, e = B[i][j]
        if t is not None: path.append((t, e))
        i, j = pi, pj
    return path[::-1], D[n][m]


def fit(pairs, rounds=8):
    C = collections.defaultdict(collections.Counter)
    for _, _, t, l in pairs:
        if len(t) == len(l):
            for a, b in zip(t, l): C[a][b] += 1
    for _ in range(rounds):
        P = {t: {e: n / sum(c.values()) for e, n in c.items()} for t, c in C.items()}
        P = collections.defaultdict(dict, P)
        C = collections.defaultdict(collections.Counter)
        for _, _, t, l in pairs:
            path, _ = align(t, l, P)
            for a, e in path: C[a][e] += 1
    return C


def decode(toks, C):
    return ''.join((C[t].most_common(1)[0][0] if C.get(t) else '?') or '' for t in toks)


if __name__ == '__main__':
    pairs = load('t170.tsv')
    if '--holdout' in sys.argv:
        random.seed(1478)
        random.shuffle(pairs)
        k = len(pairs) // 5
        test, train = pairs[:k], pairs[k:]
        C = fit(train)
        ok = tot = wok = 0
        for ln, pos, t, l in test:
            d = decode(t, C)
            g = ''.join(l)
            sm = sum(a == b for a, b in zip(d, g))
            ok += sm; tot += max(len(g), len(d)); wok += d == g
            print(f'{ln}/{pos}\t{" ".join(t)}\t{d}\t{g}')
        print(f'held-out: {len(test)} words, {wok} exact, letters {ok}/{tot} = {ok / tot:.0%}')
    else:
        C = fit(pairs)
        with open('key.tsv', 'w', encoding='utf-8') as f:
            f.write('token\tvalue\tcount\talternatives\n')
            for t in sorted(C, key=lambda x: -sum(C[x].values())):
                (v, n), *rest = C[t].most_common()
                f.write(f'{t}\t{v or "(null)"}\t{n}\t{" ".join(f"{e or 0}:{c}" for e, c in rest)}\n')
        print(len(pairs), 'pairs;', len(C), 'tokens -> key.tsv')
