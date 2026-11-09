import re,html,requests,time,sys
for i in sys.argv[1:]:
    t=requests.get('https://swisscollections.ch/Record/'+i+'/Details',headers={'User-Agent':'Mozilla/5.0 (research)'},timeout=60).text
    t=re.sub(r'<script.*?</script>','',t,flags=re.S); b=html.unescape(re.sub(r'<[^>]+>',' ',t)); b=re.sub(r'\s+',' ',b).replace('Gesamten Text anzeigen Text zuklappen','')
    b=b.split('Hierarchie / Kontext')[0]
    m=re.search(r'490 1.*?(?=583 1)',b)
    print('###',i,'\n',(m.group(0) if m else b[:1500])[:1800])
    for u in set(re.findall(r'https?://[^\s"]*(?:e-manuscripta|e-rara|iiif|doi|permalink)[^\s"]*',t)): print('  URL',u)
    time.sleep(2.5)
