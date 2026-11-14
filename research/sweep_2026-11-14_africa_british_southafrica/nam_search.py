"""National Army Museum collection search (plain curl). python nam_search.py term ... ; prints count and first rows"""
import sys, re, html, subprocess, time, urllib.parse
for term in sys.argv[1:]:
    u = "https://collection.nam.ac.uk/results.php?searchType=simple&resultsDisplay=list&keywords=" + urllib.parse.quote_plus(term)
    t = subprocess.run(["curl","-s","-m","40","-L","-A","Mozilla/5.0",u],capture_output=True).stdout.decode("utf8","replace")
    x = re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",re.sub(r"<(script|style)[^>]*>.*?</\1>","",t,flags=re.S))))
    if "No results" in x: print(repr(term), 0)
    else:
        m = re.search(r"(\d+) results?|of (\d+)", x); print(repr(term), m.group(0) if m else "?")
        rows = re.findall(r'href="(detail\.php\?[^"]+)"[^>]*>(.*?)</a>', t, re.S)
        for h, tx in rows[:12]: print("   ", re.sub(r"\s+"," ",re.sub(r"<[^>]+>","",tx))[:140], h[:60])
    time.sleep(3)
