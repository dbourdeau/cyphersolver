"""Manuscriptorium castor search, print matching BNP records' globIndex (route from research/swiss_austrian/manu.py)."""
import json, sys, time, urllib.request as u, urllib.parse as p
q = json.dumps([{"fieldId": "globIndex", "queryRow": sys.argv[1], "logOp": ""}])
url = 'https://www.manuscriptorium.com/castor/manuscriptorium/search/formSearch?' + p.urlencode({'query': q, 'coreId': 'manuscriptorium', 'sort': '', 'rows': 50, 'start': 0, 'asciiSearch': 'false', 'defLogOperator': 'AND', 'asterL': 'false', 'aster': 'false'})
r = json.loads(u.urlopen(u.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90).read())
res = r['response']['result']
print('found', res.get('found'))
for d in res['recordList']:
    g = ' | '.join(x for x in d.get('globIndex', []) if isinstance(x, str))
    print('--', d.get('GulliverSourceSystemIdentifier') or d.get('id'), g[:int(sys.argv[2]) if len(sys.argv) > 2 else 700])
