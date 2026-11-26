"""Stack class contact sheets into one image. Usage: python montage.py <outfile> <csdir> <class> [class ...]"""
import os
import sys
import numpy as np
import cv2

out, d = sys.argv[1], sys.argv[2]
rows = []
for c in sys.argv[3:]:
    p = os.path.join(d, 'cls_%s_0.png' % c)
    im = cv2.imread(p)
    cv2.putText(im, c, (im.shape[1] - 60, im.shape[0] - 8), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
    rows.append(im)
w = max(r.shape[1] for r in rows)
rows = [np.pad(r, ((0, 0), (0, w - r.shape[1]), (0, 0)), constant_values=255) for r in rows]
cv2.imwrite(out, np.vstack(rows))
print(out, np.vstack(rows).shape)
