import sys,re,json
sys.path.insert(0,'.')
from opac import search
for t in sys.argv[1:]:
    n,rows=search(t)
    print('##',t,n,len(rows),flush=True)
    for r in rows[:int(__import__('os').environ.get('N','25'))]:
        print(' ',r['shelfmark'],'D' if r['digitised'] else 'U',(r['items'][0][1][:100] if r['items'] else ''))
