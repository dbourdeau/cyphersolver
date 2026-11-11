"""python cz.py <man> i j ... : fetch each image at 2000 px and cut a 760x420 window round the digi.score maximum
(the place with most digit-like glyphs); 6 a sheet (2 cols) -> scratch/ps/<man>_c_<first>.jpg. Used to tell glossed from bare cipher."""
import sys, os
from PIL import Image
import rik, digi
man = sys.argv[1]; ids = [int(x) for x in sys.argv[2:]]; os.makedirs(rik.SP + '/hi', exist_ok=True)
tiles = []
for i in ids:
    lo = Image.open(f'{rik.SP}/pg/{man}/{i:05d}.jpg'); s, (r, c) = digi.score(lo)
    p0 = f'{rik.SP}/hi/{man}_{i:05d}_2000.jpg'
    if os.path.exists(p0): im = Image.open(p0).convert('L')
    else: im = rik.crop(rik.img(man, i, 2000, True)); im.save(p0, quality=85)
    f = im.size[0] / lo.size[0]; cx, cy = int((c + 100) * f), int((r + 60) * f); W, H = 760, 420
    x0 = max(0, min(im.size[0] - W, cx - W // 2)); y0 = max(0, min(im.size[1] - H, cy - H // 2)); tiles.append(im.crop((x0, y0, x0 + W, y0 + H)))
for k in range(0, len(ids), 6):
    print(rik.grid(tiles[k:k + 6], ids[k:k + 6], 2, 760, f'{rik.SP}/ps/{man}_c_{ids[k]}.jpg'))
