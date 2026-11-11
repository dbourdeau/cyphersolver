# AIS full-text search via the aut_hhsta helper; usage: ais.py "term" ...
import sys,time
sys.path.insert(0,"../aut_hhsta")
import ais_search as A
for term in sys.argv[1:]:
    try:
        tot,o=A.crawl(term,3)
    except Exception as e:
        print("ERR",term,e); continue
    print("==",term,tot,len(o))
    for r in o[:40]: print("  ",r["id"],"|",r["sig"],"|",r["date"],"|",r["title"][:110],"|",r["darin"][:120])
    time.sleep(3)
