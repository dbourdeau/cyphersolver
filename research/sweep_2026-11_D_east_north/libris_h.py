"""Libris xsearch harvest: Swedish union catalogue (KB, Uppsala, Lund ... manuscripts included).
Writes libris_hits.jsonl (one record per hit, term attached)."""
import requests, sys, json, time, urllib.parse, collections
sys.stdout.reconfigure(encoding='utf-8')
H = {'User-Agent':'Mozilla/5.0 (cyphersolver research sweep; polite)', 'Accept':'application/json'}
terms = sys.argv[1:] or ['chiffer','chiffre','chiffrerad','chiffrerade','chifferbrev','chifferskrift','dechiffrering','dechiffrerade','ziffer','cifra','cipher','hemlig skrift','nyckel chiffer','kryptografi']
out = open('libris_hits.jsonl','a',encoding='utf-8')
seen=set()
for t in terms:
    n=200; start=1; total=None
    while True:
        u = 'http://libris.kb.se/xsearch?query=%s&format=json&n=%d&start=%d' % (urllib.parse.quote(t), n, start)
        for attempt in range(3):
            try:
                r = requests.get(u, headers=H, timeout=40); r.raise_for_status(); break
            except Exception as e:
                print('retry', e); time.sleep(5)
        d = json.loads(r.content.decode("utf-8", "replace"))["xsearch"]
        total = d['records']
        lst = d.get('list', [])
        for rec in lst:
            rec['term']=t
            out.write(json.dumps(rec, ensure_ascii=False)+'\n')
        print(t, start, len(lst), total, flush=True)
        start += n
        time.sleep(1.2)
        if start > total or start > 1000 or not lst: break
