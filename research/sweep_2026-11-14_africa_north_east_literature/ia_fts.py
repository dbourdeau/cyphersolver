#!/usr/bin/env python3
"""archive.org full-text search harvester (fts_main_v2 backend, plain curl-style requests).
usage: ia_fts.py OUT.jsonl "query" ["query" ...]   [--hits N] [--pages P]
Writes one json line per hit (identifier, title, year, query, snippets) and prints total hit counts.
One request per 2.5 s. Stops at first 429/403."""
import sys, json, time, urllib.request, urllib.parse
args = sys.argv[1:]
hits_n, pages = 25, 1
if '--hits' in args:
    i = args.index('--hits'); hits_n = int(args[i+1]); del args[i:i+2]
if '--pages' in args:
    i = args.index('--pages'); pages = int(args[i+1]); del args[i:i+2]
out, queries = args[0], args[1:]
UA = 'Mozilla/5.0 (research sweep; polite)'
for q in queries:
    for p in range(1, pages+1):
        url = ('https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query='
               + urllib.parse.quote(q) + f'&hits_per_page={hits_n}&page={p}&page_type=collection_details&page_target=texts')
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=40))
        except Exception as e:
            print('ERR', q, e); 
            if '429' in str(e) or '403' in str(e): sys.exit(1)
            break
        body = d['response']['body']['hits']
        if p == 1: print(f"{body['total']:>7}  {q}")
        with open(out, 'a') as f:
            for h in body['hits']:
                fl = h['fields']
                f.write(json.dumps({'q': q, 'id': fl.get('identifier'), 'file': fl.get('file_basename'), 'title': fl.get('title'),
                    'year': fl.get('year'), 'creator': fl.get('creator'), 'page': fl.get('page_num'),
                    'snip': h.get('highlight', {}).get('text', [])}, ensure_ascii=False) + '\n')
        time.sleep(2.5)
        if len(body['hits']) < hits_n: break
