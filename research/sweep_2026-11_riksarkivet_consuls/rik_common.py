"""Shared helpers for the Riksarkivet consular volumes paging sweep (Nov 2026).
lbiiif returns 403 to scripts for the 4000xxxx image series unless the request carries Referer: https://sok.riksarkivet.se/."""
import io
import os
import re
import time

import requests
from PIL import Image, ImageDraw

H = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://sok.riksarkivet.se/'}
SP = os.environ.get('RIK_SP', r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\018b508d-1df1-440f-b1ab-1675801c41a6\scratchpad\rikcons')
os.makedirs(SP, exist_ok=True)


def dao(ref):
    """Image-series id for a reference code, from the APE EAD (the jsonld no longer carries it)."""
    r = requests.get('https://oai-pmh.riksarkivet.se/OAI/?verb=GetRecord&identifier=' + ref + '&metadataPrefix=oai_ape_ead',
                     headers=H, timeout=60)
    m = re.search(r'bildvisning/([0-9A-Z]+)', r.text)
    return m.group(1) if m else None


def count(man):
    j = requests.get(f'https://lbiiif.riksarkivet.se/arkis!{man}/manifest', headers=H, timeout=60).json()
    return len(j.get('items') or j.get('sequences', [{}])[0].get('canvases') or [])


def img(man, i, tw):
    u = f'https://lbiiif.riksarkivet.se/arkis!{man}_{i:05d}/full/{tw},/0/default.jpg'
    for a in range(3):
        try:
            r = requests.get(u, headers=H, timeout=90)
            if r.status_code == 200:
                return Image.open(io.BytesIO(r.content)).convert('L')
        except Exception:
            pass
        time.sleep(2)
    return Image.new('L', (tw, int(tw * 0.75)), 255)


def grid(tiles, labels, cols, tw, path):
    # tall single-page images would stretch every row: fit each tile in a tw x 0.75 tw box
    cap = int(tw * 0.75)
    tiles = [t if t.size[1] <= cap else t.resize((max(1, int(t.size[0] * cap / t.size[1])), cap)) for t in tiles]
    th = max(t.size[1] for t in tiles)
    rows = (len(tiles) + cols - 1) // cols
    out = Image.new('L', (cols * tw, rows * th), 200)
    for k, (t, lab) in enumerate(zip(tiles, labels)):
        d = ImageDraw.Draw(t)
        d.rectangle([0, 0, 44, 16], fill=255)
        d.text((2, 2), str(lab), fill=0)
        out.paste(t, ((k % cols) * tw, (k // cols) * th))
    out.save(path, quality=70)
    return path
