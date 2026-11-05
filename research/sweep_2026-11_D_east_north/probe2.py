import requests, sys, json
sys.stdout.reconfigure(encoding='utf-8')
H = {'User-Agent':'Mozilla/5.0 (cyphersolver research sweep; polite)', 'Accept':'application/json'}
tests = [
 'http://libris.kb.se/xsearch?query=chiffer&format=json&n=5',
 'https://libris.kb.se/xsearch?query=chiffer&format=json&n=5',
 'https://libris.kb.se/find.jsonld?q=chiffer&_limit=3',
 'https://api.nb.no/catalog/v1/items?q=chiffer&searchType=FULL_TEXT_SEARCH&size=3',
 'https://api.nb.no/catalog/v1/items?q=chiffer&size=3',
 'https://ais.ra.ee/',
 'https://www.nb.no/search?q=chiffer',
]
for u in tests:
    try:
        r = requests.get(u, headers=H, timeout=25)
        print(r.status_code, len(r.content), u)
        print(r.text[:400].replace('\n',' '))
    except Exception as e:
        print('ERR', u, type(e).__name__, str(e)[:100])
