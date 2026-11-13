"""python dz.py <man> : for every local image of the series, the 195x130 px window (native 900 px scale) centred on the place
with the most isolated small glyphs (digi.score), 64 windows a sheet (8x8) -> scratch/ps/<man>_d_<first>.jpg"""
import sys, os, glob, json
from PIL import Image, ImageDraw
import rik, digi
man = sys.argv[1]; fs = sorted(glob.glob(f'{rik.SP}/pg/{man}/*.jpg')); W, H = 195, 130; out = {}
tiles = []
for f in fs:
    i = int(os.path.basename(f)[:5]); im = Image.open(f).convert('L'); s, (r, c) = digi.score(im); out[i] = s
    cx, cy = c + 100, r + 60; x0 = max(0, min(im.size[0] - W, cx - W // 2)); y0 = max(0, min(im.size[1] - H, cy - H // 2))
    t = im.crop((x0, y0, x0 + W, y0 + H)); d = ImageDraw.Draw(t); d.rectangle([0, 0, 26, 11], fill=255); d.text((1, 0), str(i), fill=0)
    tiles.append((i, t))
for k in range(0, len(tiles), 64):
    ch = tiles[k:k + 64]; sh = Image.new('L', (8 * W, ((len(ch) + 7) // 8) * H), 200)
    for j, (i, t) in enumerate(ch): sh.paste(t, ((j % 8) * W, (j // 8) * H))
    p = f'{rik.SP}/ps/{man}_d_{ch[0][0]:03d}.jpg'; sh.save(p, quality=80); print(p)
json.dump(out, open(f'{rik.SP}/ps/{man}_digi.json', 'w'))
