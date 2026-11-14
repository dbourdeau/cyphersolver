"""Dump every clevel (item) of one Nationaal Archief inventory: python dump_ead.py 1.01.02 -> ead_1.01.02.jsonl

Uses GET https://zvt.nationaalarchief.nl/api/eads/<ead>/clevels?page=N (50 per page). Resumable: pages already
written are skipped.
"""
import json, os, sys, time, urllib.request

ead = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else f'ead_{ead}.jsonl'
done = set()
if os.path.exists(out):
    for l in open(out, encoding='utf8'):
        done.add(json.loads(l)['_page'])


def get(page):
    url = f'https://zvt.nationaalarchief.nl/api/eads/{ead}/clevels?page={page}'
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (cyphersolver research)'})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            print('retry', page, e, file=sys.stderr, flush=True)
            time.sleep(5 * (attempt + 1))
    return None


first = get(0)
last = first['last_page']
print('pages', last + 1, 'items', first['total'], flush=True)
with open(out, 'a', encoding='utf8') as f:
    for page in range(last + 1):
        if page in done:
            continue
        d = first if page == 0 else get(page)
        if not d:
            continue
        for c in d['data']:
            keep = {k: c.get(k) for k in ('id', 'title', 'unitid', 'path', 'availability', 'unitdate', 'physdesc', 'scopecontent')}
            keep['_page'] = page
            f.write(json.dumps(keep, ensure_ascii=False) + '\n')
        if page % 50 == 0:
            print(page, flush=True)
        time.sleep(0.25)
