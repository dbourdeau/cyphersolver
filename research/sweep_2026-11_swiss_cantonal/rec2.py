import re,html,requests,time,sys
for i in sys.argv[1:]:
    t=requests.get('https://swisscollections.ch/Record/'+i+'/Details',headers={'User-Agent':'Mozilla/5.0 (research)'},timeout=60).text
    t=re.sub(r'<script.*?</script>','',t,flags=re.S); b=html.unescape(re.sub(r'<[^>]+>',' ',t)); b=re.sub(r'\s+',' ',b)
    b=b.split('Hierarchie / Kontext')[0]
    hits=[m.start() for m in re.finditer(r'(?i)geheimschrift|chiffr|ziffer|verschl',b)]
    print('###',i,b[b.find('Titel'):b.find('Titel')+120].replace('Gesamten Text anzeigen Text zuklappen',''))
    for h in hits[:3]: print('   >>',b[max(0,h-250):h+250].replace('Gesamten Text anzeigen Text zuklappen',''))
    time.sleep(2.5)
