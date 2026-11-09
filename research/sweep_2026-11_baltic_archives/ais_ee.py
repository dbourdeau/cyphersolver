"""Estonian National Archives AIS (ais.ra.ee), server-rendered GET search, rows parsed from the result table.
python ais_ee.py <until> term...   Output ais_ee_hits.jsonl (term, ref, title, dates, level, archive)."""
import requests, re, sys, html, json, time
sys.stdout.reconfigure(encoding='utf-8')
H = {'User-Agent':'Mozilla/5.0 (cyphersolver research sweep; polite)'}
s=requests.Session(); s.headers.update(H)
until=sys.argv[1]; terms=sys.argv[2:]
out=open('ais_ee_hits.jsonl','a',encoding='utf-8')
def clean(x): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',x))).strip()
for term in terms:
    page=1; total=None
    while True:
        params={'q':term,'size':100,'page':page}
        if until!='-': params.update({'until':until})
        r=s.get('https://ais.ra.ee/et/description-unit/search',params=params,timeout=90)
        t=r.text
        body=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
        if 'Ei leitud ühtegi tulemust' in body:
            print(term,'no hits'); break
        m=re.search(r'tulemust\s*([\d\s\xa0]+)st',clean(body))
        total=int(re.sub(r'\D','',m.group(1))) if m else None
        rows=re.findall(r'<tr[^>]*>(.*?)</tr>',body,flags=re.S)
        n=0
        for row in rows:
            cells=[clean(c) for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>',row,flags=re.S)]
            href=re.search(r'href="([^"]*description-unit/[^"]*)"',row)
            if len(cells)>=6 and cells[0].isdigit():
                out.write(json.dumps({'term':term,'cells':cells,'href':href.group(1) if href else ''},ensure_ascii=False)+'\n'); n+=1
        print(term,page,n,total,flush=True)
        if n<100 or page>=12: break
        page+=1; time.sleep(2.5)
    time.sleep(2.5)
