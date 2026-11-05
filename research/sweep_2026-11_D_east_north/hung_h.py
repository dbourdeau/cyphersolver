"""Hungaricana server-rendered search harvest (plain requests). Output hung_hits.jsonl."""
import requests, re, sys, base64, json, time, html
sys.stdout.reconfigure(encoding='utf-8')
H = {'User-Agent':'Mozilla/5.0 (cyphersolver research sweep; polite)'}
b = lambda d: base64.urlsafe_b64encode(json.dumps(d).encode()).decode().rstrip('=')
terms = sys.argv[1:]
out = open('hung_hits.jsonl','a',encoding='utf-8')
def clean(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',s))).strip()
for term in terms:
    page=1; total=None
    while True:
        u = 'https://www.hungaricana.hu/hu/search/results/?list=%s&per_page=100&page=%d' % (b({'query':term}), page)
        for a in range(3):
            try:
                r = requests.get(u, headers=H, timeout=60); r.raise_for_status(); break
            except Exception as e:
                print('retry', e); time.sleep(6)
        t = r.text
        if total is None:
            m = re.search(r'(\d[\d\s \.]*)\s*találat', t)
            total = int(re.sub(r'\D','',m.group(1))) if m else 0
        items = re.split(r'<li class="list-group-item bg-light mb-2 result', t)[1:]
        for it in items:
            badge = re.search(r'badge bg-(\w+)[^>]*>([^<]+)<', it)
            href = re.search(r'<a href="([^"]+)"', it)
            title = re.search(r'<h5>.*?<a href="[^"]+">(.*?)</a>', it, re.S)
            strong = re.search(r'<strong>(.*?)</strong>', it, re.S)
            snip = re.search(r'font-size: \.9em;">(.*?)</div>', it, re.S)
            out.write(json.dumps({'term':term,'sect':badge.group(2).strip() if badge else '', 'href':href.group(1) if href else '',
               'title':clean(title.group(1)) if title else '', 'sub':clean(strong.group(1)) if strong else '', 'snip':clean(snip.group(1)) if snip else ''}, ensure_ascii=False)+'\n')
        print(term, page, len(items), total, flush=True)
        if not items or page*100 >= total or page >= 25: break
        page += 1
        time.sleep(2.5)
