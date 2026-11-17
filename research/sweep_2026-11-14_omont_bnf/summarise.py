"""Third stage: per-volume summary of explicit 'avec chiffre' / 'en chiffre' items without a decipherment.
usage: python summarise.py items2.json summary.json"""
import json, re, sys, collections
rows = json.load(open(sys.argv[1], encoding='utf8'))
exp = re.compile(r'(?:avec\s+c[hli]{1,3}if?fres?\b|en\s+c[hli]{1,3}if?fres?\b|chiffr[ée]e?s?\b|c[hl]i{1,3}ffre\s*[,.]\s*\()', re.I)
dec = re.compile(r'avec\s+\S{3,10}\s*,?\s+et\s+d[eé]|d[eé]\s?c[hl]\w{0,4}[fl]|dechi|interlin|traduction|explication|clef|clé', re.I)
bad = re.compile(r'chiffre\s+de\s+(?:Louis|Napol|Charles X)|aux?\s+armes|reliure|rel\.\s', re.I)
out = {}
for r in rows:
    if not r['fr']: continue
    key = (r['vol'][:12], r['fr'])
    for it in r['items']:
        t = it['text']
        if not exp.search(t) or bad.search(t): continue
        m = re.match(r'(\d{1,3})\.\s+(.*)', t)
        yrs = [int(y) for y in re.findall(r'\b(1[3-9]\d\d)\b', t)]
        fol = re.search(r'\(?Fol\.?\s*([\d\- ,et]+)', t)
        d = out.setdefault(key, {'fr': r['fr'], 'vol': r['vol'], 'title': r['title'][:300], 'items': []})
        d['items'].append({'n': m.group(1) if m else None, 'dec': bool(dec.search(t)), 'years': yrs, 'fol': fol.group(1).strip() if fol else None, 'text': t[:300]})
res = sorted(out.values(), key=lambda d: d['fr'])
json.dump(res, open(sys.argv[2], 'w', encoding='utf8'), ensure_ascii=False, indent=1)
for d in res:
    nd = [i for i in d['items'] if not i['dec']]
    ys = sorted(y for i in nd for y in i['years'])
    print(d['fr'], d['vol'][-8:-5], len(d['items']), len(nd), (ys[0], ys[-1]) if ys else '', re.sub(r'^\d+\.\s*', '', d['title'])[:60])
