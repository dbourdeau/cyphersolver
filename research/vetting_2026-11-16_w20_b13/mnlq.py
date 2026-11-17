import base64,json,sys,urllib.request,urllib.parse,re,html,time
def q(s,page=None):
    term={"q":s,"fq":{"db_id":{"812b4ba287f5ee0bc9d43bbf5bbe87fb":"95"}},"sort":"score"}
    u='https://adatbazisokonline.mnl.gov.hu/adatbazis/a-karolyi-leveltar-rakoczi-kori-iratai/kereses?term='+urllib.parse.quote(base64.b64encode(json.dumps(term).encode()).decode())
    if page: u+='&page=%d'%page
    r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode('utf8','replace')
    return r
for s in sys.argv[1:]:
    t=q(s)
    ids=re.findall(r'adatlap/(\d+)',t)
    txt=html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>','',t,flags=re.S)))
    m=re.search(r'(\d[\d\s]*)\s*találat',txt)
    print('==',s,'hits:',m.group(1) if m else '?','ids:',list(dict.fromkeys(ids))[:40])
    time.sleep(1)
