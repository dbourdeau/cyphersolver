"""python man.py <tag> <ark> : fetch the IIIF manifest of a digitised HIL unit -> raw/man_<tag>.json; print frame count."""
import json, os, sys, time, urllib.request
here = os.path.dirname(os.path.abspath(__file__))
tag, ark = sys.argv[1], sys.argv[2]
fn = os.path.join(here, 'raw', 'man_%s.json' % tag)
if not os.path.exists(fn):
    for cand in [ark[0:2] + '/' + ark[2:4] + '/' + ark[4:6], ark[1:3] + '/' + ark[3:5] + '/' + ark[5:7]]:
        u = 'https://iiif.durham.ac.uk/manifests/trifle/32150/%s/%s/manifest' % (cand, ark)
        try:
            d = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read()
            open(fn, 'wb').write(d); print(u); break
        except Exception as e:
            print('fail', u, e); time.sleep(1)
m = json.load(open(fn, encoding='utf8'))
cs = m['sequences'][0]['canvases']
print(tag, ark, len(cs), 'frames;', cs[0]['label'], '...', cs[-1]['label'], '; size', cs[0]['width'], cs[0]['height'])
