"""python region.py <tag> <idx> x0 y0 x1 y1 [cols] : hi-res IIIF region (fractions of the whole canvas), cols tiles across."""
import json, os, sys, io, time, urllib.request
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
ids = {'hil64': 't2mks65hc530', 'hil65': 't1mh128nf091'}
tag, idx = sys.argv[1], int(sys.argv[2]); x0, y0, x1, y1 = map(float, sys.argv[3:7]); n = int(sys.argv[7]) if len(sys.argv) > 7 else 2
c = json.load(open(os.path.join(here, 'raw', 'man_%s.json' % ids[tag]), encoding='utf8'))['sequences'][0]['canvases'][idx]
svc = c['images'][0]['resource']['service']['@id']; W, H = c['width'], c['height']
X0, Y0, BW, BH = int(x0 * W), int(y0 * H), int((x1 - x0) * W), int((y1 - y0) * H)
tw = -(-BW // n); s = min(1.0, 1024 / max(tw, BH))
out = Image.new('L', (int(BW * s) + n, int(BH * s) + 1), 128)
for q in range(n):
    x = q * tw; w = min(tw, BW - x)
    u = '%s/%d,%d,%d,%d/%d,/0/default.jpg' % (svc, X0 + x, Y0, w, BH, max(1, int(w * s)))
    d = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=120).read()
    out.paste(Image.open(io.BytesIO(d)).convert('L'), (int(x * s), 0)); time.sleep(1.0)
os.makedirs(os.path.join(here, 'img', 'v'), exist_ok=True)
fn = os.path.join(here, 'img', 'v', 'region_%s_%03d_%02d_%02d.jpg' % (tag, idx, int(x0 * 100), int(y0 * 100))); out.save(fn, quality=88); print(fn, out.size, c['label'])
