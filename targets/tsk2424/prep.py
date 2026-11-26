"""Deskew + flatten the recto for transcription. Writes img/w/flat.png (deskewed, background-flattened, contrast-stretched)."""
import cv2, numpy as np, math, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs('img/w', exist_ok=True)
g = cv2.imread('img/recto.jpg', cv2.IMREAD_GRAYSCALE)
ang = math.degrees(math.atan(0.02))
H, W = g.shape
M = cv2.getRotationMatrix2D((W / 2, H / 2), ang, 1)
r = cv2.warpAffine(g, M, (W, H), flags=cv2.INTER_CUBIC, borderValue=200)
bg = cv2.medianBlur(r, 101).astype(np.float32)
d = np.clip((bg - r.astype(np.float32)) * 3.2, 0, 255)
flat = (255 - d).astype(np.uint8)
cv2.imwrite('img/w/flat.png', flat)
cv2.imwrite('img/w/deskew_gray.png', r)
ink = (bg - r) > 45
prof = ink[:, 300:3380].sum(1)
import scipy.signal as s
sm = np.convolve(prof, np.ones(25) / 25, 'same')
pk, _ = s.find_peaks(sm, distance=150, prominence=100)
print(list(pk), [int(sm[i]) for i in pk])
