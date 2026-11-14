#!/usr/bin/env python3
"""Europeana Search API harvester (public demo key api2demo). usage: europeana.py OUT.jsonl "query" ... [--rows N]
Prints totalResults per query, appends title/provider/year/guid/description to OUT. 2.5 s between requests."""
import sys, json, time, urllib.request, urllib.parse
a = sys.argv[1:]; rows = 50
if '--rows' in a:
    i = a.index('--rows'); rows = int(a[i+1]); del a[i:i+2]
out, qs = a[0], a[1:]
for q in qs:
    url = 'https://api.europeana.eu/record/v2/search.json?wskey=api2demo&rows=%d&profile=standard&query=%s' % (rows, urllib.parse.quote(q))
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research sweep)'}), timeout=40))
    except Exception as e:
        print('ERR', q, e)
        if '429' in str(e) or '403' in str(e): sys.exit(1)
        time.sleep(5); continue
    print('%6d  %s' % (d.get('totalResults', 0), q))
    with open(out, 'a') as f:
        for it in d.get('items', []):
            f.write(json.dumps({'q': q, 'title': it.get('title'), 'prov': it.get('dataProvider'), 'country': it.get('country'),
              'year': it.get('year'), 'guid': it.get('guid'), 'id': it.get('id'),
              'desc': (it.get('dcDescription') or [''])[0][:400], 'type': it.get('type'), 'img': it.get('edmIsShownBy')}, ensure_ascii=False) + '\n')
    time.sleep(2.5)
