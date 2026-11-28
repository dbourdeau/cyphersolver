"""grid.py <spec.json> <out.png> : vue compacte (signes seuls, 2x) des options puis des questions."""
import sys, json
sys.path.insert(0, '/Users/bdudout/Library/Python/3.9/lib/python/site-packages')
from PIL import Image, ImageDraw
IMG = '/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/ljs51/img/f%s_2343.jpg'
spec = json.load(open(sys.argv[1])); cache = {}
def crop(ref):
    segfile, idx = ref.rsplit(':', 1)
    segs = json.load(open(spec['segdir'] + '/' + segfile + '.json'))
    bs = [segs[int(i)]['box'] for i in idx.split('+')]
    b = [min(x[0] for x in bs) - 6, min(x[1] for x in bs) - 6, max(x[2] for x in bs) + 6, max(x[3] for x in bs) + 6]
    f = segfile.split('_')[0].replace('seg', '')
    cache.setdefault(f, Image.open(IMG % f).convert('RGB'))
    im = cache[f].crop(b); return im.resize((im.width * 2, im.height * 2))
items = [('Forme ' + o['id'], crop(o['ref'])) for o in spec['options']] + [('---', None)] + [(q['q'], crop(q['ref'])) for q in spec['questions']]
cols = 6; cw = 260; ch = 300
rows = []; cur = []
for it in items:
    if it[1] is None: rows.append(cur); cur = []; continue
    cur.append(it)
    if len(cur) == cols: rows.append(cur); cur = []
if cur: rows.append(cur)
P = Image.new('RGB', (cols * cw, len(rows) * ch), 'white'); d = ImageDraw.Draw(P)
for r, row in enumerate(rows):
    for c, (lab, im) in enumerate(row):
        im.thumbnail((cw - 10, ch - 30)); P.paste(im, (c * cw + 5, r * ch + 22)); d.text((c * cw + 5, r * ch + 5), lab, fill=(200, 0, 0))
P.save(sys.argv[2])
