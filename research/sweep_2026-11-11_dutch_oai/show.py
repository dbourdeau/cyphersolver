"""Filter OAI hit files: keep cipher-looking components, drop classification-code and statistics noise and items dated after 1900."""
import json,sys,re
good=re.compile(r'cijferschrift|cijfercode|cijfersleutel|cijferbrie|gecijferd|in (?:het |de )?cijfer(?!s\b)|in cijfers? ge|geheim\s?schrift|geheime? (?:code|taal|teken)|chiffr|cypher|cipher|cyfer|figuurcode|cifr|ontcijfer|\bin code\b|codeschrift|cryptogra|sleutel (?:van|voor|tot)',re.I)
bad=re.compile(r'ongecodeerd|gecodeerd met|niet (?:te )?ontcijfer|onontcijfer|moeilijk te ontcijfer|slecht te ontcijfer|cijferakkoord|cijferlijst|cijfernotatie|muziek|liedjes|liederen',re.I)
for fn in sys.argv[1:]:
    for i,l in enumerate(open(fn,encoding='utf8')):
        d=json.loads(l); s=d['title']+' '+d['scope']+' '+d['odd']
        if not good.search(s) or bad.search(s): continue
        ys=[int(y) for y in re.findall(r'\b(1[0-9]{3}|20[0-2][0-9])\b',d['date']+' '+d['title'])]
        if ys and min(ys)>1900: continue
        print(fn[5:9],i,d['set'][10:],d['fond_code'],d['fond'][:40],'|',d['id'][:12],d['date'][:20],d['title'][:260],'|',d['scope'][:160],'|dao',d['dao'])
