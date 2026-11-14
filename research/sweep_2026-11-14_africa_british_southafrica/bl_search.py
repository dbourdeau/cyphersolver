"""British Library interim Archives & Manuscripts Catalogue (searcharchives.bl.uk), plain curl.
python bl_search.py "<query>" ...   ->  bl_hits.jsonl (query, shelfmark, text) and a count line per query. 2.5 s between requests."""
import re, subprocess, sys, html, time, urllib.parse, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def page(q, p):
    u = "https://searcharchives.bl.uk/?search_field=all_fields&per_page=100&page=%d&q=%s" % (p, urllib.parse.quote(q))
    t = subprocess.run(["curl", "-s", "-m", "60", "-A", "Mozilla/5.0", u], capture_output=True).stdout.decode("utf8", "replace")
    txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", "", t, flags=re.S | re.I))))
    m = re.search(r"([\d,]+) - ([\d,]+) of ([\d,]+)", txt)
    tot = int(m.group(3).replace(",", "")) if m else 0
    parts = re.split(r"(?<=[\s])(\d{1,3})\. (?=[A-Z][A-Za-z.]* ?[A-Za-z]* ?[\d/]*[^ ]* Reference \(shelfmark\))", txt)
    rows = []
    for blk in re.findall(r"\d{1,3}\. (.{0,40}?) Reference \(shelfmark\): (.*?)(?= \d{1,3}\. [^ ]+.{0,40}? Reference \(shelfmark\)| « Previous|$)", txt):
        rows.append((blk[0].strip(), blk[1][:900]))
    return tot, rows, txt
if __name__ == "__main__":
    out = open(os.path.join(HERE, "bl_hits.jsonl"), "a", encoding="utf8")
    for q in sys.argv[1:]:
        tot, rows, _ = page(q, 1); allr = list(rows); p = 1
        while len(allr) < tot and p < 5 and rows:
            p += 1; time.sleep(2.5); _, rows, _ = page(q, p); allr += rows
        print(f"{q!r}: total {tot}, parsed {len(allr)}", flush=True)
        for sm, tx in allr:
            out.write(json.dumps({"q": q, "shelfmark": sm, "text": tx}, ensure_ascii=False) + "\n")
        time.sleep(2.5)
