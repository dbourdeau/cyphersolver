"""Hungaricana archives search (Viennese inventory regests) by curl-like requests, polite (1 req/s).
Usage: python -I -X utf8 hsearch.py "<query>" out.jsonl [maxpages] [sort e.g. RECNUM] [startpage] [stop_id]
Writes one JSON line per hit: id, ref, date, desc."""
import base64, json, re, sys, time, html, urllib.request

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode('utf8', 'replace')


def parse(t):
    out = []
    for blk in t.split('list-group-item bg-light mb-2 result')[1:]:
        m = re.search(r'lear/BecsSeg/(\d+)/[^>]*>\s*(.*?)\s*</a>', blk, re.S)
        if not m:
            continue
        d = re.search(r'Date of Creation</strong></td>\s*<td>(.*?)</td>', blk, re.S)
        s = re.search(r'Description:</strong>(.*?)</td>', blk, re.S)
        clean = lambda x: ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', x)).split()) if x else ''
        out.append({'id': int(m.group(1)), 'ref': clean(m.group(2)), 'date': clean(d.group(1) if d else ''),
                    'desc': clean(s.group(1) if s else '')})
    return out


def main():
    q, outp = sys.argv[1], sys.argv[2]
    maxp = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    sort = sys.argv[4] if len(sys.argv) > 4 else ''
    start = int(sys.argv[5]) if len(sys.argv) > 5 else 1
    stop_id = int(sys.argv[6]) if len(sys.argv) > 6 else 10**9
    lst = base64.b64encode(json.dumps(dict({'query': q}, **({'sort': sort} if sort else {}))).encode()).decode().rstrip('=')
    seen = set()
    with open(outp, 'w', encoding='utf8') as f:
        for p in range(start, start + maxp):
            url = f'https://archives.hungaricana.hu/en/lear/search/results/?list={lst}&per_page=100&page={p}'
            t = get(url)
            hits = parse(t)
            new = [h for h in hits if h['id'] not in seen]
            for h in new:
                seen.add(h['id'])
                f.write(json.dumps(h, ensure_ascii=False) + '\n')
            print(f'page {p}: {len(hits)} hits, {len(new)} new', flush=True)
            if len(hits) < 100 or not new or max(h['id'] for h in hits) > stop_id:
                break
            time.sleep(1.2)
    print('total', len(seen))


main()
