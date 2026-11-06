"""python rik_pick.py <man> <name.jpg> 36,38,41 [tw=700] -> selected images, two columns."""
import os
import sys
import time

from rik_common import SP, grid, img

man, name, idx = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(',')]
tw = int(sys.argv[4]) if len(sys.argv) > 4 else 700
tiles = []
for i in idx:
    tiles.append(img(man, i, tw))
    time.sleep(0.9)
print(grid(tiles, idx, 2, tw, os.path.join(SP, name)))
