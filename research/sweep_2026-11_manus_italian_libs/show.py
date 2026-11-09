import json, sys, screen
seenp='_dl/seen_ids.json'
import os
seen=set(json.load(open(seenp))) if os.path.exists(seenp) else set()
r=json.load(open('_dl/screen.json',encoding='utf8'))
skip=('Firenze, Biblioteca nazionale centrale, Autografi Palatini, Carte M','Firenze, Biblioteca nazionale centrale, Ginori')
out=[]
for x in r:
    if x['id'] in seen: continue
    seen.add(x['id'])
    if x['title'].startswith(skip) or 'Carte machiavelli' in x['title']: continue
    out.append(x)
for x in out:
    print(x['id'],x['title'][:100]); print('    ',x['ctx'][0][50:230].encode('ascii','replace').decode())
json.dump(sorted(seen),open(seenp,'w'))
print(len(out),file=sys.stderr)
