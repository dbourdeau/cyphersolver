"""Ink row profile of a page region, to find cipher line centres. python profile.py img x0 x1 y0 y1"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
x0, x1, y0, y1 = map(int, sys.argv[2:6])
px = im.load()
prof = []
for y in range(y0, y1):
    prof.append(sum(1 for x in range(x0, x1, 2) if px[x, y] < 110))
# smooth
sm = [sum(prof[max(0, i-6):i+7]) / len(prof[max(0, i-6):i+7]) for i in range(len(prof))]
peaks = [i + y0 for i in range(8, len(sm)-8) if sm[i] == max(sm[i-8:i+9]) and sm[i] > 15]
print(peaks)
