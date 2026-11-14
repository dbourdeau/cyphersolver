"""BNP Horizon keyword searches combining cipher terms with African place words; prints hit count and titles (page 1)."""
import re, sys, time, urllib.parse, urllib.request, html
B="https://catalogo.bnportugal.gov.pt/ipac20/ipac.jsp?profile=bn&menu=search&index=.GW&term="
for t in sys.argv[1:]:
    u=B+urllib.parse.quote(t)
    try: s=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (research sweep)"}),timeout=60).read().decode("utf8","replace")
    except Exception as e: print(t,"ERR",e); time.sleep(3); continue
    m=re.search(r"(\d+)\s*(?:-|a)\s*\d+\s*(?:de|of)\s*(\d+)",s) or re.search(r"Resultados[^<]{0,80}",s)
    n=re.search(r"de\s+(\d+)\s*<",s)
    txt=re.sub(r"<[^>]+>"," ",s); txt=html.unescape(re.sub(r"\s+"," ",txt))
    k=re.search(r"(\d[\d.]*) (?:resultados|registos|títulos)",txt)
    print("##",t,"|",m.group(0) if m else "", "|", k.group(0) if k else "")
    for x in re.findall(r"<a[^>]*class=\"mediumBoldAnchor\"[^>]*>(.*?)</a>",s,flags=re.S)[:10]:
        print("   ",html.unescape(re.sub(r"<[^>]+>","",x)).strip()[:140])
    time.sleep(2.5)
