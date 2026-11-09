import json,sys,time,urllib.request,urllib.parse
terms=sys.argv[1:]
out={}
for t in terms:
    for cat in ["Manuscripts","Archives","Documents","Books"]:
      for page in (1,2):
        u="https://api.digitalnz.org/records.json?"+urllib.parse.urlencode({"text":t,"and[category][]":cat,"per_page":100,"page":page,"fields":"id,title,description,display_collection,date,landing_url,content_partner,category"})
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=40))["search"]
        except Exception as e:
            print(t,cat,page,"ERR",e);break
        for r in d["results"]: out[r["id"]]=r
        print(t,cat,page,d["result_count"],len(out),flush=True)
        time.sleep(2)
        if page*100>=d["result_count"]:break
json.dump(list(out.values()),open("dnz_hits.json","w"),indent=1,ensure_ascii=False)
