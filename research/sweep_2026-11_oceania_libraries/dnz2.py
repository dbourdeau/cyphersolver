import json,sys,time,urllib.request,urllib.parse
out={}
for t in ['"in cipher"','"in cypher"','cipher','cypher','cryptogram','"secret writing"','deciphered','undeciphered','"in code"','"written in code"','ciphered','"secret code"','"code letter"']:
    page=1
    while page<=5:
        u="https://api.digitalnz.org/records.json?"+urllib.parse.urlencode({"text":t,"per_page":100,"page":page,"fields":"id,title,description,display_collection,date,landing_url,content_partner,category"})
        try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=40))["search"]
        except Exception as e: print(t,page,"ERR",e);break
        for r in d["results"]: r["_t"]=t; out.setdefault(r["id"],r)
        print(t,page,d["result_count"],len(out),flush=True)
        time.sleep(2)
        if page*100>=d["result_count"]:break
        page+=1
json.dump(list(out.values()),open("dnz_hits.json","w"),indent=1,ensure_ascii=False)
