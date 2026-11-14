"""DSpace 7 REST discover search. python dspace.py <base> <term> ... ; prints total and title/date/type of items."""
import subprocess, sys, json, time, urllib.parse
def get(url):
    return json.loads(subprocess.run(["curl","-s","-m","60",url],capture_output=True).stdout.decode("utf8","replace"))
base=sys.argv[1]
for term in sys.argv[2:]:
    page=0; n=None; rows=[]
    while True:
        j=get(f"{base}/server/api/discover/search/objects?query={urllib.parse.quote(term)}&size=50&page={page}")
        sr=j["_embedded"]["searchResult"]
        n=sr["page"]["totalElements"]
        for o in sr["_embedded"]["objects"]:
            it=o["_embedded"]["indexableObject"]; md=it.get("metadata",{})
            g=lambda k:(md.get(k) or [{"value":""}])[0]["value"]
            rows.append((g("dc.date.issued"),g("dc.type"),it.get("handle"),it["name"][:110]))
        page+=1; time.sleep(2.5)
        if page>=sr["page"]["totalPages"] or page>=6: break
    print(f"{term!r}: {n} total")
    for r in sorted(rows)[:int(__import__('os').environ.get('SHOW','40'))]: print("  ",r)
