# usage: enhance.py : flattens background and stretches contrast on the blue channel of the full-resolution tiles
# (no server requests), enlarges 1.25x, writes scans/enh/<tile>.jpg. Reading aid for pale ink.
import glob, os
from PIL import Image, ImageFilter, ImageOps, ImageChops
for p in ['0078r','0078v','0079r','0174r','0174v','0175r','0175v']:
    for f in sorted(glob.glob(f'scans/{p}_t??.jpg')):
        im = Image.open(f).convert('RGB')
        b = im.split()[2]
        bg = b.filter(ImageFilter.GaussianBlur(40))
        d = ImageChops.subtract(bg, b)          # ink = bright
        d = d.point(lambda v: min(255, int(v * 2.0)))
        out = ImageOps.invert(d)
        out = out.resize((int(out.width*1.25), int(out.height*1.25)), Image.LANCZOS)
        out.save('scans/enh/' + os.path.basename(f), quality=88)
print(len(glob.glob('scans/enh/*.jpg')))
