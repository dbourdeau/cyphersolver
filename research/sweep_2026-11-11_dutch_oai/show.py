import json,sys,glob,re
bad=re.compile(r'in cijfers(?! (?:geschr|gest|opgest))|ongecodeerd|niet.gecodeerd|gecodeerde? (?:stukken|dossier|bijlage)|gecodeerd (?:volgens|G-)',re.I)
skip=int(sys.argv[2]) if len(sys.argv)>2 else 0
for i,l in enumerate(open(sys.argv[1],encoding='utf8')):
    if i<skip: continue
    d=json.loads(l); s=d['title']+' '+d['scope']+' '+d['odd']
    if bad.search(s) and not re.search(r'geheim|chiffr|cijferschrift|cijfercode',s,re.I): continue
    print(i,d['set'][10:],d['fond_code'],d['fond'][:40],'|',d['id'],d['date'][:20],d['title'][:220],'|',d['scope'][:200],'|dao',d['dao'])
