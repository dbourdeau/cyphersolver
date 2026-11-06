"""python rik_sheet.py <man> <n> [samples=24] [start=1] [end=n] [tw=300] -> contact sheet in SP. ~1 request/s."""
import os
import sys
import time

from rik_common import SP, grid, img

man, n = sys.argv[1], int(sys.argv[2])
samples = int(sys.argv[3]) if len(sys.argv) > 3 else 24
start = int(sys.argv[4]) if len(sys.argv) > 4 else 1
end = int(sys.argv[5]) if len(sys.argv) > 5 else n
tw = int(sys.argv[6]) if len(sys.argv) > 6 else 300
step = max(1, (end - start) / samples)
idx = sorted({int(round(start + i * step)) for i in range(samples) if start + i * step <= end})
tiles = []
for i in idx:
    tiles.append(img(man, i, tw))
    time.sleep(0.9)
print(grid(tiles, idx, 6, tw, os.path.join(SP, f'{man}_{start}_{end}.jpg')))
