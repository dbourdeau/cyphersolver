"""Sign reader for sign-cipher letters: deskew, find lines, segment glyphs, cluster by shape.
usage: python signreader.py lines  <image> <outdir>"""
import sys, os, json
import cv2, numpy as np

def load_binary(path, bg_sigma=40):
    g = cv2.imread(path, 0)
    # page mask: bright region (letters are on light paper; archive images have black borders)
    blur = cv2.GaussianBlur(g, (0, 0), 25)
    page = (blur > 90).astype(np.uint8)
    page = cv2.erode(page, np.ones((61, 61), np.uint8))
    bg = cv2.GaussianBlur(g, (0, 0), bg_sigma)
    norm = cv2.divide(g, bg, scale=255)
    ink = (norm < 0).astype(np.uint8)  # placeholder
    _, ink = cv2.threshold(norm, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    ink[page == 0] = 0
    return g, ink

def best_angle(ink, lo=-4, hi=4, step=0.25):
    h, w = ink.shape
    small = cv2.resize(ink, (w // 3, h // 3), interpolation=cv2.INTER_AREA)
    best = (None, -1)
    for a in np.arange(lo, hi + 1e-9, step):
        M = cv2.getRotationMatrix2D((small.shape[1] / 2, small.shape[0] / 2), a, 1)
        r = cv2.warpAffine(small, M, (small.shape[1], small.shape[0]))
        v = r.sum(1).astype(float).var()
        if v > best[1]: best = (a, v)
    return best[0]

def rotate(img, a):
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((w / 2, h / 2), a, 1)
    return cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderValue=0 if img.ndim == 2 and img.max() == 255 and img.dtype == np.uint8 and False else 0)

def find_lines(ink, rel=0.25):
    prof = ink.sum(1).astype(float) / 255
    k = np.ones(25) / 25
    prof = np.convolve(prof, k, 'same')
    n = len(prof)
    # line pitch from the autocorrelation of the profile
    p0 = prof - prof.mean()
    ac = np.correlate(p0, p0, 'full')[n - 1:]
    lo, hi = 35, 200
    pitch = lo + int(np.argmax(ac[lo:hi]))
    win = max(15, int(pitch * 0.45))
    thr = prof.max() * rel
    pk = [y for y in range(n) if prof[y] == prof[max(0, y - win):min(n, y + win + 1)].max() and prof[y] > thr]
    out = []
    for y in pk:
        if out and y - out[-1] < 0.6 * pitch: continue
        out.append(y)
    return out, prof

if __name__ == '__main__':
    cmd, path, outdir = sys.argv[1:4]
    os.makedirs(outdir, exist_ok=True)
    g, ink = load_binary(path)
    a = best_angle(ink)
    print('angle', a)
    ink = rotate(ink, a); g = rotate(g, a)
    cv2.imwrite(os.path.join(outdir, 'ink.png'), ink)
    cv2.imwrite(os.path.join(outdir, 'gray.png'), g)
    ys, prof = find_lines(ink)
    print('pitch-lines', len(ys), 'lines', ys, [ys[i + 1] - ys[i] for i in range(len(ys) - 1)])
    json.dump(dict(angle=a, lines=ys), open(os.path.join(outdir, 'lines.json'), 'w'))

def track_line(ink, y0, half=70, win=240, step=60):
    """Follow a text line across the page: returns y center for every column."""
    h, w = ink.shape
    xs = list(range(0, w - win, step)) + [w - win]
    ys = []
    y = y0
    # sweep from the middle outwards so a bad edge window does not drag the line
    mid = len(xs) // 2
    order = list(range(mid, len(xs))) + list(range(mid - 1, -1, -1))
    res = {}
    cur = y0
    for k, i in enumerate(order):
        if k == len(xs) - mid: cur = res[mid]
        x = xs[i]
        sub = ink[max(0, int(cur) - 45):int(cur) + 46, x:x + win].sum(1).astype(float)
        sub = np.convolve(sub, np.ones(15) / 15, 'same')
        if sub.max() > 0:
            cur = max(0, int(cur) - 45) + int(np.argmax(sub))
        res[i] = cur
    cx = [xs[i] + win / 2 for i in range(len(xs))]
    cy = [res[i] for i in range(len(xs))]
    return np.interp(np.arange(w), cx, cy)

def straighten(arr, center, half=70):
    h, w = arr.shape[:2]
    out = np.zeros((2 * half, w), arr.dtype)
    for x in range(w):
        c = int(round(center[x]))
        y0, y1 = c - half, c + half
        a, b = max(0, y0), min(h, y1)
        out[a - y0:b - y0, x] = arr[a:b, x]
    return out

def strips(outdir, half=70):
    ink = cv2.imread(os.path.join(outdir, 'ink.png'), 0)
    gray = cv2.imread(os.path.join(outdir, 'gray.png'), 0)
    lj = json.load(open(os.path.join(outdir, 'lines.json')))
    res = []
    for i, y in enumerate(lj['lines']):
        c = track_line(ink, y)
        si = straighten(ink, c, half); sg = straighten(gray, c, half)
        cv2.imwrite(os.path.join(outdir, f'strip{i+1:02d}_ink.png'), si)
        cv2.imwrite(os.path.join(outdir, f'strip{i+1:02d}_gray.png'), sg)
        res.append(dict(line=i + 1, y0=y, spread=[float(c.min()), float(c.max())]))
    json.dump(res, open(os.path.join(outdir, 'strips.json'), 'w'))
    print(res)

if __name__ == '__main__' and sys.argv[1] == 'strips':
    strips(sys.argv[3])

def segment_strip(ink_strip, min_area=35, overlap=0.4):
    n, lab, st, cen = cv2.connectedComponentsWithStats(ink_strip, 8)
    comps = []
    for i in range(1, n):
        x, y, w, h, a = st[i]
        if a < min_area: continue
        comps.append([x, y, w, h, a, [i]])
    comps.sort()
    merged = True
    while merged:
        merged = False
        comps.sort()
        for i in range(len(comps)):
            for j in range(i + 1, len(comps)):
                a, b = comps[i], comps[j]
                if b[0] > a[0] + a[2]: break
                ov = min(a[0] + a[2], b[0] + b[2]) - b[0]
                if ov >= overlap * min(a[2], b[2]):
                    x0 = min(a[0], b[0]); y0 = min(a[1], b[1])
                    x1 = max(a[0] + a[2], b[0] + b[2]); y1 = max(a[1] + a[3], b[1] + b[3])
                    comps[i] = [x0, y0, x1 - x0, y1 - y0, a[4] + b[4], a[5] + b[5]]
                    del comps[j]; merged = True; break
            if merged: break
    comps.sort()
    H = ink_strip.shape[0]
    keep = []
    for c in comps:
        cy = c[1] + c[3] / 2
        if abs(cy - H / 2) > 40 and c[3] < 0.75 * H: continue   # fragment of a neighbouring line
        if c[4] < 70 and c[3] < 22 and c[2] < 22: continue      # specks
        keep.append(c)
    return keep, lab

def seg_all(outdir, lines):
    allg = []
    for L in lines:
        ink = cv2.imread(os.path.join(outdir, f'strip{L:02d}_ink.png'), 0)
        gray = cv2.imread(os.path.join(outdir, f'strip{L:02d}_gray.png'), 0)
        comps, lab = segment_strip(ink)
        vis = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        for k, (x, y, w, h, a, ids) in enumerate(comps):
            cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 0, 255), 1)
            allg.append(dict(line=L, k=k, x=int(x), y=int(y), w=int(w), h=int(h), area=int(a)))
        cv2.imwrite(os.path.join(outdir, f'strip{L:02d}_boxes.png'), vis)
        print(L, len(comps))
    json.dump(allg, open(os.path.join(outdir, 'glyphs.json'), 'w'))

if __name__ == '__main__' and sys.argv[1] == 'seg':
    seg_all(sys.argv[3], [int(v) for v in sys.argv[4].split(',')])

def glyph_mask(lab, ids, x, y, w, h):
    m = np.isin(lab[y:y + h, x:x + w], ids).astype(np.uint8) * 255
    return m

def feat(m, S=20):
    h, w = m.shape
    side = max(h, w)
    pad = np.zeros((side, side), np.uint8)
    pad[(side - h) // 2:(side - h) // 2 + h, (side - w) // 2:(side - w) // 2 + w] = m
    r = cv2.resize(pad, (S, S), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
    r = cv2.GaussianBlur(r, (0, 0), 1.6)
    f = r.flatten()
    f = f / (np.linalg.norm(f) + 1e-6)
    aspect = np.array([np.log((w + 1) / (h + 1))], np.float32) * 1.5
    size = np.array([np.log(h + 1) * 0.5], np.float32)
    return np.concatenate([f * 3, aspect, size])

def cluster(outdir, lines, thr):
    from sklearn.cluster import AgglomerativeClustering
    G, F, M = [], [], []
    for L in lines:
        ink = cv2.imread(os.path.join(outdir, f'strip{L:02d}_ink.png'), 0)
        comps, lab = segment_strip(ink)
        for k, (x, y, w, h, a, ids) in enumerate(comps):
            m = glyph_mask(lab, ids, x, y, w, h)
            G.append(dict(line=L, k=k, x=int(x), y=int(y), w=int(w), h=int(h)))
            F.append(feat(m)); M.append(m)
    F = np.array(F)
    cl = AgglomerativeClustering(n_clusters=(int(thr) if thr>=10 else None), distance_threshold=(None if thr>=10 else thr), linkage='ward' if thr>=10 else 'average').fit(F)
    labels = cl.labels_
    order = sorted(set(labels), key=lambda c: -np.sum(labels == c))
    names = {c: f'g{i:02d}' for i, c in enumerate(order)}
    for g, l in zip(G, labels): g['sym'] = names[l]
    json.dump(G, open(os.path.join(outdir, 'tokens.json'), 'w'))
    # montage
    tiles = []
    for c in order:
        idx = [i for i, l in enumerate(labels) if l == c][:14]
        row = np.full((60, 14 * 64 + 70), 255, np.uint8)
        cv2.putText(row, f'{names[c]} n={int(np.sum(labels==c))}', (2, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.4, 0, 1)
        for j, i in enumerate(idx):
            m = 255 - M[i]
            h, w = m.shape; s = min(56 / h, 56 / w, 1.0)
            m = cv2.resize(m, (max(1, int(w * s)), max(1, int(h * s))), interpolation=cv2.INTER_AREA)
            row[2:2 + m.shape[0], 70 + j * 64:70 + j * 64 + m.shape[1]] = m
        tiles.append(row)
    for p in range(0, len(tiles), 12):
        cv2.imwrite(os.path.join(outdir, f'clusters_{p // 12}.png'), np.vstack(tiles[p:p + 12]))
    print('glyphs', len(G), 'clusters', len(order), 'sizes', [int(np.sum(labels == c)) for c in order][:30])
    # token file: per line
    out = []
    for L in lines:
        out.append(' '.join(g['sym'] for g in G if g['line'] == L))
    open(os.path.join(outdir, 'tokens.txt'), 'w').write('\n'.join(out) + '\n')

if __name__ == '__main__' and sys.argv[1] == 'cluster':
    cluster(sys.argv[3], [int(v) for v in sys.argv[4].split(',')], float(sys.argv[5]))

import pickle

def extract_page(png, outdir, tag, half=70):
    """lines.json + ink/gray from `lines` -> list of glyph records (with masks) pickled to outdir/glyphs.pkl"""
    ink = cv2.imread(os.path.join(outdir, 'ink.png'), 0)
    lj = json.load(open(os.path.join(outdir, 'lines.json')))
    ys = lj['lines']
    pitch = float(np.median(np.diff(ys))) if len(ys) > 1 else 110.0
    jump = int(max(12, 0.4 * pitch))
    recs = []
    for li, y in enumerate(ys):
        c = track_line_j(ink, y, jump)
        si = straighten(ink, c, half)
        comps, lab = segment_strip(si)
        for k, (x, yy, w, h, a, ids) in enumerate(comps):
            m = glyph_mask(lab, ids, x, yy, w, h)
            recs.append(dict(page=tag, line=li + 1, k=k, x=int(x), y=int(yy), w=int(w), h=int(h), mask=m, feat=feat(m)))
    pickle.dump(recs, open(os.path.join(outdir, 'glyphs.pkl'), 'wb'))
    print(tag, 'lines', len(ys), 'pitch', pitch, 'glyphs', len(recs))

def track_line_j(ink, y0, jump, win=240, step=60):
    h, w = ink.shape
    xs = list(range(0, w - win, step)) + [w - win]
    mid = len(xs) // 2
    order = list(range(mid, len(xs))) + list(range(mid - 1, -1, -1))
    res = {}; cur = y0
    for k, i in enumerate(order):
        if k == len(xs) - mid: cur = res[mid]
        x = xs[i]
        a0 = max(0, int(cur) - jump)
        sub = ink[a0:int(cur) + jump + 1, x:x + win].sum(1).astype(float)
        sub = np.convolve(sub, np.ones(9) / 9, 'same')
        if sub.max() > 0: cur = a0 + int(np.argmax(sub))
        res[i] = cur
    cx = [xs[i] + win / 2 for i in range(len(xs))]
    cy = [res[i] for i in range(len(xs))]
    return np.interp(np.arange(w), cx, cy)

if __name__ == '__main__' and sys.argv[1] == 'extract':
    extract_page(sys.argv[2], sys.argv[3], sys.argv[4])
