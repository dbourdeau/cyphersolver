"""Generic scopeArchiv full-text harvest. usage: scope_harvest.py BASE OUT.jsonl TERM..."""
import re,sys,json,html,time,requests
B=sys.argv[1]
def hidden(t): return {m.group(1): html.unescape(m.group(2)) for m in re.finditer(r'<input type="hidden" name="([^"]+)" id="[^"]*" value="([^"]*)"', t)}
def clean(x): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',x))).strip()
ROW=re.compile(r'hylTitel" href="detail\.aspx\?ID=(\d+)"[^>]*>(.*?)</a>.*?</td><td>(.*?)</td><td>(.*?)</td><td>\s*<span[^>]*lblSignatur">(.*?)</span>',re.S)
out=open(sys.argv[2],'a',encoding='utf-8')
for term in sys.argv[3:]:
    s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0 (research)'
    r=s.get(B+'volltextsuche.aspx',timeout=60); d=hidden(r.text)
    d['ctl00$cphMainArea$txtMitAllenWoertern']=term; d['ctl00$cphMainArea$cmdSuchen']='Suchen'
    r=s.post(B+'volltextsuche.aspx',data=d,timeout=120)
    m=re.search(r'(\d[\d\.\',]*)\s*(?:Treffer|hits|results|Resultate)',r.text); print(term,'count?',m.group(0) if m else None,flush=True)
    seen=set();page=1
    while True:
        new=0
        for m in ROW.finditer(r.text):
            i=m.group(1)
            if i in seen: continue
            seen.add(i);new+=1
            out.write(json.dumps(dict(id=i,title=clean(m.group(2)),date=clean(m.group(3)),level=clean(m.group(4)),sig=clean(m.group(5)),term=term),ensure_ascii=False)+'\n')
        n=re.search(r'class="nextPage" href="javascript:__doPostBack\(&#39;([^&]+)&#39;',r.text)
        if not n or not new or page>150: break
        d=hidden(r.text); d['__EVENTTARGET']=n.group(1); d['__EVENTARGUMENT']=''
        r=s.post(B+'resultatliste.aspx',data=d,timeout=120); page+=1; time.sleep(0.3)
    out.flush(); print(term,len(seen),'pages',page,flush=True)
