"""Cut line crops from a full-resolution page, finding each line's height per column band by ink projection."""
import sys, numpy as np
from PIL import Image
src, prefix, nlines, y0, step = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
bands = [(380,1700),(1640,2960),(2900,4220),(4160,5300)] if len(sys.argv) < 7 else eval(sys.argv[6])
im = Image.open(src); g = np.asarray(im.convert('L')).astype(float)
H = 270
for i in range(nlines):
    out = Image.new('RGB', (max(b-a for a,b in bands), H*len(bands)), 'white')
    for j,(a,b) in enumerate(bands):
        exp = int(y0 + i*step)
        col = (g[max(0,exp-110):exp+110, a:b] < 110).sum(1).astype(float)
        col = np.convolve(col, np.ones(41)/41, 'same')
        yc = max(0,exp-110) + int(col.argmax()) if col.max() > 5 else exp
        out.paste(im.crop((a, yc-H//2, b, yc+H//2)), (0, H*j))
    out.save(f'{prefix}{i+1:02d}.jpg', quality=90)
