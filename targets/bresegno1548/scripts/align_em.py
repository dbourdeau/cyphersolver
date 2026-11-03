"""Segmental EM alignment of a sign transcription against the contemporary decipherment.

Each cipher token emits a piece of the plaintext of length 0..K (0 = null). The token -> piece table is learned by EM
(soft counts, then hard Viterbi passes). Monotone alignment over the whole letter, banded.

Usage: python -E -P align_em.py <transcription.txt> <clear.txt> <out_prefix> [first_line last_line]
Writes <out_prefix>_pairs.tsv (token, piece, line) and <out_prefix>_table.tsv (token, piece, count).
"""
import math
import re
import sys
from collections import defaultdict

K = 4
BAND = 220


def norm_token(t):
    t = t.strip()
    if not t or (t.startswith('~') and t.endswith('~')):
        return None
    t = t.replace('?', '')
    t = re.sub(r'^\.', '', t)          # dot left of a sign
    t = re.sub(r'\.$', '', t)          # trailing dot
    if t in ('', ';', ','):
        return None
    return t


def load_tokens(path, lo=1, hi=99):
    toks = []
    for line in open(path, encoding='utf-8'):
        if not re.match(r'^L\d\d\t', line):
            continue
        ln = int(line[1:3])
        if not lo <= ln <= hi:
            continue
        for t in line.split('\t', 1)[1].split():
            n = norm_token(t)
            if n:
                toks.append((n, ln))
    return toks


def load_plain(path):
    s = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('P'):
            s.append(line.split('\t', 1)[1])
    s = ' '.join(s).lower()
    s = s.replace('v. ex.', 'X').replace('mag.', 'M').replace('ñ', 'n').replace('ç', 'z')
    return re.sub(r'[^a-zXM]', '', s)


def lenprior(n):
    return [0.03, 0.45, 0.40, 0.10, 0.02][n]


def run(toks, P, iters_soft=12, iters_hard=6):
    T, N = len(toks), len(P)
    table = defaultdict(lambda: defaultdict(float))

    def logp(tok, piece):
        # length: token's own length counts with a prior of weight 4; piece given length: counts with prior 25^-len
        d = table[tok]
        n = len(piece)
        tot = sum(d.values())
        cl = sum(c for s_, c in d.items() if len(s_) == n)
        pl = (cl + 4 * lenprior(n)) / (tot + 4)
        ps = (d.get(piece, 0.0) + 0.3 * (1.0 / 25) ** n) / (cl + 0.3)
        return math.log(pl) + math.log(ps)

    def window(j):
        c = j * N / T
        return max(0, int(c - BAND)), min(N, int(c + BAND))

    for it in range(iters_soft + iters_hard):
        hard = it >= iters_soft
        NEG = -1e18
        F = [dict() for _ in range(T + 1)]
        F[0][0] = 0.0
        back = [dict() for _ in range(T + 1)]
        for j in range(T):
            tok = toks[j][0]
            lo, hi = window(j + 1)
            for i, f in F[j].items():
                for k in range(K + 1):
                    i2 = i + k
                    if i2 > N or i2 < lo or i2 > hi:
                        continue
                    v = f + logp(tok, P[i:i2])
                    if hard:
                        if v > F[j + 1].get(i2, NEG):
                            F[j + 1][i2] = v
                            back[j + 1][i2] = i
                    else:
                        o = F[j + 1].get(i2)
                        F[j + 1][i2] = v if o is None else max(o, v) + math.log1p(math.exp(-abs(o - v)))
        if N not in F[T]:
            raise SystemExit('no alignment reaches the end; widen BAND')
        if hard:
            segs = []
            i = N
            for j in range(T, 0, -1):
                p = back[j][i]
                segs.append(P[p:i])
                i = p
            segs.reverse()
            table = defaultdict(lambda: defaultdict(float))
            for (tok, _), s in zip(toks, segs):
                table[tok][s] += 1
        else:
            B = [dict() for _ in range(T + 1)]
            B[T][N] = 0.0
            for j in range(T - 1, -1, -1):
                tok = toks[j][0]
                for i in F[j]:
                    acc = None
                    for k in range(K + 1):
                        i2 = i + k
                        if i2 in B[j + 1]:
                            v = logp(tok, P[i:i2]) + B[j + 1][i2]
                            acc = v if acc is None else max(acc, v) + math.log1p(math.exp(-abs(acc - v)))
                    if acc is not None:
                        B[j][i] = acc
            Z = F[T][N]
            new = defaultdict(lambda: defaultdict(float))
            for j in range(T):
                tok = toks[j][0]
                for i, f in F[j].items():
                    for k in range(K + 1):
                        i2 = i + k
                        if i2 in B[j + 1]:
                            w = math.exp(f + logp(tok, P[i:i2]) + B[j + 1][i2] - Z)
                            if w > 1e-4:
                                new[tok][P[i:i2]] += w
            table = new
        print('iter', it, 'hard' if hard else 'soft', 'logZ', round(F[T][N], 1), file=sys.stderr)
    return segs, table


def main():
    tr, cl, out = sys.argv[1:4]
    lo, hi = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (1, 99)
    toks = load_tokens(tr, lo, hi)
    P = load_plain(cl)
    print(len(toks), 'tokens', len(P), 'letters', file=sys.stderr)
    segs, table = run(toks, P)
    with open(out + '_pairs.tsv', 'w', encoding='utf-8') as f:
        for (tok, ln), s in zip(toks, segs):
            f.write(f'L{ln:02d}\t{tok}\t{s or "-"}\n')
    with open(out + '_table.tsv', 'w', encoding='utf-8') as f:
        for tok in sorted(table, key=lambda t: -sum(table[t].values())):
            d = table[tok]
            f.write(tok + '\t' + ' '.join(f'{s or "-"}:{int(c)}' for s, c in sorted(d.items(), key=lambda x: -x[1])) + '\n')


if __name__ == '__main__':
    main()
