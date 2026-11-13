"""Contact sheets of Rigsarkivet units with uniform tiles: python3 dksheets.py stride <bsid> ... (5x4 tiles of 400x300) -> scratch/dk/"""
import sys, os, time, ao
from PIL import Image, ImageDraw
out = '/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/nordic/dk'
os.makedirs(out, exist_ok=True)
st = int(sys.argv[1]); TW, TH, C, R = 400, 300, 5, 4
for b in sys.argv[2:]:
    ids = ao.refs(b); pick = list(range(1, len(ids), st))
    for s in range(0, len(pick), C * R):
        fn = f'{out}/{b}_s{st}_{pick[s]:04d}.jpg'
        if os.path.exists(fn): continue
        S = Image.new('RGB', (C * TW, R * TH), 'white')
        for k, i in enumerate(pick[s:s + C * R]):
            try: im = ao.image(ids[i], 800)
            except Exception as e: print('fail', i, e); continue
            im.thumbnail((TW, TH)); ImageDraw.Draw(im).rectangle([0, 0, 40, 12], fill='white'); ImageDraw.Draw(im).text((2, 0), str(i + 1), fill='red')
            S.paste(im, ((k % C) * TW, (k // C) * TH)); time.sleep(0.8)
        S.save(fn, quality=70); print(fn, flush=True)
