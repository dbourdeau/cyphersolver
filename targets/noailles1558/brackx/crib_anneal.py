"""Joint search for sign values and the alignment of the cipher blocks with the marginal gloss.

Model: each sign label stands for one letter or is a null. The gloss is the plaintext with hidden stretches
(written '*', 0-6 unknown letters each) where the binding swallows the start of a line. For a given key, an edit
alignment of decoded signs against the gloss costs:
  0  sign whose letter matches the gloss letter, or that fills a hidden letter
  1  null sign (key says null) - charged lightly so nulls must earn their place
  3  sign whose letter differs from the gloss letter
  2  gloss letter with no sign (a letter the cipher left out, or one sign for several letters)
The key is annealed to minimise the summed cost over both blocks; fixed values are held. Reports the best keys
and their alignments so the agreement can be checked by eye."""
import sys, random, math, json

ALPHA = 'abcdefghilmnopqrstuxyz'  # u = v, i = j, no k/w


def load(fn):
    out = {}
    for l in open(fn):
        if l.startswith('#') or ':' not in l: continue
        k, v = l.split(':', 1)
        out[k.strip()] = [t for t in v.split() if not t.startswith('[')]
    return out


def norm(s):
    return s.replace('v', 'u').replace('j', 'i').replace(' ', '')


def align(toks, tmpl, key, back=False):
    """tmpl: list of items, each a letter or '*' (one optional hidden letter). DP over toks x tmpl."""
    n, m = len(toks), len(tmpl)
    INF = 10 ** 9
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            d = D[i][j]
            if d >= INF: continue
            if j < m:  # gloss item without a sign
                c = 0 if tmpl[j] == '*' else 2
                if d + c < D[i][j + 1]: D[i][j + 1] = d + c; B[i][j + 1] = (i, j, 'skip')
            if i < n:
                v = key.get(toks[i])
                if v == '0':  # null sign
                    if d + 1 < D[i + 1][j]: D[i + 1][j] = d + 1; B[i + 1][j] = (i, j, 'null')
                else:  # unaligned sign (gloss shorter than cipher), costly
                    if d + 4 < D[i + 1][j]: D[i + 1][j] = d + 4; B[i + 1][j] = (i, j, 'extra')
                if j < m:
                    t = tmpl[j]
                    c = 0 if (t == '*' or v == t) else 3
                    if v == '0': c = 5
                    if d + c < D[i + 1][j + 1]: D[i + 1][j + 1] = d + c; B[i + 1][j + 1] = (i, j, 'pair')
    if not back: return D[n][m]
    path, i, j = [], n, m
    while (i, j) != (0, 0):
        pi, pj, op = B[i][j]
        path.append((op, toks[pi] if op in ('null', 'extra', 'pair') else None, tmpl[pj] if op in ('skip', 'pair') else None))
        i, j = pi, pj
    return D[n][m], path[::-1]


def template(g):
    out = []
    for ch in norm(g):
        if ch == '#': out += ['*'] * 6
        else: out.append(ch)
    return out


def main():
    tr = load(sys.argv[1])
    cfg = json.load(open(sys.argv[2]))
    blocks = [(sum((tr[l] for l in b['lines']), []), template(b['gloss'])) for b in cfg['blocks']]
    fixed = cfg.get('fixed', {})
    labels = sorted({t for toks, _ in blocks for t in toks})
    rng = random.Random(int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    best_all = []
    for run in range(int(cfg.get('runs', 8))):
        key = {t: fixed.get(t, rng.choice(ALPHA)) for t in labels}
        cost = sum(align(t, g, key) for t, g in blocks)
        T = 3.0
        free = [t for t in labels if t not in fixed]
        for it in range(int(cfg.get('iters', 6000))):
            t = rng.choice(free); old = key[t]
            key[t] = rng.choice(ALPHA + '0')
            c = sum(align(tt, g, key) for tt, g in blocks)
            if c <= cost or rng.random() < math.exp((cost - c) / T): cost = c
            else: key[t] = old
            T = max(0.05, T * 0.9993)
        best_all.append((cost, dict(key)))
        print('run', run, 'cost', cost, flush=True)
    best_all.sort(key=lambda x: x[0])
    cost, key = best_all[0]
    print('\nbest cost', cost)
    for (toks, g), b in zip(blocks, cfg['blocks']):
        c, path = align(toks, g, key, back=True)
        line_s, line_p = [], []
        for op, t, p in path:
            if op == 'pair': line_s.append(f'{t}={key[t]}'); line_p.append(p if key[t] == p or p == '*' else p.upper())
            elif op == 'null': line_s.append(f'{t}=0'); line_p.append('.')
            elif op == 'extra': line_s.append(f'{t}!'); line_p.append('+')
            elif op == 'skip' and p != '*': line_s.append('-'); line_p.append(p.upper())
        print(b['name'], c)
        print('  ', ' '.join(line_s))
        print('  ', ''.join(line_p))
    agree = {}
    for c, k in best_all:
        for t in labels: agree.setdefault(t, []).append(k[t])
    print('\nper-label values across runs (best first):')
    for t in labels:
        vals = agree[t]
        print(f'  {t:5} ' + ' '.join(vals), '| fixed' if t in fixed else '')


if __name__ == '__main__':
    main()
