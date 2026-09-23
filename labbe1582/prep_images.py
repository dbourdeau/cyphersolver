from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps


ROOT = Path(__file__).parent
IMAGES = ROOT / "images"

CROPS = {
    "f64_main": ("f64.jpg", (160, 70, 745, 990)),
    "f64_slip": ("f64.jpg", (735, 95, 1320, 435)),
    "f65_left": ("f65.jpg", (165, 390, 735, 985)),
    "f65_right": ("f65.jpg", (735, 70, 1385, 985)),
    "f77_cipher": ("f77.jpg", (760, 535, 1340, 700)),
    "f78_text": ("f78.jpg", (735, 55, 1385, 985)),
    "f79_cipher": ("f79.jpg", (160, 20, 745, 180)),
    "f79_text": ("f79.jpg", (160, 20, 1385, 985)),
    "f64_main_iiif": ("f64_iiif.jpg", (300, 100, 1530, 2050)),
    "f65_right_iiif": ("f65_iiif.jpg", (1460, 80, 2860, 2050)),
    "f77_cipher_iiif": ("f77_iiif.jpg", (1500, 1040, 2790, 1420)),
    "f79_cipher_iiif": ("f79_iiif.jpg", (280, 0, 1550, 400)),
    "f79_cipher_full_iiif": ("f79_iiif.jpg", (260, 0, 1740, 430)),
    "f77_cipher_full_iiif": ("f77_iiif.jpg", (1450, 980, 2950, 1460)),
    "f77_cipher_line1": ("f77_iiif.jpg", (1550, 1130, 2940, 1320)),
    "f77_cipher_line2": ("f77_iiif.jpg", (1500, 1280, 2910, 1450)),
    "f64_band1": ("f64_iiif.jpg", (260, 220, 1600, 650)),
    "f64_band2": ("f64_iiif.jpg", (260, 1180, 1600, 1740)),
    "f64_band3": ("f64_iiif.jpg", (260, 1650, 1600, 2040)),
    "f65_band1": ("f65_iiif.jpg", (1420, 220, 2940, 820)),
    "f65_band2": ("f65_iiif.jpg", (1420, 700, 2940, 1320)),
    "f65_band3": ("f65_iiif.jpg", (1420, 1200, 2940, 2020)),
    "f66_right": ("f66_iiif.jpg", (1490, 40, 2810, 1770)),
    "f66_left": ("f66_iiif.jpg", (300, 240, 1520, 1850)),
    "f77_c1a": ("f77_iiif.jpg", (1550, 1180, 2250, 1300)),
    "f77_c1b": ("f77_iiif.jpg", (2220, 1180, 2910, 1300)),
    "f77_c2a": ("f77_iiif.jpg", (1510, 1270, 2230, 1410)),
    "f77_c2b": ("f77_iiif.jpg", (2190, 1270, 2890, 1410)),
    "f79_c1a": ("f79_iiif.jpg", (280, 80, 980, 210)),
    "f79_c1b": ("f79_iiif.jpg", (930, 80, 1610, 210)),
    "f79_c2a": ("f79_iiif.jpg", (280, 160, 980, 290)),
    "f79_c2b": ("f79_iiif.jpg", (930, 160, 1610, 290)),
    "f79_c3a": ("f79_iiif.jpg", (280, 240, 980, 370)),
    "f79_c3b": ("f79_iiif.jpg", (930, 240, 1610, 370)),
    "fr3995_key": ("../src/fr3995_f10.jpg", (1400, 0, 3000, 2131)),
}


for name, (filename, box) in CROPS.items():
    image = Image.open(IMAGES / filename).convert("L").crop(box)
    if name == "fr3995_key":
        image = image.rotate(90, expand=True)
    image = ImageOps.autocontrast(image, cutoff=1)
    image = ImageEnhance.Contrast(image).enhance(1.45)
    scale = 2 if "iiif" in name else 3
    image = image.resize((image.width * scale, image.height * scale))
    image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=180, threshold=3))
    image.save(IMAGES / f"{name}_enhanced.png")


# Overlapping reading tiles keep each handwritten digit near its native size in
# a 2048-pixel viewer; wide page crops otherwise shrink the figures too far.
for page, halves, y0, y1 in [
    ("f64", [(260, 950), (900, 1560)], 220, 1810),
    ("f65", [(1430, 2180), (2100, 2850)], 190, 1430),
    ("f66", [(260, 950), (900, 1550)], 170, 370),
]:
    source = Image.open(IMAGES / f"{page}_iiif.jpg").convert("L")
    for row, top in enumerate(range(y0, y1, 180), 1):
        for side, (left, right) in enumerate(halves, 1):
            crop = source.crop((left, top, right, min(top + 240, source.height)))
            crop = ImageOps.autocontrast(crop, cutoff=1)
            crop = ImageEnhance.Contrast(crop).enhance(1.45)
            crop = crop.resize((crop.width * 2, crop.height * 2))
            crop = crop.filter(ImageFilter.UnsharpMask(radius=2, percent=180, threshold=3))
            crop.save(IMAGES / f"{page}_tile{row:02d}{side}_enhanced.png")

source = Image.open(IMAGES / "f77_iiif.jpg").convert("L")
for row, top in enumerate(range(80, 1670, 210), 1):
    crop = source.crop((1570, top, 2780, min(top + 280, source.height)))
    crop = ImageOps.autocontrast(crop, cutoff=1)
    crop = ImageEnhance.Contrast(crop).enhance(1.35)
    crop = crop.resize((crop.width * 2, crop.height * 2))
    crop = crop.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    crop.save(IMAGES / f"f77_read{row:02d}.png")

for page, halves, y0, y1 in [
    ("f63", [(2960, 4360), (4230, 5700)], 370, 3650),
    ("f64", [(530, 1850), (1760, 3080)], 400, 3610),
    ("f65", [(2900, 4310), (4190, 5680)], 360, 2930),
]:
    source = Image.open(IMAGES / f"{page}_6000.jpg").convert("L")
    for row, top in enumerate(range(y0, y1, 300), 1):
        for side, (left, right) in enumerate(halves, 1):
            crop = source.crop((left, top, right, min(top + 390, source.height)))
            crop = ImageOps.autocontrast(crop, cutoff=1)
            crop = ImageEnhance.Contrast(crop).enhance(1.4)
            crop = crop.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=2))
            crop.save(IMAGES / f"{page}_hi{row:02d}{side}.png")

for page, halves, top, bottom in [
    ("f77", [(3200, 4600), (4500, 5800)], 2380, 2810),
    ("f79", [(520, 1900), (1800, 3220)], 250, 740),
]:
    source = Image.open(IMAGES / f"{page}_6000.jpg").convert("L")
    for side, (left, right) in enumerate(halves, 1):
        crop = source.crop((left, top, right, bottom))
        crop = ImageOps.autocontrast(crop, cutoff=1)
        crop = ImageEnhance.Contrast(crop).enhance(1.5)
        crop.save(IMAGES / f"{page}_cipher_hi{side}.png")
