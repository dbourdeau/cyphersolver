import sys,json,re
sys.path.insert(0,'research/archive_sweep_2026-10')
import known
corpus=list(known.texts())
big='\n'.join(t for n,t in corpus if not n.startswith('research\pares_ags') and 'spain_nobility' not in n)
rows={}
for l in open('research/pares_ags/hits.jsonl',encoding='utf-8'):
    r=json.loads(l); rows.setdefault(r['id'],r)
FONDS=('OSUNA','FRIAS','FERNAN NUÑEZ','SANTA CRUZ','LUQUE','DIVERSOS','ACA','CODICES','BAENA','TORRELAGUNA','PARCENT','ALTAMIRA','VILLAHERMOSA','MEDINACELI','HERNANI')
out=[]
for r in rows.values():
    s=r['sig'].split(',')[0]
    if not s.startswith(FONDS): continue
    sig=r['sig']
    parts=sig.split(',')
    sigspace=sig.replace(',',' ')
    forms=[r['id'],sig]
    # e.g. OSUNA,CT.2,D.8 -> "CT.2,D.8"
    forms.append(','.join(parts[1:]))
    known_=any(f in big for f in forms if len(f)>6)
    out.append((known_,r))
json.dump([dict(r,known=k) for k,r in out],open('research/sweep_2026-11_spain_nobility_aca/screen.json','w'),ensure_ascii=False,indent=0)
import collections
print(collections.Counter((k,r['sig'].split(',')[0]) for k,r in out))
