"""Render the corpus glyph ids with the indus-website font, as labelled contact sheets.

Usage: python render_glyphs.py path/to/sk_indus_script-webfont.ttf [outdir] [glyph ids...]
With no glyph ids, every glyph that occurs in data/corpus.tsv is drawn, most
frequent first, 80 to a sheet (sheet_01.png, ...), each cell labelled
"id  count". With ids, one sheet 'pick.png' of those glyphs is drawn.
"""
import csv
import os
import sys
from collections import Counter

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    cps = {}
    with open(os.path.join(HERE, 'data', 'glyphs.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            cps[r['glyph']] = ''.join(chr(int(c, 16)) for c in r['codepoints'].split())
    freq = Counter()
    with open(os.path.join(HERE, 'data', 'corpus.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            freq.update(g for g in r['signs_visual'].split() if g != '0')
    return cps, freq


def sheet(ids, cps, freq, font, small, path, cols=10, cw=150, ch=130):
    rows = (len(ids) + cols - 1) // cols
    img = Image.new('RGB', (cols * cw, rows * ch), 'white')
    d = ImageDraw.Draw(img)
    for k, g in enumerate(ids):
        x, y = (k % cols) * cw, (k // cols) * ch
        d.rectangle([x, y, x + cw - 1, y + ch - 1], outline=(200, 200, 200))
        d.text((x + 8, y + 10), cps.get(g, '?'), font=font, fill='black')
        d.text((x + 4, y + ch - 20), '%s  n=%d' % (g, freq[g]), font=small, fill=(180, 0, 0))
    img.save(path)


def main():
    ttf = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, 'glyphs')
    os.makedirs(out, exist_ok=True)
    cps, freq = load()
    font = ImageFont.truetype(ttf, 72)
    small = ImageFont.truetype('arial.ttf', 15)
    if len(sys.argv) > 3:
        sheet(sys.argv[3:], cps, freq, font, small, os.path.join(out, 'pick.png'))
        return
    ids = [g for g, _ in freq.most_common()]
    for i in range(0, len(ids), 80):
        sheet(ids[i:i + 80], cps, freq, font, small,
              os.path.join(out, 'sheet_%02d.png' % (i // 80 + 1)))
    print(len(ids), 'glyphs drawn to', out)


if __name__ == '__main__':
    main()
