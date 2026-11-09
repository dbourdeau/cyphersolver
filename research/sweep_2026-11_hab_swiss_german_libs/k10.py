import urllib.request,urllib.parse,re,time,json,sys
terms=sys.argv[1:]
out={}
for t in terms:
    q=f'pica.tit={t} and pica.mat=handschrift'
    n=None;start=1
    while True:
        u='https://sru.k10plus.de/opac-de-627?version=1.1&operation=searchRetrieve&maximumRecords=100&recordSchema=dc&startRecord=%d&query=%s'%(start,urllib.parse.quote(q))
        x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode('utf8')
        n=int(re.search(r'numberOfRecords>(\d+)',x).group(1))
        for r in re.findall(r'<zs:recordData>(.*?)</zs:recordData>',x,flags=re.S):
            ti=re.findall(r'<dc:title>(.*?)</dc:title>',r);dt=re.findall(r'<dc:date>(.*?)</dc:date>',r);idn=re.findall(r'<dc:identifier>(.*?)</dc:identifier>',r)
            out[idn[0] if idn else str(len(out))]=(t,ti,dt,idn)
        start+=100
        time.sleep(2)
        if start>n or start>1000:break
    print(t,n)
json.dump(out,open('k10_hits.json','w'),ensure_ascii=False)
