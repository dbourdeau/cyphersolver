"""python dl.py <tag> [width] [first] [last] : download frames of raw/man_<tag>.json at <width> px (default 1024) -> img/<tag>/."""
import json, os, sys, time, urllib.request
here = os.path.dirname(os.path.abspath(__file__))
tag = sys.argv[1]; W = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
A = int(sys.argv[3]) if len(sys.argv) > 3 else 0; B = int(sys.argv[4]) if len(sys.argv) > 4 else 99999
m = json.load(open(os.path.join(here, 'raw', 'man_%s.json' % tag), encoding='utf8'))
out = os.path.join(here, 'img', tag); os.makedirs(out, exist_ok=True)
for i, c in enumerate(m["sequences"][0]["canvases"]):
    if not A <= i <= B: continue
    svc = c['images'][0]['resource']['service']['@id']
    fn = os.path.join(out, '%03d_%s.jpg' % (i, ''.join(ch for ch in c['label'].split('/')[-1] if ch.isalnum() or ch in '-_')))
    if os.path.exists(fn) and os.path.getsize(fn) > 5000: continue
    for attempt in range(4):
        try:
            d = urllib.request.urlopen(urllib.request.Request(svc + '/full/%d,/0/default.jpg' % W, headers={'User-Agent': 'Mozilla/5.0'}), timeout=120).read()
            open(fn, 'wb').write(d); break
        except Exception as e:
            print('ERR', fn, e, flush=True); time.sleep(10 * (attempt + 1))
    time.sleep(1.0)
print('done', tag, flush=True)
