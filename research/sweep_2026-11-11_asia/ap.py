"""Abhilekh Patal (abhilekh-patal.in) search client, Oct 2026 sweep.

The portal (ASP.NET Core front end over a DSpace 7 backend) serves search results as HTML:
  /Category/Search/AdvanceSearchV3?<field>=<value>,<op>   first page (10 items) + Page.TotalElements
  /Category/Search/PaginationScroll?<same params>&Number=N JSON {"partialView": html} for page N
Fields: title, recordContains, keywords, subject, series, identifier, ... ; op: contains | equals.
The plain QuerySearch?query= route applies fuzzy matching (term~0.7), so it is not used for counting.
Size is fixed at 10 per page by the server.

usage: python ap.py <outfile.jsonl> <param=value> [...] [--max-pages N] [--start N]
Sorted by dc.title,asc (the default accession sort repeats items across pages). 4 s between pages:
faster parallel harvesting drew HTTP 403 from the CloudFront WAF on 28 Oct 2026.
"""
import html as H
import json
import re
import sys
import time
import urllib.parse
import urllib.request

BASE = 'https://www.abhilekh-patal.in/Category/Search/'
DELAY = int(__import__("os").environ.get("AP_DELAY", "4"))
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'


def get(url, xhr=False, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, **({'X-Requested-With': 'XMLHttpRequest'} if xhr else {})})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read().decode('utf8', 'replace')
        except Exception as e:
            print('retry', i, e, file=sys.stderr)
            if '403' in str(e):
                raise SystemExit('403 from the portal (WAF rate limit): stopping')
            time.sleep(5 * (i + 1))
    return ''


def parse(h):
    h = re.sub(r'data:image[^"]+', '', h)
    out = []
    # each card: heading link then viewgrid fields
    for m in re.finditer(r'<li class="headingview[^"]*">\s*<a href="/Category/ItemDetails/ItemDetails\?itemId=([0-9a-f-]+)">(.*?)</a>(.*?)(?=<li class="headingview|$)', h, re.S):
        iid, title, rest = m.group(1), m.group(2), m.group(3)[:6000]
        title = H.unescape(re.sub(r'<[^>]+>', '', title)).strip()
        rec = {'itemId': iid, 'title': re.sub(r'\s+', ' ', title)}
        for f in re.finditer(r'<span class="pleft">\s*([^<:]+):?\s*</span>(.*?)</li>', rest, re.S):
            k = f.group(1).strip()
            v = H.unescape(re.sub(r'<[^>]+>', ' ', f.group(2)))
            rec[k] = re.sub(r'\s+', ' ', v).strip()
        out.append(rec)
    return out


def total(h):
    m = re.search(r'name="Page\.TotalElements" value="(\d+)"', h)
    return int(m.group(1)) if m else -1


def run(outfile, params, max_pages=1000, start=1):
    params.setdefault('sort', 'dc.title,asc')  # default sort is unstable across pages
    qs = urllib.parse.urlencode(params)
    h = get(BASE + 'AdvanceSearchV3?' + qs)
    n = total(h)
    recs = parse(h)
    print(params, 'total', n, file=sys.stderr)
    seen = set()
    with open(outfile, 'a', encoding='utf8') as f:
        def dump(rs, page):
            for r in rs:
                if r['itemId'] in seen:
                    continue
                seen.add(r['itemId'])
                r['_q'] = qs
                r['_page'] = page
                f.write(json.dumps(r, ensure_ascii=False) + '\n')
        dump(recs, 0)
        pages = min((n + 9) // 10, max_pages)
        for p in range(start, pages):
            t = get(BASE + 'PaginationScroll?' + qs + f'&number={p}&viewtype=list', xhr=True)
            try:
                pv = json.loads(t).get('partialView', '')
            except Exception:
                pv = ''
            rs = parse(pv)
            if not rs:
                print('empty page', p, file=sys.stderr)
            dump(rs, p)
            f.flush()
            time.sleep(DELAY)
    return n, len(seen)


if __name__ == '__main__':
    out = sys.argv[1]
    mp = 1000
    st = 1
    args = sys.argv[2:]
    if '--start' in args:
        i = args.index('--start'); st = int(args[i + 1]); del args[i:i + 2]
    if '--max-pages' in args:
        i = args.index('--max-pages'); mp = int(args[i + 1]); del args[i:i + 2]
    params = dict(a.split('=', 1) for a in args)
    print(run(out, params, mp, st))
