"""Glyph segmentation and shape clustering for the fr. 3096 cipher, pure Python (no third-party libraries).

Images are converted to uncompressed 24-bit BMP with `sips -s format bmp` and parsed by glyphs.read_bmp.

The shape metric is the part that matters. Binary overlap (Jaccard) on a hand this thin fails, because a
one-pixel offset destroys the overlap: measured on two known pairs of identical letters it ranked the true
partner 8th and 4th of 13. Blurring the mask before comparing fixes it. Each component is rendered as a
binary mask on an N x N grid (bounding box stretched to fill, which normalises size), box-blurred twice,
L2-normalised, and compared by cosine distance minimised over shifts of +/- 2 cells. On the same two known
pairs that metric ranks the true partner 1st of 13, at distance 0.10-0.12 against a median pair distance
of 0.33.

usage: python3 glyphs5.py BMP [--xmin N] [--k N] [--sweep] [--dump FILE]
"""
import sys, math, statistics, json
sys.path.insert(0, '.')
from glyphs import read_bmp, components
from glyphs2 import merge_overlaps
from glyphs3 import bands_of

N = 24
INK = 130

def bmask(c):
    cw = c['x1'] - c['x0'] + 1; ch = c['y1'] - c['y0'] + 1
    a = [[0.0] * N for _ in range(N)]
    for (x, y) in c['px']:
        gx = min(N - 1, (x - c['x0']) * N // cw)
        gy = min(N - 1, (y - c['y0']) * N // ch)
        a[gy][gx] = 1.0
    return a

def blur(a, times=1):
    for _ in range(times):
        b = [[0.0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                s = 0.0; n = 0
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        yy, xx = y + dy, x + dx
                        if 0 <= yy < N and 0 <= xx < N:
                            s += a[yy][xx]; n += 1
                b[y][x] = s / n
        a = b
    return a

def norm(v):
    nn = math.sqrt(sum(t * t for t in v)) or 1.0
    return [t / nn for t in v]

def shifts(a, sh=2):
    out = []
    for dy in range(-sh, sh + 1):
        for dx in range(-sh, sh + 1):
            v = []
            for y in range(N):
                for x in range(N):
                    yy, xx = y - dy, x - dx
                    v.append(a[yy][xx] if 0 <= yy < N and 0 <= xx < N else 0.0)
            out.append(norm(v))
    return out

def prep(cs):
    base, shft = [], []
    for c in cs:
        a = blur(bmask(c))
        base.append(norm([a[y][x] for y in range(N) for x in range(N)]))
        shft.append(shifts(a))
    return base, shft

def dist(i, j, base, shft):
    vb = base[j]
    return min(1.0 - sum(p * q for p, q in zip(va, vb)) for va in shft[i])

def extract(bmp, xmin=0):
    w, h, g = read_bmp(bmp)
    cs = components(g, w, h, INK, 45, 10)
    bs = bands_of(g, w, h)
    rows = {i: [] for i in range(len(bs))}
    for c in cs:
        m = (c['y0'] + c['y1']) / 2
        bi = min(range(len(bs)), key=lambda i: 0 if bs[i][0] <= m <= bs[i][1]
                 else min(abs(m - bs[i][0]), abs(m - bs[i][1])))
        if bi == 0 and c['x0'] < xmin:
            continue
        rows[bi].append(c)
    seq = []
    for i in sorted(rows):
        rows[i].sort(key=lambda c: c['x0'])
        seq.append(merge_overlaps(rows[i]))
    return bs, seq

def agglom(n, dmat, k):
    cl = [[i] for i in range(n)]
    while len(cl) > k:
        best = None; bi = bj = -1
        for i in range(len(cl)):
            for j in range(i + 1, len(cl)):
                s = sum(dmat[a][b] for a in cl[i] for b in cl[j]) / (len(cl[i]) * len(cl[j]))
                if best is None or s < best:
                    best, bi, bj = s, i, j
        cl[bi] = cl[bi] + cl[bj]; cl.pop(bj)
    lab = [0] * n
    for ci, mem in enumerate(cl):
        for i in mem:
            lab[i] = ci
    return lab

if __name__ == '__main__':
    bmp = sys.argv[1]
    xmin = int(sys.argv[sys.argv.index('--xmin') + 1]) if '--xmin' in sys.argv else 0
    bs, seq = extract(bmp, xmin)
    flat = [c for s in seq for c in s]
    print(f'# bands={bs}', file=sys.stderr)
    print(f'# per line {[len(s) for s in seq]} total {len(flat)}', file=sys.stderr)
    base, shft = prep(flat)
    n = len(flat)
    D = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = min(dist(i, j, base, shft), dist(j, i, base, shft))
            D[i][j] = D[j][i] = d
    off = [D[i][j] for i in range(n) for j in range(i + 1, n)]
    print(f'# pair distances: min={min(off):.3f} median={statistics.median(off):.3f}', file=sys.stderr)
    if '--dump' in sys.argv:
        json.dump(dict(per_line=[len(s) for s in seq], D=D), open(sys.argv[sys.argv.index('--dump') + 1], 'w'))
    if '--sweep' in sys.argv:
        for k in (24, 28, 32, 36, 40, 44):
            lab = agglom(n, D, k)
            print(f'# k={k} ok', file=sys.stderr)
        sys.exit()
    k = int(sys.argv[sys.argv.index('--k') + 1]) if '--k' in sys.argv else 34
    lab = agglom(n, D, k)
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    t = 0
    for li, s in enumerate(seq):
        print(f'L{li+1}\t' + ''.join(A[lab[t + i]] for i in range(len(s))))
        t += len(s)
