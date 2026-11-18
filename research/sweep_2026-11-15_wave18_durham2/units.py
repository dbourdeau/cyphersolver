"""python units.py : list every unit of the HIL finding aid (raw/hil.xml) with title, ref, dates, extent/microfilm and
digitised ark -> raw/units.json and units.tsv"""
import re, json, os, html
here = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(here, 'raw', 'hil.xml'), encoding='utf8', errors='replace').read()
parts = re.split(r'<div class="c\d+">', t)
out = []
for p in parts[1:]:
    m = re.search(r'<span class="utitle"[^>]*>(.*?)</span>', p, re.S)
    r = re.search(r'<b id="[^"]*">(HIL[^<]*)</b>\s*([^<]*)', p)
    if not r: continue
    title = html.unescape(re.sub('<[^>]+>', '', m.group(1))).strip() if m else ''
    arks = re.findall(r'ark:/32150/([a-z0-9]+)\.html', p)
    txt = html.unescape(re.sub(r'<[^>]+>', ' ', p)); txt = re.sub(r'\s+', ' ', txt)
    mf = re.search(r'Microfilm:\s*([^ ]+)', txt)
    out.append(dict(ref=r.group(1).strip(), dates=r.group(2).strip(), title=title, arks=arks, microfilm=mf.group(1) if mf else '', text=txt[:4000]))
json.dump(out, open(os.path.join(here, 'raw', 'units.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
with open(os.path.join(here, 'units.tsv'), 'w', encoding='utf8') as f:
    f.write('ref\tdates\ttitle\tdigitised_ark\n')
    for u in out: f.write('%s\t%s\t%s\t%s\n' % (u['ref'], u['dates'], u['title'], ' '.join(u['arks'])))
print(len(out))
