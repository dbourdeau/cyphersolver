"""JACAR (Japan Center for Asian Historical Records) search client.

/aj/search is server-rendered, so plain GET works (no login). Parameters seen: kw, page, rows (20/50/100/200),
sf (seq_a, reference_a, date_a, date_d, inst_a), f_date, f_inst, f_type, f_datatype ...
"""
import re, sys, time, html, json, urllib.request, urllib.parse

BASE = "https://www.jacar.archives.go.jp"
UA = {"User-Agent": "Mozilla/5.0 (cyphersolver research; dnbourdeau@gmail.com)"}


def get(url, tries=5):
    err = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return r.read().decode("utf8", "replace")
        except Exception as e:
            err = e
            time.sleep(3 * (i + 1))
    raise err


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def fetch(kw, page=1, rows=200, sf="reference_a", **extra):
    q = {"kw": kw, "page": page, "rows": rows, "sf": sf}
    q.update(extra)
    return get(BASE + "/aj/search?" + urllib.parse.urlencode(q))


def parse(t):
    m = re.search(r'data-count="(\d+)"', t)
    total = int(m.group(1)) if m else None
    hits = []
    for blk in t.split('archive-result-table__body-item" role="row"')[1:]:
        h = {}
        m = re.search(r'cmn-category-label__text">([^<]+)<', blk)
        h["level"] = m.group(1) if m else ""
        m = re.search(r'result-header__title">\s*<a href="[^"]*/das/meta/([A-Z0-9]+)"[^>]*>(.*?)</a>', blk, re.S)
        if not m:
            continue
        h["id"], h["title"] = m.group(1), clean(m.group(2))
        tree = re.findall(r'result-tree__item-label">\s*<a [^>]*>(.*?)</a>', blk, re.S)
        h["tree"] = [clean(x) for x in tree]
        for lab, val in re.findall(r'result-summary__label">\[<span >(.*?)</span>\]</dt>\s*<dd[^>]*>(.*?)</dd>', blk, re.S):
            h[lab] = clean(val)
        m = re.search(r'レファレンスコード</span>\]</dt>\s*<dd[^>]*>\s*<span >(\w+)', blk)
        h["ref"] = m.group(1) if m else h["id"]
        m = re.search(r'href="(https://www.digital.archives.go.jp[^"]+|[^"]*/aj/img[^"]*|[^"]*viewer[^"]*)"', blk)
        h["image"] = m.group(1) if m else ""
        hits.append(h)
    return total, hits


def harvest(kw, maxpages=60, **extra):
    total, allh = None, []
    for p in range(1, maxpages + 1):
        t = fetch(kw, p, **extra)
        total, hs = parse(t)
        if not hs:
            break
        allh += hs
        if len(allh) >= total:
            break
        time.sleep(1.0)
    return total, allh


if __name__ == "__main__":
    kw = sys.argv[1]
    t = fetch(kw, 1, rows=20)
    total, hs = parse(t)
    print(total, len(hs))
    for h in hs[:5]:
        print(json.dumps(h, ensure_ascii=False)[:500])
