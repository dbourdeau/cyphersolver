"""NA re-run with new spelling variants; writes na_new2.jsonl (hits not in nationaal_archief/hits.jsonl)."""
import sys, json, time
sys.path.insert(0, '../nationaal_archief')
import harvest as h
old = {(json.loads(l)['ead'], json.loads(l)['title_id']) for l in open('na_new.jsonl', encoding='utf8')} | {(json.loads(l)['ead'], json.loads(l)['title_id']) for l in open('../nationaal_archief/hits.jsonl', encoding='utf8')}
TERMS = ['codeboek','codeboeken','gecodeerd','geheime tekens','geheimtekens','cifferschrift','cijfertekens','cijferalfabet','dechiffre','deciffer','decijfer','ontcijfer','geheimschrift','cijferschrift','nomenclator','sleutels geheimschrift','schrijven in cijfer','in cijfer','met cijfer','stenografie','steganografie','cryptograf','cryptografie','zifra','cifra','secrete correspondentie','chiffre']
seen = {}
for t in TERMS:
    for a in h.archives(t):
        if a.get('type') != 'ARCHIVE' or h.start_year(a.get('period')) > 1900: continue
        for it in h.items(a['id'], t):
            if it.get('type') != 'CLEVEL': continue
            k = (a['id'], it['title_id'])
            if k in old: continue
            r = seen.setdefault(k, {'ead': a['id'], 'archive': a['title'], 'period': a.get('period'), 'title_id': it['title_id'], 'title': h.html.unescape(h.re.sub('<[^>]+>', '', it['title'])), 'terms': []})
            r['terms'].append(t)
        time.sleep(0.3)
    print(t, len(seen), file=sys.stderr, flush=True)
with open('na_new2.jsonl', 'w', encoding='utf8') as f:
    for r in seen.values(): f.write(json.dumps(r, ensure_ascii=False) + '\n')
