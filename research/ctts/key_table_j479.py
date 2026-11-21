"""Draw the sign table of the T-S NS J479 CTTS project in CTTS's symbol-type style: one coloured row per sign type, with the
cut-out image of signs of that type from the page. Only boxes where the blind first pass and the target's transcription
agree on the shape ("agree" in status_final.json) are shown, so the table is not a transcription copied onto itself.
Rows: the 22 base signs in alphabet order (with the Hebrew letter they carry), then variants.

  python key_table_j479.py OUT.jpg [--per-row 14]
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

P = Path(__file__).parent / 'projects' / 'tsnsj479'
OUT = sys.argv[1]
PER = int(sys.argv[sys.argv.index('--per-row') + 1]) if '--per-row' in sys.argv else 14
ORDER = 'I U E A N 4 c B d - < p P q w O 6 S X 9 C 7'.split()
HEB = dict(zip(ORDER, 'אבגדהוזחטיכלמנסעפצקרשת'))
HEB.update({'a': 'ת', 's': 'ר', '8': 'ר', '5': 'ר', 'Bc': 'ח', 'J': 'י', '<5': 'כ', 'e': 'ח', 'f': 'מ', 'b': 'ל', 't': 'ן'})   # y, n, o: no letter established
colors = [l.split(';')[0] for l in open(P / 'ctts' / 'colors.txt', encoding='utf-8') if l.strip()]
CORR = any(a.startswith('--corrected') for a in sys.argv)
SUF = '3' if '--corrected3' in sys.argv else ('2' if '--corrected2' in sys.argv else '')
boxes = json.load(open(P / (f'boxes_corrected{SUF}.json' if CORR else 'boxes_final.json'), encoding='utf-8'))
labels = json.load(open(P / (f'labels_corrected{SUF}.json' if CORR else 'labels_final.json'), encoding='utf-8'))
status = None if CORR else json.load(open(P / 'status_final.json'))
byt = {}
for img, bx in boxes.items():
    for k, b in enumerate(bx):
        lab = labels[img][str(b['n'])]
        if CORR:
            if lab[0] in '?_#':
                continue
        elif status[img][k] != 'agree':
            continue
        byt.setdefault(lab.rstrip('.?'), []).append((img, b))
ORDER2 = ['B', 'Bc', '-', 'J', '<', '<5']
BASE = [t for t in ORDER if t in byt]
types = []
for t in BASE:
    types.append(t)
    if t == 'B': types += [x for x in ('Bc',) if x in byt]
    if t == '-': types += [x for x in ('J',) if x in byt]
    if t == '<': types += [x for x in ('<5',) if x in byt]
types += sorted(t for t in byt if t not in ORDER and t not in ORDER2)
try:
    f = ImageFont.truetype('arial.ttf', 30); fh = ImageFont.truetype('arial.ttf', 26); fs = ImageFont.truetype('arial.ttf', 15)
except OSError:
    f = fh = fs = ImageFont.load_default()
H = 78; W = 1376; LW = 190
sheet = Image.new('RGB', (W, H * len(types) + 56), (250, 248, 242)); d = ImageDraw.Draw(sheet)
d.text((12, 14), 'Sign table: T-S NS J479 (Cambridge UL), corrected CTTS project, boxes not marked uncertain (model-made, not person-checked)' if CORR else 'Sign table: T-S NS J479 (Cambridge UL), boxes where the blind pass and the transcription agree', fill=(40, 40, 40), font=fs)
names = [l.split(';')[1] for l in open(P / 'ctts' / 'colors.txt', encoding='utf-8') if l.strip()]
y = 40; cache = {}
for t in types:
    d.rectangle((0, y, W, y + H - 4), fill=(235, 232, 224))
    # CTTS colours the symbol type; the swatch is that type's CTTS colour (JavaFX 0xRRGGBBAA)
    c = colors[names.index(t)] if t in names else '0x888888ff'
    d.rectangle((6, y + 6, 30, y + H - 10), fill=tuple(int(c[i:i + 2], 16) for i in (2, 4, 6)))
    d.text((40, y + 20), t, fill=(0, 0, 0), font=f)
    if t in HEB: d.text((112, y + 22), HEB[t], fill=(60, 60, 60), font=fh)
    d.text((152, y + 52), 'n=%d' % len(byt[t]), fill=(90, 90, 90), font=fs)
    x = LW
    for img, b in byt[t][:PER]:
        if img not in cache: cache[img] = Image.open(P / 'images' / img).convert('RGB')
        im = cache[img]
        pad = 4
        cr = im.crop((max(0, b['x'] - pad), max(0, b['y'] - pad), min(im.width, b['x'] + b['w'] + pad), min(im.height, b['y'] + b['h'] + pad)))
        s = min((H - 14) / cr.height, 84 / cr.width)
        cr = cr.resize((max(1, int(cr.width * s)), max(1, int(cr.height * s))), Image.LANCZOS)
        if x + cr.width > W - 6: break
        sheet.paste(cr, (x, y + (H - 4 - cr.height) // 2)); x += cr.width + 10
    y += H
sheet = sheet.crop((0, 0, W, y + 6))
sheet.save(OUT, quality=88)
print(OUT, sheet.size, len(types), 'types,', sum(len(v) for v in byt.values()), 'agreed boxes')
