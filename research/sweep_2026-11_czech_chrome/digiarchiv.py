"""Search SOA Třeboň DigiArchiv (digi.ceskearchivy.cz) without the browser.

The search page builds a PHP-serialized query ("sparam") and POSTs it to pages/search_result.php; any queryid works.
    python digiarchiv.py "šifr*" [start]
Prints the result blocks as text.
"""
import html, re, sys, urllib.parse, urllib.request

KEYS = ['searchtype', 'search', 'autor', 'evc', 'searcharch', 'date_from', 'date_to', 'allwords', 'userp', 'date_b_from',
        'date_b_to', 'date_m_from', 'date_m_to', 'date_d_from', 'date_d_to', 'search_in', 'subtyp', 'ftx_id2', 'ftx_page',
        'ai', 'imagecontent']


def ser(d):
    out = []
    for k in KEYS:
        v = d.get(k, 0 if k == 'allwords' else '')
        out.append(f's:{len(k.encode())}:"{k}";')
        out.append(f'i:{v};' if isinstance(v, int) else f's:{len(v.encode())}:"{v}";')
    return f'a:{len(KEYS)}:{{' + ''.join(out) + '}'


def search(term, start=0, order='', **kw):
    d = {'search': term, **kw}
    body = urllib.parse.urlencode({'sparam': ser(d), 'obsah_sn': '0', 'lang': 'cs', 'sst': str(start), 'order': order,
                                   'ih': '900', 'iw': '1500', 'histstore': '0'}).encode()
    req = urllib.request.Request('https://digi.ceskearchivy.cz/pages/search_result.php?id=&queryid=966c94c6682e4f7ca0892a3ab7b3103a&doctree=10',
                                 data=body, headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
    t = urllib.request.urlopen(req, timeout=90).read().decode('utf-8', 'replace')
    return t


def text(t):
    t = re.sub(r'<script.*?</script>', '', t, flags=re.S)
    t = re.sub(r'<(br|/tr|/div|/h\d|/p)[^>]*>', '\n', t)
    t = re.sub(r'</t[dh]>', ' | ', t)
    s = html.unescape(re.sub(r'<[^>]+>', '', t))
    return re.sub(r'\n\s*\n+', '\n', s)


if __name__ == '__main__':
    t = search(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 0)
    if len(sys.argv) > 3:
        open(sys.argv[3], 'w', encoding='utf-8').write(t)
    print(text(t))
