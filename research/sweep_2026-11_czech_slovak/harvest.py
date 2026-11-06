"""Harvest an ARON instance for a list of terms; append hits to aron_hits.jsonl (dedup by id)."""
import json, os, sys, time
from aron import search
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'aron_hits.jsonl')
base = sys.argv[1]
terms = sys.argv[2:]
seen = set()
if os.path.exists(OUT):
    for l in open(OUT, encoding='utf-8'):
        d = json.loads(l); seen.add((d['base'], d['id']))
with open(OUT, 'a', encoding='utf-8') as fh:
    for t in terms:
        off, n_new, total = 0, 0, None
        while True:
            try:
                j = search(base, t, 100, off)
            except Exception as e:
                print('ERR', t, e); break
            total = j['count']
            for i in j['items']:
                if (base, i['id']) in seen:
                    continue
                seen.add((base, i['id'])); n_new += 1
                fh.write(json.dumps({'base': base, 'term': t, 'id': i['id'], 'name': i.get('name'),
                                     'description': i.get('description')}, ensure_ascii=False) + '\n')
            off += 100
            if off >= total or off >= 1000:
                break
            time.sleep(0.5)
        print(f'{t}: {total} hits, {n_new} new')
        time.sleep(0.5)
