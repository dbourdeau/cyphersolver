"""Harvest JACAR volume-level (簿冊, f_type=2) and fonds-level hits for the cipher terms -> jacar_volumes.jsonl"""
import json, time, jacar
TERMS = ["暗号", "暗号電報", "暗号文", "暗号書", "暗号解読", "解読", "解読不能", "未解読", "判読不能",
         "密電", "秘密電報", "符牒", "電信暗号", "傍受", "謎", "暗号 不明", "数字電報", "符号電報", "電報 検閲",
         "偽電", "秘密通信", "暗号翻訳", "暗号訳", "暗号表", "暗号 外国", "欧文暗号", "密書", "隠語"]
seen = {}
for kw in TERMS:
    try:
        total, hs = jacar.harvest(kw, maxpages=10, f_type=2)
    except Exception as e:
        print(kw, "FAILED", e, flush=True); continue
    print(kw, total, len(hs), flush=True)
    for h in hs:
        seen.setdefault(h["id"], h).setdefault("_t", []).append(kw)
    time.sleep(2)
with open("jacar_volumes.jsonl", "w", encoding="utf8") as f:
    for h in seen.values():
        f.write(json.dumps(h, ensure_ascii=False) + "\n")
print("unique", len(seen))
