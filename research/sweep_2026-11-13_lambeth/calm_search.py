"""Lambeth Palace Library CalmView: run "Any Text" searches through advanced.aspx and save the result lists.

    python research/sweep_2026-11-13_lambeth/calm_search.py <outdir> term [term ...]

For each term: GET advanced.aspx (fresh __VIEWSTATE), POST the form, then follow the pager, one request every 3 s.
Writes <outdir>/<term>_p<n>.html (outside the repository) and prints the hit count and one line per record.
Uses curl (browser User-Agent, cookie jar) because the session proxy is configured for it.
"""
import html, os, re, subprocess, sys, time

BASE = 'https://archives.lambethpalacelibrary.org.uk/CalmView/'
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
ANY = 'ctl00$main$DSCoverySearch1$ctl03$SearchText$AnyText_default'
BTN = 'ctl00$main$DSCoverySearch1$ctl01$Button1'


def curl(out, url, jar, data=None, referer=None):
    cmd = ['curl', '-sS', '-A', UA, '-b', jar, '-c', jar, '-m', '60', '-L', '-o', out, '-w', '%{http_code} %{url_effective}']
    if referer:
        cmd += ['-e', referer]
    for k, v in (data or {}).items():
        cmd += ['--data-urlencode', f'{k}={v}']
    r = subprocess.run(cmd + [url], capture_output=True, text=True)
    time.sleep(3)
    code, _, eff = r.stdout.partition(' ')
    return code, eff, open(out, encoding='utf-8', errors='replace').read() if os.path.exists(out) else ''


def hidden(page):
    return {m.group(1): html.unescape(m.group(2))
            for m in re.finditer(r'<input type="hidden" name="([^"]+)"[^>]*value="([^"]*)"', page)}


def rows(page):
    out = []
    for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', page, re.S):
        m = re.search(r'Record\.aspx\?src=CalmView\.Catalog&(?:amp;)?id=([^"&]+)', tr)
        if not m:
            continue
        cells = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', c))).strip()
                 for c in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)]
        out.append((html.unescape(m.group(1)), cells))
    return out


def main(outdir, terms):
    os.makedirs(outdir, exist_ok=True)
    jar = os.path.join(outdir, 'jar.txt')
    for term in terms:
        safe = re.sub(r'\W+', '_', term)
        code, eff, form = curl(os.path.join(outdir, f'{safe}_form.html'), BASE + 'advanced.aspx?src=CalmView.Catalog', jar)
        if code != '200':
            print(f'== {term}: form HTTP {code}; stopping on this host')
            return
        data = hidden(form)
        data[ANY] = term
        data[BTN] = 'Search'
        code, eff, page = curl(os.path.join(outdir, f'{safe}_p1.html'), BASE + 'advanced.aspx?src=CalmView.Catalog', jar,
                               data, BASE + 'advanced.aspx?src=CalmView.Catalog')
        m = re.search(r'(\d+)\s+records?\b|of\s+(\d+)', page)
        total = re.search(r'Showing[^<]*?of\s+(\d+)', page) or re.search(r'(\d+)\s+(?:hits|records|results)', page, re.I)
        print(f'== {term}: HTTP {code} {eff} total={total.group(1) if total else "?"}')
        seen, n = set(), 1
        while True:
            new = [r for r in rows(page) if r[0] not in seen]
            for rid, cells in new:
                seen.add(rid)
                print('  ', rid, '|', ' | '.join(c for c in cells if c)[:260])
            nxt = re.search(r'href="(overview\.aspx\?[^"]*?pg=(\d+)[^"]*)"[^>]*>\s*(?:Next|&gt;|>)', page, re.I)
            if not new or not nxt or n >= 12:
                break
            n += 1
            code, eff, page = curl(os.path.join(outdir, f'{safe}_p{n}.html'), BASE + html.unescape(nxt.group(1)), jar, None, eff)
            if code != '200':
                print(f'   page {n}: HTTP {code}; stopping on this host')
                return
        print(f'   {len(seen)} records listed')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
