"""Whole-page segmentation for G 275 inf. pages (rebuild of the lost work/seg.py, 26 Nov 2026).

    python scripts/seg3.py 34r 34v ...      -> work/pages.pkl  (per page: lines with their sign crops)

Finds the main text block, splits it into text lines by horizontal projection, cuts each line into
connected shapes and groups shapes that stack vertically into one sign (the grouping rules of seg2.py).
Each line gets a 'cursive' score (share of ink in wide components), used to tell clear lines from cipher.
"""
import sys, pickle, numpy as np, cv2
from scipy import ndimage as ni
from scipy.signal import find_peaks


def binarize(g):
    g = cv2.GaussianBlur(g, (3, 3), 0)
    b = cv2.adaptiveThreshold(g, 1, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 41, 18)
    return b


def main_block(b):
    """Main text block: between the deepest column-profile valley in the left 12-45% (margin gloss gap)
    and the deepest valley in the right 85-99% (edge of the facing page)."""
    H, W = b.shape
    col = b[int(H * .08):int(H * .92)].sum(0).astype(float)
    col = np.convolve(col, np.ones(15) / 15, 'same')
    a, z = int(W * .12), int(W * .45)
    xl = a + int(np.argmin(col[a:z]))
    a2, z2 = int(W * .85), int(W * .99)
    xr = a2 + int(np.argmin(col[a2:z2]))
    row = b[:, xl:xr].sum(1).astype(float)
    row = np.convolve(row, np.ones(15) / 15, 'same')
    on = np.nonzero(row > 0.08 * row.max())[0]
    return xl, on[0], xr, on[-1]


def lines_of(b):
    row = b.sum(1).astype(float)
    row = np.convolve(row, np.ones(9) / 9, 'same')
    pk, _ = find_peaks(row, distance=30, prominence=0.15 * row.max())
    return pk


def group_line(cl, lab):
    cl.sort(key=lambda c: c['x0'])
    groups = []
    for c in cl:
        placed = False
        for g2 in groups[-3:][::-1]:
            gx0 = min(k['x0'] for k in g2); gx1 = max(k['x1'] for k in g2)
            ov = min(gx1, c['x1']) - max(gx0, c['x0'])
            wmin = min(gx1 - gx0, c['x1'] - c['x0'])
            small = c['a'] < 40
            if ov > 0.5 * wmin or (small and ov > 0):
                g2.append(c); placed = True; break
        if not placed: groups.append([c])
    G = []
    for g2 in groups:
        if G:
            pg = G[-1]
            px1 = max(k['x1'] for k in pg); px0 = min(k['x0'] for k in pg)
            py0 = min(k['y0'] for k in pg); py1 = max(k['y1'] for k in pg)
            gx0 = min(k['x0'] for k in g2); gx1 = max(k['x1'] for k in g2)
            gy0 = min(k['y0'] for k in g2); gy1 = max(k['y1'] for k in g2)
            if gx1 - gx0 <= 9 and gy1 - gy0 <= 30 and px1 - px0 <= 12 and py1 - py0 >= 20 and gx0 - px1 <= 9:
                pg.extend(g2); continue
        G.append(g2)
    return G


def run(p):
    g = cv2.imread(f'targets/ferdinand1552/scans/c{p}.jpg', 0)
    b = binarize(g)
    bx0, by0, bx1, by1 = main_block(b)
    bb = b[by0:by1, bx0:bx1]
    # remove tiny specks
    lab, n = ni.label(bb, structure=np.ones((3, 3)))
    objs = ni.find_objects(lab)
    cs = []
    for i, s in enumerate(objs):
        a = int((lab[s] == i + 1).sum())
        if a < 6: continue
        cs.append(dict(y0=s[0].start, y1=s[0].stop, x0=s[1].start, x1=s[1].stop, a=a, i=i + 1,
                       cy=(s[0].start + s[0].stop) / 2))
    pk = lines_of(bb)
    L = {i: [] for i in range(len(pk))}
    for c in cs:
        if c['y1'] - c['y0'] > 120: continue
        l = int(np.argmin(abs(pk - c['cy'])))
        if abs(pk[l] - c['cy']) > 40: continue
        L[l].append(c)
    out = []
    for l, cl in L.items():
        if not cl: continue
        ink = sum(c['a'] for c in cl)
        wide = sum(c['a'] for c in cl if c['x1'] - c['x0'] > 55)
        G = group_line(cl, lab)
        signs = []
        for g2 in G:
            a = sum(k['a'] for k in g2)
            if a < 25: continue
            gx0 = min(k['x0'] for k in g2); gx1 = max(k['x1'] for k in g2)
            gy0 = min(k['y0'] for k in g2); gy1 = max(k['y1'] for k in g2)
            m = np.isin(lab[gy0:gy1, gx0:gx1], [k['i'] for k in g2]).astype(np.uint8)
            signs.append(dict(x0=gx0 + bx0, x1=gx1 + bx0, y0=gy0 + by0, y1=gy1 + by0, m=m))
        out.append(dict(p=p, y=int(pk[l] + by0), cursive=wide / max(1, ink), signs=signs))
    return out


if __name__ == '__main__':
    pages = {}
    for p in sys.argv[1:]:
        pages[p] = run(p)
        print(p, len(pages[p]), 'lines', [f"{x['cursive']:.2f}/{len(x['signs'])}" for x in pages[p]])
    import os
    os.makedirs('targets/ferdinand1552/work', exist_ok=True)
    try:
        old = pickle.load(open('targets/ferdinand1552/work/pages.pkl', 'rb'))
    except Exception:
        old = {}
    old.update(pages)
    pickle.dump(old, open('targets/ferdinand1552/work/pages.pkl', 'wb'))
