import sys,time,json,re
sys.path.insert(0,'../tna_discovery')
from tna import q
seen={}
for t in sys.argv[1:]:
    for pg in (1,2):
        j=q(**{'sps.searchQuery':t,'sps.dateTo':'1900-12-31','sps.resultsPageSize':100,'sps.page':pg})
        if not j: break
        recs=j.get('records',[])
        for rec in recs:
            d=(rec.get('description') or rec.get('title') or '')
            if re.search(r'ciph|cypher|code|cifr|chiffr',d,re.I) and rec['reference'] not in seen:
                seen[rec['reference']]=1
                print(t,'|',rec.get('reference'),'|',rec.get('coveringDates'),'|',d[:230].replace('\n',' '))
        print('#',t,pg,j.get('count'),file=sys.stderr)
        if len(recs)<100: break
        time.sleep(2.5)
    time.sleep(2.5)
