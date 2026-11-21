"""Bands and candidate boxes for a page whose cipher lines are interleaved with clear text (an interlinear gloss).

marburg1635 (HStAM 4 d Nr. 1218 no. 49, DECODE R4500): one cipher sign per digit or letter-sign, written close
together, with a contemporary decipherment squeezed between cipher lines 1-4. prep_pages.py's gap finder and
segment_dense.py's peak finder both see the gloss as lines of their own. Here the cipher lines are given by hand as
centre points (x, y) on the page, refined to the local ink peak, and each line is cut out as its own band, straightened
by a column shear along the line through the points. Inside a band each ink blob near the line core is a candidate;
blobs that overlap horizontally (a bar over a stroke, the parts of a theta) join, wide blobs of touching signs are cut
at the column with least ink, and small marks above the core attach to the sign under them. Writes bands, boxes.json
and overlays in the format of prep_pages.py + segment.py, so to_ctts.py works unchanged.

  python segment_lines.py IMAGE PROJECT_DIR LINES_JSON [--prefix p1] [--above 70] [--below 62]

LINES_JSON: [{"line": 1, "x0": 1700, "x1": 2600, "pts": [[x, y], ...], "fixed": false}, ...] in page pixels;
"fixed": true keeps the points as given (where the gloss would pull the refinement off the line).
"""
import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from scipy import ndimage


def ink(gray, thr=28):
    a = np.asarray(gray, dtype=np.float32)
    bg = np.asarray(gray.filter(ImageFilter.GaussianBlur(25)), dtype=np.float32)
    return (bg - a) > thr


def refine(mask, x, y, half=60, win=25):
    """Move a hand-given centre point to the ink peak of the row profile nearby."""
    sub = mask[y - win - 20:y + win + 20, max(x - half, 0):x + half].sum(axis=1).astype(float)
    sub = ndimage.uniform_filter1d(sub, 15)
    k = int(np.argmax(sub[20:20 + 2 * win + 1]))
    return y - win + k


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('image'); ap.add_argument('project'); ap.add_argument('lines')
    ap.add_argument('--prefix', default='p1')
    ap.add_argument('--above', type=int, default=70)
    ap.add_argument('--below', type=int, default=62)
    a = ap.parse_args()
    proj = Path(a.project)
    for d in ('images', 'overlay'):
        (proj / d).mkdir(parents=True, exist_ok=True)
    im = Image.open(a.image).convert('RGB')
    arr = np.asarray(im)
    full_mask = ink(im.convert('L'))
    spec = json.load(open(a.lines, encoding='utf-8'))
    try:
        font = ImageFont.truetype('arial.ttf', 18)
    except OSError:
        font = ImageFont.load_default()
    allb, meta = {}, {}
    for L in spec:
        pts = [(x, y if L.get('fixed') else refine(full_mask, x, y)) for x, y in L['pts']]
        xs = np.arange(L['x0'], L['x1'])
        px, py = zip(*pts)
        yc = np.interp(xs, px, py) if len(pts) > 1 else np.full(len(xs), py[0], float)
        top = a.above; H = a.above + a.below
        band = np.full((H, len(xs), 3), 255, np.uint8)
        for i, x in enumerate(xs):
            y0 = int(round(yc[i])) - top
            band[:, i] = arr[y0:y0 + H, x]
        bim = Image.fromarray(band)
        name = f"{a.prefix}_l{L['line']:02d}.png"
        bim.save(proj / 'images' / name)
        meta[name] = {'line': L['line'], 'x0': int(L['x0']), 'pts': [[int(x), int(y)] for x, y in pts], 'above': top}
        m = ndimage.binary_opening(ink(bim.convert('L')), iterations=1)
        lab, n = ndimage.label(m)
        comps = []
        for i, sl in enumerate(ndimage.find_objects(lab)):
            if sl is None:
                continue
            area = int((lab[sl] == i + 1).sum())
            if area < 20:
                continue
            yy, xx = np.nonzero(lab[sl] == i + 1)
            comps.append([sl[1].start, sl[0].start, sl[1].stop, sl[0].stop, area, sl[0].start + yy.mean()])
        core0, core1 = top - 32, top + 30            # x-height zone around the line centre
        big = [c for c in comps if core0 <= c[5] <= core1 and (c[3] - c[1] >= 18 or c[2] - c[0] >= 22) and c[4] >= 60]
        small = [c for c in comps if c not in big and top - 75 <= c[5] < core0 + 8]
        big.sort(key=lambda c: c[0])
        groups = []
        for c in big:
            if groups:
                g = groups[-1]
                ov = min(g[2], c[2]) - max(g[0], c[0])
                if ov > 0.7 * min(g[2] - g[0], c[2] - c[0]):
                    g[0] = min(g[0], c[0]); g[1] = min(g[1], c[1]); g[2] = max(g[2], c[2]); g[3] = max(g[3], c[3])
                    continue
            groups.append(list(c[:4]))
        ws = sorted(g[2] - g[0] for g in groups)
        med = ws[len(ws) // 2] if ws else 30
        out, stack = [], list(groups)
        while stack:
            g = stack.pop(0)
            w = g[2] - g[0]
            if w <= 1.6 * med:
                out.append(g); continue
            col = ndimage.uniform_filter1d(m[core0:core1, g[0]:g[2]].sum(axis=0).astype(float), 3)
            lo, hi = int(0.5 * med), w - int(0.5 * med)
            if hi <= lo:
                out.append(g); continue
            cut = lo + int(np.argmin(col[lo:hi]))
            if col[cut] > 0.4 * col.max():
                out.append(g); continue
            sub = m[g[1]:g[3], g[0]:g[2]]
            parts = []
            for a0, a1 in ((0, cut), (cut, w)):
                ys = np.nonzero(sub[:, a0:a1].any(axis=1))[0]
                if len(ys):
                    parts.append([g[0] + a0, g[1] + int(ys[0]), g[0] + a1, g[1] + int(ys[-1]) + 1])
            stack[:0] = parts
        groups = sorted(out, key=lambda g: g[0])
        for c in small:
            cx = (c[0] + c[2]) / 2
            hit = [g for g in groups if g[0] - 6 <= cx <= g[2] + 6]
            if hit:
                g = min(hit, key=lambda g: abs((g[0] + g[2]) / 2 - cx))
                g[0] = min(g[0], c[0]); g[1] = min(g[1], c[1]); g[2] = max(g[2], c[2]); g[3] = max(g[3], c[3])
        bx = [{'line': 1, 'x': int(g[0]), 'y': int(g[1]), 'w': int(g[2] - g[0]), 'h': int(g[3] - g[1])} for g in groups]
        for i, b in enumerate(bx, 1):
            b['n'] = i
        allb[name] = bx
        ov = bim.copy(); d = ImageDraw.Draw(ov)
        for b in bx:
            col = [(220, 0, 0), (0, 140, 0), (0, 0, 220)][b['n'] % 3]
            d.rectangle([b['x'], b['y'], b['x'] + b['w'], b['y'] + b['h']], outline=col, width=2)
            d.text((b['x'] + 1, b['y'] + b['h'] + 1 if b['n'] % 2 else max(b['y'] - 19, 0)), str(b['n']), fill=col, font=font)
        ov.save(proj / 'overlay' / name)
        print(f'{name}: {len(bx)} boxes, {bim.size[0]}x{bim.size[1]}, centres {meta[name]["pts"]}')
    json.dump(allb, open(proj / 'boxes.json', 'w', encoding='utf-8'), indent=1)
    json.dump(meta, open(proj / 'bands_meta.json', 'w', encoding='utf-8'), indent=1)


if __name__ == '__main__':
    main()
