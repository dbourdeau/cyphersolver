"""List the items under JACAR volume records (fond=<ref>) -> jacar_vol_items.jsonl"""
import sys, json, time, jacar, urllib.parse
out = open("jacar_vol_items.jsonl", "a", encoding="utf8")
for ref in sys.argv[1:]:
    allh=[]
    for p in range(1, 6):
        t = jacar.get(jacar.BASE + "/aj/search?" + urllib.parse.urlencode({"fond": ref, "rows": 200, "page": p, "sf": "reference_a"}))
        total, hs = jacar.parse(t)
        allh += hs
        if not hs or len(allh) >= (total or 0): break
        time.sleep(2)
    print("##", ref, total, len(allh), flush=True)
    for h in allh:
        h["_vol"] = ref
        out.write(json.dumps(h, ensure_ascii=False) + "\n")
        print("  ", h["id"], h.get("規模",""), h["title"][:70], "|", h.get("資料作成年月日","")[:14], "|", h.get("内容","")[:90])
    time.sleep(2)
