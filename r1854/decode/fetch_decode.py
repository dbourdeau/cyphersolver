"""Download the DECODE files listed in MANIFEST.md using a logged-in browser cookie.

Usage:  python fetch_decode.py            (all records in MANIFEST order)
        python fetch_decode.py 7537 8390  (selected records)
Needs:  cookie.txt in this folder = the value of the Cookie: header of a de-crypt.org request made
        while logged in (browser dev tools, Network tab, any request to de-crypt.org, copy the
        whole "Cookie:" request header). Delete cookie.txt when done; it is git-ignored.

Alternative without a cookie: log in in the browser, open each RecordsView page below, click each
page image, save the full-size file into this folder under its DECODE name (the thumbnail name
without the TH_ prefix, e.g. IMG_R7537_I34037_P1.jpg). The scripts that follow look for those names.

A download that comes back as the 17947-byte "forbidden.png" placeholder (what the server returns
without a valid session) is deleted and reported.
"""
import glob
import os
import re
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://de-crypt.org"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
FORBIDDEN_LEN = 17947
ORDER = [7537, 8390, 8392, 8391, 8393, 8389, 8386, 8388]


def files_for(rec):
    """Full-image names from the saved public RecordsView page rec<id>.htm (thumbnail names minus TH_)."""
    p = os.path.join(HERE, "rec%d.htm" % rec)
    if not os.path.exists(p):
        req = urllib.request.Request(BASE + "/decrypt-web/RecordsView/%d" % rec, headers={"User-Agent": UA})
        open(p, "wb").write(urllib.request.build_opener(urllib.request.ProxyHandler({})).open(req, timeout=60).read())
    html = open(p, encoding="utf-8", errors="ignore").read()
    names = sorted(set(re.findall(r"filesrv/\?file=TH_([A-Za-z0-9_.]+)", html)))
    return names


def load_cookie():
    p = os.path.join(HERE, "cookie.txt")
    if not os.path.exists(p):
        sys.exit("cookie.txt not found next to this script; see the docstring / MANIFEST.md")
    c = open(p, encoding="utf-8").read().strip()
    return re.sub(r"^cookie:\s*", "", c, flags=re.I)


def fetch(name, cookie, rec):
    out = os.path.join(HERE, name)
    if os.path.exists(out) and os.path.getsize(out) not in (0, FORBIDDEN_LEN):
        return "have"
    req = urllib.request.Request(BASE + "/decrypt-custom/filesrv/?file=" + name, headers={
        "User-Agent": UA, "Cookie": cookie,
        "Referer": BASE + "/decrypt-web/RecordsView/%d" % rec,
    })
    # bypass any local HTTPS proxy setting (the PromptSecurity proxy on 127.0.0.1:3636 is not always up)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(req, timeout=180) as r:
        data = r.read()
        disp = r.headers.get("Content-Disposition", "")
    if len(data) == FORBIDDEN_LEN or "forbidden" in disp:
        return "FORBIDDEN (cookie not accepted)"
    with open(out, "wb") as f:
        f.write(data)
    return "%d bytes" % len(data)


def main():
    recs = [int(a) for a in sys.argv[1:]] or ORDER
    cookie = load_cookie()
    bad = 0
    for rec in recs:
        for name in files_for(rec):
            try:
                res = fetch(name, cookie, rec)
            except Exception as e:  # noqa: BLE001
                res = "ERROR %s" % e
            print("R%d %-28s %s" % (rec, name, res))
            if res.startswith("FORBIDDEN"):
                sys.exit("session cookie rejected; copy a fresh Cookie header into cookie.txt")
            if res.startswith("ERROR"):
                bad += 1
            time.sleep(0.5)
    print("done, %d failures" % bad)
    have = [f for f in glob.glob(os.path.join(HERE, "IMG_*")) if os.path.getsize(f) > FORBIDDEN_LEN]
    print("%d full images present" % len(have))


if __name__ == "__main__":
    main()
