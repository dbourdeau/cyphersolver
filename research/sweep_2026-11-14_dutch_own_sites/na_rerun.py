"""NA re-run with new spelling variants; writes na_new.jsonl (hits not in nationaal_archief/hits.jsonl)."""
import sys, json, time
sys.path.insert(0, '../nationaal_archief')
import harvest as h
old = {(json.loads(l)['ead'], json.loads(l)['title_id']) for l in open('../nationaal_archief/hits.jsonl', encoding='utf8')}
TERMS = ['cyffer', 'cyfer', 'cijffer', 'ciffer', 'cijfferschrift', 'cijfferen', 'gecijffert', 'gechiffreerd', 'gechifreerd',
 'gecijfert', 'in cijffer', 'in cyffer', 'ontcijffer', 'ontcijfferd', 'ontcyfferd', 'decypher', 'dechiffreren',
 'gedechiffreerd', 'geheymschrift', 'geheime schrijfwijze', 'geheimschriften', 'chiffreren', 'gechiffreerde',
 'sleutel cijfer', 'cijferbrief', 'cijferbrieven', 'cijfersleutel', 'zifferschrift', 'chifre', 'cypher', 'cipher',
 'cijferschriften', 'ontcijferingen', 'geheime sleutel', 'codeschrift', 'geheimtaal', 'sleutel van het cijfer',
 'in cijfers geschreven', 'met cijfers geschreven', 'cijferwoorden']
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
with open('na_new.jsonl', 'w', encoding='utf8') as f:
    for r in seen.values(): f.write(json.dumps(r, ensure_ascii=False) + '\n')
