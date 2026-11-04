"""Fetch MDZ IIIF page images, one request at a time, ~1 s apart, User-Agent WAINUT-research.
usage: fetch.py BSBID SIZE PAGE [PAGE ...]    SIZE e.g. 800 (width) or full.  Writes ../scans/<bsb>_p<NNN>_<size>.jpg
Stops on any HTTP error (429 included)."""
import sys, time, urllib.request, os
bsb, size = sys.argv[1], sys.argv[2]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scans')
for p in sys.argv[3:]:
    p = int(p); sz = 'full' if size == 'full' else size + ','
    fn = os.path.join(out, f'{bsb}_p{p:03d}_{size}.jpg')
    if os.path.exists(fn): continue
    url = f'https://api.digitale-sammlungen.de/iiif/image/v2/{bsb}_{p:05d}/full/{sz}/0/default.jpg'
    req = urllib.request.Request(url, headers={'User-Agent': 'WAINUT-research'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: data = r.read()
    except Exception as e:
        print('ERR', p, e); sys.exit(1)
    open(fn, 'wb').write(data); print(p, len(data)); time.sleep(1.0)
