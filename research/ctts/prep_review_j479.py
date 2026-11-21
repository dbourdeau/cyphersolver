"""Review sheets for correcting the T-S NS J479 CTTS project by hand (the files that CTTS restores a project from).

For each band: overlay_final/<band>.png (the band 2x enlarged, boxes from boxes_final.json numbered, a pixel ruler in
band pixels every 50 px, box colour = status: green agree, orange disagree, red unmatched, blue split) and one line in
review.json with the boxes (n, x, y, w, h, label, status) and the transcription tokens in box order. Pixel positions
in the sheets are band pixels (the 2x enlargement is divided out in the ruler).
"""
import json, re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

P = Path(__file__).parent / 'projects' / 'tsnsj479'
TR = Path(__file__).resolve().parents[2] / 'targets' / 'tsnsj479'
boxes = json.load(open(P / 'boxes_final.json', encoding='utf-8'))
labels = json.load(open(P / 'labels_final.json', encoding='utf-8'))
status = json.load(open(P / 'status_final.json'))
orders = json.load(open(P / 'orders.json'))
T = {}
for side in (1, 2):
    for l in open(TR / f'tr_side{side}.md', encoding='utf-8'):
        m = re.match(r'(S\d[LVU]\d\d):\s*(.*)', l)
        if m:
            T[m.group(1)] = [t for t in m.group(2).split() if t != '|']
COL = {'agree': (0, 150, 0), 'disagree': (230, 130, 0), 'unmatched': (220, 0, 0), 'split': (0, 90, 220)}
try:
    f = ImageFont.truetype('arial.ttf', 20); fs = ImageFont.truetype('arial.ttf', 14)
except OSError:
    f = fs = ImageFont.load_default()
(P / 'overlay_final').mkdir(exist_ok=True)
review = {}
for img, bx in boxes.items():
    r = img[:-4]; im = Image.open(P / 'images' / img).convert('RGB')
    S = 2; im2 = im.resize((im.width * S, im.height * S), Image.LANCZOS)
    pad = 40; canvas = Image.new('RGB', (im2.width, im2.height + pad), 'white'); canvas.paste(im2, (0, pad))
    d = ImageDraw.Draw(canvas)
    for x in range(0, im.width, 50):
        d.line((x * S, 0, x * S, pad - 4), fill=(0, 0, 0)); d.text((x * S + 2, 2), str(x), fill=(0, 0, 0), font=fs)
    for k, b in enumerate(bx):
        c = COL[status[img][k]]
        d.rectangle((b['x'] * S, b['y'] * S + pad, (b['x'] + b['w']) * S, (b['y'] + b['h']) * S + pad), outline=c, width=2)
        d.text((b['x'] * S + 2, b['y'] * S + pad - 20 if b['y'] * S > 20 else b['y'] * S + pad + b['h'] * S), str(b['n']), fill=c, font=f)
    canvas.save(P / 'overlay_final' / img)
    toks = T.get(r, [])
    toks = toks[::-1] if orders.get(r) == 'rev' else toks
    review[img] = dict(band=r, size=list(im.size), tokens_in_box_order=toks,
                       boxes=[dict(n=b['n'], x=b['x'], y=b['y'], w=b['w'], h=b['h'], label=labels[img][str(b['n'])], status=status[img][k]) for k, b in enumerate(bx)])
json.dump(review, open(P / 'review.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(len(review), 'sheets')
