"""Biblioteca Nacional Digital (BND) helpers: page list and one page image of a digitised item.

    python bnd.py pages <bnd_item_id>                 -> prints the page names (file stems) in order
    python bnd.py get <bnd_item_id> <stem> [px]       -> saves img/<stem>.jpg (longest side px, default 1800)
    python bnd.py find "<search>"                     -> BND records search (title, item id)

Route: item page /records/item/<id> -> viewer /viewer/<id>/ holds
/api/viewer/lgiiif?url=/srv/www/limbgallery/medias/<a>/<b>/<c>/<d>/<uuid>/&max=N, whose JSON lists every page tile
set; an image is /i/?IIIF=/<a>/<b>/<c>/<d>/<uuid>/iiif/<stem>.tif/full/!<px>,<px>/0/default.jpg (IIIF level 1).
The item resolves at https://purl.pt/<purl> ("ID persistente do objecto digital" on the item page).
"""
import json, os, re, sys, urllib.request, urllib.parse, html

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
B = 'https://bndigital.bnportugal.gov.pt'
HERE = os.path.dirname(os.path.abspath(__file__))


def get(url, binary=False):
    r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=90).read()
    return r if binary else r.decode('utf-8', 'replace')


def tiles(item):
    v = get(f'{B}/viewer/{item}/?offset=')
    m = re.search(r'/api/viewer/lgiiif\?url=[^"\' ]+', v)
    if not m:
        raise SystemExit('no lgiiif url on viewer page')
    j = json.loads(get(B + html.unescape(m.group(0))))
    t = j['item']['tiles']
    return [(k, t[k]['@id']) for k in sorted(t)]


def main(a):
    if a[0] == 'pages':
        for k, i in tiles(a[1]):
            print(k)
    elif a[0] == 'get':
        px = a[3] if len(a) > 3 else '1800'
        d = dict(tiles(a[1]))
        os.makedirs(os.path.join(HERE, 'img'), exist_ok=True)
        out = os.path.join(HERE, 'img', a[2] + '.jpg')
        open(out, 'wb').write(get(B + d[a[2]] + f'/full/!{px},{px}/0/default.jpg', binary=True))
        print(out)
    elif a[0] == 'find':
        s = get(f'{B}/records?search={urllib.parse.quote(a[1])}&perpage=50')
        for m in re.finditer(r'href="/records/item/(\d+)-[^"?]*\?offset=\d+"><h3>(.*?)</h3>', s, re.S):
            print(m.group(1), html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip())


if __name__ == '__main__':
    main(sys.argv[1:])
