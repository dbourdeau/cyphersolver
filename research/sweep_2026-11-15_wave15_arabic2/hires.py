"""python hires.py <hil64|hil65> <canvas index> <n> : stitch an n x n grid of 1,024-px region requests."""
import json, os, sys, io, time, urllib.request
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
ids = {'hil64': 't2mks65hc530', 'hil65': 't1mh128nf091'}
tag, idx, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
m = json.load(open(os.path.join(here, 'raw', 'man_%s.json' % ids[tag]), encoding='utf8'))
c = m['sequences'][0]['canvases'][idx]
svc = c['images'][0]['resource']['service']['@id']; W, H = c['width'], c['height']
tw, th = -(-W // n), -(-H // n)
s = 1024 / max(tw, th)
out = Image.new('RGB', (int(W * s) + n, int(H * s) + n))
for r in range(n):
    for q in range(n):
        x, y = q * tw, r * th; w, h = min(tw, W - x), min(th, H - y)
        u = '%s/%d,%d,%d,%d/%d,/0/default.jpg' % (svc, x, y, w, h, max(1, int(w * s)))
        d = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=120).read()
        out.paste(Image.open(io.BytesIO(d)), (int(x * s), int(y * s))); time.sleep(0.6)
fn = os.path.join(here, 'img', '%s_%03d_hires%d.jpg' % (tag, idx, n)); out.save(fn, quality=88); print(fn, out.size, c['label'])
