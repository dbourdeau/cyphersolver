"""Harvest KB (Koninklijke Bibliotheek, The Hague) SRU records for cipher terms; keep manuscripts (dc:type handschrift).

    python harvest_sru.py            -> raw/sru_<term>.xml pages, hits.jsonl (all records), mss.jsonl (handschrift)

Endpoint: https://jsru.kb.nl/sru/sru  (x-collection=GGC, recordSchema=dc).  Polite: one request at a time.
"""
import json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
NS = {'srw': 'http://www.loc.gov/zing/srw/', 'dc': 'http://purl.org/dc/elements/1.1/',
      'dcterms': 'http://purl.org/dc/terms/', 'dcx': 'http://krait.kb.nl/coop/tel/handbook/telterms.html'}
TERMS = sys.argv[1:] or ['geheimschrift', 'cijferschrift', '"in cijfers"', 'cijfer', 'cijfers', 'gecijferd',
         'chiffre', 'chiffres', '"en chiffre"', 'dechiffrement', 'déchiffrement', 'cryptografie', '"geheim schrift"',
         'cipher', 'ziffer', 'sleutel', 'sleutels', 'chiffer', 'cijffer', 'ontcijferd', 'ontcijfering',
         'gechiffreerd', 'dechiffre', 'déchiffré', 'cifra', 'cifras', 'nomenclator', 'cryptogram', 'code',
         'zifra', 'ciphers', 'chiffrée', 'chiffrées', '"notis arcanis"', 'steganographia', 'cryptographie',
         'geheimschriften', 'cijfersleutel', 'cijferbrieven', 'cijferbrief', 'chiffreschrift', 'geheime']


def fetch(q, start, coll='GGC'):
    url = ('https://jsru.kb.nl/sru/sru?query=' + urllib.parse.quote(q) + f'&x-collection={coll}'
           f'&recordSchema=dc&maximumRecords=50&startRecord={start}')
    for i in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read()
        except Exception as ex:
            print('  retry', ex)
            time.sleep(3)
    return b''


def parse(xml):
    root = ET.fromstring(xml)
    n = int(root.findtext('srw:numberOfRecords', '0', NS))
    recs = []
    for rec in root.iter('{http://www.loc.gov/zing/srw/}recordData'):
        d = {}
        for el in rec:
            tag = el.tag.split('}')[1]
            d.setdefault(tag, []).append((el.text or '').strip())
        recs.append(d)
    return n, recs


def main():
    seen = {}
    path_all = os.path.join(HERE, 'hits.jsonl')
    if os.path.exists(path_all):
        for line in open(path_all, encoding='utf-8'):
            r = json.loads(line)
            seen[r['ppn']] = r
    out = open(path_all, 'a', encoding='utf-8')
    for term in TERMS:
        q = f'{term} and type=handschrift'
        start, total = 1, None
        while True:
            x = fetch(q, start)
            if not x:
                break
            try:
                n, recs = parse(x)
            except ET.ParseError:
                print('parse error', term, start)
                break
            total = n
            for d in recs:
                ppn = ''
                for i in d.get('identifier', []):
                    m = re.search(r'PPN:(\w+)', i)
                    if m:
                        ppn = m.group(1)
                if not ppn or ppn in seen:
                    if ppn in seen:
                        seen[ppn].setdefault('terms', [])
                        if term not in seen[ppn]['terms']:
                            seen[ppn]['terms'].append(term)
                    continue
                r = {'ppn': ppn, 'terms': [term], **d}
                seen[ppn] = r
                out.write(json.dumps(r, ensure_ascii=False) + '\n')
            start += 50
            if start > n or start > 2000:
                break
            time.sleep(0.5)
        print(term, total)
    out.close()
    mss = [r for r in seen.values() if 'handschrift' in r.get('type', [])]
    with open(os.path.join(HERE, 'mss.jsonl'), 'w', encoding='utf-8') as fh:
        for r in mss:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    print('records', len(seen), 'manuscripts', len(mss))


if __name__ == '__main__':
    main()
