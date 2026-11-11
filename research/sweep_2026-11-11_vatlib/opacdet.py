"""python opacdet.py <outfile.jsonl> <Shelfmark>... : OPAC shelfmark page text (bibliography / items), 3 s apart"""
import http.cookiejar, urllib.request, re, json, sys, time, html
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders=[('User-Agent',UA),('Referer','https://opac.vatlib.it/mss/'),('Accept-Language','en')]
op.open('https://opac.vatlib.it/mss/',timeout=60).read(); time.sleep(2)
out=open(sys.argv[1],'a',encoding='utf8')
for sm in sys.argv[2:]:
    try:
        t=op.open('https://opac.vatlib.it/mss/detail/'+sm,timeout=60).read().decode('utf8','replace')
    except Exception as e:
        print(sm,'ERR',e,flush=True)
        if '429' in str(e) or '403' in str(e): break
        time.sleep(3); continue
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    s=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',t)))
    a=s.find('NEW SEARCH'); b=s.find('Back to Top')
    s=s[a+10:b].strip()
    out.write(json.dumps({'sm':sm,'text':s},ensure_ascii=False)+'\n'); out.flush()
    print(sm,len(s),flush=True); time.sleep(3)
