"""Harvest Alvin's OAI-PMH feed (oai_dc) and keep records whose text matches a cipher term.
Alvin's HTML search is behind Anubis; the OAI endpoint is the published machine route.
usage: python3 alvin_oai.py <outdir>   (resumes from <outdir>/token.txt)"""
import sys, re, time, json, os, urllib.request, html
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
BASE = "https://www.alvin-portal.org/oai/oai"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"}
PAT = re.compile(r"chiff|ziffer|cipher|cypher|cifr|lönnskrift|lönskrift|hemlig skrift|kryptogra|krypter|dechiff|geheimschrift|chifr|salakirjoit|cryptogr|steganogr|i siffror|sifferskrift|siffer", re.I)
tokf = os.path.join(out, "token.txt")
tok = open(tokf).read().strip() if os.path.exists(tokf) else None
n = int(tok.split("/")[3]) if tok else 0; hits = 0
while True:
    url = BASE + ("?verb=ListRecords&resumptionToken=" + urllib.request.quote(tok) if tok else "?verb=ListRecords&metadataPrefix=oai_dc")
    for attempt in range(5):
        try:
            x = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read().decode("utf-8", "replace"); break
        except Exception as e:
            print("err", e, flush=True); time.sleep(20)
    else:
        sys.exit("gave up")
    recs = re.findall(r"<record>.*?</record>", x, re.S)
    n += len(recs)
    with open(os.path.join(out, "hits.jsonl"), "a") as f:
        for r in recs:
            if PAT.search(r):
                hits += 1; f.write(json.dumps({"xml": html.unescape(r)}, ensure_ascii=False) + "\n")
    m = re.search(r"<resumptionToken[^>]*>([^<]*)</resumptionToken>", x)
    print(n, hits, m.group(0)[:120] if m else None, flush=True)
    if not m or not m.group(1): break
    # the token is <stamp>/alvin/oai_dc/<cursor>/<page size>/...; size 1000 is accepted, but the server then only
    # advances its own cursor by 100, so the cursor is set here from the number of records received
    stamp = html.unescape(m.group(1)).split("/")[0]
    tok = "%s/alvin/oai_dc/%d/1000/set/from/until/" % (stamp, n); open(tokf, "w").write(tok)
    if n >= 700000: break
    time.sleep(2.5)
