"""Fetch a IIIF manifest from archieven.nl (proxy.archieven.nl/iiif/<adt>/<GUID>), download the canvases to a scratch dir and build contact sheets.
usage: iiif_sheet.py <adt> <GUID> <scratch dir> [width=500] [per sheet=12] [first] [last]"""
import sys, json, os, time, requests
from PIL import Image
adt, guid, out = sys.argv[1:4]; w = int(sys.argv[4]) if len(sys.argv) > 4 else 500; per = int(sys.argv[5]) if len(sys.argv) > 5 else 12
a = int(sys.argv[6]) if len(sys.argv) > 6 else 1; b = int(sys.argv[7]) if len(sys.argv) > 7 else 10**6
os.makedirs(out, exist_ok=True); S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0'
m = S.get(f'https://proxy.archieven.nl/iiif/{adt}/{guid}', timeout=60).json()
ids = []
def walk(o):
    if isinstance(o, dict):
        if o.get('type') == 'ImageService3' or o.get('type') == 'ImageService2' or '@id' in o and 'profile' in o: ids.append(o.get('id') or o.get('@id'))
        for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
walk(m); ids = list(dict.fromkeys(ids)); print('label', json.dumps(m.get('label'), ensure_ascii=False)[:150], 'images', len(ids))
if not ids: print(json.dumps(m)[:1500]); sys.exit()
files = []
for i, u in enumerate(ids, 1):
    if i < a or i > b: continue
    fn = f'{out}/{i:04d}_{w}.jpg'
    if not os.path.exists(fn):
        r = S.get(f'{u}/full/{w},/0/default.jpg', timeout=120)
        if r.status_code != 200: print('ERR', i, r.status_code, u); continue
        open(fn, 'wb').write(r.content); time.sleep(0.7)
    files.append((i, fn))
for k in range(0, len(files), per):
    ch = files[k:k + per]; ims = [Image.open(f).convert('RGB') for _, f in ch]; cols = min(4, len(ims)); tw = 420
    ims = [im.resize((tw, int(im.height * tw / im.width))) for im in ims]; rows = (len(ims) + cols - 1) // cols; rh = max(im.height for im in ims)
    sh = Image.new('RGB', (cols * tw, rows * rh), 'white')
    for j, im in enumerate(ims): sh.paste(im, ((j % cols) * tw, (j // cols) * rh))
    fn = f'{out}/sheet_{ch[0][0]:04d}.jpg'; sh.save(fn, quality=80); print(fn)
