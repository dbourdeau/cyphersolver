from pathlib import Path
from PIL import Image, ImageOps
from datetime import datetime,timezone
from hashlib import sha256
import csv
d=Path(__file__).resolve().parent
raw=d.parents[2]/'sources/raw/codex_2026-11-17b/gifford_may_close/20_complete.jpg'
areas={'top':(1390,35,2360,645),'middle':(1390,645,2360,1300)}
spans={'top':[(249,103,365,129),(532,107,618,128),(638,107,748,132),(84,133,149,157),(866,162,949,180),(520,180,622,202),(81,214,216,238),(871,228,954,250),(82,268,248,292),(275,265,396,288),(467,253,673,280),(84,301,210,326),(292,290,463,318)],'middle':[(91,34,179,57),(329,16,438,43),(532,10,649,32),(866,12,961,33),(95,59,293,85),(85,96,164,117),(440,71,670,99),(838,61,947,82),(94,118,253,145),(728,98,848,124),(520,126,617,149),(95,179,208,202),(227,164,319,192),(657,142,806,167),(568,207,658,232),(737,198,843,221),(172,250,289,275),(305,241,397,270),(515,232,663,261),(557,265,663,293),(733,250,901,280)]}
src=Image.open(raw)
(d/'blind').mkdir(exist_ok=True)
with (d/'boxes.tsv').open('x',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(('group','region','left','top','right','bottom'))
 for region,coords in spans.items():
  im=src.crop(areas[region])
  for n,box in enumerate(coords,1):
   id=region[0].upper()+str(n).zfill(2);w.writerow((id,region,*box))
   tile=im.crop(box).resize(((box[2]-box[0])*3,(box[3]-box[1])*3))
   ImageOps.expand(tile,8,fill='white').save(d/'blind'/(id+'.png'))
