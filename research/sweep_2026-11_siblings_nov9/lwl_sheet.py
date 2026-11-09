"""lwl_sheet.py <series dir name e.g. 'Ber.A_M 41'> <prefix path Ber/Ber.A> n1 n2 ... -> contact sheet in scratchpad (thumb 260 px wide, 6 per row)"""
import sys, os, time, io, requests
from PIL import Image
name, pre = sys.argv[1], sys.argv[2]
ids = [int(x) for x in sys.argv[3:]]
SCR = 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/75de5c3e-f515-4461-8587-8e578d7e5174/scratchpad'
S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0'
ims = []
for n in ids:
    p = os.path.join(SCR, '%s_%03d.jpg' % (name.replace(' ', '_'), n))
    if not os.path.exists(p):
        u = 'https://www.lwl.org/325dig-download/Lesesaal-Digitalisate/C_Adelsarchive/%s/%s/%s_%03d.jpg' % (pre, name.replace(' ', '%20'), name.replace(' ', '%20'), n)
        r = S.get(u, timeout=90)
        if r.status_code != 200: print(n, r.status_code); 
        if r.status_code in (403, 429): sys.exit(1)
        if r.status_code != 200: continue
        open(p, 'wb').write(r.content); time.sleep(2.5)
    ims.append((n, Image.open(p)))
w = 260; cols = 6
th = [(n, i.resize((w, int(i.height * w / i.width)))) for n, i in ims]
H = max(i.height for n, i in th); rows = (len(th) + cols - 1) // cols
m = Image.new('RGB', (w * cols, H * rows), 'white')
from PIL import ImageDraw
d = ImageDraw.Draw(m)
for k, (n, i) in enumerate(th):
    m.paste(i, ((k % cols) * w, (k // cols) * H)); d.text(((k % cols) * w + 5, (k // cols) * H + 5), str(n), fill='red')
out = os.path.join(SCR, 'sheet_%s_%d.jpg' % (name.replace(' ', '_'), ids[0]))
m.save(out); print(out, m.size)
