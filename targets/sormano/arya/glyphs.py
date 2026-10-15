"""Segment the cipher glyphs of one image band into connected components and cluster them by shape.

Pure Python, no third-party libraries: the image is converted to an uncompressed 24-bit BMP with
  sips -s format bmp IN.jpg --out OUT.bmp
and parsed here. Written for the four-line crib on f. 124r (BnF fr. 3096 no. 67), whose plaintext is
known from the contemporary decipherment in the margin, so that the alignment can be checked.

usage: python3 glyphs.py BMP [--thresh N] [--minpx N] [--minh N]
"""
import struct, sys, math
from collections import deque

def read_bmp(path):
    d = open(path, 'rb').read()
    off = struct.unpack('<I', d[10:14])[0]
    w = struct.unpack('<i', d[18:22])[0]
    h = struct.unpack('<i', d[22:26])[0]
    bpp = struct.unpack('<H', d[28:30])[0]
    assert bpp == 24, bpp
    flip = h < 0
    h = abs(h)
    row = (w * 3 + 3) // 4 * 4
    g = [[0] * w for _ in range(h)]
    for y in range(h):
        base = off + y * row
        ty = y if flip else h - 1 - y          # BMP rows are bottom-up unless height is negative
        r = g[ty]
        for x in range(w):
            i = base + x * 3
            r[x] = (d[i] * 114 + d[i + 1] * 587 + d[i + 2] * 299) // 1000
    return w, h, g

def otsu(g, w, h):
    hist = [0] * 256
    for row in g:
        for v in row:
            hist[v] += 1
    tot = w * h
    sm = sum(i * hist[i] for i in range(256))
    best, bt, wB, sB = -1.0, 128, 0, 0
    for t in range(256):
        wB += hist[t]
        if wB == 0 or wB == tot:
            continue
        sB += t * hist[t]
        mB = sB / wB
        mF = (sm - sB) / (tot - wB)
        var = wB * (tot - wB) * (mB - mF) ** 2
        if var > best:
            best, bt = var, t
    return bt

def components(g, w, h, thresh, minpx, minh):
    ink = [[g[y][x] < thresh for x in range(w)] for y in range(h)]
    seen = [[False] * w for _ in range(h)]
    out = []
    for y in range(h):
        for x in range(w):
            if not ink[y][x] or seen[y][x]:
                continue
            q = deque([(x, y)]); seen[y][x] = True; px = []
            while q:
                cx, cy = q.popleft(); px.append((cx, cy))
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < w and 0 <= ny < h and ink[ny][nx] and not seen[ny][nx]:
                            seen[ny][nx] = True; q.append((nx, ny))
            xs = [p[0] for p in px]; ys = [p[1] for p in px]
            x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
            if len(px) >= minpx and (y1 - y0 + 1) >= minh:
                out.append(dict(x0=x0, x1=x1, y0=y0, y1=y1, n=len(px), px=px))
    return out

def lines_of(cs, gap):
    """Group components into text lines by their vertical centres."""
    cs = sorted(cs, key=lambda c: (c['y0'] + c['y1']) / 2)
    ls, cur, last = [], [], None
    for c in cs:
        m = (c['y0'] + c['y1']) / 2
        if last is not None and m - last > gap:
            ls.append(cur); cur = []
        cur.append(c); last = m
    if cur:
        ls.append(cur)
    return [sorted(l, key=lambda c: c['x0']) for l in ls]

def feat(c, n=12):
    """Normalised n x n ink-density bitmap of one component."""
    w = c['x1'] - c['x0'] + 1; h = c['y1'] - c['y0'] + 1
    f = [0.0] * (n * n)
    for (x, y) in c['px']:
        gx = min(n - 1, (x - c['x0']) * n // w)
        gy = min(n - 1, (y - c['y0']) * n // h)
        f[gy * n + gx] += 1
    s = sum(f) or 1.0
    return [v / s for v in f] + [h / max(w, 1)]     # plus the aspect ratio

def dist(a, b):
    return math.sqrt(sum((p - q) ** 2 for p, q in zip(a, b)))

def cluster(fs, thr):
    """Single-pass leader clustering, then assign each item to its nearest leader."""
    leaders = []
    for i, f in enumerate(fs):
        best, bi = None, -1
        for j, (lf, _) in enumerate(leaders):
            dd = dist(f, lf)
            if best is None or dd < best:
                best, bi = dd, j
        if best is not None and best < thr:
            leaders[bi][1].append(i)
        else:
            leaders.append([f, [i]])
    lab = [0] * len(fs)
    for j, (_, mem) in enumerate(leaders):
        for i in mem:
            lab[i] = j
    return lab, leaders

if __name__ == '__main__':
    bmp = sys.argv[1]
    th = None; minpx = 40; minh = 8
    for i, a in enumerate(sys.argv):
        if a == '--thresh': th = int(sys.argv[i + 1])
        if a == '--minpx': minpx = int(sys.argv[i + 1])
        if a == '--minh': minh = int(sys.argv[i + 1])
    w, h, g = read_bmp(bmp)
    t = th if th is not None else otsu(g, w, h)
    cs = components(g, w, h, t, minpx, minh)
    print(f'# {bmp} {w}x{h} threshold={t} components={len(cs)}', file=sys.stderr)
    ls = lines_of(cs, gap=40)
    print(f'# lines={len(ls)} sizes={[len(l) for l in ls]}', file=sys.stderr)
    fs, idx = [], []
    for li, l in enumerate(ls):
        for c in l:
            fs.append(feat(c)); idx.append((li, c))
    lab, leaders = cluster(fs, thr=float(sys.argv[sys.argv.index('--thr') + 1]) if '--thr' in sys.argv else 0.55)
    print(f'# clusters={len(leaders)}', file=sys.stderr)
    for li in range(len(ls)):
        row = [(c['x0'], lab[k]) for k, (l2, c) in enumerate(idx) if l2 == li]
        row.sort()
        print(f'L{li+1}\t' + ' '.join(f'{lb}' for _, lb in row))
    for k, (l2, c) in enumerate(idx):
        print(f'BOX\t{l2+1}\t{c["x0"]}\t{c["y0"]}\t{c["x1"]}\t{c["y1"]}\t{c["n"]}\t{lab[k]}', file=sys.stderr)
