"""BNP catalogue (Horizon ipac20) keyword harvest for cipher terms.

    python harvest.py            -> hits.jsonl (one line per term x collection x hit: term, coll, bib id, title)

Keyword search: ipac.jsp?profile=bn&menu=search&index=.GW&term=<q>[&limitbox_1=COL01+%3D+<COLL>]&page=N
(10 hits per page; `*` truncates, e.g. cifr*). Full record: ipac.jsp?profile=bn&uri=full=3100024~!<bib>~!0
Stable link: http://id.bnportugal.gov.pt/bib/catbnp/<bib>
"""
import json, re, sys, time, html, urllib.parse, urllib.request, os

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
BASE = 'https://catalogo.bnportugal.gov.pt/ipac20/ipac.jsp?profile=bn&menu=search&index=.GW&term='
HERE = os.path.dirname(os.path.abspath(__file__))

TERMS = ['cifr*', 'decifr*', 'contracifra', 'contra-cifra', 'chiffr*', 'dechiffr*', 'cyfr*', 'zifr*', 'cifer*',
         'criptogr*', 'cryptogr*', 'steganogr*', 'notis', 'arcan*', 'caracteres', 'algarismos', 'numeros',
         'segredo', 'secreta', 'secreto', 'occult*', 'chave', 'clave', 'alfabeto', 'abecedario', 'abedecedario',
         'jerogl*', 'hieroglif*', 'enigma*', 'sinais', 'carateres', 'characteres']
COLLS = ['', 'RESMAN', 'RESARQ', 'RESESP', 'RESERV']


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    for i in range(3):
        try:
            return urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'replace')
        except Exception as e:
            print('retry', e, file=sys.stderr)
            time.sleep(5)
    return ''


def parse(s):
    n = re.search(r'(\d+)</b>&nbsp;registos para', s)
    total = int(n.group(1)) if n else 0
    hits = []
    blocks = re.split(r'boldBlackFont1">\s*\d+\.', s)[1:]
    for b in blocks:
        m = re.search(r'uri%3Dfull%3D3100024%7E%21(\d+)%7E%21', b)
        a = re.search(r'class="smallAnchor"[^>]*>(.*?)</a>', b, re.S)
        if not (m and a):
            continue
        t = html.unescape(re.sub(r'<[^>]+>', '', a.group(1)))
        hits.append((int(m.group(1)), re.sub(r'\s+', ' ', t).strip()))
    return total, hits


def main():
    out = os.path.join(HERE, 'hits.jsonl')
    done = set()
    if os.path.exists(out):
        for line in open(out, encoding='utf-8'):
            r = json.loads(line)
            done.add((r['term'], r['coll']))
    terms = sys.argv[1:] or TERMS
    with open(out, 'a', encoding='utf-8') as fh:
        for term in terms:
            for coll in COLLS:
                if (term, coll) in done:
                    continue
                q = urllib.parse.quote(term, safe='*')
                lim = '&limitbox_1=' + urllib.parse.quote_plus('COL01 = ' + coll) if coll else ''
                s = get(BASE + q + lim)
                total, hits = parse(s)
                print(term, coll or 'all', total, file=sys.stderr)
                if total > 600 and not coll:
                    # too broad without a collection limit: keep only the collection-limited runs
                    fh.write(json.dumps({'term': term, 'coll': coll, 'total': total, 'skipped': True}) + '\n')
                    continue
                allh = list(hits)
                page = 2
                while len(allh) < total and page <= 80:
                    time.sleep(0.7)
                    _, h = parse(get(BASE + q + lim + f'&page={page}'))
                    if not h:
                        break
                    allh += h
                    page += 1
                if not allh:
                    fh.write(json.dumps({'term': term, 'coll': coll, 'total': total}) + '\n')
                for bib, title in allh:
                    fh.write(json.dumps({'term': term, 'coll': coll, 'total': total, 'bib': bib, 'title': title},
                                        ensure_ascii=False) + '\n')
                fh.flush()
                time.sleep(0.7)


if __name__ == '__main__':
    main()
