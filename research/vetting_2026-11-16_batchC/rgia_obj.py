# Print an RGIA KAISA (fgurgia.ru) case record from its object API. python -I -X utf8 rgia_obj.py <objectId> [...]
# The object page is a JS shell; /ajax/obj/<id>/<searchIndex> returns the attributes as JSON (search index 286525 works).
import json, sys, time, urllib.request
for oid in sys.argv[1:]:
    url = f'https://fgurgia.ru/ajax/obj/{oid}/286525?children=false'
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
    print('==', oid, 'images', len(d.get('images') or []), 'files', len(d.get('files') or []))
    for a in d['attributes']:
        print('  ', a['name'], '|', a['text'].strip())
    time.sleep(1.2)
