"""For each 'clean' date of cluster.py (every sifrír regest of that date says no decipherment), search Hungaricana for the
date string and fetch every Türkei I regest of that date, to find clear copies, extracts or decipherments filed apart.
Writes raw/datecheck.jsonl (one line per date with the regests found). Polite: about 1 request per 1.2 s."""
import json, re, sys, time, base64, urllib.request, html
sys.argv = [sys.argv[0]]
import importlib.util
spec = importlib.util.spec_from_file_location('cl', 'cluster.py')
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    cl = importlib.util.module_from_spec(spec); spec.loader.exec_module(cl)
spec2 = importlib.util.spec_from_file_location('hs', 'hsearch.py')
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode('utf8', 'replace')


def search_ids(q):
    lst = base64.b64encode(json.dumps({'query': q}).encode()).decode().rstrip('=')
    t = get(f'https://archives.hungaricana.hu/en/lear/search/results/?list={lst}&per_page=100&page=1')
    out = []
    for blk in t.split('list-group-item bg-light mb-2 result')[1:]:
        m = re.search(r'lear/BecsSeg/(\d+)/[^>]*>\s*(.*?)\s*</a>', blk, re.S)
        if m and 'Türkei I.' in m.group(2):
            out.append(int(m.group(1)))
    return out


def regest(i):
    t = get(f'https://archives.hungaricana.hu/en/lear/BecsSeg/{i}/')
    t = ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'(?s)<script.*?</script>|<style.*?</style>', '', t))).split())
    k = t.find('Reference code'); seg = t[k:t.find('Links Print metadata', k)]
    f = lambda a, b: (re.search(re.escape(a) + r'\s*(.*?)\s*(?:' + b + r'|$)', seg) or [None, ''])[1]
    return {'id': i, 'ref': f('Reference code', 'Database'), 'date': f('Date of Creation', 'Description|Links'), 'desc': f('Description', '$')}


cache = {}
try:
    for l in open('raw/regests.jsonl', encoding='utf8'):
        r = json.loads(l)
        if 'error' not in r: cache[r['id']] = r
except FileNotFoundError:
    pass
leads = [int(a) for a in sys.argv[1:]] or list(cl.out)
done = set()
try:
    for l in open('raw/datecheck.jsonl', encoding='utf8'):
        done.add((json.loads(l)['lead'], json.loads(l)['date']))
except FileNotFoundError:
    pass
with open('raw/datecheck.jsonl', 'a', encoding='utf8') as out, open('raw/regests.jsonl', 'a', encoding='utf8') as rc:
    for lead in leads:
        for d, hs in cl.out[lead]:
            if (lead, d) in done: continue
            ids = search_ids(f'"{d}"'); time.sleep(1.2)
            ids = sorted(set(ids) | {h['id'] for h in hs})
            rows = []
            for i in ids:
                if i not in cache:
                    try:
                        cache[i] = regest(i); rc.write(json.dumps(cache[i], ensure_ascii=False) + '\n'); rc.flush()
                    except Exception as e:
                        cache[i] = {'id': i, 'error': str(e)}
                    time.sleep(1.2)
                rows.append(cache[i])
            out.write(json.dumps({'lead': lead, 'date': d, 'cipher_ids': [h['id'] for h in hs], 'rows': rows}, ensure_ascii=False) + '\n'); out.flush()
            print(lead, d, len(rows), flush=True)
