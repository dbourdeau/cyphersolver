import json,sys
skip=int(sys.argv[2]) if len(sys.argv)>2 else 0
for i,l in enumerate(open(sys.argv[1],encoding='utf8')):
    if i<skip: continue
    d=json.loads(l)
    print('##',i,d['adt'],d['code'],d['term'],d.get('count'),d.get('title','')[14:75],(d.get('note') or d.get('err') or '')[:60])
    for it in d.get('items',[])[:int(sys.argv[3]) if len(sys.argv)>3 else 8]: print('    ',it[:260])
