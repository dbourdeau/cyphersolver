"""Predict unseen parts of Jerash patches; rank only fully on-sheet windows.

Locations learned on one piece of a patch are frozen before scoring
another. Baseline deformations and neighboring text can affect the scores.
"""
from pathlib import Path
import cv2
import numpy as np

im = cv2.imread(str(Path(__file__).with_name("jerash-depth.png")),0)
gray = cv2.resize(im,(520,1170),interpolation=cv2.INTER_AREA)
f = gray.astype("float32")
f -= cv2.GaussianBlur(f,(0,0),5)
bands = [(14,120),(106,188),(170,253),(236,327),(297,409),(390,471),
         (452,550),(515,613),(579,668),(640,725),(698,789),(775,859),
         (840,944),(917,1018),(987,1088),(1043,1129),(1095,1169)]


def test(label, box, train, held):
    x,y,w,h = box
    pattern = f[y:y+h,x:x+w]
    rows = []
    for line,(t,b) in enumerate(bands,1):
        if t<y+h and b>y:
            continue
        if b-t<h:
            continue
        maps = []
        for left,top,right,end in (train,held):
            # Every element of the map represents the origin of the FULL
            # patch, even though only one subregion enters the score.
            hay = f[t+top:b-h+end,left:520-w+right]
            sub = pattern[top:end,left:right]
            maps.append(cv2.matchTemplate(hay,sub,cv2.TM_CCOEFF_NORMED))
        count = cv2.integral((gray[t:b]>4).astype("uint8"))
        coverage = count[h:,w:] - count[:-h,w:] - count[h:,:-w] + count[:-h,:-w]
        maps[0][coverage<.98*w*h] = -2
        loc = np.unravel_index(maps[0].argmax(),maps[0].shape)
        rows.append((round(float(maps[1][loc]),3),line,round(float(maps[0][loc]),3)))
    print(label, sorted(rows,reverse=True)[:5])


box = (367,411,67,39)
test("curve predicts stem",box,(0,0,33,39),(33,0,67,39))
test("stem predicts curve",box,(33,0,67,39),(0,0,33,39))
test("baseline predicts tops",box,(0,22,67,39),(0,0,67,22))
test("tops predict baseline",box,(0,0,67,22),(0,22,67,39))
test("motif predicts next unit",(326,407,109,45),(41,4,108,43),(0,0,41,45))

# Different anchors and longer-range predictions than the stem/curve test.
test("line 10 opening predicts continuation",(335,652,142,50),(70,0,142,50),(0,0,70,50))
test("line 11 continuation predicts opening",(315,718,138,53),(0,0,68,53),(68,0,138,53))
test("terminal area predicts right neighbor",(268,1114,115,43),(0,0,56,43),(59,0,115,43))
test("N predicts adjacent group",(366,405,125,47),(77,0,125,47),(0,2,66,47))
test("line 1 emblem predicts adjacent sign",(39,46,139,50),(0,0,70,50),(70,0,139,50))
