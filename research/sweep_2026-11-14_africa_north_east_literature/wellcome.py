#!/usr/bin/env python3
"""Wellcome Collection catalogue API (no key, plain GET). usage: wellcome.py "query" ... ; prints total + first 10 titles/ids."""
import sys, json, time, urllib.parse, urllib.request
for q in sys.argv[1:]:
    u = 'https://api.wellcomecollection.org/catalogue/v2/works?pageSize=10&query=' + urllib.parse.quote(q)
    try: d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (research sweep)'}), timeout=40))
    except Exception as e: print('ERR', q, e); continue
    print('%5d  %s' % (d['totalResults'], q))
    for r in d['results'][:10]:
        print('        ', r['id'], (r.get('referenceNumber') or ''), '|', r['title'][:90], '|', (r.get('production') or [{}])[0].get('dates', [{}])[0].get('label', '') if r.get('production') else '')
    time.sleep(2.5)
