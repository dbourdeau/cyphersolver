"""Wellcome Collection catalogue API (api.wellcomecollection.org/catalogue/v2/works). python wellcome.py <term>... ; prints id, date, title, workType"""
import subprocess, sys, json, time, urllib.parse
for term in sys.argv[1:]:
    page=1; rows=[]; tot=None
    while True:
        u=f"https://api.wellcomecollection.org/catalogue/v2/works?query={urllib.parse.quote(term)}&pageSize=100&page={page}"
        j=json.loads(subprocess.run(["curl","-s","-m","60",u],capture_output=True).stdout)
        tot=j.get("totalResults"); 
        for r in j.get("results",[]):
            rows.append((r["id"],(r.get("production") or [{}])[0].get("dates",[{}])[0].get("label","") if r.get("production") else "",r["title"][:120],r.get("workType",{}).get("label",""),r.get("referenceNumber","")))
        time.sleep(2.5)
        if page>=j.get("totalPages",1) or page>=5: break
        page+=1
    print(f"{term!r}: {tot} total, {len(rows)} read")
    for r in rows: print("  ",r)
