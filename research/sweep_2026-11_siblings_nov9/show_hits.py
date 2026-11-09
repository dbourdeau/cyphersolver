import json,re,glob,sys
rx=re.compile(r'cijferschrift|cijfercode|cijfersleutel|gecijferd|in cijfer(?!s)|geheimschrift|secreet\s*schrift|chiffr|cypher|cipher|cyfer|figuurcode|letterschrift|cifra|cifrat|cifr\b|ontcijfer|\bin code\b|gecodeerd',re.I)
bad=re.compile(r'in cijfers|ongecodeerd|niet.gecodeerd|Code \d|code \d|gecodeerde? (?:stukken|dossier|bijlage)|gecodeerd (?:volgens|G-)',re.I)
seen=set()
for f in sorted(glob.glob('oai_h*.jsonl')+glob.glob('oai_hits*.jsonl')):
    for l in open(f,encoding='utf8'):
        d=json.loads(l); s=d['title']+' '+d['scope']+' '+d['odd']
        k=(d['guid'],d['id'],d['title'][:40])
        if k in seen: continue
        seen.add(k)
        if rx.search(s) and not bad.search(s) and d['fond_code'] not in ('1001',):
            m=re.search(r'\b(1[0-9]{3})\b',d['date']+' '+d['title'])
            y=int(m.group(1)) if m else 0
            if y<1900:
                print(d['set'][10:],d['fond_code'],d['fond'][:35],'|',d['id'],d['date'][:20],d['title'][:130],'|',d['scope'][:130])
