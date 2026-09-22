"""Fetch DOC_ transcriptions of the G15 key records (cookie kept out of the repo)."""
from pathlib import Path
import re, sys, urllib.request
ROOT = Path(__file__).resolve().parent / "keys"
BASE = "https://de-crypt.org"
cookie = re.sub(r"^cookie:\s*", "", Path(r"C:/Users/dbour/cypher/bordeaux/decode/cookie.txt").read_text(encoding="utf-8").strip(), flags=re.I)
def get(url, ref=None):
    h = {"User-Agent": "Mozilla/5.0", "Cookie": cookie}
    if ref: h["Referer"] = ref
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=90) as r:
        return r.read()
ids = [int(x) for x in sys.argv[1:]]
for rid in ids:
    url = f"{BASE}/decrypt-web/RecordsView/{rid}"
    try: html = get(url)
    except Exception as e: print(rid, "ERR", e); continue
    for n in sorted(set(re.findall(rb"file=(DOC_R%d_[A-Za-z0-9_.]+)" % rid, html))):
        n = n.decode(); out = ROOT / n
        if out.exists(): continue
        d = get(f"{BASE}/decrypt-custom/filesrv/?file={n}", url)
        if len(d) == 17947: print("forbidden"); sys.exit(1)
        out.write_bytes(d); print(rid, n, len(d))
