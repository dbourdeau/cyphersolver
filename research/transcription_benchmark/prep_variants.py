"""Check 4: tile the sensitivity-test documents under alternative setups.

  fullpage  one image per page (the whole page, rotated, at most 2000 px wide; no bands)
  band600   bands 600 px high with 60 px overlap, instead of 1000 / 90
(the third variant, a reworded prompt, uses the original tiles)

Usage: python prep_variants.py <out_dir>   -> <out_dir>/fullpage/*.jpg, <out_dir>/band600/*.jpg
"""
import os
import sys

from PIL import Image

import prep_tiles

Image.MAX_IMAGE_PIXELS = None
DOCS = ["santacroce_R7", "hellen_R1049", "carpio_R1009"]


def page(doc, pi):
    folder, pages = prep_tiles.DOCS[doc]
    name, rot = pages[pi]
    im = Image.open(os.path.join(prep_tiles.ROOT, "targets", folder, name)).convert("RGB")
    if rot:
        im = im.rotate(-rot, expand=True)
    if im.width > prep_tiles.MAXW:
        im = im.resize((prep_tiles.MAXW, round(im.height * prep_tiles.MAXW / im.width)), Image.LANCZOS)
    return im


def main(out):
    for cond in ("fullpage", "band600"):
        os.makedirs(os.path.join(out, cond), exist_ok=True)
    for doc in DOCS:
        for pi in range(len(prep_tiles.DOCS[doc][1])):
            im = page(doc, pi)
            im.save(os.path.join(out, "fullpage", f"{doc}_p{pi + 1}_t1.jpg"), quality=90)
            y, k = 0, 1
            while y < im.height:
                box = (0, y, im.width, min(im.height, y + 600))
                im.crop(box).save(os.path.join(out, "band600", f"{doc}_p{pi + 1}_t{k}.jpg"), quality=90)
                if box[3] >= im.height:
                    break
                y += 540
                k += 1
            print(doc, "page", pi + 1, im.size, "band600 tiles", k)


if __name__ == "__main__":
    main(sys.argv[1])
