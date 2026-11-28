"""plate.py <spec.json> <out.png>
Planche de formes : en haut les options (vignettes de formes, lettres A, B, C… ; aucun nom de lettre),
puis une question par ligne : contexte (ligne autour du signe, UN seul signe encadré) + le signe seul à 3x.
spec = {"title": str, "segdir": str, "options": [{"id":"A","ref":"<segfile>:<idx>"}...],
        "questions": [{"q": "Q1", "ref": "<segfile>:<idx>"}...]}
<segfile> = préfixe de sortie de segment.py (sans extension), relatif à segdir ; idx peut être "i+j" (fusion)."""
import sys, json
sys.path.insert(0, '/Users/bdudout/Library/Python/3.9/lib/python/site-packages')
from PIL import Image, ImageDraw
IMG = '/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/ljs51/img/f%s_2343.jpg'
spec = json.load(open(sys.argv[1])); out = sys.argv[2]
cache = {}
def page(f):
    if f not in cache: cache[f] = Image.open(IMG % f).convert('RGB')
    return cache[f]
def resolve(ref):
    segfile, idx = ref.rsplit(':', 1)
    segs = json.load(open(spec['segdir'] + '/' + segfile + '.json'))
    boxes = [segs[int(i)]['box'] for i in idx.split('+')]
    box = [min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes)]
    folio = segfile.split('_')[0].replace('seg', '')
    return folio, box
M = 8; SC = 3
def sign(ref):
    f, b = resolve(ref)
    im = page(f).crop((b[0] - M, b[1] - M, b[2] + M, b[3] + M))
    return im.resize((im.width * SC, im.height * SC), Image.LANCZOS)
def context(ref):
    f, b = resolve(ref)
    cx0, cx1 = b[0] - 220, b[2] + 220; cy0, cy1 = b[1] - 30, b[3] + 30
    im = page(f).crop((cx0, cy0, cx1, cy1)).copy()
    d = ImageDraw.Draw(im); d.rectangle([b[0] - cx0 - 4, b[1] - cy0 - 4, b[2] - cx0 + 4, b[3] - cy0 + 4], outline=(220, 0, 0), width=3)
    return im
rows = []
opt = [(o['id'], sign(o['ref'])) for o in spec['options']]
H = max(i.height for _, i in opt) + 40; Wd = sum(i.width + 30 for _, i in opt) + 30
r = Image.new('RGB', (Wd, H), 'white'); d = ImageDraw.Draw(r); x = 15
for k, i in opt:
    r.paste(i, (x, 30)); d.text((x, 5), 'Forme ' + k, fill=(0, 0, 0)); x += i.width + 30
rows.append(r)
for q in spec['questions']:
    c = context(q['ref']); s = sign(q['ref'])
    H = max(c.height, s.height) + 30; Wd = c.width + s.width + 60
    r = Image.new('RGB', (Wd, H), 'white'); d = ImageDraw.Draw(r)
    d.text((10, 5), q['q'] + ' : quelle forme ? (A, B, C…, ou « autre »)', fill=(0, 0, 0))
    r.paste(c, (10, 25)); r.paste(s, (c.width + 40, 25)); rows.append(r)
Wt = max(r.width for r in rows) + 20; Ht = sum(r.height + 12 for r in rows) + 50
P = Image.new('RGB', (Wt, Ht), 'white'); d = ImageDraw.Draw(P)
d.text((10, 10), spec['title'] + '  -  University of Pennsylvania, LJS 51, OPenn (PDM 1.0)', fill=(0, 0, 0)); y = 40
for r in rows:
    P.paste(r, (10, y)); y += r.height + 12
P.save(out); print(out, P.size)
