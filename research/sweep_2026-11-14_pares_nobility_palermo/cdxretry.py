import subprocess,json,time,re
rows={x[0]:x for x in json.load(open('cdx_saassipa.json'))[1:]}
bad=[tuple(map(int,m.groups())) for m in re.finditer(r'^(\d{4}) (\d+) (?:503|000)$',open('cdxpage.log').read(),re.M)]
print(len(bad),'to retry',flush=True)
for rnd in range(3):
  nb=[]
  for y,m in bad:
    u=f"http://web.archive.org/cdx/search/cdx?url=saassipa.cultura.gov.it/wp-content/uploads/{y}/{m:02d}/*&filter=mimetype:application/pdf&output=json&fl=original,timestamp,mimetype,length&collapse=urlkey"
    r=subprocess.run(['curl','-s','-m','90','-w','\n%{http_code}',u],capture_output=True,text=True).stdout
    body,code=r.rsplit('\n',1)
    if code!='200': nb.append((y,m)); time.sleep(5); continue
    try: d=json.loads(body) if body.strip() else []
    except Exception: nb.append((y,m)); continue
    for x in d[1:]: rows[x[0]]=x
    print(rnd,y,m,len(d)-1 if d else 0,flush=True); time.sleep(2)
  bad=nb
  if not bad: break
  time.sleep(30)
json.dump([["original","timestamp","mimetype","length"]]+list(rows.values()),open('cdx_saassipa.json','w'))
print('TOTAL2',len(rows),'still bad',bad,flush=True)
