"""python search.py <keyword> [...] : Durham XTF catalogue keyword search (reed.dur.ac.uk/xtf), all pages; then the hit
snippets inside each EAD finding aid -> raw/search_<kw>.json. One request a second."""
import re, os, sys, json, time, html, urllib.request, urllib.parse
here = os.path.dirname(os.path.abspath(__file__))
B = 'https://reed.dur.ac.uk/xtf/'
def get(u):
    time.sleep(1.0)
    return urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=120).read().decode('utf8', 'replace')
def clean(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()
for kw in sys.argv[1:]:
    q = urllib.parse.quote(kw)
    docs, start = [], 1
    while True:
        t = get(B + 'search?keyword=%s;startDoc=%d' % (q, start))
        found = re.findall(r'(\d+) hits?\s*</[^>]+>.*?<a href="(view\?docId=[^"]+)"[^>]*>(.*?)</a>', t, re.S)
        if not found:
            found = [(h, l, n) for l, n in re.findall(r'<a href="(view\?docId=[^";]+;query=[^"]*)"[^>]*>(.*?)</a>', t, re.S) for h in ['?']]
        new = [(h, l, clean(n)) for h, l, n in found if l not in [d[1] for d in docs]]
        docs += new
        m = re.search(r'Results:\s*</[^>]+>\s*<[^>]+>\s*(\d+)', t) or re.search(r'Results:\D*(\d+)', clean(t))
        total = int(m.group(1)) if m else len(docs)
        if not new or len(docs) >= total: break
        start += 20
    out = []
    for h, l, n in docs:
        rec = {'title': n, 'hits': h, 'link': B + l, 'snips': []}
        if l.startswith('view?docId=ark/'):
            try:
                v = clean(get(B + l.split('#')[0].replace(' ', '%20')))
                i0 = v.find('Clear Hits') + 10
                pat = re.compile(r'(?i)\b' + r'\W+'.join(map(re.escape, kw.split())))
                for m in pat.finditer(v, i0):
                    rec['snips'].append(v[max(0, m.start() - 350):m.end() + 250])
            except Exception as e:
                rec['snips'].append('ERR %s' % e)
        out.append(rec); print(kw, '|', h, '|', n, '|', l, '|', len(rec['snips']), flush=True)
    json.dump(out, open(os.path.join(here, 'raw', 'search_%s.json' % re.sub(r'\W+', '_', kw)), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
