"""archive.org full-text search helper (page-level hits). Usage: python fts.py "query" [n] [pages]
Appends raw hits to raw_hits.jsonl (query, identifier, title, year, page, snippet)."""
import sys, json, time, urllib.parse, urllib.request, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'raw_hits.jsonl')
def fts(q, n=50, page=1):
    u = ("https://archive.org/services/search/beta/page_production/?service_backend=fts&hits_per_page=%d&page=%d&user_query=%s"
         % (n, page, urllib.parse.quote(q)))
    for attempt in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60)
            return json.load(r)
        except Exception as e:
            err = e; time.sleep(3)
    print('ERR', err); return None
def run(q, n=50, pages=1, show=True, maxshow=30):
    rows = []
    for p in range(1, pages + 1):
        d = fts(q, n, p)
        if not d: break
        hs = d["response"]["body"]["hits"]
        hits = hs["hits"]
        if p == 1 and show: print('QUERY', q, 'total', hs.get('total'))
        for h in hits:
            f = h["fields"]
            hl = h.get("highlight") or {}
            sn = ' | '.join(hl.get("text", [])[:2]) if isinstance(hl, dict) else ''
            rows.append({'q': q, 'id': f.get('identifier'), 'title': f.get('title'), 'year': f.get('year') or f.get('date'),
                         'page': f.get('page_num') or f.get('page'), 'snip': sn})
        if len(hits) < n: break
        time.sleep(1.5)
    with open(OUT, 'a', encoding='utf8') as fh:
        for r in rows: fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    if show:
        for r in rows[:maxshow]:
            print(' ', r['id'], '|', (r['title'] or '')[:60], '|', r['year'], '| p', r['page'])
            print('     ', r['snip'][:300].replace('\n', ' '))
    return rows
if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    run(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 20, int(sys.argv[3]) if len(sys.argv) > 3 else 1)
