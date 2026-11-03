"""Read the contemporary interlinear decipherment (small Italian words written above each cipher line).
Run only after both blind sign passes were written. usage: gloss.py OUTFILE"""
import sys, io, base64
import os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from agent import ask
from PIL import Image, ImageOps
import bands
P = """This strip comes from an Italian letter of 1546. It shows a line of cipher signs (bottom) with a contemporary decipherment written above it in small cursive Italian (the interlinear clear). Some lines also have ordinary Italian words in the main line.
Transcribe:
G: the small interlinear Italian words above the cipher, left to right, one word per position, separated by ' | ' (keep abbreviations as written, e.g. V.Ex., S.M.ta; write a digit if one is written above a sign);
T: any ordinary full-size Italian words on the main (bottom) line, in order, separated by ' | ' (or - if none).
Output exactly two lines starting 'G:' and 'T:'."""
res = []
for n, p, c in bands.names():
    im = Image.open(f'scans/{p}_full.jpg').convert('L').crop((bands.X0, c - 150, bands.X1, c + 60))
    im = ImageOps.autocontrast(im, cutoff=1)
    W = im.width; mid = W // 2
    a = im.crop((0, 0, mid + 80, im.height)); b = im.crop((mid - 80, 0, W, im.height))
    o = Image.new('L', (a.width, a.height * 2 + 12), 255); o.paste(a, (0, 0)); o.paste(b, (0, a.height + 12))
    o = o.resize((int(o.width * 0.85), int(o.height * 0.85))).convert('RGB')
    bb = io.BytesIO(); o.save(bb, 'JPEG', quality=92)
    t, u = ask(P, image_b64=base64.b64encode(bb.getvalue()).decode(), max_tokens=800)
    g = [l for l in t.splitlines() if l.startswith('G:')]; tt = [l for l in t.splitlines() if l.startswith('T:')]
    res.append(f"{n}\tG\t{g[0][2:].strip() if g else ''}\n{n}\tT\t{tt[0][2:].strip() if tt else ''}")
    print(n, flush=True)
    open(sys.argv[1], 'w', encoding='utf8').write('\n'.join(res) + '\n')
