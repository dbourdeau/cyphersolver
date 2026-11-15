import json,re,glob
bad=re.compile(r'ongecodeerd|niet.gecodeerd|Code \d|code \d|gecodeerde? (?:stukken|dossier|bijlage)|gecodeerd (?:volgens|G-)|onontcijferbaar|slecht te ontcijferen|ontcijferen\)|moeilijk te ontcijferen',re.I)
seen=set()
for f in sorted(glob.glob('h?.jsonl')):
    for l in open(f,encoding='utf8'):
        d=json.loads(l); s=d['title']+' '+d['scope']+' '+d['odd']
        k=(d['guid'],d['id'],d['title'][:40])
        if k in seen: continue
        seen.add(k)
        if bad.search(s): continue
        m=re.search(r'\b(1[0-9]{3})\b',d['date']+' '+d['title'])
        y=int(m.group(1)) if m else 0
        if y<1921:
            print(d['set'][10:],d['fond_code'],d['fond'][:30],'|',d['id'],d['date'][:20],d['title'][:150],'|',d['scope'][:150]);print()
