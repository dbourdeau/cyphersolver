"""Montage of whole key cells: python tools/cellblock.py <sheet> <out> <cols> <blocks> [scale]   e.g. 274 o.png 0,1,2 0,1 6"""
import sys
from PIL import Image
sys.path.insert(0,'tools')
from cell import GEOM
def block(sheet, blocks, cols, scale=6):
    g = GEOM[sheet]; im = Image.open(g['f'])
    rows = []
    for b in blocks:
        parts = []
        for c in cols:
            x0, x1 = g['x'][c], g['x'][c+1]; y0, y1 = g['y'][b], g['y'][b+1]
            parts.append(im.crop((x0, y0, x1, y1)).resize((int((x1-x0)*scale), int((y1-y0)*scale)), Image.LANCZOS))
        W = sum(p.width for p in parts)+6*(len(parts)-1); H = max(p.height for p in parts)
        r = Image.new('L', (W, H), 128); x = 0
        for p in parts: r.paste(p, (x, 0)); x += p.width+6
        rows.append(r)
    W = max(r.width for r in rows); H = sum(r.height for r in rows)+6*(len(rows)-1)
    m = Image.new('L', (W, H), 128); y = 0
    for r in rows: m.paste(r, (0, y)); y += r.height+6
    return m
if __name__ == '__main__':
    sh, out, cols, blocks = sys.argv[1:5]; sc = float(sys.argv[5]) if len(sys.argv) > 5 else 6
    block(sh, [int(x) for x in blocks.split(',')], [int(x) for x in cols.split(',')], sc).save(out)
