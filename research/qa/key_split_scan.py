import json, re, sys, pathlib, csv
root = pathlib.Path(sys.argv[1])
PHR = re.compile(r"(different (key|cipher|system|code|nomenclator)|second (key|cipher|system|code)|another (key|cipher|system)|other (key|cipher)s?\b|two (keys|ciphers|systems|codes)|three (keys|ciphers)|separate (key|cipher)|not the same (key|cipher)|unrelated (key|cipher)|own key|its own key|a new key|second alphabet|different alphabet)", re.I)
KEYREF = re.compile(r"\bkeys?\s+(?:on\s+)?(?:DECODE\s+)?(R\d{2,5})|\b(R\d{2,5})\s+key|key record (R\d{2,5})", re.I)
rows = []
for d in sorted((root/'targets').iterdir()):
    pf = d/'profile.json'; nf = d/'NOTES.md'
    if not pf.exists(): continue
    try: p = json.load(open(pf, encoding='utf-8'))
    except Exception as e: print('BAD', d.name, e); continue
    notes = nf.read_text(encoding='utf-8', errors='replace') if nf.exists() else ''
    blob = json.dumps(p, ensure_ascii=False) + '\n' + notes
    docs = p.get('documents', [])
    o = p.get('outcome', {})
    parts = o.get('parts') or []
    credits = o.get('credits') or []
    lasry = [c for c in credits if c.get('who') == 'lasry']
    phrases = sorted(set(m.group(0).lower() for m in PHR.finditer(blob)))
    keys = set()
    for m in KEYREF.finditer(blob):
        keys.add(next(g for g in m.groups() if g))
    years = sorted(set(x.get('year') for x in docs if isinstance(x.get('year'), int)))
    countries = sorted(set(x.get('country','') for x in docs))
    score = 0
    score += 3 if len(parts) > 1 and len(set(x['method'] for x in parts)) > 1 else 0
    score += min(len(phrases), 4)
    score += 2 if len(keys) > 1 else 0
    score += 2 if len(countries) > 1 else 0
    score += 1 if years and years[-1]-years[0] > 5 else 0
    score += 1 if len(docs) > 3 else 0
    rows.append(dict(target=d.name, score=score, ndocs=len(docs), years=f"{years[0]}-{years[-1]}" if years else '', countries=';'.join(countries),
        parts=len(parts), part_methods=';'.join(sorted(set(x['method'] for x in parts))), keyrefs=';'.join(sorted(keys)),
        phrases=';'.join(phrases), lasry=';'.join(c.get('role','') for c in lasry), summary=p.get('system',{}).get('summary','')[:160]))
rows.sort(key=lambda r: -r['score'])
w = csv.DictWriter(open(sys.argv[2], 'w', newline='', encoding='utf-8'), fieldnames=list(rows[0]))
w.writeheader(); w.writerows(rows)
print(len(rows), 'profiles;', sum(r['score']>=4 for r in rows), 'score>=4;', sum(bool(r['lasry']) for r in rows), 'with lasry credit')
