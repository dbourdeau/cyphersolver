"""Turcica + Polonica digitised volumes, with image-series id and count -> units.json.
Starts from sweep D's rik_vols.json; fills the ids the jsonld no longer gives from the APE EAD."""
import json
import sys
import time

from rik_common import count, dao

sys.stdout.reconfigure(encoding='utf-8')
v = json.load(open('../sweep_2026-11_D_east_north/rik_vols.json', encoding='utf-8'))
try:
    done = {u['ref']: u for u in json.load(open('units.json', encoding='utf-8'))}
except FileNotFoundError:
    done = {}
for x in v:
    if x['series'] not in ('Diplomatica Turcica', 'Diplomatica Polonica') or x['ref'] in done:
        continue
    u = dict(ref=x['ref'], id=x['id'], series=x['series'], date=x.get('date'), caption=x.get('caption'), note=x.get('note'),
             man=x.get('man'), n=x.get('n'))
    try:
        if not u['man']:
            u['man'] = dao(x['ref'])
            time.sleep(1.2)
        if u['man'] and not u['n']:
            u['n'] = count(u['man'])
            time.sleep(1.2)
    except Exception as e:
        u['err'] = str(e)[:80]
    done[x['ref']] = u
    print(u['ref'].replace('SE/RA/', ''), u['man'], u['n'], flush=True)
json.dump(list(done.values()), open('units.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
