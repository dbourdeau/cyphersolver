"""segment.py <folio> <x0> <y0> <x1> <y1> <out_prefix> [thr]
Composantes connexes (encre sombre) dans une bande de ligne ; fusion des composantes qui se recouvrent
horizontalement à >50 % (points + corps) ; sortie : <out>.json (boîtes en coordonnées page, ordre droite->gauche)
et <out>.jpg annoté (indices)."""
import sys, json
sys.path.insert(0, '/Users/bdudout/Library/Python/3.9/lib/python/site-packages')
import numpy as np
from PIL import Image, ImageDraw
IMG = '/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/ljs51/img/f%s_2343.jpg'
f, x0, y0, x1, y1, out = sys.argv[1:7]
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 100
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
im = Image.open(IMG % f).convert('L').crop((x0, y0, x1, y1))
a = np.array(im) < thr
H, Wd = a.shape
lab = np.zeros(a.shape, int); n = 0; boxes = []
for yy in range(H):
    for xx in range(Wd):
        if a[yy, xx] and not lab[yy, xx]:
            n += 1; st = [(yy, xx)]; lab[yy, xx] = n; ys = []; xs = []
            while st:
                cy, cx = st.pop(); ys.append(cy); xs.append(cx)
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < H and 0 <= nx < Wd and a[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = n; st.append((ny, nx))
            if len(ys) >= 25:
                boxes.append([min(xs), min(ys), max(xs), max(ys), len(ys)])
# fusion par recouvrement horizontal
boxes.sort(key=lambda b: -b[2]); merged = []
for b in boxes:
    for m in merged:
        ov = min(m[2], b[2]) - max(m[0], b[0])
        if ov > 0.5 * min(b[2] - b[0] + 1, m[2] - m[0] + 1):
            m[0] = min(m[0], b[0]); m[1] = min(m[1], b[1]); m[2] = max(m[2], b[2]); m[3] = max(m[3], b[3]); m[4] += b[4]; break
    else:
        merged.append(list(b))
merged.sort(key=lambda b: -b[2])
res = [{'i': i, 'box': [b[0] + x0, b[1] + y0, b[2] + x0, b[3] + y0], 'px': b[4]} for i, b in enumerate(merged)]
json.dump(res, open(out + '.json', 'w'))
vis = Image.open(IMG % f).convert('RGB').crop((x0, y0, x1, y1))
d = ImageDraw.Draw(vis)
for r in res:
    bx = r['box']; d.rectangle([bx[0] - x0, bx[1] - y0, bx[2] - x0, bx[3] - y0], outline=(255, 0, 0))
    d.text((bx[0] - x0, max(0, bx[1] - y0 - 11)), str(r['i']), fill=(0, 0, 255))
vis = vis.resize((int(vis.width * 0.9), int(vis.height * 0.9)))
vis.save(out + '.jpg'); print(len(res), 'segments')
