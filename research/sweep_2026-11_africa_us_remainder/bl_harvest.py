"""Blacklight finding-aid harvest (Penn/PACSCL findingaids.library.upenn.edu, Princeton). usage: bl_harvest.py host term..."""
import sys,re,html,time,json,subprocess,urllib.parse
host=sys.argv[1]; terms=sys.argv[2:]
out=open(f"hits_{host.split('.')[1]}.jsonl","a",encoding="utf8")
for term in terms:
    n=0
    for page in range(1,30):
        q=urllib.parse.urlencode({"q":f'"{term}"' if " " in term else term,"page":page,"search_field":"all_fields"})
        h=subprocess.run(["curl","-s","-m","30","-A","Mozilla/5.0",f"https://{host}/?{q}"],capture_output=True).stdout.decode("utf8","replace")
        docs=re.split(r'<article[^>]*class="[^"]*document',h)[1:]
        if not docs: break
        for d in docs:
            m=re.search(r'href="(/(?:records|catalog)/[^"]+)"[^>]*>(.*?)</a>',d,re.S)
            if not m: continue
            snip=re.sub(r'<[^>]+>',' ',d); snip=html.unescape(re.sub(r'\s+',' ',snip))
            out.write(json.dumps({"term":term,"url":"https://"+host+m.group(1),"title":html.unescape(re.sub('<[^>]+>','',m.group(2))).strip(),"snip":snip[:700]},ensure_ascii=False)+"\n"); n+=1
        if 'rel="next"' not in h and 'next_page' not in h: break
        time.sleep(2.5)
    print(host,term,n,flush=True)
