"""Contact sheets (4x3 thumbnails) of img/t7519/*.jpg into img/t7519_sheet_NN.jpg."""
import glob, os
from PIL import Image, ImageDraw
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
fs = sorted(glob.glob(os.path.join(D, "t7519", "[0-9]*.jpg")))
W, H, C, R = 420, 560, 4, 3
for s in range(0, len(fs), C * R):
    sheet = Image.new("RGB", (W * C, H * R), "white"); dr = ImageDraw.Draw(sheet)
    for k, f in enumerate(fs[s:s + C * R]):
        im = Image.open(f).convert("RGB"); im.thumbnail((W - 6, H - 20))
        x, y = (k % C) * W, (k // C) * H
        sheet.paste(im, (x + 3, y + 18)); dr.text((x + 5, y + 2), os.path.basename(f), fill="red")
    sheet.save(os.path.join(D, f"t7519_sheet_{s // (C * R) + 1:02d}.jpg"), quality=80)
print(len(fs))
