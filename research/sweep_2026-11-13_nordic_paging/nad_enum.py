"""Enumerate digitised units of selected Riksarkivet fonds via the NAD API -> enum.json (13 Nov 2026)"""
import json, sys, time, requests
H = {'User-Agent': 'curl/8.0'}
SERIES = sys.argv[1:]
out = {}
for ser in SERIES:
    off = 0
    while True:
        d = requests.get('https://data.riksarkivet.se/api/records', headers=H, timeout=90, params={'text': '*', 'only_digitised_materials': 'true', 'max': 100, 'offset': off, 'facet': 'PartOfArchive:' + ser}).json()
        for it in d.get('items', []):
            m = it.get('metadata', {})
            out[it['id']] = dict(id=it['id'], ref=m.get('referenceCode'), caption=it.get('caption'), date=m.get('date'), note=m.get('note'), series=ser, type=it.get('type'),
                                 path=' / '.join(h['caption'].replace('\n', ' ') for h in m.get('hierarchy', [])))
        tot = d.get('totalHits', 0); off += 100; time.sleep(1.5)
        if off >= tot or off > 2000: break
    print(ser, tot, len(out), flush=True)
json.dump(list(out.values()), open(sys.argv[0].replace('nad_enum.py','') + 'enum_%s.json' % ('x'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
