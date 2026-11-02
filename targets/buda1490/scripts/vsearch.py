import json,subprocess,sys,time,urllib.parse
seen={}
for q in sys.argv[1:]:
    for page in range(1,9):
        u=f"https://www.vestigia.hu/api/search?search={urllib.parse.quote(q)}&page={page}"
        r=subprocess.run(['curl','-sL',u],capture_output=True,text=True).stdout
        try: d=json.loads(r)['documents']
        except Exception: break
        for it in d['data']:
            df=it.get('date_from') or ''
            if '1490-10'<=df<='1491-02-28':
                seen[it['vestigia_id']]=(df,it.get('archive_ref'),it.get('title'),(it.get('summary') or '')[:200])
        if page>=d.get('last_page',1): break
        time.sleep(2.5)
for k,v in sorted(seen.items(),key=lambda x:x[1][0]): print(k,v)
