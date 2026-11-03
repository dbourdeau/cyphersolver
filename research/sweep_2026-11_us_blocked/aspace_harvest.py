"""Harvest an ArchivesSpace public interface: phrase searches, then KWIC from each record page.
python aspace_harvest.py <base url> <out.json>   (polite: 1.5 s spacing)"""
import json, re, sys, time, urllib.parse, urllib.request
BASE, OUT = sys.argv[1].rstrip('/'), sys.argv[2]
TERMS = ['"in cipher"', '"in cypher"', 'cipher', 'cypher', 'ciphers', 'ciphered', 'cryptogram', 'cryptograms', 'decipher',
         'deciphered', 'undeciphered', 'decoded', 'enciphered', 'encrypted', '"in code"', '"secret code"',
         '"secret writing"', '"coded letter"', '"coded message"', '"code letter"', '"written in code"', '"cipher letter"']
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) Chrome/130'}
def get(u):
    time.sleep(1.5)
    try:
        return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read().decode('utf8', 'replace')
    except Exception as x:
        print('ERR', u, x, flush=True); return ''
rows = {}
for t in TERMS:
    page, last = 1, 1
    while page <= last and page <= 40:
        q = urllib.parse.urlencode({'utf8': '✓', 'op[]': '', 'q[]': t, 'limit': '', 'field[]': '', 'from_year[]': '', 'to_year[]': '', 'commit': 'Search', 'page': page})
        s = get(f'{BASE}/repositories/search?{q}') or get(f'{BASE}/search?{q}')
        for m in re.finditer(r'<a class="record-title" href="([^"]+)"[^>]*>(.*?)</a>', s, re.S):
            r = rows.setdefault(m[1], {'h': m[1], 'title': re.sub(r'<[^>]+>|\s+', ' ', m[2]).strip(), 'terms': []})
            if t not in r['terms']: r['terms'].append(t)
        pages = [int(x) for x in re.findall(r'[?&;]page=(\d+)', s)]
        last = max(pages + [page])
        page += 1
    print(t, 'pages', last, 'rows', len(rows), flush=True)
    json.dump(rows, open(OUT, 'w', encoding='utf8'), ensure_ascii=False)
for r in rows.values():
    s = get(BASE + r['h'])
    txt = re.sub(r'\s+', ' ', re.sub(r'<script.*?</script>|<[^>]+>', ' ', s, flags=re.S))
    r['ctx'] = [txt[max(0, m.start()-200):m.end()+200] for m in re.finditer(r'(?i)cipher|cypher|cryptogr|\bin code\b|coded |decod|encrypt|secret (writing|code)', txt)][:4]
    b = re.findall(r'<a href="[^"]*">([^<]{3,120})</a>', s[:0])
    json.dump(rows, open(OUT, 'w', encoding='utf8'), ensure_ascii=False)
print('done', len(rows))
