"""Find BSB manuscript catalogues (OCR full text on MDZ) that mention ciphers; list volumes and hit counts."""
import fetch,json,re,urllib.parse as u
S="out"  # raw hit files; not kept in the repo
KEY=re.compile(r'atalog|erzeichn|andschrift|odic|Inventa|Repertor',re.I)
res={}
for q in ['"in Chiffern"','chiffrirt','chiffrirten','"en chiffres"','"in cifra"','"in Ziffern"','Chiffernschrift','"mit Chiffern"','dechiffrirt','"Geheimschrift"']:
    for page in range(0,5):
        s,b=fetch.get("https://www.digitale-sammlungen.de/api/search?handler=simple-fulltext&pageSize=100&startPage=%d&query=%s"%(page,u.quote(q)))
        if s!=200: print('ERR',q,s); break
        d=json.loads(b)
        for x in d['docs']:
            t=x.get('title','')
            if KEY.search(t):
                r=res.setdefault(x['id'],{'title':t,'date':x.get('publicationDate'),'hits':{}})
                r['hits'][q]=x.get('totalOcrSnippets')
        if (page+1)*100>=d['numTotal']: break
    print(q,d['numTotal'],flush=True)
json.dump(res,open(S+'/mdz_catalogues.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k,v in res.items(): print(k,v['date'],v['title'][:100].encode('ascii','replace').decode(),v['hits'])
