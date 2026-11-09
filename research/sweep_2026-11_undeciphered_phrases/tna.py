import sys,time,json
sys.path.insert(0,'../tna_discovery')
from tna import q
for t in sys.argv[1:]:
    j=q(sps_searchQuery=t,sps_dateTo='1900',pageSize=50) if False else q(**{'sps.searchQuery':t,'sps.dateTo':'1900-12-31','sps.resultsPageSize':50})
    if not j: print(t,'none');continue
    print(t,j.get('count'))
    for rec in j.get('records',[]):
        print('  ',rec.get('reference'),'|',rec.get('coveringDates'),'|',(rec.get('description') or rec.get('title') or '')[:220].replace('\n',' '))
    time.sleep(2.5)
