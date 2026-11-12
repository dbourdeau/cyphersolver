"""Run one DocReader full-text (OCR) search in a collection by replaying the viewer's search postback.
Usage: python search_docreader.py <bib> <term> <outfile.html>"""
import sys, re, time, html, requests
from html.parser import HTMLParser
bib, term, out = sys.argv[1:4]
base = "https://www.docvirt.com/docreader.net/docreader.aspx"
s = requests.Session(); s.headers["User-Agent"] = "WAINUT-research"
r = s.get(base, params={"bib": bib}, timeout=60)
class F(HTMLParser):
    def __init__(a): super().__init__(); a.f = {}; a.act = None
    def handle_starttag(a, t, at):
        at = dict(at)
        if t == "form" and a.act is None: a.act = at.get("action")
        if t == "input" and at.get("name") and at.get("type", "text").lower() in ("hidden", "text"):
            a.f[at["name"]] = at.get("value") or ""
p = F(); p.feed(r.text)
d = dict(p.f); d["PesquisarTxt"] = term; d["PesquisarBtn_input"] = "Pesquisar"
d["__EVENTTARGET"] = ""; d["__EVENTARGUMENT"] = ""
time.sleep(2)
r2 = s.post(requests.compat.urljoin(r.url, html.unescape(p.act or "docreader.aspx")), data=d, timeout=90)
open(out, "w", encoding="utf8").write(r2.text)
t = r2.text
print("POST", r2.status_code, len(t))
for pat in [r'id="Ocorr[^"]*"[^>]*>[^<]*', r'(?i)ocorr[eê]ncia[^<]{0,80}', r'(?i)[^<>]{0,60}encontrad[^<]{0,80}', r'id="PagTotalLbl"[^>]*>[^<]*', r'id="hPagFis"[^>]*value="\d+"', r'(?i)pasta[^<]{0,10}GV c [0-9./]+']:
    for m in re.findall(pat, t)[:8]: print("  ", m)
