import sys, numpy as np
from PIL import Image, ImageOps
src, tag = sys.argv[1], sys.argv[2]
y0f, y1f = float(sys.argv[3]), float(sys.argv[4])
im = Image.open(src).convert('L'); w, h = im.size
a = 255 - np.asarray(im, dtype=float)
y0, y1 = int(h*y0f), int(h*y1f)
x0, x1 = int(w*0.05), int(w*0.97)
prof = (a[y0:y1, x0:x1] > 90).sum(1).astype(float)
p = np.convolve(prof, np.ones(5)/5, 'same')
cent = []
for i in range(7, len(p)-8):
    if p[i] == max(p[i-7:i+8]) and p[i] > p.max()*0.2:
        if not cent or i - cent[-1] > 15: cent.append(i)
cent = [c+y0 for c in cent]
print(len(cent), cent)
mid = (x0+x1)//2
for n, cy in enumerate(cent):
    for side, (a0, a1) in (('a', (x0-10, mid+40)), ('b', (mid-40, x1+15))):
        s = im.crop((a0, cy-19, a1, cy+17))
        s = ImageOps.autocontrast(s, cutoff=1)
        s = s.resize((s.width*3, s.height*3), Image.LANCZOS)
        s.save(f'lines/{tag}{n+1:02d}{side}.png')
