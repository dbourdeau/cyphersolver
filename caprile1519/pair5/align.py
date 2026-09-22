"""Hard-EM monotone aligner: R1131 P2 last lines (t1131.txt) vs tail of 5b (5b.txt, p.6).
Letter column -> 1 letter; code column [x] -> one whole word (1..14 letters, must start and end on a word boundary);
column may be a null (penalty); plaintext letters may be skipped (penalty, models 1882 gaps / misreadings).
Semi-global: every cipher column used, plaintext free at both ends.  Control: same run on shuffled-word plaintext."""
import re, json, math, random, sys, collections
random.seed(1)
HERE = __file__.rsplit('\\', 1)[0].rsplit('/', 1)[0]

def load_cipher():
    cols = []
    for line in open(HERE + '/t1131.txt', encoding='utf8'):
        if line.startswith('R1131'):
            for c in line.split(':', 1)[1].split():
                cols.append(c.replace('?', ''))
    return cols

def load_plain():
    txt = open(HERE + '/5b.txt', encoding='utf8').read()
    p6 = txt.split('## p.6')[1].split('\n', 1)[1]
    p6 = re.sub(r'\[[^\]]*\]', ' ', p6).lower().replace("'", ' ')
    p6 = re.sub(r'[^a-z ]', ' ', p6)
    words = p6.split()
    return words

def is_code(c): return '[' in c

def run(words, cols, seed, iters=12, verbose=False):
    plain = ''.join(words)
    bound = set([0]); k = 0
    for w in words: k += len(w); bound.add(k)
    N, M = len(plain), len(cols)
    em = collections.defaultdict(lambda: collections.Counter())
    for s, l in seed.items(): em[s][l] += 5
    NULL, SKIP = math.log(0.02), math.log(0.05)
    def lp(s, l):
        c = em[s]; tot = sum(c.values())
        return math.log((c[l] + 0.3) / (tot + 0.3 * 26))
    CODEP = math.log(0.5)
    for it in range(iters):
        NEG = -1e18
        D = [[NEG] * (N + 1) for _ in range(M + 1)]; B = [[None] * (N + 1) for _ in range(M + 1)]
        for j in range(N + 1): D[0][j] = 0.0   # free start
        for i in range(1, M + 1):
            s = cols[i - 1]; Di, Dp = D[i], D[i - 1]
            for j in range(N + 1):
                best, arg = Dp[j] + NULL, ('null', j)
                if j > 0 and D[i][j - 1] + SKIP > best: best, arg = D[i][j - 1] + SKIP, ('skip', j - 1)
                if not is_code(s):
                    if j > 0:
                        v = Dp[j - 1] + lp(s, plain[j - 1])
                        if v > best: best, arg = v, ('let', j - 1)
                elif j in bound:
                    for L in range(1, 15):
                        a = j - L
                        if a < 0: break
                        if a in bound:
                            v = Dp[a] + CODEP - 0.15 * L
                            if v > best: best, arg = v, ('code', a)
                Di[j] = best; B[i][j] = arg
        jend = max(range(N + 1), key=lambda j: D[M][j])
        # backtrace
        path = []; i, j = M, jend
        while i > 0:
            kind, pj = B[i][j]
            if kind == 'skip': j = pj; continue
            path.append((i - 1, kind, plain[pj:j] if kind in ('let', 'code') else ''))
            i, j = (i - 1, pj) if kind != 'null' else (i - 1, j)
        path.reverse()
        em = collections.defaultdict(lambda: collections.Counter())
        for s, l in seed.items(): em[s][l] += 2
        for ci, kind, seg in path:
            if kind == 'let': em[cols[ci]][seg] += 1
        score = D[M][jend]
    return score, path, em

if __name__ == '__main__':
    cols = load_cipher(); words = load_plain()
    seed = json.load(open(HERE + '/../fixed1519.json'))
    seed.update({'9/7': 'e'})  # hypothesis tested, see REPORT
    if '--noseed' in sys.argv: seed = {}
    sc, path, em = run(words, cols, seed)
    out = []
    for ci, kind, seg in path: out.append('%-7s %-5s %s' % (cols[ci], kind, seg))
    open(HERE + '/align_out.txt', 'w', encoding='utf8').write('\n'.join(out))
    lets = [(cols[ci], seg) for ci, k, seg in path if k == 'let']
    agree = sum(1 for s, l in lets if em[s].most_common(1)[0][0] == l)
    print('score %.1f letters %d agree-with-majority %d (%.0f%%)' % (sc, len(lets), agree, 100 * agree / max(1, len(lets))))
    ctrl = []
    for r in range(5):
        w2 = words[:]; random.shuffle(w2)
        w2 = [''.join(random.sample(w, len(w))) for w in w2]
        ctrl.append(run(w2, cols, seed)[0])
    print('controls (shuffled letters):', ['%.1f' % c for c in ctrl])
    key = {s: dict(c) for s, c in em.items() if c}
    json.dump(key, open(HERE + '/key_pair5_raw.json', 'w'), indent=1, sort_keys=True)
