import json,sys
from na import *
eads=sys.argv[1].split(','); terms=sys.argv[2:]
out={}
for e in eads:
    for t in terms:
        r=items(e,t)
        out[f'{e}|{t}']=r
        print(e,t,len(r))
        for x in r[:40]:
            print('   ',x.get('id'),'|',(x.get('title') or '')[:160],'|',x.get('period'))
json.dump(out,open(f'na_items_{eads[0]}.json','w'),ensure_ascii=False)
