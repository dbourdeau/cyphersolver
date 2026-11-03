"""Fetch MDZ IIIF page images of Clm 10398 (bsb00116447), one at a time, ~1 s apart.
usage: fetch.py SIZE PAGE [PAGE ...]   SIZE e.g. 600, or full"""
import sys, time, urllib.request, os
BSB = os.environ.get("BSB","bsb00116447"); size = sys.argv[1]; out = os.path.join(os.path.dirname(__file__), '..', 'scans')
for p in sys.argv[2:]:
    p = int(p); sz = 'full' if size == 'full' else size + ','
    fn = os.path.join(out, (BSB[-2:] + '_' if BSB != 'bsb00116447' else '') + f'p{p:03d}_{size}.jpg')
    if os.path.exists(fn): continue
    url = f'https://api.digitale-sammlungen.de/iiif/image/v2/{BSB}_{p:05d}/full/{sz}/0/default.jpg'
    req = urllib.request.Request(url, headers={'User-Agent': 'WAINUT-research'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: data = r.read()
    except Exception as e:
        print('ERR', p, e); sys.exit(1)
    open(fn, 'wb').write(data); print(p, len(data)); time.sleep(1.0)
