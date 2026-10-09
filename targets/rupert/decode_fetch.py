"""Fetch DECODE record pages + API views for the Rupert / Add MS 72438 / 18980-83 records (cookie from bordeaux).
Pages embed a session token: saved under decode/ (git-ignored). Usage: python decode_fetch.py pages|files <ids...>|list"""
import os, re, sys, json, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(HERE, "decode")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
op = urllib.request.build_opener(urllib.request.ProxyHandler({}))
CK = open(os.path.join(ROOT, "targets", "bordeaux", "decode", "cookie.txt"), encoding="utf-8").read().strip()
def get(url, hdr=None):
    h = {"User-Agent": UA, "Cookie": CK}; h.update(hdr or {})
    return op.open(urllib.request.Request(url, headers=h), timeout=120).read()
def ids():
    L = json.load(open(os.path.join(ROOT, "research", "catalogue_harvest", "decode", "list.json"), encoding="utf-8"))
    return [r["id"] for r in L if re.search(r"7243[0-9]|1898[0-3]", r["c_holder"] or "")]
def page(i):
    p = os.path.join(D, "rec%s.htm" % i)
    if not (os.path.exists(p) and os.path.getsize(p) > 3000):
        open(p, "wb").write(get("https://de-crypt.org/decrypt-web/RecordsView/%s" % i)); time.sleep(0.4)
    return open(p, encoding="utf-8", errors="replace").read()
def files(t):
    im = sorted(set(re.findall(r"TH_(IMG_[A-Za-z0-9_.]+)", t)))
    dc = sorted(set(re.findall(r"(DOC_R[0-9]+_[A-Za-z0-9_.]+)", t)))
    return im, dc
def fetch(name, sub="img"):
    p = os.path.join(HERE, sub, name)
    if os.path.exists(p) and os.path.getsize(p) != 17947: return p
    b = get("https://de-crypt.org/decrypt-custom/filesrv/?file=" + name)
    open(p, "wb").write(b); time.sleep(0.3)
    if len(b) == 17947: print("FORBIDDEN", name)
    return p
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "pages":
        tok = None; out = []
        for i in ids():
            t = page(i)
            if tok is None: tok = re.search(r'"API_JWT_TOKEN":"([^"]+)"', t).group(1)
            vp = os.path.join(D, "view%s.json" % i)
            if not os.path.exists(vp):
                open(vp, "wb").write(get("https://de-crypt.org/decrypt-web/api/view/Records/%s" % i, {"X-Authorization": "Bearer " + tok})); time.sleep(0.3)
            print(i, len(t), *[len(x) for x in files(t)], flush=True)
    elif cmd == "files":
        for i in sys.argv[2:]:
            im, dc = files(page(i))
            for n in dc: print(fetch(n, "decode"), os.path.getsize(fetch(n, "decode")))
            for n in im: print(fetch(n), os.path.getsize(fetch(n)))
