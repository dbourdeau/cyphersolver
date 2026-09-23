import json,requests,concurrent.futures
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
p=Path('r4817'); cs=json.load(open(p/'manifest.json'))['sequences'][0]['canvases']
def get(c):
    name=c['@id'].split('/')[-1]; path=p/(name+'.jpg')
    if not path.exists(): path.write_bytes(requests.get(c['images'][0]['resource']['@id']).content)
    return name,c['label'],path
rows=list(concurrent.futures.ThreadPoolExecutor(8).map(get,cs))
for start in range(0,len(rows),12):
    sheet=Image.new('RGB',(1600,1800),'white'); draw=ImageDraw.Draw(sheet)
    for k,(name,label,path) in enumerate(rows[start:start+12]):
        im=Image.open(path); im.thumbnail((395,550)); x=(k%4)*400;y=(k//4)*600
        sheet.paste(im,(x,y+30));draw.text((x+8,y+8),f'{name} page {label}',fill='black')
    sheet.save(p/f'contact-{start}.jpg')
print(len(rows),'pages')
pf=json.loads((p/'profile.json').read_text(encoding='utf8'))
pf['solution'].extend([{'kind':'reading','what':'Full-resolution image resolves the apparent UND as VOM: underlined small circle is O, triple angles M; triangle serves U/V. Thus ram gall, not gall and ram.','result':'worked'},{'kind':'verification','what':'All five lines read with same substitution; literal GEFAE remains a likely scribal error for GEFAS, to be preserved separately from editorial correction.','result':'partial'},{'kind':'literature search','what':'Exact-phrase searches for ram gall / hemispherical vessel / furnace-scales found no independent text match.','result':'failed'}])
(p/'profile.json').write_text(json.dumps(pf,indent=2,ensure_ascii=False),encoding='utf8')
