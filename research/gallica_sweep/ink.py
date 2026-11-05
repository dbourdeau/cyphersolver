# Ink fraction per canvas: share of pixels much darker than the local paper, central 80% of the frame.
import sys, os, json
from glob import glob
import numpy as np
from PIL import Image, ImageFilter
d = sys.argv[1]; res = {}
for f in sorted(glob(f'{d}/c*.jpg')):
    im = Image.open(f).convert('L'); im = im.resize((400, int(im.height * 400 / im.width)))
    a = np.asarray(im, dtype=float); h, w = a.shape
    a = a[int(h*.1):int(h*.9), int(w*.1):int(w*.9)]
    bg = np.asarray(Image.fromarray(a.astype('uint8')).filter(ImageFilter.MedianFilter(15)), dtype=float)
    res[os.path.basename(f)[1:4]] = round(float(((bg - a) > 40).mean()), 4)
json.dump(res, open(f'{d}_ink.json', 'w'), indent=0)
for k, v in res.items(): print(k, v)
