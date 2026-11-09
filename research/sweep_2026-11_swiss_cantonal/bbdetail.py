import re,html,requests,time,sys
for i in sys.argv[1:]:
    t=requests.get('https://katalog.burgerbib.ch/detail.aspx?ID='+i,headers={'User-Agent':'Mozilla/5.0 (research)'},timeout=60).text
    b=re.sub(r'<(script|style).*?</\1>','',t,flags=re.S|re.I); b=html.unescape(re.sub(r'<[^>]+>',' ',b)); b=re.sub(r'\s+',' ',b)
    k=b.find('Titel:'); e=b.find('Social Media')
    print('###',i,b[k:e],'\n'); time.sleep(2)
