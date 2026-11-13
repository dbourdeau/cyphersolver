"""Fetch CEHM-Carso viewer images for DCXXI records (one request at a time, 1.6 s apart)."""
import sys, time, urllib.request, urllib.error, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'scans')
UA = {'User-Agent': 'WAINUT-research'}
def get(url):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.headers.get('Content-Type'), r.read()
    except urllib.error.HTTPError as e:
        return e.code, None, b''
for shelf in sys.argv[1:]:
    parts = shelf.split('.')  # DCXXI 3 231 1
    path = '/'.join(parts)
    for n in range(1, 30):
        url = f'http://visor.cehm.org.mx/assets/docx/fondos/jzd/{path}/{shelf}.{n:04d}.jpg'
        st, ct, data = get(url)
        time.sleep(1.6)
        if st != 200 or not ct or 'image' not in ct:
            print(shelf, n, 'stop', st, ct); break
        fn = os.path.join(OUT, f'{shelf}.{n:04d}.jpg')
        open(fn, 'wb').write(data)
        print(shelf, n, len(data))
        if st in (403, 429): sys.exit('blocked')
