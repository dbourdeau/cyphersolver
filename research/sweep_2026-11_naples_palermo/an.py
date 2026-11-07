import urllib.request, urllib.parse, json, sys, time, re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
B="https://archivinazionali.cultura.gov.it"
def get(u):
    r=urllib.request.Request(u,headers={"User-Agent":UA,"Accept":"application/json, text/html"})
    return urllib.request.urlopen(r,timeout=40).read().decode("utf8","replace")
def units(field,term,cur=1,size=50):
    q=urllib.parse.urlencode({"p_p_id":"it_inera_search_unita_documentarie_SearchSimpleResultsUnitaDocumentariePortlet","p_p_lifecycle":"2","p_p_state":"normal","p_p_mode":"view","p_p_resource_id":"/simple/search","p_p_cacheability":"cacheLevelPage",field:term,"cur":cur,"pageSize":size})
    return get(B+"/it/risultati-ricerca-unita?"+q)
if __name__=="__main__":
    t=units(sys.argv[1],sys.argv[2],1,5)
    print(t[:3000])
