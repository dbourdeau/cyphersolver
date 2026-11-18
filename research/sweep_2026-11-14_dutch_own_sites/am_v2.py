import am_search as a, json
d=a.q('Vogelesangh ontcijfering correspondentie','File',per=5)
print(json.dumps(d['rows'][0],ensure_ascii=False)[:2500])
d=a.q('Vogelesangh','File',per=100)
print(d['total'])
for r in d['rows']:
    if '292' in (r['data']['parents'][0]['title'] if r['data']['parents'] else ''): print(r['title'][:200],'|',r['data'].get('date'),'|',bool(r.get('media')))
