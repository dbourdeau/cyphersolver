"""How strongly each write-up's lead figure shows under its hero (style.css .hero-ms; inserted by _build_site.py).

A lead figure is a crop of a manuscript, a microfilm frame or a printed page, and the same opacity does not suit them
all: a grey-green photograph multiplies into a murky block on the light theme, a white page screens into a glare on the
dark one, and a tight black-on-white crop puts heavy strokes behind the text. This measures each figure as the hero
crops it and writes docs/_hero_backdrops.json:

    {"<slug>": {"l": 0.72, "d": 1.0}, ...}      l, d: factors on the light and the dark theme's opacity, 0.45 to 1

Run it after adding or replacing a lead figure:   python docs/_hero_backdrops.py
Entries can also be set by hand and are kept on the next run: "skip": true leaves the hero plain, "pos": "50% 10%"
moves the crop (CSS object-position), "keep": true stops this script from recomputing l and d.
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).parent
OUT = HERE / '_hero_backdrops.json'
EXT = ('.jpg', '.jpeg', '.png', '.webp')

def measure(path):
    """Mean and spread of luminance over the part the hero shows: a portrait cut, centred, 30% from the top."""
    from PIL import Image, ImageStat
    im = Image.open(path).convert('L')
    w, h = im.size; ar = 3 / 4
    if w / h > ar:
        nw = int(h * ar); x = (w - nw) // 2; im = im.crop((x, 0, x + nw, h))
    else:
        nh = int(w / ar); y = int((h - nh) * .30); im = im.crop((0, y, w, y + nh))
    st = ImageStat.Stat(im.resize((150, 200)))
    return st.mean[0], st.stddev[0]

def factors(mean, sd):
    clamp = lambda v: round(max(.45, min(1.0, v)), 2)
    heavy = .7 if sd > 60 else .85 if sd > 48 else 1.0     # a tight, bold crop puts heavy strokes behind the title
    return clamp(mean / 190 * heavy), clamp(165 / mean * heavy)

def main():
    sys.path.insert(0, str(HERE))
    from _manifest import IMAGES
    old = json.loads(OUT.read_text(encoding='utf-8')) if OUT.exists() else {}
    new = {}
    for slug in sorted(IMAGES):
        im = IMAGES[slug]
        if not im or not im[0].lower().endswith(EXT) or not (HERE / im[0]).exists(): continue
        rec = dict(old.get(slug, {}))
        if not rec.get('keep'):
            rec['l'], rec['d'] = factors(*measure(HERE / im[0]))
        new[slug] = rec
    OUT.write_text(json.dumps(new, indent=0, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    print(f'{len(new)} lead figures measured; {sum(1 for r in new.values() if r["l"] < 1)} toned down on the light theme, '
          f'{sum(1 for r in new.values() if r["d"] < 1)} on the dark; {sum(1 for r in new.values() if r.get("skip"))} skipped by hand')

if __name__ == '__main__':
    main()
