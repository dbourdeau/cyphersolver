import re,html,urllib.request,urllib.parse,time,json
out={}
for t in ["šifra","šifrirano","šifrirano pismo","tajnopis","tajna pisava","cifra","Chiffre","Geheimschrift","chiffre","cifrirano","pismo v šifri"]:
    u="https://www.dlib.si/results/?query="+urllib.parse.quote("'keywords="+t+"'",safe="'=")+"&pageSize=50"
    r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=40).read().decode("utf8","replace")
    n=0
    for m in re.finditer(r'<a[^>]*href="(/details/[^"]+)"[^>]*>(.*?)</a>',r,re.S):
        s=html.unescape(re.sub(r'<[^>]+>','',m.group(2))).strip()
        if s and m.group(1) not in out: out[m.group(1)]=(s,t); n+=1
    print(t,n,flush=True); time.sleep(2.5)
json.dump(out,open("dlib_hits.json","w",encoding="utf8"),ensure_ascii=False,indent=1)
for k,v in out.items(): print(k[-8:],v[1],v[0][:100])
