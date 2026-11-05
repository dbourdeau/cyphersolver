import requests, re, sys, base64, json, html, time
sys.stdout.reconfigure(encoding='utf-8')
H = {'User-Agent':'Mozilla/5.0 (cyphersolver research sweep; polite)'}
b = lambda d: base64.urlsafe_b64encode(json.dumps(d).encode()).decode().rstrip('=')
def clean(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',s))).strip()
for q in sys.argv[1:]:
    u='https://library.hungaricana.hu/hu/search/results/?list=%s&per_page=20' % b({'query':q})
    r=requests.get(u,headers=H,timeout=60)
    items=re.split(r'<li class="list-group-item bg-light mb-2 result',r.text)[1:]
    print('==',q,len(items))
    for it in items[:8]:
        href=re.search(r'<a href="([^"]+)"',it); title=re.search(r'<h5>.*?<a href="[^"]+">(.*?)</a>',it,re.S)
        print(' ',clean(title.group(1))[:120] if title else '', '|', href.group(1)[:90] if href else '')
    time.sleep(2.5)
