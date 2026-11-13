"""Rigsarkivet arkivalier search (13 Nov 2026): python3 rasearch.py <query> [online] -> prints title/dates/desc, saves jsonl"""
import json, sys, time, urllib.request
URL = 'https://soeg.rigsarkivet.dk/api/v1/Search/arkivalier'
def post(b):
    for a in range(8):
        try:
            r = urllib.request.Request(URL, data=json.dumps(b).encode(), headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) Chrome/126.0 Safari/537.36'})
            return json.load(urllib.request.urlopen(r, timeout=120))
        except Exception as e:
            time.sleep(5 + 3 * a)
    raise SystemExit('gave up')
def search(q, online=True, page=0, n=100, **kw):
    b = {'searchQuery': q, 'pageNumber': page, 'resultsPerPage': n, 'exactMatch': False}
    if online: b['accessibility'] = ['online']
    b.update(kw); return post(b)
if __name__ == '__main__':
    q = sys.argv[1]; online = len(sys.argv) > 2
    d = search(q, online); print(q, d.get('totalCount'))
    for r in d.get('searchResults', []):
        print(r['daisyId'], r['documentType'], '|', r['titel'][:90], '|', (r.get('dateFrom') or '')[:4], (r.get('dateTo') or '')[:4], '|', (r.get('beskrivelse') or '')[:200].replace('\n', ' '))
