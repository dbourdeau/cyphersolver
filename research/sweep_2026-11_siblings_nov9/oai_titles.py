"""List oai_dc titles for an archieven.nl OAI-PMH set. usage: oai_titles.py SET out.jsonl"""
import sys, re, json, time, requests, html
S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0'
B = 'https://harvest.archieven.nl/OAI/OAIHandler'
sets, out = sys.argv[1], sys.argv[2]
f = open(out, 'w', encoding='utf-8')
url = B + '?verb=ListRecords&metadataPrefix=oai_dc&set=' + sets
n = 0
while True:
    r = S.get(url, timeout=120)
    if r.status_code != 200: print('STOP', r.status_code); break
    x = r.text
    for m in re.finditer(r'<record>(.*?)</record>', x, re.S):
        rec = m.group(1)
        ident = re.search(r'<identifier>([^<]*)</identifier>', rec)
        title = re.search(r'<dc:title[^>]*>([^<]*)', rec)
        ids = re.findall(r'<dc:identifier[^>]*>([^<]*)', rec)
        f.write(json.dumps({'id': ident.group(1) if ident else '', 'title': html.unescape(title.group(1)) if title else '', 'dc_id': ids}, ensure_ascii=False) + '\n'); n += 1
    tok = re.search(r'<resumptionToken[^>]*>([^<]+)', x)
    print(n, flush=True)
    if not tok: break
    url = B + '?verb=ListRecords&resumptionToken=' + requests.utils.quote(tok.group(1))
    time.sleep(2.5)
