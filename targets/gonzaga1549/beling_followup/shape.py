"""Compare a held-out native glyph with same-document atlas labels."""
import argparse
import csv
import hashlib
import json
import random
from collections import Counter
from pathlib import Path

import math
import statistics
from PIL import Image


HERE = Path(__file__).resolve().parent
options=argparse.ArgumentParser(description=__doc__)
options.add_argument("--atlas", type=Path, required=True, help="figueroa1534/validation/atlas.tsv")
options.add_argument("--tiles", type=Path, required=True, help="directory containing the archival JPEG tiles")
options.add_argument("--output", type=Path, required=True, help="existing empty output directory")
args=options.parse_args()
ATLAS=args.atlas
TILES=HERE/"atlas_tiles.tsv"
RAW=args.tiles
OUT=args.output
CLASSES = ("de", "no", "se")
THRESHOLDS = (64, 96, 128)

def table(name, header, rows):
    with (OUT / name).open("w", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)

def masks(crops, threshold):
    vectors = []
    for image in crops:
        pixels = image.load()
        remaining = {(x,y) for y in range(image.height) for x in range(image.width) if pixels[x,y] <= threshold}
        ink = set()
        while remaining:
            start = remaining.pop()
            region = {start}
            stack = [start]
            while stack:
                x,y = stack.pop()
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        q = (i,j)
                        if q in remaining:
                            remaining.remove(q)
                            region.add(q)
                            stack.append(q)
            if len(region) >= 3:
                ink.update(region)
        glyph = Image.new("L", image.size)
        for point in ink:
            glyph.putpixel(point,255)
        glyph = glyph.crop(glyph.getbbox())
        scale = 48 / max(glyph.size)
        width, height = [max(1,round(n*scale)) for n in glyph.size]
        small = glyph.resize((width,height),Image.Resampling.NEAREST)
        dx,dy = (60-width)//2,(60-height)//2
        vectors.append([(x+dx,y+dy) for y in range(height) for x in range(width) if small.getpixel((x,y))])
    return vectors

def distances(vectors):
    directed = []
    for points in vectors:
        rows = {}
        for x,y in points:
            rows.setdefault(y,[]).append(x)
        xdist = {yy:[min((x-i)**2 for i in xs) for x in range(60)] for yy,xs in rows.items()}
        field = [[math.sqrt(min(row[x]+(y-yy)**2 for yy,row in xdist.items()))
                  for x in range(60)] for y in range(60)]
        directed.append([statistics.mean(field[y][x] for x,y in mask) for mask in vectors])
    return [[(directed[i][j]+directed[j][i])/2 for j in range(len(vectors))] for i in range(len(vectors))]

def predictions(matrix, labels, lines):
    all_scores = []
    for i, line in enumerate(lines):
        scores = {}
        for candidate in CLASSES:
            scores[candidate] = float(statistics.mean(sorted(matrix[i][j] for j, value in enumerate(labels)
                                      if value == candidate and line != lines[j])[:2]))
        ordered = sorted(scores, key=scores.get)
        winner = ordered[0] if scores[ordered[0]] != scores[ordered[1]] else "tie"
        all_scores.append((winner, scores))
    return all_scores

def main():
    rows = [row for row in csv.DictReader(ATLAS.open(), delimiter="\t") if row["daniel_value"] in CLASSES]
    labels = [row["daniel_value"] for row in rows]
    lines = [(r["page"],r["line"]) for r in rows]+[("c60v","22")]
    ids = [r["crop_file"].split("/")[-1] for r in rows]+["B22.1"]
    pages = {"60r":Image.new("L",(3008,4217)), "60v":Image.new("L",(2983,4256))}
    inputs = [ATLAS,TILES]
    for name, _, leaf, x, y, w, h in csv.reader(TILES.open(),delimiter="\t"):
        if leaf not in pages:
            continue
        path = RAW / name
        inputs.append(path)
        with Image.open(path) as tile:
            assert tile.size == (int(w),int(h))
            pages[leaf].paste(tile.convert("L"), (int(x),int(y)))
    crops = [pages[r["page"][1:]].crop(tuple(int(r[c]) for c in ("x0","y0","x1","y1"))) for r in rows]
    crops.append(pages["60v"].crop((337,2815,419,2907)))
    table("shape_inputs.tsv", ["path","sha256"], ((p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for p in inputs))
    detail, controls, results = [], [], []
    for th in THRESHOLDS:
        matrix = distances(masks(crops, th))
        pred = predictions(matrix, labels, lines)
        correct = Counter(label for label,(p,_) in zip(labels,pred) if label==p)
        total = Counter(labels)
        for name,actual,(winner,scores) in zip(ids,labels+["held_out"],pred):
            detail.append((th,name,actual,winner,*[round(scores[c],6) for c in CLASSES]))
        winner,scores = pred[-1]
        ranked = sorted(scores.values())
        results.append(dict(threshold=th,total=total,correct=correct,heldout=winner,ratio=ranked[0]/ranked[1]))
        if th == 96:
            rng = random.Random(1549111422)
            for k in range(1,1001):
                shuffled = labels[:]
                rng.shuffle(shuffled)
                predicted = predictions(matrix,shuffled,lines)
                controls.append((k,sum(p==actual for (p,_),actual in zip(predicted,shuffled))))
    wins = sum(n>=sum(results[1]["correct"].values()) for _,n in controls)
    passed = (wins==0 and len({r["heldout"] for r in results})==1 and all(
        r["ratio"] <= .8 and all(r["correct"][c] >= .8*r["total"][c] for c in CLASSES) for r in results))
    table("shape_scores.tsv",["threshold","crop","reference","predicted",*CLASSES],detail)
    table("shape_controls.tsv",["permutation","matches"],controls)
    report = dict(thresholds=results,controls_equal_or_better=wins,controls_best=max(n for _,n in controls),passed=passed)
    (OUT/"shape_result.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report))
if __name__=="__main__":
    main()
