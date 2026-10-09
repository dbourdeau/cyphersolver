"""batchsheet.py prefix rec... : content pages of many records, 4 per sheet, each labelled with its file name."""
import sys, glob, os
import numpy as np
from PIL import Image, ImageDraw
def ink(p):
    im = np.asarray(Image.open(p).convert('L'), dtype=float); h, w = im.shape
    c = im[int(h*.1):int(h*.9), int(w*.1):int(w*.9)]; return (c < np.median(c)-40).mean()*1000
pages = []
for r in sys.argv[2:]:
    ps = sorted(glob.glob('img/v/R%s_I*_P*.jpg' % r), key=lambda p: int(p.rsplit('_P', 1)[1][:-4]))
    pages += [p for p in ps if ink(p) >= 8]
for k in range(0, len(pages), 4):
    ims = []
    for p in pages[k:k+4]:
        i = Image.open(p).convert('RGB'); i = i.resize((int(i.width*1400/i.height), 1400))
        d = ImageDraw.Draw(i); d.rectangle((0, 0, 330, 40), fill='yellow'); d.text((5, 5), os.path.basename(p)[:-4], fill='black', font_size=28)
        ims.append(i)
    o = Image.new('RGB', (sum(i.width for i in ims), 1400), 'white'); x = 0
    for i in ims: o.paste(i, (x, 0)); x += i.width
    o.thumbnail((2000, 2000)); out = '%s_%d.jpg' % (sys.argv[1], k//4+1); o.save(out, quality=85)
    print(out, [os.path.basename(p) for p in pages[k:k+4]])
