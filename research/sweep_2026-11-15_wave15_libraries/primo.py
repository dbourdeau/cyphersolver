"""Primo VE public API harvest (soeg.kb.dk, a-z.lu).  python -I -X utf8 primo.py kb|bnl term [term ...]
Appends raw pnx summaries to raw/primo_<site>.jsonl; prints counts and non-book records."""
import json, sys, time, urllib.request, urllib.parse, os
HERE = os.path.dirname(os.path.abspath(__file__))
SITES = {'kb': ('https://soeg.kb.dk', '45KBDK_KGL', '45KBDK_KGL:KGL', 'MyInstitution', 'Everything'),
         'bnl': ('https://www.a-z.lu', '352LUX_BIBNET_NETWORK', '352LUX_BIBNET_NETWORK:BIBNET_UNION', 'DN_and_CI', 'DiscoveryNetwork')}
def get(site, q, off=0, limit=50, facet=''):
    host, inst, vid, scope, tab = SITES[site]
    p = dict(blendFacetsSeparately='false', disableCache='false', getMore='0', inst=inst, lang='en', limit=limit, newspapersActive='false', newspapersSearch='false', offset=off, pcAvailability='false', q='any,contains,' + q, qExclude='', qInclude=facet, rapido='false', refEntryActive='false', rtaLinks='true', scope=scope, skipDelivery='Y', sort='rank', tab=tab, vid=vid)
    req = urllib.request.Request(host + '/primaws/rest/pub/pnxs?' + urllib.parse.urlencode(p), headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=90) as f:
        return json.load(f)
def main():
    site = sys.argv[1]; facet = ''
    args = sys.argv[2:]
    if args and args[0].startswith('facet='):
        facet = args[0][6:]; args = args[1:]
    out = open(os.path.join(HERE, 'raw', f'primo_{site}.jsonl'), 'a', encoding='utf-8')
    for q in args:
        off = 0; n = 0
        while off < 300:
            try: j = get(site, q, off, facet=facet)
            except Exception as e: print(q, 'ERR', e); break
            docs = j.get('docs', [])
            if off == 0:
                print('##', q, 'total', j['info'].get('total'), 'local', j['info'].get('totalResultsLocal'))
                fac = {f['name']: [(v['value'], v['count']) for v in f['values']][:12] for f in j.get('facets', []) if f['name'] in ('rtype', 'tlevel', 'library')}
                print('   facets', fac)
            for d in docs:
                px = d['pnx']; di = px.get('display', {})
                g = lambda k: ' ; '.join(di.get(k, []))
                rec = dict(q=q, id=px['control']['recordid'][0], type=g('type'), title=g('title'), date=g('creationdate'), creator=g('creator'), desc=g('description'), fmt=g('format'), ispartof=g('ispartof'), source=g('source'), lds={k: v for k, v in di.items() if k.startswith('lds')})
                out.write(json.dumps(rec, ensure_ascii=False) + '\n'); n += 1
                if rec['type'] not in ('book', 'article', 'journal', 'newspaper_article', 'review', 'audio', 'video', 'score'):
                    print('  ', rec['id'], rec['type'], rec['date'], '|', rec['title'][:110], '|', rec['creator'][:30], '|', rec['desc'][:160].replace('\n', ' '))
            off += 50
            time.sleep(1.2)
            if not docs or off >= (j['info'].get('total') or 0): break
        out.flush()
if __name__ == "__main__":
    main()
