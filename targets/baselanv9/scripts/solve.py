"""Key recovery from ADJACENT PLAINTEXT, TRAIN leaves only (ff. 4r, 4v) against the clear copy (ff. 101r-102r).
Reads ONLY tx/f004r.txt, tx/f004v.txt and tx/CLEAR_TRAIN.txt. Never opens a held-out file.

1. Word alignment (cipher words <-> clear words) by dynamic programming: match, merge of two cipher words (a word
   broken at a line end), skip of a cipher word or a clear word. Round 0 scores pairs by length only; later rounds by
   the emission model.
2. Emission model by EM (forward-backward over segmentations): each token emits a string of 0-3 letters
   (modifier tokens 0-2). Tokens: base signs, with dot above (+^), dot below (+_) and diaeresis (+") split off.
3. Key = for each token the string it emits most often in the final Viterbi alignments.
4. Two context rules are tested on the training alignments and adopted only if they hold in >= 70% of cases:
   D2 = the nearest preceding vowel of the word; +" = repeat what the sign before it emitted.
Writes KEY.tsv, work/train_alignment.tsv, SOLVE_LOG.md (appends)."""
import sys, math, collections, json, os
sys.path.insert(0, os.path.dirname(__file__))
from common import read_tx, words_with_joins, read_clear

D = '/home/claude/keyless/round40c/basel_anv9/'
TRAIN = ['tx/f004r.txt', 'tx/f004v.txt']
VOW = set('aeiou')

C = []
for f in TRAIN:
    C += words_with_joins(read_tx(D + f))
W = read_clear(D + 'tx/CLEAR_TRAIN.txt')
cw = [w['tokens'] for w in C]

PRIOR = {0: 0.10, 1: 0.60, 2: 0.18, 3: 0.08, 4: 0.04}
ALPHA = 0.5


def maxlen(t):
    return 2 if t.startswith('+') else 4


class Model:
    def __init__(self):
        self.cnt = collections.defaultdict(lambda: collections.Counter())

    def p(self, t, s):
        c = self.cnt.get(t)
        base = PRIOR.get(len(s), 0) / (26 ** len(s))
        if not c:
            return base
        tot = sum(c.values())
        return (c[s] + ALPHA * base) / (tot + ALPHA)


def fb(model, toks, w, collect=None):
    n, m = len(toks), len(w)
    A = [[0.0] * (m + 1) for _ in range(n + 1)]
    A[0][0] = 1.0
    for i in range(1, n + 1):
        t = toks[i - 1]
        for j in range(m + 1):
            v = 0.0
            for k in range(0, min(maxlen(t), j) + 1):
                if A[i - 1][j - k]:
                    v += A[i - 1][j - k] * model.p(t, w[j - k:j])
            A[i][j] = v
    Z = A[n][m]
    if collect is None or Z <= 0:
        return Z
    B = [[0.0] * (m + 1) for _ in range(n + 1)]
    B[n][m] = 1.0
    for i in range(n - 1, -1, -1):
        t = toks[i]
        for j in range(m + 1):
            v = 0.0
            for k in range(0, min(maxlen(t), m - j) + 1):
                if B[i + 1][j + k]:
                    v += model.p(t, w[j:j + k]) * B[i + 1][j + k]
            B[i][j] = v
    for i in range(1, n + 1):
        t = toks[i - 1]
        for j in range(m + 1):
            for k in range(0, min(maxlen(t), j) + 1):
                a = A[i - 1][j - k]
                if a:
                    s = w[j - k:j]
                    q = a * model.p(t, s) * B[i][j] / Z
                    if q > 1e-9:
                        collect[t][s] += q
    return Z


def viterbi(model, toks, w):
    n, m = len(toks), len(w)
    V = [[-1e18] * (m + 1) for _ in range(n + 1)]
    P = [[None] * (m + 1) for _ in range(n + 1)]
    V[0][0] = 0.0
    for i in range(1, n + 1):
        t = toks[i - 1]
        for j in range(m + 1):
            for k in range(0, min(maxlen(t), j) + 1):
                if V[i - 1][j - k] > -1e17:
                    pp = model.p(t, w[j - k:j])
                    if pp <= 0:
                        continue
                    v = V[i - 1][j - k] + math.log(pp)
                    if v > V[i][j]:
                        V[i][j] = v; P[i][j] = k
    if V[n][m] < -1e17:
        return None, None
    segs = []
    j = m
    for i in range(n, 0, -1):
        k = P[i][j]
        segs.append(w[j - k:j]); j -= k
    return V[n][m], list(reversed(segs))


def pair_cost(model, toks, w, rnd):
    if rnd == 0:
        exp = sum(0.9 if t.startswith('+') else 1.35 for t in toks)
        return 1.2 * abs(len(w) - exp)
    Z = fb(model, toks, w)
    if Z <= 0:
        return 50.0
    return -math.log(Z) / (len(w) + 1)


def align_words(model, rnd):
    N, M = len(cw), len(W)
    SKIP = 3.5 if rnd == 0 else 4.0
    INF = 1e18
    cost = [[INF] * (M + 1) for _ in range(N + 1)]
    back = [[None] * (M + 1) for _ in range(N + 1)]
    cost[0][0] = 0.0
    band = 40
    for i in range(N + 1):
        jc = int(i * M / max(1, N))
        for j in range(max(0, jc - band), min(M, jc + band) + 1):
            c0 = cost[i][j]
            if c0 >= INF:
                continue
            if i < N and j < M:
                v = c0 + pair_cost(model, cw[i], W[j], rnd)
                if v < cost[i + 1][j + 1]:
                    cost[i + 1][j + 1] = v; back[i + 1][j + 1] = ('m', i, j)
            if i + 1 < N and j < M:
                v = c0 + pair_cost(model, cw[i] + cw[i + 1], W[j], rnd) + 0.6
                if v < cost[i + 2][j + 1]:
                    cost[i + 2][j + 1] = v; back[i + 2][j + 1] = ('g', i, j)
            if i < N:
                v = c0 + SKIP
                if v < cost[i + 1][j]:
                    cost[i + 1][j] = v; back[i + 1][j] = ('c', i, j)
            if j < M:
                v = c0 + SKIP
                if v < cost[i][j + 1]:
                    cost[i][j + 1] = v; back[i][j + 1] = ('w', i, j)
    i, j = N, M
    ops = []
    while (i, j) != (0, 0):
        op = back[i][j]
        ops.append(op)
        if op[0] == 'm':
            i, j = i - 1, j - 1
        elif op[0] == 'g':
            i, j = i - 2, j - 1
        elif op[0] == 'c':
            i -= 1
        else:
            j -= 1
    ops.reverse()
    pairs = []
    for op in ops:
        if op[0] == 'm':
            pairs.append(([op[1]], op[2]))
        elif op[0] == 'g':
            pairs.append(([op[1], op[1] + 1], op[2]))
        elif op[0] == 'c':
            pairs.append(([op[1]], None))
        else:
            pairs.append(([], op[2]))
    return pairs


def em(pairs_tw, iters=15):
    model = Model()
    for it in range(iters):
        coll = collections.defaultdict(lambda: collections.Counter())
        for toks, w in pairs_tw:
            fb(model, toks, w, coll)
        model.cnt = coll
    return model


log = []
model = Model()
for rnd in range(4):
    pairs = align_words(model, rnd)
    pt = [(sum((cw[i] for i in ci), []), W[j]) for ci, j in pairs if ci and j is not None]
    model = em(pt, 15)
    nm = sum(1 for ci, j in pairs if ci and j is not None)
    nc = sum(1 for ci, j in pairs if ci and j is None)
    nw = sum(1 for ci, j in pairs if not ci)
    log.append('round %d: %d aligned pairs, %d cipher words unpaired, %d clear words unpaired' % (rnd, nm, nc, nw))

# final Viterbi alignments; drop pairs whose per-letter cost is poor (variant words, abbreviations)
rows, used = [], collections.defaultdict(lambda: collections.Counter())
bad = 0
for ci, j in pairs:
    if not ci or j is None:
        continue
    toks = sum((cw[i] for i in ci), [])
    w = W[j]
    sc, segs = viterbi(model, toks, w)
    pl = (-sc / (len(w) + 1)) if sc is not None else 99
    ok = sc is not None and pl < 2.5
    if not ok:
        bad += 1
    rows.append((ci, j, toks, w, segs, pl, ok))
    if ok:
        for t, s in zip(toks, segs):
            used[t][s] += 1
log.append('final: %d pairs, %d kept (per-letter cost < 2.5), %d dropped as non-aligning' % (len(rows), len(rows) - bad, bad))

# context rules
d2_tot = d2_prev = d2_any = 0
dbl_tot = dbl_copy = 0
for ci, j, toks, w, segs, pl, ok in rows:
    if not ok:
        continue
    pos = 0
    for k, (t, s) in enumerate(zip(toks, segs)):
        if t == 'D2' and len(s) == 1:
            d2_tot += 1
            prev = [c for c in w[:pos] if c in VOW]
            if prev and prev[-1] == s:
                d2_prev += 1
            if s in prev:
                d2_any += 1
        if t == '+"':
            dbl_tot += 1
            if k > 0 and s and s == segs[k - 1][-len(s):]:
                dbl_copy += 1
        pos += len(s)
rule_d2 = d2_tot > 0 and d2_prev / d2_tot >= 0.70
rule_dbl = dbl_tot > 0 and dbl_copy / dbl_tot >= 0.70
log.append('rule D2 = nearest preceding vowel: %d of %d (%.0f%%); any earlier vowel of the word: %d of %d -> %s'
           % (d2_prev, d2_tot, 100 * d2_prev / max(1, d2_tot), d2_any, d2_tot, 'ADOPTED' if rule_d2 else 'not adopted'))
log.append('rule +" = repeat the preceding sign\'s letter: %d of %d -> %s'
           % (dbl_copy, dbl_tot, 'ADOPTED' if rule_dbl else 'not adopted'))

# key
key = []
for t in sorted(used, key=lambda x: (-sum(used[x].values()), x)):
    c = used[t]
    tot = sum(c.values())
    s, n = c.most_common(1)[0]
    alts = '; '.join('%s:%d' % (a if a else '(none)', b) for a, b in c.most_common(5))
    key.append((t, s, n, tot, alts))
with open(D + 'KEY.tsv', 'w') as f:
    f.write('token\tvalue\tsupport\toccurrences\tvalues seen (training alignments)\n')
    for t, s, n, tot, alts in key:
        f.write('%s\t%s\t%d\t%d\t%s\n' % (t, s if s else '-', n, tot, alts))
    f.write('#RULE\tD2\t%s\n' % ('nearest preceding vowel of the decoded word' if rule_d2 else 'use value above'))
    f.write('#RULE\t+"\t%s\n' % ('repeat the letter(s) of the preceding sign' if rule_dbl else 'use value above'))
with open(D + 'work/train_alignment.tsv', 'w') as f:
    f.write('cipher_lines\tclear_word\ttokens\tsegments\tper_letter_cost\tkept\n')
    for ci, j, toks, w, segs, pl, ok in rows:
        f.write('%s\t%s\t%s\t%s\t%.2f\t%s\n' % ('|'.join(C[i]['line'] for i in ci), w, ' '.join(toks),
                                               ' '.join(s if s else '-' for s in (segs or [])), pl, ok))
    for ci, j in pairs:
        if ci and j is None:
            f.write('%s\t(unpaired cipher word)\t%s\t\t\t\n' % ('|'.join(C[i]['line'] for i in ci), ' '.join(sum((cw[i] for i in ci), []))))
        if not ci:
            f.write('\t%s\t(unpaired clear word)\t\t\t\n' % W[j])
print('\n'.join(log))
print('key tokens:', len(key))
with open(D + 'work/solve_out.txt', 'w') as f:
    f.write('\n'.join(log) + '\nkey tokens: %d\n' % len(key))
