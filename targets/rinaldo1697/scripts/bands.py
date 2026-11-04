"""Cipher bands of c. 73r (full size). Each band is centre-HU..centre+HD, which cuts away most of the interlinear
decipherment (written about 110 rows above the centre). Line L01 is on scans/c0_top.jpg (origin y 1800), L02-L06
on scans/c0_cipher.jpg (origin y 2150), L07-L09 on scans/c0_cipher2.jpg (origin y 5150); x origin 700."""
from PIL import Image, ImageOps
LINES = [('L01', 'c0_top', 1800, 1975), ('L02', 'c0_cipher', 2150, 2236), ('L03', 'c0_cipher', 2150, 2496),
         ('L04', 'c0_cipher', 2150, 3268), ('L05', 'c0_cipher', 2150, 4048), ('L06', 'c0_cipher', 2150, 4318),
         ('L07', 'c0_cipher', 2150, 4579), ('L08', 'c0_cipher', 2150, 5106), ('L09', 'c0_cipher2', 5150, 5366),
         ('L10', 'c0_cipher2', 5150, 5637), ('L11', 'c0_cipher2', 5150, 5910)]
LINES_V = [('V01', 'c1_cipher', 1450, 1727), ('V02', 'c1_cipher', 1450, 1988), ('V03', 'c1_cipher', 1450, 2247), ('V04', 'c1_cipher', 1450, 2493), ('V05', 'c1_cipher', 1450, 2780), ('V06', 'c1_cipher', 1450, 3024), ('V07', 'c1_cipher', 1450, 3279), ('V08', 'c1_cipher', 1450, 3533), ('V09', 'c1_cipher', 1450, 3789), ('V10', 'c1_cipher', 1450, 4069), ('V11', 'c1_cipher', 1450, 4333), ('V12', 'c1_cipher', 1450, 4592), ('V13', 'c1_cipher', 1450, 4837), ('V14', 'c1_cipher', 1450, 5112), ('V15', 'c1_cipher', 1450, 5378), ('V16', 'c1_cipher', 1450, 5641), ('V17', 'c1_cipher', 1450, 5913)]
HU, HD = 62, 70
def band(name, img, oy, c, top_cut=HU, scale=0.5):
    im = Image.open(f'scans/{img}.jpg').convert('L')
    y = c - oy
    b = im.crop((0, max(0, y - top_cut), im.width, min(im.height, y + HD)))
    return ImageOps.autocontrast(b, cutoff=1).resize((int(b.width * scale), int(b.height * scale))).convert('RGB')
