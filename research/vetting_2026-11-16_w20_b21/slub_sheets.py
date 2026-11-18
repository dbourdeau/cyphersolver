"""Download all 221 SLUB Mscr.Dresd.App.3165 Bd. 6 pages at 300 px and build 5x4 contact sheets in img/slub_sheet_NN.jpg."""
import json, os, time, urllib.request, io
from PIL import Image, ImageDraw
m = json.load(open('raw/slub_manifest.json', encoding='utf8'))
cs = m['sequences'][0]['canvases']
os.makedirs('img/slub_t', exist_ok=True)
for i, c in enumerate(cs, 1):
    p = f'img/slub_t/{i:04d}.jpg'
    if os.path.exists(p): continue
    u = c['images'][0]['resource']['service']['@id'] + '/full/300,/0/default.jpg'
    d = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read()
    open(p, 'wb').write(d); time.sleep(0.6)
fs = sorted(os.listdir('img/slub_t'))
for s in range(0, len(fs), 20):
    W, H = 300, 470
    sheet = Image.new('RGB', (W * 5, H * 4), 'white'); dr = ImageDraw.Draw(sheet)
    for k, f in enumerate(fs[s:s + 20]):
        im = Image.open('img/slub_t/' + f); im.thumbnail((W, H - 20))
        x, y = (k % 5) * W, (k // 5) * H
        sheet.paste(im, (x, y + 20)); dr.text((x + 5, y + 3), f[:-4], fill='red')
    sheet.save(f'img/slub_sheet_{s // 20:02d}.jpg', quality=80)
print('done', len(fs))
