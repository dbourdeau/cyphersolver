import sys, numpy as np
from PIL import Image, ImageOps
src, tag, x0f, x1f, y0f, y1f = sys.argv[1], sys.argv[2], *map(float, sys.argv[3:7])
im = Image.open(src).convert('L'); w, h = im.size
a = 255 - np.asarray(im, dtype=float)
x0, x1, y0, y1 = int(w*x0f), int(w*x1f), int(h*y0f), int(h*y1f)
prof = (a[y0:y1, x0:x1] > 90).sum(1).astype(float)
k = np.ones(5)/5; p = np.convolve(prof, k, 'same')
# local maxima = line centres
cent = []
for i in range(6, len(p)-7):
    if p[i] == max(p[i-6:i+7]) and p[i] > p.max()*0.25:
        if not cent or i - cent[-1] > 14: cent.append(i)
print(len(cent), [c+y0 for c in cent])
for n, c in enumerate(cent):
    cy = c + y0
    s = im.crop((x0, cy-22, x1, cy+18))
    s = ImageOps.autocontrast(s, cutoff=1)
    s = s.resize((s.width*3//2*2, s.height*3), Image.LANCZOS)
    s.save(f'lines/{tag}_{n+1:02d}.png')
