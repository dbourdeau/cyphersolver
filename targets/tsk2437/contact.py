"""Contact sheets of exemplars per class from a pass file.
Usage: python contact.py <passfile> <outdir> [class ...]   (no class = all classes with >= 1 sign)
Each tile is 150 x 150 native px around the sign (flattened), upscaled 1.4x, labelled line@x and grade."""
import os
import sys
import collections
import numpy as np
import cv2
import win
import tok

# line band: x0, x1, ytop at x0, ytop at x1, ybot at x0, ybot at x1 (as used for the reading windows)
BAND = {
    'L1': (1830, 5050, 440, 360, 610, 540),
    'L2': (1550, 4950, 1150, 1100, 1370, 1330),
    'L3': (1800, 4950, 1960, 1900, 2180, 2130),
    'L4': (1480, 5020, 2250, 2110, 2400, 2270),
    'L5': (1700, 4800, 2380, 2310, 2550, 2490),
    'L6': (1500, 5000, 3310, 3250, 3470, 3430),
    'L7': (1550, 5000, 4270, 4230, 4430, 4390),
    'L8': (1700, 5050, 5250, 5140, 5440, 5330),
}


def ymid(ln, x):
    x0, x1, t0, t1, b0, b1 = BAND[ln]
    f = min(1, max(0, (x - x0) / (x1 - x0)))
    return int(((t0 + (t1 - t0) * f) + (b0 + (b1 - b0) * f)) / 2)


def tile(g, ln, x, label, S=150, scale=1.4):
    y = ymid(ln, x)
    c = win.render(g, x - S // 2, y - S // 2, x + S // 2, y + S // 2, scale, 'flat')
    c = cv2.cvtColor(c, cv2.COLOR_GRAY2BGR)
    cv2.putText(c, label, (3, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (0, 0, 255), 1)
    cv2.rectangle(c, (0, 0), (c.shape[1] - 1, c.shape[0] - 1), (80, 80, 80), 1)
    return c


def sheet(g, items, cols=6):
    tiles = [tile(g, ln, x, '%s@%d %s' % (ln, x, gr[0])) for ln, x, gr in items]
    h, w = tiles[0].shape[:2]
    rows = (len(tiles) + cols - 1) // cols
    img = np.full((rows * h, cols * w, 3), 255, np.uint8)
    for i, t in enumerate(tiles):
        r, c = divmod(i, cols)
        img[r * h:(r + 1) * h, c * w:(c + 1) * w] = t
    return img


if __name__ == '__main__':
    rows = tok.parse(sys.argv[1])
    outdir = sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    want = sys.argv[3:]
    by = collections.defaultdict(list)
    for ln, x, code, grade, note in rows:
        if code in ('|', ''):
            continue
        by[code].append((ln, x, grade))
    g = win.load()
    for code, items in by.items():
        if want and code not in want:
            continue
        name = code.replace('?', 'Q').replace('^', 'hat').replace('-', 'dash').replace('.', 'dot')
        # firm first, then likely, doubtful
        order = {'firm': 0, 'likely': 1, 'doubtful': 2}
        items = sorted(items, key=lambda t: order.get(t[2], 3))
        for k in range(0, len(items), 18):
            img = sheet(g, items[k:k + 18])
            out = os.path.join(outdir, 'cls_%s_%d.png' % (name, k // 18))
            cv2.imwrite(out, img)
            print(out, len(items[k:k + 18]), 'of', len(items))
