"""python rik_sheet3.py <man> <n> [samples=15] [start=1] [end=n] [tw=600] [tag] -> 3-column contact sheet at 600 px a tile,
large enough to tell number-code rows from handwriting (a 300-px tile is not: a page of mixed digit groups and words reads
as dense text). ~1 request/s."""
import os
import sys
import time

from rik_common import SP, grid, img

man, n = sys.argv[1], int(sys.argv[2])
samples = int(sys.argv[3]) if len(sys.argv) > 3 else 15
start = int(sys.argv[4]) if len(sys.argv) > 4 else 1
end = int(sys.argv[5]) if len(sys.argv) > 5 else n
tw = int(sys.argv[6]) if len(sys.argv) > 6 else 600
tag = sys.argv[7] if len(sys.argv) > 7 else 'L'
step = max(1, (end - start) / samples)
idx = sorted({int(round(start + i * step)) for i in range(samples) if start + i * step <= end})
tiles = []
for i in idx:
    tiles.append(img(man, i, tw))
    time.sleep(0.9)
print(grid(tiles, idx, 3, tw, os.path.join(SP, f'{man}_{start}_{end}_{tag}.jpg')))
