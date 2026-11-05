import json, os, re, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, '_dl', 'manus_all.json'), encoding='utf8'))
cache_p = os.path.join(HERE, '_dl', 'manus_detail.json')
cache = json.load(open(cache_p, encoding='utf8')) if os.path.exists(cache_p) else {}
cities = sys.argv[1].split('|')
def strings(o, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ('href', 'icon', 'linkType', 'type', 'id', 'status', 'hasMore'): continue
            strings(v, acc)
    elif isinstance(o, list):
        for v in o: strings(v, acc)
    elif isinstance(o, str): acc.append(o)
n = 0
for k, v in d.items():
    c = re.split(r'[,(]', v['title'])[0].strip()
    if c not in cities or k in cache: continue
    u = f'https://manus.iccu.sbn.it/o/manus-api/title?id={k}'
    for a in range(3):
        try:
            time.sleep(1.2)
            j = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'X-Requested-With': 'XMLHttpRequest'}), timeout=60).read().decode('utf8', 'replace'), strict=False)
            acc = []; strings(j.get('data', {}), acc)
            cache[k] = ' || '.join(acc); break
        except Exception as e:
            time.sleep(6)
    n += 1
    if n % 20 == 0: json.dump(cache, open(cache_p, 'w', encoding='utf8'), ensure_ascii=False); print(n, flush=True)
json.dump(cache, open(cache_p, 'w', encoding='utf8'), ensure_ascii=False)
print('done', len(cache))
