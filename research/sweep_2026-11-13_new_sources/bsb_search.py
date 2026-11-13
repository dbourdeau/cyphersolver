import json,subprocess,sys,time,urllib.parse,re
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
SCR="/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/newsrc/"
terms=sys.argv[1:]
out={}
for t in terms:
    for h in ('simple-all',):
        n=0;docs=[];p=0
        while True:
            q=urllib.parse.urlencode({'query':t,'handler':h,'pageSize':100,'startPage':p,'filter':'type_manufact:"handmade"','ocrContext':0})
            r=subprocess.run(['curl','-s','-m','40','-A',UA,'https://www.digitale-sammlungen.de/api/search?'+q],capture_output=True,text=True).stdout
            try:d=json.loads(r)
            except Exception: print('ERR',t,r[:100]);break
            docs+=d['docs'];n=d['numTotal']
            if len(docs)>=n or not d['docs']:break
            p+=1;time.sleep(2)
        print(t,n)
        out[t]=[{'id':x['id'],'shelf':x.get('shelfNos'),'title':re.sub('<[^>]+>','',x['title']),'date':x.get('publicationDate'),'prov':x.get('provenance'),'snip':[re.sub('<[^>]+>','',s['text']) for s in x.get('ocrSnippets',[])][:2]} for x in docs]
        time.sleep(2)
json.dump(out,open(SCR+'bsb_hits_%s.json'%re.sub(r'\W','_',terms[0]),'w'),ensure_ascii=False,indent=1)
