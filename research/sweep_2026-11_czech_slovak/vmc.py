"""VadeMeCum (Bach) full-text search: NA Praha (vademecum.nacr.cz) and SOA instances.
Submits the home-page full-text form in a requests session and prints the result list.
Usage: python vmc.py <base e.g. https://vademecum.nacr.cz/vademecum> <term> [pages]"""
import re, sys, html, time, requests
sys.stdout.reconfigure(encoding='utf-8')
S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0'


def form_fields(h, idx):
    forms = re.findall(r'<form.*?</form>', h, re.S)
    f = forms[idx]
    action = html.unescape(re.search(r'action="([^"]*)"', f).group(1))
    data = {}
    for m in re.finditer(r'<input[^>]*>', f):
        t = m.group(0)
        n = re.search(r'name="([^"]*)"', t)
        v = re.search(r'value="([^"]*)"', t)
        if n and ('type="hidden"' in t or n.group(1) in ('searchFrom',)):
            data[n.group(1)] = html.unescape(v.group(1)) if v else ''
    return action, data


def search(base, term):
    root = base.rsplit('/vademecum', 1)[0]
    h = S.get(base + '/', timeout=60).text
    action, data = form_fields(h, 0)
    data['patternFulltext'] = term
    data['searchFulltext'] = ''
    data['wordPosition0'] = '1'
    data['wordOperator0'] = '1'
    r = S.post(root + action, data=data, timeout=120)
    return r


if __name__ == '__main__':
    r = search(sys.argv[1], sys.argv[2])
    open(sys.argv[3] if len(sys.argv) > 3 else 'vmc_last.html', 'w', encoding='utf-8').write(r.text)
    print(r.status_code, r.url, len(r.text))


def parse(h):
    out = []
    for blk in re.findall(r'<aricle class="contentRecordList.*?</aricle>', h, re.S):
        def g(cls):
            m = re.search(r'<p class="%s[^"]*"[^>]*>(.*?)</p>' % cls, blk, re.S)
            if not m:
                return ''
            t = re.sub(r'<[^>]+>', '', m.group(1))
            return html.unescape(re.sub(r'\s+', ' ', t)).strip()
        db = re.search(r'<span class="database">([^<]*)', blk).group(1).strip()
        arch = re.search(r'<span class="archiv">([^<]*)', blk).group(1).strip()
        xid = re.search(r'xid=([0-9a-f-]+)', blk)
        out.append({'db': db, 'archive': arch, 'title': g('title'), 'nad': g('cNAD'), 'years': g('years'),
                    'descr': g('descr'), 'xid': xid.group(1) if xid else '', 'scan': 'Zoomify' in blk})
    return out


def details(base, term, out_dir=None):
    """Search, then open each result's detail page in the same session; return [(record, detail_text)]."""
    root = base.rsplit('/vademecum', 1)[0]
    r = search(base, term)
    res = []
    links = re.findall(r'<a href="(/vademecum/VysledekBean\.action\?show=[^"]*)"', r.text)
    recs = parse(r.text)
    for rec, l in zip(recs, links):
        d = S.get(root + html.unescape(l), timeout=90).text
        t = re.sub(r'<script.*?</script>|<style.*?</style>', '', d, flags=re.S)
        t = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t)))
        res.append((rec, t, d))
    return res
