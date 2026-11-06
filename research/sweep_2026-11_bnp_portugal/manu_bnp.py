"""Manuscriptorium castor search, kept to Biblioteca Nacional de Portugal records (ids BNDPL_*) -> manu_bnp.jsonl

    python manu_bnp.py [term ...]

Manuscriptorium holds the BNP manuscript catalogue records item by item (full notes, incl. the long CONTEM field that the
BNP Horizon keyword index does not always reach). Same API as research/swiss_austrian/manu.py.
"""
import os, json, time, sys, urllib.request as u, urllib.parse as p
HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = sys.argv[1:] or ['cifras', 'cifradas', 'cifrados', 'cifrar', 'cifrou', 'decifrar', 'decifradas', 'decifrado',
    'decifração', 'decifrada', 'contracifra', 'contra-cifra', 'criptografia', 'cryptographia', 'chave da cifra',
    'em cifra', 'parte em cifra', 'cifrada em parte', 'parcialmente cifrada', 'carta cifrada', 'cartas cifradas',
    'trecho cifrado', 'caracteres', 'carateres', 'characteres', 'algarismos', 'letra secreta', 'escrita secreta',
    'linguagem cifrada', 'telegrama cifrado', 'telegramas cifrados', 'chiffres', 'chiffre', 'chiffrée', 'en chiffre',
    'zifra', 'ziffra', 'cifra', 'cifrada', 'cifrado', 'cyfra', 'descifrada', 'descifrado', 'notis', 'abecedario',
    'alfabeto']
def get(url):
    err = None
    for i in range(4):
        try:
            return json.loads(u.urlopen(u.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90).read())
        except Exception as e:
            err = e; time.sleep(3)
    print('ERR', err, flush=True)
out = open(os.path.join(HERE, 'manu_bnp.jsonl'), 'a', encoding='utf-8')
for t in TERMS:
    start = 0; total = None; kept = 0
    while True:
        q = json.dumps([{"fieldId": "globIndex", "queryRow": t, "logOp": ""}])
        url = 'https://www.manuscriptorium.com/castor/manuscriptorium/search/formSearch?' + p.urlencode({'query': q, 'coreId': 'manuscriptorium', 'sort': '', 'rows': 100, 'start': start, 'asciiSearch': 'false', 'defLogOperator': 'AND', 'asterL': 'false', 'aster': 'false'})
        r = get(url)
        if not r: break
        res = r['response']['result']; total = res.get('found'); recs = res['recordList']
        for d in recs:
            gid = d.get('ID') or ''
            if not str(gid).startswith('BNDPL'):
                continue
            g = ' | '.join(x for x in d.get('globIndex', []) if isinstance(x, str))
            out.write(json.dumps({'term': t, 'id': gid, 'glob': g[:6000]}, ensure_ascii=False) + '\n'); kept += 1
        out.flush()
        start += len(recs)
        if not recs or start >= (total or 0) or start >= 3000: break
        time.sleep(0.5)
    print(t, total, kept, flush=True)
