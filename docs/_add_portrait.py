"""Add a sender or recipient portrait to a write-up.

    python docs/_add_portrait.py <slug> <sender|recipient> "<display name>" "File:<Commons file>" "<what, e.g. Portrait by Titian, 1551>" [--box x0,y0,x1,y1]
    python docs/_add_portrait.py <slug> --clear

Checks the Commons licence (public domain or CC0 only), downloads an 800-px copy, crops a 192-px square around the
face (YuNet, fetched once into ~/.cache; top-centre fallback) to docs/portrait_<name>.jpg, and updates
docs/_portraits.json. A person already on the site reuses their image. Rebuild with _build_site.py afterwards.

--box x0,y0,x1,y1 (fractions of the image width/height) crops that region instead of detecting a face, from a
2000-px copy so a small figure in a group scene stays sharp; the region is squared around its centre and resized
to 192 px. Use it only when the source identifies which figure is the person; caption it "Detail of <scene>, ...".
"""
import io, json, pathlib, re, sys, unicodedata, urllib.parse, urllib.request
from PIL import Image

DOCS = pathlib.Path(__file__).resolve().parent
MANIFEST = DOCS / '_portraits.json'
UA = {'User-Agent': 'cyphersolver-site/1.0 (portrait fetch)'}
MODEL = pathlib.Path.home() / '.cache' / 'yunet_2023mar.onnx'
MODEL_URL = 'https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx'

def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r: return r.read()

def key(name):
    k = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', k).strip('-')

def faces(im):
    try:
        import cv2, numpy as np
        if not MODEL.exists():
            MODEL.parent.mkdir(parents=True, exist_ok=True); MODEL.write_bytes(get(MODEL_URL))
        det = cv2.FaceDetectorYN_create(str(MODEL), '', im.size, 0.6)
        _, res = det.detect(cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR))
        return [tuple(int(v) for v in r[:4]) for r in (res if res is not None else [])]
    except Exception as e:
        print('face detection unavailable, using top-centre crop:', e); return []

def crop(im, out=192, box=None):
    W, H = im.size
    if box:
        x0, y0, x1, y1 = box[0] * W, box[1] * H, box[2] * W, box[3] * H
        side = int(min(max(x1 - x0, y1 - y0), W, H)); cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        l = int(min(max(cx - side / 2, 0), W - side)); t = int(min(max(cy - side / 2, 0), H - side))
        return im.crop((l, t, l + side, t + side)).resize((out, out), Image.LANCZOS)
    fs = [f for f in faces(im) if f[1] + f[3] / 2 < H * .7]
    if fs:
        x, y, w, h = max(fs, key=lambda f: f[2]); side = min(W, H, int(w * 2.8)); cx, cy = x + w / 2, y + h * .75
    else:
        print('no face found: check the crop by eye (profiles are often missed)')
        side = min(W, H) if H <= W * 1.25 else int(W * .75); cx, cy = W / 2, side / 2 + H * .04
    l = int(min(max(cx - side / 2, 0), W - side)); t = int(min(max(cy - side / 2, 0), H - side))
    return im.crop((l, t, l + side, t + side)).resize((out, out), Image.LANCZOS)

def main(a, box=None):
    data = json.loads(MANIFEST.read_text(encoding='utf-8')) if MANIFEST.exists() else {}
    slug = a[0]
    if not (DOCS / f'{slug}.html').exists(): sys.exit(f'no page docs/{slug}.html')
    if a[1:] == ['--clear']:
        data.pop(slug, None)
    else:
        role, name, f, what = a[1:5]
        if role not in ('sender', 'recipient'): sys.exit('role must be sender or recipient')
        f = f if f.startswith('File:') else 'File:' + f
        known = {p['file']: p['img'] for v in data.values() for p in v if p.get('file')}
        img = None if box else known.get(f)
        if not img:
            q = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode({'action': 'query', 'titles': f,
                'prop': 'imageinfo', 'iiprop': 'url|extmetadata', 'iiurlwidth': 2000 if box else 800, 'format': 'json'})
            info = next(iter(json.loads(get(q))['query']['pages'].values())).get('imageinfo')
            if not info: sys.exit(f'{f} not found on Commons')
            lic = info[0].get('extmetadata', {}).get('LicenseShortName', {}).get('value', '')
            if not re.search(r'public domain|^PD|CC0', lic, re.I): sys.exit(f'licence is {lic!r}: public domain or CC0 only')
            used = {p['img'] for v in data.values() for p in v if p.get('img')}
            img, n = f'portrait_{key(name)}.jpg', 2
            while img in used or (DOCS / img).exists(): img, n = f'portrait_{key(name)}-{n}.jpg', n + 1
            crop(Image.open(io.BytesIO(get(info[0].get('thumburl') or info[0]['url']))).convert('RGB'), box=box).save(DOCS / img, quality=86, optimize=True)
            print('saved', img, '(' + lic + ')')
        rows = [p for p in data.get(slug, []) if p['role'] != role]
        rows.append({'role': role, 'name': name, 'img': img, 'what': what.rstrip('.'),
                     'credit': 'Wikimedia Commons, public domain', 'file': f})
        data[slug] = sorted(rows, key=lambda p: p['role'] != 'sender')
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
    print(slug, '->', [p['name'] for p in data.get(slug, [])])

if __name__ == '__main__':
    args, box = sys.argv[1:], None
    if '--box' in args:
        i = args.index('--box'); box = [float(v) for v in args[i + 1].split(',')]; del args[i:i + 2]
        if len(box) != 4 or not (0 <= box[0] < box[2] <= 1 and 0 <= box[1] < box[3] <= 1): sys.exit('--box x0,y0,x1,y1 in 0..1')
    if len(args) not in (2, 5): sys.exit(__doc__)
    main(args, box)
