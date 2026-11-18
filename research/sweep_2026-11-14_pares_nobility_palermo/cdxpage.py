import subprocess,json,time
rows={}
for y in range(2018,2024):
  for m in range(1,13):
    u=f"http://web.archive.org/cdx/search/cdx?url=saassipa.cultura.gov.it/wp-content/uploads/{y}/{m:02d}/*&filter=mimetype:application/pdf&output=json&fl=original,timestamp,mimetype,length&collapse=urlkey"
    r=subprocess.run(['curl','-s','-m','60','-w','\n%{http_code}',u],capture_output=True,text=True).stdout
    body,code=r.rsplit('\n',1)
    if code!='200': print(y,m,code,flush=True); time.sleep(3); continue
    try: d=json.loads(body) if body.strip() else []
    except Exception: print(y,m,'bad',flush=True); continue
    n=0
    for x in d[1:]: rows[x[0]]=x; n+=1
    print(y,m,n,flush=True)
    time.sleep(1.5)
json.dump([["original","timestamp","mimetype","length"]]+list(rows.values()),open('cdx_saassipa.json','w'))
print('TOTAL',len(rows),flush=True)
