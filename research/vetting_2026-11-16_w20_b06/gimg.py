"""Fetch Gallica views via openapi.bnf.fr IIIF. python -I -X utf8 gimg.py <ark> <view> [view ...] [--w 1200]
Also: gimg.py <ark> --labels  (prints canvas labels from the manifest)"""
import sys, os, time, json, urllib.request
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
os.makedirs(D, exist_ok=True)
a = sys.argv[1:]
ark = a.pop(0)
w = '1200'
if '--w' in a:
    i = a.index('--w'); w = a[i + 1]; del a[i:i + 2]
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90).read()
if a and a[0] == '--labels':
    m = json.loads(get(f'https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/{ark}/manifest.json'))
    items = m.get('items', [])
    print(len(items), 'canvases')
    for i, c in enumerate(items, 1):
        lab = c.get('label', {})
        lab = list(lab.values())[0][0] if isinstance(lab, dict) and lab else lab
        print(i, lab, end=' | ')
    print()
    sys.exit()
for v in a:
    p = os.path.join(D, f'{ark}_f{v}_{w}.jpg')
    if not os.path.exists(p):
        try:
            open(p, 'wb').write(get(f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ark}/f{v}/full/{w},/0/default.jpg'))
        except Exception as e:
            print(v, 'ERR', e); continue
        time.sleep(1)
    print(p)
