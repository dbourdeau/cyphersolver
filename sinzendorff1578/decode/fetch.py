"""Fetch DECODE record images (git-ignored) with the project cookie. Usage: python fetch.py 1590 1382 ..."""
import os, re, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
COOKIE = re.sub(r"^cookie:\s*", "", open(r"C:/Users/dbour/cypher/bordeaux/decode/cookie.txt", encoding="utf-8").read().strip(), flags=re.I)
def get(url, ck=True):
    h = {"User-Agent": UA}
    if ck: h["Cookie"] = COOKIE
    return urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=120).read()
for rec in sys.argv[1:]:
    p = os.path.join(HERE, "rec%s.htm" % rec)
    if not os.path.exists(p):
        open(p, "wb").write(get("https://de-crypt.org/decrypt-web/RecordsView/%s" % rec))
    html = open(p, encoding="utf-8", errors="ignore").read()
    names = sorted(set(re.findall(r"filesrv/\?file=TH_([A-Za-z0-9_.]+)", html)))
    docs = sorted(set(re.findall(r"filesrv/\?file=(DOC_[A-Za-z0-9_.]+)", html)))
    for n in names + docs:
        out = os.path.join(HERE, n)
        if os.path.exists(out): continue
        b = get("https://de-crypt.org/decrypt-custom/filesrv/?file=" + n)
        if len(b) == 17947: print("forbidden", n); continue
        open(out, "wb").write(b); print(rec, n, len(b)); time.sleep(0.5)
