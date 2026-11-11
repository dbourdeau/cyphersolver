import json,sys,re
seen=set()
skip=int(sys.argv[2]) if len(sys.argv)>2 else 0
for i,l in enumerate(open(sys.argv[1],encoding='utf8')):
    if i<skip: continue
    d=json.loads(l)
    print('##',i,d['term'],'|',d['archive'][:30],'|',d['code'],d['fond'][:60],'| n',d['n'],d['note'][:80].replace('\n',' '))
    for it in d['items']:
        k=(d['archive'],d['code'],it['id'])
        if k in seen: continue
        seen.add(k)
        t=re.sub(r'\s+',' ',it['text'])
        m=re.search(r'.{0,170}(geheimschrift|cijfer|chiffr|code|cipher|ontcijf).{0,150}',t,re.I)
        print('   ',it['id'],'|',(m.group(0) if m else t[:300]))
