"""Harvest AEF friXplore (archives.fr.ch) hit rows for terms; keep Affry (de Boccard) 225-228 and 238 pieces.
usage: python -I -X utf8 frixplore.py OUTJSON term [term ...]"""
import sys, re, html, json, time, urllib.request, urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=90).read().decode("utf8", "replace")


ROW = re.compile(r"CH AEF Affry \(de Boccard\) (\d+)\.(\d+[a-z]?) ((?:(?!CH AEF|\.\.\.).)*?),? ?(\d{4}[^()]*?|s\.d\.)? \((Pièce|Dossier|Sous-dossier)\)")
out = sys.argv[1]
rows = {}
import os
os.makedirs('raw/frix', exist_ok=True)
for term in sys.argv[2:]:
    for page in range(1, 40):
        url = "https://archives.fr.ch/search/results?q=%s&scope=all&mode=table&page=%d&limit=80" % (urllib.parse.quote(term), page)
        t = get(url)
        open('raw/frix/%s_%02d.html' % (re.sub(r'\W+', '_', term), page), 'w', encoding='utf8').write(t)
        t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
        t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
        hits = ROW.findall(t)
        new = 0
        for ser, num, title, date, lvl in hits:
            k = "%s.%s" % (ser, num)
            if k not in rows:
                new += 1
                rows[k] = {"series": int(ser), "num": num, "title": title.strip(), "date": date, "level": lvl}
        print(term, page, len(hits), "new", new, flush=True)
        if not hits:
            break
        time.sleep(1.2)
json.dump(rows, open(out, "w", encoding="utf8"), ensure_ascii=False, indent=0)
print(len(rows))
