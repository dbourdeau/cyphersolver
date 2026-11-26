"""Crop single table entries from the rotated numeric key sheets (key/r272.png, key/r1295274.png, key/r1295276.png)."""
from PIL import Image, ImageDraw
import sys
GEOM = {
 '272': dict(f='key/r272.png', x=[283,368,455,541,627,711,798,884,969,1058,1145], y=[0,85,184,284,384,484,585,688]),
 '274': dict(f='key/r1295274.png', x=[257,338,422,507,592,678,763,849,934,1020,1108], y=[0,98,195,296,393,491,590,690]),
}
def strip(sheet, n, scale=7):
    g = GEOM[sheet]; im = Image.open(g['f'])
    b = (n-1)//100; c = (n-1)%10; r = ((n-1)%100)//10
    x0, x1 = g['x'][c], g['x'][c+1]
    y0, y1 = g['y'][b], g['y'][b+1]
    h = (y1-y0)/10.0 if b else (y1-y0)/10.0
    ya = int(y0 + r*h - 1); yb = int(y0 + (r+1)*h + 1)
    s = im.crop((x0, ya, x1, yb)).resize((int((x1-x0)*scale), int((yb-ya)*scale)), Image.LANCZOS)
    return s
def sheet(nums, sheetname, out, scale=7):
    ss = [strip(sheetname, n, scale) for n in nums]
    W = max(s.width for s in ss); H = sum(s.height for s in ss)
    m = Image.new('L', (W, H), 255); y = 0
    for s in ss: m.paste(s, (0, y)); y += s.height
    m.save(out)
if __name__ == '__main__':
    sh = sys.argv[1]; out = sys.argv[2]; nums = [int(x) for x in sys.argv[3:]]
    sheet(nums, sh, out)
