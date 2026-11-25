"""Contact sheets of exemplars per class from segments_<pass>.json.
Usage: python sheet.py <pass> [CLASS ...]  -> img/w/sheet_<pass>_<CLASS>.png (all signs of the class, native scale 0.6)
Each cell is the crop of the sign's x-range over the line band (neighbouring slashes may intrude), labelled line.index."""
import sys, json, os, cv2, numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
CY = [680, 945, 1170, 1404, 1664, 1881, 2124, 2348, 2616, 2828]
p = sys.argv[1]
d = json.load(open('segments_%s.json' % p))
src = cv2.imread('img/w/flat.png', 0)
cells = {}
for ln, segs in d.items():
    L = int(ln)
    for i, (x0, x1, lab, g) in enumerate(segs, 1):
        if lab == '.':
            continue
        cy = CY[L - 1] + 20
        crop = src[cy - 170:cy + 150, max(x0 - 10, 0):x1 + 10]
        cells.setdefault(lab, []).append((L, i, crop))
want = sys.argv[2:] or sorted(cells)
S = 0.55
for lab in want:
    cs = cells.get(lab, [])
    if not cs:
        continue
    ims = []
    for L, i, crop in cs:
        im = cv2.resize(crop, None, fx=S, fy=S, interpolation=cv2.INTER_AREA)
        im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
        cv2.rectangle(im, (0, 0), (im.shape[1] - 1, im.shape[0] - 1), (160, 160, 160), 1)
        cv2.putText(im, '%d.%d' % (L, i), (3, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
        ims.append(im)
    W = 1500
    rows, row, w = [], [], 0
    for im in ims:
        if w + im.shape[1] > W and row:
            rows.append(row); row, w = [], 0
        row.append(im); w += im.shape[1]
    rows.append(row)
    H = ims[0].shape[0]
    out = []
    for r in rows:
        rr = np.hstack(r)
        rr = np.hstack([rr, np.full((H, W - rr.shape[1], 3), 255, np.uint8)]) if rr.shape[1] < W else rr
        out.append(rr)
    cv2.imwrite('img/w/sheet_%s_%s.png' % (p, lab), np.vstack(out))
    print(lab, len(cs))
