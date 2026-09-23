"""Render corpus texts as rows of glyphs (in the drawn, right-to-left layout), for comparing
the ICIT transcriptions with published drawings such as Parpola 1994 Fig. 7.14.

Usage: python render_texts.py font.ttf out.png TYPE     e.g. TAB:C   (all distinct texts of
       that object type, most frequent first, with count, motifs and CISI numbers)
"""
import sys
from collections import Counter, defaultdict

from PIL import Image, ImageDraw, ImageFont

from render_glyphs import load as load_glyphs
from signs import load


def main(ttf, out, typ):
    cps, _ = load_glyphs()
    rows = [r for r in load() if r['flat'] and r['type'] == typ]
    groups = defaultdict(list)
    for r in rows:
        groups[r['signs_visual']].append(r)
    items = sorted(groups.items(), key=lambda x: -len(x[1]))
    font = ImageFont.truetype(ttf, 40)
    small = ImageFont.truetype('arial.ttf', 13)
    H = 64
    img = Image.new('RGB', (1500, H * len(items) + 10), 'white')
    d = ImageDraw.Draw(img)
    for i, (vis, rs) in enumerate(items):
        y = i * H + 5
        glyphs = ''.join(cps.get(g, '?') for g in vis.split() if g != '0')
        d.text((10, y), glyphs, font=font, fill='black')
        mot = Counter(r['motif'] or '-' for r in rs)
        label = 'x%d  read: %s  | %s | %s' % (
            len(rs), ' '.join(rs[0]['flat']), ', '.join('%s %d' % kv for kv in mot.most_common()),
            ' '.join(r['cisi'] for r in rs[:8] if r['cisi']))
        d.text((560, y + 8), label, font=small, fill=(150, 0, 0))
        d.line([(0, y + H - 4), (1500, y + H - 4)], fill=(220, 220, 220))
    img.save(out)
    print(len(items), 'texts')


if __name__ == '__main__':
    main(*sys.argv[1:4])
