"""Align a cluster-label glyph sequence to a known plaintext and read off the key.

Iterated Needleman-Wunsch: start from a proportional monotone alignment, derive for each glyph cluster
its most frequent partner letter, re-align with that mapping as the score, repeat to a fixed point.
Each cluster may take only one letter; a letter may have several clusters (homophones).

usage: python3 align.py SEQFILE PLAINTEXT
"""
import sys, collections

def dp(G, P, score, gap=-1.2):
    n, m = len(G), len(P)
    F = [[0.0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1): F[i][0] = F[i-1][0] + gap
    for j in range(1, m+1): F[0][j] = F[0][j-1] + gap
    for i in range(1, n+1):
        for j in range(1, m+1):
            F[i][j] = max(F[i-1][j-1] + score(G[i-1], P[j-1]), F[i-1][j] + gap, F[i][j-1] + gap)
    i, j, al = n, m, []
    while i > 0 and j > 0:
        if F[i][j] == F[i-1][j-1] + score(G[i-1], P[j-1]):
            al.append((i-1, j-1)); i -= 1; j -= 1
        elif F[i][j] == F[i-1][j] + gap: i -= 1
        else: j -= 1
    return list(reversed(al)), F[n][m]

if __name__ == '__main__':
    seq = []
    for line in open(sys.argv[1]):
        if line.startswith('L'): seq.extend(list(line.split('\t')[1].strip()))
    P = sys.argv[2]
    G = seq
    print(f'glyphs={len(G)} plain={len(P)}')
    al = [(i, min(len(P)-1, round(i*(len(P)-1)/max(1,len(G)-1)))) for i in range(len(G))]
    mapping = {}
    for it in range(12):
        cnt = collections.defaultdict(collections.Counter)
        for gi, pj in al: cnt[G[gi]][P[pj]] += 1
        mapping = {g: c.most_common(1)[0][0] for g, c in cnt.items()}
        def sc(g, p): return 1.0 if mapping.get(g) == p else -0.6
        al, s = dp(G, P, sc)
        hit = sum(1 for gi, pj in al if mapping.get(G[gi]) == P[pj])
        print(f'iter {it}: aligned={len(al)} consistent={hit} ({100*hit/max(1,len(al)):.1f}%) score={s:.1f}')
    cnt = collections.defaultdict(collections.Counter)
    for gi, pj in al: cnt[G[gi]][P[pj]] += 1
    print('\ncluster -> letter (count, purity):')
    for g in sorted(cnt, key=lambda g: -sum(cnt[g].values())):
        c = cnt[g]; tot = sum(c.values()); best, bn = c.most_common(1)[0]
        print(f'  {g}: {best}  n={tot} purity={bn}/{tot}' + ('' if bn == tot else '  spread=' + str(dict(c))))
    out = ''.join(mapping.get(g, '?') for g in G)
    print('\ndecode of the glyph stream with the derived key:\n' + out)
