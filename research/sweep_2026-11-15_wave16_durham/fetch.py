"""python fetch.py <hil64|hil65> <first> <last> : fetch frames as a 2x2 grid of IIIF region requests over the
bounding box of the forms (found on the 1,024-px copy of wave 15), stitched to about 2,000 px. One request a second."""
import json, os, sys, io, time, glob, urllib.request, urllib.error
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
w15 = os.path.join(here, '..', 'sweep_2026-11-15_wave15_arabic2', 'img')
ids = {'hil64': 't2mks65hc530', 'hil65': 't1mh128nf091'}
tag, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
m = json.load(open(os.path.join(here, 'raw', 'man_%s.json' % ids[tag]), encoding='utf8'))
cs = m['sequences'][0]['canvases']
thumbs = {int(os.path.basename(f)[:3]): f for f in glob.glob(os.path.join(w15, tag, '*.jpg'))}
os.makedirs(os.path.join(here, 'img', tag), exist_ok=True)

def bbox(i):
    if i not in thumbs: return (0.0, 0.0, 1.0, 1.0)
    im = Image.open(thumbs[i]).convert('L'); w, h = im.size
    bw = im.point(lambda v: 255 if v > 195 else 0)
    cols = [sum(1 for y in range(0, h, 4) if bw.getpixel((x, y))) / (h / 4) for x in range(0, w, 2)]
    rows = [sum(1 for x in range(0, w, 4) if bw.getpixel((x, y))) / (w / 4) for y in range(0, h, 2)]
    xs = [k for k, v in enumerate(cols) if v > 0.2]; ys = [k for k, v in enumerate(rows) if v > 0.2]
    if not xs or not ys: return (0.0, 0.0, 1.0, 1.0)
    x0, x1, y0, y1 = xs[0] * 2 / w, xs[-1] * 2 / w, ys[0] * 2 / h, ys[-1] * 2 / h
    if x1 - x0 < 0.6 or y1 - y0 < 0.5: return (0.0, 0.0, 1.0, 1.0)
    return (max(0, x0 - .03), max(0, y0 - .02), min(1, x1 + .03), min(1, y1 + .02))

def get(u):
    for k in range(6):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=120).read()
        except urllib.error.HTTPError as e:
            print('HTTP', e.code, u, flush=True); time.sleep(30 * (k + 1) if e.code in (429, 503) else 5)
        except Exception as e:
            print('ERR', e, u, flush=True); time.sleep(10)
    raise SystemExit('gave up ' + u)

for i in range(a, b + 1):
    c = cs[i]; lab = ''.join(ch for ch in c['label'].split('/')[-1] if ch.isalnum() or ch in '-_')
    fn = os.path.join(here, 'img', tag, '%03d_%s.jpg' % (i, lab))
    if os.path.exists(fn): continue
    svc = c['images'][0]['resource']['service']['@id']; W, H = c['width'], c['height']
    fx0, fy0, fx1, fy1 = bbox(i)
    X0, Y0, BW, BH = int(fx0 * W), int(fy0 * H), int((fx1 - fx0) * W), int((fy1 - fy0) * H)
    n = 2; tw, th = -(-BW // n), -(-BH // n); s = 1024 / max(tw, th)
    out = Image.new('L', (int(BW * s) + n, int(BH * s) + n), 128)
    for r in range(n):
        for q in range(n):
            x, y = q * tw, r * th; w, h = min(tw, BW - x), min(th, BH - y)
            u = '%s/%d,%d,%d,%d/%d,/0/default.jpg' % (svc, X0 + x, Y0 + y, w, h, max(1, int(w * s)))
            out.paste(Image.open(io.BytesIO(get(u))).convert('L'), (int(x * s), int(y * s))); time.sleep(1.0)
    out.save(fn, quality=80); print(i, lab, 'bbox %.2f %.2f %.2f %.2f' % (fx0, fy0, fx1, fy1), out.size, flush=True)
print('done', flush=True)
