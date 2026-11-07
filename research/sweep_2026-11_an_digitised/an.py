import subprocess, json, sys, time, urllib.parse
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
B="https://archivinazionali.cultura.gov.it/it/risultati-ricerca-unita?p_p_id=it_inera_search_unita_documentarie_SearchSimpleResultsUnitaDocumentariePortlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=%2Fsimple%2Fsearch&p_p_cacheability=cacheLevelPage"
def get(url):
    time.sleep(1.2)
    r=subprocess.run(["curl","-s","-A",UA,url],capture_output=True)
    return r.stdout.decode("utf8","replace")
def search(field,term,cur=1,dig=None,size=50):
    u=B+"&%s=%s&cur=%d&pageSize=%d"%(field,urllib.parse.quote(term),cur,size)
    if dig: u+="&oggetti-digitali-un="+dig
    return get(u)
if __name__=="__main__":
    for d in [None,"true","on","1"]:
        t=search("denominazione-un","cifrato",1,d)
        print(d,len(t),t[:300].replace("\n"," "))

def children(eid,kind="unita-archivistica"):
    u="https://archivinazionali.cultura.gov.it/it/%s?p_p_id=it_inera_search_unita_documentarie_DetailUnitaArchivisticaPortlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=%%2Ftree%%2Fsearch%%2Fchildren&p_p_cacheability=cacheLevelPage&_it_inera_search_unita_documentarie_DetailUnitaArchivisticaPortlet_entitaId=%s"%(kind,eid)
    return get(u)

def kids(eid):
    import json
    d=json.loads(children(eid))["data"]
    return d.get("nodi") or d.get("cards") or []
