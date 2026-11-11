"""python dl.py <man> <n> [start] : fetch every image of a series at 900 px, crop the stand, save greyscale to scratch/<man>/<nnnnn>.jpg (resumable)"""
import os, sys, time
import rik
man, n = sys.argv[1], int(sys.argv[2]); a = int(sys.argv[3]) if len(sys.argv) > 3 else 1
d = f'{rik.SP}/pg/{man}'; os.makedirs(d, exist_ok=True)
for i in range(a, n + 1):
    p = f'{d}/{i:05d}.jpg'
    if os.path.exists(p): continue
    t = rik.crop(rik.img(man, i, 900, True)); t.save(p, quality=70); time.sleep(1.3)
print('done', man, flush=True)
