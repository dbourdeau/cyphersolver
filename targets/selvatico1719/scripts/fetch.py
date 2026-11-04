"""Fetch Estense IIIF scans for the Selvatico -> Riva letters.

One request at a time, ~1 s apart, User-Agent WAINUT-research. The server refuses
source regions over ~1 MP (HTTP 422), so full-size pages are fetched as tiles of at
most 1500x640 source pixels and stitched. Images go to ../scans/ (never committed).

usage: python fetch.py manifests            # list canvases of all uuids -> scans/canvases.json
       python fetch.py overview             # every canvas at ~1000 px wide
       python fetch.py full <uuid> <n>      # canvas n (1-based) at full size, stitched
"""
import io, json, os, sys, time, urllib.request
from PIL import Image

UA = {'User-Agent': 'WAINUT-research'}
HERE = os.path.dirname(os.path.abspath(__file__))
SCANS = os.path.join(HERE, '..', 'scans')
os.makedirs(SCANS, exist_ok=True)
UUIDS = {
    'f63082e8-940a-40f6-a750-3f79f0e92747': 'c04-07_1719-10-02',
    '50c0581b-9def-497e-88ac-54678e5eca0e': 'c12-13_1719-10-27',
    '761ee342-8fd0-49dd-8e4f-1872bb3d19d9': 'c14-15_10dic',
    '179df476-88bd-4f95-b4bd-574569bf8b6d': 'c02-03_2gen',
    'd65064be-e2e4-4e16-9289-367b8ec682ad': 'x_d65064be',
    'b398032c-89f0-4267-8ace-e5aa4d76a8e9': 'x_b398032c',
    '3cf6cbb0-da58-4f26-ae4f-c6a3e250b065': 'x_3cf6cbb0',
    '0c61023d-19aa-48e9-affa-89ec7da5ed67': 'x_0c61023d',
}
_last = [0.0]


def get(url):
    wait = 1.1 - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
    finally:
        _last[0] = time.time()
    return data


def manifests():
    out = {}
    for u, tag in UUIDS.items():
        m = json.loads(get(f'https://edl-jarvis.cultura.gov.it/meta/iiif/{u}/manifest'))
        cv = []
        for c in m['sequences'][0]['canvases']:
            img = c['images'][0]['resource']
            svc = img.get('service', {}).get('@id') or img['@id'].split('/full/')[0]
            lab = c.get('label')
            if isinstance(lab, list):
                lab = lab[0]
            if isinstance(lab, dict):
                lab = lab.get('@value')
            cv.append({'label': lab, 'service': svc, 'w': c.get('width'), 'h': c.get('height')})
        out[u] = {'tag': tag, 'canvases': cv}
        print(tag, len(cv), [x['label'][-6:] for x in cv], cv[0]['w'], cv[0]['h'])
    json.dump(out, open(os.path.join(SCANS, 'canvases.json'), 'w'), indent=1)


def load():
    return json.load(open(os.path.join(SCANS, 'canvases.json')))


def overview():
    d = load()
    for u, r in d.items():
        for i, c in enumerate(r['canvases'], 1):
            fn = os.path.join(SCANS, f"ov_{r['tag']}_{i}_{c['label'][-5:]}.jpg")
            if os.path.exists(fn):
                continue
            data = get(c['service'] + '/full/1000,/0/default.jpg')
            open(fn, 'wb').write(data)
            print('ok', fn)


def full(u, n):
    d = load()
    r = d[u]
    c = r['canvases'][n - 1]
    W, H = c['w'], c['h']
    TW, TH = 1500, 640
    im = Image.new('RGB', (W, H), 'white')
    for y in range(0, H, TH):
        for x in range(0, W, TW):
            w, h = min(TW, W - x), min(TH, H - y)
            data = get(f"{c['service']}/{x},{y},{w},{h}/full/0/default.jpg")
            im.paste(Image.open(io.BytesIO(data)).convert('RGB'), (x, y))
    fn = os.path.join(SCANS, f"full_{r['tag']}_{n}_{c['label'][-5:]}.jpg")
    im.save(fn, quality=92)
    print('ok', fn, W, H)


if __name__ == '__main__':
    a = sys.argv[1]
    if a == 'manifests':
        manifests()
    elif a == 'overview':
        overview()
    elif a == 'full':
        full(sys.argv[2], int(sys.argv[3]))
