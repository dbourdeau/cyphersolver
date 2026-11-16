# advancedsearch identifier discovery; usage: find.py out.json "<lucene query>" ...
import sys,json,urllib.parse,urllib.request,time
out=sys.argv[1]
try: res=json.load(open(out,encoding='utf-8'))
except Exception: res={}
for q in sys.argv[2:]:
    start=0
    while True:
        u="https://archive.org/advancedsearch.php?q="+urllib.parse.quote(q+" AND mediatype:texts")+"&fl[]=identifier&fl[]=title&fl[]=volume&fl[]=year&fl[]=imagecount&fl[]=contributor&rows=500&start=%d&output=json"%start
        d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=90))["response"]
        for x in d["docs"]:
            res.setdefault(x["identifier"],{"title":x.get("title"),"volume":x.get("volume"),"year":x.get("year"),"n":x.get("imagecount"),"contrib":x.get("contributor"),"q":q})
        start+=500
        if start>=d["numFound"]: break
        time.sleep(1.5)
    print(d["numFound"],q,flush=True); time.sleep(1.5)
json.dump(res,open(out,"w",encoding='utf-8'),indent=0,ensure_ascii=False)
