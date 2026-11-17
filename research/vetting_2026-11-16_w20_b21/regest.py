"""Fetch Hungaricana Viennese-inventory regests by id and print reference code, date and full description.
Usage: python -I -X utf8 regest.py <id> [<id> ...]   (or a range a-b). Appends to raw/regests.jsonl. 1 req / 1.2 s."""
import json, re, sys, time, html, urllib.request

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'


def get(i):
    req = urllib.request.Request(f'https://archives.hungaricana.hu/en/lear/BecsSeg/{i}/', headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        t = r.read().decode('utf8', 'replace')
    t = html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'(?s)<script.*?</script>|<style.*?</style>', '', t)))
    t = ' '.join(t.split())
    k = t.find('Reference code')
    seg = t[k:t.find('Links Print metadata', k)] if k >= 0 else ''
    f = lambda a, b: (re.search(re.escape(a) + r'\s*(.*?)\s*(?:' + b + r'|$)', seg) or [None, ''])[1]
    return {'id': i, 'ref': f('Reference code', 'Database'), 'date': f('Date of Creation', 'Description|Links'),
            'desc': f('Description', 'Links|$')}


ids = []
for a in sys.argv[1:]:
    if '-' in a:
        x, y = map(int, a.split('-')); ids += list(range(x, y + 1))
    else:
        ids.append(int(a))
with open('raw/regests.jsonl', 'a', encoding='utf8') as out:
    for i in ids:
        try:
            r = get(i)
        except Exception as e:
            r = {'id': i, 'error': str(e)}
        out.write(json.dumps(r, ensure_ascii=False) + '\n')
        print(f"{i} | {r.get('ref','')[17:]} | {r.get('date','')} | {r.get('desc', r.get('error'))}", flush=True)
        time.sleep(1.2)
