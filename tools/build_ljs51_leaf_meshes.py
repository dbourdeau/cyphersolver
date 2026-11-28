"""Build the LJS 51 cut meshes from the shipped photographs (OpenCV, SciPy, Shapely 2.1).

Coordinates below refer to a 450 x 650 view of each recto, with the gutter on
the right. Trace only exposed material inside the reviewed regions. The dark
round tide mark on the final leaves and the paper islands inside worm tracks
are surviving paper. The verso is registered locally because the photographer
repositioned the leaf between exposures.
"""
import json
from pathlib import Path

import cv2
import numpy as np
from scipy.interpolate import LinearNDInterpolator
from scipy.spatial import cKDTree
from shapely import LineString, Point, Polygon, box, constrained_delaunay_triangles, union_all

BOOK = Path(__file__).resolve().parents[1] / "docs/ljs51-book"
W, H = 450, 650
RECT = box(0, 0, W, H)
SEGMENTS = 48


# Outer corner outlines, traced in the recto crop. The vertical coordinate is
# distance inward from the head or tail, so the two margins share one format.
HEAD_CORNERS = {
    10: [(0,20),(9,11),(17,5),(22,0)],
    12: [(0,14),(8,7),(16,0)],
    14: [(0,22),(8,16),(17,7),(22,0)],
    16: [(0,21),(6,16),(15,7),(21,0)],
    18: [(0,17),(9,9),(16,0)],
    20: [(0,12),(5,5),(10,0)],
    42: [(0,15),(8,9),(16,0)],
    152: [(0,44),(42,0)],
    204: [(0,8),(7,4),(12,0)],
    206: [(0,23),(11,15),(25,0)],
    208: [(0,27),(12,17),(28,0)],
    210: [(0,31),(14,21),(35,0)],
    212: [(0,32),(10,24),(31,2),(44,0)],
    214: [(0,40),(12,30),(35,4),(48,0)],
    216: [(0,46),(14,36),(31,25),(51,8),(65,0)],
}
TAIL_CORNERS = {
    10: [(0,29),(8,19),(16,10),(26,0)],
    12: [(0,27),(10,19),(20,12),(31,0)],
    14: [(0,26),(9,19),(20,10),(29,0)],
    16: [(0,24),(8,16),(21,0)],
    18: [(0,24),(10,13),(22,0)],
    20: [(0,20),(8,12),(18,0)],
    44: [(0,8),(8,4),(21,0)],
    46: [(0,18),(38,0)],
    48: [(0,10),(7,4),(18,0)],
    52: [(0,10),(7,4),(22,0)],
    60: [(0,7),(10,4),(24,0)],
    62: [(0,14),(15,6),(31,0)],
    64: [(0,14),(14,7),(34,0)],
    66: [(0,22),(44,0)],
    68: [(0,17),(40,0)],
    70: [(0,15),(43,0)],
    72: [(0,15),(40,0)],
    74: [(0,7),(11,4),(24,0)],
    142: [(0,9),(8,4),(18,0)],
    162: [(0,10),(20,0)],
    164: [(0,9),(7,4),(17,0)],
    170: [(0,12),(30,0)],
    180: [(0,17),(14,0)],
    182: [(0,8),(6,3),(17,0)],
    184: [(0,9),(7,4),(19,0)],
    186: [(0,10),(9,4),(21,0)],
    188: [(0,10),(6,5),(19,0)],
    190: [(0,13),(7,5),(19,0)],
    192: [(0,14),(10,6),(23,0)],
    194: [(0,15),(12,7),(31,0)],
    196: [(0,19),(12,11),(32,0)],
    198: [(0,21),(15,11),(35,0)],
}

# Where a free flap is distinguishable, its exposed perimeter runs between
# the two ends of the crease. The sign records which face the flap lies on.
# Coordinates use the same inward distance as the corresponding outline.
FOLDS = {
    46: (-1, [(7,27),(12,29),(19,26),(29,16)]),
    66: (1, [(5,31),(19,29),(30,25),(38,12)]),
    68: (1, [(3,21),(12,23),(19,20),(30,11)]),
    70: (1, [(4,21),(16,23),(23,20),(32,12)]),
    72: (1, [(4,21),(14,23),(22,20),(32,10)]),
    152: (1, [(0,51),(18,48),(36,44),(42,40),(44,32)]),
    162: (-1, [(2,18),(8,18),(13,14)]),
    170: (-1, [(3,20),(11,21),(18,18),(23,12)]),
    180: (-1, [(1,26),(5,23),(9,17)]),
}


# Recto scan coordinates along visible ridges. Width and signed height are
# estimates in scan pixels. A crease continues across surviving paper only.
CREASES = {
    8: [(10, 2.3, [(25,493),(85,532),(157,577),(203,601),(246,620),(293,640)])],
    54: [(6, 1.4, [(0,587),(24,609),(47,629),(70,648)])],
    154: [(6, -1.2, [(40,601),(58,619),(76,640),(85,650)])],
    208: [(7, 1.6, [(89,601),(128,617),(164,632),(198,646)])],
    210: [(8, 2.1, [(89,600),(129,615),(168,629),(217,649)]),
          (5, -1.1, [(94,612),(130,632),(155,643),(190,646)])],
    212: [(8, -1.8, [(80,522),(136,550),(178,573),(225,602),(293,642)]),
          (6, 1.3, [(88,617),(128,634),(169,650)])],
}


# Fore-edge samples in the paired master crops (y, recto x, mirrored verso x).
# These early versos include a strip of the underlying stack beyond the leaf.
# The margin is registered along its entire length, independently of the ink.
FORE_EDGE = {
    8: [(0,38,73),(14,33,61),(36,32,56),(80,31,54),(155,29,55),
        (238,28,54),(293,29,59),(313,27,55),(400,25,54),(490,25,52),
        (580,25,54),(610,25,55),(623,38,56),(636,65,83),(650,108,116)],
    10: [(0,24,61),(15,9,45),(37,0,37),(80,0,36),(160,0,36),
         (245,0,35),(298,0,40),(318,0,36),(440,0,34),(540,0,34),
         (608,0,35),(621,1,36),(635,13,49),(650,27,61)],
    12: [(0,17,58),(16,2,44),(39,0,37),(80,0,35),(155,0,36),
         (245,0,36),(295,0,39),(320,0,38),(450,0,35),(560,0,34),
         (609,0,35),(624,2,41),(636,15,54),(650,32,68)],
    18: [(0,18,32),(18,1,17),(40,0,15),(160,0,17),(310,0,17),
         (470,0,16),(608,0,16),(628,2,21),(650,22,36)],
    20: [(0,13,28),(18,0,15),(40,0,13),(160,0,15),(310,0,15),
         (470,0,14),(608,0,15),(630,0,20),(650,18,33)],
}


def scan_margin(image, ys, guide):
    scale = image.shape[0] / H
    # Follow short nicks within the measured corridor. A small inward sample
    # avoids blending in a pixel of the backing at the fine/coarse mip levels.
    offsets = np.linspace(-1.75, 1.75, 15)
    xs = np.rint((guide[:,None]+offsets)*scale).astype(int).clip(0,image.shape[1]-1)
    rows = np.rint(ys*scale).astype(int).clip(0,image.shape[0]-1)
    gradient = cv2.Sobel(cv2.GaussianBlur(image[:,:int(125*scale)],(3,3),.8),cv2.CV_32F,1,0)
    scores = np.abs(gradient[rows[:,None],xs]) - 14*np.abs(offsets)
    measured = guide + offsets[np.argmax(scores,axis=1)] + .65
    return np.where(guide>0, np.maximum(0,measured), 0)


def photo(n):
    folder = "detail" if 6 <= n <= 217 else "pages"
    image = cv2.imread(str(BOOK / folder / f"0084_{n:04d}.jpg"), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Missing registered photograph for image {n}")
    return image


def build(n):
    front = photo(n)
    reverse = cv2.flip(photo(n + 1), 1)
    scale = front.shape[0] / H
    losses = []
    anchors = {(x, y): (0, 0) for x in (0, W) for y in (0, H)}
    paper = RECT

    def align(x, y, bx, by):
        anchors[x, y] = (bx-x, by-y)

    def region(points, radius, threshold, darkest=False):
        # Limit edge extraction to the photographed path. The mask never
        # bridges a gap between separate channels or discards a paper island.
        path = np.int32(np.array(points) * scale)
        region_mask = np.zeros(front.shape, np.uint8)
        cv2.polylines(region_mask, [path], False, 255, max(2, round(2*radius*scale)))
        x, y, w, h = cv2.boundingRect(region_mask)
        if not w or not h:
            return
        crop = front[y:y+h, x:x+w]
        radius_px = round(9*scale)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*radius_px+1,)*2)
        def local_contrast(gray):
            return cv2.morphologyEx(cv2.GaussianBlur(gray,(3,3),.8), cv2.MORPH_BLACKHAT, kernel)
        border = radius_px*2
        lx,ly = max(0,x-border),max(0,y-border)
        contrast = local_contrast(front[ly:y+h+border,lx:x+w+border])[y-ly:y-ly+h,x-lx:x-lx+w]
        cut = np.uint8((contrast > threshold) & (region_mask[y:y+h,x:x+w] > 0))
        if darkest:
            cut &= np.uint8(crop < np.median(crop)-18)
        # Find the same feature on the mirrored verso within the scan offset.
        pad = round(24*scale)
        x0,y0=max(0,x-pad),max(0,y-pad)
        window=reverse[y0:y+h+pad,x0:x+w+pad]
        response=cv2.matchTemplate(window,crop,cv2.TM_CCOEFF_NORMED)
        _,score,_,(dx,dy)=cv2.minMaxLoc(response)
        if score > .30:
            cx,cy=(x+w/2)/scale,(y+h/2)/scale
            align(cx,cy,cx+(x0+dx-x)/scale,cy+(y0+dy-y)/scale)
            # A matched opposite face independently supports the open channel.
            opposite = window[dy:dy+h,dx:dx+w]
            evidence = (local_contrast(opposite) > threshold*.4).astype(np.uint8)
            tolerance = max(3, round(2*scale)*2+1)
            cut &= cv2.dilate(evidence, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(tolerance,tolerance)))
        contours, tree = cv2.findContours(cut, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        if tree is None:
            return
        def ring(c):
            return (cv2.approxPolyDP(c, .32*scale, True)[:,0,:] + [x,y]) / scale
        for k,c in enumerate(contours):
            if tree[0,k,3] >= 0 or cv2.contourArea(c) < 3*scale*scale:
                continue
            outline = ring(c)
            if len(outline) < 3:
                continue
            holes = []
            child = tree[0,k,2]
            while child >= 0:
                inside = ring(contours[child])
                if len(inside) >= 3:
                    holes.append(inside)
                child = tree[0,child,0]
            losses.append(Polygon(outline, holes).buffer(0))

    def opening(points):
        # Use a narrow search band around the traced outline for the small
        # gutter perforations. Their pale inner walls belong to the next leaf.
        pts=np.array(points, dtype=float)
        x,y=pts.mean(axis=0)
        local=np.int32(pts*scale)
        mask=np.zeros(front.shape,np.uint8)
        cv2.fillPoly(mask,[local],255)
        kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))
        outer=cv2.dilate(mask,kernel)
        inner=cv2.erode(mask,kernel)
        labels=np.where(outer==0,0,np.where(mask==0,2,3)).astype(np.uint8)
        labels[inner!=0]=1
        if not inner.any():
            cv2.circle(labels,tuple(local.mean(axis=0).astype(int)),1,1,-1)
        left,top,w,h=cv2.boundingRect(outer)
        left,top=max(0,left-4),max(0,top-4)
        labels=labels[top:top+h+8,left:left+w+8].copy()
        gray=front[top:top+labels.shape[0],left:left+labels.shape[1]]
        cv2.grabCut(cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR),labels,None,
                    np.zeros((1,65)),np.zeros((1,65)),3,cv2.GC_INIT_WITH_MASK)
        contours,_=cv2.findContours(labels%2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        c=cv2.approxPolyDP(max(contours,key=cv2.contourArea),.6,True)[:,0,:]
        losses.append(Polygon((c+[left,top])/scale).buffer(0))
        pad=round(22*scale)
        x0,y0=max(0,left-pad),max(0,top-pad)
        window=reverse[y0:top+gray.shape[0]+pad,x0:left+gray.shape[1]+pad]
        _,_,_,(dx,dy)=cv2.minMaxLoc(cv2.matchTemplate(window,gray,cv2.TM_CCOEFF_NORMED))
        align(x,y,x+(x0+dx-left)/scale,y+(y0+dy-top)/scale)

    def trace_points(points, image, counts=None):
        # Follow the local scan gradient between landmarks, keeping the two
        # ends fixed so an adjacent ink stroke cannot redirect a long tear.
        gray=cv2.GaussianBlur(image,(3,3),.75)
        gx=cv2.Sobel(gray,cv2.CV_32F,1,0)
        gy=cv2.Sobel(gray,cv2.CV_32F,0,1)
        traced=[]
        for j,(start,end) in enumerate(zip(points,points[1:]+points[:1])):
            a,b=np.array(start),np.array(end)
            length=np.linalg.norm(b-a)
            count = counts[j] if counts is not None else max(1,int(length/1.8))
            normal=np.array([a[1]-b[1],b[0]-a[0]])/length
            samples=np.linspace(a,b,count,endpoint=False)
            offsets=np.arange(-3,3.01,.5)
            candidates=samples[:,None,:]+offsets[None,:,None]*normal
            ix,iy=np.rint(candidates*scale).astype(int).transpose(2,0,1)
            ix=ix.clip(0,gray.shape[1]-1)
            iy=iy.clip(0,gray.shape[0]-1)
            scores=np.abs(gx[iy,ix]*normal[0]+gy[iy,ix]*normal[1])-8*np.abs(offsets)
            best=offsets[scores.argmax(axis=1)]
            if count>=5:
                best=np.convolve(best,[.15,.2,.3,.2,.15],mode="same")
            best[0]=0
            if a[0]==b[0] and a[0] in (0,W) or a[1]==b[1] and a[1] in (0,H):
                best[:]=0
            traced.extend(samples+best[:,None]*normal)
        return traced

    def trace_edge(points):
        return Polygon(trace_points(points, front)).buffer(0).intersection(RECT)

    if n == 6:
        # Paired landmarks along the surviving first written leaf, including
        # the tongue below the principal tear. bx/by are mirrored verso pixels.
        pairs = [
            (450,0,450,0),(40,0,69,0),(32,16,51,18),(29,44,36,46),
            (28,136,32,137),(29,234,34,237),(30,347,46,349),
            (47,355,56,358),(78,369,91,370),(108,379,118,380),
            (117,391,119,390),(135,403,145,403),(145,416,149,416),
            (140,440,153,438),(142,455,157,459),(124,471,135,470),
            (115,487,122,484),(111,503,118,501),(128,506,136,508),
            (147,498,151,505),(157,500,162,501),(174,516,174,521),
            (183,530,181,530),(201,528,192,527),(214,540,200,535),
            (225,547,212,549),(232,563,228,562),(250,568,238,568),
            (261,562,251,565),(272,575,242,577),(292,582,254,584),
            (300,596,271,596),(322,597,281,600),(333,602,296,602),
            (348,596,307,610),(362,590,322,605),(376,571,332,596),
            (390,568,351,583),(406,559,370,573),(419,548,385,569),
            (433,554,402,569),(450,568,450,543)]
        front_points = [(x,y) for x,y,_,_ in pairs]
        back_points = [(x,y) for _,_,x,y in pairs]
        counts = [max(1,round(np.linalg.norm(np.subtract(a,b))/1.2))
                  for a,b in zip(front_points,front_points[1:]+front_points[:1])]
        recto = trace_points(front_points, front, counts)
        verso = trace_points(back_points, reverse, counts)
        paper = Polygon(recto).buffer(0).intersection(RECT)
        for a,b in zip(recto[::4],verso[::4]):
            align(*a,*b)
        for landmark in pairs:
            align(*landmark)
        losses.append(Polygon([(410,125),(417,123),(424,130),(431,142),(432,150),(425,152),(419,143)]))
        align(422,138,438,140)
    if n == 8:
        paper=trace_edge([(450,0),(36,0),(27,19),(24,72),(24,305),(25,552),(22,607),
                       (36,622),(67,638),(101,647),(144,646),(167,638),(184,630),
                       (200,638),(252,640),(265,633),(271,621),(279,618),(294,620),
                       (305,627),(312,639),(327,646),(368,650),(450,650)])
        for p in [(25,300,53,300),(31,615,55,624),(281,620,292,624),(450,650,450,650)]:
            align(*p)
        losses.append(Polygon([(423,126),(436,131),(447,143),(447,153),(431,143),(421,132)]))
        align(434,138,434,143)
    if 10 <= n <= 26:
        region([(240,624),(306,624)],13,13)
    if n == 10:
        opening([(417,125),(428,126),(439,135),(444,146),(444,153),(434,151),(425,141)])
    if 30 <= n <= 36:
        region([(450,151),(443,168),(433,181),(427,185)],6,15)
    if 46 <= n <= 58:
        region([(449,541),(444,548),(441,555),(430,562)],4,14)
        region([(440,547),(439,542),(439,537)],3,15)
    if 64 <= n <= 76:
        x,y={64:(446,138),66:(446,139),68:(445,139),70:(443,139),
             72:(440,138),74:(443,138),76:(441,137)}[n]
        size={64:.40,66:.76,68:.83,70:1,72:1,74:1,76:1}[n]
        opening([(min(W,x+dx*size),y+dy*size) for dx,dy in
                 [(-10,-2),(-7,-8),(1,-12),(6,-8),(8,12),(3,7),(-6,5)]])
    if 78 <= n <= 92:
        region([(449,157),(444,170),(438,178),(433,184)],6,13)
    if 102 <= n <= 116:
        region([(449,408),(446,411),(440,400),(437,394)],3,17)
    if 136 <= n <= 160:
        region([(439,451),(431,443),(423,434),(414,429),(407,426)],5,16)
    if 146 <= n <= 158:
        region([(449,590),(447,576),(443,565),(440,556)],4,15)
    if 164 <= n <= 174:
        region([(449,9),(445,22),(438,36),(433,50),(427,62)],4,15)
    if 170 <= n <= 180:
        region([(440,128),(440,140),(440,151)],4,16)
    if 192 <= n <= 198:
        region([(449,30),(441,35),(435,42)],3,16)
    if 202 <= n <= 216:
        # Long split in the lower gutter; its tip moves with each exposure.
        topx={202:412,204:423,206:418,208:415,210:425,212:422,214:415,216:426}[n]
        tipx={202:431,204:446,206:439,208:436,210:445,212:444,214:433,216:444}[n]
        opening([(topx-1,426),(topx+2,426),(topx+6,466),(tipx-3,499),
                 (tipx,522),(tipx-7,504),(topx+2,475)])
    if 12 <= n <= 24:
        region([(24,234),(52,226),(81,216),(108,207),(116,191)],5,13)
        region([(67,205),(79,219)],3,16)
    if 72 <= n <= 96:
        region([(254,563),(255,581),(245,598),(243,620),(250,628),(267,640),(286,643),
                (302,618),(333,616)],14,15)
        region([(251,581),(264,580),(282,578)],6,13)
        region([(276,592),(287,599),(296,613),(311,611),(335,596)],7,16)
    if 78 <= n <= 92:
        region([(53,351),(36,362),(41,385)],5,13)
        region([(36,362),(17,374),(16,392),(23,405),(42,419),(62,431),(80,428)],6,13)
    if 102 <= n <= 122:
        # Centers move as the text block shifts between photographs.
        centers=[(433,126),(435,129),(433,131),(434,133),(436,133),(435,133),
                 (436,134),(436,132),(436,132),(438,128),(438,128)]
        x,y=centers[(n-102)//2]
        if n<=114:
            contour=[(-11,-7),(-4,-9),(4,-6),(9,1),(12,14),(6,8),(-2,6),(-9,3)]
        else:
            contour=[(-6,-5),(-1,-6),(4,-3),(7,6),(0,5),(-5,2)]
        opening([(x+dx,y+dy) for dx,dy in contour])
    if 124 <= n <= 134:
        region([(448,482),(440,483),(442,500),(434,510),(418,517),(412,524)],5,15)
    if 182 <= n <= 216:
        centers=[(445,140),(422,133),(424,133),(421,133),(424,134),(435,132),
                 (427,131),(427,133),(429,133),(431,133),(431,133),(443,134),
                 (433,133),(432,134),(442,133),(431,133),(435,133),(441,133)]
        x,y=centers[(n-182)//2]
        opening([(x-3,y-11),(x,y-13),(x+3,y-8),(x+3,y+10),(x,y+13),(x-2,y+6)])
    if 210 <= n <= 216:
        region([(404,194),(412,194),(426,181),(434,164),(448,162)],6,17)
    if 204 <= n <= 214:
        region([(47,450),(43,474),(39,486)],4,16)
        region([(61,492),(42,510),(39,543),(37,570),(33,597),(24,615),
                (29,624),(48,637),(63,638),(77,628),(88,604),(95,575),
                (94,549),(81,524),(86,516)],5,16)
    # The tail of the final gathering is visible against the stack in both
    # views. Keep the flap bounded by the long split on ff. 101-105.
    tail_edges = {
        200: [(0,629),(15,640),(37,649),(54,650)],
        202: [(0,622),(17,633),(35,642),(49,645),(62,645),(95,648),(111,650)],
        204: [(0,626),(22,638),(39,645),(60,647),(89,647),(105,650)],
        206: [(0,629),(17,638),(40,647),(62,648),(80,650)],
        208: [(0,625),(19,634),(37,642),(55,646),(72,650)],
        210: [(0,627),(15,635),(33,644),(55,650)],
        212: [(0,615),(14,629),(34,642),(51,647),(64,650)],
        214: [(0,611),(15,627),(32,638),(53,644),(78,646),(110,650)],
        216: [(0,603),(18,617),(24,626),(36,628),(51,642),(69,638),
              (87,644),(115,648),(134,644),(153,648),(178,646),(194,637),
              (216,646),(247,649),(285,650)]}
    if n in tail_edges:
        paper=trace_edge([(0,0),*tail_edges[n],(W,H),(W,0)])
    # Register displaced corner crops locally; the opposite scan often
    # includes a wider sliver of the stack along the free edge.
    corner_matches = {
        10: [(0,20,33,39),(22,0,62,0),(0,621,30,619),(26,650,55,650)],
        12: [(0,14,31,37),(16,0,58,0),(0,623,32,615),(31,650,63,650)],
        18: [(0,17,10,17),(0,626,11,622)],
        20: [(0,12,10,16),(0,630,12,625)],
        46: [(0,632,0,631),(38,650,39,650)],
        66: [(0,628,0,629),(44,650,42,650)],
        68: [(0,633,0,633),(40,650,35,650)],
        70: [(0,635,0,636),(43,650,40,650)],
        72: [(0,635,0,638),(40,650,35,650)],
        152: [(0,44,4,46),(42,0,46,0)],
        162: [(0,640,0,639),(20,650,22,650)],
        170: [(0,638,0,638),(30,650,35,650)],
        180: [(0,633,0,634),(14,650,14,650)],
    }
    if n in corner_matches:
        for match in corner_matches[n]:
            align(*match)
        for y in (90, H-90):
            align(0,y,0,y)
            align(100,y,100,y)
        for y in (0,H):
            align(100,y,100,y)

    if n in FORE_EDGE:
        landmarks = np.array(FORE_EDGE[n])
        margin_y = np.unique(np.r_[np.arange(0,H,2.), H, landmarks[:,0]])
        fronts, backs = [np.interp(margin_y,landmarks[:,0],landmarks[:,j]) for j in (1,2)]
        front_edge = scan_margin(front, margin_y, fronts)
        back_edge = scan_margin(reverse, margin_y, backs)
        boundary = list(zip(front_edge,margin_y))
        paper = paper.intersection(Polygon([*boundary,(W,H),(W,0)]))

    flap = None
    for bottom, corners in [(False, HEAD_CORNERS), (True, TAIL_CORNERS)]:
        if n not in corners:
            continue
        def scan_points(points):
            return [(x, H - inward if bottom else inward) for x, inward in points]

        edge = scan_points(corners[n])
        corner = (0, H if bottom else 0)
        if n in FOLDS:
            # Keep the crease shared by the folded surface and the cut edge.
            losses.append(Polygon([corner, *edge]))
            side, rim = FOLDS[n]
            flap = Polygon([edge[0], *scan_points(rim), edge[-1]])
            hinge = np.array(edge, dtype=float)
        else:
            losses.append(trace_edge([corner, *edge]))
    if not losses and paper.equals(RECT) and n not in CREASES:
        return None
    paper=paper.difference(union_all(losses))
    # Clip before triangulating so every triangle bends with its own page strip.
    offsets=LinearNDInterpolator(list(anchors), list(anchors.values()),fill_value=0)
    vertices,indices,seen=[],[],{}
    relief = {}
    covered_uv = {}
    def triangulate(surface, folded, covered=False):
        for i in range(SEGMENTS):
            strip=surface.intersection(box(i*W/SEGMENTS,0,(i+1)*W/SEGMENTS,H))
            if strip.is_empty:
                continue
            # Subdivide in both directions so even broad, unmarked regions
            # flex across the height of the sheet as well as around the spine.
            first = max(0, int(strip.bounds[1]*16/H))
            last = min(15, int(strip.bounds[3]*16/H))
            for row in range(first, last+1):
                patch = strip.intersection(box(-1,row*H/16,W+1,(row+1)*H/16))
                add_triangles(patch, folded, covered)

    def add_triangles(patch, folded, covered):
        for tri in constrained_delaunay_triangles(patch).geoms:
            coords=list(tri.exterior.coords)[:3]
            if tri.exterior.is_ccw:
                coords.reverse()
            for x,y in coords:
                xy=(round(x,3),round(y,3))
                key = (xy, folded, covered)
                if key not in seen:
                    seen[key] = len(vertices)
                    if covered:
                        # The photo contains the turned-over flap here. Sample
                        # paper immediately beyond its free rim for the narrow
                        # strip of underlying sheet revealed in an oblique view.
                        point = Point(xy)
                        nearest = rim_line.interpolate(rim_line.project(point))
                        delta = np.array(nearest.coords[0]) - xy
                        sample = np.clip(np.array(nearest.coords[0]) + delta / max(1, np.linalg.norm(delta))*2 + direction*2, [0,0], [W,H])
                        if side < 0:
                            sample += offsets(sample)[0]
                        covered_uv[len(vertices)] = sample.round(3).tolist()
                    if folded:
                        dx, dy = hinge[1] - hinge[0]
                        distance = abs(dx * (y-hinge[0,1]) - dy * (x-hinge[0,0])) / np.hypot(dx, dy)
                        relief[len(vertices)] = side * distance
                    vertices.append(xy)
                indices.append(seen[key])

    # Nested contours give a ridge enough cross-sections to change both the
    # silhouette and the normals, even in a previously flat, unbroken strip.
    surfaces = [paper]
    creases = [(width, height, LineString(path)) for width, height, path in CREASES.get(n, [])]
    for width, _, path in creases:
        for fraction in (1, .65, .32, .06):
            band = path.buffer(width * fraction, quad_segs=3)
            surfaces = [part for surface in surfaces for part in
                        (surface.difference(band), surface.intersection(band)) if part.area > 0]
    if flap is not None:
        tangent = hinge[1] - hinge[0]
        direction = np.array([-tangent[1], tangent[0]]) / np.linalg.norm(tangent)
        if np.dot(direction, np.array(flap.centroid.coords[0]) - hinge[0]) < 0:
            direction = -direction
        rim_line = LineString(list(flap.exterior.coords)[:-1])
    for surface in surfaces:
        if flap is None:
            triangulate(surface, False)
        else:
            triangulate(surface.difference(flap), False)
            triangulate(surface.intersection(flap), False, covered=True)
    if flap is not None:
        folded_paper = flap.intersection(paper)
        for distance in (2, 5):
            shoulder = LineString(hinge).buffer(distance)
            triangulate(folded_paper.intersection(shoulder), True)
            folded_paper = folded_paper.difference(shoulder)
        triangulate(folded_paper, True)
    coords=np.array(vertices)
    back=coords+offsets(coords)
    if n in FORE_EDGE:
        # The mesh shares one physical boundary; each face samples its own
        # photograph at that boundary. Fade into the interior registration.
        fx = np.interp(coords[:,1], margin_y, front_edge)
        bx = np.interp(back[:,1], margin_y, back_edge)
        distance = np.maximum(0, coords[:,0]-fx)
        weight = np.clip(1-distance/75,0,1)
        back[:,0] += weight * (bx+distance-back[:,0])
    mesh = dict(vertices=np.round(np.column_stack((coords,back)),2).tolist(),indices=indices)
    # Bound the thickness by the surviving outer contour, including the torn
    # corners. Split it at the same bending strips as the face triangles.
    base_indices = [i for i in range(len(coords)) if i not in relief]
    tree = cKDTree(coords[base_indices])
    borders = []
    for piece in getattr(paper, "geoms", [paper]):
        points = []
        ring = list(piece.exterior.coords)
        for (x,y),(xx,yy) in zip(ring, ring[1:]):
            points.append((x,y))
            fractions = set()
            for start,end,count,span in ((x,xx,SEGMENTS,W),(y,yy,16,H)):
                if start == end:
                    continue
                first = int(np.floor(min(start,end)*count/span))+1
                last = int(np.ceil(max(start,end)*count/span))
                fractions.update((j*span/count-start)/(end-start) for j in range(first,last))
            points.extend((x+t*(xx-x),y+t*(yy-y)) for t in sorted(fractions))
        _, nearest = tree.query(points)
        indices = [base_indices[j] for j in nearest]
        borders.append([v for j,v in enumerate(indices) if v != indices[j-1]])
    mesh["borders"] = borders
    if creases:
        heights = []
        for i, xy in enumerate(vertices):
            point = Point(xy)
            height = 0.
            for width, amplitude, path in creases:
                d = min(1., path.distance(point) / width)
                height += amplitude * (1 - d*d*(3-2*d))
            if abs(height) >= .001:
                heights.append([i, round(height, 3)])
        mesh["creases"] = heights
    if relief:
        mesh["coveredFace"] = side
        mesh["coveredUV"] = [[i, *uv] for i, uv in covered_uv.items()]
        mesh["foldDirection"] = direction.round(6).tolist()
        mesh["flap"] = [[i, round(distance, 3)] for i, distance in relief.items()]
    return mesh


if __name__ == "__main__":
    cv2.setNumThreads(2)
    cv2.setRNGSeed(0)
    meshes={}
    for n in range(2,222,2):
        mesh=build(n)
        if mesh:
            meshes[f"0084_{n:04d}"]=mesh
    (BOOK/"leaf-meshes.json").write_text(json.dumps(meshes,separators=(",",":"))+"\n")
