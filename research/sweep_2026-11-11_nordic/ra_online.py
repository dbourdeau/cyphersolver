"""List Rigsarkivet series of a creator that are available online (scanned). usage: python3 ra_online.py "<arkivskaber>" <out.jsonl>"""
import sys, json, time, urllib.request
URL = 'https://soeg.rigsarkivet.dk/api/v1/Search/arkivalier'
def post(b):
    r = urllib.request.Request(URL, data=json.dumps(b).encode(), headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) Chrome/126.0 Safari/537.36'})
    return json.load(urllib.request.urlopen(r, timeout=120))
page = 0; n = 0
with open(sys.argv[2], 'w') as f:
    while True:
        d = post({'searchQuery': '', 'arkivskaber': sys.argv[1], 'accessibility': ['online'], 'pageNumber': page, 'resultsPerPage': 100, 'sortOptions': {'fieldName': 'Dato', 'ascending': True}, 'exactMatch': False})
        res = d.get('searchResults') or []
        for r in res: f.write(json.dumps(r, ensure_ascii=False) + '\n'); n += 1
        print(page, d.get('totalCount'), n, flush=True)
        page += 1
        if not res or n >= d.get('totalCount', 0): break
        time.sleep(1)
