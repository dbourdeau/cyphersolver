"""Harvest one Alvin OAI-PMH set in ksamsok-rdf (full description, shelfmark, attachment count) into a compact jsonl.
usage: python3 harvest_rdf.py <outdir> [set]   (default set: manuscript; resumes from <outdir>/token_<set>.txt)
The token is <stamp>/alvin/ksamsok-rdf/<cursor>/<size>/<set>/from/until/; size 1000 is honoured, the cursor is set here."""
import sys, re, time, json, os, urllib.request, html
out = sys.argv[1]; SET = sys.argv[2] if len(sys.argv) > 2 else "manuscript"; os.makedirs(out, exist_ok=True)
BASE = "https://www.alvin-portal.org/oai/oai"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"}
tokf = os.path.join(out, "token_%s.txt" % SET)
n = int(open(tokf).read().strip()) if os.path.exists(tokf) else 0
stamp = str(int(time.time() * 1000) + 3600000)
def g(p, r, fl=re.S): return [html.unescape(re.sub(r"\s+", " ", m)).strip() for m in re.findall(p, r, fl)]
while True:
    url = BASE + "?verb=ListRecords&resumptionToken=" + urllib.request.quote("%s/alvin/ksamsok-rdf/%d/1000/%s/from/until/" % (stamp, n, SET))
    for attempt in range(6):
        try:
            x = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=300).read().decode("utf-8", "replace"); break
        except Exception as e:
            print("err", e, flush=True); time.sleep(30)
    else: sys.exit("gave up")
    recs = re.findall(r"<record>.*?</record>", x, re.S)
    with open(os.path.join(out, "rdf_%s.jsonl" % SET), "a") as f:
        for r in recs:
            d = {"id": (g(r"<identifier>oai:ALVIN.org:(\d+)", r) or [""])[0], "sets": g(r"<setSpec>(.*?)</setSpec>", r),
                 "title": (g(r"<itemTitle>(.*?)</itemTitle>", r) or g(r"<itemLabel>(.*?)</itemLabel>", r) or [""])[0],
                 "nimg": len(re.findall(r"<image rdf:nodeID", r)),
                 "names": (g(r"<pres:nameLabel>(.*?)</pres:nameLabel>", r) or [""])[0],
                 "time": (g(r"<pres:timeLabel>(.*?)</pres:timeLabel>", r) or g(r"<timeText>(.*?)</timeText>", r) or [""])[0],
                 "place": (g(r"<pres:placeLabel>(.*?)</pres:placeLabel>", r) or [""])[0],
                 "tag": g(r"<pres:tag>(.*?)</pres:tag>", r), "partof": g(r"<isPartOf>.*?/(\d+)</isPartOf>", r),
                 "lang": g(r"language_code.html#(\w+)", r), "type": (g(r"<pres:type>(.*?)</pres:type>", r) or [""])[0],
                 "num": [b for a, b in re.findall(r"<itemNumber rdf:nodeID=\"[^\"]+\">\s*<type>(.*?)</type>\s*<number>(.*?)</number>", r, re.S) if a != "URN"],
                 "desc": [[html.unescape(a), html.unescape(re.sub(r"\s+", " ", b))[:600]] for a, b in re.findall(r"<itemDescription rdf:nodeID=\"[^\"]+\">\s*<type>(.*?)</type>\s*<desc>(.*?)</desc>", r, re.S) if a not in ("Katalogiseringsspråk",)],
                 "meas": g(r"<itemMeasurement rdf:nodeID=\"[^\"]+\">.*?<value>(.*?)</value>", r)}
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    n += len(recs); open(tokf, "w").write(str(n))
    m = re.search(r'completeListSize="(\d+)"', x)
    print(n, m.group(1) if m else None, flush=True)
    if not recs or not m or n >= int(m.group(1)): break
    time.sleep(2.5)
