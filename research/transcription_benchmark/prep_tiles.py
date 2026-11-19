"""Phase 2 prep: cut each benchmark page image into overlapping horizontal bands an image reader can resolve.

Pages are rotated first where the photograph is sideways (hellen1752: clockwise 90). Tiles go to the scratchpad given as
argv[1], never into the repository, and the folder holds ONLY images, so a transcriber that is pointed at it cannot see
the human reference (which stays under targets/).

Run:  python research/transcription_benchmark/prep_tiles.py <out_dir> [doc ids to redo]
Note: ferdinand3 pages need 270 (pass 1 cut them at 90, upside down; its transcriber rotated its own copies).
"""
import os
import sys

from PIL import Image

Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
# doc id -> (target folder, [(page image, rotate clockwise degrees)])
DOCS = {
    "dandini_R72": ("dandini1580/decode", [("IMG_R72_I569_P1.jpg", 0)]),
    "hellen_R1049": ("hellen1752/decode", [("IMG_R1049_I5499_P1.png", 90), ("IMG_R1049_I5500_P2.png", 90),
                                           ("IMG_R1049_I5501_P3.png", 90)]),
    "santacroce_R6": ("santacroce1552/decode", [("IMG_R6_I69_P1.jpg", 0), ("IMG_R6_I70_P2.jpg", 0)]),
    "santacroce_R7": ("santacroce1552/decode", [("IMG_R7_I71_P1.jpg", 0), ("IMG_R7_I72_P2.jpg", 0)]),
    # second round: page order follows the DECODE reference (R1953 lists images 13447, 13448, 13446)
    "hellen_R1953": ("hellen1752/decode", [("IMG_R1953_I13447_P2.png", 90), ("IMG_R1953_I13448_P3.png", 90),
                                           ("IMG_R1953_I13446_P1.png", 90)]),
    "kauderbach_R2078": ("kauderbach1754/img", [(f"IMG_R2078_I{14896 + i}_P{i + 1}.png", 90) for i in range(5)]),
    "carpio_R1009": ("carpio1677/img", [("IMG_R1009_I5197_P1.png", 0), ("IMG_R1009_I5198_P2.png", 0),
                                        ("IMG_R1009_I5199_P3.png", 0)]),
    "carpio_R1010": ("carpio1677/img", [("IMG_R1010_I5200_P1.png", 0), ("IMG_R1010_I5201_P2.png", 0),
                                        ("IMG_R1010_I5202_P3.png", 0)]),
    "ferdinand_R1889": ("ferdinand3/img", [("IMG_R1889_I9350_P1.png", 270), ("IMG_R1889_I9351_P2.png", 270)]),
    "ferdinand_R1890": ("ferdinand3/img", [("IMG_R1890_I9352_P1.png", 270), ("IMG_R1890_I9353_P2.png", 270)]),
}
MAXW, BAND, OVER = 2000, 1000, 90


def main(out, only=None):
    os.makedirs(out, exist_ok=True)
    for doc, (folder, pages) in DOCS.items():
        if only and doc not in only:
            continue
        for pi, (name, rot) in enumerate(pages, 1):
            im = Image.open(os.path.join(ROOT, "targets", folder, name)).convert("RGB")
            if rot:
                im = im.rotate(-rot, expand=True)
            if im.width > MAXW:
                im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
            y, k = 0, 1
            while y < im.height:
                box = (0, y, im.width, min(im.height, y + BAND))
                im.crop(box).save(os.path.join(out, f"{doc}_p{pi}_t{k}.jpg"), quality=90)
                if box[3] >= im.height:
                    break
                y += BAND - OVER
                k += 1
            print(doc, "page", pi, im.size, "tiles", k)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])  # optional: document ids to tile; default all
