"""Saxon State Archives (archiv.sachsen.de) cps/suche.html harvest. usage: sax_harvest.py OUT.jsonl term..."""
import sys, re, json, time, html, urllib.parse, requests
S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0'
out = open(sys.argv[1], 'a', encoding='utf-8')
def strip(s): return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()
for term in sys.argv[2:]:
    off = 1; total = None; n = 0
    while True:
        u = 'https://www.archiv.sachsen.de/cps/suche.html?q=%s&offset=%d&pagesize=10' % (urllib.parse.quote(term), off)
        r = S.get(u, timeout=60)
        if r.status_code != 200:
            print('STOP', r.status_code, term, off); break
        t = r.text
        m = re.search(r'<h2>([\d.]+) Ergebnisse', t)
        if m and total is None: total = int(m.group(1).replace(".","")); print(term, total, flush=True)
        blocks = t.split('<div class="box box-bordered">')[1:]
        cnt = 0
        for b in blocks:
            a = re.search(r'<a href="(/archiv/bestand\.jsp\?guid=[^"]+)">(.*?)</a>', b, re.S)
            if not a: continue
            d = re.search(r'search-result-date.*?<td>(.*?)</td>', b, re.S)
            c = re.search(r'search-result-content">(.*?)</div>\s*</div>\s*</div>\s*</div>', b, re.S)
            row = dict(term=term, href=a.group(1), sig=strip(a.group(2)), date=strip(d.group(1)) if d else '',
                       text=strip(c.group(1)) if c else strip(b), scan='glyphicon-camera' in b)
            out.write(json.dumps(row, ensure_ascii=False) + '\n'); cnt += 1
        n += cnt; out.flush()
        if cnt == 0 or total is None or off + 10 > total: break
        off += 10; time.sleep(2.5)
    print(term, 'got', n, flush=True); time.sleep(2.5)
