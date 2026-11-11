#!/usr/bin/env python3
"""AtoM search (informationobject/browse). usage: atom_search.py BASEURL term [...]  -> count + first titles"""
import sys, re, html, time, urllib.request, urllib.parse
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
base = sys.argv[1].rstrip("/")
for term in sys.argv[2:]:
    u = base + "/index.php/informationobject/browse?topLod=0&sort=relevance&query=" + urllib.parse.quote(term)
    try:
        s = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=60).read().decode("utf8", "replace")
    except Exception as e:
        print("##", term, "ERR", e); continue
    t = html.unescape(re.sub(r"<[^>]+>", " ", s)); t = re.sub(r"\s+", " ", t)
    m = re.search(r"(Showing|Εμφανίζονται|Εμφάνιση)\s+([\d.,]+)\s+(results|αποτελ)", t) or re.search(r"([\d.,]+)\s+(results|αποτελέσματα)", t)
    print("##", term, "|", m.group(0) if m else "no count")
    for a, b in re.findall(r'<p class="title"><a href="([^"]+)"[^>]*>(.*?)</a>', s, re.S)[:int(10)]:
        print("   ", html.unescape(re.sub(r"<[^>]+>", "", b)).strip()[:150], "|", a)
    time.sleep(2.5)
