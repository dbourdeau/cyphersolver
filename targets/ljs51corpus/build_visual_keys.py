"""Build manuscript specimens and folio records for the Penn LJS 51 key viewer.

Run with --images PATH pointing to output/ljs51 (reader crops and master TIFFs).
The public viewer uses only the checked-in files under docs/ljs51-keys.
"""
import argparse
from collections import Counter, defaultdict
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import re

from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / "docs/ljs51-keys"
CELL = 128


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")


def order(cid):
    m = re.match(r"(\d+)([rv])\.(\d+|trees)", cid)
    return int(m[1]), m[2], int(m[3]) if m[3].isdigit() else 100


def page_no(folio):
    return 6 + 2 * (int(folio[:-1]) - 1) + (folio[-1] == "v")


def row_location(cid, raw):
    if cid=="13r.11" and str(raw)=="14": return "13v",1
    folio = cid.partition(".")[0]
    m = re.fullmatch(r"(\d+[rv])[._l]*(\d+)", str(raw))
    if m:
        return m[1], int(m[2])
    if str(raw).isdigit():
        return folio, int(raw)
    return None


def reference(raw):
    m = re.search(r"output/ljs51/(crops/[^(),;:]+?\.(?:png|jpe?g))", raw, re.I)
    if not m:
        raise ValueError(raw)
    return m[1], raw[m.end():].strip(" ()")


@lru_cache(maxsize=None)
def context(rel):
    name = hashlib.sha256(rel.encode()).hexdigest()[:16] + ".webp"
    path = OUT / "context" / name
    with Image.open(IMAGES / rel) as im:
        img = im.convert("RGB")
        img.thumbnail((1450, 1200), Image.Resampling.LANCZOS)
        img.save(path, quality=73, method=3)
    return name


def sprite(cid, images):
    if not images:
        return
    sheet = Image.new("RGB",(6*CELL, ((len(images)+5)//6)*CELL), "#f5f0e6")
    for i,im in enumerate(images):
        im=ImageOps.contain(im.convert("RGB"),(CELL-8,CELL-8), Image.Resampling.LANCZOS)
        sheet.paste(im,((i%6)*CELL+(CELL-im.width)//2,(i//6)*CELL+(CELL-im.height)//2))
    sheet.save(OUT/"sheets"/(cid+".webp"), quality=88, method=4)


def ordinary(cid, d, state):
    shapes = d["shapes"]
    labels = {s["label"] for s in shapes}
    assert set(d["key"]) <= labels
    occurrences = defaultdict(list)
    lines = defaultdict(list)
    for loc,pos,sign,letter,*_ in d["alignment"]:
        if sign in labels:
            if cid=="13r.11" and str(loc)=="14":loc="13v01"
            occurrences[sign].append([str(loc),pos])
            lines[str(loc)].append([sign,letter,pos])
    cards, imgs = [], []
    for s in shapes:
        sign = s["label"]
        path, locator = reference(s["crop"])
        card = {"id":sign,"description":s["description"],"values":d["key"].get(sign,{}),
                "context":context(path),"locator":locator,"refs":occurrences[sign]}
        if s.get("position") and not locator:
            card["locator"]="Sign "+str(s["position"])+" in the recorded reading order"
        manual = EXAMPLES.get(cid, {}).get(sign)
        if manual:
            with Image.open(IMAGES/manual["file"]) as im:
                imgs.append(im.crop(manual["box"]).convert("RGB"))
            card.update(tile=len(imgs)-1,sample=[manual["row"],manual["position"]],manual=True,
                        context=context(manual["file"]),locator=f'Row {manual["row"]}, sign {manual["position"]}')
        for issue in d.get("unresolved_positions",[]) or []:
            if isinstance(issue,dict) and (issue.get("shape") or issue.get("sign"))==sign:
                card["uncertainty"]=issue
        red=d.get("red_check")
        if isinstance(red,dict):
            for mismatch in red.get("disagreements",[]) or []:
                if not isinstance(mismatch,dict):continue
                loc=str(mismatch.get("line",mismatch.get("row","")))
                pos=mismatch.get("pos",mismatch.get("position"))
                if [loc,pos] in occurrences[sign] and mismatch.get("red"):
                    card.setdefault("gloss",[]).append([loc,pos,mismatch["red"]])
        cards.append(card)
    sprite(cid,imgs)
    return {"id":cid,"state":state,"cards":cards,"lines":lines,"red":d.get("red_check"),
            "direction":d.get("direction",""),"source":"targets/ljs51corpus/keys_eye/"+cid+".json"}


def special(cid):
    d=read(HERE/"keys_eye"/(cid+".json"))
    cards, imgs=[],[]
    if cid=="14v.7":
        with Image.open(IMAGES/"crops/t_key_sheet.png") as sheet:
            for i,(sign,values) in enumerate(d["key"].items()):
                x,y=(i%5)*230,(i//5)*190
                img=sheet.crop((x+4,y+20,x+106,y+169)).convert("RGB")
                bounds=ImageOps.invert(img).convert("L").point(lambda v:255 if v>40 else 0).getbbox()
                imgs.append(img.crop(bounds) if bounds else img)
                cards.append(dict(id=sign, text=values,tile=i,refs=[]))
        state="Undotted-letter classes"
    else:
        trees={f"{t['row']}.{t['index_in_row']}":t for t in d["trees"]}
        for letter,rule in d["key"].items():
            refs=rule["trees"]
            card=dict(id=f"L{rule['left']} R{rule['right']}",values={letter:rule['attested']},
                      refs=[],description=f"{rule['left']} left and {rule['right']} right branches")
            if refs:
                rel,_=reference(trees[refs[0]]["crop"])
                card.update(tile=len(imgs), context=context(rel),locator="Tree "+refs[0])
                with Image.open(IMAGES/rel) as im: imgs.append(im.convert("RGB"))
            else:card["description"]+=" · no intact example recorded"
            card["trees"]=refs
            cards.append(card)
        state="Tree rule"
    sprite(cid,imgs)
    return dict(id=cid,state=state,cards=cards,lines={},source="targets/ljs51corpus/keys_eye/"+cid+".json")


def companions():
    for cid, folder in (("48r.8","ljs51f48r"),("106v.6","qaysarani1350")):
        target=HERE.parent/folder
        key=read(target/"key.json")
        if cid=="106v.6":key=key["key"]
        a,lines,marks=[],{},{}
        for line in (target/"transcription.txt").read_text(encoding="utf-8").splitlines():
            if line.startswith("#") or not line.strip():continue
            raw,*tokens=line.split()
            if cid=="106v.6":
                loc="106v"+str(int(raw.rstrip(":"))+5).zfill(2)
                idx=0
                for token in tokens:
                    clean=token.strip("()[]")
                    if clean=="|":continue
                    idx+=1
                    if token.startswith("("):marks[f"{loc}/{idx}"]="Damaged sign, transcribed from surviving strokes."
                    if raw=="2:" and 9<=idx<=11:
                        marks[f"{loc}/{idx}"]="Damaged group, unread as a word. At least two more letters are lost."
                tokens=[s.strip("()[]") for s in tokens]
            else:loc=raw
            lines[loc]=" ".join(tokens)
            n=0
            for sign in tokens:
                if sign=="|":continue
                n+=1
                val={"21r02":"ح","21r03":"ش"}[loc] if sign=="EK" else key[sign]
                a.append([loc,n,sign,val])
        vals=defaultdict(Counter)
        for loc,pos,sign,val in a:
            vals[sign][val]+=1
        assert set(vals)==set(key)
        cards,imgs=[],[]
        written_rows = set()
        for sign in key:
            refs=[[loc,pos] for loc,pos,s,_ in a if s==sign]
            man=EXAMPLES[cid][sign]
            path=man["file"]
            f=(ROOT/path if path.startswith("docs/") else IMAGES/path)
            with Image.open(f) as source:
                box=man["box"]
                imgs.append(source.crop(box).convert("RGB"))
                if path.startswith("crops/"):
                    name=context(path)
                else:
                    name=f"companion-{man['row']}.webp"
                    if name not in written_rows:
                        written_rows.add(name)
                        if cid=="106v.6":
                            row=int(man["row"][-2:])-5
                            bounds=[(82,188),(183,301),(302,432),(420,527),(525,629),(625,735),(729,833)]
                            top,bottom=bounds[row-1]
                            region=source.crop((0,top,source.width,bottom))
                        else:
                            # First five cipher lines in the keyed f. 21r continuation.
                            y=round((box[1]+box[3])/2)
                            region=source.crop((770,y-77,2220,y+77))
                        region.thumbnail((1450,650),Image.Resampling.LANCZOS)
                        region.convert("RGB").save(OUT/"context"/name,quality=81)
            cards.append(dict(id=sign,values=vals[sign],refs=refs,context=name,
                              tile=len(imgs)-1,manual=True,sample=[man["row"],man["position"]],
                              locator=f"Row {man['row']}, sign {man['position']}"))
        sprite(cid,imgs)
        yield dict(id=cid,state="Companion cipher",cards=cards,marks=marks,source=f"targets/{folder}/key.json",
                   lines={loc:[[s,v,p] for l,p,s,v in a if l==loc] for loc in lines})


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--images",type=Path,required=True)
    IMAGES=parser.parse_args().images.resolve()
    for part in ("records","context","sheets"): (OUT/part).mkdir(parents=True,exist_ok=True)
    EXAMPLES=read(HERE/"visual_examples.json")
    stats=read(HERE/"texts/stats.json")
    states={}
    for line in (HERE/"keys.tsv").read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#"):
            cid,_,_,state=line.split("\t");states[cid]=state
    records=[]
    for cid in stats["keyed_ids"]:
        if cid in ("14v.7","63v.trees"):r=special(cid)
        else:
            state={"letter":"Consistent letter key","partial":"Partly consistent letter key"}[states[cid]]
            r=ordinary(cid,read(HERE/"keys_eye"/(cid+".json")),state)
        records.append(r)
    records.extend(companions())
    records.sort(key=lambda r:order(r["id"]))
    manifest=[]
    for r in records:
        write(OUT/"records"/(r["id"]+".json"),r)
        folios={r["id"].split(".")[0]}
        for loc in r["lines"]:
            address=row_location(r["id"],loc)
            if address:folios.add(address[0])
        if r["id"]=="14v.7":folios.update(("15r","15v","16r","16v"))
        if r["id"]=="63v.trees":folios.add("63v")
        manifest.append(dict(id=r["id"],state=r["state"],folios=sorted(folios,key=page_no),count=len(r["cards"])))
    write(OUT/"index.json",manifest)
    print(len(records),"systems;",sum(len(r["cards"]) for r in records),"key rows;",sum("tile" in c for r in records for c in r["cards"]),"isolated details")
