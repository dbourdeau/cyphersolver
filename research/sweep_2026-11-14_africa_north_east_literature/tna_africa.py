#!/usr/bin/env python3
"""TNA Discovery API (works with curl; python TLS is reset) - cipher terms x African place words.
usage: tna_africa.py OUT.jsonl  -> prints count per query; writes all records (<=100/query, first page)."""
import subprocess, json, urllib.parse, time, sys
U = "https://discovery.nationalarchives.gov.uk/API/search/records"
out = sys.argv[1]
terms = ['cipher', 'cypher', '"in cipher"', 'decipher', 'cryptogram', 'code telegram']
places = ['Morocco', 'Tangier', 'Barbary', 'Algiers', 'Tunis', 'Tripoli', 'Egypt', 'Cairo', 'Alexandria', 'Abyssinia',
          'Ethiopia', 'Massawa', 'Eritrea', 'Somaliland', 'Zanzibar', 'Sudan', 'Khartoum', 'Mahdi', 'Harar', 'Kenya', 'Uganda',
          'Mombasa', 'Libya', 'Cyrenaica', 'Gordon Khartoum']
if len(sys.argv) > 2: places = sys.argv[2].split('|')
def q(**p):
    url = U + "?" + urllib.parse.urlencode(p)
    for i in range(3):
        r = subprocess.run(["curl", "-s", "-m", "60", url], capture_output=True)
        try: return json.loads(r.stdout.decode("utf8"))
        except Exception: time.sleep(3)
for pl in places:
    for t in terms:
        d = q(**{'sps.searchQuery': f'{t} {pl}', 'sps.resultsPageSize': 100, 'sps.dateTo': '1950-12-31'})
        time.sleep(2.5)
        if not d: print('ERR', t, pl); continue
        print('%5d  %s %s' % (d['count'], t, pl), flush=True)
        with open(out, 'a') as f:
            for r in d['records']:
                f.write(json.dumps({'q': f'{t} {pl}', 'ref': r.get('reference'), 'title': r.get('title'), 'desc': (r.get('description') or '')[:500],
                    'date': r.get('coveringDates'), 'id': r.get('id'), 'held': r.get('heldBy')}, ensure_ascii=False) + '\n')
