"""swisscollections.ch (VuFind) keyword harvest. usage: swisscoll.py OUT.jsonl TERM..."""
import re,sys,json,html,time,requests,urllib.parse
H={'User-Agent':'Mozilla/5.0 (research)'}
out=open(sys.argv[1],'a',encoding='utf-8')
def clean(x): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',x))).strip()
for term in sys.argv[2:]:
    n=0;page=1;seen=set()
    while page<=30:
        u='https://swisscollections.ch/Search/Results?'+urllib.parse.urlencode({'lookfor':term,'type':'AllFields','limit':100,'page':page})
        t=requests.get(u,headers=H,timeout=60).text
        if page==1:
            m=re.search(r'(\d[\d\'’,.]*)\s+Suchergebnisse',clean(t)); tot=m.group(1) if m else '?'
        blocks=re.split(r'<div[^>]*class="[^"]*\bresult\b[^"]*"',t)[1:]
        new=0
        for b in blocks:
            m=re.search(r'href="/Record/(\d+)',b)
            if not m or m.group(1) in seen: continue
            seen.add(m.group(1)); new+=1
            out.write(json.dumps(dict(id=m.group(1),text=clean(b)[:600],term=term),ensure_ascii=False)+'\n')
        if not new: break
        page+=1; time.sleep(2.5)
    out.flush(); print(term,'total',tot,'got',len(seen),flush=True)
