"""Fetch TNA Discovery API details for record ids; print key fields; save raw JSON."""
import sys, json, time, urllib.request, os
for rid in sys.argv[1:]:
    p = os.path.join('raw', rid + '.json')
    if not os.path.exists(p):
        req = urllib.request.Request('https://discovery.nationalarchives.gov.uk/API/records/v1/details/' + rid,
                                     headers={'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'})
        open(p, 'wb').write(urllib.request.urlopen(req, timeout=60).read()); time.sleep(1)
    d = json.load(open(p, encoding='utf8'))
    print('==', rid, d.get('citableReference'), '|', d.get('coveringDates'), '| digitised', d.get('digitised'))
    print('  ', (d.get('scopeContent') or {}).get('description'))
    for k in ('note', 'physicalDescriptionExtent', 'parentId', 'arrangement'):
        if d.get(k): print('  ', k, ':', d.get(k))
