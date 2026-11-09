import re,html,requests,time,sys
for i in sys.argv[1:]:
    t=requests.get('https://swisscollections.ch/Record/'+i+'/Details',headers={'User-Agent':'Mozilla/5.0 (research)'},timeout=60).text
    t=re.sub(r'<script.*?</script>','',t,flags=re.S); b=html.unescape(re.sub(r'<[^>]+>',' ',t)); b=re.sub(r'\s+',' ',b)
    k=b.find('Titel'); 
    print('###',i,b[k:k+1400],'\n'); time.sleep(2.5)
