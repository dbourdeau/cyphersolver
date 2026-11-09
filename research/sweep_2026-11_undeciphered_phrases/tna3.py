import sys,re
sys.path.insert(0,'../tna_discovery')
from tna import q
for t in ['G52/2/19/43','G85/5/2/29','G85/5/2/33','G85/5/2/30','SP 35/4/47','SP 35/4/62']:
    j=q(**{'sps.searchQuery':'"'+t+'"','sps.resultsPageSize':5})
    for rec in (j or {}).get('records',[]):
        if rec.get('reference')==t:
            print(t,rec.get('coveringDates'),rec.get('heldBy'),rec.get('id'),'\n ',rec.get('description')[:1500],'\n')
