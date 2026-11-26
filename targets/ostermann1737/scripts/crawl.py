import re,html,time,urllib.parse,urllib.request,sys,os,hashlib
UA="keyless-research/1.0 (historical cipher research; polite)"
OUT='/home/claude/keyless/ostermann1737/lmsrc/'
def get(url):
    for k in range(3):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=60)
            d=r.read().decode('utf8','replace'); time.sleep(5); return d
        except Exception as e:
            print('ERR',url[:80],e,flush=True); time.sleep(60)
    return ''
def cat(name):
    s=get('https://ru.wikisource.org/wiki/'+urllib.parse.quote(name.replace(' ','_')))
    i=s.find('id="mw-pages"'); j=s.find('id="catlinks"')
    subs=[html.unescape(x) for x in re.findall(r'title="(Категория:[^"]+)"',s[:i if i>0 else j])]
    pages=[html.unescape(x) for x in re.findall(r'<li><a href="/wiki/[^"]+" title="([^"]+)"',s[i:j])] if i>0 else []
    return subs,pages
seen=set(); pages=[]
queue=['Категория:Документы %d-х годов'%d for d in (1730,1720,1740,1710,1700)]
depth={q:0 for q in queue}
while queue and len(pages)<400:
    c=queue.pop(0)
    if c in seen: continue
    seen.add(c)
    subs,pg=cat(c); print(c,len(subs),len(pg),flush=True)
    pages+= [p for p in pg if p not in pages]
    for s in subs:
        if s not in seen and depth[c]<2 and re.search(r'17[0-4]\d|Документы|Указы|Письма|Манифест',s) and not re.search(r'17[5-9]\d|1[0-6]\d\d|18\d\d',s):
            depth[s]=depth[c]+1; queue.append(s)
open(OUT+'pages.txt','w').write('\n'.join(pages))
log=open(OUT+'FETCH_LOG_lm.txt','a')
for p in pages[:300]:
    if p.endswith('/ВТ'): continue
    d=get('https://ru.wikisource.org/w/index.php?title='+urllib.parse.quote(p.replace(' ','_'))+'&action=raw')
    if not d: continue
    fn=hashlib.md5(p.encode()).hexdigest()[:10]+'.txt'
    open(OUT+'raw/'+fn,'w').write(d)
    log.write('%s\t%s\t%d\t%s\n'%(fn,p,len(d),hashlib.md5(d.encode()).hexdigest())); log.flush()
print('done')
