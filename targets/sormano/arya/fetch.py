"""Fetch openings of BnF fr. 3096 (ark btv1b9060015d) from the Gallica IIIF service.

Each canvas is one microfilm frame of a double-page opening (about 9120 x 6250 px).
usage: python3 fetch.py FIRST LAST [size]   size = 'full' or a pixel width
"""
import sys, os, time, urllib.request
ARK = 'btv1b9060015d'
H = {'User-Agent': 'Mozilla/5.0'}
a, b = int(sys.argv[1]), int(sys.argv[2])
size = sys.argv[3] if len(sys.argv) > 3 else 'full'
os.makedirs('img', exist_ok=True)
for n in range(a, b + 1):
    out = f'img/f{n:04d}_{size}.jpg'
    if os.path.exists(out) and os.path.getsize(out) > 20000:
        continue
    sz = 'full' if size == 'full' else f'{size},'
    url = f'https://gallica.bnf.fr/iiif/ark:/12148/{ARK}/f{n}/full/{sz}/0/native.jpg'
    for att in range(4):
        try:
            d = urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=120).read()
            open(out, 'wb').write(d)
            print(out, len(d))
            break
        except Exception as e:
            print('retry', n, e)
            time.sleep(3 * (att + 1))
    time.sleep(0.4)
print('done')
