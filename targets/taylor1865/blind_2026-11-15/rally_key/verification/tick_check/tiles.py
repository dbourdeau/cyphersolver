# Make shuffled single-letter tiles for the blind tick check; mapping kept in tick_key.tsv (not shown to the helper)
import random
from PIL import Image, ImageOps
IMG = '../../../sources/raw/taylor1865_open_2026-11-15/nara_v11_0046.jpg'
pts = {6:(3400,2790),12:(1371,2908),16:(1921,2908),21:(2635,2895),34:(1934,3018),60:(1965,3245),64:(2575,3245),
       68:(3100,3245),75:(1475,3363),76:(1550,3363),79:(2067,3363),81:(2370,3365),96:(2850,3467),107:(1510,3615)}
im = Image.open(IMG).convert('L'); order = sorted(pts); random.Random(7).shuffle(order)
with open('tick_key.tsv', 'w') as f:
    for i, p in enumerate(order, 1):
        x, y = pts[p]; t = ImageOps.autocontrast(im.crop((x-75, y-70, x+75, y+60)), cutoff=1)
        t.resize((t.width*3, t.height*3)).save(f'tickcheck/T{i:02d}.jpg', quality=92); f.write(f'T{i:02d}\t{p}\n')
