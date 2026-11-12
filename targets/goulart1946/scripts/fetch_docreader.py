"""Fetch one DocReader page image by replaying the viewer's own image-load postback.
Usage: python fetch_docreader.py <bib> <pasta> <outprefix> [pagfis]"""
import sys, re, time, html
import requests
from html.parser import HTMLParser

UA = {"User-Agent": "WAINUT-research"}
bib, pasta, out = sys.argv[1], sys.argv[2], sys.argv[3]
pagfis = sys.argv[4] if len(sys.argv) > 4 else None
base = "https://www.docvirt.com/docreader.net/"
s = requests.Session(); s.headers.update(UA)
r = s.get(base + "docreader.aspx", params={"bib": bib, "pasta": pasta}, timeout=60)
print("GET", r.status_code, len(r.text))
page = r.text

class F(HTMLParser):
    def __init__(s2):
        super().__init__(); s2.fields = {}; s2.action = None
    def handle_starttag(s2, tag, a):
        a = dict(a)
        if tag == "form" and s2.action is None: s2.action = a.get("action")
        if tag == "input" and a.get("name") and a.get("type", "text").lower() in ("hidden", "text"):
            s2.fields[a["name"]] = a.get("value", "") or ""
f = F(); f.feed(page)
print("hPagFis", f.fields.get("hPagFis"), "action", f.action)
if pagfis: f.fields["hPagFis"] = pagfis
data = dict(f.fields)
data["__EVENTTARGET"] = ""; data["__EVENTARGUMENT"] = ""
data["CarregaImagemHiddenButton.x"] = "1"; data["CarregaImagemHiddenButton.y"] = "1"
time.sleep(2)
act = html.unescape(f.action or "docreader.aspx")
url = requests.compat.urljoin(r.url, act)
r2 = s.post(url, data=data, timeout=90)
print("POST", r2.status_code, len(r2.text))
open(out + "_post.html", "w", encoding="utf8").write(r2.text)
m = re.search(r'id="DocumentoImg"[^>]*src="([^"]*)"', r2.text) or re.search(r'<img[^>]*src="([^"]*)"[^>]*id="DocumentoImg"', r2.text)
print("img src:", m.group(1) if m else None)
if m and m.group(1):
    time.sleep(2)
    iu = requests.compat.urljoin(r2.url, html.unescape(m.group(1)))
    r3 = s.get(iu, timeout=90)
    print("IMG", r3.status_code, r3.headers.get("content-type"), len(r3.content))
    ext = ".jpg" if "jpeg" in (r3.headers.get("content-type") or "") else ".bin"
    open(out + ext, "wb").write(r3.content)
for kw in ("captcha", "Captcha"):
    for mm in re.finditer(kw + r"Abre\((\d*)", r2.text):
        print("captcha call:", r2.text[mm.start()-80:mm.end()+20])
