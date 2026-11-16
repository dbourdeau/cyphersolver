#!/usr/bin/env python3
"""LoC search JSON (slow: 30-45 s, sporadic 503; plain curl works). usage: loc.py OUT.jsonl "query" ...  prints count + titles (first 12)."""
import sys, json, subprocess, time, urllib.parse
out = sys.argv[1]
for q in sys.argv[2:]:
    url = 'https://www.loc.gov/search/?fo=json&c=12&q=' + urllib.parse.quote_plus(q)
    for attempt in range(2):
        r = subprocess.run(['curl', '-s', '-m', '90', '-A', 'Mozilla/5.0 (research sweep)', url], capture_output=True)
        try: d = json.loads(r.stdout); break
        except Exception: d = None; time.sleep(8)
    if not d: print('ERR', q); continue
    print('%6s  %s' % (d.get('pagination', {}).get('total'), q), flush=True)
    with open(out, 'a') as f:
        for it in d.get('results', []):
            f.write(json.dumps({'q': q, 'title': it.get('title'), 'date': it.get('date'), 'url': it.get('id') or it.get('url'),
                                'desc': (it.get('description') or [''])[0][:300] if isinstance(it.get('description'), list) else str(it.get('description'))[:300],
                                'format': it.get('original_format')}, ensure_ascii=False) + '\n')
    time.sleep(5)
