"""Blind sign pass: an AI language-model agent copies each cipher line from a tight band image, using only the shape legend.
No key, no decipherment, no clear text is given. usage: pass_blind.py OUTFILE [SCALE]. Passes A and B were run with two different AI language-model agents"""
import sys, io, base64, json
import os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from agent import ask
import bands
LEG = open(os.path.join(ROOT, 'validation', 'legend.md'), encoding='utf8').read()
P = """The image shows ONE line of a 1546 cipher of invented signs, cut into two overlapping halves stacked top to bottom (read the top half, then the bottom half; they overlap by a few signs: do not copy the overlap twice).
Copy ONLY the cipher signs, left to right, using exactly these sign names (separate every sign by one space):
{leg}
Rules:
- copy every component as its own name (o + is two signs, not one);
- a digit or letter written small ABOVE a sign: write it right after that sign as ^digit (e.g. e^6); if only part of it is visible at the top edge write ^?;
- a bar/tilde over a sign: write ~ after it (h~); a struck-through group: write it inside ( ) ;
- commas or dots on the line: , or .
- a gap between word groups: write | ;
- ordinary cursive Italian words on the line: write [TXT] once for each run of them; ignore writing cut off at the top or bottom edge;
- a sign you cannot match: ? .
This is a shape copy only; do not guess meaning. Output the sign sequence on ONE line and nothing else."""
out = sys.argv[1]
sc = float(sys.argv[2]) if len(sys.argv) > 2 else 0.8
res = []
for n, p, c in bands.names():
    im = bands.band(p, c, sc)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=92)
    t, u = ask(P.format(leg=LEG), image_b64=base64.b64encode(b.getvalue()).decode(), max_tokens=1500)
    lines = [l for l in t.strip().splitlines() if l.strip()]
    res.append(f"{n}\t{lines[-1] if lines else ''}")
    print(n, u, flush=True)
    open(out, 'w', encoding='utf8').write('\n'.join(res) + '\n')
