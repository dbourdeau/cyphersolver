"""Harvest Arcinsys Hessen and Niedersachsen for cipher words, without a browser.

simpleSearch_search.action (GET) returns an executionId; search_getFacetTreeJson gives the root nodeId; search_doSearch
(POST, a DataTables tableStateJson body, with the page's _csrf) returns the rows. One request a second. Writes arcinsys_hits.json keyed by portal and record id.

    python arcinsys_harvest.py --probe he Geheimschrift
    python arcinsys_harvest.py
"""
import json, os, re, sys, time
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'arcinsys_hits.json')
BASE = {'he': 'https://arcinsys.hessen.de/arcinsys/', 'ni': 'https://www.arcinsys.niedersachsen.de/arcinsys/'}
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'
TERMS = ['chiffriert', 'Geheimschrift', 'verschlüsselt', 'Chiffre', 'Chiffren', 'Dechiffrierung', 'dechiffriert',
         'chiffrierte', 'chiffrierter', 'chiffrierten', 'chiffrierter Bericht', 'chiffrirt', 'chiffrirte', 'Ziffern',
         'Chiffern', 'Chiffer', 'Zifferschrift', 'Ziffernschrift', 'Geheimzeichen', 'Geheimsprache', 'Geheimalphabet',
         'Geheimschlüssel', 'Geheimcode', 'Kryptogramm', 'Entzifferung', 'entziffert', 'dechiffrirt', 'deschiffriert',
         'en chiffre', 'in Ziffern', 'in Chiffren', 'Chiffreschlüssel', 'Chiffrenschlüssel', 'Chiffrierung',
         'Chiffrierschlüssel', 'Geheimbrief', 'verschlüsselte', 'verschlüsselter', 'Zahlenschrift', 'Geheimtinte',
         'sympathetische Tinte']


COLS = [{'data': c, 'name': c, 'searchable': True, 'orderable': o, 'search': {'value': '', 'regex': False}}
        for c, o in [('columnKeyItemType', False), ('columnKeySignatur', True), ('columnKeyBezeichnung', True),
                     ('columnKeyLaufzeit', True), ('columnKeyInfoIcons', False), ('columnKeyPreviewImage', False),
                     ('columnKeyActions', False)]]


def search(s, base, term):
    r = s.get(base + 'simpleSearch.action', timeout=60)
    ex = re.search(r'name="executionId" value="([^"]+)"', r.text).group(1)
    time.sleep(1)
    r = s.get(base + 'simpleSearch_search.action', params={
        'executionId': ex, 'filter.searchTerm': term, 'filter.selectedSearchArea': 'ALL_ARCHIVES',
        '__checkbox_filter.hasDigitalMedia': 'true'}, timeout=90)
    ex = re.search(r'executionId=(\w+)', r.url).group(1)
    h = {'X-Requested-With': 'XMLHttpRequest', 'Referer': r.url}
    m = re.search(r'name="_csrf" content="([^"]+)"', r.text)
    if m:
        h['X-CSRF-TOKEN'] = m.group(1)
    s.get(base + 'ajax_search_showSearchResultList.action', params={'executionId': ex}, headers=h, timeout=60)
    time.sleep(1)
    tree = s.get(base + 'search_getFacetTreeJson.action', params={'executionId': ex}, headers=h, timeout=90).text
    try:
        node = json.loads(tree)[0]['id']          # root of the per-archive facet tree
    except (ValueError, IndexError, KeyError):
        return 0, [], tree[:300], None
    rows, total, start = [], None, 0
    while True:
        time.sleep(1)
        state = {'draw': 2, 'columns': COLS, 'order': [], 'start': start, 'length': 50,
                 'search': {'value': '', 'regex': False}, 'selectedRowIdsPerPage': []}
        q = s.post(base + 'search_doSearch.action', params={'executionId': ex, 'nodeId': node}, headers=h,
                   data={'tableStateJson': json.dumps(state), '_csrf': h.get('X-CSRF-TOKEN', '')}, timeout=120)
        j = q.json()
        total = j.get('recordsTotal', j.get('recordsFiltered', 0)) if total is None else total
        got = j.get('data') or []
        rows += got
        start += len(got)
        if not got or start >= total:
            break
    return total, rows, tree[:300], node


def main():
    s = requests.Session()
    s.headers['User-Agent'] = UA
    if sys.argv[1:2] == ['--probe']:
        total, rows, tree, node = search(s, BASE[sys.argv[2]], sys.argv[3])
        print(total, len(rows), node)
        print(tree)
        print(json.dumps(rows[:2], ensure_ascii=False, indent=1)[:2500])
        return
    store = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {'terms': {}, 'hits': {}}
    for portal, base in BASE.items():
        for t in TERMS:
            key = portal + ':' + t
            if key in store['terms']:
                continue
            try:
                total, rows, _, _ = search(s, base, t)
            except Exception as e:
                print(key, 'ERROR', repr(e)[:200], flush=True)
                continue
            store['terms'][key] = {'count': total, 'got': len(rows)}
            for r in rows:
                rid = portal + ':' + str(r.get('DT_RowId'))
                store['hits'].setdefault(rid, r).setdefault('terms', []).append(t)
            json.dump(store, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
            print(key, total, len(rows), 'unique', len(store['hits']), flush=True)


if __name__ == '__main__':
    main()
