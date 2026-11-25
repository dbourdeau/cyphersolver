"""Second round, step 3: page order, rotation review and tiles for the drawn sample (frame2/sample2.json).

  python prep2.py order            -> frame2/pages2.json: per document, page image paths in the order the reference
                                      transcription lists them (#IMAGE NAME lines; image id = the I-number), falling
                                      back to page number
  python prep2.py sheet OUT_DIR    -> contact sheets (thumbnails, numbered) for deciding rotation by eye; written outside
                                      the repository (DECODE images are not to be committed)
  python prep2.py tiles OUT_DIR    -> tiles as in prep_tiles.py (bands of 1,000 px, 90 px overlap, max 2,000 px wide),
                                      rotations from frame2/rotations2.json {"<doc>": {"<page index>": degrees cw}}
Document id: R<rec>. Tiles go to OUT_DIR, which must hold only images (the transcriber never sees the reference).
"""
import json
import os
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = None
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
F2 = HERE / "frame2"
MAXW, BAND, OVER = 2000, 1000, 90


def ref_path(x):
    if x["source"] == "disk":
        return ROOT / x["transcription"]
    return HERE / "decode_cache" / f"R{x['rec']}" / x["transcription"]


def image_paths(x):
    if x["source"] == "disk":
        return [ROOT / p for p in x["images"]]
    return [HERE / "decode_cache" / f"R{x['rec']}" / p for p in x["images"]]


def order():
    out = {}
    for x in json.load(open(F2 / "sample2.json"))["sample"]:
        imgs = image_paths(x)
        by_id = {re.search(r"_I(\d+)_", p.name).group(1): p for p in imgs}
        listed = []
        for line in open(ref_path(x), encoding="utf-8-sig", errors="replace"):
            m = re.match(r"\s*#IMAGE NAME\s*:\s*(.*)", line, re.I)
            if m and not re.search(r"\d\s*(-|–|to)\s*\S*\d", m.group(1)):  # skip ranges such as 5179.png - 5181.png
                for i in re.findall(r"(\d+)\.(?:png|jpe?g)", m.group(1), re.I):
                    if i in by_id and by_id[i] not in listed:
                        listed.append(by_id[i])
        rest = sorted([p for p in imgs if p not in listed], key=lambda p: int(re.search(r"_P(\d+)", p.name).group(1)))
        pages = listed + rest
        out[f"R{x['rec']}"] = {"stratum": x["stratum"], "source": x["source"], "reference": str(ref_path(x)),
                               "order_from_reference": len(listed), "pages": [str(p) for p in pages]}
    json.dump(out, open(F2 / "pages2.json", "w"), indent=1)
    print(len(out), "documents;", sum(1 for v in out.values() if v["order_from_reference"] == len(v["pages"])),
          "fully ordered from the reference;", sum(len(v["pages"]) for v in out.values()), "pages")


def sheet(out, only=None):
    os.makedirs(out, exist_ok=True)
    pages = json.load(open(F2 / "pages2.json"))
    if only:
        pages = {d: v for d, v in pages.items() if d in only}
    items = [(d, i, p) for d, v in pages.items() for i, p in enumerate(v["pages"], 1)]
    W, per = 300, 12
    for s in range(0, len(items), per):
        cells = []
        for d, i, p in items[s:s + per]:
            im = Image.open(p).convert("RGB")
            im.thumbnail((W, W))
            cells.append((f"{d} p{i}", im))
        cols = 4
        rows = (len(cells) + cols - 1) // cols
        canvas = Image.new("RGB", (cols * (W + 10), rows * (W + 30)), "white")
        dr = ImageDraw.Draw(canvas)
        for k, (lab, im) in enumerate(cells):
            x0, y0 = (k % cols) * (W + 10), (k // cols) * (W + 30)
            dr.text((x0 + 4, y0 + 2), lab, fill="red")
            canvas.paste(im, (x0, y0 + 24))
        canvas.save(os.path.join(out, f"sheet_{s // per + 1:02d}.jpg"), quality=80)
    print("sheets:", (len(items) + per - 1) // per, "in", out)


def tiles(out):
    os.makedirs(out, exist_ok=True)
    pages = json.load(open(F2 / "pages2.json"))
    rot = json.load(open(F2 / "rotations2.json")) if (F2 / "rotations2.json").exists() else {}
    for d, v in pages.items():
        for pi, p in enumerate(v["pages"], 1):
            im = Image.open(p).convert("RGB")
            r = rot.get(d, {}).get(str(pi), 0)
            if r:
                im = im.rotate(-r, expand=True)
            if im.width > MAXW:
                im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
            y, k = 0, 1
            while y < im.height:
                box = (0, y, im.width, min(im.height, y + BAND))
                im.crop(box).save(os.path.join(out, f"{d}_p{pi}_t{k}.jpg"), quality=90)
                if box[3] >= im.height:
                    break
                y += BAND - OVER
                k += 1
    print("tiles written to", out)


if __name__ == "__main__":
    {"order": order, "sheet": lambda: sheet(sys.argv[2], sys.argv[3:]), "tiles": lambda: tiles(sys.argv[2])}[sys.argv[1]]()
