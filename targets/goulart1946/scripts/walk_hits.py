"""Search a DocReader collection and step through every hit with the viewer's own 'next hit' postback.
Prints hit number, physical page (pagfis) and folder (pasta) per hit. Usage: python walk_hits.py <bib> <term> [max]"""
import sys, re, time, html, requests
from html.parser import HTMLParser
bib, term = sys.argv[1:3]; mx = int(sys.argv[3]) if len(sys.argv) > 3 else 12
base = "https://www.docvirt.com/docreader.net/docreader.aspx"
s = requests.Session(); s.headers["User-Agent"] = "WAINUT-research"
class F(HTMLParser):
    def __init__(a): super().__init__(); a.f = {}; a.act = None
    def handle_starttag(a, t, at):
        at = dict(at)
        if t == "form" and a.act is None: a.act = at.get("action")
        if t == "input" and at.get("name") and at.get("type", "text").lower() in ("hidden", "text"):
            a.f[at["name"]] = at.get("value") or ""
def form(t):
    p = F(); p.feed(t); return p
def info(t):
    pf = re.findall(r'id="hPagFis"[^>]*value="(\d+)"', t)
    oc = re.findall(r'id="OcorNroLbl"[^>]*>([^<]*)', t)
    pasta = re.findall(r'(GV c [0-9./]+)', t)
    img = re.findall(r'(cache/[0-9]+/I\d+[^"]*\.JPG)', t)
    return pf, oc, sorted(set(pasta))[:3], img[:1]
r = s.get(base, params={"bib": bib}, timeout=60)
p = form(r.text); url = requests.compat.urljoin(r.url, html.unescape(p.act))
d = dict(p.f); d.update({"PesquisarTxt": term, "PesquisarBtn_input": "Pesquisar", "__EVENTTARGET": "", "__EVENTARGUMENT": ""})
time.sleep(2); r = s.post(url, data=d, timeout=90); print(1, info(r.text)); sys.stdout.flush()
for i in range(2, mx + 1):
    p = form(r.text); d = dict(p.f); d.update({"__EVENTTARGET": "", "__EVENTARGUMENT": "", "OcorPosBtn.x": "1", "OcorPosBtn.y": "1"})
    url = requests.compat.urljoin(r.url, html.unescape(p.act))
    time.sleep(2); r = s.post(url, data=d, timeout=90)
    if r.status_code != 200: print("stop", r.status_code); break
    print(i, info(r.text)); sys.stdout.flush()
