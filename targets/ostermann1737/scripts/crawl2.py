import re,html,time,urllib.parse,urllib.request,hashlib,os
UA="keyless-research/1.0 (historical cipher research; polite)"
OUT='/home/claude/keyless/ostermann1737/lmsrc/'
os.makedirs(OUT+'html',exist_ok=True)
pages=[p for p in open(OUT+'pages.txt').read().split('\n') if p and not p.endswith('/ВТ') and '/ВТ/' not in p]
log=open(OUT+'FETCH_LOG_lm.txt','a')
for p in pages:
    fn=hashlib.md5(p.encode()).hexdigest()[:10]+'.html'
    if os.path.exists(OUT+'html/'+fn): continue
    url='https://ru.wikisource.org/wiki/'+urllib.parse.quote(p.replace(' ','_'))
    try:
        d=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=60).read().decode('utf8','replace')
    except Exception as e:
        print('ERR',p,e,flush=True); time.sleep(90); continue
    i=d.find('mw-parser-output'); j=d.find('id="catlinks"')
    d=d[i:j]
    open(OUT+'html/'+fn,'w').write(d)
    log.write('%s\t%s\t%d\t%s\n'%(fn,p,len(d),hashlib.md5(d.encode()).hexdigest())); log.flush()
    time.sleep(6)
print('done')
