"""Paging every image of a volume.

python page_vol.py fetch [man ...]   : fetch EVERY image of each unit (units.json order, or the given series) at 1200 px
                                       into <SP>/hi/<man>/<i>.jpg (skips images already there); ~1 request/s; log fetch.log
python page_vol.py sheets <man>      : contact sheets of 30 images (6 x 5) at 300 px a tile from the cache,
                                       <SP>/sheets/<man>_<a>-<b>.jpg
python page_vol.py multi <tag> <man> <man> ... : 30-up sheets across small volumes (label = series tail:image)
python page_vol.py big <man> 12,17   : chosen images from the cache, two to a row at 800 px (<SP>/big_<man>_<first>.jpg)

The 300-px sheets show whole pages or blocks of digits; single digit lines inside a clear letter only show at 600-800 px,
so every cached image also goes through digitscan.py (candidate digit runs) and the flagged images are viewed large."""
import json
import os
import sys
import time

from PIL import Image, ImageOps

from rik_common import SP, grid, img

HERE = os.path.dirname(os.path.abspath(__file__))
HI = os.path.join(SP, 'hi')
SHEETS = os.path.join(SP, 'sheets')
GAMMA = [int(255 * (v / 255) ** 1.8) for v in range(256)]


def path(man, i):
    return os.path.join(HI, man, f'{i}.jpg')


def fetch(units):
    for u in units:
        os.makedirs(os.path.join(HI, u['man']), exist_ok=True)
        t0 = time.time()
        got = 0
        for i in range(1, u['n'] + 1):
            p = path(u['man'], i)
            if os.path.exists(p):
                continue
            t = time.time()
            img(u['man'], i, 1200).save(p, quality=85)
            got += 1
            time.sleep(max(0.0, 1.0 - (time.time() - t)))
        with open(os.path.join(SP, 'fetch.log'), 'a', encoding='utf-8') as f:
            f.write(f"{u['man']}\t{u['n']}\tfetched {got}\t{time.time() - t0:.0f}s\tDONE\n")


def load(man, i, tw):
    # darken faint ink so digit rows show at 300 px: autocontrast, then gamma 1.8
    im = ImageOps.autocontrast(Image.open(path(man, i)).convert('L'), cutoff=1).point(GAMMA)
    return im.resize((tw, max(1, int(im.size[1] * tw / im.size[0]))))


def sheets(man):
    os.makedirs(SHEETS, exist_ok=True)
    n = max(int(f.split('.')[0]) for f in os.listdir(os.path.join(HI, man)))
    out = []
    for a in range(1, n + 1, 30):
        idx = [i for i in range(a, min(a + 30, n + 1)) if os.path.exists(path(man, i))]
        out.append(grid([load(man, i, 300) for i in idx], idx, 6, 300, os.path.join(SHEETS, f'{man}_{idx[0]}-{idx[-1]}.jpg')))
    return out


def multi(mans, tag):
    """Sheets of 30 across several small volumes; tiles labelled <last two digits of series>:<image>."""
    os.makedirs(SHEETS, exist_ok=True)
    items = []
    for man in mans:
        n = max(int(f.split('.')[0]) for f in os.listdir(os.path.join(HI, man)))
        items += [(man, i) for i in range(2, n) if os.path.exists(path(man, i))]  # skip label card and END card
    out = []
    for k in range(0, len(items), 30):
        chunk = items[k:k + 30]
        out.append(grid([load(m, i, 300) for m, i in chunk], [f'{m[-2:]}:{i}' for m, i in chunk], 6, 300,
                        os.path.join(SHEETS, f'multi_{tag}_{k // 30 + 1}.jpg')))
    return out


def big(man, idx, tw=800):
    return grid([load(man, i, tw) for i in idx], idx, 2, tw, os.path.join(SP, f'big_{man}_{idx[0]}.jpg'))


if __name__ == '__main__':
    units = json.load(open(os.path.join(HERE, 'units.json'), encoding='utf-8'))
    cmd = sys.argv[1]
    if cmd == 'fetch':
        sel = [u for u in units if len(sys.argv) < 3 or u['man'] in sys.argv[2:]]
        fetch(sel)
    elif cmd == 'sheets':
        print('\n'.join(sheets(sys.argv[2])))
    elif cmd == 'multi':
        print('\n'.join(multi(sys.argv[3:], sys.argv[2])))
    elif cmd == 'big':
        print(big(sys.argv[2], [int(x) for x in sys.argv[3].split(',')], int(sys.argv[4]) if len(sys.argv) > 4 else 800))
