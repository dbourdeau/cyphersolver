"""Resolve ARON hits to fund, inventory number, date, parent path and digital objects; write aron_details.jsonl."""
import json, os, re, sys, time
from aron import detail, S, headers
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'aron_details.jsonl')
_fund = {}


def items(d):
    out = {}
    def walk(p):
        for it in p.get('items', []):
            out.setdefault(it['type'], []).append(it['value'])
        for c in p.get('childParts', []):
            walk(c)
    for p in d.get('parts', []):
        walk(p)
    return out


def fund_name(base, fid):
    if fid not in _fund:
        try:
            _fund[fid] = detail(base, fid).get('name')
        except Exception:
            _fund[fid] = fid
    return _fund[fid]


def resolve(base, apu_id):
    d = detail(base, apu_id)
    it = items(d)
    fund = fund_name(base, it['FUND~REF'][0]) if it.get('FUND~REF') else ''
    path = []
    p = d.get('parent')
    hops = 0
    while p and hops < 6:
        pid = p if isinstance(p, str) else p.get('id')
        try:
            pd = detail(base, pid)
        except Exception:
            break
        path.append(pd.get('name'))
        p = pd.get('parent'); hops += 1
    keep = {k: v for k, v in it.items() if k not in ('FUND~REF', 'FUND~INST~REF')}
    return {'base': base, 'id': apu_id, 'name': d.get('name'), 'description': d.get('description'), 'fund': fund,
            'path': path[::-1], 'fields': keep, 'daos': len(d.get('digitalObjects') or []),
            'dao_ids': [x.get('id') if isinstance(x, dict) else x for x in (d.get('digitalObjects') or [])][:5],
            'permalink': d.get('permalink')}


if __name__ == '__main__':
    base = sys.argv[1]
    ids = sys.argv[2:]
    done = set()
    if os.path.exists(OUT):
        done = {json.loads(l)['id'] for l in open(OUT, encoding='utf-8')}
    with open(OUT, 'a', encoding='utf-8') as fh:
        for i in ids:
            full = i
            if len(i) < 36:
                for l in open(os.path.join(HERE, 'aron_hits.jsonl'), encoding='utf-8'):
                    dd = json.loads(l)
                    if dd['id'].startswith(i) and dd['base'] == base:
                        full = dd['id']; break
            if full in done:
                continue
            r = resolve(base, full)
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
            f = r['fields']
            print(f"{full[:8]} | {r['fund']} | path={' > '.join(x or '' for x in r['path'])[:200]} | inv={f.get('INV~CISLO')} sig={f.get('SIGNATURA') or f.get('SIGN')} | date={[re.sub(r'T00:00:00|T23:59:59','',x) for x in f.get('UNIT~DATE',[])]} | daos={r['daos']}")
            print('    ', (r['name'] or '')[:300])
            time.sleep(0.4)
