# python3 pagesheets.py <dir> <start> <end> [cols rows pagew]
# Splits each microfilm opening at the gutter, drops halves with almost no writing (blank versos, address panels:
# fewer than MINROWS rows with 8 or more strong ink strokes across, page edges excluded), crops each kept half to its writing and tiles the pages. Label cNNNNL / cNNNNR.
# Dropped halves are listed in <dir>_sheets/dropped.txt so the skip can be audited.
import os, sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
d = sys.argv[1]; a = int(sys.argv[2]); b = int(sys.argv[3])
cols, rows, PW = (int(x) for x in sys.argv[4:7]) if len(sys.argv) > 6 else (6, 4, 260)
PH = int(PW * 1.44); MINROWS = 28
out = d + '_sheets'; os.makedirs(out, exist_ok=True)
def halves(fn):
    im = Image.open(fn).convert('L'); A = np.asarray(im, dtype=np.int16); h, w = A.shape
    bg = np.asarray(im.filter(ImageFilter.MedianFilter(9)).filter(ImageFilter.BoxBlur(6)), dtype=np.int16)
    ink = ((bg - A) > 28) & (bg > 105); strong = ((bg - A) > 48) & (bg > 105)
    col = ink.mean(0); k = np.convolve(col, np.ones(9) / 9, 'same')
    lo, hi = int(w * .40), int(w * .62); g = lo + int(np.argmin(k[lo:hi]))
    res = []
    for side, (x0, x1) in (('L', (0, g)), ('R', (g, w))):
        m = ink[:, x0:x1]; ms = strong[:, x0:x1]; e = int((x1 - x0) * .08); ms = ms[:, e:ms.shape[1] - e]
        tr = (ms[:, 1:] & ~ms[:, :-1]).sum(1); r = tr >= 8; nrows = int(r.sum())
        if nrows < MINROWS: res.append((side, (x0, 0, x1, h), nrows)); continue
        ys = np.where(r)[0]; cs = np.where(m[ys[0]:ys[-1] + 1].mean(0) > 0.004)[0]
        if len(cs) == 0: res.append((side, (x0, 0, x1, h), 0)); continue
        box = (max(x0 + cs[0] - 6, 0), max(ys[0] - 6, 0), min(x0 + cs[-1] + 7, w), min(ys[-1] + 7, h))
        res.append((side, im.crop(box), nrows))
    return res
BORD = 12   # halves with BORD..MINROWS-1 text rows go, uncropped, on small "b" sheets (8x5), so that only near-blank halves are unseen
tiles = []; btiles = []; drop = open(f'{out}/dropped.txt', 'a')
def fit(im, pw, ph):
    s = min(pw / im.width, ph / im.height, 1.6)
    return im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)
for i in range(a, b + 1):
    fn = f'{d}/c{i:04d}.jpg'
    if not os.path.exists(fn): continue
    for side, im, n in halves(fn):
        if isinstance(im, tuple):
            if n >= BORD: btiles.append((f'c{i:04d}{side}', fit(Image.open(fn).convert('L').crop(im), 195, 280)))
            else: drop.write(f'c{i:04d}{side} rows={n}\n')
            continue
        tiles.append((f'c{i:04d}{side}', fit(im, PW, PH)))
def emit(tiles, cols, rows, PW, PH, pre):
    per = cols * rows
    for k in range(0, len(tiles), per):
        grp = tiles[k:k + per]
        sh = Image.new('L', (PW * cols, (PH + 12) * rows), 200); dr = ImageDraw.Draw(sh)
        for j, (lab, im) in enumerate(grp):
            x = PW * (j % cols); y = (PH + 12) * (j // cols); sh.paste(im, (x, y + 12)); dr.text((x + 2, y), lab, fill=0)
        fn = f'{out}/{pre}{grp[0][0]}_{grp[-1][0]}.jpg'; sh.save(fn, quality=80); print(fn)
emit(tiles, cols, rows, PW, PH, 'p'); emit(btiles, 8, 5, 195, 280, 'b')
