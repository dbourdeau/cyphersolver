"""Enumerate digitised Volumes in the western Diplomatica series and the Stedingk fonds through the NAD API
(data.riksarkivet.se/api/records, text=* with facet PartOfArchive) -> enum.json. ~1 request / 1.3 s."""
import json
import sys
import time

import requests

sys.stdout.reconfigure(encoding='utf-8')
H = {'User-Agent': 'curl/8.0'}
SERIES = ['Diplomatica Muscovitica', 'Diplomatica Gallica', 'Diplomatica Italica', 'Diplomatica Hollandica',
          'Diplomatica Anglica', 'Diplomatica Danica', 'Diplomatica Germanica', 'Diplomatica Americana',
          'Diplomatica Hispanica', 'Diplomatica Lusitanica', 'Diplomatica Maroccana', 'Diplomatica Cosacica',
          'Diplomatica Helvetica', 'Diplomatica Curlandica', 'Diplomatica Livonica', 'Diplomatica Brandenburgica',
          'Diplomatica Saxonica', 'Diplomatica Bavarica', 'Diplomatica Hamburgensia', 'Diplomatica Lubecensia',
          'Diplomatica Hanseatica', 'Diplomatica Ragusina', 'Diplomatica Persica', 'Diplomatica Hispanica et Lusitanica',
          'Diplomatica Svecica', 'Diplomatica. Kartor och ritningar', 'Stedingkska arkivet']
out = {}
for ser in SERIES:
    off = 0
    while True:
        try:
            r = requests.get('https://data.riksarkivet.se/api/records', headers=H, timeout=90,
                             params={'text': '*', 'only_digitised_materials': 'true', 'max': 100, 'offset': off,
                                     'facet': 'PartOfArchive:' + ser})
            d = r.json()
        except Exception as e:
            print('ERR', ser, off, e)
            break
        for it in d.get('items', []):
            if it.get('type') not in ('Volume', 'Dossier', 'Document'):
                continue
            m = it.get('metadata', {})
            out[it['id']] = dict(id=it['id'], ref=m.get('referenceCode'), caption=it.get('caption'), date=m.get('date'),
                                 note=m.get('note'), series=ser, type=it.get('type'),
                                 path=' / '.join(h['caption'].replace('\n', ' ') for h in m.get('hierarchy', [])))
        tot = d.get('totalHits', 0)
        off += 100
        time.sleep(1.3)
        if off >= tot:
            break
    print(ser, tot, len(out), flush=True)
json.dump(list(out.values()), open('enum.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
