# Cut cipher-line crops from the raw AIS images. Centres chosen by eye on ruler views (work/ruler.py) and the
# ink-profile peaks of work/seglines.py. Label prefix: P,Q = 8-2-24 img1,img2; N = 9-1-2 img2; M = 8-3-10 img1;
# S,E = 8-2-22 img3 (left page, second passage of the original), img4 (last passage).
from PIL import Image
R='./images/'  # the AIS images (not included; see README), saved as named below
O='./lines/'
JOBS=[('P','8-2-24_img1.jpg',2100,3561,42,44,[542,614,680,752,829,895,972,1037,1110,1185,1256,1326,1399,1472,1548,1622,1698,1773,1859,1935]),
('Q','8-2-24_img2.jpg',60,1880,40,42,[290,361,428,508,579,653]),
('N','9-1-2_img2.jpg',240,2584,38,44,[968,1028,1088]),
('M','8-3-10_img1.jpg',2080,4000,42,42,[1650,1740,1825,1910,2000,2120,2210,2290,2370,2450]),
('S','8-2-22_img3.jpg',60,1840,38,40,[1905,1985,2065,2140]),
('E','8-2-22_img4.jpg',100,1850,38,40,[900,970,1045,1110,1190,1275])]
for pre,f,x0,x1,up,dn,cs in JOBS:
    im=Image.open(R+f).convert('RGB')
    for n,c in enumerate(cs,1): im.crop((x0,c-up,x1,c+dn)).save(f'{O}{pre}{n:02d}.png')
