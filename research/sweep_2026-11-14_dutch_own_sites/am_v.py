import am_search as a, json
d=a.q('Vogelesangh ontcijfering correspondentie','File',per=20)
print(d['total'])
for r in d['rows']: print(r['title'][:200],'|',r['data'].get('date'),'|',bool(r.get('media')), r['data']['parents'][-1]['title'][:70])
d=a.q('"Pieter Vogelesangh" brieven','File',per=40)
print(d['total'])
for r in d['rows']:
    if r['data']['parents'] and '292' in r['data']['parents'][0]['title']: print(r['title'][:220],'|',r['data'].get('date'),'|',bool(r.get('media')))
