"""Candidate sign boxes for scripts whose signs are separate strokes inside a word (invented sign alphabets such as
T-S NS J479), where segment.py merges whole words: one box per connected ink component, small marks (dots, ticks)
attached to the nearest larger component, specks dropped. Signs that the hand joins stay one box (to be split in
CTTS); signs drawn in two strokes stay two (to be merged). A first pass for correction, not a final segmentation.

  python segment_glyphs.py BAND_DIR [--min-area 120] [--mark-area 900]
  -> BAND_DIR/../boxes.json and BAND_DIR/../overlay/<band>.png (numbered boxes, left to right)
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from scipy import ndimage


def ink(gray):
    a = np.asarray(gray, dtype=np.float32)
    bg = np.asarray(gray.filter(ImageFilter.GaussianBlur(25)), dtype=np.float32)
    return ndimage.binary_opening((bg - a) > 32, iterations=1)


def boxes_of(mask, min_area, mark_area):
    lab, n = ndimage.label(ndimage.binary_closing(mask, iterations=2))
    objs = ndimage.find_objects(lab)
    areas = ndimage.sum(mask, lab, range(1, n + 1))
    comps = []
    for i, s in enumerate(objs):
        if areas[i] < min_area:
            continue
        comps.append(dict(x0=s[1].start, y0=s[0].start, x1=s[1].stop, y1=s[0].stop, a=float(areas[i])))
    big = [c for c in comps if c['a'] >= mark_area]
    small = [c for c in comps if c['a'] < mark_area]
    for m in small:                      # attach a mark to the big component nearest its centre
        cx, cy = (m['x0'] + m['x1']) / 2, (m['y0'] + m['y1']) / 2
        best, bd = None, 1e9
        for b in big:
            dx = max(b['x0'] - cx, 0, cx - b['x1']); dy = max(b['y0'] - cy, 0, cy - b['y1'])
            d = (dx * dx + dy * dy) ** .5
            if d < bd: best, bd = b, d
        if best is not None and bd < 70:
            best.update(x0=min(best['x0'], m['x0']), y0=min(best['y0'], m['y0']),
                        x1=max(best['x1'], m['x1']), y1=max(best['y1'], m['y1']))
        else:
            big.append(m)
    big.sort(key=lambda c: c['x0'])
    return [dict(line=1, x=c['x0'], y=c['y0'], w=c['x1'] - c['x0'], h=c['y1'] - c['y0'], n=k + 1)
            for k, c in enumerate(big)]


def main():
    bd = Path(sys.argv[1]); args = sys.argv[2:]
    min_area = int(args[args.index('--min-area') + 1]) if '--min-area' in args else 120
    mark_area = int(args[args.index('--mark-area') + 1]) if '--mark-area' in args else 900
    out = {}; ov = bd.parent / 'overlay'; ov.mkdir(exist_ok=True)
    try: font = ImageFont.truetype('arial.ttf', 22)
    except OSError: font = ImageFont.load_default()
    for p in sorted(bd.glob('*.png')):
        im = Image.open(p).convert('RGB'); bx = boxes_of(ink(im.convert('L')), min_area, mark_area)
        out[p.name] = bx
        d = ImageDraw.Draw(im)
        for b in bx:
            d.rectangle((b['x'], b['y'], b['x'] + b['w'], b['y'] + b['h']), outline=(220, 0, 0), width=2)
            d.text((b['x'] + 2, max(0, b['y'] - 24)), str(b['n']), fill=(0, 0, 220), font=font)
        im.save(ov / p.name)
        print(p.name, len(bx), 'boxes')
    json.dump(out, open(bd.parent / 'boxes.json', 'w'), indent=0)


if __name__ == '__main__':
    main()
