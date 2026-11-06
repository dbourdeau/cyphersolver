"""OPAC (opac.vatlib.it/mss) keyword harvester. Usage: python opac.py term1 term2 ...
Appends to hits.jsonl: {term, shelfmark, digitised, items:[(id,text)]}"""
import http.cookiejar, urllib.request, urllib.parse, re, json, sys, time, html, os

HERE = os.path.dirname(os.path.abspath(__file__))
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [('User-Agent', UA), ('Referer', 'https://opac.vatlib.it/mss/'), ('Accept-Language', 'en')]


def get(url):
    for k in range(3):
        try:
            r = op.open(url, timeout=60)
            return r.read().decode('utf-8', 'replace')
        except Exception as e:
            print('ERR', url, e, file=sys.stderr)
            time.sleep(5)
    return ''


def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


get('https://opac.vatlib.it/mss/')
time.sleep(1)


def search(term):
    out = []
    p = 1
    while True:
        q = urllib.parse.urlencode({'k_f': 0, 'k_v': term, 'r': 100, 'p': p})
        t = get('https://opac.vatlib.it/mss/search?' + q)
        time.sleep(1.1)
        m = re.search(r'([\d.,]+)\s*results found', clean(t))
        n = int(re.sub(r'\D', '', m.group(1))) if m else 0
        blocks = t.split('<div class="result">')[1:]
        for b in blocks:
            sm = re.search(r'<a href="/mss/detail/([^"]+)">', b)
            if not sm:
                continue
            dig = 'document-not-digitised' not in b
            items = re.findall(r'<a href="/mss/detail/(\d+)">(.*?)</a>', b, re.S)
            out.append({'term': term, 'shelfmark': sm.group(1), 'digitised': dig,
                        'items': [(i, clean(x)) for i, x in items]})
        if p * 100 >= n or not blocks or p >= 20:
            break
        p += 1
    return n, out


if __name__ == '__main__':
    with open(os.path.join(HERE, 'hits.jsonl'), 'a', encoding='utf-8') as f:
        for term in sys.argv[1:]:
            n, rows = search(term)
            print(f'{term!r}: {n} results, {len(rows)} rows', flush=True)
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + '\n')
            f.flush()
