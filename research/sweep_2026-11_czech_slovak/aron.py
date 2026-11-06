"""ARON (Czech archival portal, Národní archiv and the SOA instances) APU search.
POST {base}/api/aron/apu/listview with filters [type EQ <TYPE>, FTX <term>].
Usage: python aron.py <base> <term> [size] [offset] [TYPE]   (TYPE: ARCH_DESC, FUND, FINDING_AID, ENTITY)"""
import json, sys, requests
from urllib.parse import urlsplit
sys.stdout.reconfigure(encoding='utf-8')
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
S = requests.Session()


def headers(base):
    o = '{0.scheme}://{0.netloc}'.format(urlsplit(base))
    # MZA's nginx answers 403 to the API without a browser User-Agent, Origin and Referer
    return {'User-Agent': UA, 'Origin': o, 'Referer': base + '/apu?type=ARCH_DESC',
            'Accept': 'application/json, text/plain, */*'}


def search(base, term, size=50, off=0, typ='ARCH_DESC'):
    body = {"size": size, "offset": off,
            "filters": [{"field": "type", "operation": "EQ", "value": typ},
                        {"operation": "FTX", "value": term}]}
    r = S.post(f'{base}/api/aron/apu/listview', json=body, headers=headers(base), timeout=90)
    r.raise_for_status()
    return r.json()


def detail(base, apu_id):
    return S.get(f'{base}/api/aron/apu/{apu_id}', headers=headers(base), timeout=60).json()


if __name__ == '__main__':
    base, term = sys.argv[1], sys.argv[2]
    size = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    off = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    typ = sys.argv[5] if len(sys.argv) > 5 else 'ARCH_DESC'
    j = search(base, term, size, off, typ)
    print(j['count'])
    for i in j['items']:
        print(' ', i['id'], (i.get('name') or '')[:200], '|', (i.get('description') or '')[:200])
