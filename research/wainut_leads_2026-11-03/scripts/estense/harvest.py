"""Harvest Lodovico manuscript search hits per term into hits.json (id -> titles, terms)."""
import json, re, sys, html, os, urllib.parse
from fetch import get
OUT = os.path.join(os.path.dirname(__file__), "hits.json")
hits = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
def page(term, p):
    field, _, val = term.partition("=") if "=" in term else ("keywords", "", term)
    q = urllib.parse.urlencode({"advanced": "1", field: val, "rictip": "documenti manoscritti"} if field != "keywords" else {"keywords": val, "rictip": "documenti manoscritti"})
    url = "https://lodovico.medialibrary.it/media/ricercadl.aspx?" + q + (f"&page={p}" if p > 1 else "")
    b = get(url)
    n = re.search(r'id="pager"[^>]*data-pages="(\d+)"', b)
    items = list(dict.fromkeys(re.findall(r'product-title" href="\.\./media/schedadl\.aspx\?id=([0-9a-f-]+)" itemprop="url" title="([^"]*)"', b)))
    tot = re.search(r'numresult">(\d+)<', b)
    return (int(n.group(1)) if n else 1), items
for term in sys.argv[1:]:
    pages, items = page(term, 1)
    allids = [i for i, _ in items]
    seen = set(allids)
    for p in range(2, min(pages, 15) + 1):
        _, it = page(term, p)
        new = [x for x in it if x[0] not in seen]
        if not new: print(term, "page", p, "no new ids; paging param wrong?"); break
        items += new; seen |= {i for i, _ in new}
    for i, t in items:
        h = hits.setdefault(i, {"title": html.unescape(t.strip()), "terms": []})
        if term not in h["terms"]: h["terms"].append(term)
    print(term, "pages", pages, "ids", len(seen))
    json.dump(hits, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
