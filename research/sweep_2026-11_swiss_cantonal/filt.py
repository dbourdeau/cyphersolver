import json,re,sys
seen={}
for l in open('sc_a.jsonl',encoding='utf8'):
    r=json.loads(l)
    if r['id'] in seen: seen[r['id']]['terms'].append(r['term']); continue
    r['terms']=[r['term']]; seen[r['id']]=r
pat=re.compile(r'Brief|Korrespondenz|Lettre|Schreiben|Handschrift|Nachlass|\bNL\b|\bMss|\bMs\b|Archiv|Akten|Missive|Depesche|Bericht|Relation|Kopie|Ms\.',re.I)
n=0
for r in seen.values():
    t=r['text'].split('Treffernummer',1)[-1]
    t=re.sub(r'^\s*\d+\s*','',t)
    if ' : ' in t.split('zur Detail')[0] and not re.search(r'Brief|Korrespondenz|Lettre',t): continue
    if pat.search(t):
        n+=1; print(r['id'],'|',','.join(r['terms'][:2]),'|',t[:260].replace('zur Detailansicht',''))
print(n,len(seen))
