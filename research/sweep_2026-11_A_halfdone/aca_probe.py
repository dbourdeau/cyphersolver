"""One-off PARES probes for ACA Cancilleria register 3225 and neighbours (uses sweep.fetch, same 20 s spacing).

    python aca_probe.py "texto" [facet]     e.g. python aca_probe.py "Registro 3225" "idFI=15"

Prints the banner and the first 25 rows (id, signatura, date, images, title). Raw page saved to PARES_RAW if set.
"""
import os, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sweep

sys.stdout.reconfigure(encoding='utf-8')
term = sys.argv[1]
facet = sys.argv[2] if len(sys.argv) > 2 else None
op = sweep.opener()
q = {'nm': '', 'texto': term}
if facet:
    q.update(urllib.parse.parse_qsl(facet))
url = f'{sweep.BASE}/find?' + urllib.parse.urlencode(q, encoding='latin-1')
h = sweep.fetch(op, url)
sweep.save_raw('probe_' + term, 'find', h)
print('banner', sweep.banner(h), 'error' if sweep.is_error(h) else '')
for r in sweep.parse(h):
    print(r['id'], '|', r['sig'], '|', r['date'], '|', 'IMG' if r['images'] else '-', '|', r['title'][:140])
