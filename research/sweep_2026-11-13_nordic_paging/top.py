"""python top.py <man> [N=64] [skip=0]: windows (195x130, native 900 px) of the N highest digit-texture scores of a volume, highest first, 8x8 sheet.
Scores come from digi.score; cached in ps/<man>_digi.json"""
import sys, os, glob, json
from PIL import Image, ImageDraw
import rik, digi
man = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 64; skip = int(sys.argv[3]) if len(sys.argv) > 3 else 0
cache = f'{rik.SP}/ps/{man}_digi.json'
sc = json.load(open(cache)) if os.path.exists(cache) else {}
fs = sorted(glob.glob(f'{rik.SP}/pg/{man}/*.jpg'))
for f in fs:
    i = str(int(os.path.basename(f)[:5]))
    if i in sc and len(sc[i]) == 3: continue
    s, (r, c) = digi.score(Image.open(f)); sc[i] = [s, r, c]
json.dump(sc, open(cache, 'w'))
top = sorted(sc.items(), key=lambda kv: -kv[1][0])[skip:skip + N]
W, H = 195, 130; sh = Image.new('L', (8 * W, ((len(top) + 7) // 8) * H), 200)
for j, (i, (s, r, c)) in enumerate(top):
    im = Image.open(f'{rik.SP}/pg/{man}/{int(i):05d}.jpg').convert('L')
    cx, cy = c + 100, r + 60; x0 = max(0, min(im.size[0] - W, cx - W // 2)); y0 = max(0, min(im.size[1] - H, cy - H // 2))
    t = im.crop((x0, y0, x0 + W, y0 + H)); d = ImageDraw.Draw(t); d.rectangle([0, 0, 50, 11], fill=255); d.text((1, 0), f'{i}:{s}', fill=0)
    sh.paste(t, ((j % 8) * W, (j // 8) * H))
p = f'{rik.SP}/ps/{man}_top{skip}.jpg'; sh.save(p, quality=80); print(p, 'n', len(sc), 'median', sorted(v[0] for v in sc.values())[len(sc)//2])
