"""Manus Online: fetch detail records by id -> raw/manus_detail/<id>.json; print cipher-context snippets."""
import json, os, re, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "raw", "manus_detail"); os.makedirs(D, exist_ok=True)
RX = re.compile(r"cifr|decifr|critt|cript|segret|zifer|furtiv|convenzional", re.I)
def flat(o, out):
    if isinstance(o, dict):
        for v in o.values(): flat(v, out)
    elif isinstance(o, list):
        for v in o: flat(v, out)
    elif isinstance(o, str): out.append(o)
for i in sys.argv[1:]:
    p = os.path.join(D, i + ".json")
    if not os.path.exists(p):
        time.sleep(1.1)
        req = urllib.request.Request("https://manus.iccu.sbn.it/o/manus-api/title?id=" + i, headers={"User-Agent": "Mozilla/5.0", "X-Requested-With": "XMLHttpRequest"})
        open(p, "wb").write(urllib.request.urlopen(req, timeout=60).read())
    out = []; flat(json.load(open(p, encoding="utf8"), strict=False), out)
    txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", " ¦ ".join(out)))
    print("=====", i, txt[:160])
    seen = set()
    for m in RX.finditer(txt):
        s = txt[max(0, m.start() - 220): m.end() + 260]
        k = m.start() // 300
        if k in seen: continue
        seen.add(k); print("   ..", s)
