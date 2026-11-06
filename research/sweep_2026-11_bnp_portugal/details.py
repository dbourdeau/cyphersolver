"""Fetch the full BNP catalogue record of every bib id in hits.jsonl -> details.jsonl.

    python details.py [bib ...]

Each line: bib, title, fields (label -> text, from the full-record table), cota (shelfmarks), colecao,
links (purl / bndigital links found in the record), text (whole record flattened).
"""
import json, os, re, sys, time, html, urllib.request

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
HERE = os.path.dirname(os.path.abspath(__file__))
URL = 'https://catalogo.bnportugal.gov.pt/ipac20/ipac.jsp?profile=bn&source=~!bnp&view=subscriptionsummary&uri=full=3100024~!{}~!0&ri=1&aspect=basic_search&menu=search'


def get(url):
    for i in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60).read().decode('utf-8', 'replace')
        except Exception as e:
            print('retry', e, file=sys.stderr)
            time.sleep(5)
    return ''


def flat(s):
    t = re.sub(r'<script.*?</script>', '', s, flags=re.S)
    t = re.sub(r'<style.*?</style>', '', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '|', t)
    t = html.unescape(re.sub(r'\s+', ' ', t))
    return re.sub(r'(\|\s*)+', '|', t)


def parse(bib, s):
    t = flat(s)
    a = t.find('|na Europeana|')
    b = t.find('|Propor correção do registo')
    body = t[a + 14:b] if a >= 0 and b > a else t
    fields, cur = {}, 'TITULO'
    for part in body.split('|'):
        p = part.strip()
        if re.fullmatch(r'[A-ZÀ-Ý .]{3,}:', p):
            cur = p[:-1].strip()
            continue
        if p:
            fields.setdefault(cur, []).append(p)
    ex = t[t.find('|Exemplares|'):t.find('|Assunto:|')] if '|Exemplares|' in t else ''
    cotas = re.findall(r'\|((?:COD|PBA|MSS|CAD|BN|ARQ|ESP|F|L|H|S|J|E|A|N|CF)\.?[^|]{0,40}?\d[^|]{0,30})\|', ex)
    links = sorted(set(re.findall(r'https?://(?:purl\.pt|bndigital\.bnportugal\.gov\.pt)[^"\'<> |]*', s)))
    return {'bib': bib, 'title': ' '.join(fields.get('TITULO', [])), 'fields': {k: ' / '.join(v) for k, v in fields.items()},
            'exemplares': ex.strip('|'), 'cotas': cotas, 'links': links, 'text': body}


def main():
    out = os.path.join(HERE, os.environ.get('DETAILS', 'details.jsonl'))
    have = set()
    if os.path.exists(out):
        have = {json.loads(l)['bib'] for l in open(out, encoding='utf-8')}
    if len(sys.argv) > 1:
        bibs = [int(x) for x in sys.argv[1:]]
    else:
        bibs = []
        for l in open(os.path.join(HERE, 'hits.jsonl'), encoding='utf-8'):
            r = json.loads(l)
            if 'bib' in r and r['bib'] not in bibs:
                bibs.append(r['bib'])
    with open(out, 'a', encoding='utf-8') as fh:
        for bib in bibs:
            if bib in have:
                continue
            s = get(URL.format(bib))
            fh.write(json.dumps(parse(bib, s), ensure_ascii=False) + '\n')
            fh.flush()
            have.add(bib)
            time.sleep(0.6)


if __name__ == '__main__':
    main()
