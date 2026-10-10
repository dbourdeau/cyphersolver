"""Draft visual alignment of Tomokiyo's token labels with the first manuscript line."""

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SOURCE = "cipher_f138.png"
TOKENS = "SP53_11_50b.txt"

im = cv2.imread(SOURCE, cv2.IMREAD_GRAYSCALE)
residual = cv2.GaussianBlur(im.astype(np.float32), (0, 0), 35) - im
y0, y1 = 450, 620
x0, x1 = 250, 5350
projection = (residual[y0:y1, x0:x1] > 18).sum(axis=0)
occupied = (projection > 4).astype(np.uint8).reshape(1, -1)
occupied = cv2.morphologyEx(
    occupied, cv2.MORPH_CLOSE, np.ones((1, 12), np.uint8)
).ravel()
edges = np.diff(np.pad(occupied, (1, 1)).astype(np.int16))
starts = np.where(edges == 1)[0]
ends = np.where(edges == -1)[0]
runs = [(int(x0 + a), int(x0 + b)) for a, b in zip(starts, ends) if b-a >= 8]

with open(TOKENS, encoding="utf-8") as handle:
    lines = [line.strip().strip(";").split(";") for line in handle if not line.startswith("#")]
labels = lines[0]

canvas = Image.new("RGB", (1200, ((len(runs)+9)//10)*180), "white")
draw = ImageDraw.Draw(canvas)
for i, (a, b) in enumerate(runs):
    crop = Image.fromarray(im[y0-15:y1+15, max(0,a-10):min(im.shape[1],b+10)])
    crop.thumbnail((100, 125))
    xx = (i % 10) * 120
    yy = (i // 10) * 180
    canvas.paste(crop, (xx + (100-crop.width)//2, yy+40))
    draw.text((xx+6, yy+5), f"{i+1}: {labels[i] if i < len(labels) else '?'}", fill="black")
    draw.text((xx+6, yy+22), f"x={a}-{b}", fill="black")
canvas.save("line1_segments.png")
print(f"runs={len(runs)} labels={len(labels)}")
print(runs)
