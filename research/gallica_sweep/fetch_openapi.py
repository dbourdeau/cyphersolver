# Fetch every canvas of a Gallica volume through openapi.bnf.fr (gallica.bnf.fr/iiif 403s scripts since Oct 2026).
#   python fetch_openapi.py <ark> <n_canvases> [width]
import sys, os, time, urllib.request
ark = sys.argv[1]; n = int(sys.argv[2]); W = int(sys.argv[3]) if len(sys.argv) > 3 else 800
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) cyphersolver research', 'Accept': 'image/jpeg'}
out = f'{ark}_w{W}'; os.makedirs(out, exist_ok=True)
for i in range(1, n + 1):
    fn = f'{out}/c{i:03d}.jpg'
    if os.path.exists(fn) and os.path.getsize(fn) > 5000:
        continue
    url = f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ark}/f{i}/full/{W},/0/default.jpg'
    for t in range(6):
        try:
            d = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()
            open(fn, 'wb').write(d); print(i, len(d), flush=True); break
        except Exception as e:
            print(i, 'fail', str(e)[:80], flush=True); time.sleep(10 * (t + 1))
    time.sleep(0.3)
print('DONE', flush=True)
