"""Build contact sheets from imgs/. usage: sheets.py  -> sheets/t1_NNN.jpg, sheets/t2_NNN.jpg and sheets/index.json
Each cell: first image of the document (and the second, side by side, if present) with a caption 'pgpid shelfmark'."""
import csv, json, os, sys
prefix = sys.argv[1] if len(sys.argv) > 1 else 'b1'
usedp = S0 = '/tmp/claude-0/-home-user-cyphersolver/b1a9cfe8-0cc7-5c06-b209-188424217ec7/scratchpad/sheets/used.json'
from PIL import Image, ImageDraw, ImageFont
csv.field_size_limit(10**9)
S = '/tmp/claude-0/-home-user-cyphersolver/b1a9cfe8-0cc7-5c06-b209-188424217ec7/scratchpad'
rows = {x['pgpid']: x for x in csv.DictReader(open(S + '/pgpdump/documents.csv', encoding='utf-8-sig'))}
t = json.load(open(S + '/pgpdump/tiers.json'))
os.makedirs(S + '/sheets', exist_ok=True)
font = ImageFont.load_default()
def cell(pid, w, h):
    imgs = [S + '/imgs/%s_%d.jpg' % (pid, k) for k in (1, 2) if os.path.exists(S + '/imgs/%s_%d.jpg' % (pid, k))]
    c = Image.new('RGB', (w, h + 22), 'white'); d = ImageDraw.Draw(c)
    d.text((3, 3), '%s  %s' % (pid, rows[pid]['shelfmark'][:42]), fill=(200, 0, 0), font=font)
    if not imgs: return c
    if len(imgs) == 1:
        im = Image.open(imgs[0]).convert('RGB'); im.thumbnail((w, h)); c.paste(im, ((w - im.size[0]) // 2, 22))
    else:
        for i, p in enumerate(imgs):
            im = Image.open(p).convert('RGB'); im.thumbnail((w // 2 - 2, h)); c.paste(im, (i * (w // 2), 22))
    return c
index = {}
used = set(json.load(open(usedp))) if os.path.exists(usedp) else set()
for tier, per, cols, cw, ch in (('t1', 6, 3, 640, 760), ('t2', 8, 4, 480, 640)):
    ids = [p for p in t[tier] if p not in used and any(os.path.exists(S + '/imgs/%s_%d.jpg' % (p, k)) for k in (1, 2))]
    rws = per // cols
    for n in range(0, len(ids), per):
        grp = ids[n:n + per]
        sheet = Image.new('RGB', (cols * cw, rws * (ch + 22)), (230, 230, 230))
        for i, pid in enumerate(grp):
            sheet.paste(cell(pid, cw, ch), ((i % cols) * cw, (i // cols) * (ch + 22)))
        name = '%s_%s_%03d.jpg' % (prefix, tier, n // per); used.update(grp)
        sheet.save(S + '/sheets/' + name, quality=82); index[name] = grp
old = json.load(open(S + '/sheets/index.json')) if os.path.exists(S + '/sheets/index.json') else {}
old.update(index); json.dump(old, open(S + '/sheets/index.json', 'w')); json.dump(sorted(used), open(usedp, 'w'))
print(len(index), 'sheets', sum(len(v) for v in index.values()), 'docs')
