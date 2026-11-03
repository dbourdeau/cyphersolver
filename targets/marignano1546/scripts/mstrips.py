"""Line strips of the c. 13r cipher (scans/c13r_cipher.jpg = canvas 1 region x 800-5300, y 2950-5050).
usage: mstrips.py OUTPREFIX PER_IMAGE SCALE HALF_H"""
import sys
from PIL import Image, ImageOps, ImageDraw
CENTRES = [190, 378, 552, 743, 939, 1121, 1309, 1489, 1698, 1907]
pref, per, sc, hh = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
im = Image.open('scans/c13r_cipher.jpg').convert('L'); W = im.width
rows = []
for i, c in enumerate(CENTRES):
    for k, (x0, x1) in enumerate([(0, W // 2 + 120), (W // 2 - 120, W)]):
        r = ImageOps.autocontrast(im.crop((x0, c - hh, x1, c + hh)), cutoff=1)
        r = r.resize((int(r.width * sc), int(r.height * sc))).convert('RGB')
        ImageDraw.Draw(r).text((4, 2), f'M{i+1:02d}{"ab"[k]}', fill=(255, 0, 0)); rows.append(r)
for j in range(0, len(rows), 2 * per):
    g = rows[j:j + 2 * per]
    o = Image.new('RGB', (max(x.width for x in g), sum(x.height + 6 for x in g)), (0, 0, 255)); y = 0
    for x in g: o.paste(x, (0, y)); y += x.height + 6
    o.save(f'{pref}{j // (2 * per)}.png'); print(o.size)
