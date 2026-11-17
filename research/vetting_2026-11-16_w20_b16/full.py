"""Fetch full images n1..n2 of an Arcinsys NI unit, save downscaled to 1400 px wide. python full.py <dir-url> <prefix> <outdir> n1 n2"""
import sys, os, time, io, requests
from PIL import Image
base, pre, out, a, b = sys.argv[1:6]
os.makedirs(out, exist_ok=True)
s = requests.Session(); s.headers['User-Agent'] = 'Mozilla/5.0'
for n in range(int(a), int(b)+1):
    p = os.path.join(out, f'f{n:04d}.jpg')
    if os.path.exists(p): continue
    r = s.get(f'{base}/{pre}_aufn_{n:04d}.jpg', timeout=120)
    if r.status_code != 200: print('miss', n); continue
    im = Image.open(io.BytesIO(r.content)).convert('L'); im.thumbnail((1400, 1400)); im.save(p, quality=80)
    time.sleep(0.8)
print('done')
