"""Download full-size frames of a unit to scratch and write crops. usage: python3 full.py <bsid> <outdir> <img> [<img> ...]
Each frame is saved as f<img>.jpg (full size); l<img>.jpg and r<img>.jpg are the left and right halves at 1500 px wide."""
import sys, time, io, os
import ao
from PIL import Image
bsid, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True); ids = ao.refs(bsid)
for n in [int(x) for x in sys.argv[3:]]:
    fn = os.path.join(out, 'f%d.jpg' % n)
    if not os.path.exists(fn):
        open(fn, 'wb').write(ao.get('https://api.rigsarkivet.dk/ao/v1/images/%s' % ids[n - 1], True)); time.sleep(1.5)
    im = Image.open(fn).convert('RGB'); w, h = im.size
    for tag, box in (('l', (0, 0, w // 2 + 60, h)), ('r', (w // 2 - 60, 0, w, h))):
        c = im.crop(box); c = c.resize((1500, int(c.height * 1500 / c.width))); c.save(os.path.join(out, '%s%d.jpg' % (tag, n)), quality=80)
    print(n, ids[n - 1], im.size, flush=True)
