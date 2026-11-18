import json, urllib.request, sys, time
def q(term, types="File,Series,Fonds", page=1, per=60):
    body={"pagination":{"page":page,"perPage":per},"query":{"type":"AndQuery","queries":[{"type":"FieldQuery","operator":"equals","field":"data.recordType.id","value":types},{"type":"FullTextQuery","query":""},{"type":"FullTextQuery","query":term}]}}
    req=urllib.request.Request("https://id.archief.amsterdam/search/records?lang=nl",data=json.dumps(body).encode(),headers={"content-type":"application/json","User-Agent":"Mozilla/5.0"})
    return json.load(urllib.request.urlopen(req,timeout=60))
if __name__=="__main__":
    d=q(sys.argv[1]); print(json.dumps(d,ensure_ascii=False)[:3000])
