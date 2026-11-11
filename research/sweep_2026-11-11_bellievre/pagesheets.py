# python3 pagesheets.py <dir> <start> <end> [cols rows pagew]
# Splits each microfilm opening at the gutter, drops halves with almost no writing (blank versos, address panels:
# fewer than MINROWS rows with 9 or more ink strokes across), crops each kept half to its writing and tiles the pages. Label cNNNNL / cNNNNR.
# Dropped halves are listed in <dir>_sheets/dropped.txt so the skip can be audited.
import os, sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
d = sys.argv[1]; a = int(sys.argv[2]); b = int(sys.argv[3])
cols, rows, PW = (int(x) for x in sys.argv[4:7]) if len(sys.argv) > 6 else (6, 3, 260)
PH = int(PW * 1.45); MINROWS = 28
out = d + '_sheets'; os.makedirs(out, exist_ok=True)
def halves(fn):
    im = Image.open(fn).convert('L'); A = np.asarray(im, dtype=np.int16); h, w = A.shape
    bg = np.asarray(im.filter(ImageFilter.MedianFilter(9)).filter(ImageFilter.BoxBlur(6)), dtype=np.int16)
    ink = ((bg - A) > 28) & (bg > 105)
    col = ink.mean(0); k = np.convolve(col, np.ones(9) / 9, 'same')
    lo, hi = int(w * .40), int(w * .62); g = lo + int(np.argmin(k[lo:hi]))
    res = []
    for side, (x0, x1) in (('L', (0, g)), ('R', (g, w))):
        m = ink[:, x0:x1]; tr = (m[:, 1:] & ~m[:, :-1]).sum(1); r = tr >= 9; nrows = int(r.sum())
        if nrows < MINROWS: res.append((side, None, nrows)); continue
        ys = np.where(r)[0]; cs = np.where(m[ys[0]:ys[-1] + 1].mean(0) > 0.004)[0]
        if len(cs) == 0: res.append((side, None, nrows)); continue
        box = (max(x0 + cs[0] - 6, 0), max(ys[0] - 6, 0), min(x0 + cs[-1] + 7, w), min(ys[-1] + 7, h))
        res.append((side, im.crop(box), nrows))
    return res
tiles = []; drop = open(f'{out}/dropped.txt', 'a')
for i in range(a, b + 1):
    fn = f'{d}/c{i:04d}.jpg'
    if not os.path.exists(fn): continue
    for side, im, n in halves(fn):
        if im is None: drop.write(f'c{i:04d}{side} rows={n}\n'); continue
        s = min(PW / im.width, PH / im.height, 1.6)
        tiles.append((f'c{i:04d}{side}', im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)))
per = cols * rows
for k in range(0, len(tiles), per):
    grp = tiles[k:k + per]
    sh = Image.new('L', (PW * cols, (PH + 12) * rows), 200); dr = ImageDraw.Draw(sh)
    for j, (lab, im) in enumerate(grp):
        x = PW * (j % cols); y = (PH + 12) * (j // cols); sh.paste(im, (x, y + 12)); dr.text((x + 2, y), lab, fill=0)
    fn = f'{out}/p{grp[0][0]}_{grp[-1][0]}.jpg'; sh.save(fn, quality=80); print(fn)
