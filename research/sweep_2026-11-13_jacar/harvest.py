"""Harvest JACAR search results for a list of cipher-related terms -> hits/<term>.jsonl (one hit per line)."""
import json, os, sys, time
import jacar

TERMS = sys.argv[1:] or ["暗号", "暗号電報", "暗号文", "暗号書", "暗号解読", "解読", "解読不能", "未解読", "判読不能",
                         "密電", "秘密電報", "符牒", "電信暗号", "傍受", "謎", "暗号 不明", "数字電報", "符号電報", "電報 検閲",
                         "偽電", "秘密通信", "暗号翻訳", "暗号訳", "暗号表", "暗号 外国", "欧文暗号", "密書", "隠語"]
os.makedirs("hits", exist_ok=True)
for kw in TERMS:
    fn = "hits/%s.jsonl" % kw.replace(" ", "_")
    if os.path.exists(fn):
        continue
    try:
        total, hs = jacar.harvest(kw, maxpages=80)
    except Exception as e:
        print(kw, "FAILED", e, flush=True)
        continue
    with open(fn, "w", encoding="utf8") as f:
        for h in hs:
            f.write(json.dumps(h, ensure_ascii=False) + "\n")
    print(kw, total, len(hs), flush=True)
