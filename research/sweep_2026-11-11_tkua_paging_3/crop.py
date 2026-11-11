"""Full-size frame (cached in <dir>/f<img>.jpg) cropped by fractions and scaled. usage: python3 crop.py <bsid> <dir> <img> <x0> <y0> <x1> <y1> [width=1500] -> <dir>/c<img>_<x0>_<y0>.jpg"""
import sys, os, time, ao
from PIL import Image
bsid, d, n = sys.argv[1], sys.argv[2], int(sys.argv[3]); x0, y0, x1, y1 = (float(v) for v in sys.argv[4:8]); W = int(sys.argv[8]) if len(sys.argv) > 8 else 1500
os.makedirs(d, exist_ok=True); fn = '%s/f%d.jpg' % (d, n)
if not os.path.exists(fn):
    open(fn, 'wb').write(ao.get('https://api.rigsarkivet.dk/ao/v1/images/%s' % ao.refs(bsid)[n - 1], True)); time.sleep(1)
im = Image.open(fn).convert('RGB'); w, h = im.size; c = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
c = c.resize((W, int(c.height * W / c.width))); out = '%s/c%d_%s_%s.jpg' % (d, n, sys.argv[4], sys.argv[5]); c.save(out, quality=82); print(out)
