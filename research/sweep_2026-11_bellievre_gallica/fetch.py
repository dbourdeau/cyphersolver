# python fetch.py <ark> <outdir> [width] [start] [end]  -- openapi.bnf.fr IIIF, one request ~0.7s
import sys, os, time, urllib.request
ark, out = sys.argv[1], sys.argv[2]
W = int(sys.argv[3]) if len(sys.argv) > 3 else 500
a = int(sys.argv[4]) if len(sys.argv) > 4 else 1
b = int(sys.argv[5]) if len(sys.argv) > 5 else 9999
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) cyphersolver research', 'Accept': 'image/jpeg'}
os.makedirs(out, exist_ok=True)
for i in range(a, b + 1):
    fn = f'{out}/c{i:03d}.jpg'
    if os.path.exists(fn) and os.path.getsize(fn) > 3000: continue
    url = f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ark}/f{i}/full/{W},/0/default.jpg'
    for t in range(4):
        try:
            d = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
            open(fn, 'wb').write(d); break
        except Exception as e:
            if '404' in str(e): print('END', i); sys.exit()
            if '429' in str(e) or '403' in str(e): print('BLOCK', i, e); sys.exit()
            time.sleep(8 * (t + 1))
    time.sleep(0.7)
print('DONE')
