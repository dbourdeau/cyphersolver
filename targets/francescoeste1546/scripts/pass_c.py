"""Third blind sign pass on c. 42r (c0): each line in two halves sent separately at full size, same legend, no key, no clear.
usage: pass_c.py OUT"""
import sys, io, base64
import os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from agent import ask
from PIL import Image, ImageOps
import bands, pass_blind_prompt as pp
im = Image.open(os.path.join(ROOT, 'scans', 'c0_full.jpg')).convert('L')
X0, X1 = bands.X0, bands.X1; mid = (X0 + X1) // 2
res = []
for i, c in enumerate(bands.LINES['c0']):
    out = []
    for k, (a, b) in enumerate(((X0, mid + 20), (mid - 20, X1))):
        h = ImageOps.autocontrast(im.crop((a, c - bands.HH_UP, b, c + bands.HH_DN)), cutoff=1).convert('RGB')
        bb = io.BytesIO(); h.save(bb, 'JPEG', quality=92)
        t, u = ask(pp.P.format(leg=pp.LEG), image_b64=base64.b64encode(bb.getvalue()).decode(), max_tokens=1500)
        ls = [l for l in t.strip().splitlines() if l.strip()]; out.append(ls[-1] if ls else '')
    res.append(f'c0L{i:02d}\t' + ' | '.join(out)); print(i, flush=True)
open(sys.argv[1], 'w', encoding='utf8').write('\n'.join(res) + '\n')
