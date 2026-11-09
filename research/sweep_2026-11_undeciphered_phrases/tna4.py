import sys,re
sys.path.insert(0,'../tna_discovery')
from tna import q
want={'G52/2/19/43','G85/5/2/29','G85/5/2/33','G85/5/2/30'}
j=q(**{'sps.searchQuery':'cipher not deciphered','sps.resultsPageSize':100,'sps.dateTo':'1900-12-31'})
for rec in j['records']:
    if rec['reference'] in want: print(rec['reference'],rec['id'],rec.get('description') or rec.get('title') or rec.get('scopeContent'),'\n')
