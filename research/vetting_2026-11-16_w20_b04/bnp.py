"""BNP catalogue (Horizon ipac20) helpers, plain HTTP with a browser User-Agent (route from research/sweep_2026-11_bnp_portugal).

    python bnp.py search "<keywords>" [page]   -> bib ids and titles of the hits
    python bnp.py full <bib> [<bib> ...]       -> the flattened full record (saved to img/raw/bnp_<bib>.txt too)
    python bnp.py bnd "<keywords>"             -> Biblioteca Nacional Digital search (digitised items)
"""
import os, re, sys, time, html, urllib.request, urllib.parse
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
HERE = os.path.dirname(os.path.abspath(__file__))
S = 'https://catalogo.bnportugal.gov.pt/ipac20/ipac.jsp?profile=bn&menu=search&index=.GW&term={}&page={}'
F = 'https://catalogo.bnportugal.gov.pt/ipac20/ipac.jsp?profile=bn&source=~!bnp&view=subscriptionsummary&uri=full=3100024~!{}~!0&ri=1&aspect=basic_search&menu=search'


def get(u):
    time.sleep(1)
    return urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': UA}), timeout=90).read().decode('utf-8', 'replace')


def flat(s):
    t = re.sub(r'<(script|style).*?</\1>', '', s, flags=re.S)
    t = re.sub(r'<[^>]+>', '|', t)
    t = html.unescape(re.sub(r'\s+', ' ', t))
    return re.sub(r'(\|\s*)+', '|', t)


a = sys.argv[1:]
if a[0] == 'search':
    s = get(S.format(urllib.parse.quote(a[1]), a[2] if len(a) > 2 else 1))
    seen = []
    for m in re.finditer(r'full(?:=|%3D)3100024(?:~!|%7E%21)(\d+)(?:~!|%7E%21)', s):
        if m.group(1) not in seen:
            seen.append(m.group(1))
    t = flat(s)
    m = re.search(r'\|(\d+) (?:títulos|registos|resultados)[^|]*', t)
    print('hits text:', m.group(0) if m else '?', '| bibs:', seen)
    i, j = t.find('|PRR|--PRR|'), t.find('|Adic./Remover')
    print(t[i + 11:j] if i >= 0 else t[:3000])
elif a[0] == 'full':
    for b in a[1:]:
        s = get(F.format(b))
        t = flat(s)
        i, j = t.find('|na Europeana|'), t.find('|Propor correção do registo')
        body = t[i + 14:j] if i >= 0 and j > i else t
        open(os.path.join(HERE, 'img', 'raw', f'bnp_{b}.txt'), 'w', encoding='utf8').write(body)
        links = sorted(set(re.findall(r'https?://(?:purl\.pt|bndigital\.bnportugal\.gov\.pt)[^"\'<> |]*', s)))
        print('=====', b, 'links:', links)
        print(body[:4000])
elif a[0] == 'bnd':
    s = get('https://bndigital.bnportugal.gov.pt/records?search=' + urllib.parse.quote(a[1]) + '&perpage=50')
    hits = [(m.group(1), html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip())
            for m in re.finditer(r'href="/records/item/(\d+)-[^"?]*\?offset=\d+"><h3>(.*?)</h3>', s, re.S)]
    print(len(hits), 'BND hits'); [print(' ', h) for h in hits[:30]]
