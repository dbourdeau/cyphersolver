"""Landesarchiv NRW sufservice API harvest. usage: nrw_harvest.py OUT.jsonl term..."""
import sys, json, time, urllib.parse, requests
S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0'
out = open(sys.argv[1], 'a', encoding='utf-8')
for term in sys.argv[2:]:
    page = 0; n = 0; hits = None
    while True:
        u = 'https://www.archive.nrw.de/sufservice/api/search?keyword=%s&size=50&page=%d' % (urllib.parse.quote(term), page)
        r = S.get(u, timeout=60)
        if r.status_code != 200: print('STOP', r.status_code, term, page); break
        d = r.json(); hits = d['hits']
        for x in d['searchResult']:
            x['term'] = term; out.write(json.dumps(x, ensure_ascii=False) + '\n'); n += 1
        out.flush()
        page += 1
        if not d['searchResult'] or page >= d['pages']: break
        time.sleep(2.5)
    print(term, hits, 'got', n, flush=True); time.sleep(2.5)
