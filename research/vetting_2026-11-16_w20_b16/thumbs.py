"""Fetch Arcinsys NI thumbnails of a digitised unit until 404; build contact sheets. python thumbs.py <dir-url> <prefix> <outdir>"""
import sys, os, time, requests
from PIL import Image
base, pre, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
s = requests.Session(); s.headers['User-Agent'] = 'Mozilla/5.0'
n = 1; files = []
while True:
    p = os.path.join(out, f'{n:04d}.jpg')
    if not os.path.exists(p):
        r = s.get(f'{base}/thumbs/{pre}_aufn_{n:04d}.jpg', timeout=60)
        if r.status_code != 200: break
        open(p, 'wb').write(r.content); time.sleep(0.4)
    files.append(p); n += 1
print('thumbs', len(files))
per = 40
for k in range(0, len(files), per):
    ims = [Image.open(f) for f in files[k:k+per]]
    w = max(i.width for i in ims); h = max(i.height for i in ims)
    sheet = Image.new('RGB', (w*8, h*5), 'white')
    for j, im in enumerate(ims): sheet.paste(im, ((j % 8)*w, (j//8)*h))
    sheet.save(os.path.join(out, f'sheet_{k+1:04d}.jpg'))
