import sys, os, shutil
from PIL import Image
R, G2, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
im = Image.open(os.path.join(R, '0019_502968547.jpg'))
shutil.copy(os.path.join(G2, 'S27.png'), os.path.join(out, 'sec11_s01.png'))
key = [('batch3','sec11_s01.png','seed:S27','','')]
y, y1, n = 1370, 1830, 0
while True:
    ye = min(y + 360, y1); n += 1
    name = f'sec12_s{n:02d}.png'; im.crop((0, y, im.width, ye)).save(os.path.join(out, name)); key.append(('batch3', name, '0019', y, ye))
    if ye >= y1: break
    y = ye - 80
with open(os.path.join(os.path.dirname(out), 'strip_key.tsv'), 'a') as fh:
    for r in key: fh.write('\t'.join(map(str, r)) + '\n')
print(key)
