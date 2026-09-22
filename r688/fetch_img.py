"""Fetch DECODE record pages, DOC transcriptions and images (cookie kept out of the repo)."""
from pathlib import Path
import re, sys, urllib.request
ROOT = Path(__file__).resolve().parent
BASE = "https://de-crypt.org"
cookie = re.sub(r"^cookie:\s*", "", (Path(r"C:/Users/dbour/cypher/bordeaux")/"decode"/"cookie.txt").read_text(encoding="utf-8").strip(), flags=re.I)
def get(url, ref=None):
    h = {"User-Agent": "Mozilla/5.0", "Cookie": cookie}
    if ref: h["Referer"] = ref
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=90) as r:
        d = r.read()
    if len(d) == 17947: raise RuntimeError("cookie rejected")
    return d
for rid in map(int, sys.argv[1:]):
    url = f"{BASE}/decrypt-web/RecordsView/{rid}"
    html = get(url)
    (ROOT/"img").mkdir(exist_ok=True)
    (ROOT/"img"/f"rec{rid}.htm").write_bytes(html)
    names = sorted(set(re.findall(rb"file=((?:DOC|IMG)_R%d_[A-Za-z0-9_.]+)" % rid, html)))
    for n in names:
        n = n.decode()
        if n.startswith("IMG") and not n.endswith("_P.jpg") and "TH_" in n: continue
        out = (ROOT if n.startswith("DOC") else ROOT/"img")/n
        if out.exists(): continue
        out.write_bytes(get(f"{BASE}/decrypt-custom/filesrv/?file={n}", url))
        print(rid, n, out.stat().st_size)
