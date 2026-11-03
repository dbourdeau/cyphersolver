# c. 50r: enlarged strips, gloss masked, for the row-by-row copy. Four parts per row, 2.1x.
import json, sys
from PIL import Image, ImageDraw, ImageEnhance

im = ImageEnhance.Contrast(Image.open('scans/e50r_full.jpg')).enhance(1.2)
rows = json.load(open('work/rows.json'))
H, SC, TOP = 96, 2.1, 22
hh = int(H * SC)
A, B = 190, 3010
want = [int(a) for a in sys.argv[1:]] or list(range(1, 20))


def band(r, x0, x1):
    o = Image.new('RGB', (x1 - x0, H), 'white')
    for x in range(x0, x1, 4):
        y = int(r['a'] * (x + 2) + r['c']) - TOP
        o.paste(im.crop((x, y, x + 4, y + H)), (x - x0, 0))
    return o


items = []
w = (B - A) // 4
for i in want:
    r = rows[i - 1]
    for j in range(4):
        items.append((i, j, r, A + j * w - 20, A + (j + 1) * w + 20))
n = 0
for k in range(0, len(items), 5):
    ch = items[k:k + 5]
    S = Image.new('RGB', (1610, len(ch) * (hh + 6)), 'white')
    d = ImageDraw.Draw(S)
    for q, (ln, j, r, x0, x1) in enumerate(ch):
        b = band(r, x0, x1).resize((int((x1 - x0) * SC), hh), Image.LANCZOS)
        S.paste(b, (40, q * (hh + 6)))
        d.text((2, q * (hh + 6) + 60), f'{ln:02d}{"abcd"[j]}', fill='red')
    S.save(f'scans/t/z50_{n}.png')
    n += 1
print(n)
