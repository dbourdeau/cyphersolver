"""Survey of the digitised Durham Wingate Papers units for other Arabic-numeral leaves (step 2 of the crib search).

    python survey_durham.py <outdir>

Fetches the IIIF manifests of the four Nile Campaign units that cover the period of the note (SAD.250/1/1-58,
59-96, 97-133, 528-606), a 260 px thumbnail of every leaf (278 leaves, about 6 minutes at one request every 0.9 s) and
builds contact sheets with the shelfmarks written on them, to be looked through for leaves of numeral groups. Images go
to <outdir>, outside the repository. The 14 Nov 2026 pass found only SAD.250/1/550 itself (and the table 81).
"""
import json, os, subprocess, sys, time
from PIL import Image, ImageDraw

UNITS = {'u1': 't1mt148fh16v', 'u59': 't1m6969z078q', 'u97': 't1mmw22v5473', 'u528': 't2mqj72p714z'}


def sh(args):
    subprocess.run(args, check=False)


def main(out):
    os.makedirs(os.path.join(out, 'th'), exist_ok=True)
    allc = []
    for u, a in UNITS.items():
        url = f'https://iiif.durham.ac.uk/manifests/trifle/32150/{a[:2]}/{a[2:4]}/{a[4:6]}/{a}/manifest'
        p = os.path.join(out, f'{u}.json'); sh(['curl', '-s', '-m', '60', url, '-o', p]); time.sleep(1.5)
        for c in json.load(open(p))['sequences'][0]['canvases']:
            allc.append((c['label'], c['images'][0]['resource']['service']['@id']))
    for i, (lab, svc) in enumerate(allc):
        f = os.path.join(out, 'th', f'{i:03d}.jpg')
        if not (os.path.exists(f) and os.path.getsize(f) > 2000):
            sh(['curl', '-s', '-m', '40', f'{svc}/full/260,/0/default.jpg', '-o', f]); time.sleep(0.9)
    cols, rows, tw, th = 6, 4, 170, 215
    for s in range(0, len(allc), cols * rows):
        m = Image.new('RGB', (cols * tw, rows * (th + 14)), 'white'); d = ImageDraw.Draw(m)
        for k, i in enumerate(range(s, min(s + cols * rows, len(allc)))):
            try: im = Image.open(os.path.join(out, 'th', f'{i:03d}.jpg')).convert('RGB')
            except Exception: continue
            im.thumbnail((tw - 4, th - 2)); x, y = (k % cols) * tw, (k // cols) * (th + 14)
            m.paste(im, (x + 2, y + 14)); d.text((x + 3, y + 1), allc[i][0][:22], fill='red')
        m.save(os.path.join(out, f'sheet_{s // (cols * rows):02d}.png'))
    print(len(allc), 'leaves')


if __name__ == '__main__':
    main(sys.argv[1])
