"""Language-model decoding of the cipher: noisy glyph evidence + Italian n-grams, combined by Viterbi.

The shape classifier alone is about 40% accurate, which is unreadable. But the cipher is a letter-for-letter
substitution of Italian, and the letters themselves supply several thousand characters of clear text in
exactly the right orthography and register. So: score every glyph against labelled exemplars taken from the
f.124r crib, convert to a distribution over letters, and Viterbi-decode under a character 4-gram model
trained on ct/clear_texts.md. Errors the shape model makes should be repaired by the language model.
"""
import sys, math, re, collections
sys.path.insert(0,'.')
from glyphs import read_bmp, components
from glyphs2 import merge_overlaps
from glyphs3 import bands_of
from clean import pipeline

AL = 'abcdefghilmnopqrstuvxz'      # no j/k/w/y in this hand
N = 12

# ---------- language model ----------
def corpus():
    t = open('ct/clear_texts.md', encoding='utf-8').read()
    t = re.sub(r'`[^`]*`', ' ', t)
    t = re.sub(r'\[chiffre\]|\[\.\.\.\]|⟨[^⟩]*⟩', ' ', t)
    t = re.sub(r'^#.*$', ' ', t, flags=re.M)
    t = t.lower().replace('j', 'i').replace('y', 'i').replace('k', 'c').replace('w', 'v')
    t = re.sub(r'[^a-z]', '', t)
    return t

def build_lm(txt, n=4):
    cnt = [collections.Counter() for _ in range(n + 1)]
    for k in range(1, n + 1):
        for i in range(len(txt) - k + 1):
            cnt[k][txt[i:i + k]] += 1
    return cnt

def lp(cnt, ctx, ch, n=4):
    for k in range(min(n - 1, len(ctx)), -1, -1):
        c = ctx[len(ctx) - k:] if k else ''
        num = cnt[k + 1][c + ch]; den = cnt[k][c] if k else sum(cnt[1].values())
        if den and num:
            return math.log((num + 0.1) / (den + 0.1 * len(AL)))
    return math.log(1e-6)

# ---------- glyph features ----------
def mask(g, c):
    cw = c['x1'] - c['x0'] + 1; ch = c['y1'] - c['y0'] + 1
    a = [[0.0] * N for _ in range(N)]
    for (x, y) in c['px']:
        a[min(N - 1, (y - c['y0']) * N // ch)][min(N - 1, (x - c['x0']) * N // cw)] = 1.0
    b = [[0.0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            s = 0.0; k = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    yy, xx = y + dy, x + dx
                    if 0 <= yy < N and 0 <= xx < N: s += a[yy][xx]; k += 1
            b[y][x] = s / k
    v = [b[y][x] for y in range(N) for x in range(N)]
    nn = math.sqrt(sum(t * t for t in v)) or 1.0
    return [t / nn for t in v]

def shifts(v):
    out = []
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            q = [0.0] * (N * N)
            for i in range(N):
                for j in range(N):
                    si, sj = i - dy, j - dx
                    q[i * N + j] = v[si * N + sj] if 0 <= si < N and 0 <= sj < N else 0.0
            nn = math.sqrt(sum(t * t for t in q)) or 1.0
            out.append([t / nn for t in q])
    return out

def sim(a_shifts, b):
    return max(sum(p * q for p, q in zip(v, b)) for v in a_shifts)

if __name__ == '__main__':
    txt = corpus(); print(f'LM corpus {len(txt)} chars', file=sys.stderr)
    cnt = build_lm(txt)
    # labelled exemplars from the crib
    wc, hc, gc = read_bmp('/tmp/crib.bmp')
    _, cseq = pipeline('/tmp/crib.bmp', 2115, 3270, maxw=64)
    cflat = [c for s in cseq for c in s]
    P = sys.argv[1].lower().replace('j','i')
    ex = [(mask(gc, c), P[i]) for i, c in enumerate(cflat) if i < len(P) and P[i] in AL]
    print(f'{len(ex)} labelled exemplars', file=sys.stderr)
    # target glyphs
    wt, ht, gt = read_bmp('/tmp/conc.bmp')
    _, tseq = pipeline('/tmp/conc.bmp', 0, 10**9, maxw=64)
    print('target per line', [len(s) for s in tseq], file=sys.stderr)
    for li, s in enumerate(tseq):
        obs = []
        for c in s:
            sh = shifts(mask(gt, c))
            best = {}
            for v, ch in ex:
                d = sim(sh, v)
                if ch not in best or d > best[ch]: best[ch] = d
            tot = sum(math.exp(12 * best.get(ch, 0.0)) for ch in AL)
            obs.append({ch: math.log(max(1e-12, math.exp(12 * best.get(ch, 0.0)) / tot)) for ch in AL})
        # Viterbi
        V = [{}]; B = [{}]
        for ch in AL:
            V[0][ch] = obs[0][ch] + lp(cnt, '', ch); B[0][ch] = ''
        for t in range(1, len(obs)):
            V.append({}); B.append({})
            for ch in AL:
                bs, bp = None, None
                for pv in AL:
                    hist = ''
                    k = t - 1; cur = pv
                    h = []
                    kk = k
                    while kk >= 0 and len(h) < 3:
                        h.append(B[kk][cur] if False else None); break
                    sc = V[t-1][pv] + lp(cnt, pv, ch)
                    if bs is None or sc > bs: bs, bp = sc, pv
                V[t][ch] = obs[t][ch] * 1.0 + bs; B[t][ch] = bp
        last = max(AL, key=lambda ch: V[-1][ch])
        outs = [last]
        for t in range(len(obs) - 1, 0, -1):
            last = B[t][last]; outs.append(last)
        print(f'L{li+1}\t' + ''.join(reversed(outs)))
