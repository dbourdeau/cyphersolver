import urllib.request, urllib.parse, re, time, json, sys
import xml.etree.ElementTree as ET
ns={'dc':'http://purl.org/dc/elements/1.1/','dcterms':'http://purl.org/dc/terms/','os':'http://a9.com/-/spec/opensearchrss/1.0/','rdfs':'http://www.w3.org/2000/01/rdf-schema#','dcndl':'http://ndl.go.jp/dcndl/terms/'}
out={}
terms=sys.argv[1:]
for kw in terms:
    start=1
    while True:
        u="https://ndlsearch.ndl.go.jp/api/opensearch?"+urllib.parse.urlencode({"any":kw,"cnt":200,"idx":start})
        t=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (research)"}),timeout=60).read()
        r=ET.fromstring(t)
        tot=int(r.find('channel/os:totalResults',ns).text)
        items=r.findall('channel/item')
        for it in items:
            g=lambda p:[e.text for e in it.findall(p,ns)]
            link=it.findtext('link')
            out.setdefault(link,{"title":(g('dc:title') or [''])[0],"creator":g('dc:creator'),"date":g('dc:date')+g('dcterms:issued'),"publisher":g('dc:publisher'),"type":g('dc:type'),"link":link,"kw":[]})["kw"].append(kw)
        print(kw,start,tot,len(items),flush=True)
        start+=200; time.sleep(3)
        if start>tot or not items or start>1000: break
json.dump(list(out.values()),open("ndl_hits.json","w",encoding="utf8"),ensure_ascii=False,indent=0)
print(len(out))
