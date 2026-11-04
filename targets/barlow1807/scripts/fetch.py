import json, time, urllib.request, urllib.parse, sys, os
UA={'User-Agent':'WAINUT-research'}
base="File:Two letters to Thomas Grenville (in cipher) and to George Tierney on affairs in India - DPLA - e4082bb91cf5f55ec10516bc367df12d (page %d).jpg"
out=sys.argv[1]
for p in range(1,27):
    fn=os.path.join(out,'p%02d.jpg'%p)
    if os.path.exists(fn): continue
    q=urllib.parse.urlencode({'action':'query','titles':base%p,'prop':'imageinfo','iiprop':'url|size','format':'json'})
    r=json.load(urllib.request.urlopen(urllib.request.Request('https://commons.wikimedia.org/w/api.php?'+q,headers=UA)))
    ii=list(r['query']['pages'].values())[0]['imageinfo'][0]
    time.sleep(30)
    data=urllib.request.urlopen(urllib.request.Request(ii['url'],headers=UA)).read()
    open(fn,'wb').write(data); print(p,ii['width'],ii['height'],ii['url']); time.sleep(30)
