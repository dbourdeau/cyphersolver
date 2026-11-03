# c. 50r: full-width strips, gloss masked (only the band from the dots down is shown), dots counted by machine.
# Dots are blobs of ink in a thin band above the signs; language and key play no part.
import json
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance
from scipy import ndimage as ni

raw = Image.open('scans/e50r_full.jpg')
im = ImageEnhance.Contrast(raw).enhance(1.25)
g = np.array(raw.convert('L')).astype(float)
rows = json.load(open('work/rows.json'))
H, SC, TOP = 96, 1.5, 22
X0, X1 = 150, 3000


def dots(r):
    W = X1 - X0
    b = np.full((60, W), 255.0)
    for x in range(X0, X1):
        y = int(r['a'] * x + r['c'])
        b[:, x - X0] = g[y - 30:y + 30, x]
    bg = ni.median_filter(b, size=(1, 61))
    m = (b < bg - 45) & (b < 165)
    lab, n = ni.label(ni.binary_opening(m, iterations=1))
    out = []
    for i, sl in enumerate(ni.find_objects(lab)):
        h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        area = (lab[sl] == i + 1).sum()
        cy = (sl[0].start + sl[0].stop) / 2
        if area >= 90 and 18 <= h <= 46 and 8 <= w <= 36 and h >= 1.0 * w and 18 <= cy <= 42:
            out.append(X0 + (sl[1].start + sl[1].stop) / 2)
    return sorted(out)


def band(r, x0, x1):
    o = Image.new('RGB', (x1 - x0, H), 'white')
    for x in range(x0, x1, 4):
        y = int(r['a'] * (x + 2) + r['c']) - TOP
        o.paste(im.crop((x, y, x + 4, y + H)), (x - x0, 0))
    return o


items, res = [], {}
for i, r in enumerate(rows):
    xs = dots(r)
    res[f'{i + 1:02d}'] = xs
    a, b = 190, 3010
    w = (b - a) // 3
    for j in range(3):
        items.append((i + 1, 'abc'[j], r, a + j * w - (45 if j else 0), a + (j + 1) * w + (45 if j < 2 else 0), xs))
json.dump(res, open('work/e50r_dots.json', 'w'))
print({k: len(v) for k, v in res.items()})

per, n = 8, 0
hh = int(H * SC)
for k in range(0, len(items), per):
    ch = items[k:k + per]
    S = Image.new('RGB', (1560, len(ch) * (hh + 6)), 'white')
    d = ImageDraw.Draw(S)
    for j, (ln, s, r, x0, x1, xs) in enumerate(ch):
        b = band(r, x0, x1)
        b = b.resize((int(b.width * SC), hh), Image.LANCZOS)
        y = j * (hh + 6)
        S.paste(b, (44, y))
        d.text((2, y + 40), f'{ln:02d}{s}', fill='red')
    S.save(f'scans/t/r50_{n}.png')
    n += 1
print(n)
