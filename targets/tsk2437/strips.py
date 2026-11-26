"""Overview strips of each line band (0.5x) for locating lines and extents."""
import os
import cv2
import win

bands = {'2': (1120, 1400), '3': (1900, 2150), '45': (2150, 2650), '6': (3200, 3560), '7': (4150, 4450), '8': (5150, 5600)}
g = win.load()
for k, (a, b) in bands.items():
    c = win.render(g, 1400, a, 5200, b, 0.5, 'flat')
    cv2.imwrite(os.path.join(win.HERE, 'img', 'w', 's%s.png' % k), c)
